# scenari-2035.json

I tre scenari previsionali al 2035 dell'Unione (popolazione, par. 1.6; imprese, par. 1.11) e le stime comunali dell'Allegato I. `dati` = 3 scenari dell'Unione; `dati_comuni` = 11 record comunali con 3 scenari ciascuno.

## Campi (`dati`)

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `scenario` | string | – | `attrattivo`, `lineare`, `crisi` |
| `nome` | string | – | Denominazione nel testo |
| `ipotesi` | string | – | Ipotesi demografiche (sintesi fedele, con rimando alle note del documento) |
| `popolazione_2035` | int | abitanti | Popolazione stimata ("circa") |
| `densita_imprese_pct` | float | % | Densità imprenditoriale ipotizzata (imprese / abitanti x 100) |
| `imprese_2035` | int | imprese | Imprese attive stimate |
| `var_imprese_pct_vs_2025` | float | % | Variazione rispetto alle 4.792 del 2025 |
| `ipotesi_imprese` | string | – | Ipotesi economiche |

## Campi (`dati_comuni`)

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `comune`, `slug`, `fascia` | string | – | Come in popolazione-storica |
| `popolazione_2025` | int | abitanti | Base 1° gennaio 2025 |
| `tasso_medio_annuo_2011_2023` | float | residenti/anno | Variazione media annua 2011-2023 dichiarata nella scheda |
| `scenari[]` | object[] | – | `scenario` (chiave normalizzata), `nome` (originale), `variazione_annua_residenti`, `popolazione_2035` |
| `pagine_pdf` | int[] | – | Pagina della stima |

## Fonte
Parte 1: par. 1.6 e note 1-4 (pag. 24-25); par. 1.11 e note 5-7 (pag. 30-31); Allegato I, paragrafi "Stima sulla Evoluzione della Popolazione Residente al 2035" (pag. 100, 104, 108, 112, 117, 122, 127, 132, 137, 142, 147).

## Avvertenze
- Modello dichiarato: r_com = (P2023 - P2011)/12; P2035 = P2025 + r_com x 10. Imprese 2035 = popolazione x densità.
- I nomi degli scenari comunali variano (es. "Auspicabile / Cauto", "Sviluppo e Attrattività Turistica"): mappati su attrattivo/lineare/crisi conservando il nome originale.
- La somma delle stime comunali non coincide con gli scenari dell'Unione: 35.197 vs 36.500 (attrattivo), 33.473 vs 34.100 (lineare), 32.086 vs 32.400 (crisi).
- L'aritmetica di alcune stime comunali non è riproducibile con il modello dichiarato (es. Aggius lineare 1.216 = 1.411 - 16,25 x 12).
- Tutti i valori sono "circa" nel testo.

## Idee per il sito
- Ventaglio (fan chart) 2001-2035: storico fino al 2025 e tre rami colorati verso 36.500 / 34.100 / 32.400.
- Tabella interattiva imprese 2035 con densità regolabile per spiegare il modello.
- Per comune: tre pallini 2035 su una riga per confrontare l'ampiezza dell'incertezza (Tempio 11.986-12.736).
