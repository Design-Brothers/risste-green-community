# famiglie.json

Numero di famiglie e numero medio di componenti per famiglia nel 2003, 2011, 2023 e 2024 per ciascun comune (serie annidata) più una riga `TOTALE ALTA GALLURA`. 12 record.

## Campi

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `comune`, `slug`, `fascia` | string | – | Come in popolazione-storica |
| `serie[]` | object[] | – | Un elemento per anno |
| `serie[].anno` | int | – | 2003, 2011, 2023, 2024 |
| `serie[].numero_famiglie` | int\|null | famiglie | Nuclei familiari residenti |
| `serie[].componenti_medi` | float\|null | persone/famiglia | Numero medio di componenti |
| `var_pct_famiglie_2003_2011` | float\|null | % | Variazione % del numero di famiglie 2003-2011, solo dove il testo la cita |
| `var_pct_famiglie_2003_2023` | float | % | Solo riga Unione: +19,41 |
| `note` | string\|null | – | Lacune e precisazioni |
| `pagine_pdf` | int[] | – | Pagine PDF |

## Fonte
Allegato I, tabelle "Anno / Numero Famiglie / Numero Medio Componenti" e testo "Le Famiglie e il Numero Medio dei Componenti" delle schede (pag. 98-144); Parte 1 par. 1.3 (pag. 23) e 1.7.3 (pag. 26).

## Avvertenze
- I valori 2024 provengono dal testo delle schede: Aggius ha solo i componenti medi (2,16); Aglientu nessun valore ("si stabilizza").
- La somma comunale 2003 (13.925) e 2023 (16.628) coincide con il par. 1.3; il totale 2011 (16.258) è una somma delle schede non citata nel testo.
- Il par. 1.7.3 inverte i componenti medi di Badesi e Trinità d'Agultu ("1,76 e 1,97"): dalle schede Badesi = 1,97 e Trinità = 1,76 (2024).
- Il valore 2,09 "nel 2024" del par. 1.3 è riferito alla media dei piccoli comuni costieri, non all'Unione: non inserito.

## Idee per il sito
- Doppio asse per comune: famiglie (barre) in crescita e componenti medi (linea) in calo, 2003 -> 2024.
- Slope chart dei componenti medi 2003 -> 2023 per gli 11 comuni (da 2,87 Calangianus a 1,67 Aglientu).
- KPI "+19,41% famiglie con popolazione in calo".
