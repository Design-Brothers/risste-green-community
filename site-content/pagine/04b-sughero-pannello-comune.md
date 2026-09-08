---
slug: /sughero-sardegna?comune=[slug]      # non è una pagina: pannello laterale sopra l'esploratore di /sughero-sardegna
tipo: pannello
componente: ComuneDrawer
sezione: sughero-sardegna
eyebrow: "Sughero Sardegna · Scheda comune"
title: "{{nome_corrente}}"
document_title: "{{nome_corrente}} – Sughereta Sardegna · UCAG 193"   # aggiorna document.title a pannello aperto; canonical resta /sughero-sardegna
share_text: "{{nome_corrente}}: {{sugherete_ha}} ettari di sughereta, {{rank}}° su 30 in Sardegna. Suolo, fuoco, continuità e indicazioni dello studio RISSTE."
og_image: source/parte2-filiera-sughero-sardegna/images/fig-2-ivp-ranking-30-comuni.jpeg   # ereditata dalla pagina, nessun OG per comune
fonti:
  - documento: parte2
    pagine: "{{pagine_fonte}}"   # es. [82, 83, 84, 85]; più quadro sinottico [50, 51]
dati:
  - sughero-sardegna/comuni-sughereta.json
  - sughero-sardegna/indici-definizioni.json
  - sughero-sardegna/sintesi-regionale.json
figure: []
---

<!--
SPECIFICA DEL PANNELLO SCHEDA COMUNE (30 schede, componente `ComuneDrawer`). Non è una pagina: si apre sopra l'esploratore di /sughero-sardegna.
Un record di data/sughero-sardegna/comuni-sughereta.json → `dati[]` per scheda; il record si individua dal campo `slug`.
Pagine citate (P2 p.N) = pagine fisiche del PDF della Parte 2; la numerazione stampata è inferiore di 17.
-->

## Apertura e URL {type=spec}
- **Da dove si apre:** click su una barra o una riga dell'esploratore (`/sughero-sardegna#esploratore`); click su un comune nella matrice dei profili; click sul nome di un comune nelle card dei sette profili; apertura diretta di un link condiviso.
- **URL:** `/sughero-sardegna?comune={{slug}}` (es. `/sughero-sardegna?comune=tempio-pausania`). Gli slug sono i 30 valori di `comuni-sughereta.json → dati[].slug`, kebab-case senza accenti (`ala-dei-sardi`, `budduso`, `villanova-monteleone`).
- **Cronologia:** l'apertura fa `pushState`; "Chiudi" e il tasto Indietro tolgono il parametro e riportano il focus sulla barra/riga di origine. Cambiare comune dal pannello fa `replaceState`.
- **Caricamento con `?comune=` già presente:** la pagina si apre scrollata all'esploratore, con il pannello aperto e la riga del comune evidenziata. Nessuno stato di caricamento: i dati sono nel bundle.
- **Layout:** desktop pannello laterale destro, larghezza 480-560 px, sfondo `--ice`, il resto della pagina resta visibile e scorrevole; mobile foglio a tutta altezza. Focus intrappolato nel pannello, chiusura con Esc, `role="dialog"`, `aria-labelledby` = titolo.
- **Ancore interne al pannello:** nessuna; il pannello ha un solo scroll verticale.

## Azioni {type=spec}
<!-- barra fissa in testa al pannello; etichette da microcopy.md §6 -->
- **Chiudi** — chiude il pannello, toglie `?comune=` dall'URL, riporta il focus all'esploratore.
- **Copia link** — copia `https://{{host}}/sughero-sardegna?comune={{slug}}`; conferma "Link copiato".
- **Comune precedente nel ranking** — apre `?comune={{slug_precedente}}` (record con `rank − 1`); disattivato per Bitti (rank 1). Tooltip "{{rank − 1}}° · {{nome_precedente}}".
- **Comune successivo nel ranking** — apre `?comune={{slug_successivo}}` (record con `rank + 1`); disattivato per Bultei (rank 30). Tooltip "{{rank + 1}}° · {{nome_successivo}}".
- **Vedi {{nome_corrente}} nell'Alta Gallura** → `/alta-gallura?comune={{slug}}` — **solo** per `calangianus` e `tempio-pausania`, gli unici due comuni presenti in entrambi gli studi. Per gli altri 28 comuni il bottone non viene renderizzato.
- **Scheda completa nel PDF (pp. {{pagine_fonte_range}})** → `/progetto#documenti` (in coda al pannello, nel blocco Fonti).

