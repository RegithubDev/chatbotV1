const fs = require("fs");
const path = require("path");
require("dotenv").config({ path: path.join(__dirname, ".env") });
require("dotenv").config({ path: path.join(__dirname, "..", ".env") });
const mysql = require("mysql2/promise");
const CATALOG = path.join(__dirname, "..", "data", "catalog", "schema.json");
const MASTERS = path.join(__dirname, "..", "data", "knowledge", "masters.md");

function pretty(n) {
  return String(n).replace(/^backend_/, "").replace(/^auth_/, "").replace(/_/g, " ");
}

(async () => {
  const db = await mysql.createConnection({
    host: process.env.DB_HOST || "localhost",
    port: Number(process.env.DB_PORT || 3306),
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
  });
  const [dbn] = await db.query("SELECT DATABASE() AS name");
  const [tables] = await db.query("SELECT table_name AS name FROM information_schema.tables WHERE table_schema=DATABASE() AND table_type='BASE TABLE'");
  const [cols] = await db.query("SELECT table_name AS tableName, column_name AS name, column_key AS columnKey, data_type AS dataType FROM information_schema.columns WHERE table_schema=DATABASE()");
  const [rels] = await db.query("SELECT table_name AS fromTable, column_name AS fromColumn, referenced_table_name AS toTable, referenced_column_name AS toColumn FROM information_schema.key_column_usage WHERE table_schema=DATABASE() AND referenced_table_name IS NOT NULL");
  const by = {}, pk = {};
  for (const c of cols) {
    by[c.tableName] = by[c.tableName] || [];
    by[c.tableName].push({ name: c.name, type: c.dataType, key: c.columnKey });
    if (c.columnKey === "PRI") { pk[c.tableName] = pk[c.tableName] || []; pk[c.tableName].push(c.name); }
  }
  const inbound = {};
  for (const r of rels) inbound[r.toTable] = (inbound[r.toTable] || 0) + 1;

  const catalog = {
    database: dbn[0] && dbn[0].name,
    refreshedAt: new Date().toISOString(),
    tables: tables.map((t) => ({
      name: t.name,
      pretty: pretty(t.name),
      pk: pk[t.name] || [],
      inbound: inbound[t.name] || 0,
      columns: by[t.name] || [],
      master: (inbound[t.name] || 0) >= 3 || /^(backend_)?(customer|customers|order|orders|product|products|user|users)$/i.test(t.name)
    })),
    relationships: rels
  };
  fs.mkdirSync(path.dirname(CATALOG), { recursive: true });
  fs.writeFileSync(CATALOG, JSON.stringify(catalog, null, 2));

  const masters = catalog.tables.filter((t) => t.master).sort((a, b) => b.inbound - a.inbound);
  let md = "# Masters and keys\nDatabase: " + catalog.database + "\nTables: " + catalog.tables.length + "\n\n";
  md += "## Master tables (most referenced)\n";
  for (const t of masters.slice(0, 40)) {
    md += "- " + t.pretty + " | pk: " + (t.pk.join(",") || "id") + " | referenced by " + t.inbound + " tables\n";
  }
  md += "\n## Relationships\n";
  for (const r of rels) md += "- " + pretty(r.fromTable) + "." + r.fromColumn + " -> " + pretty(r.toTable) + "." + r.toColumn + "\n";
  fs.mkdirSync(path.dirname(MASTERS), { recursive: true });
  fs.writeFileSync(MASTERS, md);
  await db.end();
  console.log("SYNC_OK tables=" + catalog.tables.length + " masters=" + masters.length);
})().catch((e) => { console.error(e); process.exit(1); });
