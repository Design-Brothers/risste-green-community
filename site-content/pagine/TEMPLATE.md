---
# Frontmatter di ogni pagina del sito (YAML)
slug: /alta-gallura/strategia           # percorso URL (una delle 6 pagine)
sezione: alta-gallura                    # home | progetto | alta-gallura | sughero-sardegna
eyebrow: "Alta Gallura · Strategia"      # etichetta di sezione sopra il titolo
title: "Un territorio a due velocità"    # H1 (≤ 60 caratteri)
seo_title: "…"                           # ≤ 60 caratteri
description: "…"                         # meta description 140-160 caratteri
og_image: source/parte1-green-community-alta-gallura/images/fig-3a-quadro-sinottico-comuni.jpeg
fonti:                                   # documenti e pagine PDF usati nella pagina
  - documento: parte1
    pagine: [21, 32]
dati:                                    # dataset usati (percorsi relativi a data/)
  - alta-gallura/popolazione-storica.json
figure:                                  # immagini usate (percorsi relativi a source/)
  - parte1-green-community-alta-gallura/images/fig-1a-analisi-demografico-economica-imprese.png
---

<!-- Corpo: sezioni nell'ordine in cui compaiono in pagina. Ogni sezione è un blocco `## ` con un attributo tipo. Un blocco può avere anche `id=nome` per essere raggiungibile con un'ancora (es. `{type=cards id=documenti}` → `/progetto#documenti`). Tipi: hero · kpi · text · message · chart · figure · cards · tabs · quote · sources. -->

## Hero {type=hero}
**Standfirst:** una o due frasi (≤ 45 parole) che dicono la cosa più importante della pagina.
**CTA:** Testo del bottone → /percorso (opzionale)
<!-- Campi aggiuntivi dell'hero immersivo della landing (BRIEF §3); facoltativi nelle pagine di sezione, che usano un solo orbo o gli anelli. -->
**Titolo:** Riga uno / Riga due (il titolo enorme spezzato alla barra, 2-3 righe; se manca vale `title`)
**Parola fantasma:** UCAG 193 (parola in outline sottile dietro l'orbo, tagliata dai bordi)
**Micro-etichette:** RISSTE — · — UCAG 193 · 11 COMUNI (etichette 11-12 px maiuscole agli angoli e sugli orbi, separate da " · ")
**Orbi:** verde #4E9A3F · ciano #3FE9FF · … (palette e numero degli orbi, 4-6)
**Fonte:** P1 p. N (se il standfirst cita numeri)

## Titolo-messaggio della sezione {type=kpi}
<!-- 3-4 KPI. Formato: valore | unità | etichetta | contesto (≤ 20 parole) | fonte -->
- 35.242 | abitanti | Residenti nel 2025 | Undici comuni, dalla costa al Limbara. | P1 p.22
- …

## Frase-titolo del messaggio {type=message}
<!-- Messaggio chiave della landing: una schermata intera, sequenza a scorrimento. A sinistra numero grande e frase-titolo (l'H2), a destra l'orbo che cambia colore e la parola-fantasma. Il KPI compare con un conteggio breve. Fonte sempre presente. -->
**Numero:** 01 (due cifre, grande)
**Testo:** Due frasi, ≤ 22 parole ciascuna: il fatto e la sua conseguenza.
**KPI:** valore | unità | etichetta (uno solo, con conteggio animato)
**Orbo:** nome colore · #da → #a (colore dell'orbo di questa schermata; sequenza verde → ciano → blu → ambra → verde)
**Parola fantasma:** PAROLA (outline dietro l'orbo; cambia a ogni messaggio)
**Dati:** data/…/file.json → campi usati (opzionale)
**Fonte:** P1, Tab. N, p. N
**CTA:** Testo del bottone → /percorso (opzionale, uno solo)

## Titolo-messaggio {type=text}
Paragrafi di testo (≤ 22 parole a frase). Gli acronimi si sciolgono la prima volta e si marcano con [[IVP]] per il tooltip del glossario.

## Titolo-messaggio {type=chart}
**Grafico:** tipo (barre orizzontali / slope / impilate 100% / timeline) — cosa mostra in una riga.
**Dati:** data/alta-gallura/popolazione-storica.json → campi usati.
**Lettura:** 1-2 frasi che dicono cosa si vede (va in pagina sotto al grafico).
**Fonte:** P1, Tab. 1a, p.22

## Titolo {type=figure}
**Immagine:** source/…/fig-xx.jpeg
**Didascalia:** testo (fedele all'originale, abbreviato se serve).
**Alt:** descrizione per screen reader (≤ 125 caratteri).

## Titolo {type=cards}
<!-- Card con titolo + 1-2 frasi; eventuale icona suggerita -->
- **Titolo card** — testo. `icona: tree`

## Titolo {type=tabs}
### Nome tab 1
…
### Nome tab 2
…

## Titolo {type=quote}
> Citazione testuale breve dallo studio (≤ 40 parole).
— Fonte, p. N

## Fonti {type=sources}
- Titolo studio, capitolo, pp. N-M
