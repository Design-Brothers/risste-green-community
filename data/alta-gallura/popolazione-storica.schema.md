# popolazione-storica.json / .csv

Popolazione residente dei 11 Comuni dell'Unione Alta Gallura nel 2001, 2011, 2023 e 2025, con variazioni assolute e percentuali e la classificazione costa/entroterra usata dallo studio. `dati` contiene 11 record comunali + 1 riga `TOTALE ALTA GALLURA` + 2 righe di fascia (`fascia-costiera`, `fascia-interna`).

## Campi

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `comune` | string | – | Nome come nel documento (o etichetta dell'aggregato) |
| `slug` | string | – | Identificatore kebab-case; aggregati: `totale-alta-gallura`, `fascia-costiera`, `fascia-interna` |
| `fascia` | string | – | `costiera` (Aglientu, Badesi, Santa Teresa Gallura, Trinità d'Agultu e Vignola), `interna` (gli altri 7), `unione` per il totale |
| `abitanti_2001` | int | abitanti | Censimento 2001 |
| `abitanti_2011` | int | abitanti | Censimento 2011 |
| `abitanti_2023` | int | abitanti | Residenti al 31 dicembre 2023 |
| `abitanti_2025` | int | abitanti | Residenti al 1° gennaio 2025 |
| `var_ass_2001_2011` | int | abitanti | Variazione assoluta 2001-2011 (schede Allegato I) |
| `var_ass_2011_2023` | int | abitanti | Variazione assoluta 2011-2023 (schede Allegato I) |
| `var_ass_2001_2023` | int | abitanti | Variazione assoluta 2001-2023 |
| `var_pct_2001_2023` | float\|null | % | Variazione % 2001-2023 (Tab. 1a); null per le righe di fascia (non riportata) |
| `var_pct_2001_2025` | float | % | Solo righe di fascia: +14,0 costa / -10,1 interno (Tab. 1c) |
| `pagine_pdf` | int[] | – | Pagine PDF di provenienza |

Il CSV contiene le stesse righe senza `var_pct_2001_2025` e `pagine_pdf`.

## Fonte
Parte 1: par. 1.1 e Tabella 1a (pag. 21-22); par. 1.7 e Tabella 1c (pag. 25); Allegato I, schede comunali (pag. 97, 101, 105, 109, 113, 118, 123, 128, 133, 138, 143).

## Avvertenze
- Le somme comunali coincidono con i totali della Tabella 1a per tutti gli anni (verificato).
- I valori 2011 e 2023 delle righe di fascia sono somme delle righe comunali (non compaiono nel testo); 2001 e 2025 sono quelli della Tabella 1c.
- Il par. 1.7.1 dice che l'entroterra "ha perso quasi 3.000 abitanti": la differenza 2001-2025 è 2.760.
- Le schede dell'Allegato I chiamano "2024" il dato che la Tabella 1a chiama "2025" (stessa cifra: 31/12/2024 = 1/1/2025).

## Idee per il sito
- Grafico a linee 2001-2025 con selettore comune e confronto costa/entroterra (due colori).
- Mappa coropletica dei comuni colorata per `var_pct_2001_2023` (da -20,43% Bortigiadas a +16,14% Santa Teresa).
- KPI "35.242 residenti" con barra costa 10.616 / entroterra 24.626.
