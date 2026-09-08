# indicatori-esg.json

Tutti gli indicatori di sostenibilità (KPI) citati nel framework ESG (4.3.1), nel set integrato di 4.5 e nei paragrafi di monitoraggio delle tre filiere, organizzati per dimensione E/S/G e per filiera. `dati` è un array piatto di indicatori.

## Campi

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `id` | string | – | Codice redazionale `<dimensione>-<T/S/B/P><nn>` (T trasversale, S sughero, B bovina, P suinicola) |
| `dimensione` | string | – | `E`, `S`, `G` |
| `filiera` | string | – | `trasversale`, `sughero`, `bovina`, `suinicola` |
| `nome` | string | – | Nome sintetico (redazionale) |
| `cosa_misura` | string | – | Formulazione fedele del documento |
| `unita` | string\|null | – | Unità di misura solo se indicata o chiaramente implicita nel testo |
| `fonte_dato` | string\|null | – | Fonte del dato solo se indicata (quasi sempre `null`) |
| `pagina_pdf` | int | – | Pagina PDF |

## Fonte
Parte 1: 4.3.1 (pag. 72-73), 4.5 (pag. 79), 4.5.2.1 (pag. 81-82), 4.5.2.2-4.5.2.3 sughero (pag. 82), monitoraggio bovina (pag. 84-85), monitoraggio suinicola (pag. 87-88), 4.7.2 baseline (pag. 90), Figura 4a (pag. 72).

## Avvertenze
- Sistema dichiaratamente "preliminare": nessun valore target, nessuna baseline numerica.
- I nomi sono redazionali; unità e fonti mancano nel documento nella quasi totalità dei casi.
- Numerazione dei sottoparagrafi di monitoraggio duplicata nel documento (tutti "4.5.2.1"): usare le pagine.

## Idee per il sito
- Matrice 3x4 (dimensione x filiera) con conteggio indicatori e drill-down.
- Filtri per dimensione/filiera con schede indicatore.
- Cruscotto "baseline da costruire": indicatori con `unita` null evidenziati come da definire.
