---
slug: /alta-gallura?comune=[slug]          # non è una pagina: pannello laterale sopra la sezione #comuni di /alta-gallura
tipo: pannello
componente: ComuneDrawer
sezione: alta-gallura
eyebrow: "Alta Gallura · Scheda comune"
title: "{{comune}}"
document_title: "{{comune}} – scheda comune · Alta Gallura"   # aggiorna document.title a pannello aperto (seo.md, riga P); canonical resta /alta-gallura
share_text: "{{comune}}, Alta Gallura: {{abitanti_2025}} abitanti nel 2025 ({{var_pct_2001_2023}} % dal 2001), {{sugherete_testo_breve}}. La scheda del comune nello studio RISSTE."
og_image: source/parte1-green-community-alta-gallura/images/fig-3a-quadro-sinottico-comuni.jpeg   # ereditata dalla pagina, nessun OG per comune
fonti:
  - documento: parte1
    pagine: "[22, 37, {{pagine_quadro_sinottico}}, {{pagine_allegato_1}}, {{pagine_scheda_preliminare}}, 172]"
dati:
  - alta-gallura/schede-comuni.json
  - alta-gallura/popolazione-storica.json
  - alta-gallura/saldi-demografici.json
  - alta-gallura/struttura-eta.json
  - alta-gallura/famiglie.json
  - alta-gallura/stranieri-e-scuola.json
  - alta-gallura/imprese.json
  - alta-gallura/scenari-2035.json
  - alta-gallura/uso-suolo-comuni.json
  - alta-gallura/pedologia-comuni.json
  - alta-gallura/matrice-pedologia-uso-suolo.json
  - alta-gallura/sintesi-comparativa-comuni.json
figure: []
---

<!--
SPECIFICA DEL PANNELLO SCHEDA COMUNE (11 schede, componente `ComuneDrawer`). Non è una pagina: si apre sopra la sezione "Gli 11 comuni" di /alta-gallura (ARCHITETTURA `/alta-gallura` punto 7; SITEMAP).
Chiave di join tra i JSON: `slug` (11 valori di schede-comuni.json → dati[].slug). Il testo fisso è scritto qui; i segnaposto {{campo}} si riempiono dai dataset in data/alta-gallura/ (legenda in coda).
Regola: i testi di `schede-comuni.json` (inquadramento, implicazioni, criticità, opportunità) sono riportati integralmente come nella fonte; il testo redazionale segue la regola ≤ 22 parole. Nessun dato nuovo: un campo `null` mostra "Dato non riportato nello studio."
-->

## Apertura e URL {type=spec}
- **Da dove si apre:** click su un comune nella mappa SVG (`ComuniMap`); bottone "Apri scheda" di una card della griglia "Le undici schede"; voce dell'"Elenco dei comuni" (alternativa testuale della mappa); click su una barra del grafico "Dove crescono le sugherete"; apertura diretta di un link condiviso. `aria-label` dei trigger: "Apri la scheda di {{comune}}".
- **URL:** `/alta-gallura?comune={{slug}}` (es. `/alta-gallura?comune=tempio-pausania`). Gli slug sono gli 11 valori di `schede-comuni.json → dati[].slug`, kebab-case senza accenti (`trinita-d-agultu-e-vignola`, `santa-teresa-gallura`). I vecchi URL `/alta-gallura/comuni/[slug]` fanno redirect 301 qui (microcopy §6).
- **Cronologia:** l'apertura fa `pushState`; "Chiudi" e il tasto Indietro tolgono il parametro e riportano il focus al trigger di origine. Cambiare comune dal pannello (precedente/successivo) fa `replaceState`.
- **Caricamento con `?comune=` già presente:** la pagina si apre scrollata a `#comuni`, con il pannello aperto e il comune evidenziato su mappa e griglia. Nessuno stato di caricamento: i dati sono nel bundle.
- **Layout:** desktop pannello laterale destro, larghezza 480-560 px, sfondo `--ice`, il resto della pagina resta visibile; mobile foglio a tutta altezza dal basso. Focus intrappolato nel pannello, chiusura con Esc e click sul velo, `role="dialog"`, `aria-modal="true"`, `aria-labelledby` = titolo. Motivo grafico: anelli di decortica verde-ciano in filigrana dietro l'intestazione (BRIEF §3).
- **Ancore interne al pannello:** nessuna; un solo scroll verticale. I blocchi 7-9 stanno in un accordion "Altri dati", chiuso di default.

