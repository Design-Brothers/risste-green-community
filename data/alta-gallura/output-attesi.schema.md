# output-attesi.json

Output ambientali e territoriali attesi: il SIT/GIS del paragrafo 4.6 più gli output esplicitamente nominati nel resto della Parte 4 e nella Figura 4a. `dati` è un array di 12 record.

## Campi

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `ordine` | int | – | Ordine di presentazione |
| `slug` | string | – | Identificatore kebab-case |
| `nome` | string | – | Denominazione dell'output |
| `categoria` | string | – | `informativo`, `pianificazione`, `gestionale`, `economico`, `economico-ambientale`, `governance`, `territoriale`, `strategico` (redazionale) |
| `da_paragrafo_4_6` | bool | – | true solo per l'output descritto nel paragrafo 4.6 |
| `descrizione` | string | – | Sintesi fedele |
| `paragrafo` | string | – | Paragrafi/figure di provenienza |
| `pagine_pdf` | int[] | – | Pagine PDF |

## Fonte
Parte 1: 4.6 (pag. 89); 4.3.1, 4.4.3, 4.5.1-4.5.4, 4.7.1-4.7.5 (pag. 72-92); Figura 4a (pag. 72), Figura 4f (pag. 90).

## Avvertenze
- Il paragrafo 4.6 descrive solo il SIT/GIS: gli altri output sono una raccolta redazionale da altri paragrafi.
- Nessun output quantificato.
- Le categorie sono redazionali.

## Idee per il sito
- Griglia di card "Cosa produce la Green community" con filtro per categoria.
- Collegamento output → azione della roadmap (tramite `roadmap.json`).
- Evidenza del SIT/GIS con link all'Allegato II.
