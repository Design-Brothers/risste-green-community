# filiere.json

Le tre filiere della Green community Alta Gallura e il Contratto di Filiera come strumento trasversale. `dati` contiene 3 record `tipo` = `filiera` e 1 record `tipo` = `contratto_di_filiera`.

## Campi (record `filiera`)

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `nome`, `slug` | string | – | Denominazione e identificatore kebab-case |
| `descrizione` | string | – | Sintesi fedele in 3-4 frasi |
| `fasi_gestione` / `criteri_sostenibilita` / `parametri_compatibilita` | string[] | – | Elenchi puntati propri di ciascuna filiera (rispettivamente sughero, bovina, suinicola) |
| `attori_segmenti` | string[] | – | Attori e segmenti della catena del valore (ricavati da testo e infografiche) |
| `parametri_esg_monitorati` | object | – | `ambientali`, `sociali`, `governance`: string[] |
| `water_footprint`, `carbon_footprint`, `carbon_farming` | string | – | Sintesi delle applicazioni per filiera |
| `prodotti_sbocchi` | string[] | – | Prodotti e mercati di sbocco |
| `comuni_prioritari` | string[]\|null | – | Slug dei comuni prioritari (null se non indicati) |
| `comuni_prioritari_nota` | string | – | Provenienza/limiti dell'informazione |
| `criticita` | string[] | – | Criticità esplicitate nel testo |
| `figura` | string | – | File immagine in `source/.../images/` |
| `pagine_pdf` | int[] | – | Pagine PDF |

## Campi (record `contratto_di_filiera`)
`cos_e`, `come_si_applica` (string), `strumenti_finanziari` (string[]), `progettualita_citate` (array di {nome, descrizione}), `estensioni_previste_4_7_4` (string[]), `pagine_pdf`.

## Fonte
Parte 1: 4.5 (pag. 78-79), 4.5.1 (pag. 79-80), 4.5.2 (pag. 80-83), 4.5.3 (pag. 83-85), 4.5.4 (pag. 86-88), 4.7.4 (pag. 91); Figure 4c (pag. 81), 4d (pag. 84), 4e (pag. 87).

## Avvertenze
- Attori/segmenti e criticità sono ricostruiti dal testo, non da elenchi formali.
- Nessun importo per i fondi dei Contratti di Filiera.
- Filiera bovina senza comuni prioritari nel documento.

## Idee per il sito
- Tre pagine-filiera con schema (riproduzione delle Fig. 4c/4d/4e) e tab ESG / Water / Carbon / Carbon Farming.
- Mappa dei comuni prioritari colorata per filiera.
- Box "Contratto di Filiera" con le progettualità citate e le estensioni previste.
