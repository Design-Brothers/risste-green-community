---
slug: /sughero-sardegna/innovazione
sezione: sughero-sardegna
eyebrow: "Sughero Sardegna · Innovazione"
title: "Dove va l'innovazione del sughero"
seo_title: "Innovazione del sughero: technology scouting – Sardegna"
description: "Technology scouting sul sughero: dove si fa ricerca, gli ambiti (compositi, edilizia, biomedicale, economia circolare), maturità tecnologica e certificazioni."
og_image: source/parte2-filiera-sughero-sardegna/images/fig-6-ambiti-innovazione-sughero.jpeg
fonti:
  - documento: parte2
    pagine: [17, 21, 22, 23, 24, 29, 30, 31, 32, 33, 34, 37, 38, 39, 40, 41, 142, 194]
dati:
  - sughero-sardegna/technology-scouting.json
  - sughero-sardegna/direttrici-innovazione.json
  - sughero-sardegna/strumenti-certificazione.json
  - sughero-sardegna/bibliografia-scientifica.json
figure:
  - parte2-filiera-sughero-sardegna/images/fig-5-distribuzione-geografica-innovazione.jpeg
  - parte2-filiera-sughero-sardegna/images/fig-6-ambiti-innovazione-sughero.jpeg
---

<!-- Pagine citate (P2 p.N) = pagine fisiche del PDF della Parte 2; la numerazione stampata è inferiore di 17. -->
<!-- Regola dati: il totale delle pubblicazioni è 153 (Allegato II, Figure 5-6). Il numero 166 compare in un passaggio del testo e si cita solo con la nota. -->

## Hero {type=hero}
**Standfirst:** La ricerca internazionale porta il sughero nei compositi, nell'edilizia, nel biomedicale e nell'economia circolare. Lo studio ha censito 153 pubblicazioni e ne ricava nove direttrici di innovazione per la Sardegna.
**CTA:** Consulta il database bibliografico → /sughero-sardegna/innovazione#database

## Una ricerca concentrata dove c'è la filiera {type=kpi}
<!-- valore | unità | etichetta | contesto | fonte -->
- 153 | pubblicazioni | Censite dal Technology Scouting, 2015-2025 | Articoli, atti, tesi, brevetti e documentazione tecnica; un passaggio del testo indica 166. | P2 pp.30, 142
- 37,9 % | delle pubblicazioni | Prodotte in Portogallo (58) | Seguono Spagna 15,0 % e Italia 7,2 %: insieme circa i due terzi. | P2 pp.30-31
- 66 | pubblicazioni | Sui materiali compositi e innovativi | L'ambito più studiato (43,1 %); seguono edilizia sostenibile (29) e biomedicale (23). | P2 pp.31-32
- TRL 3-6 | fascia prevalente | Maturità intermedia delle tecnologie censite | Validate in laboratorio o in ambienti rilevanti, in fase di dimostrazione preindustriale. | P2 p.32

## Come è stata costruita la mappa dell'innovazione {type=text}
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

## Compositi ed edilizia guidano, biomedicale e circolare crescono {type=chart}
**Grafico:** barre orizzontali ordinate (12 ambiti) — pubblicazioni per ambito applicativo, etichetta diretta "n (% su 153)".
**Dati:** data/sughero-sardegna/technology-scouting.json → `per_ambito.valori[]` (`ambito`, `n_pubblicazioni`, `pct`): Materiali compositi e innovativi 66 (43,1 %) · Edilizia sostenibile 29 (19,0 %) · Biomedicale, cosmetico e bioattivi 23 (15,0 %) · Economia circolare e valorizzazione degli scarti 22 (14,4 %) · Isolamento termo-acustico 14 (9,2 %) · Design e arredo 9 (5,9 %) · Energia 7 (4,6 %) · Packaging enologico 6 (3,9 %) · Automotive 6 (3,9 %) · Aerospaziale 6 (3,9 %) · Trattamento delle acque 5 (3,3 %) · Manifattura additiva 4 (2,6 %).
**Lettura:** Una pubblicazione può riguardare più ambiti: i 12 ambiti sommano 197 attribuzioni su 153 record. Le percentuali sono calcolate su 153 e non vanno sommate.
**Fonte:** P2, Figura 6 e par. 3.3.2, pp. 30-32

