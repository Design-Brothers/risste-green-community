# strumenti-certificazione.json

Gli 11 strumenti della Tabella 2 (pag. 41) più 3 strumenti citati solo nel testo/Figura 1, con tipologia, finalità, contributo alla filiera e le criticità/raccomandazioni dei par. 3.4.2 e 4.4.

## Campi (`dati[]`)

| campo | tipo | unità | significato |
|---|---|---|---|
| `id` | int | – | ordine (1-11 = righe della Tabella 2; 12-14 extra-tabella) |
| `strumento` | string | – | denominazione come in Tabella 2 (o nel testo) |
| `nome_completo` | string o `null` | – | esplicitazione redazionale della sigla |
| `tipo` | string | – | categoria secondo le classi usate dal documento (forestale, agroforestale, sistema di gestione aziendale/ambientale, standard di prodotto/packaging, tracciabilità, valutazione ambientale, quadro ESG) |
| `cosa_certifica` | string o `null` | – | "Finalità principale" (testo originale Tabella 2) |
| `rilevanza_filiera` | string o `null` | – | "Contributo alla filiera del sughero" (testo originale) o sintesi dal testo per gli extra-tabella |
| `in_tabella_2` | bool | – | true se la riga è nella Tabella 2 |
| `note` | string o `null` | – | varianti di denominazione, riferimenti puntuali |
| `pagina_pdf` | list[int] | – | pagine in cui lo strumento è citato |

Sezione aggiuntiva `criticita_e_raccomandazioni` con liste di `{testo, pagina_pdf}`: `benefici_citati`, `criticita`, `raccomandazioni`.

## Fonte

Parte 2, Tabella 2 pag. 41 (`tables/p041-t0.csv`, qualità "ok"); par. 2.4 pag. 22; par. 2.5 pag. 23; par. 3.4.2 pag. 34; par. 4.4 pagg. 38-41; Conclusioni pag. 45; Figura 1 pag. 26.

## Avvertenze

- Nessun dato quantitativo (ettari o aziende certificate, costi) nel documento.
- `tipo` e `nome_completo` sono classificazioni/esplicitazioni redazionali coerenti con il testo, non colonne della fonte.
- Per il PEFC agroforestale il documento usa quattro denominazioni diverse (vedi `note` del file).

## Idee di rappresentazione

- Tabella filtrabile per `tipo` con colonne strumento / cosa certifica / contributo, evidenziando le righe `in_tabella_2 = false` come "citati nel testo".
- Schema a livelli: foresta (FSC, PEFC, PEFC Agroforestale) → impresa (ISO 9001, ISO 14001, EMAS) → prodotto/packaging (BRCGS, IFS PACsecure, SYSTECODE) → misura ambientale (LCA, Carbon/Water Footprint) → rendicontazione ESG.
- Box "criticità → raccomandazioni" affiancate (frammentazione fondiaria → certificazione di gruppo, ecc.).
