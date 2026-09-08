# uso-suolo-comuni.json / .csv

Principali classi di uso del suolo (CORINE Land Cover, Carta dell'Uso del Suolo della Sardegna 2008) per ciascuno degli 11 Comuni dell'Unione Alta Gallura, con superficie in ettari e incidenza percentuale sul territorio comunale, più la superficie delle sugherete per Comune. `dati` contiene 74 righe: 66 righe da tabella (6 classi × 11 Comuni) + 8 righe "Sugherete" da testo per i Comuni in cui le sugherete non rientrano tra le prime 6 classi. Il JSON ha inoltre il blocco `sugherete_per_comune` (11 righe).

## Campi (`dati` e CSV)

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `comune` | string | – | Nome come nel documento |
| `slug` | string | – | Identificatore kebab-case (`aggius`, …, `trinita-d-agultu-e-vignola`) |
| `classe_uso_suolo` | string | – | Etichetta della classe come nella scheda (es. `Prati artificiali`, `Sugherete`) |
| `rango` | int\|null | – | Posizione nella tabella della scheda (1 = classe più estesa); null per righe da testo |
| `superficie_ha` | int | ha | Superficie della classe nel Comune (area risultante dall'intersezione GIS) |
| `incidenza_pct` | float\|null | % | Percentuale sul territorio comunale; null per righe da testo |
| `origine` | string | – | `tabella` (tabella "Sintesi dell'uso del suolo") o `testo` (superficie delle sugherete citata nel testo, "circa N ha") |
| `pagina_pdf` | int | – | Pagina PDF della riga |
| `nota` | string\|null | – | Citazione/avvertenza (solo righe da testo) |

## Blocco `sugherete_per_comune` (solo JSON)

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `comune`, `slug` | string | – | Comune |
| `superficie_ha` | int | ha | Sugherete: 574 Aggius, 321 Aglientu, 0 Badesi, 116 Bortigiadas, 2014 Calangianus, 449 Luogosanto, 645 Luras, 0 Santa Teresa Gallura, 1937 Tempio Pausania, 211 Trinità, 52 Viddalba |
| `incidenza_pct` | float\|null | % | Solo dove le sugherete sono in tabella (Aggius 6,9; Calangianus 15,9; Tempio 9,1) |
| `origine` | string | – | `tabella` / `testo` |
| `pagina_pdf`, `nota` | – | – | Riferimento e chiarimento (per i due valori 0 il documento dichiara che le tabelle non riportano sugherete) |

## Fonte
Parte 1, Allegato II – Schede comunali preliminari, par. "Sintesi dell'uso del suolo" (pag. 156-171); metodologia GIS pag. 149-155 (CSV grezzi `tables/p156-t0`, `p158-t0`, `p159-t0`, `p161-t0`, `p162-t0`, `p163-t1`+`p164-t0`, `p165-t0`, `p166-t0`, `p168-t0`, `p169-t0`, `p170-t1`+`p171-t0`).

## Avvertenze
- Solo le prime 6 classi per Comune: le percentuali non sommano a 100 e l'elenco completo non è pubblicato (le tabelle finali dell'Allegato II, pag. 173-219, contengono vocazioni/ambiti/roadmap, non tabelle estese).
- La superficie comunale totale non è riportata: nessun campo la contiene. Il rapporto ha/% dà un valore indicativo (le righe di ogni Comune sono coerenti entro il 3%).
- La superficie di riferimento è l'area comunale risultante dall'intersezione dei tre layer GIS, che esclude piccole porzioni costiere non coincidenti (pag. 151-152, 155).
- Etichette variabili per la stessa classe: "Seminativi in aree non irrigue" (Calangianus, Luras) vs "Seminativi non irrigui" (Tempio).
- Le percentuali dell'uso del suolo di Luogosanto e Viddalba sono spezzate su due pagine nel PDF (pag. 163-164, 170-171).

## Idee per il sito
- Barre orizzontali impilate per Comune (6 classi + "altro" residuo non dettagliato, indicato come tale).
- Mappa/KPI "ettari di sugherete per Comune" con evidenza di Calangianus e Tempio (oltre il 60% del totale comunale pubblicato).
- Filtro per classe (es. "Macchia mediterranea") con confronto tra Comuni in ha e %.