## Azioni {type=spec}
<!-- barra fissa in testa al pannello; etichette da microcopy.md §5-6 -->
- **Chiudi** — chiude il pannello, toglie `?comune=` dall'URL, riporta il focus al trigger. `aria-label` "Chiudi la scheda"; anche Esc e click fuori.
- **Copia link** — copia `https://{{host}}/alta-gallura?comune={{slug}}`; conferma "Link copiato" (2 secondi); errore "Non è stato possibile copiare il link".
- **Comune precedente** · **Comune successivo** — aprono `?comune={{slug_precedente}}` / `?comune={{slug_successivo}}` nell'ordine alfabetico della griglia, rispettando il filtro costa/interno attivo; disattivati agli estremi. Tooltip "{{nome_precedente}}" / "{{nome_successivo}}".
- **Vedi anche nella sezione Sughero Sardegna** → `/sughero-sardegna?comune={{slug}}` — **solo** per `calangianus` e `tempio-pausania`, gli unici due comuni presenti in entrambi gli studi (stessi slug nei due dataset). Per gli altri nove comuni il bottone non viene renderizzato.
- **Scheda completa nel PDF (pp. {{pagine_allegato_1}})** → `/pdf/RISSTE_CUP_E77G24000450002_Parte1_signed.pdf#page={{prima_pagina_allegato_1}}` e **Scarica gli studi integrali (PDF)** → `/progetto#documenti` — in coda al pannello, nel blocco "Approfondisci nello studio".
- **Torna a tutti i comuni** — in fondo al pannello, equivale a Chiudi.

## Stati {type=spec}
- **Vuoto (nessun `?comune=`):** pannello chiuso; nessun comune evidenziato. Sopra la mappa resta l'istruzione "Seleziona un comune sulla mappa o nell'elenco."
- **Non trovato (`?comune=` con slug sconosciuto, es. `?comune=olbia`):** pannello aperto con eyebrow "Alta Gallura · Scheda comune", titolo "Comune non trovato", testo "Comune non trovato. Scegli un comune dall'elenco." e l'elenco degli undici comuni come link `?comune=slug`. Azione unica "Chiudi"; il parametro non valido viene rimosso alla chiusura. `document.title` non cambia. La pagina non risponde 404.
- **Slug con maiuscole o accenti:** normalizzare in minuscolo e kebab-case prima del confronto (`Calangianus` → `calangianus`); se lo slug normalizzato esiste, aprire la scheda e riscrivere l'URL con `replaceState`.
- **Parametro vuoto (`?comune=`):** trattato come "vuoto": il parametro si rimuove.
- **Dato mancante in un campo:** la riga mostra "Dato non riportato nello studio."; il blocco non scompare. Casi noti: saldi di Viddalba (`null`), `imprese_2021` di Viddalba (`null`, omettere la variazione), quota over 65 del 2002 per Bortigiadas e Trinità (omettere la frase), `principali_paesi` vuoto per Aggius (usare `provenienza_continenti[].paesi`), sugherete 0 per Badesi e Santa Teresa Gallura ("sugherete non rilevate nelle tabelle").
- **Caricamento differito del modulo:** "Caricamento della scheda…"; in caso di errore "Non è stato possibile caricare i dati. Ricarica la pagina."
- **Stampa:** il pannello aperto si stampa da solo (pagina ospite nascosta in `@media print`), con URL e data in piè di pagina.

## Ordine dei blocchi {type=spec}
1. Intestazione (eyebrow, titolo, sottotitolo con fascia e abitanti 2025, badge della funzione territoriale, azioni)
2. KPI "{{comune}} in quattro numeri" (4)
3. Grafico "Come è cambiata la popolazione" (mini-linea 2001-2025 + barre dei saldi)
4. Grafico "Il suolo e le sue coperture" (prime sei classi di uso del suolo, riga Sugherete evidenziata)
5. Testo "Cosa dice lo studio" (inquadramento e implicazioni per le due filiere, integrali)
6. Card "Criticità e opportunità" (2) con valutazione preliminare
7. Card "La sintesi comparativa" (4 giudizi con badge) e nota "non una graduatoria"
8. Accordion "Altri dati": KPI "Chi vive a {{comune}}" (4) · Testo "Vent'anni di invecchiamento" · Testo "Un suolo da leggere prima di usarlo" · Card "Elementi identitari"
9. Testo "Approfondisci nello studio" (con i link al PDF)
10. Fonti

