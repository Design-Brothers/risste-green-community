# `sintesi-regionale.json`

Totali, conteggi per classe, estremi e profili dei 30 comuni della Sughereta Sardegna, ricalcolati da `comuni-sughereta.json` e confrontati con quanto riporta il testo del rapporto (par. 2.2, 3.1-3.2). Include il registro delle incoerenze rilevate nella fonte.

**Fonte.** Parte 2: pag. 20 (≈83.800 ha), pag. 27 (83.790,90 ha, elenco dei maggiori comuni), pag. 27-29 (conteggi e comuni estremi per IVP, IPI, ICR), Allegato I pag. 50-141 (dati per comune).

## Struttura di `dati`

| Campo | Tipo | Significato |
|---|---|---|
| `totali.sugherete_30_comuni_ha_testo` | float | 83.790,90 ha (pag. 27) |
| `totali.sugherete_30_comuni_ha_testo_arrotondato` | int | 83.800 ("circa", pag. 20) |
| `totali.somma_sugherete_30_comuni_ha` | float | Somma delle 30 superfici del dataset (coincide con il testo) |
| `totali.somma_peso_pct` | float | Somma dei pesi % (99,98: la "Sughereta Sardegna" di riferimento è l'insieme dei 30 comuni) |
| `totali.n_comuni`, `n_complessi_totali` | int | 30 comuni; somma dei complessi sughericoli |
| `totali.superficie_medioalto_alto_ha`, `quota_medioalto_alto_pct_sul_totale` | float | Superficie e quota in pericolo Medioalto+Alto sul totale dei 30 comuni |
| `totali.ivp_medio_ponderato_ha`, `ipi_medio_ponderato_ha` | float | Medie degli indici comunali pesate per ettari (elaborazione nostra, non nel testo) |
| `superficie_per_classe_incendio_ha` / `_pct` | oggetto | Somma delle tabelle incendio dei 30 comuni per classe Basso…Alto |
| `superficie_per_classe_ivp_unita_ha` | oggetto | Somma delle superfici per classe IVP delle unità pedologiche |
| `conteggi_classe_ivp` / `_incendio` / `_icr` | oggetto | `dataset` (lista `{classe, n_comuni, comuni}`), valore del testo, `differenze` |
| `conteggi_classe_densita`, `conteggi_profilo_integrato` | lista | Conteggi dal dataset |
| `top5_estensione` | lista | I 5 comuni più estesi (`rank`, `comune`, `slug`, `sugherete_ha`, `peso_pct_sughereta_sardegna`) |
| `estremi` | oggetto | Top/bottom per `ivp`, `quota_medioalto_alto_pct`, `quota_complesso_maggiore_pct`, `n_complessi` |
| `profili_estremi` | oggetto | `piu_favorevoli`, `priorita_alta_governabili`, `piu_critici`: criterio testuale, elenco slug e riferimento alle frasi del testo (pag. 28-29) |
| `comprensori_citati` | string[] | Comprensori storici citati a pag. 27 (senza attribuzione per comune) |
| `incoerenze_fonte` | oggetto | `sinottico_vs_dossier` (nessuna), `ricalcoli` (Bultei IVP), `testo_vs_dossier` (conteggi 22/4/4 vs 21/4/5; 8 vs 9 ICR Alta; refusi di numerazione figure), `confronto_figure` (comuni non coerenti per figura, comuni estranei/assenti, duplicato Nuoro), `estrazione` (righe reintegrate dal PDF) |

## Avvertenze

- I conteggi "del testo" e "del dataset" differiscono per IVP (testo 22 Alta / 4 Media / 4 Bassa; dossier 21 / 4 / 5) e ICR (testo 8 Alta; dossier 9, con Aidomaggiore). Nei contenuti del sito indicare i conteggi dei dossier e, se si cita il testo, segnalare la differenza.
- Il documento non definisce una graduatoria "migliore/peggiore": `profili_estremi` si basa sui profili integrati assegnati dai dossier e sulle frasi del par. 3.2; è una lettura, non un dato del rapporto.
- Le medie ponderate regionali (`ivp_medio_ponderato_ha`, `ipi_medio_ponderato_ha`) non compaiono nel documento: sono elaborazioni derivate, da etichettare come tali.

## Idee di rappresentazione

1. **KPI header**: 30 comuni, 83.790,90 ha, quota in pericolo Medioalto+Alto, n. complessi totali, 21/4/5 comuni per classe IVP.
2. **Barre impilate regionali**: superficie per classe di pericolosità incendio e per classe IVP delle unità pedologiche (`superficie_per_classe_*`).
3. **Donut/waffle** dei 30 comuni per `classe_ivp`, `classe_incendio`, `classe_icr`, `profilo_integrato`, con confronto "testo vs dossier" in nota.
4. **Top 5 per estensione** come mini-ranking con peso % cumulato.
5. **Pannello "differenze rilevate"** (da `incoerenze_fonte`) per la sezione metodologica/trasparenza del sito.