## Stati {type=spec}
- **Vuoto (nessun `?comune=`):** pannello chiuso. Sotto il titolo dell'esploratore compare l'istruzione "Seleziona un comune nel grafico o nell'elenco per aprire la scheda."
- **Non trovato (`?comune=` con slug sconosciuto):** pannello aperto con eyebrow "Sughero Sardegna · Scheda comune", titolo "Comune non trovato", testo "Nessun comune della Sughereta Sardegna corrisponde a «{{valore_param}}». Il link potrebbe contenere un errore." CTA "Vedi i 30 comuni" (chiude il pannello e azzera i filtri) e "Cerca nell'Alta Gallura" → `/alta-gallura`. Il parametro non valido viene rimosso dall'URL alla chiusura. `document.title` non cambia.
- **Parametro vuoto (`?comune=`):** trattato come "vuoto": il parametro si rimuove.
- **Dato mancante in un campo:** la riga mostra "Dato non riportato nello studio." (microcopy §6). Nei 30 record correnti non si verifica.

## Ordine dei blocchi {type=spec}
1. Intestazione (eyebrow, titolo, sottotitolo con rank, ettari e quota; badge del profilo integrato)
2. KPI "Quanta sughereta e quanto pesa" (4)
3. KPI "Tre indici, tre classi" (3, con badge di classe)
4. Testo "Cosa dice la scheda dello studio" (sintesi esecutiva integrale)
5. Grafico "Dove il fuoco pesa di più" (barra impilata incendio)
6. Grafico "Su quali suoli cresce la sughera" (barra impilata pedologica)
7. Testo "Un nucleo o tanti frammenti"
8. Testo "Il profilo integrato" (con gli altri comuni dello stesso profilo, cliccabili)
9. Card "Indicazioni operative preliminari" (4)
10. Citazione "Cautela metodologica"
11. Testo "Da dove vengono questi numeri"
12. Fonti (con il link al PDF)

<!--
LEGENDA DEI SEGNAPOSTO {{campo}} (file → campo). Formato numeri: italiano (punto migliaia, virgola decimali), unità sempre esplicite.
Da data/sughero-sardegna/comuni-sughereta.json → dati[] (record del comune):
  {{nome_corrente}} nome del comune nella forma corrente · {{slug}} · {{rank}} posizione per estensione (1-30)
  {{sugherete_ha}} superficie a sughera (ha) · {{peso_pct_sughereta_sardegna}} quota % sul totale dei 30 comuni
  {{ivp}} indice 1-4 · {{classe_ivp}} Alta/Media/Bassa
  {{ipi}} indice incendio ponderato 0-100 · {{classe_incendio}} Mediobasso/Medio/Medioalto/Alto
  {{quota_medioalto_alto_pct}} % · {{quota_medioalto_alto_ha}} ha in classi Medioalto+Alto
  {{n_complessi}} · {{superficie_complesso_maggiore_ha}} · {{quota_complesso_maggiore_pct}} · {{superficie_media_complesso_ha}} · {{densita_frammentazione}} (complessi/100 ha) · {{classe_densita}} · {{classe_icr}}
  {{profilo_ivp_x_incendio}} profilo a due fattori · {{profilo_integrato}} profilo a tre fattori · {{combinazione}} terna "Alta x Medioalto x Media"
  {{sintesi_esecutiva}} testo integrale del punto 1 della scheda · {{lettura_icr}} frase di lettura della classe ICR
  {{indicazioni_operative}} lista di 4 frasi · {{distribuzione_incendio}} righe (classe, superficie_ha, incidenza_pct, indice_classe) · {{distribuzione_pedologica}} righe (unita_pedologica, superficie_ha, incidenza_pct, classe_capacita_uso, classe_ivp, punteggio_ivp)
  {{pagine_fonte}} pagine PDF della scheda · {{pagine_fonte_range}} derivato "prima-ultima" (es. 82-85) · {{pagine_stampate_range}} derivato = pagine PDF − 17 (es. 65-68)
  {{confronto_figure.ivp_fig2}} {{confronto_figure.ipi_fig3}} {{confronto_figure.classe_icr_fig4}} valori delle Figure 2-4 (null se il comune manca nella figura) · {{note}} avvertenze del record (lista, spesso vuota)
