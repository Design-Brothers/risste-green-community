// Consolida i dataset per le pagine Strategia, Sughereta e Innovazione.
// Uso: node build-data2.mjs   (dalla cartella prototype/)
import { readFileSync, writeFileSync } from "node:fs";

const D = "../data";
const load = (f) => JSON.parse(readFileSync(`${D}/${f}`, "utf8"));

/* ---- Sughereta + Innovazione ---- */
const comuni = load("sughero-sardegna/comuni-sughereta.json").dati.map((c) => ({
  rank: c.rank, comune: c.comune, slug: c.slug, sugherete_ha: c.sugherete_ha,
  peso_pct: c.peso_pct_sughereta_sardegna, ivp: c.ivp, classe_ivp: c.classe_ivp,
  classe_incendio: c.classe_incendio, quota_medioalto_alto_pct: c.quota_medioalto_alto_pct,
  classe_icr: c.classe_icr, n_complessi: c.n_complessi, quota_complesso_maggiore_pct: c.quota_complesso_maggiore_pct,
  densita_frammentazione: c.densita_frammentazione,
  profilo_ivp_x_incendio: c.profilo_ivp_x_incendio, profilo_integrato: c.profilo_integrato,
  indicazioni_operative: c.indicazioni_operative, lettura_icr: c.lettura_icr,
  distribuzione_pedologica: c.distribuzione_pedologica, distribuzione_incendio: c.distribuzione_incendio,
}));
const bib = load("sughero-sardegna/bibliografia-scientifica.json").dati.map((b) => ({
  id: b.id, anno: b.anno, paese: b.paese, settore: b.settore_applicativo, materiale: b.materiale,
  trl: b.trl_stimato, trl_min: b.trl_min, trl_max: b.trl_max, priorita: b.priorita,
  stelle: b.potenziale_sardegna_stelle, riferimento: b.riferimento,
}));
writeFileSync("assets/data-sughero.js", "window.RISSTE_SUGHERO = " + JSON.stringify({
  comuni,
  sintesi: load("sughero-sardegna/sintesi-regionale.json").dati,
  indici: load("sughero-sardegna/indici-definizioni.json").dati,
  contesto: load("sughero-sardegna/contesto-sughero-sardegna.json"),
  bibliografia: bib,
  scouting: load("sughero-sardegna/technology-scouting.json").dati,
  direttrici: load("sughero-sardegna/direttrici-innovazione.json").dati,
  certificazioni: load("sughero-sardegna/strumenti-certificazione.json").dati,
  framework: load("sughero-sardegna/framework-sughera.json").dati,
  conclusioni: load("sughero-sardegna/conclusioni.json").dati,
}, null, 1) + ";\n");

/* ---- Strategia ---- */
writeFileSync("assets/data-strategia.js", "window.RISSTE_STRATEGIA = " + JSON.stringify({
  roadmap: load("alta-gallura/roadmap.json").dati,
  esg: load("alta-gallura/indicatori-esg.json").dati,
  filiere: load("alta-gallura/filiere.json").dati,
  servizi: load("alta-gallura/servizi-ecosistemici-carbon-farming.json").dati,
  formazione: load("alta-gallura/formazione-e-professioni.json").dati,
  frameworkGreen: load("alta-gallura/framework-green-community.json").dati,
  obiettivi: load("alta-gallura/obiettivi-studio.json").dati,
}, null, 1) + ";\n");

// diagnostica strutture
const rm = load("alta-gallura/roadmap.json").dati;
console.log("roadmap tipi:", [...new Set(rm.map((r) => r.tipo))].join(","), "| record:", rm.length);
console.log("azione sample:", JSON.stringify(rm.find((r) => r.tipo !== "fase")).slice(0, 320));
const sc = load("sughero-sardegna/technology-scouting.json").dati;
console.log("scouting:", JSON.stringify(sc[0]).slice(0, 300));
const cert = load("sughero-sardegna/strumenti-certificazione.json").dati;
console.log("cert:", JSON.stringify(cert[0]).slice(0, 260));
const fw = load("sughero-sardegna/framework-sughera.json").dati;
console.log("fw:", JSON.stringify(fw[0]).slice(0, 260));
const fil = load("alta-gallura/filiere.json").dati;
console.log("filiere:", JSON.stringify(fil[0]).slice(0, 260));
console.log("sintesi row0:", JSON.stringify(load("sughero-sardegna/sintesi-regionale.json").dati[0]).slice(0, 260));
console.log("indici row0:", JSON.stringify(load("sughero-sardegna/indici-definizioni.json").dati[0]).slice(0, 220));
console.log("direttrici row0:", JSON.stringify(load("sughero-sardegna/direttrici-innovazione.json").dati[0]).slice(0, 220));
console.log("conclusioni row0:", JSON.stringify(load("sughero-sardegna/conclusioni.json").dati[0]).slice(0, 160));
console.log("dimensioni:", JSON.stringify({ sughero: null, strategia: null }));
