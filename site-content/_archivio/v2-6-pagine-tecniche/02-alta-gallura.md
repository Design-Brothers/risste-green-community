---
slug: /alta-gallura
sezione: alta-gallura
eyebrow: "Alta Gallura"
title: "Un territorio a due velocità"
seo_title: "Alta Gallura, un territorio a due velocità – UCAG 193"
description: "Undici comuni e 35.242 abitanti tra costa e Limbara: popolazione 2001-2025, saldi, imprese, scenari 2035, sugherete e Natura 2000. Con la scheda di ogni comune."
og_image: source/parte1-green-community-alta-gallura/images/fig-3a-quadro-sinottico-comuni.jpeg
ancore:                                  # id delle sezioni raggiungibili con /alta-gallura#… (sottomenu in pagina)
  - popolazione
  - saldi
  - eta
  - imprese
  - ambiente
  - comuni
fonti:
  - documento: parte1
    pagine: [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 35, 37, 39, 40, 41, 42, 43, 44, 45, 46, 48, 53, 55, 56, 58, 63, 64, 66, 67, 70, 71, 79, 98, 103, 114, 115, 116, 126, 134, 136, 141, 151, 152, 156, 159, 161, 162, 165, 166, 168, 169, 171, 172, 178, 183, 189]
dati:
  - alta-gallura/kpi-sintesi.json
  - alta-gallura/popolazione-storica.json
  - alta-gallura/saldi-demografici.json
  - alta-gallura/confronto-costa-entroterra.json
  - alta-gallura/struttura-eta.json
  - alta-gallura/famiglie.json
  - alta-gallura/stranieri-e-scuola.json
  - alta-gallura/imprese.json
  - alta-gallura/scenari-2035.json
  - alta-gallura/uso-suolo-comuni.json
  - alta-gallura/superfici-unione.json
  - alta-gallura/natura-2000-e-vincoli.json
  - alta-gallura/schede-comuni.json
  - alta-gallura/sintesi-comparativa-comuni.json
  - alta-gallura/pedologia-comuni.json
figure:
  - parte1-green-community-alta-gallura/images/fig-3a-quadro-sinottico-comuni.jpeg
  - parte1-green-community-alta-gallura/images/fig-1a-analisi-demografico-economica-imprese.png
---

**Ancore:** `#popolazione` → "La costa cresce, l'entroterra si spopola" · `#saldi` → "Nascono meno persone di quante ne muoiano, in ogni comune" · `#eta` → "Tre anziani ogni giovane" · `#imprese` → "Le imprese tengono, ma cambiano pelle" · `#ambiente` → "Il sughero è l'infrastruttura identitaria" · `#comuni` → "Ogni comune ha un ruolo". Il pannello scheda comune si apre con `?comune=slug` (specifica in `02b-alta-gallura-pannello-comune.md`).

<!-- Pagina unica della sezione (ARCHITETTURA `/alta-gallura`): fonde i v1 02-hub, 03-territorio, 04-comuni. Ordine: hero con fig-3a → popolazione → saldi → età/famiglie/stranieri/scuola → imprese e scenari → ambiente → gli 11 comuni con mappa, filtro e pannello. -->
<!-- Interazioni: (1) selettore comune sullo slope chart, che evidenzia la stessa linea/barra in tutti i grafici demografici; (2) filtro "Tutti · Costa · Interno" su mappa e griglia; (3) click su mappa, card o barra → pannello scheda (`?comune=slug`). Colori: costa blu, interno verde. Motivo grafico dell'hero: due orbi (verde interno, blu costa) descritti nel blocco visual; poi l'intro a capitoli (BRIEF §3). -->

## Hero {type=hero}
**Standfirst:** L'Unione dei Comuni dell'Alta Gallura riunisce 35.242 abitanti tra la costa e il Monte Limbara. La costa cresce del 14,0 %, l'entroterra perde il 10,1 %. Lo studio RISSTE legge i due assi come un solo sistema, con il sughero al centro.
**CTA:** Scegli il tuo comune → /alta-gallura#comuni
**CTA:** Vai alla strategia → /alta-gallura/strategia
**Figura hero:** source/parte1-green-community-alta-gallura/images/fig-3a-quadro-sinottico-comuni.jpeg — a piena larghezza sotto lo standfirst, con "Ingrandisci" (lightbox) e fonte.
**Didascalia:** Figura 3a. Schema sinottico dei comuni dell'Alta Gallura: articolazione territoriale, dinamiche demografiche e vocazioni strategiche nell'ambito della Green community.
**Alt:** Mappa degli undici comuni dell'Alta Gallura, costa e interno, con schede sintetiche su demografia e vocazioni.

