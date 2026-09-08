# Componenti del mini-sito – specifica e codice di esempio

Riferimento per chi sviluppa. Stack: React 19 + TypeScript + Vite + Tailwind 4, Recharts per i grafici, `motion` per le animazioni, `d3-geo` + `topojson-client` per la mappa. Ogni componente: cosa fa, dove si usa, props, esempio di implementazione, note di accessibilità. Il codice è indicativo ma completo: si può incollare e adattare.

Convenzioni: cartella `src/components/<Nome>/<Nome>.tsx`; classi Tailwind con token CSS del brief (`--ice`, `--green`, `--cork`…); numeri sempre via `formatInt/formatPct` (§14); ogni blocco dati termina con `<SourceNote>`.

---

## 1. `HeroOrbs` – sfere fluttuanti della landing

**Cosa fa.** Sfondo dell'hero: 4-6 orbi sfumati e sgranati che derivano lentamente, con parallasse allo scroll e reazione minima al puntatore. Solo `transform`/`opacity`, disattivato con `prefers-reduced-motion`.
**Dove.** Landing (piena altezza); versione ridotta (1 orbo) negli hero di sezione.
**Props.** `variant: "landing" | "alta-gallura" | "sughero"` (palette), `intensity?: number` (0-1, default 1).

```tsx
// src/components/HeroOrbs/HeroOrbs.tsx
import { motion, useReducedMotion, useScroll, useTransform } from "motion/react"
import { useEffect, useState } from "react"

type Orb = { x: number; y: number; size: number; colors: [string, string, string]; drift: number; delay: number }

const PALETTES: Record<string, Orb[]> = {
  landing: [
    { x: 62, y: 18, size: 520, colors: ["#7CFF3F", "#3FE9FF", "transparent"], drift: 26, delay: 0 },
    { x: 18, y: 48, size: 460, colors: ["#4E9A3F", "#7CFF3F", "transparent"], drift: 22, delay: 4 },
    { x: 74, y: 60, size: 420, colors: ["#3FE9FF", "#2F6FB0", "transparent"], drift: 30, delay: 8 },
    { x: 40, y: 82, size: 380, colors: ["#7CFF3F", "#4E9A3F", "transparent"], drift: 18, delay: 2 },
    { x: 50, y: 42, size: 220, colors: ["#FFFFFF", "#DFFCF6", "transparent"], drift: 12, delay: 6 }, // cuore bianco
  ],
  "alta-gallura": [{ x: 70, y: 40, size: 520, colors: ["#4E9A3F", "#3FE9FF", "transparent"], drift: 20, delay: 0 }],
  sughero: [{ x: 70, y: 40, size: 520, colors: ["#E8C28E", "#C2603A", "transparent"], drift: 20, delay: 0 }],
}

export function HeroOrbs({ variant = "landing", intensity = 1 }: { variant?: keyof typeof PALETTES; intensity?: number }) {
  const reduce = useReducedMotion()
  const { scrollY } = useScroll()
  const parallax = useTransform(scrollY, [0, 800], [0, -120]) // lo sfondo sale più lento del testo
  const [pointer, setPointer] = useState({ x: 0, y: 0 })

  useEffect(() => {
    if (reduce) return
    const onMove = (e: PointerEvent) => setPointer({ x: (e.clientX / innerWidth - 0.5) * 2, y: (e.clientY / innerHeight - 0.5) * 2 })
    addEventListener("pointermove", onMove, { passive: true })
    return () => removeEventListener("pointermove", onMove)
  }, [reduce])

  return (
    <div aria-hidden className="pointer-events-none absolute inset-0 overflow-hidden bg-[var(--ice)]">
      <motion.div style={{ y: reduce ? 0 : parallax }} className="absolute inset-0">
        {PALETTES[variant].map((o, i) => (
          <motion.div
            key={i}
            className="absolute rounded-full will-change-transform"
            style={{
              left: `${o.x}%`, top: `${o.y}%`, width: o.size, height: o.size,
              marginLeft: -o.size / 2, marginTop: -o.size / 2,
              background: `radial-gradient(circle at 40% 40%, ${o.colors[0]} 0%, ${o.colors[1]} 45%, ${o.colors[2]} 72%)`,
              filter: "blur(48px)", opacity: 0.85 * intensity,
              x: reduce ? 0 : pointer.x * 12 * (i % 2 ? -1 : 1), // reazione al puntatore 2-4 %
            }}
            animate={reduce ? undefined : { x: [0, o.drift, -o.drift * 0.6, 0], y: [0, -o.drift * 0.8, o.drift * 0.5, 0] }}
            transition={{ duration: 18 + i * 3, delay: o.delay, repeat: Infinity, ease: "easeInOut" }}
          />
        ))}
      </motion.div>
      {/* grana: un solo SVG fisso a bassa opacità */}
      <svg className="absolute inset-0 h-full w-full opacity-[0.10] mix-blend-multiply">
        <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch" /></filter>
        <rect width="100%" height="100%" filter="url(#grain)" />
      </svg>
    </div>
  )
}
```

