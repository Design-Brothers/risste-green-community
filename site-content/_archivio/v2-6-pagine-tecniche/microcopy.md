# Microcopy – etichette, CTA, testi di stato, tooltip

Testi brevi ricorrenti del mini-sito Green community UCAG 193 (6 pagine + pannello comune). Regole: italiano, tono istituzionale ma piano, frasi ≤ 22 parole, verbi attivi, nessuna enfasi promozionale. Ogni numero citato ha la pagina PDF (P1 = Studio 1 Alta Gallura, P2 = Studio 2 Sughero Sardegna).

## 1. Navigazione principale (3 voci)

| Etichetta | Slug | Note |
|---|---|---|
| Progetto | `/progetto` | apre il sotto-menu con le ancore della pagina |
| Alta Gallura | `/alta-gallura` | apre il sotto-menu di sezione |
| Sughero Sardegna | `/sughero-sardegna` | apre il sotto-menu di sezione |

Logo/home: "Green community UCAG 193" (link a `/`). Attributo `aria-label` del nav: "Navigazione principale".
Bottone menu mobile: "Menu" / "Chiudi menu".
Skip-link: "Vai al contenuto".
Bottone secondario nell'header (desktop): "Scarica i PDF" → `/progetto#documenti`.

## 2. Sotto-menu di sezione (pill sticky)

**Progetto** (ancore della stessa pagina)

| Etichetta | Slug |
|---|---|
| Il progetto | `/progetto` |
| Documenti | `/progetto#documenti` |
| Dati aperti | `/progetto#dati` |
| Glossario | `/progetto#glossario` |

**Alta Gallura**

| Etichetta | Slug |
|---|---|
| Territorio e comuni | `/alta-gallura` |
| Strategia | `/alta-gallura/strategia` |

**Sughero Sardegna**

| Etichetta | Slug |
|---|---|
| La Sughereta | `/sughero-sardegna` |
| Innovazione | `/sughero-sardegna/innovazione` |

Le schede comune non hanno breadcrumb: si aprono in un pannello laterale sopra la pagina di sezione (vedi §6, Pannello comune). Il pannello ha un'intestazione "Alta Gallura · Scheda comune" o "Sughero Sardegna · Scheda comune".

## 3. Eyebrow di sezione (sopra l'H1)

| Pagina | Eyebrow |
|---|---|
| `/` | Green community UCAG 193 |
| `/progetto` | Il progetto |
| `/progetto#documenti` (intestazione della macro-sezione) | Il progetto · Documenti |
| `/alta-gallura` | Alta Gallura |
| `/alta-gallura/strategia` | Alta Gallura · Strategia |
| `/sughero-sardegna` | Sughero Sardegna |
| `/sughero-sardegna/innovazione` | Sughero Sardegna · Innovazione |
| pannello `?comune=slug` su `/alta-gallura` | Alta Gallura · Scheda comune |
| pannello `?comune=slug` su `/sughero-sardegna` | Sughero Sardegna · Scheda comune |

## 4. Footer

Colonna 1 – Progetto
- "Green community UCAG 193 – Strategie territoriali integrate per l'Unione dei Comuni Alta Gallura."
- "CUP E77G24000450002"
- Loghi: R.I.S.S.T.E.; Unione dei Comuni Alta Gallura; PNRR / Next Generation EU e Regione Sardegna se richiesti dal finanziamento (da procurare).

Colonna 2 – Studi
- "Studio 1 · Green community UCAG 193 (PDF, 219 pagine, 6,2 MB)" → `/pdf/RISSTE_CUP_E77G24000450002_Parte1_signed.pdf`
- "Studio 2 · Valorizzazione della filiera del sughero in Sardegna (PDF, 196 pagine, 5,3 MB)" → `/pdf/RISSTE_CUP_E77G24000450002_Parte2_signed.pdf`
- "Le 16 figure originali" → `/progetto#figure`
- "Dataset aperti" → `/progetto#dati`
- "Glossario" → `/progetto#glossario`

Colonna 3 – R.I.S.S.T.E.
- "R.I.S.S.T.E. – Centro Studi per la Ricerca, l'Innovazione, lo Sviluppo Sostenibile e la Transizione Energetica"
- "Via Basilicata n. 3, 07026 Olbia"
- "PEC centrostudirisste@pec.it · risste.life@gmail.com"
- "Contatti" → `/progetto#contatti`

