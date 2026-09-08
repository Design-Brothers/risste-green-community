# direttrici-innovazione.json

Le 9 righe della Tabella 1 (pag. 40) – direttrici di innovazione emerse dal Technology Scouting – arricchite con la maturità tecnologica (par. 3.3.3 e 4.3) e il collegamento agli ambiti della Figura 6.

## Campi (`dati[]`)

| campo | tipo | unità | significato |
|---|---|---|---|
| `id` | int | – | ordine di riga nella Tabella 1 |
| `direttrice` | string | – | "Ambito strategico" (testo originale) |
| `driver_europeo` | string | – | "Driver europeo di riferimento" (testo originale) |
| `evidenze_emerse` | string | – | "Evidenze emerse" (testo originale) = esempi/applicazioni |
| `opportunita_sardegna` | string | – | "Opportunità per la Sardegna" (testo originale) = rilevanza per la Sardegna |
| `descrizione` | string | – | sintesi redazionale dal par. 4.3 / 3.3.2 con pagina citata |
| `maturita` | string o `null` | – | indicazione qualitativa di TRL dalle pagg. 32-33 e 38; `null` se il documento non si esprime |
| `n_pubblicazioni_fig6` | int o `null` | pubblicazioni | conteggio dell'ambito corrispondente in Figura 6 (o somma di due ambiti, vedi `nota`) |
| `pct_fig6` | float o `null` | % su 153 | percentuale della Figura 6 (null quando la direttrice somma due ambiti) |
| `nota` | string (opz.) | – | avvertenze sulla corrispondenza |
| `pagina_pdf` | int | – | 40 |

## Fonte

Parte 2, Tabella 1 pag. 40 (`tables/p040-t0.csv`, qualità "ok"); par. 4.3 pagg. 37-38; par. 3.3.2-3.3.3 pagg. 30-33; Figura 6 pag. 32.

## Avvertenze

- Solo `direttrice`, `driver_europeo`, `evidenze_emerse`, `opportunita_sardegna` sono testo della tabella; `descrizione` e `maturita` sono sintesi con pagina.
- La corrispondenza con la Figura 6 non è biunivoca: "Edilizia sostenibile" nella figura è separata da "Isolamento termo-acustico"; "Energia e tecnologie ambientali" e "Automotive e aerospaziale" sommano due ambiti ciascuna.
- Le direttrici 8 e 9 sono trasversali (nessun conteggio).

## Idee di rappresentazione

- Griglia di 9 card: direttrice, badge driver europeo, barra con `n_pubblicazioni_fig6`, semaforo maturità (elevata / intermedia / iniziale / n.d.).
- Matrice "maturità × numero di pubblicazioni" per posizionare le direttrici (quadranti: pronte al trasferimento vs. emergenti).
- Filtro incrociato con `bibliografia-scientifica.json` tramite parole chiave del settore applicativo.