## Intestazione {type=hero}
**Eyebrow:** Alta Gallura · Scheda comune
**Titolo:** {{comune}}
**Sottotitolo:** {{fascia_label_badge}} · {{abitanti_2025}} abitanti (2025) · {{var_pct_2001_2023}} % dal 2001
**Badge:** {{funzione_territoriale}} (colore della fascia: costa blu, interno verde; tooltip "Costa" / "Interno", microcopy §9)
**Visual:** `DecorticaRings` statico, 48 px, a sinistra del titolo, `aria-hidden`, `spin=false`. Colorato per fascia: interno tone `green` (`--green` → `--acid`), costa variante `blue` (`--blue` → `--cyan`, da aggiungere al componente). Il colore ha sempre accanto il testo della fascia nel sottotitolo.
**Standfirst:** Comune {{fascia_label}} dell'Alta Gallura, nel {{posizione_parte3}}. Ruolo strategico: {{ruolo_strategico}}.
**Azioni:** Chiudi · Copia link · Comune precedente · Comune successivo · [[if slug in (calangianus, tempio-pausania)]]Vedi anche nella sezione Sughero Sardegna → /sughero-sardegna?comune={{slug}}[[endif]]

## {{comune}} in quattro numeri {type=kpi}
<!-- valore | unità | etichetta | contesto | fonte -->
- {{abitanti_2025}} | abitanti | Residenti al 1° gennaio 2025 | Erano {{abitanti_2001}} nel 2001 e {{abitanti_2023}} a fine 2023. | P1 p.22
- {{var_pct_2001_2023}} | % | Variazione della popolazione 2001-2023 | {{var_ass_2001_2023}} residenti in ventidue anni; fascia {{fascia_label}}. | P1 p.22; All. I p.{{pagine_allegato_1}}
- {{quota_65_piu_pct}} | % | Residenti con 65 anni e oltre (2025) | Indice di vecchiaia {{indice_vecchiaia_2025}}; età media {{eta_media_2025}} anni. | All. I p.{{pagina_struttura_eta}}
- {{imprese_2025}} | imprese | Imprese attive nel 2025 | {{var_pct_imprese}} % rispetto alle {{imprese_2021}} del 2021. | P1 pp.27-28

## Come è cambiata la popolazione {type=chart}
**Grafico:** mini-grafico a linea — abitanti 2001, 2011, 2023, 2025 nel colore della fascia; sotto, due barre contrapposte con saldo naturale e saldo migratorio 2002-2023.
**Dati:** data/alta-gallura/popolazione-storica.json → riga con `slug` = {{slug}}: `abitanti_2001`, `abitanti_2011`, `abitanti_2023`, `abitanti_2025`. data/alta-gallura/saldi-demografici.json → `dati[]` con `livello` = `comune`: `saldo_naturale_2002_2023`, `saldo_migratorio_2002_2023`, `incidenza_prevalente` (per Viddalba i saldi sono `null`: mostrare "Dato non riportato nello studio."). Tabella "Vedi i dati": Anno · Abitanti; Saldo · Valore.
**Lettura:** Saldo naturale {{saldo_naturale}}, saldo migratorio {{saldo_migratorio}} tra 2002 e 2023. Lo studio sintetizza la dinamica così: "{{incidenza_prevalente}}".
**Fonte:** P1, Tabella 1a, p.22; Allegato I, scheda di {{comune}}, pp.{{pagine_allegato_1}}

## Il suolo e le sue coperture {type=chart}
**Grafico:** barre orizzontali — le prime sei classi di uso del suolo in % del territorio comunale; la riga "Sugherete" è evidenziata, anche quando proviene dal testo (senza %).
**Dati:** data/alta-gallura/uso-suolo-comuni.json → `dati[]` con `slug` = {{slug}} e `origine` = `tabella`: `classe_uso_suolo`, `rango`, `superficie_ha`, `incidenza_pct`; `sugherete_per_comune[]` → `superficie_ha`, `incidenza_pct`, `origine`, `nota`. Le percentuali non sommano a 100: lo studio pubblica solo le prime sei classi. Tabella "Vedi i dati": Classe · ha · %.
**Lettura:** La copertura più estesa è {{classe_1}} ({{classe_1_ha}} ha, {{classe_1_pct}} %), seguita da {{classe_2}} ({{classe_2_pct}} %). Le sugherete coprono {{sugherete_testo_breve}}.
**Fonte:** P1, Allegato II, scheda di {{comune}}, p.{{pagina_uso_suolo}}

## Cosa dice lo studio {type=text}
<!-- Testi integrali dalla scheda dell'Allegato II e dalla Terza parte -->
**Inquadramento.** {{inquadramento_0}} {{inquadramento_1}}

**Filiera bosco-sughero.** {{implicazioni_bosco_sughero}}

**Filiera suinicola.** {{implicazioni_suinicola}}

## Criticità e opportunità {type=cards}
<!-- Due card affiancate con elenco puntato; sotto, la valutazione preliminare in una riga -->
- **Criticità** — {{criticita_elenco}} `icona: alert-triangle`
- **Opportunità** — {{opportunita_elenco}} `icona: sparkles`

**Valutazione preliminare.** {{valutazione_preliminare}}.

