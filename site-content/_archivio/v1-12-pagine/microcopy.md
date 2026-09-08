# Microcopy – etichette, CTA, testi di stato, tooltip

Testi brevi ricorrenti del mini-sito Green community UCAG 193. Regole: italiano, tono istituzionale ma piano, frasi ≤ 22 parole, verbi attivi, nessuna enfasi promozionale. Ogni numero citato ha la pagina PDF (P1 = Studio 1 Alta Gallura, P2 = Studio 2 Sughero Sardegna).

## 1. Navigazione principale

| Etichetta | Slug | Note |
|---|---|---|
| Progetto | `/progetto` | |
| Alta Gallura | `/alta-gallura` | apre il sotto-menu di sezione |
| Sughero Sardegna | `/sughero-sardegna` | apre il sotto-menu di sezione |
| Documenti | `/documenti` | |

Logo/home: "Green community UCAG 193" (link a `/`). Attributo `aria-label` del nav: "Navigazione principale".
Bottone menu mobile: "Menu" / "Chiudi menu".
Skip-link: "Vai al contenuto".

## 2. Sotto-menu di sezione (pill sticky)

**Alta Gallura**

| Etichetta | Slug |
|---|---|
| Panoramica | `/alta-gallura` |
| Territorio | `/alta-gallura/territorio` |
| Comuni | `/alta-gallura/comuni` |
| Green community | `/alta-gallura/green-community` |
| Roadmap | `/alta-gallura/roadmap` |

**Sughero Sardegna**

| Etichetta | Slug |
|---|---|
| Panoramica | `/sughero-sardegna` |
| Sughereta | `/sughero-sardegna/sughereta` |
| Innovazione | `/sughero-sardegna/innovazione` |
| Framework | `/sughero-sardegna/framework` |

Breadcrumb schede comune: "Alta Gallura › Comuni › Tempio Pausania"; "Sughero Sardegna › Sughereta › Bitti".

## 3. Eyebrow di sezione (sopra l'H1)

| Pagina | Eyebrow |
|---|---|
| `/` | Green community UCAG 193 |
| `/progetto` | Il progetto |
| `/alta-gallura` | Alta Gallura |
| `/alta-gallura/territorio` | Alta Gallura · Territorio |
| `/alta-gallura/comuni` | Alta Gallura · Comuni |
| `/alta-gallura/comuni/[slug]` | Alta Gallura · Scheda comune |
| `/alta-gallura/green-community` | Alta Gallura · Green community |
| `/alta-gallura/roadmap` | Alta Gallura · Roadmap |
| `/sughero-sardegna` | Sughero Sardegna |
| `/sughero-sardegna/sughereta` | Sughero Sardegna · Sughereta |
| `/sughero-sardegna/comuni/[slug]` | Sughero Sardegna · Scheda comune |
| `/sughero-sardegna/innovazione` | Sughero Sardegna · Innovazione |
| `/sughero-sardegna/framework` | Sughero Sardegna · Framework |
| `/documenti` | Documenti |

## 4. Footer

Colonna 1 – Progetto
- "Green community UCAG 193 – Strategie territoriali integrate per l'Unione dei Comuni Alta Gallura."
- "CUP E77G24000450002"
- Loghi: R.I.S.S.T.E.; Unione dei Comuni Alta Gallura; PNRR / Next Generation EU e Regione Sardegna se richiesti dal finanziamento (da procurare).

Colonna 2 – Studi
- "Studio 1 · Green community UCAG 193 (PDF, 219 pagine, 6,2 MB)"
- "Studio 2 · Valorizzazione della filiera del sughero in Sardegna (PDF, 196 pagine, 5,3 MB)"
- "Dataset aperti" → `/documenti#dati`
- "Glossario" → `/documenti#glossario`

Colonna 3 – R.I.S.S.T.E.
- "R.I.S.S.T.E. – Centro Studi per la Ricerca, l'Innovazione, lo Sviluppo Sostenibile e la Transizione Energetica"
- "Via Basilicata n. 3, 07026 Olbia"
- "PEC centrostudirisste@pec.it · risste.life@gmail.com"

