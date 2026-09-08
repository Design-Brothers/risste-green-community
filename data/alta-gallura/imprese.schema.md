# imprese.json / imprese.csv / imprese-macro-settori.csv

Imprese attive per comune nel 2021 e 2025 con variazione % e ripartizione per settore 2025 (dal testo del par. 1.8), aggregati per fascia costiera / entroterra / Unione (par. 1.9-1.10) e la Tabella 1d per macro-settore economico a livello di Unione (2021, 2023, 2025). `dati` = 11 record `livello` = `comune` + 3 `aggregato`; `macro_settori_unione` = 7 righe (6 settori + totale).

## Campi (`dati`)

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `comune`, `slug`, `fascia` | string | – | Come in popolazione-storica |
| `livello` | string | – | `comune` o `aggregato` |
| `imprese_2021` | int\|null | imprese | Imprese attive 2021 (null per Viddalba e per le fasce: non scritte) |
| `imprese_2023` | int\|null | imprese | Solo Unione: 4.822 |
| `imprese_2025` | int | imprese | Imprese attive 2025 |
| `var_pct_2021_2025` | float | % | Variazione 2021-2025 |
| `servizi_2025`, `agricoltura_2025`, `costruzioni_2025`, `commercio_2025`, `industria_2025` | int\|null | imprese | Imprese del settore nel 2025; null = non citato nel testo (NON zero) |
| `*_2025_pct` | float\|null | % | Quota del settore sul totale comunale, solo dove il testo la scrive |
| `densita_imprese_per_1000_ab_2025` | int | imprese/1.000 ab. | Solo Unione: 136 |
| `note` | string\|null | – | Precisazioni |
| `pagine_pdf` | int[] | – | Pagine PDF |

## Campi (`macro_settori_unione`)

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `macro_settore` | string | – | Denominazione della Tabella 1d |
| `codice` | string | – | servizi, agricoltura, costruzioni, commercio, industria, non-classificate, totale |
| `imprese_2021`, `imprese_2023`, `imprese_2025` | int | imprese | Consistenza |
| `quota_2025_pct` | float | % | Quota sul totale 2025 |
| `var_pct_2021_2025` | float | % | Variazione 2021-2025 |

## Fonte
Parte 1: par. 1.8 e Figura 1a (pag. 27-28), par. 1.9 (pag. 28), par. 1.10 (pag. 29-30), Tabella 1d (pag. 30), par. 1.11 (pag. 30). Fonte originaria: Registro Imprese CCIAA e ASIA-ISTAT 2021-2025.

## Avvertenze
- Il dettaglio comunale per settore proviene dal testo del par. 1.8 (la Figura 1a non è una tabella estraibile): il testo cita 3-5 settori per comune, gli altri sono null.
- Viddalba: il 2021 non è scritto (solo 332 nel 2025 e +3,11%); il valore implicito 322 rende le somme comunali pari ai totali 4.801 / 4.792 della Tabella 1d.
- Per le fasce: commercio costa (14,99%) e servizi entroterra (28,51%) sono dati solo in %, senza il numero.
- Le schede dell'Allegato I non contengono dati sulle imprese.
- Tutte le quote % comunali scritte nel testo sono riproducibili come settore / totale 2025 (verificato).

## Idee per il sito
- Barre orizzontali delle imprese 2025 per comune (Tempio 1.614 = 33,68%) con freccia della variazione 2021-2025.
- Barre impilate per settore dove disponibili, e treemap della Tabella 1d con variazione colorata (Servizi +6,67%, Industria -11,69%).
- Confronto costa vs entroterra: quota servizi 43,43% vs 28,51%, industria 5,57% vs 10,40%.
