# obiettivi-studio.json

Finalità, obiettivi strategici e operativi, destinatari e gruppo di lavoro dello studio "Green community UCAG 193" (Parte 1). Struttura standard (`titolo`, `fonte`, `note`, `dati`); `dati` è un array di record eterogenei distinti dal campo `tipo`.

## Campi

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `tipo` | string | – | `finalita`, `obiettivo_strategico`, `obiettivo_operativo`, `destinatario`, `componente_gruppo_di_lavoro` |
| `ordine` | int | – | Ordine di esposizione nel documento (solo obiettivi e gruppo di lavoro) |
| `pagina_pdf` | int | – | Pagina PDF della fonte |
| `testo` | string | – | Sintesi fedele (max 3-4 frasi) di finalità/obiettivo |
| `nome` | string | – | Nome del destinatario o del componente |
| `nota` | string | – | Chiarimento sulla provenienza (solo destinatari) |
| `ruolo` | string | – | Qualifica/ruolo come riportato nel documento |
| `competenze` | string | – | Ambiti di competenza dichiarati |

## Fonte
Parte 1, Premessa par. ii-iii (pag. 14), par. v (pag. 15), Quadro metodologico par. vii (pag. 18-19).

## Avvertenze
- La scomposizione in punti degli obiettivi è redazionale: nel documento sono esposti in forma discorsiva.
- I destinatari non hanno un paragrafo dedicato nel documento.
- Nessun dato numerico oltre al riferimento alle 11 municipalità dell'Unione.

## Idee per il sito
- Blocco "Perché questo studio" con finalità + 3 obiettivi strategici come card.
- Timeline/elenco degli obiettivi operativi collegati ai dataset che li dettagliano (roadmap, filiere, formazione).
- Sezione "Gruppo di lavoro" con schede nome/ruolo/competenze.