Derivati dal ranking (stesso file): {{slug_precedente}} {{nome_precedente}} = record con rank − 1 · {{slug_successivo}} {{nome_successivo}} = record con rank + 1
Da data/sughero-sardegna/indici-definizioni.json → dati:
  {{lettura_classe_ivp}} = indici[IVP].lettura_classi[classe_ivp]
  {{comuni_stesso_profilo}} = profili_integrati_distinti[profilo_integrato == profilo_integrato del comune].comuni, escluso il comune, resi con nome_corrente e cliccabili (?comune=slug) · {{n_comuni_stesso_profilo}} = numero degli altri comuni con lo stesso profilo
Da data/sughero-sardegna/sintesi-regionale.json → dati:
  {{totale_ha_30_comuni}} = totali.somma_sugherete_30_comuni_ha (83.790,90)
Derivati per i grafici (dal record del comune):
  {{quota_ivp_alta_pct}} {{quota_ivp_media_pct}} {{quota_ivp_bassa_pct}} {{quota_ivp_molto_bassa_pct}} = somma di incidenza_pct di distribuzione_pedologica per classe_ivp
Blocchi condizionali: [[if ...]] … [[endif]] si rendono solo se la condizione è vera.
Testo fisso di raccordo: tutto ciò che non è tra doppie graffe.
-->

## Intestazione {type=hero}
**Eyebrow:** Sughero Sardegna · Scheda comune
**Titolo:** {{nome_corrente}}
**Sottotitolo:** {{rank}}° comune su 30 per estensione · {{sugherete_ha}} ha · {{peso_pct_sughereta_sardegna}} % della Sughereta Sardegna
**Badge:** {{profilo_integrato}} (tooltip "Profilo integrato", microcopy §9)
**Azioni:** Chiudi · Copia link · Comune precedente · Comune successivo · [[if slug in (calangianus, tempio-pausania)]]Vedi {{nome_corrente}} nell'Alta Gallura → /alta-gallura?comune={{slug}}[[endif]]

## Quanta sughereta e quanto pesa {type=kpi}
<!-- valore | unità | etichetta | contesto | fonte -->
- {{sugherete_ha}} | ha | Superficie a sughera del comune | Su {{totale_ha_30_comuni}} ha complessivi dei 30 comuni prioritari. | P2 pp.{{pagine_fonte_range}}
- {{peso_pct_sughereta_sardegna}} % | della Sughereta Sardegna | Quota sul totale dei 30 comuni | La somma dei 30 pesi è 99,98 %. | P2 pp.50-51
- {{rank}}° | su 30 | Posizione per estensione | Ordine del quadro sinottico dell'Allegato I (1 = Bitti, 30 = Bultei). | P2 pp.50-51
- {{n_complessi}} | complessi | Nuclei di sughereta distinti | In media {{superficie_media_complesso_ha}} ha ciascuno. | P2 pp.{{pagine_fonte_range}}

## Tre indici, tre classi {type=kpi}
<!-- il badge di classe si colora con la scala ordinale §4 del brief e mostra sempre l'etichetta testuale -->
- {{ivp}} | IVP, scala 1-4 | Vocazionalità pedologica: classe {{classe_ivp}} | Media dei punteggi delle unità pedologiche pesata per superficie. | P2 pp.{{pagine_fonte_range}}
- {{ipi}} | IPI, scala 0-100 | Pericolo incendio: classe {{classe_incendio}} | {{quota_medioalto_alto_pct}} % della sughereta ({{quota_medioalto_alto_ha}} ha) è in classe Medioalto o Alto. | P2 pp.{{pagine_fonte_range}}
- {{quota_complesso_maggiore_pct}} % | nel nucleo maggiore | Continuità della risorsa: classe ICR {{classe_icr}} | Il complesso più esteso copre {{superficie_complesso_maggiore_ha}} ha. | P2 pp.{{pagine_fonte_range}}

