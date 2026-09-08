---
slug: /sughero-sardegna
sezione: sughero-sardegna
eyebrow: "Sughero Sardegna"
title: "La Sughereta Sardegna: suolo, fuoco, continuità"
seo_title: "Sughereta Sardegna – 30 comuni e tre indici"
description: "La Sardegna ospita circa il 90 % delle sugherete italiane. Esplora i 30 comuni, 83.790 ettari, con tre indici: suoli (IVP), fuoco (IPI), continuità (ICR)."
og_image: source/parte2-filiera-sughero-sardegna/images/fig-1-workflow-analisi-integrata.jpeg
ancore:                                  # id delle sezioni raggiungibili con /sughero-sardegna#…
  - indici
  - esploratore
  - lettura-integrata
fonti:
  - documento: parte2
    pagine: [15, 16, 17, 19, 20, 24, 26, 27, 28, 29, 30, 35, 36, 37, 42, 50, 51, 52, 141]
dati:
  - sughero-sardegna/contesto-sughero-sardegna.json
  - sughero-sardegna/comuni-sughereta.json
  - sughero-sardegna/indici-definizioni.json
  - sughero-sardegna/sintesi-regionale.json
figure:
  - parte2-filiera-sughero-sardegna/images/fig-1-workflow-analisi-integrata.jpeg
  - parte2-filiera-sughero-sardegna/images/fig-2-ivp-ranking-30-comuni.jpeg
  - parte2-filiera-sughero-sardegna/images/fig-3-ipi-pericolosita-incendio-30-comuni.jpeg
  - parte2-filiera-sughero-sardegna/images/fig-4-icr-continuita-risorsa-30-comuni.jpeg
---

**Ancore:** `#indici` → "I tre indici in breve" · `#esploratore` → "Esploratore: ordina e confronta i 30 comuni" · `#lettura-integrata` → "Leggere i tre indici insieme". Il pannello scheda comune si apre con `?comune=slug` (specifica in `04b-sughero-pannello-comune.md`).

