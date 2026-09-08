# source/ – materiale estratto dai report RISSTE (progetto Green community UCAG 193)

Estrazione automatica (PyMuPDF + pdfplumber) dei due PDF in `Documenti/`, ripulita di header/footer e organizzata per capitolo. È la base di lavoro per il mini-sito: **non modificare a mano questi file**, sono rigenerabili; le rielaborazioni vanno in `data/` (dataset curati) e `site-content/` (testi del sito).

| Cartella | Documento | Pagine |
|---|---|---|
| [parte1-green-community-alta-gallura/](parte1-green-community-alta-gallura/README.md) | *Green community UCAG 193 – Strategie territoriali integrate: gestione forestale e sviluppo sostenibile delle filiere locali* (Anno 2025) | 219 |
| [parte2-filiera-sughero-sardegna/](parte2-filiera-sughero-sardegna/README.md) | *Valorizzazione della filiera del sughero in Sardegna – Un framework multidisciplinare per l'integrazione tra analisi territoriale, innovazione e gestione sostenibile* (Anno 2025) | 196 |
| [brand/](brand/manifest.csv) | Logo R.I.S.S.T.E. (orizzontale e verticale) e sfondo di copertina | – |

Struttura di ogni cartella documento:

- `README.md` – indice dei capitoli con pagine PDF
- `capitoli/NN-*.md` – testo per capitolo, con titoli gerarchici, elenchi, tabelle Markdown in posizione e marcatori `<!-- pagina N -->`
- `full-text.md` – testo integrale continuo
- `headings.md` – outline dei titoli rilevati
- `tables/pNNN-tK.csv` – ogni tabella in CSV (`manifest.csv` con pagina, righe/colonne, qualità `ok`/`sparse`, contesto)
- `images/` – figure raster del documento, rinominate in modo parlante (`manifest.csv` con didascalia originale e pagina)

Note:

- Le firme autografe presenti nei frontespizi e i loghi duplicati sono stati **esclusi** dagli asset.
- Le tabelle marcate `sparse` avevano colonne fantasma nel PDF: sono state compattate automaticamente, verificarle prima dell'uso.
- I numeri di pagina nei marcatori sono quelli fisici del PDF (non la numerazione stampata, che riparte in ogni sezione).
- Autori: R.I.S.S.T.E. – Centro Studi per la Ricerca, l'Innovazione, lo Sviluppo Sostenibile e la Transizione Energetica (Olbia). Coordinatrice scientifica: Maria Fais; collaboratori: Nicola Garippa, Gianfranco Sanna, Vincenzo Sechi. CUP E77G24000450002.
