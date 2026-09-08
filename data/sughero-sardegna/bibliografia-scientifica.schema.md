# bibliografia-scientifica.json / .csv

Database bibliografico completo dell'Allegato II (pagg. 142-194): le pubblicazioni del Technology Scouting sul sughero con classificazione per Paese, settore, materiale, innovazione, TRL, potenziale industriale, potenziale per la Sardegna, valutazione scientifica e priorità.

**Record: 153** (contati dai CSV grezzi `tables/p142-t0.csv` … `p194-t0.csv`, dopo aver ricomposto 17 record spezzati su due pagine e scartato la riga di intestazione). Generati con `parse_bibliografia.py` (stessa cartella; rieseguibile da root repo).

## Campi (`dati[]` nel JSON; stesse colonne nel CSV, liste unite con ` | `, booleani `true/false`, null = vuoto)

| campo | tipo | unità | significato | origine |
|---|---|---|---|---|
| `id` | int | – | progressivo 1-153 nell'ordine del documento (ordinato per anno decrescente, poi alfabetico) | derivato |
| `riferimento` | string | – | riferimento bibliografico completo (col. 1), ricomposto e ripulito | fonte |
| `anno` | int o null | anno | primo anno 20xx trovato nel riferimento | derivato |
| `anno_inferito` | bool | – | true per i 2 record senza anno leggibile (id 125 'Blanc, S.018' → 2018; id 133 Aroso → 2017) ricostruiti dalla posizione cronologica | derivato |
| `autore_primo` | string | – | cognome del primo autore (solo cognome, senza iniziali) | derivato |
| `titolo` | string o null | – | titolo estratto con euristica (testo tra anno e primo punto seguito da maiuscola, o tra virgolette); null dove non separabile (7 record: riferimenti con anno in coda o testo frammentato) | derivato, best effort |
| `doi` | string o null | – | DOI normalizzato (col. 2): spazi rimossi, prefisso doi.org eliminato, `_N` finale ricomposto, `%2F`→`/`; null se 'ND' o cella vuota (28 record) | fonte |
| `paese` | string | – | col. 3 come nel documento (con separatore ' / ' per studi bi-nazionali; 'Multipaese', 'ND', 'Area mediterranea') | fonte |
| `paesi` | list[string] | – | `paese` spezzato su '/', con normalizzazione minima (Brazil→Brasile, Poland→Polonia, UK→Regno Unito) | derivato |
| `settore_applicativo` | string | – | col. 4, testo originale ricomposto (79 valori distinti, non normalizzati) | fonte |
| `materiale` | string o null | – | col. 5 tipologia di sughero/materiale; null nei record `inferenza` | fonte |
| `livello_innovazione` | string | – | col. 6: Medio, Alto, Medio-Alto, Molto alto, Medio-basso | fonte |
| `trl` | string o null | – | col. 7 testo originale ('TRL 2–4', '3–4 (stimato)', 'ND/Non tecnologico', 'NA', …) | fonte |
| `trl_min`, `trl_max` | int o null | TRL | estremi numerici della fascia; null se non quantificato | derivato |
| `trl_stimato` | bool | – | true se la fonte scrive '(stimato)' | derivato |
| `potenziale_industriale` | string o null | – | col. 9 (legenda: 8): Medio, Alto, Medio-Alto, Molto alto; null nei record `inferenza` | fonte |
| `potenziale_sardegna_stelle` | int (2-5) | stelle | numero di ★ nella col. 10 | derivato |
| `potenziale_sardegna_commento` | string o null | – | testo della col. 10 dopo le stelle; null se assente | fonte |
| `valutazione_scientifica` | int (3-5) o null | – | col. 11; null nei record `inferenza` (valore 'inferenza' non numerico) | fonte |
| `priorita` | string | – | col. 12: A, B, C | fonte |
| `inferenza` | bool | – | true per gli 11 record con struttura anomala nella fonte (colonne disallineate, marcati 'Inferenza'); per questi sono conservate le `celle_originali` (solo JSON) | derivato |
| `pagine_pdf` | list[int] | – | pagina/e PDF del record (due valori se spezzato) | fonte |
| `note` | list[string] | – | avvertenze per record (DOI ND, anno ricostruito, riga anomala, ricomposizione) | derivato |

Il JSON contiene anche `aggregati` (le distribuzioni qui sotto, ricalcolabili) e `note` di file.

## Pulizia applicata

