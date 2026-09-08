# Convenzioni per i dataset curati in `data/`

Questi file sono la "verità" numerica che il sito userà. Regole:

1. **Fedeltà alla fonte.** Ogni valore deve comparire nei testi/tabelle in `source/`. Niente stime, niente arrotondamenti diversi dall'originale. Se un dato manca, `null` + spiegazione in `note`.
2. **Formati.** JSON UTF-8 indentato 2 spazi; CSV con virgola, header in prima riga, UTF-8. Numeri come numeri (non stringhe): `"1.685"` → `1685`, `"-16,26%"` → `-16.26` in un campo con suffisso `_pct`. Ettari con suffisso `_ha` (float), superfici in `%` con `_pct`. Categorie testuali mantenute come nell'originale (es. `"Medio-alta"`).
3. **Chiavi** in italiano, `snake_case`. Comuni identificati da `comune` (nome come nel documento) e `slug` kebab-case senza accenti: `aggius`, `aglientu`, `badesi`, `bortigiadas`, `calangianus`, `luogosanto`, `luras`, `santa-teresa-gallura`, `tempio-pausania`, `trinita-d-agultu-e-vignola`, `viddalba`; per i 30 comuni della Sughereta Sardegna stesso criterio (`ala-dei-sardi`, `budduso`, `villanova-monteleone`, ...).
4. **Struttura JSON** di ogni file:
   ```json
   {
     "titolo": "…",
     "fonte": { "documento": "parte1|parte2", "capitolo": "…", "pagine_pdf": [22, 23] },
     "note": ["…"],
     "dati": [ … ]
   }
   ```
5. **Schema.** Ogni dataset `nome.json`/`nome.csv` è accompagnato da `nome.schema.md`: cosa contiene, un rigo per campo (nome, tipo, unità, significato), fonte con pagine, avvertenze, e 2-3 idee di rappresentazione per il sito (grafico, mappa, filtro, KPI).
6. **Cartelle.** `data/alta-gallura/` (Parte 1 – Green community UCAG 193, 11 comuni) e `data/sughero-sardegna/` (Parte 2 – filiera sughero, 30 comuni). File trasversali in `data/`.
