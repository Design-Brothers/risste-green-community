# Dataset "Sughereta Sardegna" – 30 comuni e indici territoriali (Parte 2, Allegato I)

Dati curati dallo studio RISSTE *Valorizzazione della filiera del sughero in Sardegna – Un framework multidisciplinare* (2025), Parte 2. Fonte primaria: Allegato I "Studio tecnico sugherete – Dossier comunale integrato" (pag. PDF 50-141), integrato con par. 2.2, 3.1-3.2, 4.1-4.2 e Figure 2-4.

## File

| File | Contenuto |
|---|---|
| `comuni-sughereta.json` | 30 record (uno per comune): estensione, peso %, IVP, IPI, ICR con classi, indicatori di continuità, profili, distribuzione per unità pedologica e per classe di pericolosità incendio, indicazioni operative, sintesi esecutiva, confronto con le figure |
| `comuni-sughereta.csv` | Stessi 30 record, solo campi scalari (24 colonne) |
| `comuni-sughereta.schema.md` | Descrizione campo per campo, avvertenze, idee di rappresentazione |
| `indici-definizioni.json` + `.schema.md` | Definizione di IVP, IPI, ICR; classi, soglie dichiarate e intervalli osservati; legenda dei profili a 2 e 3 fattori; indicazioni operative ricorrenti; catalogo unità pedologiche |
| `sintesi-regionale.json` + `.schema.md` | Totali, conteggi per classe (dataset vs testo), top 5, estremi, profili più favorevoli/critici, registro delle incoerenze |
| `parse_comuni_sughereta.py` | Script di parsing e costruzione dei tre file dal Markdown/CSV in `source/` (riproducibile) |

## Come sono stati costruiti

1. Parsing sistematico dei 30 dossier (struttura identica: quadro sintetico, sintesi esecutiva, tabella pedologica, tabella incendio, tabella ICR, matrice integrata, indicazioni operative) dal Markdown `08-allegato1-studio-tecnico-sugherete.md`.
2. Controlli incrociati automatici su ogni comune: quadro sintetico vs sintesi esecutiva vs tabelle vs matrice vs quadro sinottico (pag. 50-51); somme delle tabelle vs totale comunale; ricalcolo di IVP e IPI ponderati, superficie media, densità e quota del complesso maggiore.
3. Verifica manuale sul PDF originale di 5 comuni (Nuoro, Orune, Olbia, Abbasanta, Iglesias) e delle pagine con tabelle spezzate (86, 95, 110, 139).
4. Trascrizione manuale delle Figure 2, 3, 4 e confronto con i dossier.

## Avvertenze principali

- **Fare fede ai dossier, non alle figure.** Le Figure 2-4 (pag. 28-30) riportano valori e classi diversi per la maggior parte dei comuni e sembrano derivare da una versione precedente dell'elaborazione (Fig. 2 include Oniferi, Dualchi, Noragugume; Fig. 4 ha Nuoro due volte e non ha Ardara). I valori delle figure sono conservati in `confronto_figure` a solo scopo documentale.
- **Soglie delle classi non esplicitate.** Il testo non fornisce soglie numeriche; le legende delle figure (IVP ≥ 3,50; ICR ≥ 70) non riproducono la classificazione dei dossier. Usare gli `intervalli_osservati` in `indici-definizioni.json`.
- **Conteggi del testo ≠ dossier**: IVP 22/4/4 (testo) vs 21/4/5 (dossier); ICR "8 comuni Alta" vs 9.
- **Bultei**: IVP dichiarato 3,395, ricalcolato dalla tabella 3,448 (unico caso su 30). Mantenuto il valore dichiarato.
- **Righe reintegrate dal PDF**: Telti, Chiaramonti, Pozzomaggiore (riga "Alto" della tabella incendio, persa nell'estrazione a cavallo di pagina).
- **Provincia** non deducibile dal documento (`null`). Per il join cartografico usare `nome_corrente`/`slug`.
- Le pagine indicate sono **pagine fisiche del PDF**; la numerazione stampata è inferiore di 17.

## Campi non ricavabili dalla fonte

`provincia`; soglie numeriche ufficiali delle classi IVP/IPI/ICR; un valore ICR numerico "0-100" distinto dalla quota del complesso maggiore (i dossier non lo riportano); profilo integrato per le combinazioni di classi non presenti tra i 30 comuni.
