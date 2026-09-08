# schede-comuni.json

Una scheda territoriale per ciascuno degli 11 Comuni dell'Unione Alta Gallura che integra: Tabella 2a (funzione territoriale e ruolo paesaggistico, pag. 37), quadro sinottico della Terza parte (pag. 53-68) e scheda comunale preliminare dell'Allegato II (pag. 156-171), con i giudizi della sintesi comparativa (pag. 172). `dati` è un array di 11 oggetti.

## Campi

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `slug` | string | – | Identificatore kebab-case |
| `comune` | string | – | Nome come nel documento (apostrofo semplice per Trinità d'Agultu e Vignola) |
| `fascia` | string | – | `costiera` (4 Comuni) / `interna` (7 Comuni), coerente con gli altri dataset |
| `posizione_parte3` | string | – | Collocazione secondo il quadro sinottico (pag. 53); Viddalba = "cerniera" |
| `tab_2a` | object | – | Riga della Tab. 2a: `ambito_territoriale`, `tipologia_territoriale`, `funzione_territoriale`, `elementi_paesaggistici_dominanti`, `ruolo_strategico`, `pagina_pdf` |
| `funzione_territoriale` | string | – | = `tab_2a.funzione_territoriale` (es. "Polo forestale e sughericolo") |
| `ruolo_paesaggistico` | string | – | Concatenazione "Elementi paesaggistici dominanti – Ruolo strategico" della Tab. 2a |
| `inquadramento` | string[] | – | 2 frasi/paragrafi fedeli: inquadramento della scheda Allegato II + sintesi del quadro sinottico |
| `sugherete_ha` | int | ha | Superficie sugherete (vedi uso-suolo-comuni.json; 0 dove il documento dichiara assenza nelle tabelle) |
| `implicazioni_bosco_sughero` | string | – | Testo integrale par. X.5 della scheda |
| `implicazioni_suinicola` | string | – | Testo integrale par. X.6 |
| `criticita` | string[] | – | Elenco dal par. X.7 |
| `opportunita` | string[] | – | Elenco dal par. X.8 |
| `valutazione_preliminare` | string | – | Frase conclusiva del par. X.8 |
| `sintesi_comparativa` | object | – | I 4 giudizi di pag. 172 (`vocazione_sughericola`, `interesse_suinicolo_agroforestale`, `fragilita_pedologica`, `priorita_approfondimento`) |
| `elementi_identitari` | string[] | – | Luoghi, beni e caratteri citati nel quadro sinottico (granito, stazzi, siti archeologici, aree protette, ecc.) |
| `pagine_fonte` | object | – | `scheda_preliminare`, `quadro_sinottico_parte3`, `tabella_2a`, `sintesi_comparativa` (liste di pagine PDF) |

## Fonte
Parte 1: Seconda parte, Tab. 2a (pag. 37) e par. 2.1.3, 2.3.3 (pag. 38, 47); Terza parte (pag. 53-68); Allegato II, schede comunali preliminari (pag. 156-171) e sintesi comparativa (pag. 172).

## Avvertenze
- La Tab. 2a è per ambiti anche pluricomunali: i valori sono ripetuti per ogni Comune dell'ambito; per "Aglientu – Badesi" la tipologia è resa "Costa / Interfaccia entroterra-costa" (cella fusa nell'estrazione).
- `criticita`/`opportunita` derivano dallo spezzettamento di frasi discorsive; `elementi_identitari` è una selezione redazionale, non un elenco del documento.
- Incoerenza narrativa: la Terza parte descrive Bortigiadas e Aggius come dominati da sugherete/leccete/macchia, mentre i dati GIS danno sugherete pari a 116 ha (Bortigiadas) e 6,9% (Aggius).
- Nessun giudizio è un'idoneità definitiva (natura preliminare dichiarata dal documento).

## Idee per il sito
- Pagina-scheda per Comune con header (fascia, funzione territoriale, KPI sugherete), tab "Filiere" (bosco-sughero / suinicola), "Criticità & Opportunità", "Identità".
- Mappa cliccabile dei Comuni che apre la scheda.
- Confronto side-by-side di due Comuni sui giudizi della sintesi comparativa.
