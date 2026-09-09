import { mkdirSync, readdirSync, readFileSync, writeFileSync, statSync, copyFileSync } from "fs";
import { dirname, join, relative } from "path";
import { fileURLToPath } from "url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const src = join(root, "data");
const dest = join(root, "prototype", "dati");

const walk = (dir) =>
  readdirSync(dir).flatMap((name) => {
    const p = join(dir, name);
    return statSync(p).isDirectory() ? walk(p) : [p];
  });

const flatten = (value, prefix = "") => {
  if (Array.isArray(value)) return value.flatMap((item, i) => flatten(item, prefix ? `${prefix}.${i}` : String(i)));
  if (value && typeof value === "object") {
    return Object.entries(value).flatMap(([k, v]) => flatten(v, prefix ? `${prefix}.${k}` : k));
  }
  return [{ key: prefix, value }];
};

const rowsFromJson = (json) => {
  const table = Array.isArray(json.dati) ? json.dati
    : Array.isArray(json.comuni) ? json.comuni
    : Array.isArray(json.record) ? json.record
    : Array.isArray(json) ? json
    : null;
  if (table && table.every((row) => row && typeof row === "object" && !Array.isArray(row))) return table;
  return [json];
};

const toCsv = (rows) => {
  const keys = [...new Set(rows.flatMap((row) => Object.keys(row)))];
  const esc = (v) => {
    if (v == null) return "";
    const s = typeof v === "object" ? JSON.stringify(v) : String(v);
    return `"${s.replace(/"/g, '""')}"`;
  };
  return [keys.map(esc).join(";"), ...rows.map((row) => keys.map((k) => esc(row[k])).join(";"))].join("\n");
};

mkdirSync(dest, { recursive: true });
const files = walk(src).filter((p) => p.endsWith(".json"));
const catalog = [];

for (const file of files) {
  const rel = relative(src, file).replace(/\\/g, "/");
  const outJson = join(dest, rel);
  mkdirSync(dirname(outJson), { recursive: true });
  copyFileSync(file, outJson);
  const json = JSON.parse(readFileSync(file, "utf8"));
  const rows = rowsFromJson(json);
  const outCsv = outJson.replace(/\.json$/, ".csv");
  writeFileSync(outCsv, "\ufeff" + toCsv(rows));
  catalog.push({
    id: rel.replace(/\.json$/, ""),
    titolo: json.titolo || rel,
    json: `dati/${rel}`,
    csv: `dati/${rel.replace(/\.json$/, ".csv")}`,
    fonte: json.fonte || null,
    note: Array.isArray(json.note) ? json.note[0] : null,
    area: rel.startsWith("alta-gallura") ? "Focus Gallura" : rel.startsWith("sughero-sardegna") ? "Sughero Sardegna" : "Trasversale",
  });
}

writeFileSync(join(dest, "catalogo.json"), JSON.stringify({
  titolo: "Catalogo dei dataset aperti — Sughero Sardegna",
  cup: "CUP E77G24000450002",
  soggetto: "Centro Studi R.I.S.S.T.E. APS",
  n: catalog.length,
  note: "I dati del sito derivano dal database validato. I file identificativi delle imprese non sono pubblicati.",
  dataset: catalog,
}, null, 2));

console.log(`Scritti ${catalog.length} dataset in prototype/dati`);
