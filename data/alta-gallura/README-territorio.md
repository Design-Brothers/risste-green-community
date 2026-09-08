# Dataset territoriali – Unione dei Comuni dell'Alta Gallura

Dataset curati (uso del suolo, pedologia, vocazioni, aree protette e vincoli) degli 11 Comuni dell'Unione Alta Gallura, estratti dallo studio RISSTE "Green community UCAG 193 – Strategie territoriali integrate" (Parte 1, 2025). Seguono le regole di `data/CONVENZIONI.md`: ogni numero compare nel documento alla pagina PDF indicata; nessuna stima. Fonti principali: Allegato II (pag. 149-219), Seconda parte (pag. 33-52), Terza parte (pag. 53-68).

## File

| File | Contenuto | Record | Fonte (pag. PDF) |
|---|---|---|---|
| `uso-suolo-comuni.json` / `.csv` (+ `.schema.md`) | Prime 6 classi di uso del suolo per Comune (ha, %) + superficie sugherete per Comune | 74 righe (66 da tabella + 8 da testo); blocco `sugherete_per_comune` 11 | 156-171 |
| `pedologia-comuni.json` / `.csv` (+ `.schema.md`) | Unità pedologiche per Comune (ha, %), dizionario di 12 unità, commenti per Comune | 51 righe | 156-171 |
| `matrice-pedologia-uso-suolo.json` (+ `.schema.md`) | Top-5 combinazioni uso del suolo × unità pedologica per Comune, con lettura | 11 Comuni × 5 = 55 combinazioni | 156-171 |
| `sintesi-comparativa-comuni.json` / `.csv` (+ `.schema.md`) | Tabella comparativa (4 giudizi qualitativi), 4 gruppi funzionali, quadro delle 8 vocazioni | 11 righe; 4 gruppi; 8 vocazioni | 172, 178 |
| `schede-comuni.json` (+ `.schema.md`) | Scheda integrata per Comune: Tab. 2a, inquadramento, implicazioni filiere, criticità, opportunità, elementi identitari | 11 schede | 37, 53-68, 156-172 |
| `natura-2000-e-vincoli.json` (+ `.schema.md`) | Siti Natura 2000 (6) e AMP (1), habitat (7), vincoli (9), vulnerabilità (5), rischio incendio (5 dati numerici) | – | 39-46, 56-67, 75-77, 183-213 |
| `superfici-unione.json` (+ `.schema.md`) | Grandezze sovracomunali disponibili (13) e indicatori di Unione non riportati (5, null) | 18 | 39-48, 56 |

Chiave di join tra file: `slug` (`aggius`, `aglientu`, `badesi`, `bortigiadas`, `calangianus`, `luogosanto`, `luras`, `santa-teresa-gallura`, `tempio-pausania`, `trinita-d-agultu-e-vignola`, `viddalba`).

## Avvertenze generali

1. **Dati parziali per costruzione.** Le schede dell'Allegato II pubblicano solo le prime 6 classi di uso del suolo, 4-5 unità pedologiche e 5 combinazioni per Comune. Le tabelle GIS complete ("Comuni intersezione UdS", "UdS-Pedologia", "Pedologia", pag. 153-154) sono descritte ma non riprodotte; le pagine 173-219 contengono vocazioni, ambiti di progettazione, metodo e roadmap, non tabelle estese. Le percentuali di uso del suolo quindi non sommano a 100; quelle pedologiche sommano tra 95,1% (Viddalba) e 100% (Badesi).
2. **Superficie comunale e totali di Unione non riportati.** Il documento non indica la superficie dei Comuni né totali di Unione (superficie, forestale, agricola, sugherete). Il rapporto ha/% delle righe restituisce un valore indicativo coerente entro il 3% per ogni Comune, ma non è stato inserito come dato.
3. **Superficie di riferimento GIS.** Le percentuali sono calcolate sull'area comunale risultante dall'intersezione Comuni × Carta Uso del Suolo 2008 (1:25.000) × Carta dei Suoli (1:250.000), che esclude piccole porzioni costiere non coincidenti fra i layer (pag. 151-152, 155). Scale diverse delle carte: dettaglio non omogeneo.
4. **Sugherete.** Valori per Comune: Calangianus 2.014, Tempio Pausania 1.937, Luras 645, Aggius 574, Luogosanto 449, Aglientu 321, Trinità 211, Bortigiadas 116, Viddalba 52 ha; Badesi e Santa Teresa Gallura 0 (il documento dichiara che le tabelle non riportano sugherete). Solo per Aggius, Calangianus e Tempio le sugherete sono tra le prime 6 classi (con %); gli altri valori sono "circa N ha" nel testo.
5. **Natura preliminare.** Tutti i giudizi (vocazione, interesse suinicolo, fragilità, priorità) sono dichiarati dallo studio come orientativi, non idoneità né graduatorie; per la filiera suinicola "nessun Comune va dichiarato idoneo in modo definitivo" (pag. 172).
6. **Siti Natura 2000 senza codici.** Il documento non riporta codici ITB, superfici (eccetto Monte Limbara 16.588 ha) né un elenco tabellare; sono censiti solo i siti nominati nel testo. Nessuna classe di rischio incendio per Comune.