## Cosa dice la scheda dello studio {type=text}
Il testo che segue è la sintesi esecutiva della scheda comunale dell'Allegato I, riportata integralmente (P2 pp.{{pagine_fonte_range}}).

{{sintesi_esecutiva}}

## Dove il fuoco pesa di più {type=chart}
**Grafico:** barre impilate al 100 % (una barra) — ripartizione dei {{sugherete_ha}} ha per classe di pericolo incendio, da Basso ad Alto, colori della scala incendio con etichetta di classe e valore diretto (ha e %).
**Dati:** data/sughero-sardegna/comuni-sughereta.json → `distribuzione_incendio[]` (`classe`, `superficie_ha`, `incidenza_pct`, `indice_classe`) del record `{{slug}}`. Tabella "Vedi i dati": Classe · ha · % · indice di classe.
**Lettura:** Le classi Medioalto e Alto coprono {{quota_medioalto_alto_ha}} ha, il {{quota_medioalto_alto_pct}} % della sughereta comunale. L'indice incendio ponderato è {{ipi}} (classe {{classe_incendio}}).
**Fonte:** P2, Allegato I, scheda comunale, tabella "pericolo incendio", pp. {{pagine_fonte_range}}

## Su quali suoli cresce la sughera {type=chart}
**Grafico:** barre impilate al 100 % (una barra) — ripartizione della sughereta per classe IVP delle unità pedologiche (Alta, Media, Bassa, Molto bassa); tooltip con le sigle delle unità (Carta dei suoli della Sardegna) e le classi di capacità d'uso.
**Dati:** data/sughero-sardegna/comuni-sughereta.json → `distribuzione_pedologica[]` (`unita_pedologica`, `superficie_ha`, `incidenza_pct`, `classe_capacita_uso`, `classe_ivp`, `punteggio_ivp`) del record `{{slug}}`; quote per classe derivate: Alta {{quota_ivp_alta_pct}} %, Media {{quota_ivp_media_pct}} %, Bassa {{quota_ivp_bassa_pct}} %, Molto bassa {{quota_ivp_molto_bassa_pct}} %. Tabella "Vedi i dati": Unità · ha · % · capacità d'uso · classe IVP · punteggio.
**Lettura:** L'IVP ponderato è {{ivp}}, in classe {{classe_ivp}}. {{lettura_classe_ivp}}
**Fonte:** P2, Allegato I, scheda comunale, tabella pedologica, pp. {{pagine_fonte_range}}

## Un nucleo o tanti frammenti {type=text}
La sughereta di {{nome_corrente}} è divisa in {{n_complessi}} complessi. Il maggiore copre {{superficie_complesso_maggiore_ha}} ha, pari al {{quota_complesso_maggiore_pct}} % del totale comunale. La superficie media per complesso è {{superficie_media_complesso_ha}} ha; la densità di frammentazione è {{densita_frammentazione}} complessi ogni 100 ha, in classe {{classe_densita}} (P2 pp.{{pagine_fonte_range}}).

{{lettura_icr}}

## Il profilo integrato {type=text}
Incrociando suolo e fuoco la scheda definisce il comune "{{profilo_ivp_x_incendio}}". Con la continuità la combinazione diventa {{combinazione}}. Il profilo integrato è: **{{profilo_integrato}}** (P2 pp.{{pagine_fonte_range}}).

[[if n_comuni_stesso_profilo > 0]]Lo stesso profilo è assegnato ad altri {{n_comuni_stesso_profilo}} comuni: {{comuni_stesso_profilo}} (ogni nome apre la sua scheda). Confrontali nell'esploratore, filtrato su questo profilo → /sughero-sardegna#esploratore[[endif]]
[[if n_comuni_stesso_profilo == 0]]Nessun altro comune tra i 30 ha questo profilo. Confronta gli altri profili nell'esploratore → /sughero-sardegna#esploratore[[endif]]

