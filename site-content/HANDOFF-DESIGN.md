# Handoff per il design – in una pagina

**Cosa devi progettare.** Un mini-sito istituzionale di 6 pagine che racconta due studi scientifici con una landing d'effetto e pagine interne pulite, fatte di poco testo, pochi numeri forti e tabelle di approfondimento su richiesta.

**Cosa ti diamo**
1. [BRIEF-DESIGN.md](BRIEF-DESIGN.md) – obiettivo, pubblico, cinque messaggi, tono, look and feel con i riferimenti visivi tradotti, colori, tipografia, regole per i dati, come si costruisce.
2. [SITEMAP.md](SITEMAP.md) – le 6 pagine e i due pannelli comune.
3. `pagine/` – il **copy finale** di ogni pagina, 250-500 parole: titolo, sottotitolo, capitoli di apertura con i numeri, sezioni brevi, elenco degli approfondimenti da rendere in tabella o grafico. Nel frontmatter una riga `visual` descrive l'illustrazione animata di apertura.
4. [COMPONENTI.md](COMPONENTI.md) – come realizzare ogni componente, con codice di esempio.
5. `../data/` – i dataset per tabelle e grafici (ogni file ha uno schema che spiega i campi); `../source/*/images/` – le 16 infografiche originali; `../source/brand/` – logo RISSTE.

**Struttura di ogni pagina** (dall'alto): illustrazione animata + titolo → capitoli di apertura scroll-driven (solo home e due pagine di sezione) → 3-5 sezioni brevi con al massimo tre numeri ciascuna → blocco "Approfondimenti" con tabelle e grafici filtrabili → fonti in una riga.

**Priorità di design**
- Landing: effetto wow con sfere di luce fluttuanti, tipografia enorme e leggera, cinque capitoli con un numero ciascuno, poi il sito "atterra".
- Pagine interne: molto bianco, card arrotondate, un'interazione per pagina (scegli il comune, ordina i 30 comuni, filtra le pubblicazioni).
- Pannello comune: laterale, condivisibile via URL, stesso schema per gli 11 e i 30 comuni.
- Mobile: capitoli come card, tabelle con scroll interno, pannello dal basso.

**Cosa non fare.** Foto stock, 3D, gradienti scuri, tabelle a vista senza contesto, testo che si muove, più di un'interazione per blocco.

**Consegne.** Design system (token) e moodboard landing; wireframe delle 6 pagine e del pannello, desktop e mobile; prototipo motion dell'hero e dei capitoli.
