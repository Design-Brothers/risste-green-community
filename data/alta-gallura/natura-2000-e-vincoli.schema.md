# natura-2000-e-vincoli.json

Siti Natura 2000 e altre aree tutelate citati nello studio, habitat prioritari, vincoli ambientali/territoriali, vulnerabilità e sintesi del rischio incendio per l'Unione Alta Gallura. `dati` è un oggetto con sei sezioni.

## Sezioni e campi

### `siti_natura_2000[]` (6 siti)
| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `nome` | string | – | Denominazione come nel testo |
| `tipologia` | string\|null | – | `ZSC`, `ZPS` o null se non specificata (Foci del Coghinas, Isola Rossa – Costa Paradiso) |
| `codice` | null | – | Codice ufficiale ITB…: non riportato nel documento |
| `superficie_ha` | int\|null | ha | Solo Monte Limbara (16588) |
| `comuni_interessati` / `comuni_interessati_nomi` | string[] | – | Comuni associati esplicitamente nel testo ([] se assenti) |
| `descrizione` | string | – | Sintesi fedele |
| `pagine_pdf` | int[] | – | Pagine di citazione |

### `altre_aree_tutelate[]` (1: Area Marina Protetta Capo Testa – Punta Falcone) – stessi campi senza `codice`/`superficie_ha`.

### `habitat_prioritari_citati[]` – `habitat`, `pagine_pdf`.

### `vincoli[]` – `vincolo`, `ambito`, `pagine_pdf` (PPR, fascia costiera 300 m, Natura 2000, PAI, PGRA, vincoli idraulici retrodunali/alluvionali, verifiche vincolistiche preliminari).

### `vulnerabilita[]` – `vulnerabilita`, `ambito`, `pagine_pdf`.

### `rischio_incendio` (oggetto)
| Campo | Tipo | Significato |
|---|---|---|
| `sintesi` | string | Sintesi fedele dei par. 2.2.9 e 4.4.2 |
| `classi_rischio` | null | Il documento non riporta classi/mappe di rischio per Comune |
| `dati_numerici[]` | array | `indicatore`, `valore` (num), `operatore` (`>`, `=`, `circa`), `unita`, `nota`, `pagina_pdf`: intensità di fuoco >1600 kW/m; periodo arido ~99 giorni/anno; deficit idrico 269 mm; piovosità 954,1 mm; surplus 435 mm |
| `pratiche_prevenzione[]` | string[] | Pratiche previste dallo studio |
| `comuni_prioritari_prevenzione_incendi` | object | Ambito 4 dell'Allegato II: 7 Comuni, urgenza "Alto" (pag. 183, 189) |

## Fonte
Parte 1: Seconda parte par. 2.2.1 (pag. 39-40), 2.2.6-2.2.9 (pag. 43-46), 2.3.3 (pag. 48); Terza parte (pag. 56, 58, 63-67); Quarta parte par. 4.4.1-4.4.2 (pag. 75-77); Allegato II (pag. 183, 189, 197, 213).

## Avvertenze
- Nessun codice sito, nessun elenco tabellare dei siti, nessuna superficie protetta totale: i siti sono solo quelli menzionati nel testo.
- I parametri climatici (pag. 48) sono della stazione di Caddau (UGB Limbara Sud, Berchidda), esterna all'Unione.
- Il documento dà una lettura positiva dei vincoli ("dispositivi di governance", "funzione abilitante"): non sono elencati come divieti.

## Idee per il sito
- Mappa con pin/aree dei 6 siti Natura 2000 + AMP, colorati per tipologia (ZSC/ZPS/n.d.).
- Pannello "Rischio incendio": KPI 1600 kW/m, 99 giorni aridi, 269 mm di deficit, con elenco pratiche di prevenzione e Comuni prioritari.
- Timeline/elenco dei vincoli con icone (paesaggio, costa 300 m, Natura 2000, PAI/PGRA).
