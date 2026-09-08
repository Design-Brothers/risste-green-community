# sintesi-comparativa-comuni.json / .csv

Tabella "Sintesi comparativa preliminare" (pag. 172): giudizi qualitativi per gli 11 Comuni su vocazione sughericola, interesse suinicolo agroforestale, fragilità pedologica e priorità di approfondimento. Il JSON aggiunge `gruppi_funzionali` (i 4 gruppi della "Lettura conclusiva preliminare", pag. 172) e `quadro_vocazioni_territoriali` (tabella delle 8 vocazioni prevalenti, pag. 178).

## Campi (`dati` e CSV)

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `comune` | string | – | Nome come nel documento |
| `slug` | string | – | Identificatore kebab-case |
| `vocazione_sughericola` | string | – | `Alta`, `Medio-alta`, `Media`, `Medio-bassa`, `Bassa` |
| `interesse_suinicolo_agroforestale` | string | – | Giudizio con qualificatore (es. `Medio, solo pilota`, `Medio-alta da verificare`, `Bassa/localizzata`) |
| `fragilita_pedologica` | string | – | `Alta`, `Medio-alta`, `Media` |
| `priorita_approfondimento` | string | – | `Molto alta`, `Alta`, `Media`, `Media, soprattutto commerciale` |

## Blocco `gruppi_funzionali` (solo JSON)

| Campo | Tipo | Significato |
|---|---|---|
| `gruppo` | string | Nome del gruppo (4: prioritari bosco-sughero; agroforestali integrabili; funzione ambientale/paesaggistica/commerciale; attenzione forestale/protettiva) |
| `comuni` / `comuni_nomi` | string[] | Comuni citati pienamente |
| `comuni_parziali` / `comuni_parziali_nomi` | string[] | Comuni citati "in parte" |
| `descrizione` | string | Testo fedele |
| `pagina_pdf` | int | 172 |

## Blocco `quadro_vocazioni_territoriali` (solo JSON)

`vocazione_prevalente`, `comuni_testo` (cella originale), `comuni`/`comuni_nomi` (slug/nome, inclusi quelli "parti di"), `ruolo_preliminare`, `pagina_pdf` (178).

## Fonte
Parte 1, Allegato II: "Sintesi comparativa preliminare" e "Lettura conclusiva preliminare" (pag. 172; CSV grezzo `tables/p172-t0.csv`), "Quadro sintetico delle vocazioni territoriali" (pag. 178; `tables/p178-t0.csv`).

## Avvertenze
- Scala qualitativa, non graduatoria: il documento avverte che la matrice "non deve essere interpretata come una graduatoria definitiva" e che per il suino "nessun Comune va dichiarato idoneo in modo definitivo".
- Ricomposte le forme spezzate dall'estrazione ("Medio- bassa" → "Medio-bassa").
- Un Comune può stare in più gruppi funzionali (Aggius in 3).
- Lieve differenza tra pag. 172 (prioritari bosco-sughero: Calangianus, Tempio, poi Luras e Aggius) e pag. 178-179 (Luogosanto incluso tra i Comuni sughericoli integrati / Ambito 1).

## Idee per il sito
- Tabella a semaforo (colori per livello) ordinabile per colonna.
- Mappa dei Comuni colorata per `vocazione_sughericola`, con toggle su `fragilita_pedologica`.
- Diagramma a insiemi/chip dei 4 gruppi funzionali con i Comuni condivisi evidenziati.
