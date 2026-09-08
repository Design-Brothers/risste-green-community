---
slug: /sughero-sardegna/innovazione
sezione: sughero-sardegna
eyebrow: "Sughero Sardegna · Innovazione"
title: "L'innovazione del sughero e un modello per decidere"
seo_title: "Innovazione del sughero e modello S.U.G.H.E.R.A. – Sardegna"
description: "Technology scouting su 153 pubblicazioni, 9 direttrici, certificazioni, database bibliografico e il framework S.U.G.H.E.R.A. per la filiera del sughero sarda."
og_image: source/parte2-filiera-sughero-sardegna/images/fig-6-ambiti-innovazione-sughero.jpeg
ancore:                                  # id delle sezioni raggiungibili con /sughero-sardegna/innovazione#…
  - ricerca
  - ambiti
  - trl
  - direttrici
  - certificazioni
  - database
  - sughera
  - conclusioni
fonti:
  - documento: parte2
    pagine: [9, 17, 20, 21, 22, 23, 24, 29, 30, 31, 32, 33, 34, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 142, 194]
dati:
  - sughero-sardegna/technology-scouting.json
  - sughero-sardegna/direttrici-innovazione.json
  - sughero-sardegna/strumenti-certificazione.json
  - sughero-sardegna/bibliografia-scientifica.json
  - sughero-sardegna/framework-sughera.json
  - sughero-sardegna/conclusioni.json
  - sughero-sardegna/sintesi-regionale.json
figure:
  - parte2-filiera-sughero-sardegna/images/fig-5-distribuzione-geografica-innovazione.jpeg
  - parte2-filiera-sughero-sardegna/images/fig-6-ambiti-innovazione-sughero.jpeg
  - parte2-filiera-sughero-sardegna/images/fig-7-framework-sughera.jpeg
---

**Ancore:** `#ricerca` → "Come è stata costruita la mappa dell'innovazione" · `#ambiti` → "Compositi ed edilizia guidano…" · `#trl` → "Tecnologie mature e filoni emergenti convivono" · `#direttrici` → "Nove direttrici di innovazione" · `#certificazioni` → "Undici strumenti, dalla foresta al prodotto" · `#database` → "Il database: 153 pubblicazioni da esplorare" · `#sughera` → "S.U.G.H.E.R.A.: un modello in sette passaggi" · `#conclusioni` → "Le conclusioni dello studio in otto messaggi".

<!-- Pagina unica: fonde i v1 09-sughero-innovazione e 10-sughero-framework. Ordine: Paese → ambiti → TRL → direttrici → certificazioni → database → S.U.G.H.E.R.A. → conclusioni. -->
<!-- Pagine citate (P2 p.N) = pagine fisiche del PDF della Parte 2; la numerazione stampata è inferiore di 17. -->
<!-- Regola dati: il totale delle pubblicazioni è 153 (Allegato II, Figure 5-6). Il numero 166 compare in un passaggio del testo e si cita solo con la nota. -->

## Hero {type=hero}
**Standfirst:** La ricerca internazionale porta il sughero nei compositi, nell'edilizia, nel biomedicale e nell'economia circolare. Lo studio ha censito 153 pubblicazioni e ne ricava nove direttrici per la Sardegna. Poi riunisce indici, certificazioni e innovazione in un modello per decidere: S.U.G.H.E.R.A.
**CTA:** Consulta il database bibliografico → /sughero-sardegna/innovazione#database

## Illustrazione di apertura {type=visual}
<!-- Scelta: anelli con micro-etichette agganciate (più leggibile dell'alternativa "orbo che si divide in 12 ambiti"). Numeri da technology-scouting.json → per_paese, per_ambito. -->
**Elemento:** `DecorticaRings` tone `cork` (`--cork` → `--cork-light`), 12 anelli, 520 px, a destra del titolo, opacità 0,4 e grana 8 %. Cinque `MicroLabel` agganciate agli anelli da linee sottili (`--line`, 1 px, lunghe 40-80 px). Sugli anelli esterni "PORTOGALLO 58", "SPAGNA 23", "ITALIA 11"; su quelli interni "COMPOSITI 66", "EDILIZIA 29". Il raggio dell'aggancio è proporzionale al numero: più pubblicazioni, più esterno l'anello. `GhostWord` "S.U.G.H.E.R.A." in outline 1 px al 15 %, dietro gli anelli, tagliata dal bordo destro. Nessun orbo.
**Animazione:** Gli anelli ruotano in 24 s, lineari. Etichette e linee non ruotano: il punto di aggancio scorre sull'anello, la linea si allunga e si accorcia di pochi px. Le etichette entrano in sequenza al caricamento (150 ms l'una, dissolvenza), poi restano ferme. Allo scroll parallasse −60 px; al puntatore spostamento del 2 % dei soli anelli. Con `prefers-reduced-motion` tutto è fermo e le etichette sono subito visibili.
**Significato:** Il turno di decortica come mappa: attorno alla risorsa si dispongono i Paesi e gli ambiti della ricerca.
**Fallback:** Statico: anelli fermi con le cinque etichette. Mobile: anelli da 280 px sopra il titolo, solo "PORTOGALLO 58" e "COMPOSITI 66", parola-fantasma nascosta.