**Note.** Gli orbi stanno in un contenitore `relative` con il testo dell'hero sopra (`relative z-10`). Massimo 6 orbi; `blur` su elementi ≤ 600 px per non pesare sulla GPU mobile. Test: 60 fps su un telefono di fascia media con Chrome DevTools "CPU 4× slowdown".

---

## 2. `GhostWord` – parola-fantasma in outline

**Cosa fa.** Testo enorme in solo contorno dietro l'hero (es. "ALTA GALLURA"), tagliato dai bordi.
```tsx
export function GhostWord({ text }: { text: string }) {
  return (
    <span aria-hidden className="pointer-events-none absolute -left-8 top-1/2 -translate-y-1/2 select-none whitespace-nowrap text-[22vw] font-light leading-none tracking-tight text-transparent"
      style={{ WebkitTextStroke: "1px rgba(19,32,25,0.18)" }}>
      {text}
    </span>
  )
}
```

## 3. `MicroLabel` – micro-etichette ai bordi

```tsx
export function MicroLabel({ children, side = "left" }: { children: string; side?: "left" | "right" }) {
  return (
    <span className={`inline-flex items-center gap-2 text-[11px] uppercase tracking-[0.08em] text-[var(--ink-muted)] ${side === "right" ? "flex-row-reverse" : ""}`}>
      {children}<span className="block h-px w-6 bg-current" />
    </span>
  )
}
// uso: <MicroLabel>RISSTE</MicroLabel> in alto a sinistra, <MicroLabel side="right">UCAG 193</MicroLabel> in basso a destra
```

---

## 4. `DecorticaRings` – anelli concentrici (motivo grafico e loader)

**Cosa fa.** 12 anelli concentrici sfumati (il turno di decortica di dodici anni), sgranati; ruotano piano quando `spin`. Colori per sezione.
```tsx
export function DecorticaRings({ size = 480, tone = "green", spin = false }: { size?: number; tone?: "green" | "cork"; spin?: boolean }) {
  const [a, b] = tone === "green" ? ["#4E9A3F", "#3FE9FF"] : ["#C2603A", "#E8C28E"]
  return (
    <svg width={size} height={size} viewBox="0 0 100 100" aria-hidden className={spin ? "animate-[spin_24s_linear_infinite] motion-reduce:animate-none" : ""}>
      <defs><radialGradient id={`g-${tone}`}><stop offset="0%" stopColor={b} /><stop offset="100%" stopColor={a} /></radialGradient></defs>
      {Array.from({ length: 12 }, (_, i) => (
        <circle key={i} cx="50" cy="50" r={4 + i * 3.8} fill="none" stroke={`url(#g-${tone})`} strokeWidth={i % 3 === 0 ? 2.2 : 1.1} opacity={0.25 + (i / 12) * 0.6} />
      ))}
    </svg>
  )
}
```

---

## 5. `MessageSlide` – i cinque messaggi della landing

**Cosa fa.** Una schermata per messaggio: numero d'ordine, frase-titolo, due frasi, KPI con conteggio, fonte; l'orbo di sfondo cambia colore. Contenuto dai blocchi `{type=message}` di `pagine/00-landing.md`.
**Props.** `index`, `title`, `body`, `kpi: { value, unit, label }`, `tone`, `source`.
```tsx
import { motion, useInView } from "motion/react"
import { useRef } from "react"
import { CountUp } from "../CountUp/CountUp"