- Interruzioni di riga dentro le celle ricomposte con dizionario esplicito (es. 'Cosmesi/Far maceutico/Bi oattivi' → 'Cosmesi/Farmaceutico/Bioattivi', 'Scarti/sototpro dotti' → 'Scarti/sottoprodotti', 'Medio- Alto' → 'Medio-Alto', '(stima to)' → '(stimato)').
- Refusi da legature tipografiche dell'estrazione PDF corretti (tt/ff/fl: 'distretot'→'distretto', 'rispetot'→'rispetto', 'tratatmento'→'trattamento', 'Efefct'→'Effect', 'Senf,f'→'Senff,', 'Sufof'→'Suffo', …).
- Trattini di fine riga ('Governance- Centred' → 'Governance-Centred'), numeri di fascicolo spezzati ('17(1 2)' → '17(12)'), URL DOI spezzati nel testo.
- Non corretti: refusi d'autore o del documento originale (es. 'Accountin', 'Engenhairia', 'S.018', riferimento duplicato in id 61).
- Doppioni/quasi-doppioni presenti nella fonte e mantenuti (contano nei 153): id 130-131 (Sierra-Pérez 2018, identici), id 87 e 94 (Barrigón Morillas 2021, stesso DOI), id 115 e 122 (do Rosário / Rosário 2019, stessa tesi), id 15-16-17 (Pino 2025, tre varianti dello stesso lavoro; id 15 condivide il DOI con id 66 Suffo 2023), id 61 (Pereira 2023: riferimento duplicato dentro la stessa cella).
- Verifica a campione: 10 record (id 8, 17, 31, 47, 63, 69, 88, 100, 125, 136) confrontati campo per campo con il Markdown dell'Allegato II: nessuna differenza oltre alla pulizia descritta.

## Distribuzioni calcolate dal dataset (153 record)

### Per anno
| anno | n |
|---|---|
| 2015 | 7 |
| 2016 | 3 |
| 2017 | 10 |
| 2018 | 8 |
| 2019 | 12 |
| 2020 | 14 |
| 2021 | 14 |
| 2022 | 16 |
| 2023 | 20 |
| 2024 | 23 |
| 2025 | 23 |
| 2026 | 3 |

Nota: 3 record datati 2026 sono fuori dal periodo dichiarato 2015-2025 (la Figura 1 indica 2015-2026).

### Per Paese – confronto con la Figura 5 (pag. 31)
| Paese | Figura 5 | DB: stringa esatta | DB: primo Paese elencato | DB: qualsiasi menzione |
|---|---|---|---|---|
| Portogallo | 58 | 58 | 64 | 67 |
| Spagna | 23 | 21 | 23 | 29 |
| Italia | 11 | 11 | 16 | 16 |
| Studi multipaese | 20 | 17 | 17 | 17 |
| Francia | 8 | 7 | 7 | 7 |
| Polonia | 6 | 1 | 6 | 6 |
| Danimarca | 2 | 3 | 3 | 4 |
| Algeria | 2 | 2 | 2 | 3 |
| Marocco | 1 | 1 | 1 | 1 |
| Altri Paesi | 22 | – | 14 (residuo) | – |
| **Totale** | **153** | 153 | 153 | 172 (menzioni) |

La Figura 5 (totale 153) coincide con il database per Portogallo (58 con stringa esatta), Spagna (23 = primo Paese elencato), Italia (11 stringa esatta), Algeria (2) e Marocco (1); non coincide per Studi multipaese (20 vs 17), Francia (8 vs 7), Polonia (6 solo contando il primo Paese elencato), Danimarca (2 vs 3). Il criterio con cui la figura attribuisce gli studi bi-nazionali non è dichiarato. 'Altri Paesi' = 22 nella figura; nel database i Paesi con 1-3 record (Germania, Austria, Svizzera/Cina, Brasile, India, Cina, Turchia, Repubblica Ceca, Regno Unito, Finlandia, Svezia, Area mediterranea, ND, …) sommano a 14 contando il primo Paese elencato (22 nella figura): la differenza dipende dal criterio di attribuzione degli studi bi-nazionali e multipaese, non dichiarato.

### Per ambito – confronto con la Figura 6 (pag. 32)
| Ambito (Figura 6) | Figura 6 n | Figura 6 % | DB: parole chiave nel settore applicativo |
|---|---|---|---|
| Materiali compositi e innovativi | 66 | 43.1 | 81 |
| Edilizia sostenibile | 29 | 19.0 | 31 |
| Biomedicale, cosmetico e bioattivi | 23 | 15.0 | 6 |
| Economia circolare e valorizzazione degli scarti | 22 | 14.4 | 24 |
| Isolamento termo-acustico | 14 | 9.2 | 20 |
| Design e arredo | 9 | 5.9 | 9 |
| Energia | 7 | 4.6 | 7 |
| Packaging enologico | 6 | 3.9 | 6 |
| Automotive | 6 | 3.9 | 6 |
| Aerospaziale | 6 | 3.9 | 6 |
| Trattamento delle acque | 5 | 3.3 | 5 |
| Manifattura additiva | 4 | 2.6 | 4 |
| **Somma** | **197** | 128,8 | 205 (+9 record senza corrispondenza: ND, agricoltura/biomassa, governance/mercato) |

La colonna "DB" è una **mappatura euristica per parole chiave** del campo `settore_applicativo` (79 valori liberi) sui 12 ambiti della figura, con attribuzione multipla: è indicativa e non riproduce la classificazione degli autori. Coincidono Design (9), Energia (7), Packaging (6), Automotive (6), Aerospaziale (6), Trattamento acque (5), Manifattura additiva (4); i macro-ambiti (compositi, edilizia, isolamento, economia circolare, biomedicale) divergono perché dipendono dalle parole chiave scelte.

