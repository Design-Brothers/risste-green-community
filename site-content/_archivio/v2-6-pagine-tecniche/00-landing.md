---
slug: /
sezione: home
eyebrow: "Green community UCAG 193"
title: "Green community Alta Gallura"
seo_title: "Green community UCAG 193 – Alta Gallura e sughero sardo"
description: "I risultati di due studi RISSTE per l'Unione dei Comuni Alta Gallura: demografia, sugherete, tre filiere ESG, roadmap di 36 mesi. Dati, mappe, PDF."
og_image: source/brand/copertina-sfondo.jpeg
fonti:
  - documento: parte1
    pagine: [3, 13, 14, 15, 18, 19, 21, 22, 23, 42, 72, 73, 79, 89, 90]
  - documento: parte2
    pagine: [15, 16, 20, 27, 28, 29, 42, 43, 50]
dati:
  - alta-gallura/kpi-sintesi.json
  - alta-gallura/popolazione-storica.json
  - alta-gallura/saldi-demografici.json
  - alta-gallura/filiere.json
  - alta-gallura/indicatori-esg.json
  - alta-gallura/roadmap.json
  - sughero-sardegna/sintesi-regionale.json
  - sughero-sardegna/contesto-sughero-sardegna.json
  - sughero-sardegna/comuni-sughereta.json
  - sughero-sardegna/framework-sughera.json
figure: []
---