Riga legale
- "© 2025 R.I.S.S.T.E. Testi e dati degli studi riprodotti con il consenso degli autori. Licenza dati: CC BY 4.0 (da confermare)."
- "Note legali" · "Privacy" (nessun cookie di tracciamento) · "Dichiarazione di accessibilità"
- "Ultimo aggiornamento: [data build]"
- "I numeri di questo sito provengono dagli studi RISSTE 2025; ogni dato indica la pagina del PDF di origine." (vedi §8)

## 5. CTA ricorrenti

| Contesto | Testo | Destinazione |
|---|---|---|
| Hero landing, CTA 1 | Esplora l'Alta Gallura | `/alta-gallura` |
| Hero landing, CTA 2 | Scopri la Sughereta Sardegna | `/sughero-sardegna` |
| Landing, "in 60 parole" e "Chi siamo" | Conosci il progetto | `/progetto` |
| Landing, messaggio 01 | Leggi il territorio | `/alta-gallura` |
| Landing, messaggio 02 | Scopri la Sughereta Sardegna | `/sughero-sardegna` |
| Landing, messaggio 03 | Esplora i 30 comuni | `/sughero-sardegna#esploratore` |
| Landing, messaggio 04 | Vedi la strategia | `/alta-gallura/strategia` |
| Landing, messaggio 05 | Vedi la roadmap | `/alta-gallura/strategia#roadmap` |
| Fine blocco / hub di sezione | Approfondisci | sottopagina di sezione |
| Blocco dati | Vedi i dati | tabella accessibile sotto il grafico |
| Fine pagina di sezione | Leggi il capitolo nel PDF (pp. N-M) | `/pdf/…#page=N` |
| Ovunque | Scarica gli studi integrali (PDF) | `/progetto#documenti` |
| Esploratore comuni (card, riga, mappa) | Apri scheda | `?comune=[slug]` (pannello) |
| Pannello comune | Chiudi | chiude il pannello, torna all'esploratore |
| Pannello comune | Copia link | copia `…/alta-gallura?comune=[slug]` |
| Pannello comune (Calangianus, Tempio Pausania) | Vedi anche nella sezione Sughero Sardegna | `/sughero-sardegna?comune=[slug]` |
| Pannello comune (Calangianus, Tempio Pausania) | Vedi anche nella sezione Alta Gallura | `/alta-gallura?comune=[slug]` |
| Pannello comune | Scheda completa nel PDF (pp. N-M) | `/pdf/…#page=N` |
| Figura | Ingrandisci · Scarica | lightbox / file |
| Alta Gallura, fine ambiente | Vedi la strategia e la roadmap | `/alta-gallura/strategia` |
| Strategia, fine pagina | Torna al territorio e ai comuni | `/alta-gallura` |
| Sughereta, lettura integrata | Scopri innovazione e S.U.G.H.E.R.A. | `/sughero-sardegna/innovazione` |
| Innovazione, fine pagina | Torna ai 30 comuni | `/sughero-sardegna` |
| Bibliografia | Esporta CSV | download client-side |
| Progetto, cautela sulle figure | Vedi i grafici ricostruiti dalle schede | `/sughero-sardegna` |

## 6. Testi di stato e controlli

**Pagina 404**
- Titolo: "Questa pagina non esiste"
- Testo: "Il link potrebbe essere cambiato o contenere un errore. Riparti dalla home oppure cerca il tuo comune."
- CTA: "Torna alla home" → `/` · "Gli 11 comuni dell'Alta Gallura" → `/alta-gallura#comuni` · "I 30 comuni della Sughereta" → `/sughero-sardegna#esploratore`
- Redirect dai vecchi URL (prima versione a 12 pagine): `/alta-gallura/territorio`, `/alta-gallura/comuni` → `/alta-gallura`; `/alta-gallura/green-community`, `/alta-gallura/roadmap` → `/alta-gallura/strategia`; `/sughero-sardegna/sughereta` → `/sughero-sardegna`; `/sughero-sardegna/framework` → `/sughero-sardegna/innovazione`; `/documenti` → `/progetto#documenti`; `/alta-gallura/comuni/[slug]` → `/alta-gallura?comune=[slug]`; `/sughero-sardegna/comuni/[slug]` → `/sughero-sardegna?comune=[slug]`.

