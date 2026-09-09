# Sughero Sardegna — Ricerca, innovazione e gestione sostenibile

Sito del *Progetto di ricerca e sviluppo, valorizzazione del sughero sardo e innovazione tecnologica* (CUP E77G24000450002). Soggetto attuatore: **Centro Studi R.I.S.S.T.E. APS**. Finanziato dalla Regione Autonoma della Sardegna – Assessorato dell’Agricoltura e riforma agro-pastorale.

La Gallura è presentata come principale sistema territoriale e produttivo della filiera, non come ambito esclusivo del progetto.

## Il sito

| | |
|---|---|
| **Sito live** | **https://risste-green-community.vercel.app** (alias previsto: risste-sughero-sardegna.vercel.app) |
| Repo | https://github.com/Design-Brothers/risste-green-community |
| Hosting | Vercel (cartella `prototype/`) |

### Pagine

| URL | Contenuto |
|---|---|
| `/` | Home — cornice regionale, WP1–4, tre percorsi |
| `/progetto` | Il progetto regionale: obiettivi, metodo, gruppo |
| `/ricerca-mercato` | WP2 — filiera, imprese aggregate, criticità e opportunità |
| `/sughero-sardegna` | Atlante del sughero: 30 comuni, mappa, IVP · IPI · ICR |
| `/innovazione` | Innovazione, certificazioni, 153 pubblicazioni, S.U.G.H.E.R.A. |
| `/alta-gallura` | Focus Gallura — approfondimento territoriale |
| `/strategia` | Filiere, ESG e roadmap del focus Gallura |
| `/database` | Mappa, catalogo dati, censimento aziende |
| `/documenti` | PDF e 36 dataset JSON/CSV |

Stack: HTML/CSS/JS statico (`prototype/assets/site.css` + `site.js`). Dati in `prototype/assets/data*.js` e dataset aperti in `prototype/dati/`.

## Sviluppo

```bash
cd prototype
node build-open-data.mjs   # rigenera prototype/dati da data/
node shoot.mjs             # verifica visiva (Playwright + Chrome)
vercel --prod --yes        # deploy
```

I PDF in `prototype/pdf/` hanno copertina e premessa istituzionali anteposte agli studi firmati (`build-pdf-covers.py`).
