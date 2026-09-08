# servizi-ecosistemici-carbon-farming.json

Servizi ecosistemici del territorio, definizione e applicazione delle impronte (Carbon e Water Footprint) e meccanismi di Carbon Farming, generali e per filiera. `dati` è un array di record distinti da `tipo`.

## Campi

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `tipo` | string | – | `servizio_ecosistemico`, `impronta`, `carbon_farming_definizione`, `carbon_farming_pratica`, `carbon_farming_variabile`, `valore_numerico` |
| `nome` | string | – | Denominazione |
| `descrizione` | string | – | Sintesi fedele dal testo |
| `descrizione_fig_4b` | string\|null | – | Didascalia letta nell'infografica Figura 4b |
| `definizione` | string | – | Definizione metodologica (impronte, carbon farming) |
| `unita` | string\|null | – | Unità (es. `t CO2 eq`, `anni`) |
| `applicazione_generale` / `_sughero` / `_bovina` / `_suinicola` | string | – | Applicazione dell'impronta al territorio e alle tre filiere |
| `filiera` | string | – | Per le pratiche: `sughero`, `bovina`, `suinicola` |
| `valore` | number\|null | – | Valore numerico citato (solo `valore_numerico`) |
| `nota` | string | – | Contesto del valore o motivo del `null` |
| `pagina_pdf` / `pagine_pdf` | int / int[] | – | Pagine PDF |

## Fonte
Parte 1: 4.3.2 (pag. 73-74), 4.3.3 (pag. 74), Figura 4b (pag. 75), 4.5.2.2-4.5.2.4 sughero (pag. 82-83), bovina (pag. 85), suinicola (pag. 88), 4.7.3 (pag. 91).

## Avvertenze
- Nessuna quantificazione biofisica o economica nel documento: l'unico numero è la durata minima di 20 anni degli schemi di crediti.
- Il record "Sequestro di carbonio per ettaro" è `null` per esplicitare l'assenza del dato.

## Idee per il sito
- Mappa concettuale interattiva (albero/suolo) che riprende Fig. 4b con tooltip per servizio.
- Schede confronto Carbon vs Water Footprint con le quattro applicazioni (generale + 3 filiere) come tab.
- Elenco pratiche di Carbon Farming filtrabile per filiera.
