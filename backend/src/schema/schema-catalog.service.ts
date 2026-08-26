import { Injectable } from '@nestjs/common';
import * as fs from 'fs';
import * as path from 'path';
import { DbService } from '../db/db.service';

export type ColumnMeta = {
  table: string;
  name: string;
  type: string;
  nullable: boolean;
  key: string;
  comment: string;
};

export type TableMeta = {
  name: string;
  comment: string;
  columns: ColumnMeta[];
};

export type Relationship = {
  fromTable: string;
  fromColumn: string;
  toTable: string;
  toColumn: string;
};

export type SchemaCatalog = {
  database: string;
  refreshedAt: string;
  tables: TableMeta[];
  relationships: Relationship[];
};

@Injectable()
export class SchemaCatalogService {
  private catalog: SchemaCatalog | null = null;
  private catalogPath = path.join(process.cwd(), '..', 'data', 'catalog', 'schema.json');

  constructor(private readonly db: DbService) {}

  async refresh(): Promise<SchemaCatalog> {
    const dbNameRows = await this.db.query<any>('SELECT DATABASE() AS name');
    const database = dbNameRows[0]?.name || process.env.DB_NAME || '';

    const tableRows = await this.db.query<any>(
      `SELECT table_name AS name, IFNULL(table_comment,'') AS tableComment
       FROM information_schema.tables
       WHERE table_schema = DATABASE() AND table_type = 'BASE TABLE'
       ORDER BY table_name`,
    );

    const columnRows = await this.db.query<any>(
      `SELECT table_name AS tableName, column_name AS name, data_type AS dataType,
              is_nullable AS isNullable, IFNULL(column_key,'') AS colKey,
              IFNULL(column_comment,'') AS colComment
       FROM information_schema.columns
       WHERE table_schema = DATABASE()
       ORDER BY table_name, ordinal_position`,
    );

    const relRows = await this.db.query<any>(
      `SELECT table_name AS fromTable, column_name AS fromColumn,
              referenced_table_name AS toTable, referenced_column_name AS toColumn
       FROM information_schema.key_column_usage
       WHERE table_schema = DATABASE() AND referenced_table_name IS NOT NULL`,
    );

    const columnsByTable = new Map<string, ColumnMeta[]>();
    for (const c of columnRows) {
      const list = columnsByTable.get(c.tableName) || [];
      list.push({
        table: c.tableName,
        name: c.name,
        type: c.dataType,
        nullable: c.isNullable === 'YES',
        key: c.colKey,
        comment: c.colComment,
      });
      columnsByTable.set(c.tableName, list);
    }

    const tables: TableMeta[] = tableRows.map((t) => ({
      name: t.name,
      comment: t.tableComment,
      columns: columnsByTable.get(t.name) || [],
    }));

    const relationships: Relationship[] = relRows.map((r) => ({
      fromTable: r.fromTable,
      fromColumn: r.fromColumn,
      toTable: r.toTable,
      toColumn: r.toColumn,
    }));

    this.catalog = {
      database,
      refreshedAt: new Date().toISOString(),
      tables,
      relationships,
    };

    fs.mkdirSync(path.dirname(this.catalogPath), { recursive: true });
    fs.writeFileSync(this.catalogPath, JSON.stringify(this.catalog, null, 2), 'utf8');
    return this.catalog;
  }

  async get(): Promise<SchemaCatalog> {
    if (this.catalog) return this.catalog;
    if (fs.existsSync(this.catalogPath)) {
      this.catalog = JSON.parse(fs.readFileSync(this.catalogPath, 'utf8'));
      return this.catalog!;
    }
    return this.refresh();
  }

  async stats() {
    const c = await this.get();
    return {
      database: c.database,
      refreshedAt: c.refreshedAt,
      tables: c.tables.length,
      columns: c.tables.reduce((n, t) => n + t.columns.length, 0),
      relationships: c.relationships.length,
    };
  }

  async listTables() {
    const c = await this.get();
    return c.tables.map((t) => ({
      name: t.name,
      comment: t.comment,
      columns: t.columns.map((col) => col.name),
    }));
  }

  findTablesByKeyword(question: string, limit = 12): TableMeta[] {
    if (!this.catalog) return [];
    const q = question.toLowerCase();
    const tokens = q.split(/[^a-z0-9_]+/).filter((t) => t.length > 2);
    const scored = this.catalog.tables.map((t) => {
      const hay = (
        t.name +
        ' ' +
        t.comment +
        ' ' +
        t.columns.map((c) => c.name + ' ' + c.comment).join(' ')
      ).toLowerCase();
      let score = 0;
      for (const tok of tokens) if (hay.includes(tok)) score += tok.length;
      if (q.includes(t.name.toLowerCase())) score += 50;
      return { t, score };
    });
    return scored
      .filter((x) => x.score > 0)
      .sort((a, b) => b.score - a.score)
      .slice(0, limit)
      .map((x) => x.t);
  }

  tableNames(): Set<string> {
    return new Set((this.catalog?.tables || []).map((t) => t.name.toLowerCase()));
  }
}