## Indicazioni operative preliminari {type=cards}
<!-- quattro card, una per frase di indicazioni_operative (ordine del record); prima lettera maiuscola, punto finale aggiunto -->
- **1** — {{indicazioni_operative[0]}}. `icona: check`
- **2** — {{indicazioni_operative[1]}}. `icona: check`
- **3** — {{indicazioni_operative[2]}}. `icona: check`
- **4** — {{indicazioni_operative[3]}}. `icona: check`

## Cautela metodologica {type=quote}
> La scheda è una sintesi comunale. Per individuare puntualmente le porzioni di sughereta più strategiche e vulnerabili è opportuno procedere con overlay GIS diretto tra unità pedologiche riclassificate, classi di pericolosità incendio e complessi sughericoli.
— Allegato I, scheda comunale di {{nome_corrente}}, punto 6, pp. {{pagine_fonte_range}}

## Da dove vengono questi numeri {type=text}
Tutti i valori sono tratti dalla scheda comunale dell'Allegato I (pagine PDF {{pagine_fonte_range}}, pagine stampate {{pagine_stampate_range}}) e coincidono con il quadro sinottico (P2 pp.50-51). Lo studio non esplicita soglie numeriche per le classi: fa fede la classe indicata nella scheda.

[[if confronto_figure.ivp_fig2 != null]]Nelle Figure 2, 3 e 4 dello studio il comune compare con valori diversi (IVP {{confronto_figure.ivp_fig2}}, IPI {{confronto_figure.ipi_fig3}}, ICR {{confronto_figure.classe_icr_fig4}}). Quelle figure sono un'elaborazione grafica precedente. I valori di riferimento sono quelli della scheda.[[endif]]
[[if confronto_figure.ivp_fig2 == null]]Il comune non compare in tutte le Figure 2-4 dello studio; i valori di riferimento sono quelli della scheda.[[endif]]

[[if note non vuota]]Avvertenze specifiche del record: {{note}}[[endif]]

## Fonti {type=sources}
- Valorizzazione della filiera del sughero in Sardegna – Un framework multidisciplinare (RISSTE, 2025), Allegato I "Studio tecnico sugherete – Dossier comunale integrato", scheda {{rank}} "{{nome_corrente}}", pp. {{pagine_fonte_range}} (stampate {{pagine_stampate_range}})
- Idem, Allegato I, nota metodologica e quadro sinottico, pp. 50-51
- Idem, Seconda parte, par. 2.2 "Analisi territoriale" (definizione degli indici), pp. 19-21
- Le pagine indicate sono quelle fisiche del PDF; la numerazione stampata è inferiore di 17.
- Scheda completa nel PDF (pp. {{pagine_fonte_range}}) → /progetto#documenti

---

<!-- ============================================================
ESEMPIO COMPILATO: Tempio Pausania (record slug "tempio-pausania", rank 11)
URL: /sughero-sardegna?comune=tempio-pausania
Valori reali da data/sughero-sardegna/comuni-sughereta.json; testo fisso identico alla specifica.
Precedente nel ranking: 10° Orani (?comune=orani) · Successivo: 12° Telti (?comune=telti)
Bottone Alta Gallura: renderizzato → /alta-gallura?comune=tempio-pausania
============================================================ -->

```yaml
slug: /sughero-sardegna?comune=tempio-pausania
tipo: pannello
sezione: sughero-sardegna
eyebrow: "Sughero Sardegna · Scheda comune"
title: "Tempio Pausania"
document_title: "Tempio Pausania – Sughereta Sardegna · UCAG 193"
share_text: "Tempio Pausania: 2.945,38 ettari di sughereta, 11° su 30 in Sardegna. Suolo, fuoco, continuità e indicazioni dello studio RISSTE."
fonti:
  - documento: parte2
    pagine: [50, 51, 82, 83, 84, 85]
dati:
  - sughero-sardegna/comuni-sughereta.json
  - sughero-sardegna/indici-definizioni.json
  - sughero-sardegna/sintesi-regionale.json
figure: []
```

## Intestazione {type=hero}
**Eyebrow:** Sughero Sardegna · Scheda comune
**Titolo:** Tempio Pausania
**Sottotitolo:** 11° comune su 30 per estensione · 2.945,38 ha · 3,52 % della Sughereta Sardegna
**Badge:** Priorità alta: risorsa vocata, esposta e territorialmente governabile
**Azioni:** Chiudi · Copia link · Comune precedente (10° · Orani) · Comune successivo (12° · Telti) · Vedi Tempio Pausania nell'Alta Gallura → /alta-gallura?comune=tempio-pausania

