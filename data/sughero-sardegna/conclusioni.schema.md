# conclusioni.json

Conclusioni e prospettive della Quinta parte (pagg. 45-46) come 10 messaggi chiave testuali e 7 raccomandazioni, più la frase di chiusura.

## Struttura (`dati` è un oggetto)

| campo | tipo | significato |
|---|---|---|
| `messaggi_chiave[]` | list | 10 elementi |
| `messaggi_chiave[].id` | int | ordine nel testo |
| `messaggi_chiave[].tema` | string | etichetta redazionale breve (approccio, indicatori territoriali, innovazione, certificazioni, framework, DSS, visione, …) |
| `messaggi_chiave[].testo` | string | frase fedele del documento |
| `messaggi_chiave[].pagina_pdf` | int o list[int] | pagina/e |
| `raccomandazioni[]` | list | 7 elementi |
| `raccomandazioni[].destinatari` | string | destinatario redazionale (ricerca, imprese forestali, governance, pianificazione, …) |
| `raccomandazioni[].testo` | string | raccomandazione, parafrasi minima in forma prescrittiva del testo citato |
| `raccomandazioni[].pagina_pdf` | int o list[int] | pagina/e (33, 34, 41, 42, 44, 45, 46) |
| `prospettiva_finale` | {testo, pagina_pdf} | frase conclusiva del documento |

## Fonte

Parte 2, Quinta parte pagg. 45-46; raccomandazioni integrate da pag. 33 (par. 3.3.3), pag. 34 (par. 3.4.2), pagg. 41-42 e 44 (par. 4.4-4.5).

## Avvertenze

- `tema` e `destinatari` sono etichette redazionali, non presenti nel documento.
- Le raccomandazioni 1-4 sono nel testo in forma di "suggerimento"/"necessità"; qui sono rese in forma imperativa senza aggiungere contenuti.
- Nessun dato numerico.

## Idee di rappresentazione

- Sezione "In sintesi" con i 10 messaggi come elenco numerato a scomparsa, ognuno con link alla pagina PDF.
- Griglia delle raccomandazioni per destinatario (ricerca / imprese / governance / pianificazione).
- Citazione in evidenza per `prospettiva_finale`.