## Illustrazione di apertura {type=visual}
**Elemento:** `HeroOrbs` con palette `alta-gallura` estesa a due orbi, blur 48 px e grana 8-12 %. Verde (`--green` → `--acid`, 480 px) per l'interno e il Limbara: in basso a sinistra, dietro lo standfirst. Blu (`--blue` → `--cyan`, 420 px) per la costa: in alto a destra. `GhostWord` "DUE VELOCITÀ" in outline 1 px al 18 %, tra i due orbi, tagliata dal bordo destro. `MicroLabel` "INTERNO" sull'orbo verde, "COSTA" su quello blu, "— ALTA GALLURA" in alto a destra. La Figura 3a resta sotto lo standfirst, a piena larghezza, sopra gli orbi. Il blocco KPI «L'Alta Gallura in quattro numeri» usa `StatArc` tone `green`: numeri a sinistra, arco con tacche, card a destra.
**Animazione:** I due orbi si allontanano piano: il blu sale verso destra, il verde scende verso sinistra, poi tornano; ciclo 24 s. Deriva propria di 12-16 px, easing sinusoidale. Allo scroll parallasse −100 px nei primi 800 px; al puntatore spostamento del 2 %. Nell'intro a capitoli gli stessi orbi continuano la scena (vedi blocco intro). Con `prefers-reduced-motion` restano fermi alla distanza massima.
**Significato:** Due luci che si separano: costa e interno divergono, e il numero della pagina è questa distanza.
**Fallback:** Statico: orbi alla distanza massima, parola-fantasma fissa. Mobile: orbi da 260 px, uno sopra e uno sotto il titolo; parola-fantasma 28 vw; resta solo l'etichetta "— ALTA GALLURA".

## Introduzione {type=intro}
<!-- Quattro capitoli con i numeri principali della sezione (ARCHITETTURA `/alta-gallura` punto 0; COMPONENTI §5b). Numeri e fonti dal blocco KPI "L'Alta Gallura in quattro numeri" e dal blocco #popolazione. Scena: i due orbi dell'hero (verde interno, blu costa) si allontanano; nell'ultimo capitolo entrano gli anelli di decortica verde-ciano. -->
**Salta a:** #popolazione

### 01 · Undici comuni, 35.242 abitanti tra costa e Limbara
**Numero:** 35.242 | abitanti (2025)
**Contesto:** Erano 36.694 nel 2001: −4,02 % fino al 2023, poi una lieve ripresa.
**Scena:** due orbi vicini · verde `--green` → `--acid` e blu `--blue` → `--cyan` · centro-destra, quasi sovrapposti · "ALTA GALLURA"
**Dati:** data/alta-gallura/kpi-sintesi.json; popolazione-storica.json → abitanti_2001, abitanti_2025
**Fonte:** P1 pp. 21-22

### 02 · La costa cresce, l'entroterra si spopola
**Numero:** +16,14 / −20,43 | % (2001-2023)
**Contesto:** Santa Teresa Gallura +16,14 %, Bortigiadas −20,43 %: le due traiettorie estreme tra 2001 e 2023.
**Scena:** due orbi in allontanamento · blu `--blue` → `--cyan` e verde `--green` → `--acid` · costa alto-destra, interno basso-sinistra · "DUE VELOCITÀ"
**Dati:** data/alta-gallura/popolazione-storica.json → var_pct_2001_2023
**Fonte:** P1, Tab. 1a, p. 22

### 03 · Nascono meno persone di quante ne muoiano
**Numero:** −3.402 / +3.286 | persone (2002-2023)
**Contesto:** Saldo naturale negativo in tutti gli undici comuni; il saldo migratorio copre il 96,6 % del deficit, il 77,2 % sulla costa.
**Scena:** due orbi distanti · il verde si restringe e si scurisce (`--green` → `#389848`), il blu cresce (`--blue` → `--cyan`) · "SALDI"
**Dati:** data/alta-gallura/saldi-demografici.json → saldo_naturale_2002_2023, saldo_migratorio_2002_2023
**Fonte:** P1, Tab. 1b, pp. 22-23

### 04 · Tre anziani ogni giovane
**Numero:** 301,54 | anziani ogni 100 giovani (2025)
**Contesto:** 9.791 over 65 contro 3.247 ragazzi sotto i 15 anni.
**Scena:** anelli `DecorticaRings` tone green (`--green` → `--cyan`) · centro-destra, 60 vmin, rotazione lenta; gli orbi sfumano dietro · "TRE A UNO"
**Dati:** data/alta-gallura/kpi-sintesi.json → indice_vecchiaia_2025; struttura-eta.json → anno 2025
**Fonte:** P1 p. 23