## Quanta sughereta e quanto pesa {type=kpi}
- 2.945,38 | ha | Superficie a sughera del comune | Su 83.790,90 ha complessivi dei 30 comuni prioritari. | P2 pp.82-85
- 3,52 % | della Sughereta Sardegna | Quota sul totale dei 30 comuni | La somma dei 30 pesi è 99,98 %. | P2 pp.50-51
- 11° | su 30 | Posizione per estensione | Ordine del quadro sinottico dell'Allegato I (1 = Bitti, 30 = Bultei). | P2 pp.50-51
- 34 | complessi | Nuclei di sughereta distinti | In media 86,63 ha ciascuno. | P2 pp.82-85

## Tre indici, tre classi {type=kpi}
- 3,751 | IVP, scala 1-4 | Vocazionalità pedologica: classe Alta | Media dei punteggi delle unità pedologiche pesata per superficie. | P2 pp.82-85
- 43,12 | IPI, scala 0-100 | Pericolo incendio: classe Medioalto | 90,07 % della sughereta (2.653,00 ha) è in classe Medioalto o Alto. | P2 pp.82-85
- 73,87 % | nel nucleo maggiore | Continuità della risorsa: classe ICR Media | Il complesso più esteso copre 2.175,85 ha. | P2 pp.82-85

## Cosa dice la scheda dello studio {type=text}
Il testo che segue è la sintesi esecutiva della scheda comunale dell'Allegato I, riportata integralmente (P2 pp.82-85).

Tempio Pausania presenta 2.945,38 ha di sugherete, pari al 3,52% della Sughereta Sardegna. L'IVP ponderato è 3,751, in classe Alta. La risorsa mostra una buona coerenza pedologica complessiva con la sughereta, pur con limitazioni locali legate alle unità pedologiche specifiche. Il profilo incendio evidenzia una criticità elevata: la classe ponderata è Medioalto e 2.653,00 ha (90,07%) ricadono nelle classi Medioalto e Alto. Queste superfici richiedono priorità nella pianificazione antincendio e nella gestione attiva. La classe ICR è Media: il complesso maggiore concentra il 73,87% della risorsa, con nuclei secondari significativi. La gestione può concentrarsi sul nucleo principale, senza trascurare le aree minori. Il profilo integrato assegnato è: Priorità alta: risorsa vocata, esposta e territorialmente governabile.

## Dove il fuoco pesa di più {type=chart}
**Grafico:** barre impilate al 100 % (una barra) — ripartizione dei 2.945,38 ha per classe di pericolo incendio, da Basso ad Alto, colori della scala incendio con etichetta di classe e valore diretto (ha e %).
**Dati:** data/sughero-sardegna/comuni-sughereta.json → `distribuzione_incendio[]` del record `tempio-pausania`: Mediobasso 24,57 ha (0,83 %, indice 23,20) · Medio 267,81 ha (9,09 %, indice 31,75) · Medioalto 1.214,43 ha (41,23 %, indice 39,94) · Alto 1.438,57 ha (48,84 %, indice 48,26). Nessuna superficie in classe Basso.
**Lettura:** Le classi Medioalto e Alto coprono 2.653,00 ha, il 90,07 % della sughereta comunale. L'indice incendio ponderato è 43,12 (classe Medioalto).
**Fonte:** P2, Allegato I, scheda comunale, tabella "pericolo incendio", pp. 82-85