## La figura originale: gli ambiti di innovazione {type=figure}
**Immagine:** source/parte2-filiera-sughero-sardegna/images/fig-6-ambiti-innovazione-sughero.jpeg
**Didascalia:** Figura 6. Principali ambiti di innovazione del sughero: 153 pubblicazioni per settore applicativo.
**Alt:** Grafico a tessere dei 12 ambiti di innovazione del sughero, dimensionate per numero di pubblicazioni; i compositi sono i più grandi.
**Nota:** La didascalia originale indica 166 pubblicazioni e percentuali (34,9 %, 19,3 %, 12,7 %) non coerenti con i conteggi. Il sito usa i conteggi della figura, che coincidono con il testo.

## Tecnologie mature e filoni emergenti convivono {type=chart}
**Grafico:** barra orizzontale a tre fasce (qualitativa, senza conteggi) — TRL 1-3 emergenti · TRL 3-6 prevalenti · TRL 7-9 consolidate; sotto ogni fascia gli ambiti citati dallo studio come chip.
**Dati:** data/sughero-sardegna/technology-scouting.json → `per_trl_documento.valori[]` (`fascia_trl`, `descrizione`, `prevalenza`, `ambiti`). In "Vedi i dati": `per_trl_database.valori[]`, distribuzione calcolata dal database (3-5 → 38; 2-4 → 36; 3-4 → 31; 4-6 → 16; 6-8 → 9; 5-7 → 5; 2-3 → 1; non quantificato → 17), etichettata come elaborazione del sito.
**Lettura:** La maggior parte delle soluzioni è a TRL 3-6. Le applicazioni TRL 7-9 riguardano compositi, edilizia, isolamento, packaging e valorizzazione degli scarti. Quelle TRL 1-3 riguardano biomateriali, biomedicale, manifattura additiva, trattamento delle acque e alcune applicazioni aerospaziali. Nel database nessun record supera TRL 8.
**Fonte:** P2, par. 3.3.3, pp. 32-33; par. 4.3, p. 38; Allegato II, pp. 142-194 (distribuzione calcolata)

## Cosa significa per la Sardegna {type=text}
Lo studio traduce i risultati in nove direttrici (Tabella 1). Ciascuna ha un driver europeo, le evidenze emerse e un'opportunità per la Sardegna (P2 p.40). Le prime sette sono ambiti applicativi; le ultime due, TRL e ESG, sono trasversali. La raccomandazione è concentrare la ricerca sul consolidamento delle tecnologie a maturità intermedia, con validazione industriale e dimostrazione su scala reale (P2 p.33).

## Nove direttrici di innovazione {type=cards}
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

## Gestire bene la foresta è la prima innovazione {type=text}
Il secondo filone della ricognizione riguarda la gestione delle sugherete. La letteratura legge il loro declino come fenomeno multifattoriale: clima, incendi ricorrenti, eventi estremi, frammentazione, patogeni, abbandono delle pratiche selvicolturali (P2 pp.33-34). La prevenzione passa da gestione attiva del combustibile, pianificazione, monitoraggio fitosanitario e pascolo estensivo pianificato, che riduce il combustibile fine (P2 p.33). Crescono il monitoraggio geospaziale, la gestione adattativa e i pagamenti per servizi ecosistemici, incluso il carbon farming (P2 p.34).