Riga legale
- "© 2025 R.I.S.S.T.E. Testi e dati degli studi riprodotti con il consenso degli autori. Licenza dati: CC BY 4.0 (da confermare)."
- "Note legali" · "Privacy" (nessun cookie di tracciamento) · "Dichiarazione di accessibilità"
- "Ultimo aggiornamento: [data build]"
- "I numeri di questo sito provengono dagli studi RISSTE 2025; ogni dato indica la pagina del PDF di origine." (vedi §8)

## 5. CTA ricorrenti

| Contesto | Testo | Destinazione |
|---|---|---|
| Hero home, card 1 | Esplora l'Alta Gallura | `/alta-gallura` |
| Hero home, card 2 | Scopri la Sughereta Sardegna | `/sughero-sardegna` |
| Fine blocco home / hub | Approfondisci | pagina tematica |
| Blocco dati | Vedi i dati | tabella accessibile sotto il grafico |
| Fine pagina tematica | Leggi il capitolo nel PDF (pp. N-M) | `/pdf/…#page=N` |
| Ovunque | Scarica lo studio integrale (PDF) | `/documenti` |
| Indice comuni | Apri la scheda | `/…/comuni/[slug]` |
| Scheda comune | Torna a tutti i comuni | indice |
| Scheda comune | Scheda completa nel PDF (pp. N-M) | `/pdf/…#page=N` |
| Figura | Ingrandisci · Scarica | lightbox / file |
| Roadmap | Vedi la roadmap completa | `/alta-gallura/roadmap` |
| Sughereta | Esplora i 30 comuni | `/sughero-sardegna/sughereta` |
| Bibliografia | Esporta CSV | download client-side |
| Home, blocco "Chi siamo" | Conosci il progetto | `/progetto` |

## 6. Testi di stato e controlli

**Pagina 404**
- Titolo: "Questa pagina non esiste"
- Testo: "Il link potrebbe essere cambiato o contenere un errore. Riparti dalla home oppure cerca il tuo comune."
- CTA: "Torna alla home" → `/` · "Tutti i comuni dell'Alta Gallura" → `/alta-gallura/comuni` · "I 30 comuni della Sughereta" → `/sughero-sardegna/sughereta`

**Grafici e dati**
- Espandi tabella: "Vedi i dati" · chiudi: "Nascondi i dati"
- Didascalia tabella: "Tabella dei valori mostrati nel grafico."
- Fonte: "Fonte: *titolo breve dello studio*, p. N" (es. "Fonte: Green community UCAG 193, Tab. 1a, p. 22")
- Tooltip valore: "{comune}: {valore} {unità}"
- Legenda costa/interno: "Costa (4 comuni)" · "Interno (7 comuni)"
- Nota valori mancanti: "Dato non riportato nello studio."
- Nota refuso: "Valore come scritto nella fonte; vedi nota nel dataset."

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
- Tooltip: "{comune} · {fascia} · {abitanti} abitanti (2025)"
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

Versione estesa (pagina Documenti, blocco dati):
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

**Profilo integrato** (schede comune Sughereta)
"Lettura congiunta di IVP, pericolo incendio e ICR assegnata a ciascun comune nell'Allegato I. Indica priorità e tipo di gestione consigliata, ad esempio 'Priorità alta: risorsa vocata, esposta e territorialmente governabile'." (P2 pp. 35-37, 52-141)

## 10. Note ricorrenti

- Cautela metodologica (schede Sughereta): "Le classi derivano da elaborazioni GIS su carte regionali a scale diverse. Il documento non esplicita le soglie numeriche: i valori vanno letti come indicazioni di priorità, non come misure di campo." (P2 p. 50; indici-definizioni.json)
- Cautela sulle Figure 2-4 di P2: "Le classi delle figure originali non coincidono sempre con i dossier comunali. I grafici del sito usano i dossier." (sintesi-regionale.json, note)
- Anno di riferimento popolazione: "2025 = residenti al 1° gennaio 2025; 2023 = 31 dicembre; 2001 e 2011 = censimenti." (README-demografia.md)
- Pagine PDF: "I numeri di pagina rimandano alla pagina fisica del PDF, non alla numerazione stampata."