## Su quali suoli cresce la sughera {type=chart}
**Grafico:** barre impilate al 100 % (una barra) — ripartizione della sughereta per classe IVP delle unità pedologiche; tooltip con sigle delle unità e classi di capacità d'uso.
**Dati:** data/sughero-sardegna/comuni-sughereta.json → `distribuzione_pedologica[]` del record `tempio-pausania`: C2 2.212,82 ha (75,13 %, capacità VII-VI-IV, Alta, 4) · C1 361,24 ha (12,26 %, VIII, Media, 3) · C3 283,94 ha (9,64 %, VII-VI-IV, Media, 3) · B2 53,00 ha (1,80 %, VII-VI, Media, 3) · I1 33,29 ha (1,13 %, III-IV, Media, 3) · O 1,10 ha (0,04 %, –, Molto bassa, 1). Quote per classe: Alta 75,13 %, Media 24,83 %, Bassa 0 %, Molto bassa 0,04 %.
**Lettura:** L'IVP ponderato è 3,751, in classe Alta. La risorsa mostra una buona coerenza pedologica complessiva con la sughereta, pur con limitazioni locali legate alle unità pedologiche specifiche.
**Fonte:** P2, Allegato I, scheda comunale, tabella pedologica, pp. 82-85

## Un nucleo o tanti frammenti {type=text}
La sughereta di Tempio Pausania è divisa in 34 complessi. Il maggiore copre 2.175,85 ha, pari al 73,87 % del totale comunale. La superficie media per complesso è 86,63 ha; la densità di frammentazione è 1,15 complessi ogni 100 ha, in classe Media (P2 pp.82-85).

La classe ICR è Media: il complesso maggiore concentra il 73,87% della risorsa, con nuclei secondari significativi. La gestione può concentrarsi sul nucleo principale, senza trascurare le aree minori.

## Il profilo integrato {type=text}
Incrociando suolo e fuoco la scheda definisce il comune "Risorsa strategica vulnerabile". Con la continuità la combinazione diventa Alta x Medioalto x Media. Il profilo integrato è: **Priorità alta: risorsa vocata, esposta e territorialmente governabile** (P2 pp.82-85).

Lo stesso profilo è assegnato ad altri 7 comuni: Berchidda, Oschiri, Telti, Illorai, Oliena, Bono, Bultei (ogni nome apre la sua scheda). Confrontali nell'esploratore, filtrato su questo profilo → /sughero-sardegna#esploratore

## Indicazioni operative preliminari {type=cards}
- **1** — Valorizzare la buona vocazionalità pedologica come base per progetti pilota, certificazione e gestione forestale attiva. `icona: check`
- **2** — Attribuire priorità agli interventi di prevenzione incendi, riduzione del combustibile e presidio delle aree in classi Medioalto e Alto. `icona: check`
- **3** — Utilizzare il complesso principale come ambito preferenziale per interventi coordinati e monitoraggio. `icona: check`
- **4** — Integrare i risultati con verifiche locali su proprietà, accessibilità, stato selvicolturale e continuità del combustibile. `icona: check`

## Cautela metodologica {type=quote}
> La scheda è una sintesi comunale. Per individuare puntualmente le porzioni di sughereta più strategiche e vulnerabili è opportuno procedere con overlay GIS diretto tra unità pedologiche riclassificate, classi di pericolosità incendio e complessi sughericoli.
— Allegato I, scheda comunale di Tempio Pausania, punto 6, pp. 82-85

## Da dove vengono questi numeri {type=text}
Tutti i valori sono tratti dalla scheda comunale dell'Allegato I (pagine PDF 82-85, pagine stampate 65-68) e coincidono con il quadro sinottico (P2 pp.50-51). Lo studio non esplicita soglie numeriche per le classi: fa fede la classe indicata nella scheda.

Nelle Figure 2, 3 e 4 dello studio il comune compare con valori diversi (IVP 3,582, IPI 41,2, ICR Media). Quelle figure sono un'elaborazione grafica precedente. I valori di riferimento sono quelli della scheda.

## Fonti {type=sources}
- Valorizzazione della filiera del sughero in Sardegna – Un framework multidisciplinare (RISSTE, 2025), Allegato I "Studio tecnico sugherete – Dossier comunale integrato", scheda 11 "Tempio Pausania", pp. 82-85 (stampate 65-68)
- Idem, Allegato I, nota metodologica e quadro sinottico, pp. 50-51
- Idem, Seconda parte, par. 2.2 "Analisi territoriale" (definizione degli indici), pp. 19-21
- Le pagine indicate sono quelle fisiche del PDF; la numerazione stampata è inferiore di 17.
- Scheda completa nel PDF (pp. 82-85) → /progetto#documenti