Le certificazioni sono lette come strumenti di governance, non solo di qualità del prodotto (P2 pp.34, 38). In Portogallo, Spagna e Italia i sistemi certificati si associano a pianificazione più strutturata, monitoraggio più efficace e migliore conservazione degli habitat (P2 p.38). Restano quattro ostacoli: frammentazione fondiaria, piccole dimensioni aziendali, costi, complessità amministrativa (P2 p.34). La risposta indicata è la certificazione di gruppo, con gestione associata e governance territoriale (P2 p.41).

## Undici strumenti, dalla foresta al prodotto {type=chart}
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

## Il database: 153 pubblicazioni da esplorare {type=chart}
<!-- id="database" (destinazione della CTA). Unica interazione della pagina. -->
**Grafico:** tabella dati (DataTable) paginata e collassabile — 153 righe, 25 per pagina, ordinabile per colonna, ricerca testuale, export CSV. Su mobile scorre in orizzontale dentro il proprio contenitore.
**Filtri:** Paese (`paesi`, multi-valore: Portogallo, Spagna, Italia, Multipaese, Francia, Polonia, altri) · Priorità (`priorita`: A 68 · B 79 · C 6) · Potenziale per la Sardegna (`potenziale_sardegna_stelle`: 5★ 16 · 4★ 52 · 3★ 82 · 2★ 3) · Fascia TRL (`trl_min`-`trl_max`, con "non quantificato") · Anno (`anno`, 2015-2026). Ricerca su `riferimento`, `titolo`, `settore_applicativo`.
**Colonne:** Riferimento (`riferimento`; `doi` come link a doi.org quando presente, 28 record senza DOI) · Anno (`anno`) · Paese (`paese`) · Settore applicativo (`settore_applicativo`) · Innovazione (`livello_innovazione`) · TRL (`trl`) · Potenziale Sardegna (★ da `potenziale_sardegna_stelle`, tooltip `potenziale_sardegna_commento`) · Priorità (badge `priorita`) · Pagina PDF (`pagine_pdf`).
**Dati:** data/sughero-sardegna/bibliografia-scientifica.json → `dati[]` (153 record, 24 campi) e `aggregati`. I campi `anno`, `autore_primo`, `titolo`, `paesi`, `trl_min`, `trl_max`, `potenziale_sardegna_stelle` sono derivati dal riferimento: per la citazione usare `riferimento`. Gli 11 record con `inferenza = true` hanno materiale, potenziale industriale e valutazione vuoti: mostrare l'etichetta "dato inferito dalla fonte". I doppioni presenti nella fonte sono mantenuti (es. id 130-131).
**Lettura:** 68 pubblicazioni su 153 sono in priorità A e 16 hanno cinque stelle di potenziale per la Sardegna. Il numero di pubblicazioni cresce nel periodo: 7 nel 2015, 23 nel 2024 e 23 nel 2025; tre record sono datati 2026.
**Fonte:** P2, Allegato II "Database bibliografia scientifica", pp. 142-194 (legenda p. 142)

## In una frase {type=quote}
> Nel complesso, i risultati descrivono una filiera caratterizzata da una marcata capacità innovativa e da un elevato potenziale di trasferimento tecnologico.
— Terza parte, par. 3.3.3, p. 33

## Fonti {type=sources}
- Valorizzazione della filiera del sughero in Sardegna – Un framework multidisciplinare (RISSTE, 2025), Seconda parte, par. 2.4-2.6 "Technology Scouting", pp. 21-24
- Idem, Terza parte, par. 3.3 "Innovazione della filiera del sughero", pp. 29-33 (Figura 5 p. 31, Figura 6 p. 32); par. 3.4 "Gestione forestale e certificazioni", pp. 33-34
- Idem, Quarta parte, par. 4.3 "Innovazione, bioeconomia e sostenibilità", pp. 37-38 (Tabella 1 p. 40); par. 4.4 "Gestione sostenibile, certificazioni e governance", pp. 38-41 (Tabella 2 p. 41)
- Idem, Allegato II "Database bibliografia scientifica", pp. 142-194
- Le pagine indicate sono quelle fisiche del PDF; la numerazione stampata è inferiore di 17.