<!-- Landing (ARCHITETTURA "Landing", BRIEF §3). Sequenza: hero immersivo → intro a capitoli (i 5 messaggi chiave, una schermata ciascuno, orbo che cambia colore; saltabile) → il progetto in 60 parole (#progetto) → 4 KPI → due porte → chi siamo. Solo lo sfondo si muove; il testo è fermo. Testo visibile ≈ 520 parole. -->

## Hero {type=hero}
**Titolo:** Green community / Alta Gallura
<!-- Titolo enorme (72-120 px, peso 300-400) spezzato su due righe alla barra. Su mobile una parola per riga: Green / community / Alta Gallura. -->
**Standfirst:** Due studi RISSTE leggono l'Alta Gallura con i dati: undici comuni, la demografia, le sugherete, tre filiere. Il secondo allarga lo sguardo ai 30 comuni sughericoli della Sardegna. Qui trovi i risultati in sintesi e i PDF integrali.
**CTA:** Esplora l'Alta Gallura → /alta-gallura
**CTA:** Scopri la Sughereta Sardegna → /sughero-sardegna
**Parola fantasma:** UCAG 193
<!-- Outline 1 px al 20 %, tagliata dai bordi dietro l'orbo principale. Alternativa: ALTA GALLURA. -->
**Micro-etichette:** RISSTE — · — UCAG 193 · 11 COMUNI · 30 COMUNI · 2025
<!-- Posizioni: alto-sinistra "RISSTE —"; alto-destra "— UCAG 193"; sull'orbo verde "11 COMUNI"; sull'orbo ambra "30 COMUNI"; basso-destra "2025". 11-12 px maiuscole, tracking 0,08 em. -->
**Orbi:** verde acido #7CFF3F · verde #4E9A3F · ciano #3FE9FF · blu #2F6FB0 · ambra #E8C28E (5 orbi, cuore bianco sfumato, grana 8-12 %)
**Fonte:** P1 pp. 13-15, 22; P2 pp. 16, 20

## Illustrazione di apertura {type=visual}
**Elemento:** `HeroOrbs` variant `landing` a piena altezza, dietro il titolo. Cinque orbi sfumati e sgranati (blur 48 px, grana 8-12 %) più il cuore bianco. Colori, dall'alto: `--acid`→`--cyan`, `--green`→`--acid`, `--cyan`→`--blue`, `--blue`→`--cyan`, `--cork-light`→`--cork`. Diametri 520, 460, 420, 380 e 360 px; cuore bianco `#FFFFFF`→`#DFFCF6` di 220 px al centro. Gli orbi occupano i due terzi destri dello schermo; il titolo sta a sinistra su sette colonne. `GhostWord` "UCAG 193" in outline 1 px al 18 %, dietro l'orbo principale, tagliata dal bordo destro. `MicroLabel`: "RISSTE —" alto-sinistra, "— UCAG 193" alto-destra, "11 COMUNI" sull'orbo verde, "30 COMUNI" sull'orbo ambra, "2025" basso-destra.
**Animazione:** Ogni orbo deriva su un percorso ellittico proprio: ampiezza 12-30 px, ciclo 18-30 s, easing sinusoidale. Il cuore bianco respira (scala 1→1,04) in 12 s. Allo scroll lo sfondo sale più lento del testo: parallasse −120 px nei primi 800 px. Al puntatore gli orbi si spostano del 2-4 % in direzioni alternate, con inerzia. Micro-etichette e parola-fantasma non si muovono; il testo mai. Con `prefers-reduced-motion` tutto resta fermo nella posizione iniziale.
**Significato:** Cinque luci per cinque messaggi, con il bianco al centro: il territorio come sistema vivo, non come mappa.
**Fallback:** Statico: orbi nella posizione iniziale, senza deriva né parallasse; la grana resta. Mobile (< 768 px): tre orbi (verde, ciano, ambra) da 260-320 px e blur 32 px. Parola-fantasma a 28 vw; restano solo le etichette "RISSTE —" e "— UCAG 193".

## Introduzione {type=intro}
<!-- I cinque messaggi chiave (BRIEF §1) come capitoli scroll-driven (COMPONENTI §5b). Sostituisce i cinque blocchi {type=message}: titoli, numeri, orbi, parole-fantasma e fonti sono gli stessi. Sequenza degli orbi: verde → ciano → blu → ambra → verde. Le CTA di sezione sono nelle due porte più sotto. -->
**Salta a:** #progetto

### 01 · Un territorio a due velocità
**Numero:** 301 | anziani ogni 100 giovani
**Contesto:** Santa Teresa Gallura +16,14 %, Bortigiadas −20,43 % dal 2001 al 2023; l'Unione tiene grazie ai nuovi residenti (+3.286 contro −3.402).
**Scena:** orbo · `--green` → `--acid` · destra, grande (70 vmin) · "DUE VELOCITÀ"
**Dati:** data/alta-gallura/kpi-sintesi.json → indice_vecchiaia_2025; popolazione-storica.json → var_pct_2001_2023; saldi-demografici.json
**Fonte:** P1, Tab. 1a-1b, pp. 21-23

### 02 · Il sughero è l'infrastruttura identitaria
**Numero:** >80 | % del sughero lavorato in Italia
**Contesto:** L'Alta Gallura lavora oltre l'80 % del sughero italiano; la Sardegna ospita circa il 90 % delle sugherete nazionali.
**Scena:** orbo · `--cyan` → `--green` · si sposta al centro-destra e si allarga · "SUGHERO"
**Dati:** data/sughero-sardegna/contesto-sughero-sardegna.json → quota_superfici_italiane_sughereta_pct
**Fonte:** P1, pp. 42-43; P2, p. 16

### 03 · La risorsa non basta: contano suolo, fuoco e continuità
**Numero:** 21 | comuni su 30 con suoli vocati
**Contesto:** Trenta comuni, 83.790,90 ettari, tre indici: suolo [[IVP]], fuoco [[IPI]], continuità [[ICR]]; in 16 oltre il 90 % è in pericolo alto.
**Scena:** orbo · `--blue` → `--cyan` · scende in basso a destra, più compatto · "IVP · IPI · ICR"
**Dati:** data/sughero-sardegna/sintesi-regionale.json → conteggi_classe_ivp.dataset; comuni-sughereta.json → quota_medioalto_alto_pct
**Fonte:** P2, par. 3.2, pp. 27-29; Allegato I, pp. 50-141 (il testo indica 22 comuni a IVP alta; le schede 21)

### 04 · Tre filiere, un metodo ESG
**Numero:** 3 | filiere
**Contesto:** Bosco-sughero, bovina estensiva, suinicola agroforestale controllata: 56 indicatori ambientali, sociali e di governance, tenuti insieme dai contratti di filiera.
**Scena:** orbo · `--cork-light` → `--cork` · risale a destra, con tre lobi appena distinti (le tre filiere) · "ESG"
**Dati:** data/alta-gallura/filiere.json; indicatori-esg.json
**Fonte:** P1, pp. 72-73, 79, 81-88

### 05 · Trentasei mesi e un modello replicabile
**Numero:** 36 | mesi
**Contesto:** Quattro fasi: baseline, sei comuni pilota, Living Lab, certificazione di gruppo; per la Sardegna il modello [[SUGHERA]] in sette passi.
**Scena:** orbo · `--acid` → `--green` · torna a destra, grande; dietro compaiono gli anelli di decortica verde-ciano · "36 MESI"
**Dati:** data/alta-gallura/roadmap.json → tipo=fase; sughero-sardegna/framework-sughera.json
**Fonte:** P1, Fig. 4f, p. 90; par. 4.7, pp. 89-92; P2, pp. 42-43

## Un progetto per gestire il capitale naturale, non solo conservarlo {type=text id=progetto}
<!-- "Il progetto in 60 parole": 60 parole esatte, da leggere in un colpo d'occhio. -->
La Green community UCAG 193 è il progetto dell'Unione dei Comuni Alta Gallura per la transizione ecologica. Si fonda sulla gestione attiva del capitale naturale, nel quadro della Legge 221/2015 e del [[PNRR]]. RISSTE ha prodotto due studi: uno sull'Alta Gallura, l'altro sulla filiera del sughero in Sardegna. Questo sito ne racconta i risultati con dati, mappe e figure.

**CTA:** Conosci il progetto → /progetto
**Fonte:** P1, Premessa, pp. 13-15

## Undici comuni e oltre l'80 % del sughero lavorato in Italia {type=kpi}
<!-- Blocco statistiche (BRIEF §3): numero grande, linea sottile verso il semicerchio sfumato, card bianche a destra, pillola con la fonte. valore | unità | etichetta | contesto | fonte -->
- 11 | comuni | Comuni dell'Unione Alta Gallura | Quattro sulla costa e sette nell'entroterra, dal mare al Limbara. | P1 p.22
- 35.242 | abitanti | Residenti al 1° gennaio 2025 | Erano 36.694 nel 2001: −4,02 % al 2023. | P1 pp.21-22
- >80 | % | Sughero lavorato in Italia che passa dall'Alta Gallura | Il distretto presidia e gestisce la filiera nazionale del sughero. | P1 p.42
- 83.790,90 | ha | Sugherete nei 30 comuni prioritari della Sardegna | È il nucleo della "Sughereta Sardegna" studiata dal secondo rapporto. | P2 p.27

## Due studi, due percorsi di lettura {type=cards}
<!-- Due card-porta a piena larghezza, una verde e una ambra, con il cerchio di decortica a 12 anelli come motivo. -->
- **Alta Gallura · Green community** — Undici comuni e 35.242 abitanti, con la costa che cresce e l'interno che si spopola. Tre filiere misurate con criteri [[ESG]] e una roadmap di 36 mesi con aree pilota e cabina di regia. → /alta-gallura `icona: tree`
- **Sughero Sardegna · La filiera regionale** — La Sardegna ospita circa il 90 % delle sugherete italiane. Trenta comuni prioritari letti con tre indici: suolo, fuoco, continuità. Le direttrici di innovazione internazionali e il framework [[SUGHERA]] per decidere. → /sughero-sardegna `icona: layers`

**Fonte:** P1 pp. 22, 79-90; P2 pp. 16, 20, 42

## Chi ha scritto gli studi e per chi {type=text}
Gli studi sono opera di R.I.S.S.T.E., Centro Studi per la Ricerca, l'Innovazione, lo Sviluppo Sostenibile e la Transizione Energetica. Ha sede a Olbia ed è un istituto di ricerca privato accreditato. Il lavoro è realizzato per l'Unione dei Comuni Alta Gallura ([[UCAG]]), progetto Green community UCAG 193, CUP E77G24000450002. Il gruppo di lavoro riunisce cinque professionisti: diritto amministrativo, biologia, agronomia, pianificazione ambientale ed economia.

<!-- Loghi: RISSTE (source/brand/), Unione dei Comuni Alta Gallura, PNRR e Regione Sardegna se richiesti dal finanziamento (da procurare). -->

**CTA:** Conosci il progetto e il gruppo di lavoro → /progetto
**CTA:** Scarica gli studi integrali (PDF) → /progetto#documenti
**Fonte:** P1, frontespizio p. 3 e par. vii, pp. 18-19

## Fonti {type=sources}
- Green community UCAG 193 – Strategie territoriali integrate (RISSTE, 2025), Premessa e Quadro metodologico, pp. 13-19
- Green community UCAG 193, Prima parte – Demografia, Tab. 1a-1b, pp. 21-23
- Green community UCAG 193, Seconda parte – Ambiente e territorio, pp. 42-43
- Green community UCAG 193, Quarta parte – Framework ESG, filiere e Roadmap operativa, pp. 72-73, 79-92
- Valorizzazione della filiera del sughero in Sardegna (RISSTE, 2025), Contesto strategico, pp. 15-16
- Valorizzazione della filiera del sughero in Sardegna, Metodologia e Risultati, pp. 20, 27-29; Allegato I, pp. 50-141
- Valorizzazione della filiera del sughero in Sardegna, Quarta parte – Framework S.U.G.H.E.R.A., pp. 42-43
