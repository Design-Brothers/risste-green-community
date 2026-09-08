---
slug: /alta-gallura/comuni
sezione: alta-gallura
eyebrow: "Alta Gallura · Comuni"
title: "Undici comuni, undici vocazioni"
seo_title: "I comuni dell'Alta Gallura: mappa e schede"
description: "Mappa e schede degli undici comuni dell'Alta Gallura: abitanti 2025, variazione dal 2001, sugherete e vocazione di ciascun comune nella Green community."
og_image: source/parte1-green-community-alta-gallura/images/fig-3a-quadro-sinottico-comuni.jpeg
fonti:
  - documento: parte1
    pagine: [22, 25, 37, 53, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 178]
dati:
  - alta-gallura/schede-comuni.json
  - alta-gallura/popolazione-storica.json
  - alta-gallura/sintesi-comparativa-comuni.json
  - alta-gallura/uso-suolo-comuni.json
figure: []
---

<!-- Pagina indice (ARCHITETTURA §3.5). Unica interazione: filtro costa | interno, applicato alla mappa e alla griglia di card. Ogni card apre /alta-gallura/comuni/[slug]. -->

## Hero {type=hero}
**Standfirst:** Dalla costa di Santa Teresa Gallura ai versanti di Bortigiadas, ogni comune ha un ruolo nella Green community. Scegli il tuo comune sulla mappa, oppure filtra tra costa e interno.

## Due assi, un solo sistema {type=kpi}
<!-- valore | unità | etichetta | contesto | fonte -->
- 4 | comuni costieri | Aglientu, Badesi, Santa Teresa Gallura, Trinità d'Agultu e Vignola | 10.616 abitanti nel 2025, +14,0 % dal 2001. | P1 p.25
- 7 | comuni interni | Aggius, Bortigiadas, Calangianus, Luogosanto, Luras, Tempio Pausania, Viddalba | 24.626 abitanti nel 2025, −10,1 % dal 2001. | P1 p.25
- 2 | poli sughericoli primari | Calangianus e Tempio Pausania | 2.014 e 1.937 ettari di sugherete; hub della filiera e della governance. | P1 pp.162, 168, 178
- 8 | vocazioni prevalenti | Dal sughero al turismo-commerciale | Un comune può avere più vocazioni; nessuna è una graduatoria. | P1 p.178

## Scegli il comune sulla mappa {type=chart}
**Grafico:** mappa SVG dei confini comunali (ComuniMap) colorata per fascia, costa in blu e interno in verde; hover con nome, abitanti 2025 e variazione 2001-2023; click → scheda comune. Filtro costa | interno (unica interazione della pagina). Lista testuale equivalente sotto la mappa.
**Dati:** data/alta-gallura/popolazione-storica.json → `dati[]`: `slug`, `comune`, `fascia`, `abitanti_2025`, `var_pct_2001_2023`; data/alta-gallura/schede-comuni.json → `funzione_territoriale`, `sugherete_ha`; data/alta-gallura/sintesi-comparativa-comuni.json → `vocazione_sughericola`. Confini: TopoJSON ISTAT dei comuni (da procurare, vedi BRIEF §5.6).
**Lettura:** I quattro comuni costieri crescono o restano stabili; i sette interni calano, con Tempio Pausania che resta il centro maggiore.
**Fonte:** P1, Tabella 1a, p.22; Tabella 2a, p.37; Allegato II, p.172