**Pannello comune** (`ComuneDrawer`, URL `?comune=slug`)
- Trigger su card, riga della tabella e comune della mappa: "Apri scheda" (`aria-label`: "Apri la scheda di {comune}")
- Intestazione: eyebrow di sezione (§3) + nome del comune come titolo + sottotitolo "{fascia} · {abitanti} abitanti (2025)" (Alta Gallura) oppure "{ettari} ha di sughereta · {rank}° su 30" (Sughereta)
- Bottone di chiusura: "Chiudi" (`aria-label`: "Chiudi la scheda"; anche tasto Esc e click fuori dal pannello)
- Condividi: "Copia link" → conferma "Link copiato" (2 secondi), errore "Non è stato possibile copiare il link"
- Rimando incrociato (solo Calangianus e Tempio Pausania): "Vedi anche nella sezione Sughero Sardegna" / "Vedi anche nella sezione Alta Gallura"
- Navigazione tra schede: "Comune precedente" · "Comune successivo" (nell'ordine dell'esploratore)
- Fine scheda: "Scheda completa nel PDF (pp. N-M)" · "Torna a tutti i comuni" (= Chiudi)
- Stato: "Caricamento della scheda…" · "Comune non trovato. Scegli un comune dall'elenco." (slug sconosciuto in URL)
- Accessibilità: `role="dialog"`, `aria-modal="true"`, `aria-labelledby` sul nome del comune; focus sul titolo all'apertura, ritorno al trigger alla chiusura.
- Titolo documento con pannello aperto: vedi `seo.md`, riga "pannello comune".

**Grafici e dati**
- Espandi tabella: "Vedi i dati" · chiudi: "Nascondi i dati"
- Didascalia tabella: "Tabella dei valori mostrati nel grafico."
- Fonte: "Fonte: *titolo breve dello studio*, p. N" (es. "Fonte: Green community UCAG 193, Tab. 1a, p. 22")
- Tooltip valore: "{comune}: {valore} {unità}"
- Legenda costa/interno: "Costa (4 comuni)" · "Interno (7 comuni)"
- Nota valori mancanti: "Dato non riportato nello studio."
- Nota refuso: "Valore come scritto nella fonte; vedi nota nel dataset."
- Pillola fonte dei KPI (landing e blocchi statistiche): "Da ISTAT 2025" · "Da schede comunali" · "Da Studio 1, p. N" · "Da Studio 2, p. N"

**Landing (hero e messaggi)**
- Indicatore di scorrimento sotto l'hero: "Scorri" (freccia; nascosto con `prefers-reduced-motion`)
- Contatore dei messaggi: "01 / 05" … "05 / 05"
- Micro-etichette dell'hero: "RISSTE —" · "— UCAG 193" · "11 COMUNI" · "30 COMUNI" · "2025"
- Alternativa testuale degli orbi: `aria-hidden="true"` (decorativi); nessun testo.

**Figure (lightbox)**
- "Ingrandisci" · "Chiudi" · "Scarica l'immagine" · "Figura N di 16"
- Fonte sotto la figura: "Figura originale dello studio, p. N. Riprodotta senza modifiche."

**Download**
- "Scarica (PDF, 6,2 MB)" · "Scarica (PDF, 5,3 MB)" · "Scarica i dati (JSON)" · "Scarica i dati (CSV)"
- Avviso: "Il PDF si apre in una nuova scheda."

**Filtri, ordinamento, ricerca**
- "Ordina per: ettari · IVP · pericolo incendio · ICR" · "Filtra per classe" · "Tutte le classi"
- Costa/interno: "Tutti · Costa · Interno"
- Ricerca bibliografia: "Cerca per titolo, autore o parola chiave" · "Settore" · "Paese" · "Priorità" · "TRL"
- Risultati: "{n} pubblicazioni su 153" · "Nessun risultato. Prova con un termine più generale o azzera i filtri." · "Azzera i filtri"
- Paginazione: "Pagina {n} di {m}" · "Precedente" · "Successiva" · "25 righe per pagina"
- Stato: "Caricamento dei dati…" · "Non è stato possibile caricare i dati. Ricarica la pagina."

**Mappa**
- Istruzione: "Seleziona un comune sulla mappa o nell'elenco."
- Tooltip: "{comune} · {fascia} · {abitanti} abitanti (2025)" (Alta Gallura) · "{comune} · {ettari} ha · IVP {classe}" (Sughereta)
- Alternativa testuale: "Elenco dei comuni" (lista equivalente sempre presente)

**Varie**
- "Torna su" · "Condividi" · "Copia link" · "Link copiato"
- Aggiornamento: "Dati aggiornati agli studi RISSTE 2025."
- Badge classe: sempre con etichetta testuale, es. "IVP Alta", "Incendio Medioalto", "ICR Molto bassa".

## 7. Formula di citazione consigliata

Studio 1 — R.I.S.S.T.E. (2025). *Green community UCAG 193 – Strategie territoriali integrate: gestione forestale e sviluppo sostenibile delle filiere locali*. Olbia: R.I.S.S.T.E. Progetto CUP E77G24000450002, 219 pp.