## L'Alta Gallura in quattro numeri {type=kpi}
<!-- valore | unità | etichetta | contesto | fonte -->
<!-- Layout StatArc tone green (COMPONENTI §7): numeri a sinistra, arco con tacche, card a destra. -->
- 35.242 | abitanti | Residenti al 1° gennaio 2025 | Dai 36.694 del 2001: −4,02 % fino al 2023, poi una lieve ripresa. | P1 pp.21-22
- −3.402 | persone | Saldo naturale 2002-2023 | Nati meno morti: negativo in tutti gli undici comuni. | P1 p.22
- +3.286 | persone | Saldo migratorio 2002-2023 | Copre il 96,6 % del deficit naturale; il 77,2 % arriva sulla costa. | P1 p.22
- 301,54 | anziani per 100 giovani | Indice di vecchiaia 2025 | 9.791 over 65 contro 3.247 ragazzi sotto i 15 anni. | P1 p.23

## La costa cresce, l'entroterra si spopola {type=text id=popolazione}
Lo studio descrive l'Alta Gallura come un sistema "a due velocità" (P1 p.21). Tra il 2001 e il 2025 la fascia costiera passa da 9.308 a 10.616 residenti (+14,0 %). L'entroterra scende da 27.386 a 24.626, cioè 2.760 abitanti in meno (−10,1 %) (P1 p.25). Nel periodo 2001-2023 crescono Santa Teresa Gallura (+16,14 %), Trinità d'Agultu e Vignola (+15,87 %) e Aglientu (+7,69 %). Bortigiadas (−20,43 %), Calangianus (−18,34 %) e Aggius (−16,26 %) registrano le perdite maggiori (P1 p.22).

Lo studio collega il calo di Calangianus alla crisi delle filiere tradizionali del sughero e del granito (P1 p.25). Il dualismo non è una condanna: lo studio lo assume come punto di partenza per una strategia unitaria. L'interno mantiene il capitale naturale, la costa ne apre i mercati (P1 p.79). La popolazione è "l'infrastruttura viva" che tiene in piedi boschi e filiere (P1 p.21).

## Popolazione 2001 → 2025: undici traiettorie {type=chart}
**Grafico:** slope chart — abitanti 2001 e 2025 per comune, costa in blu e interno in verde; selettore comune che evidenzia una linea (interazione condivisa con gli altri grafici demografici); etichette dirette con la variazione % 2001-2023.
**Dati:** data/alta-gallura/popolazione-storica.json → `dati[]`: `comune`, `slug`, `fascia`, `abitanti_2001`, `abitanti_2011`, `abitanti_2023`, `abitanti_2025`, `var_pct_2001_2023`; righe `fascia-costiera` e `fascia-interna` per i totali di fascia (`var_pct_2001_2025`: +14,0 / −10,1).
**Lettura:** Quattro linee salgono, sette scendono. Tempio Pausania resta il centro maggiore (13.036 abitanti) ma perde 849 residenti tra 2001 e 2023.
**Fonte:** P1, Tabella 1a, p.22; Tabella 1c, p.25

## Nascono meno persone di quante ne muoiano, in ogni comune {type=chart id=saldi}
**Grafico:** barre divergenti per comune — saldo naturale (a sinistra, negativo) e saldo migratorio (a destra) cumulati 2002-2023; ordinamento per popolazione; in testa le due righe di fascia e il totale Unione.
**Dati:** data/alta-gallura/saldi-demografici.json → `dati[]`: `comune`, `slug`, `fascia`, `livello` (`comune` | `aggregato`), `saldo_naturale_2002_2023`, `saldo_migratorio_2002_2023`, `incidenza_prevalente` (tooltip). Totali per asse anche in data/alta-gallura/confronto-costa-entroterra.json → `dati[]` con `indicatore` = `saldo_naturale_2002_2023`, `saldo_migratorio_2002_2023`: `fascia_costiera`, `entroterra`. Viddalba ha valori `null`: mostrare "Dato non riportato nello studio.", non zero.
**Lettura:** Sulla costa il saldo migratorio (+2.538) supera di quasi tre volte le perdite naturali (−861). Nell'entroterra i nuovi arrivi (+748) coprono solo il 29,4 % del deficit naturale (−2.541).
**Fonte:** P1, Tabella 1b, p.23; Tabella 1c, pp.25-26; par. 1.7.2, p.26; Allegato I, pp. 97-139

## Tre anziani ogni giovane {type=text id=eta}
Al 1° gennaio 2025 i ragazzi sotto i 15 anni sono 3.247 (9,21 %). Le persone in età attiva sono 22.204 (63,00 %), gli over 65 sono 9.791 (27,78 %) (P1 p.23). L'indice di vecchiaia dell'Unione è 301,54: oltre 301 anziani ogni 100 giovani. L'indice di dipendenza è 58,72: circa 59 persone a carico ogni 100 in età lavorativa (P1 p.24). L'età media è 49,6 anni, da 48,2 a Trinità d'Agultu a 52,6 a Bortigiadas (P1 p.24).