## La sintesi comparativa {type=cards}
<!-- Quattro giudizi qualitativi; badge con la scala ordinale del brief (§4) e sempre l'etichetta testuale -->
- **Vocazione sughericola** — {{vocazione_sughericola}} `icona: tree`
- **Interesse suinicolo agroforestale** — {{interesse_suinicolo}} `icona: pig`
- **Fragilità pedologica** — {{fragilita_pedologica}} `icona: mountain`
- **Priorità di approfondimento** — {{priorita_approfondimento}} `icona: search`

Lo studio precisa che la sintesi comparativa "non deve essere interpretata come una graduatoria definitiva" (P1 p.172). Per la filiera suinicola "nessun Comune va dichiarato idoneo in modo definitivo in questa fase". Le verifiche pedologiche e agronomiche sul campo sono la prima azione della roadmap (P1 p.90).

## Chi vive a {{comune}} {type=kpi}
<!-- Accordion "Altri dati" -->
- {{componenti_medi_2023}} | persone per famiglia | Componenti medi nel 2023 | {{numero_famiglie_2023}} famiglie; nel 2003 erano {{numero_famiglie_2003}} con {{componenti_medi_2003}} componenti. | All. I p.{{pagina_famiglie}}
- {{stranieri_2025}} | persone | Residenti stranieri (2025) | Il {{stranieri_pct}} % dei residenti; provenienze principali: {{principali_paesi}}. | All. I p.{{pagina_stranieri}}
- {{utenza_0_18}} | ragazzi | Residenti da 0 a 18 anni (2025) | Di cui {{alunni_primaria}} in età da scuola primaria e {{alunni_sec_ii}} da secondaria di II grado. | All. I p.{{pagina_stranieri}}
- circa {{pop_2035_lineare}} | abitanti | Stima 2035, scenario lineare | Tra circa {{pop_2035_crisi}} (scenario di crisi) e circa {{pop_2035_attrattivo}} (scenario attrattivo). | All. I p.{{pagina_scenari}}

## Vent'anni di invecchiamento {type=text}
<!-- Accordion "Altri dati" -->
Nel 2002 gli over 65 erano il {{quota_65_piu_pct_2002}} % dei residenti, con un indice di vecchiaia di {{indice_vecchiaia_2002}} (All. I p.{{pagina_struttura_eta}}). Nel 2025 sono il {{quota_65_piu_pct}} %: {{classe_65_piu_2025}} persone contro {{classe_0_14_2025}} ragazzi sotto i 15 anni. L'indice di dipendenza è {{indice_dipendenza_2025}}. Le stime al 2035 sono indicate come "circa" e non vanno sommate tra comuni (All. I p.{{pagina_scenari}}).

## Un suolo da leggere prima di usarlo {type=text}
<!-- Accordion "Altri dati" -->
Il territorio poggia per il {{ped_1_pct}} % sull'unità {{ped_1_codice}} e per il {{ped_2_pct}} % sull'unità {{ped_2_codice}} della Carta dei Suoli (P1 p.{{pagina_pedologia}}). {{ped_1_codice}}: {{ped_1_descrizione}} La combinazione più estesa tra copertura e suolo è "{{combinazione_1}}" ({{combinazione_1_pct}} % del territorio). Lo studio commenta: "{{commento_pedologico}}"

## Elementi identitari {type=cards}
<!-- Accordion "Altri dati". Una card per ciascun elemento di schede-comuni.json → elementi_identitari[]; selezione redazionale, non elenco del documento -->
- **{{elementi_identitari[0]}}**
- **{{elementi_identitari[1]}}**
- **{{elementi_identitari[n]}}**

## Approfondisci nello studio {type=text}
La scheda demografica completa è nell'Allegato I (pp. {{pagine_allegato_1}}). La scheda territoriale preliminare è nell'Allegato II (pp. {{pagine_scheda_preliminare}}). Il profilo del comune è nella Terza parte (pp. {{pagine_quadro_sinottico}}).
**CTA:** Scheda completa nel PDF (pp. {{pagine_allegato_1}}) → /pdf/RISSTE_CUP_E77G24000450002_Parte1_signed.pdf#page={{prima_pagina_allegato_1}}
**CTA:** Scarica gli studi integrali (PDF) → /progetto#documenti
**CTA:** Torna a tutti i comuni → (Chiudi)

## Fonti {type=sources}
- Green community UCAG 193 – Strategie territoriali integrate (RISSTE, 2025), Prima parte – Demografia, Tabella 1a, p. 22; par. 1.8, pp. 27-28
- Green community UCAG 193, Seconda parte – Ambiente e territorio, Tabella 2a, p. 37
- Green community UCAG 193, Terza parte – I Comuni dell'Unione, pp. {{pagine_quadro_sinottico}}
- Green community UCAG 193, Allegato I – Report demografico dei Comuni, pp. {{pagine_allegato_1}}
- Green community UCAG 193, Allegato II – SIT, cartografia e analisi biofisica, pp. {{pagine_scheda_preliminare}}, 172

