# technology-scouting.json

Sintesi strutturata dell'attività di Technology Scouting: metodologia (par. 2.4-2.6), distribuzione per Paese (Figura 5), per ambito (Figura 6), maturità tecnologica (par. 3.3.3) ed evidenze testuali.

## Struttura

`dati` è un oggetto con sezioni nominate (richiesta esplicita: `per_paese`, `per_ambito`, `per_trl`, evidenze), non una lista.

| campo | tipo | unità | significato |
|---|---|---|---|
| `metodologia.motore_ricerca_principale` | string | – | Google Scholar (pag. 21) |
| `metodologia.tipologie_contributi` | list[string] | – | tipi di documenti inclusi |
| `metodologia.periodo.inizio/fine` | int | anno | 2015-2025 (testo); nota su 2015-2026 (Figura 1) |
| `metodologia.ambiti_query` | list[string] | – | ambiti usati per le parole chiave (pagg. 21-22) |
| `metodologia.procedura` | list[string] | – | fasi di selezione/classificazione (pag. 22) |
| `metodologia.attributi_registrati` | list[string] | – | attributi rilevati per ogni pubblicazione (pag. 23) |
| `metodologia.macro_settori_classificazione` | list[string] | – | macro-settori di raggruppamento (pag. 23) |
| `metodologia.approfondimenti_separati[]` | {tema, pagina_pdf} | – | i due approfondimenti (incendi; certificazioni) non inclusi nel database |
| `n_pubblicazioni.*` | int | pubblicazioni | i vari totali citati (153 vs 166) con pagine |
| `per_paese.valori[]` | {paese, n_pubblicazioni, pct} | pubblicazioni, % | Figura 5; totale 153 |
| `per_paese.quota_portogallo_spagna_italia_pct_didascalia` | float | % | 67,5 (didascalia) |
| `per_paese.quota_portogallo_spagna_italia_pct_calcolata` | float | % | 60,1 = (58+23+11)/153 |
| `per_ambito.valori[]` | {ambito, n_pubblicazioni, pct} | pubblicazioni, % | Figura 6; 12 ambiti, somma 197, % su 153 |
| `per_ambito.didascalia_figura_6_pct` | object | % | percentuali della didascalia, incoerenti (vedi note) |
| `per_trl_documento.valori[]` | {fascia_trl, descrizione, prevalenza, ambiti, n_pubblicazioni=null} | – | descrizione qualitativa di pagg. 32-33 |
| `per_trl_database.valori[]` | {fascia_trl, n_pubblicazioni} | pubblicazioni | **calcolato** dal dataset bibliografico, non dal documento |
| `evidenze[]` | {testo, pagina_pdf} | – | 6 frasi testuali fedeli |

## Fonte

Parte 2, pagg. 21-24 (par. 2.4-2.6), 29-33 (par. 3.3), 38 (par. 4.3); immagini `fig-5-distribuzione-geografica-innovazione.jpeg` (pag. 31) e `fig-6-ambiti-innovazione-sughero.jpeg` (pag. 32).

## Avvertenze

- **153 vs 166**: il documento usa entrambi i numeri; le figure e il database dicono 153. Usare 153 come totale e citare 166 solo con la nota.
- **Figura 6**: attribuzione multipla (somma 197 > 153); le percentuali della didascalia (34,9 / 19,3 / 12,7) non tornano con nessuna base.
- **Figura 5**: 67,5% in didascalia vs 60,1% calcolato dai numeri della stessa figura.
- **TRL**: nel documento è qualitativo; le fasce numeriche vengono dal database (nessun record oltre TRL 8).
- Le distribuzioni per Paese e per ambito calcolate dal database non coincidono esattamente con le figure (vedi `bibliografia-scientifica.schema.md`).

## Idee di rappresentazione

- Mappa Europa/Mediterraneo con bolle proporzionali a `per_paese` (replica della Figura 5) + barre laterali.
- Treemap o barre degli ambiti (Figura 6) con toggle "conteggio / % su 153", avviso sull'attribuzione multipla.
- Timeline della metodologia (fonti → selezione → classificazione → TRL) e badge TRL con le tre fasce qualitative.