Nelle schede comunali l'indice di vecchiaia va da 230,6 a Luras a 368,3 a Trinità d'Agultu e Vignola (P1 pp.126, 141). Trinità è anche l'unico comune che ringiovanisce: età media da 49,5 (2023) a 48,2 anni (2025) (P1 p.141). Lo studio risponde con le filiere come presidio e con l'inclusione di giovani, donne e nuovi residenti (P1 pp.70-71).

## Vent'anni dopo: meno giovani e più anziani ovunque {type=chart}
**Grafico:** barre impilate al 100 % — quote 0-14 / 15-64 / 65+ per comune, al 1° gennaio 2002 e 2025 affiancati; riga Unione 2025 come riferimento.
**Dati:** data/alta-gallura/struttura-eta.json → `dati[]` filtrati per `anno` ∈ {2002, 2025}: `comune`, `slug`, `classe_0_14`, `classe_15_64`, `classe_65_piu`, `totale`, `indice_vecchiaia`, `eta_media` (tooltip). Non confrontare 2011 e 2023 con la Tabella 1a: le date di riferimento sono diverse.
**Lettura:** Nel 2002 gli over 65 erano il 16,6 % a Tempio Pausania e il 17,7 % a Calangianus. Nel 2025 sono il 27,1 % e il 29,6 %. Bortigiadas arriva al 33,7 %.
**Fonte:** P1, par. 1.4, pp.23-24; Allegato I, pp. 98-146

## Famiglie più numerose, ma più piccole {type=kpi}
<!-- valore | unità | etichetta | contesto | fonte -->
- +19,41 | % | Famiglie in più tra 2003 e 2023 | Da 13.925 a 16.628 nuclei, mentre la popolazione cala. | P1 p.23
- 2,12 | persone per famiglia | Componenti medi nel 2023 | Erano 2,63 nel 2003; Aglientu scende a 1,67, Calangianus resta a 2,33. | P1 p.23; All. I pp.103, 115
- 2.151 | persone | Residenti stranieri (2025) | Il 6,10 % del totale: 11,4 % sulla costa, 3,8 % nell'entroterra. | P1 pp.24, 26
- 4.295 | ragazzi | Utenza scolastica 0-18 anni (2025) | Tempio Pausania ne accoglie 1.649 (38,4 %); l'entroterra il 72,6 %. | P1 pp.24, 27

## Chi arriva e chi va a scuola {type=text}
Gli stranieri hanno provenienze diverse lungo i due assi. A Santa Teresa Gallura e a Luras i cittadini romeni superano rispettivamente il 53 % e il 59 % degli stranieri (P1 p.24). A Trinità d'Agultu e Vignola la comunità pakistana è il 34,88 % degli stranieri residenti, con un'incidenza complessiva del 18,8 % (P1 pp.24, 141). Nell'entroterra Tempio Pausania e Calangianus accolgono famiglie dal Marocco, dal Senegal e dall'Argentina (P1 p.24).

I bambini stranieri sostengono i servizi per l'infanzia: a Tempio Pausania sono il 37,0 % dei bambini di un anno (P1 p.136). Lo studio li considera un fattore determinante per la sopravvivenza dei presidi scolastici (P1 p.24). Nei piccoli centri costieri, Badesi (159 ragazzi) e Aglientu (147), le autonomie scolastiche restano fragili (P1 p.27). La leva indicata è il sostegno alla residenzialità stabile di giovani e famiglie (P1 p.71).

## Le imprese tengono, ma cambiano pelle {type=text id=imprese}
Le imprese attive sono 4.792 nel 2025, quasi quante nel 2021 (4.801, −0,19 %) (P1 p.28). Sotto la stabilità si muove una terziarizzazione: i Servizi crescono del 6,67 % e valgono il 33,37 % del totale. Il Commercio cala dell'8,93 %, l'Industria manifatturiera dell'11,69 % (P1 p.30).

Tempio Pausania concentra il 33,68 % delle imprese dell'Unione (1.614). Calangianus ha l'incidenza industriale più alta, 19,77 %, legata alla trasformazione del sughero (P1 pp.27-28). Luras (+11,26 %) e Luogosanto (+6,00 %) sono i comuni interni che crescono di più. La leva indicata è il rilancio occupazionale del distretto del sughero (P1 p.30).

