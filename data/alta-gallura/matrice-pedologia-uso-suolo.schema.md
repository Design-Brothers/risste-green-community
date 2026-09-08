# matrice-pedologia-uso-suolo.json

Le 5 combinazioni principali "classe di uso del suolo su unità pedologica" per ciascuno degli 11 Comuni (55 combinazioni), con superficie e incidenza sul territorio comunale, e la lettura interpretativa della scheda. `dati` è un array di 11 oggetti-Comune.

## Campi

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `comune` | string | – | Nome come nel documento |
| `slug` | string | – | Identificatore kebab-case |
| `pagina_pdf` | int | – | Pagina PDF della tabella |
| `combinazioni[]` | array | – | 5 combinazioni ordinate per superficie |
| `combinazioni[].combinazione` | string | – | Stringa originale (es. `Sugherete su C1`) |
| `combinazioni[].classe_uso_suolo` | string | – | Parte sinistra della combinazione, come scritta |
| `combinazioni[].classe_uso_suolo_normalizzata` | string | – | Dicitura della classe nella tabella di uso del suolo (es. `Boschi misti` → `Boschi misti di conifere e latifoglie`) |
| `combinazioni[].unita_pedologica` | string | – | Codice unità (parte destra) |
| `combinazioni[].rango` | int | – | Posizione 1-5 |
| `combinazioni[].superficie_ha` | int | ha | Superficie della combinazione |
| `combinazioni[].incidenza_pct` | float | % | Percentuale sul territorio comunale |
| `lettura` | string | – | Commento interpretativo fedele della scheda |

## Fonte
Parte 1, Allegato II – Schede comunali preliminari, par. "Lettura della matrice pedologia × uso del suolo" (pag. 156, 158, 160, 161, 163, 164, 165, 167, 168, 170, 171). Tabella completa "Comuni intersezione UdS-Pedologia" descritta a pag. 153 ma non pubblicata.

## Avvertenze
- Solo le top-5 per Comune: la matrice completa non è nel documento.
- Le sugherete compaiono tra le combinazioni solo per Calangianus (Sugherete su C1, 1.166 ha) e Tempio Pausania (Sugherete su C2, 1.370 ha); per Aggius il testo indica che "ricadono soprattutto su C2, C1 e B2" senza cifre.
- Etichette abbreviate rispetto alle tabelle di uso del suolo: vedi `classe_uso_suolo_normalizzata`.

## Idee per il sito
- Heatmap Comune × combinazione (o classe × unità) con intensità = ha.
- Card per Comune: "dove sta la vegetazione" con badge dell'unità fragile (C1) evidenziato.
- Incrocio con `pedologia-comuni.json` per mostrare quanta parte dell'unità dominante è coperta da vegetazione naturale vs prati/seminativi.
