# Dataset della parte progettuale – Green community UCAG 193 (Parte 1)

Dataset curati che strutturano la **parte progettuale** dello studio RISSTE "Green community UCAG 193 – Strategie territoriali integrate" (Parte 1): framework Green community, governance, ESG, filiere, strumenti di valorizzazione, roadmap, formazione, output attesi. Seguono `data/CONVENZIONI.md` (struttura `titolo/fonte/note/dati`, chiavi `snake_case`, slug dei comuni, `null` + nota per i dati mancanti). Ogni `nome.json` ha il suo `nome.schema.md`.

Fonti: `source/parte1-green-community-alta-gallura/capitoli/05-parte4-prospettive-green-communities.md` (pag. 69-92), `03-parte2-ambiente-territorio.md` par. 2.3 (pag. 46-52), `01-premessa-e-quadro-metodologico.md` (pag. 13-20), infografiche in `source/parte1-green-community-alta-gallura/images/` (fig-2a, fig-4a … fig-4f), CSV `tables/p051-t0.csv` (Tabella 2b).

## File

| File | Contenuto | Fonte principale |
|---|---|---|
| `obiettivi-studio.json` | Finalità, 3 obiettivi strategici, 4 obiettivi operativi, destinatari, gruppo di lavoro (5 componenti con ruoli) | Premessa ii-iii, Quadro metodologico vii (pag. 14, 18-19) |
| `framework-green-community.json` | 6 pilastri del modello territoriale integrato (Fig. 2a / 4a), 3 dimensioni ESG con priorità di Fig. 4a, 8 organi/strumenti di governance con stato (esistente/proposto) | 4.1, 4.2, 4.3, 4.7.3, 4.7.5; Fig. 2a, 4a |
| `indicatori-esg.json` | 56 indicatori KPI per dimensione E/S/G e filiera (trasversale / sughero / bovina / suinicola) | 4.3.1, 4.5, paragrafi di monitoraggio delle filiere |
| `servizi-ecosistemici-carbon-farming.json` | 9 servizi ecosistemici, Carbon e Water Footprint (definizione + 4 applicazioni), Carbon Farming (definizione, 7 pratiche, 5 variabili), valori numerici | 4.3.2, 4.3.3, 4.5.2.x; Fig. 4b |
| `filiere.json` | 3 filiere (bosco-sughero, bovina estensiva, suinicola agroforestale controllata) + Contratto di Filiera | 4.5-4.5.4; Fig. 4c, 4d, 4e |
| `strumenti-valorizzazione.json` | Habitat/Natura 2000, vulnerabilità e rischio incendio, uso del suolo: approccio, obiettivi, azioni, strumenti | 4.4.1-4.4.3 |
| `roadmap.json` | 4 fasi, 20 azioni con mesi M1-M36, aree pilota (4.7.1), azioni prioritarie (4.7.2), governance futura (4.7.3), ulteriori contratti di filiera (4.7.4), Living Lab e replicabilità (4.7.5) | 4.7; Fig. 4f |
| `formazione-e-professioni.json` | Tabella 2b (8 profili regionali con EQF e codice), 14 nuove professionalità su 3 livelli, 3 istituzioni formative, Living Lab (2.3.2), ricerca applicata (2.3.3) con 13 valori numerici | 2.3.2-2.3.5, Tabella 2b |
| `output-attesi.json` | SIT/GIS (unico output del 4.6) + 11 output nominati altrove nella Parte 4 | 4.6 e Parte 4 |

## Cosa proviene solo dalle infografiche

- **Nomi dei pilastri** del framework (Piattaforma di governance, Poli dell'entroterra, Gateway costieri, Infrastruttura verde d'area) e l'inclusione di Trinità d'Agultu tra i gateway: Fig. 2a.
- **Priorità E/S/G** (tre per dimensione), tecnologie della piattaforma dati (PAI, PFP, FlamMap, Tobler Algorithm, DTM) e interoperabilità UCAG-AGRIS-Forestas: Fig. 4a.
- **Didascalie dei servizi ecosistemici** (intercettazione/ritenzione/infiltrazione, ecc.): Fig. 4b.
- **Fasi, numerazione 1-20 e finestre mensili** della roadmap: Fig. 4f. Il testo di 4.7 non riporta né mesi né numeri; i titoli delle azioni sono trascritti dall'infografica, gli output attesi dal testo.

## Avvertenze generali

- Il documento è una **proposta metodologica preliminare**: indicatori, impronte e Carbon Farming sono definiti qualitativamente; non esistono target, baseline, t CO2/ha, importi finanziari. I campi `unita`, `fonte_dato`, `responsabile`, `ore` sono quasi sempre `null` con nota.
- Le azioni 1-5 della roadmap non sono numerate nell'infografica: numerazione dedotta (la Fase 2 inizia dal 6). L'asse dei mesi mostra 11 colonne per anno (artefatto grafico).
- Refuso della fonte: 4.7 (pag. 89) parla di "tredici Comuni dell'Unione", l'Unione conta 11 comuni.
- Numerazione duplicata nella fonte: i sottoparagrafi di monitoraggio delle filiere bovina e suinicola sono tutti "4.5.2.1-4.5.2.4"; si cita la pagina.
- La sigla "CA-TE-LU-AG-LU" (azione 6) è interpretata come Calangianus, Tempio Pausania, Luras, Aggius, Luogosanto, coerentemente con 4.7.1.
- Scomposizioni in punti (obiettivi, azioni/strumenti, attori di filiera, categorie degli output) sono redazionali su testo discorsivo; le formulazioni restano quelle del documento.
- I dati climatici in `formazione-e-professioni.json` riguardano la stazione di Caddau e l'UGB Limbara Sud (Berchidda, fuori dall'Unione).