### Per settore applicativo (prime 15 stringhe originali)
| settore_applicativo (testo originale) | n |
|---|---|
| Materiali/Innovazione | 14 |
| Edilizia / isolamento | 9 |
| Compositi | 9 |
| Compositi strutturali / protezione | 5 |
| Edilizia / Isolamento / Architettura | 5 |
| ND | 5 |
| Materiali compositi / Ingegneria | 5 |
| Compositi strutturali / trasporti | 5 |
| Cosmesi/Farmaceutico/Bioattivi | 4 |
| Edilizia/Materiali | 4 |
| Edilizia/isolamento | 3 |
| Rivestimenti funzionali / materiali avanzati | 3 |
| Materiali bio-based / review | 3 |
| Compositi / Automotive/Aerospazio/Protezione | 3 |
| Economia circolare/Governance | 3 |

### Per livello di innovazione
| livello_innovazione | n |
|---|---|
| Medio | 92 |
| Alto | 36 |
| Medio-Alto | 16 |
| Molto alto | 8 |
| Medio-basso | 1 |

### Per TRL (fascia `trl_min–trl_max`)
| fascia TRL | n |
|---|---|
| 3–5 | 38 |
| 2–4 | 36 |
| 3–4 | 31 |
| non quantificato (ND/NA/non tecnologico/review) | 17 |
| 4–6 | 16 |
| 6–8 | 9 |
| 5–7 | 5 |
| 2–3 | 1 |

Il documento (pag. 32-33) descrive TRL 3–6 come prevalenti, con "un numero significativo" di applicazioni TRL 7–9 e "una componente rilevante" TRL 1–3, senza conteggi. Nel database la fascia più alta è 6–8 (9 record); nessun record raggiunge TRL 9; il grosso (105 record) è tra 2 e 5.

### Per potenziale industriale
| potenziale_industriale | n |
|---|---|
| Medio | 72 |
| Alto | 54 |
| Medio-Alto | 15 |
| (null) | 11 |
| Molto alto | 1 |

### Per potenziale per la Sardegna (stelle)
| stelle ★ | n |
|---|---|
| 2 | 3 |
| 3 | 82 |
| 4 | 52 |
| 5 | 16 |

### Per valutazione scientifica
| valutazione_scientifica | n |
|---|---|
| (null) | 11 |
| 3 | 61 |
| 4 | 80 |
| 5 | 1 |

### Per priorità
| priorita | n |
|---|---|
| B | 79 |
| A | 68 |
| C | 6 |

(Gli 11 record `inferenza` hanno priorità 'A' nella cella corrispondente, ma la loro attendibilità è dichiarata come inferita dalla fonte stessa.)

## Discrepanza 153 vs 166

- Il par. 3.3 (pag. 29) e la didascalia della Figura 6 (pag. 32) parlano di **166** pubblicazioni.
- Il par. 3.3.2 (pag. 30), la Figura 5 e la Figura 6 (totali) parlano di **153**.
- L'Allegato II contiene **153 record** (conteggio effettivo di questo dataset, doppioni inclusi; 148 pubblicazioni distinte se si escludono i 5 doppioni evidenti).
- Interpretazione più plausibile (non esplicitata nel documento): 166 = pubblicazioni individuate prima della validazione, 153 = pubblicazioni selezionate. Nel sito usare 153 e segnalare 166 in nota.

## Fonte

Parte 2, Allegato II pagg. 142-194 (legenda a pag. 142; le colonne della tabella sono numerate 1-2-3-4-5-6-7-9-10-11-12, la legenda numera il potenziale industriale come 8). CSV grezzi: `source/parte2-filiera-sughero-sardegna/tables/p142-t0.csv` … `p194-t0.csv` (manifest: qualità "ok", p148 "sparse").

## Avvertenze

- `titolo`, `autore_primo`, `anno` sono derivati con euristiche: usarli per filtri/ordinamenti, non come citazione ufficiale (usare `riferimento`).
- I valori categoriali (`settore_applicativo`, `materiale`, `paese`) sono testo libero degli autori: per filtri sul sito conviene una tassonomia ridotta (vedi mappatura euristica sopra) dichiarata come tale.
- 11 record `inferenza` hanno materiale, potenziale industriale e valutazione a null.
- 'ND' e 'NA' sono mantenuti come stringhe (categorie usate dalla fonte), non convertiti in null, salvo per il DOI.

## Idee di rappresentazione

- Tabella esplorabile (153 righe) con filtri per Paese, priorità (A/B/C), stelle Sardegna, fascia TRL, anno; ricerca full-text su riferimento.
- Scatter "TRL (min-max) × stelle potenziale Sardegna" colorato per priorità, per individuare le pubblicazioni pronte al trasferimento (id con 5 stelle e priorità A).
- Istogramma per anno 2015-2026 + mappa per Paese (con avviso sul criterio di attribuzione degli studi bi-nazionali).