## Le undici schede {type=cards}
<!-- Griglia di card: nome · fascia · abitanti 2025 · var % 2001-2023 · vocazione sughericola (p.172) · sugherete (ha). La funzione territoriale (Tab. 2a) compare nella scheda. Ordine alfabetico. -->
- **Aggius** — Interno · 1.403 abitanti (2025) · −16,26 % dal 2001 · vocazione sughericola medio-alta · 574 ha di sugherete. → /alta-gallura/comuni/aggius
- **Aglientu** — Costa · 1.195 abitanti · +7,69 % · vocazione medio-bassa · circa 321 ha. → /alta-gallura/comuni/aglientu
- **Badesi** — Costa · 1.832 abitanti · −0,27 % · vocazione bassa · sugherete non rilevate. → /alta-gallura/comuni/badesi
- **Bortigiadas** — Interno · 700 abitanti · −20,43 % · vocazione medio-bassa · circa 116 ha. → /alta-gallura/comuni/bortigiadas
- **Calangianus** — Interno · 3.726 abitanti · −18,34 % · vocazione alta · 2.014 ha. → /alta-gallura/comuni/calangianus
- **Luogosanto** — Interno · 1.815 abitanti · −1,26 % · vocazione media · circa 449 ha. → /alta-gallura/comuni/luogosanto
- **Luras** — Interno · 2.368 abitanti · −10,55 % · vocazione medio-alta · circa 645 ha. → /alta-gallura/comuni/luras
- **Santa Teresa Gallura** — Costa · 5.078 abitanti · +16,14 % · vocazione bassa · sugherete non rilevate. → /alta-gallura/comuni/santa-teresa-gallura
- **Tempio Pausania** — Interno · 13.036 abitanti · −6,07 % · vocazione alta · 1.937 ha. → /alta-gallura/comuni/tempio-pausania
- **Trinità d'Agultu e Vignola** — Costa · 2.511 abitanti · +15,87 % · vocazione medio-bassa · circa 211 ha. → /alta-gallura/comuni/trinita-d-agultu-e-vignola
- **Viddalba** — Interno · 1.578 abitanti · −6,89 % · vocazione bassa · circa 52 ha. → /alta-gallura/comuni/viddalba

## Quattro gruppi di comuni, quattro compiti {type=cards}
<!-- Dai gruppi funzionali della "Lettura conclusiva preliminare", P1 p.172. Un comune può stare in più gruppi. -->
- **Prioritari per la filiera bosco-sughero** — Calangianus e Tempio Pausania, poi Luras e Aggius: sugherete, decortica, proprietà, trasformazione. `icona: tree`
- **Agroforestali integrabili** — Luogosanto, Aggius, Luras e in parte Tempio: pilota tra bosco, pascolo e filiera suinicola controllata. `icona: sprout`
- **Funzione ambientale, paesaggistica e commerciale** — Aglientu, Santa Teresa Gallura, Trinità d'Agultu, Badesi: sbocco dei prodotti, turismo, paesaggio. `icona: store`
- **Attenzione forestale e protettiva** — Bortigiadas e parte di Calangianus, Aggius e Tempio: suoli fragili, gestione prudenziale. `icona: shield`

## Una lettura preliminare, non una classifica {type=text}
Lo studio avverte che la matrice comparativa "non deve essere interpretata come una graduatoria definitiva" (P1 p.172). Per la filiera suinicola "nessun Comune va dichiarato idoneo in modo definitivo in questa fase". I giudizi orientano gli approfondimenti della roadmap.

Le schede mostrano solo le prime sei classi di uso del suolo e le principali unità pedologiche (P1 pp.156-171). La superficie comunale non è riportata: le percentuali si riferiscono all'intersezione [[GIS]] dei tre strati cartografici (P1 pp.151-152).

## Fonti {type=sources}
- Green community UCAG 193 – Strategie territoriali integrate (RISSTE, 2025), Prima parte – Demografia, Tabella 1a, p. 22; Tabella 1c, p. 25
- Green community UCAG 193, Seconda parte – Ambiente e territorio, Tabella 2a, p. 37
- Green community UCAG 193, Terza parte – I Comuni dell'Unione, pp. 53-68
- Green community UCAG 193, Allegato II – SIT, cartografia e analisi biofisica, schede comunali pp. 156-171; sintesi comparativa p. 172; quadro delle vocazioni p. 178
