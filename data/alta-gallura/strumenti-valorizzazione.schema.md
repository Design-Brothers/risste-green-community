# strumenti-valorizzazione.json

I tre strumenti di valorizzazione territoriale del paragrafo 4.4, ciascuno con approccio, obiettivi, azioni e strumenti. `dati` è un array di 3 record.

## Campi

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `ordine` | int | – | Ordine nel documento |
| `slug` | string | – | Identificatore kebab-case |
| `nome` | string | – | Titolo del sottoparagrafo |
| `paragrafo` | string | – | Numero del sottoparagrafo (4.4.1, 4.4.2, 4.4.3) |
| `pagine_pdf` | int[] | – | Pagine PDF |
| `approccio` | string | – | Impostazione generale (max 3-4 frasi) |
| `obiettivi` | string[] | – | Obiettivi dichiarati |
| `azioni` | string[] | – | Azioni/interventi previsti |
| `strumenti` | string[] | – | Strumenti operativi, regolativi o analitici citati |

## Fonte
Parte 1: 4.4 (pag. 75), 4.4.1 (pag. 75-76), 4.4.2 (pag. 76-77), 4.4.3 (pag. 77-78).

## Avvertenze
- Ripartizione obiettivi/azioni/strumenti redazionale su testo discorsivo.
- Nessun dato quantitativo nel paragrafo.

## Idee per il sito
- Tre card affiancate con accordion obiettivi/azioni/strumenti.
- Schema "gradiente di fragilità" (suoli fragili → prudenza; suoli profondi → pascolo controllato) per 4.4.3.
- Collegamento incrociato a `filiere.json` (pascolo come prevenzione incendi) e a `roadmap.json` (azioni 8 e 16).