## Imprese 2021 → 2025: chi cresce e chi cala {type=chart}
**Grafico:** barre orizzontali ordinate — imprese attive 2025 per comune, con etichetta della variazione % 2021-2025 (freccia); costa e interno nei due colori.
**Dati:** data/alta-gallura/imprese.json → `dati[]` con `livello` = `comune`: `comune`, `slug`, `fascia`, `imprese_2021`, `imprese_2025`, `var_pct_2021_2025`. I settori 2025 (`servizi_2025`, `agricoltura_2025`, `costruzioni_2025`, `commercio_2025`, `industria_2025`) solo in tooltip: `null` significa "non citato nel testo", non zero. Viddalba: `imprese_2021` è `null`, mostrare solo 2025 e variazione.
**Lettura:** Tempio Pausania (1.614) e Santa Teresa Gallura (731) sono le due economie maggiori. Le variazioni sono contenute: da −7,00 % a Bortigiadas a +11,26 % a Luras.
**Fonte:** P1, par. 1.8 e Figura 1a, pp.27-29

## L'analisi comune per comune {type=figure}
<!-- Solo in lightbox (ARCHITETTURA §/alta-gallura punto 5): in pagina una miniatura con "Ingrandisci" -->
**Immagine:** source/parte1-green-community-alta-gallura/images/fig-1a-analisi-demografico-economica-imprese.png
**Didascalia:** Figura 1a. Analisi demografico-economica sulle attività produttive degli 11 Comuni dell'Alta Gallura: Aggius (A), Aglientu (B), Badesi (C), Bortigiadas (D), Calangianus (E), Luogosanto (F), Luras (G), Santa Teresa di Gallura (H), Tempio Pausania (I), Trinità d'Agultu e Vignola (L), Viddalba (M).
**Alt:** Undici grafici con imprese attive 2021 e 2025 e ripartizione per settore economico, uno per comune.

## Servizi in crescita, industria e commercio in calo {type=chart}
**Grafico:** barre orizzontali — imprese 2025 per macro-settore, con variazione % 2021-2025 in etichetta e quota sul totale.
**Dati:** data/alta-gallura/imprese.json → `macro_settori_unione[]`: `macro_settore`, `codice`, `imprese_2021`, `imprese_2023`, `imprese_2025`, `quota_2025_pct`, `var_pct_2021_2025` (escludere la riga `totale`).
**Lettura:** Servizi 1.599 (+6,67 %), Agricoltura 980 (+0,51 %), Costruzioni 839 (+3,45 %), Commercio 714 (−8,93 %), Industria 423 (−11,69 %).
**Fonte:** P1, Tabella 1d, p.30

## Costa e interno, due modelli economici {type=text}
La costa ha 1.561 imprese: i Servizi sono il 43,43 %, l'Industria manifatturiera il 5,57 % (P1 p.29). L'entroterra ne ha 3.231, con Agricoltura al 21,91 %, Costruzioni al 19,37 % e Industria al 10,40 % (P1 pp.29-30). Due modelli: terziario-turistico sulla costa, diversificato tradizionale-manifatturiero nell'interno, con il sughero di Calangianus e il granito di Tempio (P1 p.30).

## Tre scenari per il 2035 {type=cards}
<!-- Da scenari-2035.json → dati[] (livello Unione). Tre card affiancate, ordine: attrattivo · lineare · crisi -->
- **Attrattivo ed espansivo — circa 36.500 abitanti** — Occupazione stabile in sughero e granito, costa più attrattiva. Imprese a circa 5.110 (+6,6 %) con densità al 14,0 %. `icona: trending-up`
- **Lineare e inerziale — circa 34.100 abitanti** — Prosegue la dinamica 2011-2023: costa in crescita, borghi interni in calo. Imprese a circa 4.637 (−3,2 %) con densità costante al 13,6 %. `icona: minus`
- **Accentuato di crisi — circa 32.400 abitanti** — La mortalità della coorte over 65 supera l'attrazione migratoria; calano costa e interno. Imprese a circa 4.147 (−13,4 %) con densità al 12,8 %. `icona: trending-down`

## Come leggere gli scenari {type=text}
Le proiezioni applicano il tasso medio annuo 2011-2023 alla popolazione del 2025 (P1 p.24, nota 1). Le imprese derivano dalla densità imprenditoriale: 136 imprese ogni 1.000 abitanti nel 2025 (P1 p.30). Sono ordini di grandezza, indicati come "circa" nel testo (P1 pp.24-25, 30-31). Lo scenario attrattivo è quello che la Green community vuole rendere possibile.

## Il sughero è l'infrastruttura identitaria {type=text id=ambiente}
L'Alta Gallura lavora oltre l'80 % del sughero italiano (P1 p.42). Le sugherete sono gestite con turni di estrazione di dodici anni, adattati ai suoli granitici. Lo studio le descrive come infrastrutture verdi: serbatoi di carbonio, difesa dal fuoco e dall'erosione, habitat di biodiversità (P1 pp.42-43). Una sughereta attiva e produttiva coincide spesso con una sughereta più resiliente (P1 p.43).