<!--
LEGENDA DEI SEGNAPOSTO {{campo}} (file → campo; tutti i file in data/alta-gallura/). Formato numeri: italiano (punto migliaia, virgola decimali), segno sempre esplicito nelle variazioni, unità esplicite.

| Segnaposto | File → campo | Note |
|---|---|---|
| {{slug}}, {{comune}} | schede-comuni.json → dati[].slug, .comune | |
| {{fascia}} / {{fascia_label}} / {{fascia_label_badge}} | schede-comuni.json → dati[].fascia | costiera → "costiero" / "Costa"; interna → "dell'entroterra" / "Interno" |
| {{posizione_parte3}} | schede-comuni.json → dati[].posizione_parte3 | |
| {{funzione_territoriale}} | schede-comuni.json → dati[].funzione_territoriale (= tab_2a.funzione_territoriale) | |
| {{ambito_territoriale}}, {{elementi_paesaggistici}}, {{ruolo_strategico}} | schede-comuni.json → dati[].tab_2a.ambito_territoriale, .elementi_paesaggistici_dominanti, .ruolo_strategico | Tab. 2a, p.37 |
| {{inquadramento_0}}, {{inquadramento_1}} | schede-comuni.json → dati[].inquadramento[0], [1] | testo integrale |
| {{implicazioni_bosco_sughero}}, {{implicazioni_suinicola}} | schede-comuni.json → dati[].implicazioni_bosco_sughero, .implicazioni_suinicola | testo integrale |
| {{criticita_elenco}}, {{opportunita_elenco}} | schede-comuni.json → dati[].criticita[], .opportunita[] | elenco puntato; prima lettera maiuscola |
| {{valutazione_preliminare}} | schede-comuni.json → dati[].valutazione_preliminare | |
| {{vocazione_sughericola}}, {{interesse_suinicolo}}, {{fragilita_pedologica}}, {{priorita_approfondimento}} | sintesi-comparativa-comuni.json → dati[].vocazione_sughericola, .interesse_suinicolo_agroforestale, .fragilita_pedologica, .priorita_approfondimento (= schede-comuni.json → dati[].sintesi_comparativa) | p.172 |
| {{elementi_identitari[]}} | schede-comuni.json → dati[].elementi_identitari[] | una card per elemento |
| {{sugherete_ha}} | schede-comuni.json → dati[].sugherete_ha (= uso-suolo-comuni.json → sugherete_per_comune[].superficie_ha) | 0 = "non rilevate nelle tabelle" |
| {{sugherete_pct}}, {{sugherete_origine}}, {{sugherete_nota}} | uso-suolo-comuni.json → sugherete_per_comune[].incidenza_pct, .origine, .nota | pct solo per Aggius, Calangianus, Tempio |
| {{sugherete_testo_breve}} | derivato: "N ha di sugherete" / "circa N ha di sugherete" (origine testo) / "sugherete non rilevate nelle tabelle" (0) | |
| {{abitanti_2001}}, {{abitanti_2011}}, {{abitanti_2023}}, {{abitanti_2025}} | popolazione-storica.json → dati[] | |
| {{var_ass_2001_2023}}, {{var_pct_2001_2023}} | popolazione-storica.json → dati[].var_ass_2001_2023, .var_pct_2001_2023 | segno da mostrare |
| {{saldo_naturale}}, {{saldo_migratorio}}, {{incidenza_prevalente}} | saldi-demografici.json → dati[] con livello = comune: .saldo_naturale_2002_2023, .saldo_migratorio_2002_2023, .incidenza_prevalente | Viddalba: null → "Dato non riportato nello studio." |
| {{classe_0_14_2025}}, {{classe_15_64_2025}}, {{classe_65_piu_2025}}, {{quota_0_14_pct}}, {{quota_65_piu_pct}}, {{indice_vecchiaia_2025}}, {{indice_dipendenza_2025}}, {{eta_media_2025}} | struttura-eta.json → dati[] con anno = 2025 | |
| {{quota_65_piu_pct_2002}}, {{indice_vecchiaia_2002}}, {{eta_media_2002}} | struttura-eta.json → dati[] con anno = 2002 | Bortigiadas e Trinità: quota 2002 null → omettere la frase |
| {{numero_famiglie_2003}}, {{numero_famiglie_2023}}, {{componenti_medi_2003}}, {{componenti_medi_2023}} | famiglie.json → dati[].serie[] con anno = 2003 / 2023 | |
| {{stranieri_2025}}, {{stranieri_pct}}, {{principali_paesi}} | stranieri-e-scuola.json → dati[].stranieri_2025, .stranieri_pct, .principali_paesi[].paese (primi 3) | Aggius: principali_paesi vuoto → usare provenienza_continenti[].paesi |
| {{utenza_0_18}}, {{alunni_nido}}, {{alunni_infanzia}}, {{alunni_primaria}}, {{alunni_sec_i}}, {{alunni_sec_ii}} | stranieri-e-scuola.json → dati[].utenza_scolastica_0_18, .cicli_scolastici[].alunni | Calangianus: 466 (valore testuale, vedi note_scuola) |
| {{imprese_2021}}, {{imprese_2025}}, {{var_pct_imprese}} | imprese.json → dati[] livello = comune: .imprese_2021, .imprese_2025, .var_pct_2021_2025 | Viddalba: imprese_2021 null → omettere |
| {{settori_citati}} | imprese.json → dati[] campi *_2025 non null, con *_2025_pct se presente | "null = non citato", non zero |
| {{pop_2035_attrattivo}}, {{pop_2035_lineare}}, {{pop_2035_crisi}}, {{nome_scenario_*}} | scenari-2035.json → dati_comuni[].scenari[] | valori "circa"; non sommare tra comuni |
| {{uso_suolo_top6[]}} → {{classe_n}}, {{classe_n_ha}}, {{classe_n_pct}} | uso-suolo-comuni.json → dati[] con origine = tabella, ordinati per rango: .classe_uso_suolo, .superficie_ha, .incidenza_pct | |
| {{ped_n_codice}}, {{ped_n_ha}}, {{ped_n_pct}} | pedologia-comuni.json → dati[] ordinati per rango: .unita_pedologica, .superficie_ha, .incidenza_pct | |
| {{ped_n_descrizione}} | pedologia-comuni.json → unita_pedologiche[codice].descrizione | B3, G1, I1: "unità non descritta nello studio" |
| {{commento_pedologico}} | pedologia-comuni.json → commenti_per_comune[].testo | testo integrale |
| {{combinazione_1}}, {{combinazione_1_pct}} | matrice-pedologia-uso-suolo.json → dati[].combinazioni[0] | |
| {{pagine_allegato_1}}, {{prima_pagina_allegato_1}} | popolazione-storica.json → dati[].pagine_pdf[1] fino a +4 (scheda Allegato I); la prima pagina per il link `#page=` | es. Calangianus 113-117 → 113 |
| {{pagine_scheda_preliminare}}, {{pagine_quadro_sinottico}}, {{pagina_tab_2a}}, {{pagina_sintesi}} | schede-comuni.json → dati[].pagine_fonte.scheda_preliminare, .quadro_sinottico_parte3, .tabella_2a, .sintesi_comparativa | |
| {{pagina_uso_suolo}}, {{pagina_pedologia}} | uso-suolo-comuni.json → dati[].pagina_pdf; pedologia-comuni.json → dati[].pagina_pdf | |
| {{pagina_struttura_eta}}, {{pagina_famiglie}}, {{pagina_stranieri}}, {{pagina_scenari}} | struttura-eta.json, famiglie.json, stranieri-e-scuola.json → dati[].pagine_pdf; scenari-2035.json → dati_comuni[].pagine_pdf | |
| {{slug_precedente}}, {{nome_precedente}}, {{slug_successivo}}, {{nome_successivo}} | derivati: comune adiacente nell'ordine alfabetico della griglia (rispettando il filtro costa/interno attivo) | |
| {{host}} | dominio del sito (da configurazione) | |