Studio 2 — R.I.S.S.T.E. (2025). *Valorizzazione della filiera del sughero in Sardegna – Un framework multidisciplinare per l'integrazione tra analisi territoriale, innovazione e gestione sostenibile*. Olbia: R.I.S.S.T.E. Progetto CUP E77G24000450002, 196 pp.

Pagina del sito — R.I.S.S.T.E. (2025). *Green community UCAG 193 – [titolo pagina]*, [URL], consultato il [data].

Forma breve nelle note fonte: "Green community UCAG 193, p. N" · "Filiera del sughero in Sardegna, p. N".

## 8. Dichiarazione breve sui numeri

Versione footer (una riga):
"I numeri di questo sito provengono dai due studi RISSTE 2025; ogni dato indica la pagina del PDF di origine."

Versione estesa (`/progetto#dati`, sopra le tab dei dataset):
"I numeri di questo sito provengono dai due studi RISSTE del 2025 e dai loro allegati. Non contengono stime aggiunte: dove lo studio non riporta un dato, il sito non lo mostra. Ogni grafico e ogni KPI indica la pagina del PDF da cui è tratto. I dataset in formato aperto sono la base di tutti i grafici."

## 9. Tooltip degli indici e delle fasce

Ogni tooltip: sigla sciolta, domanda a cui risponde, scala, classi, una riga di lettura. ≤ 45 parole.

**IVP — Indice di Vocazionalità Pedologica**
"Su quali suoli cresce la sughereta? Riclassifica i suoli sotto sughereta con un punteggio da 1 a 4 e ne fa la media ponderata per comune. Classi: Alta, Media, Bassa, Molto bassa. Alta = suoli coerenti con la sughera." (P2 pp. 20, 27, 50)

**IPI — Indice di Pericolosità da Incendio**
"Quanto è esposta al fuoco la risorsa? Incrocia le sugherete con la carta regionale del pericolo incendio 2023-2025. Classi: Basso, Mediobasso, Medio, Medioalto, Alto. Ogni scheda indica anche la quota di superficie nelle classi Medioalto e Alto." (P2 pp. 20, 28, 50)

**ICR — Indice di Continuità della Risorsa**
"Quanto è continua o frammentata la sughereta? Conta i complessi boscati e misura il peso del nucleo maggiore. Classi: Alta, Media, Bassa, Molto bassa. Alta = risorsa accorpata, più facile da gestire con interventi coordinati." (P2 pp. 20, 28-29, 50)

**Costa — Fascia costiera**
"Quattro comuni: Aglientu, Badesi, Santa Teresa Gallura, Trinità d'Agultu e Vignola. Economia balneare e ricettiva, forte attrazione migratoria: +14 % di residenti dal 2001 al 2025." (P1 pp. 16, 25)

**Interno — Entroterra**
"Sette comuni: Aggius, Bortigiadas, Calangianus, Luogosanto, Luras, Tempio Pausania, Viddalba. Nucleo storico, manifatturiero e del sughero; popolazione in calo del 10,1 % dal 2001 al 2025." (P1 pp. 16, 25)

**Profilo integrato** (pannello comune Sughereta)
"Lettura congiunta di IVP, pericolo incendio e ICR assegnata a ciascun comune nell'Allegato I. Indica priorità e tipo di gestione consigliata, ad esempio 'Priorità alta: risorsa vocata, esposta e territorialmente governabile'." (P2 pp. 35-37, 52-141)

## 10. Note ricorrenti

- Cautela metodologica (pannello Sughereta): "Le classi derivano da elaborazioni GIS su carte regionali a scale diverse. Il documento non esplicita le soglie numeriche: i valori vanno letti come indicazioni di priorità, non come misure di campo." (P2 p. 50; indici-definizioni.json)
- Cautela sulle Figure 2-4 di P2: "Le classi delle figure originali non coincidono sempre con i dossier comunali. I grafici del sito usano i dossier." (sintesi-regionale.json, note)
- Anno di riferimento popolazione: "2025 = residenti al 1° gennaio 2025; 2023 = 31 dicembre; 2001 e 2011 = censimenti." (README-demografia.md)
- Pagine PDF: "I numeri di pagina rimandano alla pagina fisica del PDF, non alla numerazione stampata."
- Conteggi dai dossier vs testo (landing, messaggio 03 e Sughereta): "Il testo indica 22 comuni a IVP alta; le 30 schede ne danno 21. Il sito usa le schede." (P2 pp. 27, 50-141; sintesi-regionale.json)
