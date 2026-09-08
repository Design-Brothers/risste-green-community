# saldi-demografici.json / .csv

Saldo naturale (nati - morti) e saldo migratorio totale (iscritti - cancellati) cumulati 2002-2023 per ciascun comune, con l'"incidenza prevalente" testuale della scheda, più i totali per asse costiero, asse interno e Unione (Tabella 1b). `dati` = 11 record `livello` = `comune` + 3 record `livello` = `aggregato`.

## Campi

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `comune`, `slug`, `fascia` | string | – | Come in popolazione-storica |
| `livello` | string | – | `comune` o `aggregato` |
| `saldo_naturale_2002_2023` | int\|null | persone | Nati meno morti, cumulato 2002-2023 |
| `saldo_migratorio_2002_2023` | int\|null | persone | Iscritti meno cancellati anagrafici, cumulato 2002-2023 |
| `saldo_migratorio_estero_2004_2023` | int\|null | persone | Saldo con l'estero cumulato 2004-2023; riportato solo per Aggius (+32) |
| `incidenza_prevalente` | string\|null | – | Testo della colonna "Incidenza prevalente" / "Impatto prevalente" |
| `note` | string\|null | – | Dati annuali recenti citati nel testo della scheda (es. Bortigiadas 2024: 0 nati, 13 morti) |
| `pagine_pdf` | int[] | – | Pagine PDF |

## Fonte
Parte 1: par. 1.2 e Tabella 1b (pag. 22-23); Tabella 1c (pag. 25-26); Allegato I, tabelle "Saldo Naturale e Saldo Migratorio Totale" delle schede (pag. 97-139).

## Avvertenze
- **Viddalba**: la scheda non riporta i saldi cumulati; i campi sono null. Per differenza dai totali dell'Asse Interno risulterebbero -218 / +276 (non scritti nel documento).
- Saldo con l'estero disponibile solo per Aggius.
- La tabella dei saldi di Santa Teresa Gallura è estratta in modo frammentato nel Markdown (pag. 128-129); i valori -263 / +1.337 sono confermati dal testo.
- Indicatori derivati del testo: copertura del deficit naturale da parte del saldo migratorio 96,6% (Unione), 29,4% (entroterra); quota costiera del saldo migratorio 77,2%.

## Idee per il sito
- Grafico a barre divergenti per comune: saldo naturale (negativo) vs saldo migratorio, ordinato per popolazione.
- "Bilancia" costa/entroterra: -861/+2.538 contro -2.541/+748.
- KPI con la frase "i flussi migratori coprono il 96,6% del deficit naturale".