Blocchi condizionali: [[if …]] … [[endif]] si rendono solo se la condizione è vera (usato per il rimando alla Sughereta Sardegna).
Testo fisso di raccordo: tutto ciò che non è tra doppie graffe.
-->


<!-- ============================================================================
ESEMPIO COMPILATO: CALANGIANUS (valori reali dai dataset, 1° gennaio 2025 dove non indicato)
URL: /alta-gallura?comune=calangianus · document.title: "Calangianus – scheda comune · Alta Gallura"
============================================================================ -->

## Intestazione {type=hero}
**Eyebrow:** Alta Gallura · Scheda comune
**Titolo:** Calangianus
**Sottotitolo:** Interno · 3.726 abitanti (2025) · −18,34 % dal 2001
**Badge:** Polo forestale e sughericolo (verde, interno)
**Visual:** `DecorticaRings` statico, 48 px, tone `green` (interno), a sinistra del titolo.
**Standfirst:** Comune dell'entroterra dell'Alta Gallura, nel settore collinare e montano dell'interno. Ruolo strategico: produzione sughericola, gestione forestale, tutela idrogeologica.
**Azioni:** Chiudi · Copia link (`/alta-gallura?comune=calangianus`) · Comune precedente (Bortigiadas) · Comune successivo (Luogosanto) · Vedi anche nella sezione Sughero Sardegna → /sughero-sardegna?comune=calangianus

