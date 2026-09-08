# framework-green-community.json

Pilastri del modello territoriale integrato della Green community Alta Gallura (da 4.1, Fig. 2a e Fig. 4a), le tre dimensioni ESG (4.3) e il modello di governance con gli organi/strumenti citati (4.2, 4.7.3, 4.7.5). `dati` è un array di record distinti da `tipo`.

## Campi

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `tipo` | string | – | `pilastro`, `dimensione_esg`, `organo_governance` |
| `ordine` | int | – | Ordine di presentazione (pilastri) |
| `nome` | string | – | Denominazione |
| `slug` | string | – | Identificatore kebab-case (pilastri) |
| `sigla` | string | – | E / S / G (dimensioni ESG) |
| `descrizione_breve` | string | – | Sintesi fedele, max 3-4 frasi |
| `elementi` | string[] | – | Elementi costitutivi del pilastro |
| `priorita_fig_4a` | string[] | – | Le tre priorità per dimensione lette dall'infografica di Fig. 4a |
| `comuni` / `comuni_fig_2a` / `comuni_testo_4_5` | string[] | – | Slug dei comuni citati (rispettivamente da Fig. 2a e dal testo di 4.5) |
| `stato` | string | – | Per gli organi: `esistente`, `proposta`, `da rafforzare (proposta)`, ecc., secondo il testo |
| `funzione` | string | – | Funzione attribuita dal documento |
| `fonte_figura` | string\|null | – | Nome file immagine in `source/.../images/` |
| `pagine_pdf` | int[] | – | Pagine PDF di riferimento del record |

## Fonte
Parte 1: 4.1 (pag. 69), 4.2 (pag. 69-70), 4.3 (pag. 70-72), 4.7.3 (pag. 91), 4.7.5 (pag. 91-92); Figura 2a (pag. 35), Figura 4a (pag. 72); Premessa iii (pag. 14).

## Avvertenze
- I nomi dei pilastri sono quelli dell'infografica 2a; il testo 4.1 non li enumera.
- Fig. 2a include Trinità d'Agultu tra i gateway costieri; il testo 4.5 cita Aglientu, Badesi, Santa Teresa Gallura.
- Il documento non dettaglia composizione o regolamento degli organi di governance.

## Idee per il sito
- Diagramma interattivo a 4 blocchi (Unione → Poli entroterra / Gateway costieri → Infrastruttura verde) con hover sugli elementi.
- Tre colonne E/S/G con le priorità di Fig. 4a e link agli indicatori.
- Tabella organi di governance filtrabile per `stato` (esistente vs proposto).
