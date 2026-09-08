# Dataset "innovazione, technology scouting, certificazioni e bibliografia" – Parte 2 (filiera del sughero in Sardegna)

Dati curati dallo studio RISSTE *Valorizzazione della filiera del sughero in Sardegna – Un framework multidisciplinare* (Parte 2), estratti da `source/parte2-filiera-sughero-sardegna/` secondo `data/CONVENZIONI.md`. Ogni file JSON ha `titolo`, `fonte` (documento, capitolo, pagine PDF), `note` e `dati`; ogni dataset ha il suo `*.schema.md` con campi, fonte, avvertenze e idee di rappresentazione.

| file | contenuto | fonte (pagg. PDF) | dimensione |
|---|---|---|---|
| `contesto-sughero-sardegna.json` | numeri e riferimenti di contesto regionale (90% delle sugherete italiane, 83.790,90 ha nei 30 comuni, 7 comuni con maggiore estensione, comprensori, distretto Alta Gallura, proprietà e settori del sughero); indicatori assenti nel documento a `null` | 15-18, 20, 27 | 18 indicatori |
| `technology-scouting.json` | metodologia del Technology Scouting; `per_paese` (Figura 5); `per_ambito` (Figura 6); `per_trl_documento` (qualitativo) e `per_trl_database` (calcolato); 6 evidenze testuali | 21-24, 29-33, 38 | 10 Paesi, 12 ambiti |
| `direttrici-innovazione.json` | Tabella 1: 9 direttrici con driver europeo, evidenze, opportunità per la Sardegna, maturità e collegamento alla Figura 6 | 40 (+30-33, 37-38) | 9 righe |
| `strumenti-certificazione.json` | Tabella 2: 11 strumenti (FSC, PEFC, PEFC Agroforestale, ISO 9001, ISO 14001, EMAS, BRCGS, IFS PACsecure, SYSTECODE, Carbon Footprint, LCA) + 3 citati nel testo; tipo, cosa certifica, contributo; criticità e raccomandazioni | 41 (+22-23, 26, 34, 38-39, 45) | 14 strumenti |
| `framework-sughera.json` | acronimo S.U.G.H.E.R.A. (EN e IT), 7 step della Figura 7 con input/output, modello integrato del par. 4.5, strategie territoriali per profilo, profili integrati dei 30 comuni (Allegato I) | 9, 41-45 (+49-141) | 7 step, 5 profili |
| `conclusioni.json` | 10 messaggi chiave testuali della Quinta parte + 7 raccomandazioni + prospettiva finale | 45-46 (+33, 34, 41-44) | 10 + 7 |
| `bibliografia-scientifica.json` / `.csv` | database completo dell'Allegato II: **153 record**, 24 campi (riferimento, anno, primo autore, titolo, DOI, Paese, settore, materiale, innovazione, TRL, potenziale industriale, stelle e commento per la Sardegna, valutazione, priorità, pagine, note) + aggregati | 142-194 | 153 record |
| `parse_bibliografia.py` | script Python che rigenera JSON e CSV bibliografici dai CSV grezzi (`python3 data/sughero-sardegna/parse_bibliografia.py` dalla root) | – | – |

## Avvertenze principali

1. **153 vs 166 pubblicazioni.** Il testo (pag. 29) e la didascalia della Figura 6 dicono 166; il par. 3.3.2, la Figura 5, la Figura 6 (totali) e l'Allegato II dicono 153. Il dataset conta 153 record (doppioni inclusi: id 130-131 identici, 87/94, 115/122, 15-16-17 varianti). Usare 153.
2. **Figura 6 con attribuzione multipla**: i 12 ambiti sommano a 197 (128,8%) su 153; le percentuali della didascalia (34,9 / 19,3 / 12,7) non sono coerenti con la figura né con base 166.
3. **Figura 5**: la didascalia dice 67,5% per Portogallo+Spagna+Italia; dai numeri della figura risulta 60,1%. Le distribuzioni per Paese calcolate dal database coincidono con la figura solo per alcuni Paesi (il criterio per gli studi bi-nazionali non è dichiarato).
4. **TRL**: il documento è qualitativo (TRL 3–6 prevalenti; "numero significativo" a 7–9); nel database nessun record supera TRL 8.
5. **Periodo**: testo 2015-2025, Figura 1 2015-2026; 3 record datati 2026.
6. **Dati di contesto assenti**: produzione, imprese, addetti, export e quota mondiale non sono nella Parte 2 (indicatori a `null` con nota). L'unico dato di quota è "circa il 90% delle superfici italiane a sughereta" (pag. 16, senza anno).
7. **Record anomali** nel database: 11 righe con struttura disallineata (marcate 'Inferenza' nella fonte) hanno materiale, potenziale industriale e valutazione a `null`, flag `inferenza = true` e celle originali conservate.
8. **Pulizia testuale**: interruzioni di riga e refusi di estrazione (legature tt/ff) ricomposti con dizionario esplicito; i refusi d'autore del documento non sono corretti. `titolo`, `autore_primo`, `anno` sono derivati con euristiche (best effort).
9. **Numerazione figure** nel Markdown estratto incoerente (Figura 8/9/10 per quelle richiamate nel testo come 5/6/7).
10. I campi `descrizione`, `maturita`, `tipo`, `input/output`, `tema`, `destinatari` sono sintesi/classificazioni redazionali dichiarate nelle note di ciascun file; il testo originale della fonte è sempre nei campi indicati come "testo originale" negli schema.

## Immagini di riferimento

`source/parte2-filiera-sughero-sardegna/images/`: `fig-1-workflow-analisi-integrata.jpeg` (pag. 26), `fig-5-distribuzione-geografica-innovazione.jpeg` (pag. 31), `fig-6-ambiti-innovazione-sughero.jpeg` (pag. 32), `fig-7-framework-sughera.jpeg` (pag. 43).