## Una ricerca concentrata dove c'è la filiera {type=kpi}
<!-- valore | unità | etichetta | contesto | fonte -->
- 153 | pubblicazioni | Censite dal Technology Scouting, 2015-2025 | Articoli, atti, tesi, brevetti e documentazione tecnica; un passaggio del testo indica 166. | P2 pp.30, 142
- 37,9 % | delle pubblicazioni | Prodotte in Portogallo (58) | Seguono Spagna 15,0 % e Italia 7,2 %: insieme circa i due terzi. | P2 pp.30-31
- 66 | pubblicazioni | Sui materiali compositi e innovativi | L'ambito più studiato (43,1 %); seguono edilizia sostenibile (29) e biomedicale (23). | P2 pp.31-32
- TRL 3-6 | fascia prevalente | Maturità intermedia delle tecnologie censite | Validate in laboratorio o in ambienti rilevanti, in fase di dimostrazione preindustriale. | P2 p.32

## Come è stata costruita la mappa dell'innovazione {type=text id=ricerca}
Il Technology Scouting è una ricognizione sistematica della letteratura scientifica. Lo studio ha usato Google Scholar, con parole chiave in inglese per ambito: compositi, edilizia, isolamento, design, manifattura additiva, automotive, aerospazio, economia circolare, servizi ecosistemici, sottoprodotti (P2 pp.21-22).

Il periodo è 2015-2025. Ogni contributo è stato verificato su titolo, abstract e, se necessario, testo integrale. Poi è stato classificato per ambito, settore, tipo di innovazione e interesse per la Sardegna (P2 p.22). A ciascuna tecnologia è stato attribuito un livello di maturità ([[TRL]]) secondo la scala dei programmi europei (P2 pp.23-24).

Due approfondimenti, su rischio incendio e su certificazioni, sono stati gestiti a parte e non entrano nel database (P2 pp.22-23). Il database finale (Allegato II) conta 153 record. In un passaggio il testo parla di 166 pubblicazioni: verosimilmente il numero prima della validazione, ma lo studio non lo spiega (P2 pp.29-30).

## Portogallo, Spagna e Italia fanno la ricerca sul sughero {type=chart}
**Grafico:** barre orizzontali ordinate (10 righe) — pubblicazioni per Paese, con etichetta diretta "n (%)"; "Altri Paesi" e "Studi multipaese" in `--ink-muted`.
**Dati:** data/sughero-sardegna/technology-scouting.json → `per_paese.valori[]` (`paese`, `n_pubblicazioni`, `pct`): Portogallo 58 (37,9 %) · Spagna 23 (15,0 %) · Altri Paesi 22 (14,4 %) · Studi multipaese 20 (13,1 %) · Italia 11 (7,2 %) · Francia 8 (5,2 %) · Polonia 6 (3,9 %) · Danimarca 2 (1,3 %) · Algeria 2 (1,3 %) · Marocco 1 (0,7 %). Totale 153.
**Lettura:** Portogallo, Spagna e Italia sommano 92 pubblicazioni su 153, il 60,1 %. La didascalia della figura indica 67,5 %: qui si usa il valore calcolato dai numeri della figura stessa.
**Fonte:** P2, Figura 5 e par. 3.3.1, pp. 30-31

## La figura originale: distribuzione geografica {type=figure}
**Immagine:** source/parte2-filiera-sughero-sardegna/images/fig-5-distribuzione-geografica-innovazione.jpeg
**Didascalia:** Figura 5. Distribuzione geografica delle 153 pubblicazioni analizzate nel Technology Scouting (2015-2025). Portogallo, Spagna e Italia sono i principali poli di ricerca sulla filiera del sughero.
**Alt:** Mappa dell'Europa e del Mediterraneo con i Paesi colorati per numero di pubblicazioni; Portogallo in evidenza con 58.
**Nota:** La didascalia originale attribuisce ai tre Paesi il 67,5 % della produzione scientifica; dai numeri della figura risulta il 60,1 %.

