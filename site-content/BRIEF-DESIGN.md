# Brief di design e sviluppo – Mini-sito "Green community UCAG 193"

Committente contenuti: R.I.S.S.T.E. (Olbia) per l'Unione dei Comuni Alta Gallura. CUP E77G24000450002.
Documenti collegati: sitemap e pagine in [ARCHITETTURA.md](ARCHITETTURA.md); specifica e codice dei componenti in [COMPONENTI.md](COMPONENTI.md); testi in `pagine/`; dati in `../data/`; figure in `../source/*/images/`; brand in `../source/brand/`.

## 1. Obiettivo, pubblico, messaggi

**Obiettivo.** Far capire in 30 secondi cos'è il progetto, in 3 minuti i cinque messaggi chiave, e dare a chi vuole approfondire la scheda del proprio comune e i PDF. Comunicazione istituzionale con una landing memorabile, non un report online.

**Pubblico.** Amministratori e tecnici degli 11 Comuni e dell'Unione; Regione e agenzie (Forestas, ARPAS, Laore); filiere (proprietari forestali, aziende del sughero, allevatori, GAL, Distretto delle Ruralità); poi stampa, cittadini, ricercatori, partner PNRR.

**Cinque messaggi** (sequenza della landing e titoli delle sezioni):
1. **Un territorio a due velocità.** Costa +16 %, interno fino a −20 %; l'Unione tiene solo grazie ai migranti (+3.286) contro un saldo naturale di −3.402. 301 anziani ogni 100 giovani.
2. **Il sughero è l'infrastruttura identitaria.** L'Alta Gallura lavora oltre l'80 % del sughero italiano; la Sardegna ha ≈90 % delle sugherete nazionali.
3. **La risorsa non basta.** Nei 30 comuni della Sughereta Sardegna (83.790,90 ha) contano suolo (IVP), fuoco (IPI), continuità (ICR): 21 su 30 hanno suoli vocati, in 16 oltre il 90 % delle sugherete è in classe di pericolo alta.
4. **Tre filiere, un metodo ESG.** Bosco-sughero, bovina estensiva, suinicola agroforestale, misurate con indicatori e impronte, governate da contratti di filiera.
5. **36 mesi e un modello replicabile.** Aree pilota, baseline, Living Lab, certificazione di gruppo; S.U.G.H.E.R.A. come sistema di supporto alle decisioni per la Sardegna.

## 2. Tono di voce
Istituzionale ma piano: frasi ≤ 22 parole, una idea per frase, titoli che affermano. Acronimi sciolti la prima volta e con tooltip. Ogni numero ha la fonte (studio + pagina). Dopo ogni criticità, la leva proposta dallo studio. Niente enfasi promozionale.

## 3. Look and feel

**In una frase.** Carta bianco-ghiaccio, luce colorata che galleggia, tipografia grande e leggera, dati puliti in card arrotondate. Il sito deve sembrare un'installazione luminosa più che una brochure: poco inchiostro, molta aria, colore solo come luce sfumata e come significato nei dati.

**Riferimenti visivi** (forniti dal committente) e come li traduciamo:

| Riferimento | Cosa prendiamo | Dove |
|---|---|---|
| Sfere sfumate e sgranate verde-ciano-blu su fondo ghiaccio, micro-etichette "CRY — / — STILLE" | Orbi con `radial-gradient` + blur + grana; deriva lenta e parallasse; etichette 11 px maiuscole con tratto sottile | Landing, hero di sezione |
| Sfera unica gradiente verde→blu | Un solo orbo grande, quasi statico, nelle pagine di servizio | `/progetto`, stati vuoti |
| Anelli concentrici morbidi (target arancione) | **Cerchio di decortica**: 12 anelli sfumati e sgranati (il turno dodicennale del sughero), verde-ciano per l'Alta Gallura, ambra-terracotta per il Sughero; ruota piano; è anche il loader | Hero di sezione, pannello comune, loader |
| Hero "Human Voice Over": titolo enorme leggero in tre righe, sfondo neutro, controlli tondi | Titolo 72-120 px peso 300-400, interlinea 0.95, standfirst piccolo grigio | Landing, hero di ogni pagina |
| "Meridian Fund": blob sfumato + parola-fantasma in outline dietro il titolo | `GhostWord` in outline 1 px, tagliata dai bordi ("ALTA GALLURA", "SUGHERETA", "UCAG 193") | Landing e hero di sezione |
| "03 Problem": percentuali grandi, linee sottili verso un semicerchio sfumato con tacche, card arrotondate con icona tonda, pillole "From User Interviews" | `StatArc` + `KpiRow` con pillola "Fonte: …" | Blocchi KPI di landing e sezioni |

