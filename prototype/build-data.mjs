// Consolida i dataset reali di data/alta-gallura in assets/data.js (globale window.RISSTE_DATA)
// Uso: node build-data.mjs   (dalla cartella prototype/)
import { readFileSync, writeFileSync } from "node:fs"

const D = "../data/alta-gallura"
const load = (f) => JSON.parse(readFileSync(`${D}/${f}`, "utf8"))

const schede = load("schede-comuni.json").dati
const pop = load("popolazione-storica.json").dati
const saldi = load("saldi-demografici.json").dati
const eta = load("struttura-eta.json").dati
const imprese = load("imprese.json").dati
const usoSuolo = load("uso-suolo-comuni.json")
const kpi = load("kpi-sintesi.json").dati
const scenari = load("scenari-2035.json")

const bySlug = (arr) => Object.fromEntries(arr.map((r) => [r.slug, r]))
const popBy = bySlug(pop.filter((r) => !r.slug.startsWith("fascia") && r.slug !== "totale-alta-gallura"))
const saldiBy = bySlug(saldi.filter((r) => r.livello === "comune"))
const eta25 = bySlug(eta.filter((r) => r.anno === 2025))
const eta02 = bySlug(eta.filter((r) => r.anno === 2002))
const impBy = bySlug(imprese.filter((r) => r.livello === "comune"))

const usoBy = {}
for (const r of usoSuolo.dati) {
  ;(usoBy[r.slug] ??= []).push({
    classe: r.classe_uso_suolo, ha: r.superficie_ha, pct: r.incidenza_pct, rango: r.rango, origine: r.origine,
  })
}
for (const s of Object.keys(usoBy)) usoBy[s].sort((a, b) => (a.rango ?? 99) - (b.rango ?? 99))
const sughereteBy = bySlug(usoSuolo.sugherete_per_comune)

const comuni = schede.map((s) => {
  const slug = s.slug
  const p = popBy[slug] ?? {}
  const e = eta25[slug] ?? {}
  const e0 = eta02[slug] ?? {}
  const im = impBy[slug] ?? {}
  const sa = saldiBy[slug] ?? {}
  return {
    slug, comune: s.comune, fascia: s.fascia,
    funzione: s.funzione_territoriale,
    ruolo: s.ruolo_paesaggistico,
    inquadramento: s.inquadramento,
    implicazioni_sughero: s.implicazioni_bosco_sughero,
    implicazioni_suinicola: s.implicazioni_suinicola,
    criticita: s.criticita, opportunita: s.opportunita,
    valutazione: s.valutazione_preliminare,
    identita: s.elementi_identitari,
    sintesi: s.sintesi_comparativa,
    abitanti_2001: p.abitanti_2001, abitanti_2011: p.abitanti_2011,
    abitanti_2023: p.abitanti_2023, abitanti_2025: p.abitanti_2025,
    var_pct_2001_2023: p.var_pct_2001_2023,
    over65_pct: e.quota_65_piu_pct ?? null, under15_pct: e.quota_0_14_pct ?? null,
    indice_vecchiaia: e.indice_vecchiaia ?? null, eta_media: e.eta_media ?? null,
    indice_vecchiaia_2002: e0.indice_vecchiaia ?? null,
    imprese_2025: im.imprese_2025 ?? null, imprese_var_pct: im.var_pct_2021_2025 ?? null,
    saldo_naturale: sa.saldo_naturale_2002_2023 ?? null, saldo_migratorio: sa.saldo_migratorio_2002_2023 ?? null,
    sugherete_ha: sughereteBy[slug]?.superficie_ha ?? s.sugherete_ha ?? null,
    uso_suolo: usoBy[slug] ?? [],
  }
})

const fasce = pop.filter((r) => r.slug.startsWith("fascia") || r.slug === "totale-alta-gallura")
  .map((r) => ({ slug: r.slug, comune: r.comune, fascia: r.fascia, a2001: r.abitanti_2001, a2025: r.abitanti_2025, var_pct_2001_2025: r.var_pct_2001_2025 ?? null }))
const saldiFasce = saldi.filter((r) => r.livello !== "comune")
  .map((r) => ({ slug: r.slug, comune: r.comune, fascia: r.fascia, naturale: r.saldo_naturale_2002_2023, migratorio: r.saldo_migratorio_2002_2023 }))

const out = {
  comuni, fasce, saldiFasce,
  kpi: Object.fromEntries(kpi.map((k) => [k.chiave, { valore: k.valore, unita: k.unita, etichetta: k.etichetta, contesto: k.contesto, pagina: k.pagina_pdf }])),
  scenari: scenari.dati ?? scenari.scenari ?? scenari,
}
writeFileSync("assets/data.js", "window.RISSTE_DATA = " + JSON.stringify(out, null, 1) + ";\n")
console.log("comuni:", comuni.length, "| fasce:", fasce.length, "| saldiFasce:", saldiFasce.length)
console.log("scenari keys:", Object.keys(scenari))
