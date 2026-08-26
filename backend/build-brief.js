const fs = require("fs");
const path = require("path");
require("dotenv").config({ path: path.join(__dirname, ".env") });
require("dotenv").config({ path: path.join(__dirname, "..", ".env") });
const mysql = require("mysql2/promise");

const OUT = path.join(__dirname, "..", "data", "knowledge", "db-brief.md");
const CATALOG = path.join(__dirname, "..", "data", "catalog", "schema.json");

function small(name, count) {
  if (count <= 80) return true;
  return /type|category|bag|price|status|reason|ward|state|localbody|vehicle_type|how_it_works|waste/i.test(name) && count <= 400;
}
function lines(rows) {
  return rows.map((r) =>
    Object.entries(r).filter(([, v]) => v !== null && v !== "").slice(0, 12).map(([k, v]) => k + "=" + String(v).slice(0, 80)).join("; ")
  ).join("\n");
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
  const [tables] = await db.query("SELECT table_name AS name FROM information_schema.tables WHERE table_schema = DATABASE() AND table_type='BASE TABLE'");
  const [cols] = await db.query("SELECT table_name AS tableName, column_name AS name, data_type AS dataType FROM information_schema.columns WHERE table_schema = DATABASE()");
  const [rels] = await db.query("SELECT table_name AS fromTable, column_name AS fromColumn, referenced_table_name AS toTable, referenced_column_name AS toColumn FROM information_schema.key_column_usage WHERE table_schema = DATABASE() AND referenced_table_name IS NOT NULL");
  const by = {};
  for (const c of cols) { by[c.tableName] = by[c.tableName] || []; by[c.tableName].push({ name: c.name, type: c.dataType }); }

  let md = "# Database brief: " + (dbn[0] && dbn[0].name) + "\nRefreshed: " + new Date().toISOString() + "\nTables: " + tables.length + "\n\n## Table index\n";
  for (const t of tables) md += "- " + t.name + " :: " + (by[t.name] || []).map((c) => c.name).join(", ") + "\n";
  md += "\n## Relationships\n";
  for (const r of rels) md += "- " + r.fromTable + "." + r.fromColumn + " -> " + r.toTable + "." + r.toColumn + "\n";
  md += "\n## Table data\n";

  for (const t of tables) {
    process.stdout.write(t.name + " ");
    let count = 0;
    try { const [c] = await db.query("SELECT COUNT(*) AS c FROM `" + t.name + "`"); count = Number(c[0].c); } catch { md += "\n### " + t.name + "\nunreadable\n"; continue; }
    const colList = (by[t.name] || []).map((c) => c.name);
    md += "\n### " + t.name + " (" + count + " rows)\ncolumns: " + colList.join(", ") + "\n";
    if (!count) { md += "empty\n"; continue; }
    const limit = small(t.name, count) ? Math.min(count, 120) : 8;
    const dateish = colList.find((n) => /date|created|updated/i.test(n));
    const sql = dateish
      ? "SELECT * FROM `" + t.name + "` ORDER BY `" + dateish + "` DESC LIMIT " + limit
      : "SELECT * FROM `" + t.name + "` LIMIT " + limit;
    try {
      const [rows] = await db.query(sql);
      md += lines(rows) + "\n";
      if (count > rows.length) md += "... " + (count - rows.length) + " more rows not copied\n";
    } catch (e) { md += "unreadable: " + e.message + "\n"; }
  }

  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  fs.writeFileSync(OUT, md);
  fs.mkdirSync(path.dirname(CATALOG), { recursive: true });
  fs.writeFileSync(CATALOG, JSON.stringify({
    database: dbn[0] && dbn[0].name,
    refreshedAt: new Date().toISOString(),
    tables: tables.map((t) => ({ name: t.name, columns: by[t.name] || [] })),
    relationships: rels
  }, null, 2));
  await db.end();
  console.log("\nWROTE", OUT, "bytes", md.length);
})().catch((e) => { console.error(e); process.exit(1); });