**Regole di composizione**
- Il colore saturo vive solo negli orbi, negli anelli e nelle classi dei dati. Testo e UI restano in `--ink`, `--ink-muted`, bianco.
- Si muove lo sfondo, mai il testo. Cicli tra 12 e 30 s, easing sinusoidale, tutto disattivabile con `prefers-reduced-motion`.
- Massimo 6 orbi per schermata, 1 negli hero interni. Nessuna foto stock, nessun gradiente scuro, nessun glassmorphism.
- Le 16 infografiche originali sono le uniche "immagini": a piena larghezza, mai ritagliate, con didascalia, fonte e lightbox.
- Ogni pagina: hero → KPI → sezioni con un messaggio ciascuna → una sola interazione → porte verso le altre pagine → note e fonti. Un sottomenu sticky con le ancore della pagina.

**Apertura a capitoli (intro immersiva).** Riferimento: le esperienze scroll-driven "a capitoli" (schermate a tutta altezza bloccate allo scroll, una scena e un numero per capitolo, indicatore di avanzamento, poi il sito prosegue in layout tradizionale). Lo adottiamo in tre pagine: **landing** (5 capitoli = i cinque messaggi), **`/alta-gallura`** e **`/sughero-sardegna`** (4 capitoli ciascuna con i numeri principali della sezione). Regole:
- Ogni capitolo: una frase ≤ 12 parole, un numero grande con unità, una riga di contesto, la fonte in piccolo. La scena è fatta con orbi, anelli e parola-fantasma (nessun 3D/WebGL): cambia colore, dimensione e posizione tra un capitolo e l'altro.
- Il contenitore è `sticky` a tutta altezza; lo scroll fa avanzare i capitoli (scroll-snap opzionale, mai obbligatorio). Indicatore verticale a puntini con numero `01 / 05`, hint "scorri" al primo capitolo, pulsante **"Salta l'introduzione"** sempre visibile che porta all'ancora del contenuto.
- Durata: 5 capitoli ≈ 4 schermate di scroll; niente autoplay. Tastiera: frecce e Pag↓ avanzano; Tab salta ai controlli.
- `prefers-reduced-motion` e mobile stretto: nessun pinning, i capitoli diventano card verticali con lo stesso contenuto.
- Dopo l'ultimo capitolo il sito "atterra" sul layout tradizionale (KPI, sezioni, esploratore). Il passaggio è marcato da un titolo di sezione e dal sottomenu sticky che compare.
- Le pagine `/progetto`, `/alta-gallura/strategia` e `/sughero-sardegna/innovazione` non hanno l'intro: hero semplice con un solo elemento animato.

**Landing, sequenza.** (1) Hero a piena altezza: orbi, parola-fantasma, titolo *Green community / Alta Gallura*, standfirst, due CTA, micro-etichette `RISSTE —`, `— UCAG 193`, `11 COMUNI`, `30 COMUNI`. (2) Il progetto in 60 parole e 4 KPI con `StatArc`. (3) Intro a capitoli: cinque schermate, un messaggio ciascuna: numero d'ordine, frase, KPI con conteggio; l'orbo cambia colore e forma (verde → ciano → blu → ambra → verde) e la parola-fantasma cambia. (4) Due porte verso le sezioni. (5) Chi siamo. La descrizione dell'illustrazione di ogni pagina è nella riga `visual` del frontmatter dei file in `pagine/`; i capitoli di apertura sono la sezione "Capitoli di apertura" degli stessi file.

## 4. Identità visiva

**Colori**
| Token | Hex | Uso |
|---|---|---|
| `--ice` | `#F4FBFA` | fondo pagina |
| `--ink` / `--ink-muted` | `#132019` / `#5B6B62` | testo / secondario |
| `--green` | `#4E9A3F` | primario, sezione Alta Gallura (logo `#78C850`→`#389848` per gradienti) |
| `--acid` / `--cyan` | `#7CFF3F` / `#3FE9FF` | solo orbi e accenti luminosi, mai testo |
| `--blue` | `#2F6FB0` | dati, governance, link |
| `--cork` / `--cork-light` | `#C2603A` / `#E8C28E` | sezione Sughero Sardegna |
| `--fire` | `#E0592A` | solo classe incendio Alto |
| `--line` | `#DDE6E2` | bordi, linee sottili |

Scala ordinale delle classi (IVP/ICR Alta→Molto bassa; incendio Basso→Alto): `#2E7D32 · #8BC34A · #F0B800 · #F08800 · #D84315`, sempre con etichetta testuale. Costa blu, interno verde. Categoriale max 6: verde, blu, ambra `#D9A441`, terracotta, teal `#207868`, viola spento `#7A6685`.

**Tipografia.** Un solo sans geometrico self-hosted (Inter, variabile): hero 300-400, H2 500 28-40 px, corpo 17 px / 1.6, KPI cifre tabulari 48-72 px peso 500, micro-etichette 11-12 px maiuscole tracking 0.08 em.

