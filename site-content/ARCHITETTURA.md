# Architettura del mini-sito – Green community UCAG 193

Sito di **comunicazione**, non portale dati: il succo di due studi RISSTE (≈415 pagine) in **6 pagine**, con una landing d'effetto, dati resi visivi e le infografiche originali. Dettagli e PDF restano scaricabili. Lingua: italiano.

## Sitemap (6 pagine + schede comune in pannello)

```
/                              Landing            effetto wow, 5 messaggi chiave, 4 KPI, ingresso alle due sezioni
/progetto                      Progetto           cos'è UCAG 193, metodo, gruppo di lavoro, PDF, dataset, glossario, crediti
/alta-gallura                  Alta Gallura       un territorio a due velocità: demografia, ambiente, 11 comuni (pannello scheda)
/alta-gallura/strategia        Strategia          framework Green community, ESG, tre filiere, roadmap 36 mesi
/sughero-sardegna              Sughereta          30 comuni e tre indici IVP·IPI·ICR, esploratore (pannello scheda)
/sughero-sardegna/innovazione  Innovazione        technology scouting, certificazioni, database, modello S.U.G.H.E.R.A., conclusioni
```

Le **schede comune** (11 + 30) non sono pagine: si aprono in un pannello laterale sopra l'esploratore, con URL condivisibile `?comune=slug`. Calangianus e Tempio Pausania rimandano da una sezione all'altra.

Navigazione: **Progetto · Alta Gallura · Sughero Sardegna**, con le due sottopagine nel menu di sezione. Footer: loghi, RISSTE, CUP, PDF.

## Principi

1. Piramide rovesciata: messaggio-titolo, 3-4 numeri, spiegazione, fonte (P1/P2 + pagina PDF).
2. Un'interazione per blocco dati (ordina, filtra, scegli il comune). Niente dashboard.
3. Infografiche originali a piena larghezza con lightbox; i grafici ricostruiti dai dataset in `data/` (per la Sughereta **solo** dai dataset, vedi avvertenze nel brief).
4. Ogni pagina è una sequenza di sezioni, ciascuna con un compito solo.

## Pagine

Notazione: `[dati]` file in `data/`, `[fig]` immagine in `source/*/images/`, `[testo]` file in `site-content/pagine/` da cui prendere i contenuti (i file restano granulari; si accorpano in build).

### `/` Landing — `[testo] 00-home`
1. **Hero** immersivo (vedi brief §3): titolo, standfirst, due CTA. Sfere fluttuanti.
2. **Il progetto in 60 parole** + 4 KPI: 11 comuni · 35.242 abitanti · >80 % del sughero italiano · 83.790,90 ha di sugherete. `[dati] alta-gallura/kpi-sintesi`, `sughero-sardegna/sintesi-regionale`.
3. **Cinque messaggi chiave** come sequenza a scorrimento (una schermata ciascuno, sfondo che cambia colore): due velocità · il sughero come infrastruttura · suolo-fuoco-continuità · tre filiere ESG · roadmap e modello.
4. **Due porte** (card) verso Alta Gallura e Sughero Sardegna.
5. **Chi siamo**: RISSTE, Unione dei Comuni, CUP.

### `/progetto` — `[testo] 01-progetto + 12-documenti`
Cos'è la Green community (L. 221/2015, PNRR) · finalità e obiettivi · metodo a tre pilastri · perché due studi · gruppo di lavoro (5 profili) · **Documenti**: i due PDF, galleria 16 figure, dataset aperti, glossario, limiti, crediti e contatti. `[dati] obiettivi-studio`; `[fig] fig-2a`.

