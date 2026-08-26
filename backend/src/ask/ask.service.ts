import { BadRequestException, Injectable } from '@nestjs/common';
import { DbService } from '../db/db.service';
import { SchemaCatalogService, TableMeta } from '../schema/schema-catalog.service';
import OpenAI from 'openai';

@Injectable()
export class AskService {
  constructor(
    private readonly db: DbService,
    private readonly catalog: SchemaCatalogService,
  ) {}

  async ask(question: string) {
    const started = Date.now();
    if (!question.trim()) throw new BadRequestException('question is required');

    const schema = await this.catalog.get();

    // Catalog questions — no SQL invention
    if (/how many tables|table count|number of tables/i.test(question)) {
      return {
        answer: `Database "${schema.database}" has ${schema.tables.length} real tables and ${schema.relationships.length} relationships.`,
        sql: null,
        tablesUsed: [],
        data: {
          database: schema.database,
          tables: schema.tables.length,
          relationships: schema.relationships.length,
        },
        elapsedMs: Date.now() - started,
      };
    }

    const slice = this.catalog.findTablesByKeyword(question, 10);
    if (!slice.length) {
      return {
        answer: `No matching tables or columns were found in the real schema of "${schema.database}". I will not invent tables.`,
        sql: null,
        tablesUsed: [],
        data: [],
        elapsedMs: Date.now() - started,
      };
    }

    const generated = await this.generateSql(question, slice);
    if (!generated.sql) {
      return {
        answer: generated.reason,
        sql: null,
        tablesUsed: slice.map((t) => t.name),
        data: slice.map((t) => ({ table: t.name, columns: t.columns.map((c) => c.name) })),
        elapsedMs: Date.now() - started,
      };
    }

    const safe = this.validateSql(generated.sql, this.catalog.tableNames());
    if (!safe.ok) {
      return {
        answer: `Generated SQL was rejected: ${safe.reason}`,
        sql: generated.sql,
        tablesUsed: slice.map((t) => t.name),
        data: [],
        elapsedMs: Date.now() - started,
      };
    }

    const rows = await this.db.query(safe.sql);
    const preview = rows.slice(0, Number(process.env.DB_MAX_ROWS || 200));
    return {
      answer: this.explain(question, preview),
      sql: safe.sql,
      tablesUsed: safe.tables,
      data: preview,
      rowCount: preview.length,
      elapsedMs: Date.now() - started,
    };
  }

  private async generateSql(question: string, slice: TableMeta[]): Promise<{ sql: string | null; reason: string }> {
    const key = process.env.OPENAI_API_KEY;
    if (!key || key.includes('REPLACE')) {
      const first = slice[0];
      const cols = first.columns.slice(0, 8).map((c) => `\`${c.name}\``).join(', ');
      return {
        sql: `SELECT ${cols} FROM \`${first.name}\` LIMIT 10`,
        reason: 'No LLM key; used top matching real table only.',
      };
    }

    const schemaText = slice
      .map((t) => {
        const cols = t.columns.map((c) => `  - ${c.name} ${c.type}`).join('\n');
        const rel = '';
        return `TABLE ${t.name}\n${cols}${rel}`;
      })
      .join('\n\n');

    const client = new OpenAI({ apiKey: key });
    const model = process.env.OPENAI_MODEL || 'gpt-4.1';
    const resp = await client.chat.completions.create({
      model,
      temperature: 0,
      messages: [
        {
          role: 'system',
          content:
            'You generate MySQL SELECT queries. Use ONLY tables and columns listed. Never invent names. Return JSON only: {"sql":"SELECT ... LIMIT 50"} or {"sql":null,"reason":"..."}. One SELECT or WITH. No writes.',
        },
        {
          role: 'user',
          content: `SCHEMA:\n${schemaText}\n\nQUESTION:\n${question}`,
        },
      ],
    });

    const raw = resp.choices[0]?.message?.content || '{}';
    const jsonText = raw.replace(/```json|```/g, '').trim();
    try {
      const parsed = JSON.parse(jsonText);
      return { sql: parsed.sql || null, reason: parsed.reason || 'LLM did not produce SQL' };
    } catch {
      return { sql: null, reason: 'LLM returned invalid JSON' };
    }
  }

  private validateSql(sql: string, knownTables: Set<string>) {
    let s = sql.trim().replace(/;+\s*$/, '');
    s = s.replace(/\/\*[\s\S]*?\*\//g, '').replace(/--.*$/gm, '');
    if (s.includes(';')) return { ok: false, reason: 'multiple statements', sql: s, tables: [] as string[] };
    if (!/^(select|with)\b/i.test(s)) return { ok: false, reason: 'not a SELECT', sql: s, tables: [] };
    if (/\b(insert|update|delete|drop|alter|truncate|create|grant|revoke|replace|load_file|outfile|dumpfile|into\s+outfile)\b/i.test(s)) {
      return { ok: false, reason: 'write/dangerous keyword', sql: s, tables: [] };
    }
    const tables = Array.from(s.matchAll(/\b(?:from|join)\s+`?([a-zA-Z0-9_]+)`?/gi)).map((m) => m[1]);
    for (const t of tables) {
      if (!knownTables.has(t.toLowerCase())) {
        return { ok: false, reason: `unknown table ${t}`, sql: s, tables };
      }
    }
    if (!/\blimit\s+\d+/i.test(s)) s += ' LIMIT 50';
    return { ok: true, reason: 'ok', sql: s, tables };
  }

  private explain(question: string, rows: any[]) {
    if (!rows.length) return `Query ran against the real database. 0 rows for: "${question}"`;
    return `Query ran against the real database and returned ${rows.length} row(s) for: "${question}"`;
  }
}