Il territorio ricade nei Distretti forestali 01 Alta Gallura e 04 Coghinas-Limbara, che non coincidono con i confini comunali (P1 p.42). Il Monte Limbara, 1.359 metri, è il nodo morfologico e climatico dell'area (P1 p.39). I suoli granitici, acidi e poco profondi sono adatti alla sughera, ma fragili all'erosione (P1 pp.40, 48).

## L'ambiente in quattro numeri {type=kpi}
<!-- valore | unità | etichetta | contesto | fonte -->
- 150.251 | ha | Distretto forestale 01 Alta Gallura | Il 6,2 % della superficie regionale; il Distretto 04 Coghinas-Limbara copre altri 123.387 ha. | P1 p.42
- 16.588 | ha | Sito Natura 2000 Monte Limbara | Habitat forestali montani e formazioni granitiche; corridoio ecologico di rango regionale. | P1 pp.44, 65
- 2.014 | ha | Sugherete di Calangianus | La superficie più estesa dell'Unione; Tempio Pausania segue con 1.937 ha. | P1 pp.162, 168
- oltre 67 | % | Superfici ad alta fertilità nel Distretto di Calangianus | Spiega la qualità del sughero locale e la competitività della filiera. | P1 p.41

## Dove crescono le sugherete {type=chart}
**Grafico:** barre orizzontali ordinate — ettari di sugherete per comune; etichetta "non rilevate nelle tabelle" per Badesi e Santa Teresa Gallura; incidenza % solo dove riportata. Click su una barra → pannello scheda del comune.
**Dati:** data/alta-gallura/uso-suolo-comuni.json → `sugherete_per_comune[]`: `comune`, `slug`, `superficie_ha`, `incidenza_pct` (solo Aggius 6,9, Calangianus 15,9, Tempio 9,1), `origine`, `nota`. Non sommare i valori: il totale di Unione non è riportato nello studio (vedi superfici-unione.json).
**Lettura:** Calangianus (2.014 ha) e Tempio Pausania (1.937 ha) concentrano le sugherete; seguono Luras (645), Aggius (574) e Luogosanto (449). Sulla costa la funzione è ambientale e commerciale, non produttiva.
**Fonte:** P1, Allegato II, pp.156-171