export function MessageSlide({ index, title, body, kpi, source, tone }: MessageProps) {
  const ref = useRef<HTMLElement>(null)
  const inView = useInView(ref, { amount: 0.6, once: true })
  return (
    <section ref={ref} className="relative grid min-h-[90vh] items-center gap-10 px-6 md:grid-cols-2" data-tone={tone}>
      <div className="relative z-10 max-w-xl">
        <span className="text-[12px] uppercase tracking-[0.08em] text-[var(--ink-muted)]">0{index}</span>
        <motion.h2 initial={{ opacity: 0, y: 24 }} animate={inView ? { opacity: 1, y: 0 } : {}} transition={{ duration: 0.6 }}
          className="mt-3 text-4xl font-light leading-[1.05] md:text-6xl">{title}</motion.h2>
        <p className="mt-6 text-lg text-[var(--ink-muted)]">{body}</p>
        <p className="mt-6 text-[12px] text-[var(--ink-muted)]">Fonte: {source}</p>
      </div>
      <div className="relative z-10">
        <p className="text-6xl font-medium tabular-nums md:text-8xl">{inView ? <CountUp to={kpi.value} /> : 0}<span className="ml-2 text-3xl">{kpi.unit}</span></p>
        <p className="mt-2 text-[var(--ink-muted)]">{kpi.label}</p>
      </div>
    </section>
  )
}
```
`CountUp`: interpola in 900 ms con `requestAnimationFrame`, salta al valore finale con `prefers-reduced-motion`, formatta con `formatInt`.

---

## 6. `KpiRow` – numeri con etichetta e fonte

**Dove.** Landing e apertura di ogni sezione. 3-4 card; su mobile 2 colonne.
**Props.** `items: { value: string; label: string; hint?: string; source: string; tone?: "default" | "positive" | "negative" }[]`.
```tsx
export function KpiRow({ items }: { items: KpiItem[] }) {
  return (
    <dl className="grid grid-cols-2 gap-4 lg:grid-cols-4">
      {items.map((k) => (
        <div key={k.label} className="rounded-3xl border border-[var(--line)] bg-white p-6">
          <dd className={`text-4xl font-medium tabular-nums md:text-5xl ${k.tone === "negative" ? "text-[var(--fire)]" : ""}`}>{k.value}</dd>
          <dt className="mt-2 text-sm text-[var(--ink)]">{k.label}</dt>
          {k.hint && <p className="mt-1 text-xs text-[var(--ink-muted)]">{k.hint}</p>}
          <span className="mt-3 inline-block rounded-full bg-[var(--ice)] px-2.5 py-1 text-[11px] text-[var(--ink-muted)]">Fonte: {k.source}</span>
        </div>
      ))}
    </dl>
  )
}
```
La pillola "Fonte" riprende il riferimento visivo "From User Interviews". I dati arrivano da `kpi-sintesi.json` (campi `valore`, `unita`, `etichetta`, `contesto`, `pagina`).

---

## 7. `StatArc` – semicerchio sfumato con tacche radiali

**Cosa fa.** Il blocco statistiche del riferimento: percentuali grandi a sinistra, linee sottili verso un semicerchio con tacche e alone sfumato, card a destra. Usato per i 3-4 KPI "problema" (es. saldo naturale, indice di vecchiaia, quota over 65).
```tsx
export function StatArc({ ticks = 72, tone = "green" }: { ticks?: number; tone?: "green" | "cork" }) {
  const color = tone === "green" ? "var(--green)" : "var(--cork)"
  return (
    <svg viewBox="0 0 200 400" className="h-[400px] w-[200px]" aria-hidden>
      <defs><radialGradient id="halo"><stop offset="0%" stopColor={color} stopOpacity="0.55" /><stop offset="100%" stopColor={color} stopOpacity="0" /></radialGradient></defs>
      <circle cx="200" cy="200" r="190" fill="url(#halo)" style={{ filter: "blur(18px)" }} />
      {Array.from({ length: ticks }, (_, i) => {
        const a = Math.PI / 2 + (i / (ticks - 1)) * Math.PI // da alto a basso, lato sinistro
        const [x1, y1] = [200 + Math.cos(a) * 120, 200 + Math.sin(a) * 120]
        const [x2, y2] = [200 + Math.cos(a) * 160, 200 + Math.sin(a) * 160]
        return <line key={i} x1={x1} y1={y1} x2={x2} y2={y2} stroke={color} strokeWidth="2" opacity={0.7} />
      })}
      <path d="M200 20 A180 180 0 0 0 200 380" fill="none" stroke={color} strokeWidth="0.75" strokeDasharray="2 4" />
    </svg>
  )
}
```
Layout: griglia 3 colonne (`[1fr_200px_1fr]`), a sinistra `KpiRow` in colonna con linee `border-t` che puntano all'arco, a destra card arrotondate 24 px con icona in cerchio pieno.

---

## 8. `FigureLightbox` – infografiche originali

**Cosa fa.** Figura a piena larghezza, didascalia, fonte, pulsante "Ingrandisci" che apre `<dialog>` nativo con zoom e "Scarica".
**Props.** `src`, `alt`, `caption`, `source`, `note?` (es. "Elaborazione grafica dello studio; i valori di riferimento sono quelli delle schede comunali").
```tsx
import { useRef } from "react"
export function FigureLightbox({ src, alt, caption, source, note }: FigureProps) {
  const dlg = useRef<HTMLDialogElement>(null)
  return (
    <figure className="my-12">
      <button onClick={() => dlg.current?.showModal()} className="group block w-full overflow-hidden rounded-3xl border border-[var(--line)] bg-white" aria-label={`Ingrandisci: ${caption}`}>
        <img src={src} alt={alt} loading="lazy" className="w-full transition group-hover:scale-[1.01]" />
      </button>
      <figcaption className="mt-3 text-sm text-[var(--ink-muted)]">{caption} <span className="ml-2">Fonte: {source}</span>{note && <em className="block mt-1">{note}</em>}</figcaption>
      <dialog ref={dlg} className="max-w-[96vw] rounded-2xl p-0 backdrop:bg-black/70" onClick={(e) => e.target === dlg.current && dlg.current.close()}>
        <img src={src} alt={alt} className="max-h-[92vh]" />
        <div className="flex justify-between p-3 text-sm"><a href={src} download>Scarica</a><button onClick={() => dlg.current?.close()}>Chiudi</button></div>
      </dialog>
    </figure>
  )
}
```
`alt` e `caption` vengono da `source/*/images/manifest.csv`. Le immagini si servono in due misure (1600 px per la pagina, originale per il lightbox).

---

## 9. Grafici (Recharts)

Regole comuni: `ResponsiveContainer`, etichette dirette sui valori (`LabelList`), niente griglia verticale, tooltip con formattatori italiani, colori dai token, tabella dati equivalente collassata sotto (`<details>`).

**9a. `BarRanking`** – barre orizzontali ordinate (30 comuni per ettari/IVP/%; 11 comuni per variazione).
```tsx
import { BarChart, Bar, XAxis, YAxis, Tooltip, LabelList, ResponsiveContainer, Cell } from "recharts"
import { formatDec } from "@/lib/format"

export function BarRanking({ rows, valueKey, labelKey, colorOf, format = formatDec, onSelect }: BarRankingProps) {
  return (
    <ResponsiveContainer width="100%" height={rows.length * 28 + 24}>
      <BarChart data={rows} layout="vertical" margin={{ left: 8, right: 56 }}>
        <XAxis type="number" hide />
        <YAxis type="category" dataKey={labelKey} width={150} tick={{ fontSize: 13 }} axisLine={false} tickLine={false} />
        <Tooltip formatter={(v) => format(Number(v))} cursor={{ fill: "rgba(0,0,0,0.03)" }} />
        <Bar dataKey={valueKey} radius={[0, 6, 6, 0]} onClick={(d) => onSelect?.(d.slug)} className="cursor-pointer">
          {rows.map((r) => <Cell key={r.slug} fill={colorOf(r)} />)}
          <LabelList dataKey={valueKey} position="right" formatter={format} className="fill-[var(--ink)] text-xs tabular-nums" />
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  )
}
```

**9b. `SlopeChart`** – popolazione 2001 → 2025 per comune, costa blu e interno verde: due assi verticali (anno) e una linea per comune; implementato con `LineChart` a due punti per serie, `dataKey` = comune, `stroke` per fascia, etichette ai due estremi.

**9c. `StackedBar100`** – distribuzioni al 100 % (classi di età 2002 vs 2025; uso del suolo per comune; classi di pericolo incendio per comune). `BarChart` con `stackId="a"`, scala ordinale delle classi, legenda testuale sotto.

**9d. `ClassBadge`** – etichetta di classe con colore + testo, mai colore da solo:
```tsx
const CLASS_COLORS: Record<string, string> = { Alta: "#2E7D32", Media: "#F0B800", Bassa: "#F08800", "Molto bassa": "#D84315", Basso: "#2E7D32", Mediobasso: "#8BC34A", Medio: "#F0B800", Medioalto: "#F08800", Alto: "#D84315" }
export const ClassBadge = ({ value }: { value: string }) => (
  <span className="inline-flex items-center gap-1.5 rounded-full border border-[var(--line)] px-2 py-0.5 text-xs">
    <span className="h-2 w-2 rounded-full" style={{ background: CLASS_COLORS[value] ?? "#999" }} />{value}
  </span>
)
```

---

## 10. `Explorer` – selettore indicatore + filtro + ordine

**Cosa fa.** Il controllo unico dei blocchi dati interattivi: un `select` per l'indicatore, uno per il filtro (fascia costa/interno; classe IVP/incendio/ICR), uno per l'ordine; sotto, `BarRanking` e `DataTable` sincronizzati; click su barra o riga → `ComuneDrawer`.
```tsx
const INDICATORI = [
  { key: "sugherete_ha", label: "Sugherete (ha)", format: formatDec },
  { key: "ivp", label: "Vocazionalità pedologica (IVP)", format: (v: number) => formatDec(v, 3) },
  { key: "quota_medioalto_alto_pct", label: "Sugherete in pericolo Medioalto+Alto (%)", format: formatPct },
  { key: "quota_complesso_maggiore_pct", label: "Continuità: quota del nucleo maggiore (%)", format: formatPct },
] as const

export function ExplorerSughereta({ rows }: { rows: ComuneSughereta[] }) {
  const [ind, setInd] = useState<typeof INDICATORI[number]["key"]>("sugherete_ha")
  const [classe, setClasse] = useState<string>("")
  const [order, setOrder] = useState<"desc" | "asc">("desc")
  const [, setParams] = useSearchParams()
  const cfg = INDICATORI.find((i) => i.key === ind)!
  const data = useMemo(() => rows.filter((r) => !classe || r.classe_ivp === classe).sort((a, b) => (order === "desc" ? b[ind] - a[ind] : a[ind] - b[ind])), [rows, ind, classe, order])
  return (
    <section id="esploratore" className="space-y-6">
      <div className="flex flex-wrap items-end gap-4 rounded-3xl border border-[var(--line)] bg-white p-4">
        <Select label="Indicatore" value={ind} onChange={setInd} options={INDICATORI.map((i) => [i.key, i.label])} />
        <Select label="Classe IVP" value={classe} onChange={setClasse} options={[["", "Tutte"], ["Alta", "Alta"], ["Media", "Media"], ["Bassa", "Bassa"]]} />
        <Select label="Ordine" value={order} onChange={setOrder} options={[["desc", "Decrescente"], ["asc", "Crescente"]]} />
        <span className="ml-auto text-xs text-[var(--ink-muted)]">{data.length} comuni</span>
      </div>
      <BarRanking rows={data} valueKey={ind} labelKey="comune" format={cfg.format} colorOf={(r) => CLASS_COLORS[r.classe_ivp]} onSelect={(slug) => setParams({ comune: slug })} />
      <details><summary className="cursor-pointer text-sm text-[var(--ink-muted)]">Vedi i dati</summary><DataTable rows={data} columns={COLONNE} rowKey={(r) => r.slug} onRowClick={(r) => setParams({ comune: r.slug })} exportName="sughereta-30-comuni" /></details>
    </section>
  )
}
```
`Select` è un wrapper di `<select>` nativo con `<label>`: niente combobox custom, funziona con tastiera e screen reader.

---

## 11. `DataTable` – tabella ordinabile con paginazione ed export

**Dove.** Database bibliografico (153 righe: ricerca + 3 filtri sopra), tabella nascosta sotto ogni grafico, esploratore.
**Props.** `columns: { key, header, align?, sortable?, cell?, exportValue? }[]`, `rows`, `rowKey`, `pageSize = 25`, `onRowClick?`, `exportName?`.
Implementazione: stato `sort {key, dir}` e `page`; ordinamento con `localeCompare(…, "it")` per le stringhe e `null` in fondo; paginazione 25/50/tutte; export CSV con separatore `;` e BOM UTF-8 (apre bene in Excel italiano):
```ts
export function exportCsv<Row>(filename: string, cols: ExportColumn<Row>[], rows: Row[]) {
  const esc = (v: unknown) => { const s = v == null ? "" : String(v); return /[;"\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s }
  const lines = [cols.map((c) => esc(c.header)).join(";"), ...rows.map((r) => cols.map((c) => esc(c.value(r))).join(";"))]
  const blob = new Blob(["﻿" + lines.join("\r\n")], { type: "text/csv;charset=utf-8" })
  const a = Object.assign(document.createElement("a"), { href: URL.createObjectURL(blob), download: `${filename}.csv` }); a.click(); URL.revokeObjectURL(a.href)
}
```
Markup: `<table>` semantico con `<th scope="col" aria-sort>`, righe cliccabili anche da tastiera (`tabIndex=0`, Enter). Su mobile: contenitore `overflow-x-auto`, prima colonna `sticky`. Filtri della bibliografia: input di ricerca (su riferimento + settore), `select` settore, Paese, priorità; il filtro applica `useMemo` sui 153 record già in pagina.

---

## 12. `ComuneDrawer` – pannello scheda comune

**Cosa fa.** Pannello laterale (destra, 480 px; su mobile a tutta larghezza dal basso) che si apre quando l'URL ha `?comune=slug`. Contenuto e ordine dei blocchi in `pagine/02b-…` e `04b-…`. Azioni: Chiudi (Esc, click fuori), Copia link, precedente/successivo, link incrociato per Calangianus e Tempio Pausania.
```tsx
export function ComuneDrawer({ byslug, render }: { byslug: Record<string, Comune>; render: (c: Comune) => ReactNode }) {
  const [params, setParams] = useSearchParams()
  const slug = params.get("comune")
  const comune = slug ? byslug[slug] : undefined
  const close = () => { params.delete("comune"); setParams(params) }
  useEffect(() => { const k = (e: KeyboardEvent) => e.key === "Escape" && close(); addEventListener("keydown", k); return () => removeEventListener("keydown", k) }, [])
  return (
    <AnimatePresence>
      {slug && (
        <>
          <motion.div className="fixed inset-0 z-40 bg-black/30" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} onClick={close} />
          <motion.aside role="dialog" aria-modal aria-labelledby="drawer-title" className="fixed right-0 top-0 z-50 h-full w-full max-w-[480px] overflow-y-auto bg-white p-6 shadow-xl"
            initial={{ x: 480 }} animate={{ x: 0 }} exit={{ x: 480 }} transition={{ type: "spring", stiffness: 260, damping: 30 }}>
            <header className="flex items-start justify-between">
              <h2 id="drawer-title" className="text-2xl font-medium">{comune?.comune ?? "Comune non trovato"}</h2>
              <div className="flex gap-2">
                <button onClick={() => navigator.clipboard.writeText(location.href)} className="btn-ghost">Copia link</button>
                <button onClick={close} aria-label="Chiudi" className="btn-ghost">✕</button>
              </div>
            </header>
            {comune ? render(comune) : <p className="mt-4 text-[var(--ink-muted)]">Scegli un comune dalla mappa o dall'elenco.</p>}
          </motion.aside>
        </>
      )}
    </AnimatePresence>
  )
}
```
Il focus va sul titolo all'apertura e torna all'elemento che ha aperto il pannello alla chiusura (`useRef` sull'ultimo trigger). Il `render` compone `KpiRow`, `StackedBar100`, testi da `schede-comuni.json` / `comuni-sughereta.json`.

---

## 13. `ComuniMap` – mappa SVG dei comuni

**Cosa fa.** Confini comunali (11 dell'Alta Gallura; 30 della Sughereta con la Sardegna in grigio come sfondo) da un TopoJSON statico; riempimento per fascia o classe; hover → tooltip; click → `?comune=slug`; sotto, elenco testuale equivalente.
**Dati.** `public/geo/comuni-sardegna.topo.json`: confini ISTAT 2025 (licenza CC BY 4.0), filtrati e semplificati con mapshaper (`-simplify 8% keep-shapes`), campo `slug` aggiunto in ETL per fare join con i dataset.
```tsx
import { geoMercator, geoPath } from "d3-geo"
import { feature } from "topojson-client"

export function ComuniMap({ topo, fillOf, onSelect, width = 640, height = 520 }: MapProps) {
  const fc = useMemo(() => feature(topo, topo.objects.comuni) as FeatureCollection, [topo])
  const path = useMemo(() => geoPath(geoMercator().fitSize([width, height], fc)), [fc, width, height])
  const [hover, setHover] = useState<string | null>(null)
  return (
    <figure>
      <svg viewBox={`0 0 ${width} ${height}`} role="img" aria-labelledby="map-title" className="w-full">
        <title id="map-title">Mappa dei comuni</title>
        {fc.features.map((f) => (
          <path key={f.properties.slug} d={path(f) ?? ""} fill={fillOf(f.properties.slug)} stroke="#fff" strokeWidth={0.8}
            className="cursor-pointer transition-opacity hover:opacity-80 focus:outline-none focus:stroke-[var(--ink)]" tabIndex={0}
            onMouseEnter={() => setHover(f.properties.slug)} onMouseLeave={() => setHover(null)}
            onClick={() => onSelect(f.properties.slug)} onKeyDown={(e) => e.key === "Enter" && onSelect(f.properties.slug)}>
            <title>{f.properties.comune}</title>
          </path>
        ))}
      </svg>
      <figcaption className="sr-only">Elenco comuni: …</figcaption>
    </figure>
  )
}
```
Nessun tile server, nessuna chiave API. Il file TopoJSON pesa 60-150 kB dopo la semplificazione.

---

## 14. `Timeline36` – roadmap 4 fasi × 36 mesi

**Cosa fa.** Griglia orizzontale con 36 colonne (mesi) e le 20 azioni di `roadmap.json` come pill posizionate da `mese_inizio`/`mese_fine`, raggruppate per fase (4 corsie colorate). Click → pannello con titolo, fase, output atteso, area pilota. Su mobile diventa elenco per fase.
```tsx
export function Timeline36({ fasi, azioni, onSelect }: TimelineProps) {
  return (
    <div className="overflow-x-auto">
      <div className="grid min-w-[900px]" style={{ gridTemplateColumns: "180px repeat(36, 1fr)" }}>
        <div /> {Array.from({ length: 36 }, (_, m) => <div key={m} className="border-l border-[var(--line)] text-center text-[10px] text-[var(--ink-muted)]">{(m + 1) % 6 === 0 ? `M${m + 1}` : ""}</div>)}
        {fasi.map((fase) => (
          <Fragment key={fase.id}>
            <div className="py-3 pr-3 text-sm font-medium">{fase.nome}<span className="block text-xs text-[var(--ink-muted)]">mesi {fase.mese_inizio}–{fase.mese_fine}</span></div>
            <div className="relative col-span-36 border-t border-[var(--line)] py-2">
              {azioni.filter((a) => a.fase === fase.id).map((a, i) => (
                <button key={a.numero} onClick={() => onSelect(a)} className="absolute h-7 truncate rounded-full bg-[var(--green)]/15 px-3 text-xs hover:bg-[var(--green)]/30"
                  style={{ left: `${((a.mese_inizio - 1) / 36) * 100}%`, width: `${((a.mese_fine - a.mese_inizio + 1) / 36) * 100}%`, top: 8 + (i % 3) * 32 }}>
                  {a.numero}. {a.titolo}
                </button>
              ))}
            </div>
          </Fragment>
        ))}
      </div>
    </div>
  )
}
```

---

## 15. `SourceNote`, `MethodNotes`, `Glossary`

```tsx
export const SourceNote = ({ children }: { children: ReactNode }) => (
  <p className="mt-3 text-[12px] text-[var(--ink-muted)]">Fonte: {children}</p>
)
// Fonte: Studio Green community UCAG 193, Tab. 1a, p. 22
```
`MethodNotes`: `<section>` con `<dl>` di voci {label, formula?, desc} per spiegare IVP, IPI, ICR e gli indici demografici; sfondo `--ice`, icona calcolatrice.
`Glossary`: i termini marcati `[[IVP]]` nei Markdown diventano `<abbr title="…">` con sottolineatura a puntini e tooltip su hover/focus; dizionario da `glossario.md` convertito in JSON in build.

---

## 16. Utility condivise

```ts
// src/lib/format.ts – formato italiano ovunque
const nf = new Intl.NumberFormat("it-IT")
export const formatInt = (n?: number | null) => (n == null ? "—" : nf.format(Math.round(n)))
export const formatDec = (n?: number | null, d = 1) => (n == null ? "—" : new Intl.NumberFormat("it-IT", { maximumFractionDigits: d, minimumFractionDigits: d }).format(n))
export const formatPct = (n?: number | null, sign = false) => (n == null ? "—" : `${sign && n > 0 ? "+" : ""}${formatDec(n)} %`)
```
```ts
// src/data/index.ts – i JSON entrano nel bundle e vengono validati in build
import { z } from "zod"
import raw from "../../data/sughero-sardegna/comuni-sughereta.json"
const Comune = z.object({ slug: z.string(), comune: z.string(), rank: z.number(), sugherete_ha: z.number(), ivp: z.number(), classe_ivp: z.string(), /* … */ })
export const comuniSughereta = z.object({ dati: z.array(Comune) }).parse(raw).dati
```
Gli schemi Zod si scrivono leggendo i `.schema.md` dei dataset; un test `vitest` fa il parse di tutti i JSON così un dato malformato blocca la build.

---

## 17. Pagina tipo (composizione)

```
<SectionHero eyebrow title standfirst figure|orbs>
<KpiRow>                       ← apertura numerica
<Section id="…">               ← una per messaggio: <h2 titolo-messaggio> <p lettura> <Chart> <SourceNote>
<FigureLightbox>               ← infografica originale dove esiste
<Explorer> + <ComuneDrawer>    ← unica interazione della pagina
<Cards "Continua">             ← porte verso le altre pagine
<MethodNotes> <Footer>
```
Sottomenu di pagina: `<nav aria-label="In questa pagina">` sticky con le ancore dichiarate nel frontmatter (`Ancore:`), evidenziazione con `IntersectionObserver`.
