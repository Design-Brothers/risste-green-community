# End-off — Revisione sito Sughero Sardegna

**Progetto:** Progetto di ricerca e sviluppo, valorizzazione del sughero sardo e innovazione tecnologica  
**CUP:** E77G24000450002  
**Soggetto attuatore:** Centro Studi R.I.S.S.T.E. APS  
**Branch:** `revisione-sughero-sardegna`  
**Live:** https://risste-sughero-sardegna.vercel.app  
**Alias precedente:** https://risste-green-community.vercel.app  

Questo documento confronta le indicazioni di revisione con quanto è stato implementato, segnala i residui e raccoglie le domande da rivolgere al committente.

---

## 1. Obiettivo generale

| Richiesta | Stato | Note |
|---|---|---|
| Cornice regionale, non più Green Community / Unione dei Comuni | Fatto | Gallura resta come focus territoriale e caso di studio |
| Soggetto attuatore Centro Studi R.I.S.S.T.E. APS | Fatto | Home, progetto, footer, metadati |
| CUP in evidenza | Fatto | Hero, footer, SEO |

## 2. Denominazione e indirizzo

| Richiesta | Stato | Note |
|---|---|---|
| «Green Community Alta Gallura» → «Sughero Sardegna» / titolo istituzionale | Fatto | Titoli, menu, footer, SEO, OG |
| Dominio `risste-sughero-sardegna.vercel.app` | Fatto | L’URL precedente resta attivo |

## 3. Sostituzioni globali

| Espressione da eliminare | Stato |
|---|---|
| Green Community Alta Gallura | Fatto nelle pagine |
| Green Community UCAG 193 | Fatto nelle pagine |
| UCAG 193 | Fatto nelle pagine |
| Unione dei Comuni come committente del progetto | Fatto |
| Due studi, un territorio | Fatto |
| Studio di fattibilità (come titolo del progetto) | Fatto |
| Programma dell’Unione | Fatto |

Residuo: alcuni file di archivio in `data/` e qualche nome file storico (`framework-green-community`) restano come fonte. Non compaiono nel menu né nei titoli pubblici.

## 4. Menu principale

Richiesta originale: 8 voci. In seguito: troppe voci, alcune a tendina, pulsante censimento nel footer.

**Menu attuale (4 voci):**

1. Home  
2. Il progetto ▾ — Il progetto · Ricerca e mercato · Documenti  
3. Atlante ▾ — Atlante del sughero · Database · Focus Gallura  
4. Innovazione  

| Richiesta | Stato |
|---|---|
| Home, Il progetto, Ricerca e mercato, Atlante, Innovazione, Focus Gallura, Database, Documenti | Fatto, raggruppate |
| Alta Gallura non è più direttrice principale | Fatto (Focus Gallura sotto Atlante) |
| Pulsante «Partecipa al censimento» nel footer | Fatto |

## 5. Home

| Richiesta | Stato |
|---|---|
| Titolo browser regionale | Fatto |
| Eliminare UCAG, Unione, 11 comuni come identità del progetto, Green Community, «Due studi…» | Fatto |
| Titolo SUGHERO SARDEGNA + sottotitolo + CUP | Fatto |
| Nuovo testo introduttivo regionale | Fatto |
| «Il progetto in 60 parole» | Fatto |
| Blocchi WP1–WP4 | Fatto |
| Tre porte: Atlante / Innovazione e certificazioni / Focus Gallura | Fatto |
| Chi siamo con titolo regionale e CUP | Fatto |

## 6. Il progetto e i documenti

| Richiesta | Stato |
|---|---|
| Nuovo titolo pagina | Fatto |
| Banner regionale, no PNRR/221 come fondamento | Fatto |
| Testo descrittivo, obiettivi, metodo in 10 punti | Fatto |
| Studio 1 e Studio 2 ridenominati | Fatto (titoli sito + copertina/premessa PDF) |
| Dataset 36 JSON/CSV scaricabili | Fatto (`/documenti`, `/dati/catalogo.json`) |

Nota PDF: alle copie scaricabili è stata anteposta copertina e premessa istituzionali. La riscrittura invalida eventuali firme digitali originali; il contenuto scientifico resta quello validato.

## 7. Focus Gallura (ex Alta Gallura)

| Richiesta | Stato |
|---|---|
| Nuovo titolo e banner | Fatto |
| Introduzione come approfondimento regionale | Fatto |
| Dati demografici, imprese, 11 schede, GIS, scenari | Conservati |
| Maggiore evidenza Calangianus–Tempio e filiera | Fatto |
| Demografia in chiave di competenze e ricambio | Fatto |

## 8. Atlante del sughero