### `/alta-gallura` — `[testo] 02-hub + 03-territorio + 04-comuni + 04b-template`
1. Hero di sezione con `[fig] fig-3a` (mappa sinottica).
2. **Popolazione 2001→2025**: slope/barre per comune, costa vs interno. `[dati] popolazione-storica`.
3. **Saldi**: naturale −3.402 vs migratorio +3.286 per asse. `[dati] saldi-demografici`, `confronto-costa-entroterra`.
4. **Età, famiglie, stranieri, scuola**: KPI e barre impilate 2002/2025. `[dati] struttura-eta`, `famiglie`, `stranieri-e-scuola`.
5. **Imprese e scenari 2035**: variazione per settore, tre scenari come card. `[dati] imprese`, `scenari-2035`; `[fig] fig-1a` in lightbox.
6. **Ambiente**: sugherete e distretti forestali, uso del suolo per comune, Natura 2000, incendi. `[dati] uso-suolo-comuni`, `natura-2000-e-vincoli`.
7. **Gli 11 comuni**: mappa SVG + griglia card, filtro costa/interno, click → **pannello scheda** (KPI, mini-grafico popolazione, uso suolo top 6, cosa dice lo studio, criticità e opportunità). `[dati] schede-comuni`, `sintesi-comparativa-comuni`, `pedologia-comuni`.

### `/alta-gallura/strategia` — `[testo] 05-green-community + 06-roadmap`
Framework e governance `[fig] fig-4a` · ESG in tre colonne `[dati] indicatori-esg` · servizi ecosistemici `[fig] fig-4b` · **tre filiere** in tab `[fig] fig-4c/4d/4e` `[dati] filiere` · contratto di filiera e strumenti · formazione · **Roadmap** timeline 4 fasi × 36 mesi `[fig] fig-4f` `[dati] roadmap` · aree pilota sulla mappa · Living Lab e replicabilità.

### `/sughero-sardegna` — `[testo] 07-hub + 08-sughereta + 08b-template`
1. Hero: Sardegna ≈90 % delle sugherete italiane; 30 comuni = 83.790,90 ha. `[dati] contesto-sughero-sardegna`.
2. **Tre indici** in tre card (domanda, scala, classi). `[dati] indici-definizioni`.
3. **Esploratore 30 comuni**: barre ordinabili (ettari · IVP · % pericolo · ICR), filtro per classe, tabella compatta con badge; click → **pannello scheda** (indici, distribuzioni pedologica e incendio, continuità, profilo integrato, indicazioni operative). `[dati] comuni-sughereta`. `[fig] fig-2/3/4` solo in lightbox come elaborazione grafica.
4. **Lettura integrata**: matrice IVP × incendio × ICR e profili. `[dati] sintesi-regionale`.

### `/sughero-sardegna/innovazione` — `[testo] 09-innovazione + 10-framework`
Ricerca per Paese `[fig] fig-5` · ambiti `[fig] fig-6` · TRL a tre fasce · 9 direttrici (card) `[dati] direttrici-innovazione` · certificazioni (tabella leggera) `[dati] strumenti-certificazione` · **database bibliografico** 153 record con ricerca e 3 filtri `[dati] bibliografia-scientifica` · **S.U.G.H.E.R.A.** stepper 7 passi `[fig] fig-7` `[dati] framework-sughera` · conclusioni in 8 messaggi `[dati] conclusioni`.

## Componenti

Specifica e codice di esempio in [COMPONENTI.md](COMPONENTI.md).

| Componente | Dove |
|---|---|
| `HeroOrbs`, `GhostWord`, `MicroLabel`, `DecorticaRings` | landing e hero di sezione |
| `MessageSlide` | i cinque messaggi della landing |
| `KpiRow`, `StatArc` | apertura numerica di ogni pagina |
| `FigureLightbox` | le 16 infografiche originali |
| `BarRanking`, `SlopeChart`, `StackedBar100`, `ClassBadge` | blocchi dati |
| `Explorer` + `DataTable` | 30 comuni, 11 comuni, database bibliografico |
| `ComuneDrawer` | pannello scheda comune (`?comune=slug`) |
| `ComuniMap` | mappa SVG dei comuni (TopoJSON ISTAT) |
| `Timeline36` | roadmap 4 fasi × 36 mesi |
| `SourceNote`, `MethodNotes`, `Glossary` | fonti, note metodologiche, tooltip acronimi |

## Fuori dal sito
Schede PDF integrali, tabelle GIS estese, bibliografie di capitolo, firme e dati personali oltre nome e ruolo.
