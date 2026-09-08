# formazione-e-professioni.json

Profili di qualificazione professionale regionali (Tabella 2b), nuove professionalità territoriali su tre livelli (2.3.5), istituzioni formative (2.3.4), Living Lab (2.3.2) e ricerca applicata (2.3.3) in sintesi. `dati` è un array di record distinti da `tipo`.

## Campi

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `tipo` | string | – | `profilo_tabella_2b`, `nuova_professionalita`, `istituzione_formativa`, `living_lab`, `ricerca_applicata` |
| `eqf` | int | livello EQF | Livello del Quadro europeo delle qualifiche (Tabella 2b) |
| `codice` | string | – | Codice del Repertorio regionale, come nel documento |
| `profilo` | string | – | Denominazione del profilo |
| `settore_complessita`, `contesto_esercizio`, `descrizione_competenze` | string | – | Colonne della Tabella 2b |
| `ore` | null | ore | Non indicate nel documento |
| `livello`, `livello_nome` | int, string | – | Livello 1-3 della gerarchia di 2.3.5 |
| `descrizione` | string | – | Sintesi del ruolo |
| `in_tabella_2b`, `codice_tabella_2b` | bool, string\|null | – | Corrispondenza con un profilo della Tabella 2b |
| `nome`, `livello`, `sede` | string | – | Istituzione formativa; `sede` slug del comune se indicato |
| `definizione`, `esperienze_citate` | string, array | – | Living Lab |
| `sintesi`, `soggetti`, `dati_numerici_citati` | string, string[], array {nome, valore, unita, nota} | – | Ricerca applicata; valori numerici come nel testo |
| `pagina_pdf` / `pagine_pdf` | int / int[] | – | Pagine PDF |

## Fonte
Parte 1: 2.3.2 (pag. 47), 2.3.3 (pag. 47-49), 2.3.4 (pag. 49), 2.3.5 (pag. 49-50), Tabella 2b (pag. 51; CSV `source/parte1-green-community-alta-gallura/tables/p051-t0.csv`).

## Avvertenze
- Nessuna indicazione di ore di formazione.
- I dati climatici e forestali di 2.3.3 si riferiscono alla stazione di Caddau e all'UGB Limbara Sud (Berchidda, esterno all'Unione).
- "Operatori zootecnici e agro-pastorali" citati genericamente, senza codice regionale.

## Idee per il sito
- Piramide delle professionalità su 3 livelli con badge EQF per i profili codificati.
- Tabella 2b filtrabile per EQF/settore con link a `indicatori-esg.json` (formazione scorzini).
- Infografica clima del Limbara (pioggia mensile, deficit/surplus idrico, 99 giorni di aridità).
