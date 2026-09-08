# site-content/ – tutto ciò che serve per progettare e costruire il sito

| File | Cosa contiene |
|---|---|
| [HANDOFF-DESIGN.md](HANDOFF-DESIGN.md) | **Da qui parte chi disegna**: cosa progettare, cosa riceve, priorità, consegne (una pagina) |
| [SITEMAP.md](SITEMAP.md) | Sitemap visiva (Mermaid) |
| [ARCHITETTURA.md](ARCHITETTURA.md) | Sitemap a 6 pagine, struttura di ogni pagina con dataset, figure e file di testo da usare, elenco componenti |
| [COMPONENTI.md](COMPONENTI.md) | Specifica di ogni componente con codice di esempio (React + Tailwind + Recharts + motion): orbi, anelli, KPI, grafici, esploratore, tabella, pannello comune, mappa, timeline |
| [BRIEF-DESIGN.md](BRIEF-DESIGN.md) | Obiettivi, messaggi, tono, landing "wow" con orbi fluttuanti, identità visiva, regole dati, come si costruisce (stack, struttura, pipeline contenuti e dati, deploy Vercel, qualità), consegne |
| [glossario.md](glossario.md) | 50 acronimi con significato, per i tooltip |
| [pagine/TEMPLATE.md](pagine/TEMPLATE.md) | Formato dei file pagina: frontmatter breve + copy finale in Markdown |
| [pagine/microcopy.md](pagine/microcopy.md) | Menu, pulsanti, footer, citazione, 404 |

## Pagine

Il sito ha 6 pagine (vedi [SITEMAP.md](SITEMAP.md)): un file di copy finale per pagina in `pagine/`, più due file `*-pannello-comune.md` che descrivono il pannello scheda comune. Title e description SEO sono nel frontmatter di ogni pagina. Le versioni precedenti (12 pagine; 6 pagine in formato tecnico) sono in `_archivio/`.

Regole dei testi: copy breve e umano, ogni numero esiste in `data/`, fonti in una riga a fondo pagina. Dove testo e tabelle dello studio divergono vale il valore indicato in `data/README.md`; le figure 2-4 dello studio sul sughero si mostrano solo come elaborazione grafica, i grafici si ricostruiscono dai dataset.
