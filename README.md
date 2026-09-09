# RISSTE – Green community UCAG 193

Mini-sito che presenta i due studi RISSTE (2025) del progetto **Green community UCAG 193** (Unione dei Comuni Alta Gallura, CUP E77G24000450002):

1. *Strategie territoriali integrate: gestione forestale e sviluppo sostenibile delle filiere locali* (Alta Gallura, 11 comuni) – 219 pagine
2. *Valorizzazione della filiera del sughero in Sardegna – Un framework multidisciplinare* (30 comuni della Sughereta Sardegna) – 196 pagine

## Il sito

| | |
|---|---|
| **Sito live** | **https://risste-green-community.vercel.app** |
| Repo sorgente | https://github.com/Design-Brothers/risste-green-community |
| Hosting | Vercel (deploy statico dalla cartella `prototype/`, URL puliti via `vercel.json`) |

### Pagine

| URL | Contenuto |
|---|---|
| `/` | Landing — hero a sfere di luce, 5 capitoli scroll-driven, le due "porte" degli studi |
| `/alta-gallura` | Studio 1 — 11 comuni a due velocità, capitoli, schede comune con pannello condivisibile via URL |
| `/strategia` | Framework ESG, 3 filiere, roadmap operativa 36 mesi (timeline con pill cliccabili) |
| `/sughero-sardegna` | Studio 2 — 30 comuni, tre indici (IVP/IPI/ICR), esploratore con drawer comunale |
| `/innovazione` | Technology scouting: 153 pubblicazioni, 9 direttrici, certificazioni, framework S.U.G.H.E.R.A., database bibliografico filtrabile con export CSV |
| `/progetto` | Il progetto, il metodo, il gruppo di lavoro, i documenti (PDF + figure + dataset) |

Stack: sito statico HTML/CSS/JS senza framework (design system in `prototype/assets/site.css` + `site.js`), dati consolidati in `prototype/assets/data*.js`. Desktop first, adattato mobile con menu hamburger.

## Sviluppo

```bash
cd prototype
node shoot.mjs          # verifica visiva: screenshot + overflow-x + errori console (Playwright + Chrome)
node build-data.mjs     # rigenera assets/data.js da data/
node build-data2.mjs    # rigenera assets/data-sughero.js e data-strategia.js
vercel --prod --yes     # deploy di produzione (richiede Vercel CLI autenticata)
```

## Le tre "passate" di preparazione

| Cartella | Contenuto | Stato |
|---|---|---|
| `Documenti/` | I due PDF originali firmati | sorgente |
| `source/` | Testo integrale in Markdown per capitolo, 349 tabelle CSV, 23 figure rinominate, brand ([indice](source/README.md)) | passata 1 ✔ |
| `data/` | 35 dataset curati JSON/CSV con schema e README per area ([indice](data/README.md), [convenzioni](data/CONVENZIONI.md)) | passata 2 ✔ |
| `site-content/` | [Architettura del sito](site-content/ARCHITETTURA.md), [brief di design](site-content/BRIEF-DESIGN.md), 14 file pagina in `pagine/`, microcopy, SEO, [glossario](site-content/glossario.md) ([indice](site-content/README.md)) | passata 3 ✔ |
| `prototype/` | Il sito pubblicato (6 pagine, assets, PDF, script di verifica e build) | prodotto ✔ |

Rigenerare `source/`: vedi [scripts/README.md](scripts/README.md).
Note di lavoro sul consolidamento dei dati: [NOTES-next.md](NOTES-next.md).
