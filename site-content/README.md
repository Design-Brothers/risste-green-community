# site-content/ – tutto ciò che serve per progettare e costruire il sito

| File | Cosa contiene |
|---|---|
| [SITEMAP.md](SITEMAP.md) | Sitemap visiva (Mermaid) |
| [ARCHITETTURA.md](ARCHITETTURA.md) | Sitemap a 6 pagine, struttura di ogni pagina con dataset, figure e file di testo da usare, elenco componenti |
| [COMPONENTI.md](COMPONENTI.md) | Specifica di ogni componente con codice di esempio (React + Tailwind + Recharts + motion): orbi, anelli, KPI, grafici, esploratore, tabella, pannello comune, mappa, timeline |
| [BRIEF-DESIGN.md](BRIEF-DESIGN.md) | Obiettivi, messaggi, tono, landing "wow" con orbi fluttuanti, identità visiva, regole dati, come si costruisce (stack, struttura, pipeline contenuti e dati, deploy Vercel, qualità), consegne |
| [glossario.md](glossario.md) | 50 acronimi con significato, per i tooltip |
| [pagine/TEMPLATE.md](pagine/TEMPLATE.md) | Formato dei file pagina: frontmatter + blocchi `## Titolo {type=hero/kpi/text/chart/figure/cards/tabs/quote/sources}` |
| [pagine/microcopy.md](pagine/microcopy.md) | Menu, footer, CTA, testi di stato, tooltip indici e fasce, formula di citazione |
| [pagine/seo.md](pagine/seo.md) | Title, description e OG image per tutte le pagine |

## Pagine

Il sito ha 6 pagine (vedi [SITEMAP.md](SITEMAP.md)); i 14 file in `pagine/` sono i contenuti granulari da accorpare come indicato nella tabella della sitemap. I due file `*-template.md` descrivono il pannello scheda comune.

Regole seguite nei testi: ogni numero ha la fonte (P1/P2 + pagina fisica del PDF); dove testo e tabelle dello studio divergono si usa il valore indicato in `data/README.md`; le figure 2-4 dello studio sul sughero sono mostrate solo come elaborazione grafica, i grafici si ricostruiscono dai dataset.