## Calangianus in quattro numeri {type=kpi}
- 3.726 | abitanti | Residenti al 1° gennaio 2025 | Erano 4.635 nel 2001 e 3.785 a fine 2023. | P1 p.22
- −18,34 | % | Variazione della popolazione 2001-2023 | −850 residenti in ventidue anni; fascia dell'entroterra. | P1 p.22; All. I p.113
- 29,6 | % | Residenti con 65 anni e oltre (2025) | Indice di vecchiaia 322,2; età media 50,1 anni. | All. I pp.114, 116
- 511 | imprese | Imprese attive nel 2025 | −1,16 % rispetto alle 517 del 2021. | P1 pp.27-28

## Come è cambiata la popolazione {type=chart}
**Grafico:** mini-grafico a linea — abitanti 2001, 2011, 2023, 2025 (verde, interno); sotto, due barre contrapposte con saldo naturale e saldo migratorio 2002-2023.
**Dati:** data/alta-gallura/popolazione-storica.json → `slug` = `calangianus`: 4.635 / 4.257 / 3.785 / 3.726. data/alta-gallura/saldi-demografici.json → `saldo_naturale_2002_2023` = −423, `saldo_migratorio_2002_2023` = −365.
**Lettura:** Saldo naturale −423, saldo migratorio −365 tra 2002 e 2023. Lo studio sintetizza la dinamica così: "Forte decrescita indotta dall'azione congiunta di deficit naturale e migratorio".
**Fonte:** P1, Tabella 1a, p.22; Allegato I, scheda di Calangianus, pp.113-114

## Il suolo e le sue coperture {type=chart}
**Grafico:** barre orizzontali — le prime sei classi di uso del suolo in % del territorio comunale; la riga "Sugherete" è evidenziata.
**Dati:** data/alta-gallura/uso-suolo-comuni.json → `slug` = `calangianus`, `origine` = `tabella`: Bosco di latifoglie 2.745 ha (21,7 %); Macchia mediterranea 2.070 ha (16,4 %); Sugherete 2.014 ha (15,9 %); Gariga 1.412 ha (11,2 %); Vegetazione rada 1.290 ha (10,2 %); Seminativi in aree non irrigue 663 ha (5,2 %). `sugherete_per_comune[]` → 2.014 ha, 15,9 %, origine tabella.
**Lettura:** La copertura più estesa è il bosco di latifoglie (2.745 ha, 21,7 %), seguita dalla macchia mediterranea (16,4 %). Le sugherete coprono 2.014 ha, il 15,9 % del territorio: la superficie più estesa dell'Unione.
**Fonte:** P1, Allegato II, scheda di Calangianus, p.162

## Cosa dice lo studio {type=text}
**Inquadramento.** Calangianus emerge come uno dei Comuni chiave per la filiera bosco-sughero. Presenta la maggiore superficie di sugherete tra i Comuni analizzati, oltre a boschi di latifoglie, macchia e gariga. Tuttavia, la forte presenza di C1 impone una lettura molto prudente della componente produttiva e zootecnica. Calangianus rappresenta il principale polo industriale della filiera sughericola dell'Alta Gallura e si colloca come uno dei più rilevanti distretti europei specializzati nella lavorazione di questa risorsa; tra il 2001 e il 2023 ha perso oltre il 18 % dei propri abitanti. Ospita la più estesa superficie di sugherete dell'Alta Gallura.

**Filiera bosco-sughero.** Calangianus è un Comune prioritario per la filiera sughericola. Le circa 2.014 ha di sugherete indicano una rilevanza territoriale elevata. Le successive fasi dovranno verificare stato vegetativo, turni di decortica, qualità del sughero, proprietà, accessibilità, operatori e connessioni con trasformazione e distretto produttivo esistente.

**Filiera suinicola.** Il suino agroforestale deve essere trattato come tema secondario e molto controllato. La presenza di vaste aree forestali e sugherete non implica automaticamente idoneità al pascolo suino. Al contrario, la diffusione di C1 e vegetazione rada rende prioritaria la tutela del suolo e della rinnovazione.

## Criticità e opportunità {type=cards}
- **Criticità** — Sugherete su suoli fragili; rischio erosione; vegetazione rada su C1; necessità di protezione della rinnovazione; possibile conflitto tra funzione produttiva e funzione protettiva. `icona: alert-triangle`
- **Opportunità** — Piano di gestione delle sugherete; mappatura di dettaglio; distretto rurale del sughero; formazione operatori; certificazioni; filiera corta; integrazione con artigianato, bioedilizia, design e turismo esperienziale. `icona: sparkles`