## Compositi ed edilizia guidano, biomedicale e circolare crescono {type=chart id=ambiti}
**Grafico:** barre orizzontali ordinate (12 ambiti) — pubblicazioni per ambito applicativo, etichetta diretta "n (% su 153)".
**Dati:** data/sughero-sardegna/technology-scouting.json → `per_ambito.valori[]` (`ambito`, `n_pubblicazioni`, `pct`): Materiali compositi e innovativi 66 (43,1 %) · Edilizia sostenibile 29 (19,0 %) · Biomedicale, cosmetico e bioattivi 23 (15,0 %) · Economia circolare e valorizzazione degli scarti 22 (14,4 %) · Isolamento termo-acustico 14 (9,2 %) · Design e arredo 9 (5,9 %) · Energia 7 (4,6 %) · Packaging enologico 6 (3,9 %) · Automotive 6 (3,9 %) · Aerospaziale 6 (3,9 %) · Trattamento delle acque 5 (3,3 %) · Manifattura additiva 4 (2,6 %).
**Lettura:** Una pubblicazione può riguardare più ambiti: i 12 ambiti sommano 197 attribuzioni su 153 record. Le percentuali sono calcolate su 153 e non vanno sommate.
**Fonte:** P2, Figura 6 e par. 3.3.2, pp. 30-32

## La figura originale: gli ambiti di innovazione {type=figure}
**Immagine:** source/parte2-filiera-sughero-sardegna/images/fig-6-ambiti-innovazione-sughero.jpeg
**Didascalia:** Figura 6. Principali ambiti di innovazione del sughero: 153 pubblicazioni per settore applicativo.
**Alt:** Grafico a tessere dei 12 ambiti di innovazione del sughero, dimensionate per numero di pubblicazioni; i compositi sono i più grandi.
**Nota:** La didascalia originale indica 166 pubblicazioni e percentuali (34,9 %, 19,3 %, 12,7 %) non coerenti con i conteggi. Il sito usa i conteggi della figura, che coincidono con il testo.

## Tecnologie mature e filoni emergenti convivono {type=chart id=trl}
**Grafico:** barra orizzontale a tre fasce (qualitativa, senza conteggi) — TRL 1-3 emergenti · TRL 3-6 prevalenti · TRL 7-9 consolidate; sotto ogni fascia gli ambiti citati dallo studio come chip.
**Dati:** data/sughero-sardegna/technology-scouting.json → `per_trl_documento.valori[]` (`fascia_trl`, `descrizione`, `prevalenza`, `ambiti`). In "Vedi i dati": `per_trl_database.valori[]`, distribuzione calcolata dal database (3-5 → 38; 2-4 → 36; 3-4 → 31; 4-6 → 16; 6-8 → 9; 5-7 → 5; 2-3 → 1; non quantificato → 17), etichettata come elaborazione del sito.
**Lettura:** La maggior parte delle soluzioni è a TRL 3-6. Le applicazioni TRL 7-9 riguardano compositi, edilizia, isolamento, packaging e valorizzazione degli scarti. Quelle TRL 1-3 riguardano biomateriali, biomedicale, manifattura additiva, trattamento delle acque e alcune applicazioni aerospaziali. Nel database nessun record supera TRL 8.
**Fonte:** P2, par. 3.3.3, pp. 32-33; par. 4.3, p. 38; Allegato II, pp. 142-194 (distribuzione calcolata)

## Cosa significa per la Sardegna {type=text}
Lo studio traduce i risultati in nove direttrici (Tabella 1). Ciascuna ha un driver europeo, le evidenze emerse e un'opportunità per la Sardegna (P2 p.40). Le prime sette sono ambiti applicativi; le ultime due, TRL e ESG, sono trasversali. La raccomandazione è concentrare la ricerca sul consolidamento delle tecnologie a maturità intermedia, con validazione industriale e dimostrazione su scala reale (P2 p.33).

