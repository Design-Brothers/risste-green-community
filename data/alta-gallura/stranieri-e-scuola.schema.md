# stranieri-e-scuola.json

Per ciascun comune: stranieri residenti al 1° gennaio 2025, incidenza % sui residenti, provenienza per continente e principali paesi; utenza scolastica potenziale 0-18 anni al 1° gennaio 2025 per ciclo scolastico e per singola età. 11 record comunali + 1 riga `TOTALE ALTA GALLURA` (solo totali).

## Campi

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `comune`, `slug`, `fascia` | string | – | Come in popolazione-storica |
| `stranieri_2025` | int | persone | Residenti stranieri al 1° gennaio 2025 |
| `stranieri_pct` | float | % | Incidenza sul totale dei residenti |
| `provenienza_continenti[]` | object[] | – | `area` (Europa, Africa, Asia, America, Oceania), `quota_pct` (% sul totale stranieri), eventuale `paesi` (stringa) |
| `principali_paesi[]` | object[] | – | `paese`, `quota_pct` (% sul totale stranieri) |
| `note_stranieri` | string\|null | – | Valori assoluti citati (es. Romania 288 a Santa Teresa), genere a Trinità |
| `utenza_scolastica_0_18` | int | persone | Residenti 0-18 anni (totale dichiarato nel testo) |
| `cicli_scolastici[]` | object[] | – | `ciclo` (asilo_nido_0_2, infanzia_3_5, primaria_6_10, secondaria_i_11_13, secondaria_ii_14_18), `etichetta`, `alunni` |
| `coorti_per_eta[]` | object[] | – | `eta` 0..18, `alunni`, eventuale `stranieri_pct` (quota di stranieri nella coorte, dove indicata) |
| `note_scuola` | string\|null | – | Incoerenze e annotazioni della tabella |
| `pagine_pdf` | int[] | – | Pagine PDF |

## Fonte
Allegato I, paragrafi "Popolazione Straniera" e tabelle "Ciclo Scolastico" delle schede (pag. 98-146); Parte 1 par. 1.5 (pag. 24), 1.7.3 e 1.7.4 (pag. 26-27).

## Avvertenze
- Somma stranieri comunali = 2.151 (par. 1.5); costa 1.213 / entroterra 938 (par. 1.7.3): coerente.
- **Calangianus**: tabella totale 476 (cicli coerenti) ma il testo dice 466 in tre punti; il totale Unione 4.295 torna solo con 466, qui adottato.
- Santa Teresa: primaria 166 vs coorti 164. Bortigiadas: secondaria II 22 vs coorti 26.
- Tabella 1c attribuisce 1.177 ragazzi alla costa e 3.118 all'entroterra; dalle schede risultano 1.167 e 3.128.
- Per Aggius le aree di provenienza includono l'elenco dei paesi senza quote individuali.

## Idee per il sito
- Mappa a bolle: dimensione = stranieri, colore = incidenza % (da 1,6% Aggius a 18,8% Trinità).
- Grafico a torta/treemap per comune della provenienza per continente con i paesi principali.
- Piramide/istogramma 0-18 per comune con evidenza delle coorti a forte presenza straniera (Tempio: 46,3% a 3 anni).
