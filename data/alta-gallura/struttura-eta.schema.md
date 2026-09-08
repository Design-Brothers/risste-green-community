# struttura-eta.json / .csv

Popolazione per macro-classi di età (0-14, 15-64, 65+) al 1° gennaio 2002, 2011, 2023 e 2025 per ciascun comune (44 record = 11 comuni x 4 anni) più una riga `TOTALE ALTA GALLURA` per il 2025. Gli indicatori derivati sono presenti solo quando il testo li riporta per quell'anno.

## Campi

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `comune`, `slug`, `fascia` | string | – | Come in popolazione-storica |
| `anno` | int | – | 2002, 2011, 2023, 2025 (dato al 1° gennaio) |
| `classe_0_14` | int | persone | Popolazione 0-14 anni (giovanile) |
| `classe_15_64` | int | persone | Popolazione 15-64 anni (attiva) |
| `classe_65_piu` | int | persone | Popolazione 65 anni e oltre |
| `totale` | int | persone | Totale residenti al 1° gennaio (= somma delle tre classi) |
| `quota_0_14_pct`, `quota_15_64_pct`, `quota_65_piu_pct` | float\|null | % | Incidenze % sul totale, come scritte nel testo |
| `indice_vecchiaia` | float\|null | anziani per 100 giovani | 65+ / 0-14 x 100 |
| `indice_dipendenza` | float\|null | non attivi per 100 attivi | (0-14 + 65+) / 15-64 x 100 |
| `eta_media` | float\|null | anni | Età media dei residenti |
| `pagine_pdf` | int[] | – | Pagine PDF |

## Fonte
Allegato I, tabelle "Anno (1° Gen)" e paragrafi "Gli Indici Strutturali ed Età Media" delle schede (pag. 98-145); Parte 1 par. 1.4 (pag. 23-24) per la riga Unione 2025.

## Avvertenze
- I totali 2011 e 2023 sono al 1° gennaio e **non coincidono** con la Tabella 1a (censimento 2011 e 31/12/2023): es. Tempio 14.290 vs 13.936 (2011), Santa Teresa 5.225 vs 5.018, Trinità d'Agultu 2.239 vs 2.351 (2023). I totali 2025 coincidono.
- La somma delle righe comunali 2025 riproduce esattamente i valori dell'Unione del par. 1.4 (3.247 / 22.204 / 9.791) e gli indici 301,54 e 58,72 (verificato).
- Il par. 1.4 cita come massimi dell'indice di vecchiaia Bortigiadas (342) e Aggius/Aglientu (333), ma Trinità d'Agultu ha 368,3 (scheda pag. 141).
- Non inseriti perché fuori griglia annuale: età media Luras 2010 (42,8), indice di vecchiaia Trinità 2010 (197,9), indice di vecchiaia Aglientu 2024 (386,0).
- Le righe 2025 di Badesi e Luogosanto erano spezzate nel Markdown per cambio pagina e sono state ricomposte dal testo.

## Idee per il sito
- Barre impilate 100% (0-14 / 15-64 / 65+) per comune, con slider anno 2002 -> 2025.
- Ranking dell'indice di vecchiaia 2025 (Luras 230,6 -> Trinità 368,3) con linea Unione 301,54.
- Piccoli multipli dell'età media 2002/2011/2025 per comune, evidenziando Trinità d'Agultu che ringiovanisce (49,5 -> 48,2).
