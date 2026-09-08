# Dataset demografici ed economici – Unione dei Comuni Alta Gallura

Fonte: RISSTE, *Green community UCAG 193 – Strategie territoriali integrate* (2025), Parte 1 – Demografia (pag. PDF 21-32) e Allegato I – Report demografico dei Comuni (pag. 96-148). Regole in `data/CONVENZIONI.md`. Ogni JSON ha `titolo`, `fonte`, `note`, `dati` e un `.schema.md` gemello.

## File prodotti

| File | Record | Descrizione |
|---|---|---|
| `popolazione-storica.json` / `.csv` | 14 | Abitanti 2001/2011/2023/2025, variazioni, `fascia` costiera/interna; 11 comuni + totale + 2 fasce |
| `saldi-demografici.json` / `.csv` | 14 | Saldo naturale e migratorio cumulati 2002-2023, saldo estero (solo Aggius), incidenza prevalente; 11 comuni + costa + interno + Unione |
| `struttura-eta.json` / `.csv` | 45 | Classi 0-14 / 15-64 / 65+ al 1° gennaio 2002, 2011, 2023, 2025 con indici solo se citati nel testo; + Unione 2025 |
| `famiglie.json` | 12 | Famiglie e componenti medi 2003/2011/2023/2024 per comune + Unione |
| `stranieri-e-scuola.json` | 12 | Stranieri 2025, incidenza, provenienza; utenza 0-18 per ciclo e per età |
| `imprese.json` / `imprese.csv` / `imprese-macro-settori.csv` | 14 + 7 | Imprese 2021/2025 e settori per comune, aggregati per fascia, Tabella 1d per macro-settore |
| `scenari-2035.json` | 3 + 11 | Tre scenari Unione (popolazione e imprese) e stime comunali |
| `confronto-costa-entroterra.json` | 11 + 4 | Tabella 1c integrata con par. 1.10 e sintesi delle dinamiche 1.7.1-1.7.4 |
| `kpi-sintesi.json` | 16 | Numeri da titolo per la landing page |

## Avvertenze generali

- Riferimenti temporali: 2001 e 2011 = censimenti; 2023 = 31 dicembre; 2025 = 1° gennaio 2025 (nelle schede detto "2024"). Le tabelle per età usano il 1° gennaio, quindi i totali 2011 e 2023 differiscono dalla Tabella 1a.
- Nessun valore stimato: dove il documento non riporta il dato il campo è `null` e la nota spiega l'eventuale valore implicito.

## Dati mancanti nella fonte

- Viddalba: saldi naturale e migratorio 2002-2023 assenti dalla scheda (impliciti -218 / +276 per differenza dai totali).
- Viddalba: imprese 2021 non scritte (implicito 322).
- Saldo migratorio con l'estero riportato solo per Aggius.
- Aglientu: numero famiglie 2024 non riportato; Aggius: solo componenti medi 2024.
- Imprese 2023 solo a livello di Unione; densità imprenditoriale solo Unione; settori comunali citati parzialmente (3-5 su 6).
- L'Allegato I non contiene dati sulle imprese.

## Incoerenze rilevate nella fonte

1. **Calangianus, utenza 0-18**: tabella 476 (cicli coerenti) contro 466 nel testo (scheda, par. 1.5, par. 1.7.4); il totale Unione 4.295 richiede 466.
2. **Utenza 0-18 per fascia**: Tabella 1c 1.177 costa / 3.118 interno; somma delle schede 1.167 / 3.128.
3. **Coorti scolastiche**: Santa Teresa primaria 166 vs coorti 164; Bortigiadas secondaria II 22 vs coorti 26.
4. **Componenti medi Badesi/Trinità** (par. 1.7.3): "1,76 e 1,97" invertiti rispetto alle schede (Badesi 1,97; Trinità 1,76).
5. **Indice di vecchiaia massimo**: par. 1.4 cita Bortigiadas 342 e Aggius/Aglientu 333, ma Trinità d'Agultu ha 368,3.
6. **Indici per fascia (Tab. 1c)**: IV 316,5 / 291,6 e ID 58,1 non riproducibili dai dati comunali; ID costa 59,9 = media semplice.
7. **Scenari 2035**: la somma delle stime comunali (35.197 / 33.473 / 32.086) non coincide con gli scenari Unione (36.500 / 34.100 / 32.400); alcune stime comunali non seguono il modello dichiarato.
8. **Totali 1° gennaio vs Tabella 1a**: es. Tempio 14.290 vs 13.936 (2011), Trinità 2.239 vs 2.351 (2023).
9. **Refusi**: "l'interno ha perso quasi 3.000 abitanti" (in realtà 2.760); Aggius "indice di dipendenza salito da 52,5 a 52,1"; "picchi superiori al 35% in età 1 e 2 anni a Tempio" (37,0% e 34,4%).
10. **Estrazione PDF**: tabella saldi di Santa Teresa frammentata (pag. 128-129) e righe 2025 di Badesi/Luogosanto spezzate: valori ricomposti dal testo.

## Verifiche eseguite

Somme comunali = totali Tabella 1a (tutti gli anni); saldi per fascia = Tabella 1b (con Viddalba implicito); classi di età 2025 = par. 1.4 (3.247 / 22.204 / 9.791, IV 301,54, ID 58,72); famiglie 2003/2023 = par. 1.3; stranieri = 2.151 e 1.213 / 938; imprese 2025 = 4.792 e costa 1.561; Tabella 1d somme e quote; indici comunali 2025 e quote settoriali riproducibili dalle classi/valori.
