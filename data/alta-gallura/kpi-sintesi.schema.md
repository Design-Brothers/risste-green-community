# kpi-sintesi.json

Sedici numeri "da titolo" per la landing page, tutti a livello di Unione (o di fascia dove indicato), con etichetta breve, unità, frase di contesto (max 20 parole) e pagina PDF di provenienza.

## Campi

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `chiave` | string | – | Identificatore snake_case (es. `popolazione_2025`, `indice_vecchiaia_2025`) |
| `etichetta` | string | – | Etichetta breve da mostrare sopra il numero |
| `valore` | number | vedi `unita` | Valore come scritto nel documento (percentuali come numeri, es. -4.02) |
| `unita` | string | – | abitanti, %, unità, persone, anni, imprese, "anziani per 100 giovani", "imprese per 1.000 abitanti" |
| `contesto` | string | – | Frase di contesto (max 20 parole), sintesi non letterale |
| `pagina_pdf` | int | – | Pagina PDF della fonte del valore |

## Fonte
Parte 1, cap. 1 (pag. 21-25, 28, 30). Il dettaglio comunale citato nei contesti (es. IV Trinità 368,3) proviene dall'Allegato I.

## Avvertenze
- Le percentuali negative sono valori numerici con segno (es. `-4.02`).
- `costa_var_pct_2001_2025` è l'unico KPI a livello di fascia.
- I KPI derivano dai dataset dettagliati (popolazione-storica, saldi-demografici, struttura-eta, famiglie, stranieri-e-scuola, imprese, scenari-2035): per approfondimenti collegare i rispettivi file.

## Idee per il sito
- Griglia di KPI card nella hero della landing (4x4 o carosello), con il contesto in tooltip.
- Contatore animato per popolazione, imprese e stranieri.
- Sezione "due velocità" con la coppia costa +14,0% / entroterra -10,1%.