## Nove direttrici di innovazione {type=cards id=direttrici}
<!-- da direttrici-innovazione.json: direttrice, driver_europeo, evidenze_emerse, opportunita_sardegna, maturita (badge), n_pubblicazioni_fig6 -->
- **Materiali compositi e materiali innovativi** — Driver: Green Deal – Bioeconomy Strategy. Biomateriali leggeri, multifunzionali e ad alte prestazioni. Per la Sardegna: nuove filiere industriali basate su granulato, polveri e sottoprodotti. Maturità elevata · 66 pubblicazioni. `icona: layers`
- **Edilizia sostenibile** — Driver: Renovation Wave; EPBD. Isolamento termo-acustico, bioedilizia, efficienza energetica. Per la Sardegna: materiali naturali per riqualificazione energetica e costruzioni sostenibili. Maturità elevata · 29 pubblicazioni (più 14 sull'isolamento). `icona: home`
- **Biomedicale, cosmetico e bioattivi** — Driver: EU Health & Bioeconomy Strategy. Molecole bioattive, biomateriali e applicazioni medicali. Per la Sardegna: diversificazione verso mercati ad alto valore aggiunto. Maturità iniziale/intermedia · 23 pubblicazioni. `icona: heart-pulse`
- **Economia circolare e valorizzazione degli scarti** — Driver: Circular Economy Action Plan. Recupero dei residui di lavorazione e nuovi prodotti bio-based. Per la Sardegna: riduzione dei rifiuti e incremento del valore della filiera. Maturità elevata · 22 pubblicazioni. `icona: recycle`
- **Energia e tecnologie ambientali** — Driver: REPowerEU – Climate Neutrality. Biochar, adsorbenti, materiali funzionali e tecnologie ambientali. Per la Sardegna: nuovi impieghi energetici e ambientali del sughero. Maturità iniziale/intermedia · 12 pubblicazioni (energia 7, acque 5). `icona: zap`
- **Packaging sostenibile** — Driver: EU Packaging Regulation. Soluzioni naturali, riciclabili e a ridotto impatto ambientale. Per la Sardegna: innovazione nella filiera del tappo e del packaging alimentare. Maturità elevata · 6 pubblicazioni. `icona: package`
- **Automotive e aerospaziale** — Driver: Horizon Europe – Clean Industrial Deal. Materiali ultraleggeri e ad alte prestazioni. Per la Sardegna: collaborazioni con comparti industriali avanzati. Maturità mista · 12 pubblicazioni (6 + 6). `icona: rocket`
- **TRL e trasferimento tecnologico** — Driver: Horizon Europe – EIC. Coesistenza di tecnologie mature ed emergenti. Per la Sardegna: Living Lab, dimostratori tecnologici, spin-off e trasferimento alle imprese. Direttrice trasversale. `icona: arrow-right-left`
- **ESG e certificazioni ambientali** — Driver: CSRD – Tassonomia UE – Strategia Forestale 2030. Integrazione tra sostenibilità, tracciabilità e governance. Per la Sardegna: rafforzamento della competitività internazionale della filiera. Direttrice trasversale. `icona: badge-check`

**Fonte:** P2, Tabella 1 "Direttrici di innovazione", p. 40; conteggi per ambito dalla Figura 6, p. 32.

## Gestire bene la foresta è la prima innovazione {type=text}
Il secondo filone della ricognizione riguarda la gestione delle sugherete. La letteratura legge il loro declino come fenomeno multifattoriale: clima, incendi ricorrenti, eventi estremi, frammentazione, patogeni, abbandono delle pratiche selvicolturali (P2 pp.33-34). La prevenzione passa da gestione attiva del combustibile, pianificazione, monitoraggio fitosanitario e pascolo estensivo pianificato, che riduce il combustibile fine (P2 p.33). Crescono il monitoraggio geospaziale, la gestione adattativa e i pagamenti per servizi ecosistemici, incluso il carbon farming (P2 p.34).

Le certificazioni sono lette come strumenti di governance, non solo di qualità del prodotto (P2 pp.34, 38). In Portogallo, Spagna e Italia i sistemi certificati si associano a pianificazione più strutturata, monitoraggio più efficace e habitat meglio conservati (P2 p.38). Restano quattro ostacoli: frammentazione fondiaria, piccole dimensioni aziendali, costi, complessità amministrativa (P2 p.34). La risposta indicata è la certificazione di gruppo, con gestione associata e governance territoriale (P2 p.41).

## Undici strumenti, dalla foresta al prodotto {type=chart id=certificazioni}
**Grafico:** tabella leggera (non interattiva), 11 righe raggruppate per livello: foresta → impresa → prodotto e packaging → misura ambientale. Colonne: Strumento · Cosa certifica · Contributo alla filiera.
**Dati:** data/sughero-sardegna/strumenti-certificazione.json → `strumento`, `tipo`, `cosa_certifica`, `rilevanza_filiera`, `in_tabella_2` (solo `true`). I tre strumenti citati fuori tabella (Water Footprint, criteri ESG, certificazioni di prodotto) vanno in nota a piè di tabella.
**Righe:**

| Strumento | Cosa certifica | Contributo alla filiera |
|---|---|---|
| FSC | Gestione forestale sostenibile | Conservazione della biodiversità, tracciabilità e accesso ai mercati |
| PEFC | Gestione forestale sostenibile | Valorizzazione delle produzioni forestali e gestione di gruppo |
| PEFC Agroforestale | Gestione sostenibile dei sistemi agroforestali | Integrazione tra produzione forestale, pascolo e servizi ecosistemici |
| ISO 9001 | Sistema di gestione della qualità | Miglioramento dei processi aziendali |
| ISO 14001 | Sistema di gestione ambientale | Riduzione degli impatti ambientali |
| EMAS | Eccellenza ambientale | Trasparenza e miglioramento continuo |
| BRCGS Packaging | Sicurezza e qualità del packaging | Qualificazione dei processi produttivi |
| IFS PACsecure | Sicurezza degli imballaggi | Affidabilità della filiera di trasformazione |
| SYSTECODE | Tracciabilità del sughero | Garanzia di origine e controllo della filiera |
| Carbon Footprint (ISO 14067) | Quantificazione delle emissioni climalteranti | Valorizzazione del carbonio incorporato nei prodotti e supporto al Carbon Farming |
| LCA – ISO 14040/44 | Valutazione del ciclo di vita | Misurazione degli impatti ambientali e supporto all'eco-progettazione |

**Lettura:** Per lo studio il PEFC Italia – Gestione Sostenibile dei Sistemi Agroforestali è "particolarmente coerente" con le sugherete mediterranee (P2 p.39). Lì foresta, pascolo e servizi ecosistemici si integrano. Lo studio non riporta dati su superfici o aziende certificate.
**Fonte:** P2, Tabella 2, p. 41; par. 3.4.2, p. 34; par. 4.4, pp. 38-41

## Il database: 153 pubblicazioni da esplorare {type=chart id=database}
<!-- destinazione della CTA dell'hero. Unica interazione della pagina. Componente DataTable (sort, paginazione, export CSV). -->
**Grafico:** tabella dati (DataTable) paginata e collassabile — 153 righe, 25 per pagina, ordinabile per colonna, ricerca testuale, export CSV. Su mobile scorre in orizzontale dentro il proprio contenitore.
**Filtri:** Paese (`paesi`, multi-valore: Portogallo, Spagna, Italia, Multipaese, Francia, Polonia, altri) · Priorità (`priorita`: A 68 · B 79 · C 6) · Potenziale per la Sardegna (`potenziale_sardegna_stelle`: 5★ 16 · 4★ 52 · 3★ 82 · 2★ 3) · Fascia TRL (`trl_min`-`trl_max`, con "non quantificato") · Anno (`anno`, 2015-2026). Ricerca su `riferimento`, `titolo`, `settore_applicativo`. Risultati: "{n} pubblicazioni su 153"; "Azzera i filtri".
**Colonne:** Riferimento (`riferimento`; `doi` come link a doi.org quando presente, 28 record senza DOI) · Anno (`anno`) · Paese (`paese`) · Settore applicativo (`settore_applicativo`) · Innovazione (`livello_innovazione`) · TRL (`trl`) · Potenziale Sardegna (★ da `potenziale_sardegna_stelle`, tooltip `potenziale_sardegna_commento`) · Priorità (badge `priorita`) · Pagina PDF (`pagine_pdf`).
**Dati:** data/sughero-sardegna/bibliografia-scientifica.json → `dati[]` (153 record, 24 campi) e `aggregati`. I campi `anno`, `autore_primo`, `titolo`, `paesi`, `trl_min`, `trl_max`, `potenziale_sardegna_stelle` sono derivati dal riferimento: per la citazione usare `riferimento`. Gli 11 record con `inferenza = true` hanno materiale, potenziale industriale e valutazione vuoti: mostrare l'etichetta "dato inferito dalla fonte". I doppioni presenti nella fonte sono mantenuti (es. id 130-131).
**Lettura:** 68 pubblicazioni su 153 sono in priorità A e 16 hanno cinque stelle di potenziale per la Sardegna. Il numero di pubblicazioni cresce nel periodo: 7 nel 2015, 23 nel 2024 e 23 nel 2025; tre record sono datati 2026.
**Fonte:** P2, Allegato II "Database bibliografia scientifica", pp. 142-194 (legenda p. 142)

## In una frase {type=quote}
> Nel complesso, i risultati descrivono una filiera caratterizzata da una marcata capacità innovativa e da un elevato potenziale di trasferimento tecnologico.
— Terza parte, par. 3.3.3, p. 33

## S.U.G.H.E.R.A.: un modello in sette passaggi {type=kpi id=sughera}
<!-- apre la seconda metà della pagina (ex framework). valore | unità | etichetta | contesto | fonte -->
- 7 | step | Dalla risorsa forestale ai risultati attesi | Lo step 4 si sdoppia: gestione e certificazioni (4A), innovazione (4B). | P2 Fig. 7, p.43
- 4 | strategie | Produzione, Conservazione, Sperimentazione, Valorizzazione | Assegnabili ai comprensori in funzione del profilo territoriale. | P2 p.43
- 3 | dimensioni ESG | Ambiente, Sociale, Governance | I benefici attesi del modello, dal carbonio alla partecipazione. | P2 p.43
- 5 | componenti | Del futuro sistema di supporto alle decisioni (DSS) | Indicatori, GIS, certificazioni, valutazione ambientale, Technology Scouting. | P2 p.44

## Un acronimo, due letture {type=text}
Lo studio riunisce indici territoriali, certificazioni e innovazione in un unico modello. È pensato come base di un sistema di supporto alle decisioni per amministrazioni, gestori, imprese e ricerca (P2 p.42).

S.U.G.H.E.R.A. sta per Strategic Unified Governance, Habitat Evaluation and Regional Assessment (P2 p.42). La lista delle abbreviazioni lo rende in italiano come Sistema Unificato di Gestione, Habitat, Ecosistemi, Resilienza e Analisi (P2 p.9).

È un framework multidisciplinare: integra in un unico sistema informazioni ecologiche, territoriali, tecnologiche e gestionali (P2 p.42). L'elemento distintivo è il collegamento tra i tre indici ([[IVP]], [[IPI]], [[ICR]]), la ricerca internazionale e le opportunità dell'innovazione (P2 p.42).

Il principio di fondo: la disponibilità della risorsa è solo uno dei fattori. Contano vocazionalità ecologica, resilienza, qualità della gestione, capacità organizzativa e possibilità di trasferire le innovazioni sul territorio (P2 p.42).

## Il framework in un'immagine {type=figure}
**Immagine:** source/parte2-filiera-sughero-sardegna/images/fig-7-framework-sughera.jpeg
**Didascalia:** Figura 7. Framework S.U.G.H.E.R.A. (Strategic Unified Governance, Habitat Evaluation and Regional Assessment): schema del modello integrato che mette in relazione analisi territoriale, gestione forestale, certificazioni, innovazione tecnologica e governance.
**Alt:** Diagramma di flusso verticale a sette blocchi, dalla risorsa forestale alla valorizzazione della filiera, con due blocchi paralleli al passo 4.

## Sette passaggi, dalla risorsa alle strategie {type=tabs}
<!-- rendering: stepper verticale numerato (su mobile accordion). Testi dei blocchi = Figura 7; "Ingresso/Esito" = lettura redazionale del flusso (framework-sughera.json → step[].input/output). -->
### 1 · Risorsa forestale
Le sugherete della Sardegna: patrimonio naturale, produttivo e territoriale ad elevato valore ecologico ed economico.
### 2 · Analisi territoriale (GIS)
Tre indicatori per ciascun comune: [[IVP]] per il suolo, [[IPI]] per il fuoco, [[ICR]] per la continuità. Ingresso: cartografia pedologica, pericolo incendio, uso del suolo (P2 p.20). Vai ai 30 comuni → /sughero-sardegna#esploratore
### 3 · Caratterizzazione dei comprensori
Per ogni territorio: punti di forza, criticità e priorità di intervento. Esito: il profilo integrato, lo stesso riportato nelle 30 schede comunali → /sughero-sardegna#lettura-integrata
### 4A · Gestione forestale e certificazioni
Gestione sostenibile e adattativa; prevenzione incendi e biodiversità; governance e gestione associata; certificazioni FSC, PEFC, PEFC Agroforestale; sistemi ISO 9001, ISO 14001, EMAS, BRCGS, IFS, SYSTECODE; certificazione di gruppo. In dialogo con 4B. Gli strumenti → #certificazioni
### 4B · Technology scouting e innovazione
Compositi e bioedilizia; biomateriali e packaging; nuove applicazioni e design; sottoprodotti ed economia circolare; digitalizzazione e monitoraggio; ricerca e trasferimento tecnologico. Le direttrici → #direttrici
### 5 · Strategie territoriali differenziate
Quattro strategie assegnabili in funzione del profilo. Produzione: materia prima e certificazione. Conservazione: biodiversità, servizi ecosistemici, continuità. Sperimentazione: nuove tecnologie e modelli gestionali. Valorizzazione: sottoprodotti, economia circolare, nuovi mercati.
### 6 · Bioeconomia, ESG, sviluppo sostenibile
Ambiente: conservazione, resilienza climatica, carbonio. Sociale: comunità locali, occupazione, coesione. Governance: reti territoriali, partecipazione, decisioni condivise.
### 7 · Valorizzazione della filiera regionale
Risultati attesi: competitività e innovazione; gestione sostenibile delle foreste; economia circolare e nuovi mercati; sviluppo territoriale e benessere delle comunità.

**Fonte:** P2, Figura 7, p. 43; par. 4.5, pp. 41-44.

## Territori diversi, strategie diverse {type=text}
Il modello non propone una ricetta unica. Suoli vocati, copertura continua e bassa vulnerabilità al fuoco indicano produzione primaria, certificazione e valorizzazione industriale (P2 p.42). Nei comprensori più vulnerabili vengono prima gestione adattativa, ripristino ecologico, prevenzione incendi, ricostituzione della continuità e governance locale (P2 p.42).

Le vocazioni diverse non frammentano la filiera: sono una risorsa da organizzare in rete (P2 p.42). L'Alta Gallura è il polo regionale del trasferimento tecnologico: concentrazione della risorsa, imprese storiche, competenze tecniche (P2 p.42). Un ruolo che integra, non sostituisce, gli altri comprensori (P2 p.44).

## Cinque profili, quattro strategie {type=cards}
<!-- da framework-sughera.json → strategie_territoriali_per_profilo.profili[]; la strategia tra parentesi è l'associazione redazionale alla Figura 7 -->
- **Vocato, continuo, poco esposto (Produzione)** — IVP alto, ICR alto, IPI basso: sviluppo della produzione primaria, certificazione forestale, valorizzazione industriale della materia prima. Nelle schede il profilo più vicino è "Area vocata e relativamente governabile", 3 comuni. `icona: trees`
- **Vulnerabile (Conservazione e ripristino)** — Fuoco alto o risorsa frammentata: gestione adattativa, ripristino, prevenzione incendi, continuità, governance locale. `icona: shield`
- **Vocato alla biodiversità (Conservazione)** — Comprensori orientati alla conservazione della biodiversità e dei servizi ecosistemici. `icona: leaf`
- **Sperimentazione e sottoprodotti (Sperimentazione / Valorizzazione)** — Modelli innovativi di gestione forestale, valorizzazione dei sottoprodotti, nuove applicazioni industriali. `icona: flask-conical`
- **Alta Gallura, distretto industriale (Sperimentazione / Valorizzazione)** — Ricerca applicata, sperimentazione industriale, diffusione delle tecnologie emergenti, trasferimento tecnologico. Le aree pilota sono nella roadmap → /alta-gallura/strategia#roadmap `icona: factory`

**Fonte:** P2, par. 4.5, p. 42; Figura 7, p. 43.

## Nota di lettura {type=text}
Lo studio descrive i profili in forma discorsiva e non assegna i singoli comuni a una strategia (P2 p.42). L'unico ponte con i 30 comuni è il profilo integrato delle schede: 7 profili, 30 comuni (P2 pp.52-141). L'associazione tra profili e le quattro strategie della Figura 7 è una lettura redazionale. I profili dei 30 comuni → /sughero-sardegna#lettura-integrata

## Le conclusioni dello studio in otto messaggi {type=cards id=conclusioni}
<!-- da conclusioni.json → messaggi_chiave (id 2, 3, 4, 5, 6, 7, 8, 10), riformulati in breve; pagina in coda -->
- **La risorsa è solo uno dei fattori** — La disponibilità di sughereta non basta a determinare il potenziale della filiera: contano suolo, fuoco e continuità. (P2 p.45) `icona: scale`
- **Ogni comprensorio ha condizioni diverse** — IVP, IPI e ICR insieme rivelano condizioni ecologiche, strutturali e gestionali differenti: serve pianificare per vocazioni. (P2 p.45) `icona: map`
- **Il sughero si diversifica** — La ricerca va verso compositi, edilizia sostenibile, biomateriali, biomedicale ed economia circolare. (P2 p.45) `icona: sparkles`
- **Competere significa integrare** — Gestione sostenibile, innovazione, tracciabilità, qualità dei processi e governance territoriale contano sempre di più. (P2 p.45) `icona: link`
- **Le certificazioni funzionano se associate** — FSC, PEFC e il PEFC Italia agroforestale sono coerenti con le sugherete mediterranee, soprattutto in modelli di gestione associata. (P2 p.45) `icona: badge-check`
- **La frammentazione è il nodo** — Frammentazione fondiaria, piccole proprietà e complessità organizzativa riguardano una parte significativa del patrimonio regionale. (P2 p.45) `icona: puzzle`
- **Un quadro unico per decidere** — Il framework S.U.G.H.E.R.A. integra analisi territoriale, gestione, innovazione, certificazioni e governance in un solo supporto alle decisioni. (P2 p.45) `icona: layout-grid`
- **Un'infrastruttura naturale strategica** — Le sugherete generano valore ambientale, economico e sociale: materia prima, biodiversità, carbonio, nuove filiere. (P2 p.46) `icona: trees`

**Fonte:** P2, Quinta parte "Conclusioni e prospettive", pp. 45-46.

## Cosa succede dopo: dal modello al DSS {type=text}
Il passo successivo indicato dallo studio è trasformare il modello in un Decision Support System ([[DSS]]) (P2 p.44). Cinque componenti: indicatori territoriali integrati, [[GIS]], strumenti di certificazione, metodologie di valutazione ambientale (Carbon Footprint, Water Footprint, [[LCA]]) e Technology Scouting (P2 pp.44, 46).

Servirebbe ad amministrazioni, enti gestori, imprese e ricerca per pianificare interventi e fissare priorità di investimento (P2 p.44). La struttura è modulare: dati territoriali, evidenze scientifiche e innovazioni si aggiornano nel tempo (P2 p.45).

Lo studio raccomanda di concentrare la ricerca sulle tecnologie a maturità intermedia (P2 p.33). E di promuovere certificazione collettiva, aggregazione territoriale e supporto tecnico-amministrativo (P2 p.34). La roadmap operativa per l'Alta Gallura è nella prima sezione → /alta-gallura/strategia#roadmap

## La prospettiva finale {type=quote}
> Il modello proposto costituisce […] uno strumento operativo per trasformare la conoscenza scientifica in strategie di pianificazione territoriale e di sviluppo sostenibile.
— Quinta parte, "Conclusioni e prospettive", p. 46

## Continua {type=cards}
<!-- card di navigazione a fine pagina -->
- **I 30 comuni della Sughereta** — Suolo, fuoco e continuità comune per comune, con la scheda di ciascuno. → /sughero-sardegna#esploratore `icona: map`
- **Strategia dell'Alta Gallura** — Framework Green community, ESG, tre filiere e roadmap di 36 mesi con le aree pilota. → /alta-gallura/strategia `icona: route`
- **Scarica lo studio integrale (PDF)** — I due studi RISSTE, le 16 figure e i dataset aperti. → /progetto#documenti `icona: download`

## Fonti {type=sources}
- Valorizzazione della filiera del sughero in Sardegna – Un framework multidisciplinare (RISSTE, 2025), Lista delle abbreviazioni, p. 9
- Idem, Seconda parte, par. 2.4-2.6 "Technology Scouting", pp. 21-24
- Idem, Terza parte, par. 3.3 "Innovazione della filiera del sughero", pp. 29-33 (Figura 5 p. 31, Figura 6 p. 32); par. 3.4 "Gestione forestale e certificazioni", pp. 33-34
- Idem, Quarta parte, par. 4.3 "Innovazione, bioeconomia e sostenibilità", pp. 37-38 (Tabella 1 p. 40); par. 4.4 "Gestione sostenibile, certificazioni e governance", pp. 38-41 (Tabella 2 p. 41); par. 4.5 "Un modello integrato per la valorizzazione della Sughereta Sardegna", pp. 41-44 (Figura 7, p. 43)
- Idem, Quinta parte "Conclusioni e prospettive", pp. 45-46
- Idem, Allegato I, profili integrati delle 30 schede comunali, pp. 52-141
- Idem, Allegato II "Database bibliografia scientifica", pp. 142-194
- Le pagine indicate sono quelle fisiche del PDF; la numerazione stampata è inferiore di 17.