| Richiesta | Stato |
|---|---|
| Titolo browser e visibile | Fatto |
| 30 comuni, 83.790,90 ha, IVP, incendio, ICR, filtri, schede | Conservati |
| Mappa interattiva Sardegna | Fatto — fondo **OpenStreetMap** (nessuna chiave) |
| Nome del comune al passaggio del mouse | Fatto (tooltip sulla mappa) |
| Card cliccabili dei comuni, oltre alla mappa | Fatto (griglia sotto la mappa; l’esploratore a barre resta) |

## 9. Innovazione

| Richiesta | Stato |
|---|---|
| Nuovo titolo e introduzione | Fatto |
| 153 pubblicazioni, ambiti, TRL, S.U.G.H.E.R.A., FSC/PEFC/ISO | Conservati |
| Uniformare 153 (non 166) e 21 comuni IVP alta | Fatto, con nota metodologica |

## 10. Ricerca e mercato (nuova)

| Richiesta | Stato |
|---|---|
| Pagina WP2 con filiera, imprese, prodotti, criticità, opportunità | Fatto |
| Dati aggregati, senza identificativi aziendali | Fatto |

## 11. Database (nuova)

| Richiesta | Stato |
|---|---|
| Hub: mappa, 30 comuni, 11 Gallura, bibliografia, dataset, mercato, form | Fatto |
| Pulsante censimento | Nel footer di tutte le pagine + form in pagina |
| Campi richiesti e consenso | Fatto |
| Niente pubblicazione automatica | Fatto (validazione / fallback PEC) |

## 12. Footer

| Richiesta | Stato |
|---|---|
| RISSTE APS + titolo regionale + CUP | Fatto |
| Finanziamento RAS – Assessorato Agricoltura | Fatto |
| Loghi istituzionali | Presenti come lockup testuali, non come stemmi ufficiali |
| Canali social | PEC + collegamenti di ricerca; mancano URL ufficiali del progetto |

## 13. Cosa non è stato disperso

Dati, grafici, 11+30 schede, IVP/IPI/ICR, GIS, bibliografia, Technology Scouting, certificazioni, S.U.G.H.E.R.A., PDF, filtri, approfondimento Gallura: conservati.

## 14. Verifiche richieste (checklist originale)

1. Assenza «Green Community UCAG 193» — ok  
2. Progetto non presentato come iniziativa dell’Unione — ok  
3. Titolo regionale completo — ok  
4. CUP in tutte le pagine — ok  
5. RISSTE soggetto attuatore — ok  
6. Finanziamento regionale — ok  
7. Centralità regionale — ok  
8. Gallura solo come focus — ok  
9. PDF funzionanti — ok  
10. Filtri — ok  
11. Mappa geografica — ok (OSM + nome in hover + card)  
12. Database bibliografico — ok  
13. Download dataset — ok  
14. Modulo aziende — ok (webhook opzionale non ancora configurato)  
15. Canali social — parziale (mancano URL ufficiali)  
16. Uniformità 153 / 21 — ok  
17. SEO e metadati — ok  
18. Computer / tablet / smartphone — menu compatto; da rivedere dopo il restyling a 4 voci  

---

## Domande e richieste per il committente

1. **Loghi ufficiali.** Possiamo usare gli stemmi della Regione e dell’Assessorato (file e linee guida grafiche)? Oggi in footer ci sono lockup testuali.  
2. **Social del progetto.** Quali sono gli URL ufficiali (Facebook, Instagram, LinkedIn, sito RAS)? Oggi i link sono di ricerca, non di profilo.  
3. **Destinatario del censimento.** Chi deve ricevere le segnalazioni delle aziende? Serve un indirizzo dedicato, un foglio condiviso o un gestionale? Il webhook `CENSIMENTO_WEBHOOK_URL` è pronto ma non è ancora collegato.  
4. **Informativa privacy del modulo.** Va pubblicata una informativa breve e un responsabile del trattamento, oltre al checkbox di consenso?  
5. **Indirizzo pubblico.** Teniamo entrambi gli URL o reindirizziamo `risste-green-community.vercel.app` sul nuovo dominio? Serve un dominio proprio (es. `sugherosardegna.it`)?  
6. **PDF firmati.** Confermate che va bene la copertina istituzionale anteposta (le firme digitali originali non restano valide sul file nuovo)?  
7. **Dati di mercato.** Restiamo sui risultati aggregati o, in una seconda fase, si possono pubblicare elenchi di imprese (con quali consensi)?  
8. **Canali istituzionali RAS.** Va aggiunto un riferimento o un logo del bando / misura di finanziamento oltre alla formula già in footer?

---

*Documento interno di consegna, settembre 2026.*