## Un mosaico di macchia, boschi e pascoli {type=chart}
**Grafico:** barre impilate — prime sei classi di uso del suolo per comune (% del territorio comunale), più una fascia grigia "altre classi non dettagliate"; tooltip con ettari.
**Dati:** data/alta-gallura/uso-suolo-comuni.json → `dati[]` con `origine` = `tabella`: `comune`, `slug`, `classe_uso_suolo`, `rango`, `superficie_ha`, `incidenza_pct`. Le percentuali non sommano a 100: lo studio pubblica solo le prime sei classi per comune. Unificare le etichette "Seminativi in aree non irrigue" e "Seminativi non irrigui".
**Lettura:** Macchia mediterranea e gariga dominano la costa (Trinità: 26,6 % e 26,0 %). Nell'interno prevalgono i boschi di latifoglie (Bortigiadas 28,9 %, Calangianus 21,7 %) e i prati artificiali (Aggius 17,0 %). Badesi è l'unico comune a matrice agricola: seminativi 14,2 %, vigneti 11,6 %.
**Fonte:** P1, Allegato II, pp.156-171 (Carta dell'Uso del Suolo della Sardegna 2008, CORINE)

## Sei siti Natura 2000 e un'area marina protetta {type=text}
La Rete Natura 2000 copre montagna, foreste, zone umide e coste (P1 p.44). Il Monte Limbara (Tempio Pausania) e Monte Russu (Aglientu) sono Zone Speciali di Conservazione ([[ZSC]]). Capo Testa (Santa Teresa Gallura) è ZSC; "Da Capo Testa all'Isola Rossa" (Trinità) è Zona di Protezione Speciale ([[ZPS]]). Le Foci del Coghinas tutelano le dune di Badesi e la bassa valle di Viddalba. Lo studio cita anche i sistemi costieri di Isola Rossa – Costa Paradiso (P1 pp.44, 56-67). Santa Teresa ospita l'Area Marina Protetta Capo Testa – Punta Falcone (P1 p.64).

Lo studio non legge i siti come vincoli, ma come "laboratori territoriali" dove conservazione e filiere convergono (P1 p.44). Lo stesso vale per la disciplina del [[PPR]], la fascia costiera dei 300 metri e il [[PAI]]. Sono dispositivi di governance, non ostacoli (P1 pp.44-45).

## Il fuoco è la minaccia più immediata {type=kpi}
<!-- valore | unità | etichetta | contesto | fonte -->
- oltre 1.600 | kW/m | Intensità del fuoco simulata | Con macchia alta e continua: preclude l'attacco manuale diretto. | P1 p.40
- circa 99 | giorni/anno | Periodo arido cumulativo | Riserva idrica del suolo azzerata a settembre; siccità estiva estrema. | P1 p.40
- 269 | mm | Deficit idrico reale annuo | Stazione di Caddau (Limbara Sud, esterna all'Unione), riferimento per il massiccio; piovosità 954,1 mm. | P1 p.48
- 7 | comuni | Priorità alta per la prevenzione incendi | Calangianus, Tempio Pausania, Luogosanto, Aggius, Luras, Aglientu, Trinità d'Agultu. | P1 pp.183, 189

## Prevenire con la gestione attiva, non con l'emergenza {type=text}
Lo studio definisce il rischio incendio "la minaccia ambientale più immediata e sistemica" per il territorio (P1 p.45). Gli incendi bruciano biomassa, habitat, carbonio e reddito. La risposta è la gestione attiva del combustibile: sottobosco, fasce tagliafuoco, viabilità forestale, interfacce urbano-rurali (P1 pp.45-46). Il pascolo controllato bovino e suinicolo riduce il combustibile fine; il pascolo ghiandatico regolato nelle sugherete integra produzione e prevenzione (P1 p.46). Lo studio non riporta classi di rischio incendio per comune.

## Il territorio nelle parole dello studio {type=quote}
> Una sughereta economicamente valorizzata, monitorata e inserita in una filiera funzionante è intrinsecamente meno vulnerabile al rischio incendio, poiché beneficia di manutenzione costante e presenza antropica qualificata.
— P1, par. 2.2.9, p. 46

**CTA:** Vedi la strategia e la roadmap → /alta-gallura/strategia

## Ogni comune ha un ruolo {type=text id=comuni}
L'Unione dei Comuni è la piattaforma di coordinamento, secondo il modello della "Città dei Paesi" (P1 p.35). Calangianus e Tempio Pausania sono gli hub del sughero e dei servizi. Luogosanto, Luras e Aggius formano il mosaico agro-silvano; Bortigiadas presidia suolo e versanti. I comuni costieri sono la vetrina commerciale delle produzioni dell'interno (P1 p.79). Dalla costa di Santa Teresa Gallura ai versanti di Bortigiadas, scegli il tuo comune sulla mappa, oppure filtra tra costa e interno.

## Scegli il comune sulla mappa {type=chart}
**Grafico:** mappa SVG dei confini comunali (ComuniMap) colorata per fascia, costa in blu e interno in verde; hover con nome, fascia, abitanti 2025 e variazione 2001-2023; click → pannello scheda (`?comune=slug`, vedi `02b-alta-gallura-pannello-comune.md`). Filtro "Tutti · Costa · Interno" applicato a mappa e griglia di card. Lista testuale equivalente ("Elenco dei comuni") sotto la mappa; istruzione: "Seleziona un comune sulla mappa o nell'elenco."
**Dati:** data/alta-gallura/popolazione-storica.json → `dati[]`: `slug`, `comune`, `fascia`, `abitanti_2025`, `var_pct_2001_2023`; data/alta-gallura/schede-comuni.json → `funzione_territoriale`, `sugherete_ha`; data/alta-gallura/sintesi-comparativa-comuni.json → `vocazione_sughericola`. Confini: TopoJSON ISTAT dei comuni (da procurare, vedi BRIEF §5.6).
**Lettura:** I quattro comuni costieri crescono o restano stabili; i sette interni calano, con Tempio Pausania che resta il centro maggiore.
**Fonte:** P1, Tabella 1a, p.22; Tabella 2a, p.37; Allegato II, p.172

## Le undici schede {type=cards}
<!-- Griglia di card (stesso filtro costa | interno della mappa): nome · fascia · abitanti 2025 · var % 2001-2023 · vocazione sughericola (p.172) · sugherete (ha). Ordine alfabetico. Ogni card ha il bottone "Apri scheda" (aria-label "Apri la scheda di {comune}") e apre il pannello: il link è l'URL condivisibile `?comune=slug`. -->
- **Aggius** — Interno · 1.403 abitanti (2025) · −16,26 % dal 2001 · vocazione sughericola medio-alta · 574 ha di sugherete. → /alta-gallura?comune=aggius
- **Aglientu** — Costa · 1.195 abitanti · +7,69 % · vocazione medio-bassa · circa 321 ha. → /alta-gallura?comune=aglientu
- **Badesi** — Costa · 1.832 abitanti · −0,27 % · vocazione bassa · sugherete non rilevate. → /alta-gallura?comune=badesi
- **Bortigiadas** — Interno · 700 abitanti · −20,43 % · vocazione medio-bassa · circa 116 ha. → /alta-gallura?comune=bortigiadas
- **Calangianus** — Interno · 3.726 abitanti · −18,34 % · vocazione alta · 2.014 ha. → /alta-gallura?comune=calangianus
- **Luogosanto** — Interno · 1.815 abitanti · −1,26 % · vocazione media · circa 449 ha. → /alta-gallura?comune=luogosanto
- **Luras** — Interno · 2.368 abitanti · −10,55 % · vocazione medio-alta · circa 645 ha. → /alta-gallura?comune=luras
- **Santa Teresa Gallura** — Costa · 5.078 abitanti · +16,14 % · vocazione bassa · sugherete non rilevate. → /alta-gallura?comune=santa-teresa-gallura
- **Tempio Pausania** — Interno · 13.036 abitanti · −6,07 % · vocazione alta · 1.937 ha. → /alta-gallura?comune=tempio-pausania
- **Trinità d'Agultu e Vignola** — Costa · 2.511 abitanti · +15,87 % · vocazione medio-bassa · circa 211 ha. → /alta-gallura?comune=trinita-d-agultu-e-vignola
- **Viddalba** — Interno · 1.578 abitanti · −6,89 % · vocazione bassa · circa 52 ha. → /alta-gallura?comune=viddalba

## Quattro gruppi di comuni, quattro compiti {type=cards}
<!-- Da sintesi-comparativa-comuni.json → gruppi_funzionali[] ("Lettura conclusiva preliminare", P1 p.172). Un comune può stare in più gruppi. -->
- **Prioritari per la filiera bosco-sughero** — Calangianus e Tempio Pausania, poi Luras e Aggius: sugherete, decortica, proprietà, trasformazione. `icona: tree`
- **Agroforestali integrabili** — Luogosanto, Aggius, Luras e in parte Tempio: pilota tra bosco, pascolo e filiera suinicola controllata. `icona: sprout`
- **Funzione ambientale, paesaggistica e commerciale** — Aglientu, Santa Teresa Gallura, Trinità d'Agultu, Badesi: sbocco dei prodotti, turismo, paesaggio. `icona: store`
- **Attenzione forestale e protettiva** — Bortigiadas e parte di Calangianus, Aggius e Tempio: suoli fragili, gestione prudenziale. `icona: shield`

## Una lettura preliminare, non una classifica {type=text}
Lo studio avverte che la matrice comparativa "non deve essere interpretata come una graduatoria definitiva" (P1 p.172). Per la filiera suinicola "nessun Comune va dichiarato idoneo in modo definitivo in questa fase". Il quadro delle vocazioni ne elenca otto, dal sughero al turismo-commerciale; un comune può averne più d'una (P1 p.178). I giudizi orientano gli approfondimenti della roadmap.

Le schede mostrano solo le prime sei classi di uso del suolo e le principali unità pedologiche (P1 pp.156-171). La superficie comunale non è riportata: le percentuali si riferiscono all'intersezione [[GIS]] dei tre strati cartografici (P1 pp.151-152).

## Continua {type=cards}
<!-- Card di navigazione a fine pagina (sostituiscono le quattro card del vecchio hub) -->
- **Strategia · 3 filiere, 36 mesi** — Il framework [[ESG]], i servizi ecosistemici, le filiere bosco-sughero, bovina e suinicola, la roadmap in quattro fasi e le aree pilota. → /alta-gallura/strategia `icona: leaf`
- **Sughero Sardegna · la Sughereta** — Calangianus e Tempio Pausania nel quadro regionale: i comuni sughericoli dell'isola letti con tre indici, suolo, fuoco e continuità. → /sughero-sardegna `icona: map`

## Fonti {type=sources}
- Green community UCAG 193 – Strategie territoriali integrate (RISSTE, 2025), Prima parte – Demografia, pp. 21-31 (Tabelle 1a-1d, Figura 1a)
- Green community UCAG 193, Seconda parte – Ambiente e territorio, pp. 35, 37 (Tabella 2a); par. 2.2, pp. 39-46; par. 2.3.3, p. 48
- Green community UCAG 193, Terza parte – I Comuni dell'Unione, pp. 53-68 (Figura 3a, p. 55)
- Green community UCAG 193, Quarta parte – Prospettive Green communities, pp. 70-71, 79
- Green community UCAG 193, Allegato I – Report demografico dei Comuni, pp. 97-147
- Green community UCAG 193, Allegato II – SIT, cartografia e analisi biofisica, pp. 151-152, 156-171 (schede comunali), 172 (sintesi comparativa), 178 (quadro delle vocazioni), 183, 189
