# roadmap.json

Roadmap operativa a 36 mesi (Figura 4f + paragrafo 4.7): 4 fasi, 20 azioni numerate con finestre mensili, più le sezioni testuali 4.7.1-4.7.5. `dati` è un array di record distinti da `tipo`.

## Campi

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `tipo` | string | – | `fase`, `azione`, `area_pilota`, `azione_prioritaria_baseline`, `governance_futura`, `contratto_filiera_ulteriore`, `living_lab_replicabilita` |
| `numero` | int | – | Numero di fase (1-4) o di azione (1-20) |
| `nome` / `titolo` | string | – | Denominazione (titolo azione trascritto dall'infografica) |
| `mese_inizio`, `mese_fine` | int | mese (M1-M36) | Finestra temporale letta dalle etichette dell'infografica |
| `prosegue_oltre_m36` | bool | – | Freccia "FUTURE" nell'infografica (Fase 4) |
| `fase` | int | – | Fase di appartenenza dell'azione |
| `area_pilota_comuni` | string[]\|null | – | Slug dei comuni interessati, se indicati |
| `area_pilota_nota` | string | – | Nota quando i comuni non sono nominati |
| `responsabile` | string\|null | – | Soggetto esplicito nel testo, altrimenti null |
| `output_atteso` | string | – | Output ricavato dal testo di 4.7 |
| `numerazione_implicita` | bool | – | true per le azioni 1-5 (non numerate nell'infografica) |
| `obiettivo`, `paragrafo_testo`, `fonte` | string | – | Per le fasi: obiettivo sintetico, paragrafo di riferimento, provenienza (`fig-4f`, `fig-4f + testo`) |
| `sezione`, `ordine`, `ambito`, `comuni`, `comuni_seconda_battuta`, `descrizione` | vari | – | Per i record testuali 4.7.1-4.7.5 |
| `azione_roadmap` | int | – | Numero dell'azione dell'infografica corrispondente al record testuale |
| `valore_numerico` | object\|null | – | Es. `{durata_minima_anni: 20}` |
| `pagine_pdf` | int[] | – | Pagine PDF |

## Fonte
Parte 1: 4.7 (pag. 89), 4.7.1 (pag. 89-90), 4.7.2 (pag. 90-91), 4.7.3 (pag. 91), 4.7.4 (pag. 91), 4.7.5 (pag. 91-92); Figura 4f (pag. 90).

## Avvertenze
- Mesi e numerazione esistono solo nell'infografica; gli output attesi solo nel testo: l'accoppiamento è redazionale.
- Azioni 1-5 numerate per deduzione (la Fase 2 parte dal 6).
- Asse mesi dell'infografica con 11 colonne/anno (artefatto grafico).
- "Tredici Comuni" a pag. 89 vs 11 comuni dell'Unione: refuso della fonte.
- "CA-TE-LU-AG-LU" interpretato come Calangianus, Tempio Pausania, Luras, Aggius, Luogosanto.

## Idee per il sito
- Diagramma di Gantt interattivo (36 mesi, 4 fasi colorate, 20 barre) con tooltip output/comuni.
- Mappa delle aree pilota con layer per ambito (sugherete, mosaico, suini, incendi, suolo).
- Timeline "cosa succede nell'anno 1/2/3" per il pubblico non tecnico.