<!-- Pagina unica della sezione: fonde i v1 07-sughero-hub e 08-sughero-sughereta. Pagine citate (P2 p.N) = pagine fisiche del PDF della Parte 2; la numerazione stampata è inferiore di 17. -->
<!-- Regola dati: tutti i valori per comune vengono da comuni-sughereta.json (schede dell'Allegato I). Le Figure 2-4 non si usano come fonte numerica: solo in lightbox, come "elaborazione grafica dello studio". -->

## Hero {type=hero}
**Standfirst:** La Sardegna ospita circa il 90 % delle sugherete italiane. Nei 30 comuni prioritari, 83.790,90 ettari, lo studio RISSTE misura suolo, fuoco e continuità con tre indici. Ventuno comuni hanno suoli vocati; in 16 oltre il 90 % della sughereta è in pericolo Medioalto o Alto.
**CTA:** Esplora i 30 comuni → /sughero-sardegna#esploratore
**Figura hero:** source/parte2-filiera-sughero-sardegna/images/fig-1-workflow-analisi-integrata.jpeg — a piena larghezza sotto lo standfirst, con "Ingrandisci" (lightbox) e fonte.
**Didascalia:** Figura 1. Workflow metodologico dell'analisi integrata. Analisi territoriale, Technology Scouting e approfondimento su gestione sostenibile e certificazione confluiscono in un quadro conoscitivo unitario (P2 p.26).
**Alt:** Schema a blocchi: analisi territoriale, technology scouting e certificazioni convergono in un quadro integrato di supporto alle decisioni.
<!-- Motivo grafico dell'hero: le 30 sferette e gli anelli di decortica ambra-terracotta descritti nel blocco visual (brief §3). -->

## Illustrazione di apertura {type=visual}
**Elemento:** Trenta sferette sfumate ambra (`--cork-light` → `--cork`), una per comune. Il diametro è proporzionale agli ettari di sughereta, scala a radice quadrata: da 24 px (Bultei) a 120 px (Bitti). Dati: `comuni-sughereta.json` → `sugherete_ha`, `rank`. Galleggiano nella metà destra dell'hero, dietro e attorno al titolo, con blur 6 px e grana 8 %. `GhostWord` "SUGHERETA" in outline 1 px al 18 %, dietro le sferette, tagliata dal bordo destro. `MicroLabel` "30 COMUNI" in alto a destra e "83.790,90 HA" in basso a destra. La Figura 1 resta sotto lo standfirst, a piena larghezza.
**Animazione:** Ogni sferetta deriva su una piccola ellisse (8-20 px) con ciclo 14-26 s, easing sinusoidale, fase casuale. Allo scroll verso l'esploratore (`#esploratore`) le sferette si ordinano in colonna, per ettari decrescenti. Il moto è guidato dallo scroll (`useScroll`), non a tempo; le sferette atterrano sulle barre del ranking. Nell'intro a capitoli le stesse sferette compongono le scene 02-04 (vedi blocco intro). Al puntatore spostamento del 2 %. Con `prefers-reduced-motion` restano ferme nella disposizione galleggiante.
**Significato:** La Sughereta Sardegna non è una massa ma trenta comuni di peso diverso: l'illustrazione è già il ranking.
**Fallback:** Statico: sferette ferme nella disposizione galleggiante, nessun riordino. Mobile: le 12 sferette maggiori, da 16 a 80 px, sopra il titolo; parola-fantasma 28 vw; resta l'etichetta "30 COMUNI".

## Introduzione {type=intro}
<!-- Quattro capitoli con i numeri principali della sezione (ARCHITETTURA `/sughero-sardegna` punto 0; COMPONENTI §5b). Numeri e fonti dal blocco KPI "Una risorsa grande, un mosaico di condizioni" e dal blocco "Suoli buoni quasi ovunque, fuoco quasi ovunque". Scena: l'orbo ambra si scompone nelle 30 sferette dell'hero, che si colorano per classe; chiudono gli anelli di decortica tone cork. -->
**Salta a:** #indici

### 01 · Nove sugherete italiane su dieci sono in Sardegna
**Numero:** ≈90 | % delle sugherete italiane
**Contesto:** Ordine di grandezza indicato dallo studio, senza anno di riferimento.
**Scena:** orbo · `--cork-light` → `--cork` · destra, grande (70 vmin) · "SUGHERETA"
**Dati:** data/sughero-sardegna/contesto-sughero-sardegna.json → quota_superfici_italiane_sughereta_pct
**Fonte:** P2 p. 16

### 02 · Trenta comuni prioritari, 83.790,90 ettari di sughereta
**Numero:** 83.790,90 | ha
**Contesto:** Il nucleo della Sughereta Sardegna, da elaborazione [[GIS]] su tutta la regione.
**Scena:** l'orbo si scompone in 30 sferette ambra (`--cork-light` → `--cork`), diametro proporzionale agli ettari · sparse a destra · "30 COMUNI"
**Dati:** data/sughero-sardegna/sintesi-regionale.json → totali.somma_sugherete_30_comuni_ha; comuni-sughereta.json → sugherete_ha
**Fonte:** P2 pp. 20, 27

### 03 · Suoli vocati in ventuno comuni su trenta
**Numero:** 21 | comuni su 30 in classe IVP Alta
**Contesto:** Conteggio dalle schede comunali; il testo dello studio indica 22.
**Scena:** sferette colorate per classe [[IVP]] · Alta `#2E7D32` ×21, Media `#F0B800` ×4, Bassa `#F08800` ×5 · le 21 verdi al centro · "IVP"
**Dati:** data/sughero-sardegna/sintesi-regionale.json → conteggi_classe_ivp.dataset; comuni-sughereta.json → classe_ivp
**Fonte:** P2 pp. 27, 50-141

### 04 · In sedici comuni oltre il 90 % è in pericolo alto
**Numero:** 16 | comuni
**Contesto:** Oltre il 90 % della sughereta in classe Medioalto o Alto, da Iglesias (98,28 %) a Calangianus (93,20 %).
**Scena:** anelli `DecorticaRings` tone cork · `--cork` → `--cork-light` · centro-destra, 60 vmin, rotazione lenta; le 16 sferette virano a `#F08800`/`#D84315` dentro gli anelli · "IPI"
**Dati:** data/sughero-sardegna/comuni-sughereta.json → quota_medioalto_alto_pct, classe_incendio
**Fonte:** P2 p. 28; Allegato I, pp. 52-141

## Una risorsa grande, un mosaico di condizioni {type=kpi}
<!-- valore | unità | etichetta | contesto | fonte — unico blocco KPI della pagina -->
- 90 % | circa | Sugherete italiane che si trovano in Sardegna | Ordine di grandezza indicato dallo studio, senza anno di riferimento. | P2 p.16
- 83.790,90 | ha | Sugherete nei 30 comuni prioritari | Il nucleo della Sughereta Sardegna, da elaborazione GIS su tutta la regione. | P2 pp.20, 27
- 21 | comuni su 30 | Con suoli in classe IVP Alta | Conteggio dalle schede comunali; il testo dello studio indica 22. | P2 pp.27, 50-141
- 71,8 % | della superficie | In classe di pericolo incendio Medioalto o Alto | 60.175,57 ha: somma delle tabelle incendio delle 30 schede (elaborazione del sito). | P2 pp.52-141

## Un patrimonio che vale più della corteccia {type=text}
La quercia da sughero trova in Sardegna uno dei suoi principali areali. L'isola ospita circa il 90 % delle superfici italiane a sughereta. È tra i primi territori europei per produzione e trasformazione (P2 p.16).

Per secoli le sugherete hanno sostenuto i sistemi agro-silvo-pastorali: corteccia, pascolo, prodotti del sottobosco, biomassa. Lo studio le descrive anche come ecosistema multifunzionale: conservano la biodiversità, proteggono il suolo, regolano il ciclo idrologico, sequestrano carbonio. La corteccia suberosa rende la specie particolarmente resistente al fuoco (P2 p.16).

Dal XVIII secolo la Gallura è il centro della filiera industriale. L'Alta Gallura è ancora oggi il principale distretto italiano della lavorazione del sughero. È anche il riferimento per ricerca applicata e trasferimento tecnologico (P2 pp.15-16).

## Perché la risorsa non basta {type=text}
La filiera sarda resta orientata agli impieghi tradizionali (P2 p.17). Per lo studio la competitività non dipende solo dalla materia prima. Conta la capacità di integrare innovazione, sostenibilità, gestione forestale responsabile e strumenti di valorizzazione (P2 p.17).

Da qui un metodo in tre passaggi. Primo: un'analisi territoriale in ambiente [[GIS]] sui 30 comuni con la maggiore estensione di sughereta (P2 p.20). Secondo: un Technology Scouting su 153 pubblicazioni. Terzo: un approfondimento su gestione forestale e certificazioni (P2 pp.19-24). I risultati convergono nel framework S.U.G.H.E.R.A., base di un futuro sistema di supporto alle decisioni (P2 p.42). Questa pagina racconta il primo passaggio; gli altri due sono in → /sughero-sardegna/innovazione.

Contare gli ettari non basta a descrivere una sughereta. Lo studio affianca all'estensione tre indici originali, costruiti su cartografie regionali: [[PFAR]], uso del suolo, carta pedologica, pericolo incendio (P2 pp.19-20). L'Indice di Vocazionalità Pedologica ([[IVP]]) dice su quali suoli cresce la sughera. L'Indice di Pericolosità da Incendio ([[IPI]]) dice quanto è esposta al fuoco. L'Indice di Continuità della Risorsa ([[ICR]]) dice se è accorpata o dispersa (P2 pp.20, 50).

Letti insieme descrivono tre dimensioni della resilienza. L'IVP misura la resilienza potenziale del sito, l'IPI il principale fattore di pressione, l'ICR la configurazione spaziale (P2 p.37).

## I tre indici in breve {type=cards id=indici}
<!-- una card per indice: domanda, come si calcola, scala e classi con gli intervalli osservati nelle 30 schede. Dati: indici-definizioni.json → indici[IVP|IPI|ICR] (definizione, scala, classi, intervalli_osservati) -->
- **IVP · Su quali suoli insiste la sughereta?** — Ogni unità pedologica riceve un punteggio da 1 (Molto bassa) a 4 (Alta); l'indice comunale è la media pesata per superficie. Classi osservate: Alta 3,26-3,99 (21 comuni), Media 2,57-2,99 (4), Bassa 2,00-2,48 (5). `icona: mountain`
- **IPI · Quanto è esposta al fuoco?** — Le sugherete sono incrociate con le cinque classi del Piano regionale antincendio 2023-2025 (Basso→Alto); l'indice comunale (scala 0-100) è la media pesata. Classi comunali osservate: Mediobasso 1 comune, Medio 3, Medioalto 20, Alto 6. Ogni scheda riporta anche la quota Medioalto+Alto. `icona: flame`
- **ICR · Quanto è continua o frammentata?** — Conta i complessi (patch) di sughereta e il peso del nucleo maggiore. Classi per quota del nucleo: Alta 80-97 % (9 comuni), Media 61-78 % (6), Bassa 43-59 % (8), Molto bassa 28-37 % (7). `icona: git-branch`

**Fonte:** P2, par. 2.2 pp. 19-21; Allegato I, nota metodologica p. 50 e schede pp. 52-141 (intervalli osservati: elaborazione del sito).

## Come leggere le classi {type=text}
Lo studio non pubblica soglie numeriche per le classi. Gli intervalli indicati sono quelli osservati nelle 30 schede comunali, che fanno fede (P2 pp.50-141). Le legende delle figure originali (IVP ≥ 3,50; ICR ≥ 70) non coincidono con la classificazione delle schede (P2 pp.28, 30).

## Suoli buoni quasi ovunque, fuoco quasi ovunque {type=text}
Il suolo è il fattore meno critico. Nelle schede 21 comuni sono in classe IVP Alta, 4 Media e 5 Bassa; il testo indica 22, 4 e 4 (P2 p.27; pp.50-141). I valori più alti sono a Oliena (3,987), Padru (3,971), Monti (3,936), Nuoro (3,908) e Telti (3,881). I più bassi ad Abbasanta (2,000), Pozzomaggiore e Aidomaggiore (2,001), Mores (2,477) e Ardara (2,480) (P2 pp.27-28).

Il fuoco è il fattore di pressione. Venti comuni hanno classe comunale Medioalto e sei Alto. Solo Bitti, Buddusò e Orune sono in classe Medio, Alà dei Sardi in Mediobasso (P2 pp.50-141). In 16 comuni oltre il 90 % della sughereta ricade nelle classi Medioalto e Alto. Lo studio ne cita otto, da Iglesias (98,28 %) a Calangianus (93,20 %) (P2 p.28). All'opposto Alà dei Sardi (3,58 %), Bitti (13,43 %) e Buddusò (16,94 %) (P2 p.28).

La continuità divide i territori. Nove comuni hanno ICR Alta, sei Media, otto Bassa e sette Molto bassa (P2 pp.50-141). A Buddusò il nucleo maggiore concentra il 97,02 % della sughereta; a Olbia il 28,20 %, in 78 complessi. Ozieri ne conta 80 (P2 pp.61-64, 76-79, 103-106). In totale le schede contano 882 complessi sughericoli nei 30 comuni.

## Esploratore: ordina e confronta i 30 comuni {type=chart id=esploratore}
<!-- Componente `Explorer` (pattern RankingsPage) + `DataTable` + `ComuneDrawer`. Unica interazione della sezione. -->
**Grafico:** barre orizzontali ordinabili (30 comuni) + tabella compatta con badge di classe — una barra per comune, lunghezza = valore dell'indice scelto, colore = classe (scala ordinale §4 del brief, sempre con etichetta testuale). Etichette dirette sui valori; su mobile la barra resta a piena larghezza e la tabella scorre in orizzontale nel proprio contenitore.
**Ordinamenti ("Ordina per"):** Ettari di sughereta (default, decrescente) · IVP · Quota Medioalto+Alto · Indice incendio (IPI) · Quota del nucleo maggiore · Numero di complessi. Ogni ordinamento è invertibile (crescente/decrescente).
**Filtri ("Mostra solo"):** tutte · IVP Alta/Media/Bassa · Incendio Mediobasso/Medio/Medioalto/Alto · ICR Alta/Media/Bassa/Molto bassa · Profilo integrato (7 valori). Contatore "{n} comuni su 30"; "Azzera i filtri".
**Colonne della tabella ("Vedi i dati", accessibile, collassata):** Comune · ha · % Sughereta · IVP (badge classe) · IPI (badge classe) · % Medioalto+Alto · ICR (badge classe) · Complessi · Profilo integrato. Export CSV equivalente a `comuni-sughereta.csv`.
**Hover:** valore esatto, classe e profilo integrato ("{comune}: {valore} {unità}").
**Apertura del pannello:** click su barra o riga → pannello laterale `ComuneDrawer` con la scheda del comune; l'URL diventa `/sughero-sardegna?comune={{slug}}` ed è condivisibile. Il pannello è specificato in `04b-sughero-pannello-comune.md`. All'apertura della pagina con `?comune=slug` il pannello è già aperto sopra l'esploratore.
**Figure originali:** link "Vedi le figure originali dello studio (Fig. 2-4)" sotto il grafico → lightbox (blocchi seguenti).
**Dati:** data/sughero-sardegna/comuni-sughereta.json → `rank`, `nome_corrente`, `slug`, `sugherete_ha`, `peso_pct_sughereta_sardegna`, `ivp`, `classe_ivp`, `ipi`, `classe_incendio`, `quota_medioalto_alto_pct`, `n_complessi`, `quota_complesso_maggiore_pct`, `classe_icr`, `profilo_integrato`.
**Lettura:** Bitti, Berchidda, Oschiri e Buddusò superano i 5.000 ettari ciascuno e sommano il 26,1 % della Sughereta Sardegna. L'ordine cambia molto per indice: Alà dei Sardi è settima per ettari ma la meno esposta al fuoco.
**Fonte:** P2, Allegato I, quadro sinottico pp. 50-51 e schede comunali pp. 52-141. Grafico ricostruito dai dati delle schede, non dalle Figure 2-4.

## La figura originale dello studio: IVP {type=figure lightbox=solo}
<!-- SOLO in lightbox ("Vedi la figura originale"), mai a piena larghezza: i valori non coincidono con le schede. Etichetta obbligatoria: "Elaborazione grafica dello studio". -->
**Immagine:** source/parte2-filiera-sughero-sardegna/images/fig-2-ivp-ranking-30-comuni.jpeg
**Didascalia:** Figura 2. Indice di Vocazionalità Pedologica (IVP) – ranking dei 30 comuni. Elaborazione grafica dello studio (P2 p.28).
**Alt:** Grafico a barre dei 30 comuni ordinati per IVP, colorato per classe di vocazionalità.
**Nota:** Elaborazione grafica dello studio; i valori di riferimento sono quelli delle schede comunali. La figura include Oniferi, Dualchi e Noragugume, non tra i 30 comuni, e omette Ozieri, Calangianus e Olbia.

## La figura originale dello studio: IPI {type=figure lightbox=solo}
**Immagine:** source/parte2-filiera-sughero-sardegna/images/fig-3-ipi-pericolosita-incendio-30-comuni.jpeg
**Didascalia:** Figura 3. Indice di Pericolosità da Incendio (IPI) – classi per comune. Elaborazione grafica dello studio (P2 p.29).
**Alt:** Grafico a barre dei 30 comuni per indice di pericolosità da incendio, colorato per classe.
**Nota:** Elaborazione grafica dello studio; i valori di riferimento sono quelli delle schede comunali. I valori della figura differiscono dalle schede per 24 comuni su 30.

## La figura originale dello studio: ICR {type=figure lightbox=solo}
**Immagine:** source/parte2-filiera-sughero-sardegna/images/fig-4-icr-continuita-risorsa-30-comuni.jpeg
**Didascalia:** Figura 4. Indice di Continuità della Risorsa (ICR) – classi per comune. Elaborazione grafica dello studio (P2 p.30).
**Alt:** Grafico a barre dei 30 comuni per continuità della risorsa, colorato per classe.
**Nota:** Elaborazione grafica dello studio; i valori di riferimento sono quelli delle schede comunali. La figura riporta Nuoro due volte e non riporta Ardara.

## Quattro ettari su dieci sono in classe di pericolo Alto {type=chart}
**Grafico:** barre impilate al 100 % (una sola barra) — ripartizione degli 83.790,90 ha dei 30 comuni per classe di pericolo incendio, da Basso ad Alto.
**Dati:** data/sughero-sardegna/sintesi-regionale.json → `superficie_per_classe_incendio_ha`, `superficie_per_classe_incendio_pct` (Basso 495,47 ha, 0,59 %; Mediobasso 8.214,35 ha, 9,80 %; Medio 14.905,49 ha, 17,79 %; Medioalto 27.860,11 ha, 33,25 %; Alto 32.315,45 ha, 38,57 %).
**Lettura:** Il 38,6 % della sughereta dei 30 comuni è in classe Alto e il 33,2 % in Medioalto. Meno dell'1 % è in classe Basso.
**Fonte:** P2, Allegato I, tabelle "pericolo incendio" delle 30 schede, pp. 52-141 (somma regionale: elaborazione del sito).

## Leggere i tre indici insieme {type=text id=lettura-integrata}
Nessun indice da solo orienta una scelta. Le schede comunali combinano le tre classi in una matrice integrata: IVP × incendio × ICR (P2 p.50). Nei 30 comuni compaiono 17 combinazioni, ricondotte dallo studio a 7 profili integrati (P2 pp.52-141).

Un primo livello incrocia solo suolo e fuoco. Diciassette comuni sono "risorsa strategica vulnerabile": suoli vocati, pericolo Medioalto o Alto. Tre sono "risorsa vocata con criticità localizzate" (Bitti, Buddusò, Orune), uno "risorsa vocata e relativamente meno esposta" (Alà dei Sardi). Cinque sono "area critica o marginale esposta", quattro "risorsa compatibile ma fragile" (P2 pp.52-141).

La continuità aggiunge il terzo fattore. Distingue i comuni "governabili", con un nucleo accorpato, da quelli "frammentati", dove servono accordi territoriali e selezione dei nuclei (P2 pp.52-141).

## La matrice dei profili {type=chart}
**Grafico:** matrice (heatmap) — righe: classe IVP (Alta, Media, Bassa); colonne: classe incendio (Mediobasso, Medio, Medioalto, Alto); in ogni cella i comuni con il badge ICR; colore di cella = profilo integrato. Hover: nome e profilo; click su un comune → pannello scheda `?comune={{slug}}` (stessa destinazione dell'esploratore, nessuna interazione aggiuntiva).
**Dati:** data/sughero-sardegna/indici-definizioni.json → `profili_integrati[]` (`classe_ivp`, `classe_incendio`, `classe_icr`, `profilo_integrato`, `comuni`), `profili_ivp_x_incendio[]`; data/sughero-sardegna/comuni-sughereta.json → `nome_corrente`, `slug`.
**Lettura:** La colonna Medioalto raccoglie 20 comuni su 30. Le celle vuote (per esempio IVP Bassa con incendio Medio) non hanno profilo: lo studio descrive solo le combinazioni osservate.
**Fonte:** P2, Allegato I, matrici integrate delle 30 schede, pp. 52-141.

## Sette profili, dal più favorevole al più complesso {type=cards}
<!-- ordine editoriale; n. comuni da sintesi-regionale.json → conteggi_profilo_integrato. Il nome di ogni comune apre il pannello ?comune=slug. -->
- **Area vocata e relativamente governabile (3 comuni)** — Bitti, Buddusò, Alà dei Sardi: suoli vocati, fuoco contenuto, nucleo ben accorpato. È l'unico profilo senza richiamo a criticità. `icona: shield-check`
- **Area vocata, con gestione a mosaico (1)** — Orune: suoli vocati e pericolo Medio, ma risorsa policentrica (nucleo maggiore 50,16 %). `icona: grid`
- **Priorità alta: risorsa vocata, esposta e territorialmente governabile (8)** — Berchidda, Oschiri, Tempio Pausania, Telti, Illorai, Oliena, Bono, Bultei. Suoli buoni ed esposizione elevata, ma nuclei accorpati che consentono interventi coordinati. `icona: target`
- **Priorità alta ma gestione complessa: risorsa vocata, esposta e frammentata (9)** — Nuoro, Ozieri, Orani, Calangianus, Padru, Olbia, Benetutti, Pattada, Monti. Il profilo più frequente: suoli vocati, fuoco Medioalto o Alto, sughereta dispersa. `icona: puzzle`
- **Risorsa compatibile, esposta e gestibile con interventi coordinati (1)** — Iglesias: suoli di classe Media, pericolo Alto (98,28 %), ma un nucleo che concentra l'80,43 %. `icona: layers`
- **Risorsa compatibile ma fragile e frammentata (3)** — Villanova Monteleone, Chiaramonti, Ploaghe: suoli Media, esposizione Medioalto, nuclei frammentati. `icona: alert-triangle`
- **Area critica/marginale esposta: priorità selettiva (5)** — Mores, Pozzomaggiore, Abbasanta, Aidomaggiore, Ardara: suoli Bassa e pericolo Medioalto. Le schede chiedono di scegliere con cura le aree pilota. `icona: filter`

**Fonte:** P2, Allegato I, "Lettura integrata" delle 30 schede, pp. 52-141; conteggi: elaborazione del sito.

## Cosa chiede lo studio ai territori {type=text}
Le indicazioni operative delle schede sono sette frasi ricorrenti. Tutte le 30 schede chiedono verifiche locali su proprietà, accessibilità, stato selvicolturale e continuità del combustibile. Ventisei danno priorità alla prevenzione incendi e alla riduzione del combustibile nelle classi Medioalto e Alto. Ventuno invitano a usare la buona vocazionalità come base per progetti pilota, certificazione e gestione attiva. Quindici indicano il complesso principale come ambito per interventi coordinati; altre quindici una gestione a mosaico con accordi territoriali (P2 pp.52-141). Le strategie per profilo sono nel modello S.U.G.H.E.R.A. → /sughero-sardegna/innovazione#sughera.

## La cautela dello studio {type=quote}
> La scheda è una sintesi comunale. Per individuare puntualmente le porzioni di sughereta più strategiche e vulnerabili è opportuno procedere con overlay GIS diretto tra unità pedologiche riclassificate, classi di pericolosità incendio e complessi sughericoli.
— Allegato I, "Cautela metodologica" di ogni scheda comunale, pp. 52-141

## Come leggere i numeri di questa pagina {type=text}
Tutti i valori per comune vengono dalle 30 schede dell'Allegato I, verificate con il quadro sinottico (P2 pp.50-141). I conteggi del testo differiscono in due casi: IVP 22/4/4 contro 21/4/5 delle schede; ICR 8 comuni contro 9 (il testo non cita Aidomaggiore) (P2 pp.27-29). Le Figure 2, 3 e 4 derivano da una versione diversa dell'elaborazione: qui i grafici sono ricostruiti dalle schede. Per Bultei l'IVP dichiarato (3,395) differisce dal ricalcolo (3,448): si mantiene il valore dichiarato (P2 pp.139-141). Somme e quote regionali (71,8 %, 882 complessi, 26,1 %) sono elaborazioni del sito sui dati delle schede.

## Continua {type=cards}
<!-- card di navigazione a fine pagina -->
- **Innovazione e modello S.U.G.H.E.R.A.** — 153 ricerche internazionali in 12 ambiti, 9 direttrici, 11 strumenti di certificazione e il framework in sette passaggi con le conclusioni dello studio. → /sughero-sardegna/innovazione `icona: flask-conical`
- **Alta Gallura, il distretto del sughero** — Undici comuni, il principale polo italiano di lavorazione del sughero: demografia, ambiente e schede comunali. Calangianus e Tempio Pausania sono in entrambe le sezioni. → /alta-gallura `icona: map`

## Fonti {type=sources}
- Valorizzazione della filiera del sughero in Sardegna – Un framework multidisciplinare (RISSTE, 2025), Prima parte "Contesto strategico", pp. 15-17
- Idem, Seconda parte "Metodologia di analisi", par. 2.2 "Analisi territoriale", pp. 19-21; Figura 1, p. 26
- Idem, Terza parte, par. 3.1-3.2 (IVP, IPI, ICR), pp. 27-30 (Figure 2-4, pp. 28-30)
- Idem, Quarta parte, par. 4.1-4.2 "Gli indicatori territoriali", pp. 35-37; par. 4.5 "Un modello integrato", p. 42
- Idem, Allegato I "Studio tecnico sugherete – Dossier comunale integrato": nota metodologica e quadro sinottico pp. 50-51; schede comunali 01-30 pp. 52-141
- Le pagine indicate sono quelle fisiche del PDF; la numerazione stampata è inferiore di 17.
- Scarica lo studio integrale (PDF) → /progetto#documenti