**Valutazione preliminare.** Vocazione sughericola alta; priorità forestale alta; interesse suinicolo basso-medio solo come sperimentazione controllata; fragilità alta.

## La sintesi comparativa {type=cards}
- **Vocazione sughericola** — Alta `icona: tree`
- **Interesse suinicolo agroforestale** — Basso-medio controllato `icona: pig`
- **Fragilità pedologica** — Alta `icona: mountain`
- **Priorità di approfondimento** — Molto alta `icona: search`

Lo studio precisa che la sintesi comparativa "non deve essere interpretata come una graduatoria definitiva" (P1 p.172). Per la filiera suinicola "nessun Comune va dichiarato idoneo in modo definitivo in questa fase". Le verifiche pedologiche e agronomiche sul campo sono la prima azione della roadmap (P1 p.90).

## Chi vive a Calangianus {type=kpi}
<!-- Accordion "Altri dati" -->
- 2,33 | persone per famiglia | Componenti medi nel 2023 | 1.618 famiglie; nel 2003 erano 1.595 con 2,87 componenti. | All. I pp.114-115
- 155 | persone | Residenti stranieri (2025) | Il 4,2 % dei residenti; provenienze principali: Marocco, Romania, Senegal. | All. I p.116
- 466 | ragazzi | Residenti da 0 a 18 anni (2025) | Di cui 138 in età da scuola primaria e 135 da secondaria di II grado. | All. I pp.116-117
- circa 3.333 | abitanti | Stima 2035, scenario lineare | Tra circa 3.176 (scenario di crisi) e circa 3.526 (scenario di ripresa e contenimento). | All. I p.117

## Vent'anni di invecchiamento {type=text}
<!-- Accordion "Altri dati" -->
Nel 2002 gli over 65 erano il 17,7 % dei residenti, con un indice di vecchiaia di 124,7 (All. I pp.114, 116). Nel 2025 sono il 29,6 %: 1.102 persone contro 342 ragazzi sotto i 15 anni. L'indice di dipendenza è 63,3. Le stime al 2035 sono indicate come "circa" e non vanno sommate tra comuni (All. I p.117).

## Un suolo da leggere prima di usarlo {type=text}
<!-- Accordion "Altri dati" -->
Il territorio poggia per il 63,8 % sull'unità C1 e per il 27,4 % sull'unità C2 della Carta dei Suoli (P1 p.162). C1: suoli su graniti delle aree più aspre, con pendenze elevate, rocciosità, scarsa profondità e forte pericolo di erosione. La combinazione più estesa tra copertura e suolo è "Bosco di latifoglie su C1" (16,1 % del territorio). Lo studio commenta: "La prevalenza di C1 indica ampie superfici con forti limitazioni: pendenze, rocciosità, pietrosità, scarsa profondità, erosione. C5 e C3 possono indicare ambiti dove approfondire forestazione, infittimento e gestione razionale della vegetazione naturale."

## Elementi identitari {type=cards}
<!-- Accordion "Altri dati" -->
- **Polo industriale del sughero, distretto europeo della lavorazione**
- **Altopiani granitici e rilievi collinari**
- **Ex convento settecentesco, sede della Mostra del Sughero**
- **Complessi megalitici**
- **Saperi artigianali e manifatturieri del sughero**
- **Hub del Distretto Rurale del Sughero**

## Approfondisci nello studio {type=text}
La scheda demografica completa è nell'Allegato I (pp. 113-117). La scheda territoriale preliminare è nell'Allegato II (pp. 162-163). Il profilo del comune è nella Terza parte (pp. 59-60).
**CTA:** Scheda completa nel PDF (pp. 113-117) → /pdf/RISSTE_CUP_E77G24000450002_Parte1_signed.pdf#page=113
**CTA:** Scarica gli studi integrali (PDF) → /progetto#documenti
**CTA:** Torna a tutti i comuni → (Chiudi)

## Fonti {type=sources}
- Green community UCAG 193 – Strategie territoriali integrate (RISSTE, 2025), Prima parte – Demografia, Tabella 1a, p. 22; par. 1.8, pp. 27-28
- Green community UCAG 193, Seconda parte – Ambiente e territorio, Tabella 2a, p. 37
- Green community UCAG 193, Terza parte – I Comuni dell'Unione, par. 3.5, pp. 59-60
- Green community UCAG 193, Allegato I – Report demografico dei Comuni, scheda Calangianus, pp. 113-117
- Green community UCAG 193, Allegato II – SIT, cartografia e analisi biofisica, scheda Calangianus pp. 162-163; sintesi comparativa p. 172
