# superfici-unione.json

Grandezze territoriali di scala sovracomunale riportate nello studio (distretti forestali, Monte Limbara, quota nazionale del sughero, parametri di riferimento) e indicatori di Unione NON disponibili (valore null). `dati` contiene 18 record.

## Campi

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `indicatore` | string | – | Descrizione della grandezza |
| `valore` | number\|null | vedi `unita` | Valore come nel documento; null se non riportato |
| `unita` | string | – | `ha`, `%`, `m s.l.m.`, `m3/ha`, `anni`, `km` |
| `operatore` | string | – | Presente solo se il testo qualifica il numero (`oltre`, `circa`) |
| `ambito` | string | – | Scala di riferimento (`Unione`, `Distretto forestale 01`, `Monte Limbara`, …) |
| `pagina_pdf` | int\|null | – | Pagina PDF; null per indicatori assenti |
| `nota` | string\|null | – | Contesto/avvertenza |

## Valori presenti
Quota sughero nazionale lavorato: oltre 80% (pag. 42-43) · Distretto forestale 01 Alta Gallura: 150.251 ha = 6,2% della Sardegna (pag. 42) · Distretto 04 Coghinas-Limbara: 123.387 ha = 5,1% (pag. 42) · Sito Monte Limbara: 16.588 ha (pag. 44) · Monte Limbara 1359 m (pag. 39) · Distretto di Calangianus: oltre 67% superfici ad elevata fertilità (pag. 41) · leccete mature 145,96 m3/ha (pag. 40) · turno di estrazione 12 anni (pag. 42) · costa di Aglientu circa 18 km (pag. 56) · UGB Limbara Sud 3.630,1 ha, macchia evoluta 51% (pag. 48).

## Fonte
Parte 1, Seconda parte par. 2.2.1-2.2.6 (pag. 39-44), 2.3.3 (pag. 47-48); Terza parte (pag. 56).

## Avvertenze
- Il documento non riporta la superficie complessiva dell'Unione né totali di superfici agricole, pascolive, forestali o di sugherete a scala di Unione (5 record con `valore: null`).
- La somma dei valori comunali di sugherete (uso-suolo-comuni.json) non compare nel documento e non è stata inserita.
- Il Distretto forestale 01 non coincide con l'Unione; l'UGB Limbara Sud è in comune di Berchidda (esterno).

## Idee per il sito
- KPI "oltre l'80% del sughero lavorato in Italia" come numero-chiave della home.
- Infografica a scale: Distretto 01 (150.251 ha) → sito Monte Limbara (16.588 ha) → sugherete per Comune.
- Nota trasparente "dati non disponibili nello studio" per superficie Unione e totali, per evitare stime.