## Incoerenze e ambiguità rilevate nella fonte

- **Bortigiadas / Aggius, narrativa vs GIS**: la Terza parte descrive Bortigiadas con "sugherete, leccete e macchia mediterranea evoluta [che] occupano la maggior parte della superficie comunale" (pag. 59) e Aggius "dominato da sugherete, leccete e macchia" (pag. 54), mentre le tabelle GIS danno 116 ha di sugherete a Bortigiadas (circa 1,5%) e 6,9% ad Aggius.
- **Gruppi prioritari bosco-sughero**: pag. 172 cita "Calangianus e Tempio Pausania, seguiti da Luras e Aggius"; pag. 173-174, 178 e 179 includono anche Luogosanto tra i Comuni "sughericoli integrati" / Ambito 1.
- **Fragilità pedologica di Badesi, Santa Teresa Gallura e Trinità**: compare solo nella tabella di pag. 172 (Media, Medio-alta, Medio-alta); le rispettive schede non esplicitano il giudizio nella valutazione preliminare.
- **Etichette non uniformi**: "Seminativi in aree non irrigue" (Calangianus, Luras) vs "Seminativi non irrigui" (Tempio); nelle combinazioni della matrice le classi sono abbreviate ("Seminativi", "Boschi misti", "Pascolo naturale"). Nomi: "Santa Teresa di Gallura" nel titolo del par. 3.8 vs "Santa Teresa Gallura" altrove; "Comuna di Trinità" (refuso, pag. 65).
- **Tab. 2a**: la cella tipologia di "Aglientu – Badesi" riporta "Costa Interfaccia entroterra-costa" (probabile fusione di due valori); resa come "Costa / Interfaccia entroterra-costa".
- **Unità pedologiche non descritte**: B3 (Aggius), G1 (Bortigiadas), I1 (Aglientu, Bortigiadas, Trinità) sono elencate senza descrizione; le descrizioni delle altre unità sono ricavate dai commenti delle schede, non dalla legenda ufficiale della Carta dei Suoli.
- **Distretto forestale vs Unione**: il Distretto 01 "Alta Gallura" (150.251 ha) non coincide con il territorio dell'Unione (Limbara Sud di Tempio nel Distretto 04); i parametri climatici e l'UGB Limbara Sud (3.630,1 ha) sono riferiti a Berchidda, esterna all'Unione.
- **Estrazione PDF**: categorie spezzate ("Medio- bassa", "bassomedio", "medioalta") ricomposte; numerazione mancante del par. 7.4 (Luras) e tabelle spezzate su due pagine (Luogosanto pag. 163-164, Viddalba pag. 170-171) gestite senza perdita di righe.

## Verifiche effettuate
- Tutti i valori confrontati con i CSV grezzi `source/parte1-green-community-alta-gallura/tables/p156…p172` (coincidenti).
- Coerenza ha/%: per ogni Comune la superficie comunale implicita dalle diverse righe varia meno del 3%.
- JSON validi (UTF-8, indentazione 2 spazi), CSV con header e virgola.
