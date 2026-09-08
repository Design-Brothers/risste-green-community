# framework-sughera.json

Il framework S.U.G.H.E.R.A. (par. 4.5, Figura 7): acronimo nelle due versioni, i 7 step della figura con input/output, il modello integrato e le strategie territoriali differenziate per profilo, più i profili integrati assegnati ai 30 comuni nell'Allegato I.

## Struttura (`dati` è un oggetto)

| campo | tipo | significato |
|---|---|---|
| `acronimo.sigla` | string | "S.U.G.H.E.R.A." |
| `acronimo.espansione_inglese` | string | Strategic Unified Governance, Habitat Evaluation and Regional Assessment (pagg. 42, 43, 45) |
| `acronimo.espansione_italiana` | string | Sistema Unificato di Gestione, Habitat, Ecosistemi, Resilienza e Analisi (Lista abbreviazioni, pag. 9) |
| `acronimo.sottotitolo_figura` / `definizione` | string | sottotitolo della Figura 7 / definizione di pag. 42 |
| `step[]` | list | 7 step (1, 2, 3, 4A, 4B, 5, 6, 7) |
| `step[].n` | string | numero come in figura ("4A" e "4B" sono paralleli) |
| `step[].nome`, `sottotitolo`, `descrizione` | string / null | testi della Figura 7 |
| `step[].input`, `step[].output` | string / null | **ricostruiti** dal flusso della figura e dal testo (non etichette della fonte) |
| `step[].contenuti` | list[string] o list[object] | voci elencate nel blocco della figura; per lo step 5 `{strategia, descrizione}`, per lo step 6 `{dimensione, descrizione}` |
| `legenda_figura` | list[string] | le 5 tipologie di freccia della figura |
| `modello_integrato.*` | object | elementi del par. 4.5 (pagg. 42-44) e della struttura modulare (pag. 45): elemento distintivo, fattori di competitività, organizzazione reticolare, polo Alta Gallura, coerenza con politiche UE, evoluzione in DSS |
| `strategie_territoriali_per_profilo.profili[]` | list | profili descritti a pag. 42: `profilo`, `indicatori` (traduzione redazionale alta/bassa di IVP/ICR/IPI), `strategia` (azioni citate), `strategia_figura_7` (associazione redazionale a Produzione/Conservazione/Sperimentazione/Valorizzazione) |
| `profili_integrati_allegato_1.valori[]` | {profilo, n_comuni} | etichette di profilo integrato delle schede comunali (Allegato I) con numero di comuni; somma = 30 |

## Fonte

Parte 2: par. 4.5 pagg. 41-44; Figura 7 pag. 43 (`images/fig-7-framework-sughera.jpeg`); Lista abbreviazioni pag. 9 (`tables/p009-t0.csv`); Conclusioni pag. 45; Allegato I pagg. 49-141 (frase "Il profilo integrato assegnato è: …" nelle 30 schede).

## Avvertenze

- `input`/`output` degli step e le associazioni `strategia_figura_7` / `indicatori` sono interpretazioni redazionali della figura e del testo, segnalate come tali.
- Il documento non assegna esplicitamente ciascun comune a una delle quattro strategie della Figura 7; l'unico collegamento comunale è l'etichetta di profilo integrato dell'Allegato I.
- Il numero della figura nel Markdown estratto (Figura 10) non coincide con il richiamo nel testo (Figura 7).

## Idee di rappresentazione

- Diagramma di flusso verticale interattivo che replica la Figura 7 (step cliccabili → contenuti, input/output).
- Selettore "strategia" (Produzione / Conservazione / Sperimentazione / Valorizzazione) che evidenzia i profili e, tramite l'Allegato I, i comuni con profilo compatibile.
- Card dell'acronimo con doppia espansione (EN/IT) e riquadro "verso il DSS" con le 5 componenti.
