# pedologia-comuni.json / .csv

Principali unità pedologiche (Carta dei Suoli della Sardegna, 1:250.000) per ciascuno degli 11 Comuni dell'Unione Alta Gallura, con superficie e incidenza sul territorio comunale. `dati` contiene 51 righe (4-5 unità per Comune). Il JSON aggiunge `unita_pedologiche` (dizionario di 12 codici con descrizione ricavata dal testo) e `commenti_per_comune` (lettura pedologica di ciascuna scheda).

## Campi (`dati` e CSV)

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `comune` | string | – | Nome come nel documento |
| `slug` | string | – | Identificatore kebab-case |
| `unita_pedologica` | string | – | Codice dell'unità (`C1`, `C2`, `C3`, `C5`, `B1`, `B2`, `B3`, `M1`, `L1`, `L2`, `I1`, `G1`) |
| `rango` | int | – | Posizione nella tabella della scheda (1 = unità più estesa) |
| `superficie_ha` | int | ha | Superficie dell'unità nel Comune |
| `incidenza_pct` | float | % | Percentuale sul territorio comunale |
| `pagina_pdf` | int | – | Pagina PDF della tabella |

## Blocco `unita_pedologiche` (solo JSON)

Oggetto `codice → {descrizione, pagine_pdf, substrato}`. `substrato`: `rocce intrusive` (C*), `metamorfiti paleozoiche` (B*), `sabbie eoliche` (M1), `alluvioni / aree pianeggianti` (L1, L2), null (I1, G1: non descritte).

## Blocco `commenti_per_comune` (solo JSON)

`comune`, `slug`, `pagina_pdf`, `testo` (commento fedele della scheda alla tabella pedologica).

## Fonte
Parte 1, Allegato II – Schede comunali preliminari, par. "Sintesi pedologica" (pag. 156, 158, 160, 161, 162, 164, 165, 167, 168, 169, 171); descrizione della Carta dei Suoli (Aru, Baldaccini, Vacca 1991) pag. 150.

## Avvertenze
- Le somme delle incidenze per Comune vanno dal 95,1% (Viddalba) e 96,3% (Bortigiadas) al 100,0% (Badesi): la quota residua non è dettagliata (elenco completo nella prima nota del JSON).
- Le descrizioni delle unità non sono la legenda ufficiale della Carta dei Suoli ma sintesi dei commenti presenti nelle schede; B3, G1 e I1 non sono descritte nel documento.
- C1 e C2 dominano quasi tutti i Comuni (C2 fino all'84,1% a Luogosanto; C1 fino al 63,8% a Calangianus); Badesi è l'unico Comune a prevalenza M1 (sabbie eoliche, 50,1%).

## Idee per il sito
- Barre impilate per Comune colorate per unità, con legenda che spiega i codici (tooltip con `unita_pedologiche`).
- Indicatore "quota di suoli fragili (C1 + B1)" per Comune, da collegare alla fragilità pedologica della sintesi comparativa.
- Scheda glossario delle unità pedologiche con substrato e limitazioni.