**Layout.** Contenitore 1200 px, griglia 12, testo su 8 colonne (≤ 70 caratteri/riga), figure e dati fino a 12. Sezioni con 96-128 px di aria (64 su mobile). Card bianche raggio 20-24 px, ombra quasi nulla, bordo `--line`. Mobile first: KPI in 2 colonne, tabelle con scroll orizzontale interno, pannello comune dal basso.

**Icone e loghi.** Lucide 1,5 px. RISSTE da `brand/`; Unione, PNRR e Regione da richiedere in vettoriale. Non usare il logo QGIS.

## 5. Dati e grafici

1. Un grafico dice una cosa: titolo-messaggio, sottotitolo con unità e anno, fonte sotto, tabella dati collassata ("Vedi i dati").
2. Forme semplici: barre orizzontali ordinate, slope 2001→2025, impilate 100 %, KPI. Niente torte, radar, 3D.
3. Colore = significato (scale sopra); etichette dirette sui valori, leggibili anche senza hover.
4. Interazione minima: selettore indicatore + filtro + ordine; click su riga, barra o comune sulla mappa → pannello comune con URL `?comune=slug`.
5. Mappe senza servizi esterni: TopoJSON dei comuni sardi (ISTAT, CC BY 4.0) semplificato e reso in SVG.
6. Numeri in formato italiano (`Intl.NumberFormat("it-IT")`), unità sempre esplicite.

**Avvertenze dai dataset** (dettagli in `../data/README.md`): le figure 2-4 dello studio sul sughero non coincidono con le schede comunali → grafici solo da `comuni-sughereta.json`, figure mostrate come "elaborazione grafica dello studio"; database bibliografico 153 record (non 166); 21 comuni a IVP alta (non 22); mesi della roadmap letti dall'infografica; nessun valore quantitativo ESG e nessuna superficie comunale totale: non inventarli.

## 6. Come si costruisce

**Stack.** React 19 + TypeScript + Vite + Tailwind 4; Recharts per i grafici; `motion` per le animazioni; `d3-geo` + `topojson-client` per la mappa; Zod per validare i dati; `react-router` con prerender statico delle 6 pagine (`vite-react-ssg`) per SEO e primo paint immediato. Nessun backend, nessun database, nessun CMS: i contenuti vivono nel repo.

**Struttura**
```
site/
  public/figure/         ← copia di source/*/images (due misure: 1600 px e originale)
  public/pdf/            ← i due PDF
  public/geo/            ← comuni-sardegna.topo.json (ISTAT semplificato)
  public/fonts/          ← Inter variabile, self-hosted
  src/pages/             ← 6 pagine: Landing, Progetto, AltaGallura, Strategia, Sughereta, Innovazione
  src/components/        ← vedi COMPONENTI.md
  src/content/           ← i Markdown di site-content/pagine, letti in build
  src/data/              ← i JSON di data/, validati con Zod
  src/lib/               ← format, glossario, url del pannello
```

**Pipeline contenuti.** I file `pagine/*.md` sono il copy finale: frontmatter (slug, title, description, visual) e sezioni Markdown. In build il frontmatter diventa metadati e SEO; le sezioni "Capitoli di apertura" alimentano `IntroChapters`; le righe "Numeri:" diventano `KpiRow`; il blocco "Approfondimenti" indica quali dataset rendere con `Explorer`, `DataTable` o grafici. I pannelli comune leggono i campi dei JSON indicati in `02b`/`04b`.

**Pipeline dati.** `data/**/*.json` copiati in `src/data/`, ognuno con uno schema Zod scritto leggendo il rispettivo `.schema.md`; un test fa il parse di tutti i file: se un dato non valida, la build fallisce. Le classifiche e gli aggregati si calcolano in build o in `useMemo`, mai a mano nei testi.

**Deploy.** Repository Git collegato a Vercel, build `vite build` (con prerender), output statico, preview per branch, dominio del committente. Nessuna variabile d'ambiente. Header di cache lunghi su figure, geo e font.

**Qualità.** Lighthouse ≥ 95 su tutte le aree, LCP < 2 s su 4G, JS iniziale < 120 kB per pagina (Recharts caricato solo nelle pagine dati), WCAG 2.1 AA (obbligo PA): skip-link, focus visibile, `alt` da `images/manifest.csv`, tabella equivalente sotto ogni grafico, contrasto verificato, animazioni disattivabili. `lang="it"`, sitemap, Open Graph per pagina, nessun cookie di tracciamento (niente banner).

## 7. Consegne e aperti
1. Design system (token §4) e moodboard della landing – 1 tavola Figma.
2. Wireframe delle 6 pagine e del pannello comune (desktop e mobile); prototipo motion dell'hero.
3. Sviluppo con dati reali da `data/` e testi da `pagine/`; QA numeri vs fonte, accessibilità, performance.

Da chiedere al committente: loghi vettoriali Unione, Regione, PNRR; dominio e account Vercel; licenza dati (proposta CC BY 4.0); eventuale versione inglese.
