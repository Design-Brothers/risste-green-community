# contesto-sughero-sardegna.json

Numeri e riferimenti di contesto sulla filiera del sughero in Sardegna così come citati nella Parte 2 (contesto strategico, pagg. 15-18, con i richiami quantitativi di pagg. 20 e 27).

## Struttura

`dati` è una lista di indicatori; ogni elemento ha:

| campo | tipo | unità | significato |
|---|---|---|---|
| `chiave` | string | – | identificativo snake_case dell'indicatore |
| `descrizione` | string | – | cosa misura / descrive |
| `valore` | number, string, list, object o `null` | vedi `unita` | valore come nel documento (numeri come numeri; liste/oggetti per le informazioni qualitative) |
| `unita` | string o `null` | – | `%`, `ha`, `comuni`, … |
| `approssimazione` | string (opz.) | – | presente quando il testo dice "circa" |
| `anno` | int o `null` | – | anno di riferimento del dato: **sempre `null`**, il documento non lo indica |
| `pagina_pdf` | int, list o `null` | – | pagina/e PDF della fonte |
| `testo_fonte` | string (opz.) | – | frase originale da cui è tratto il valore |
| `note` | string (opz.) | – | avvertenze; per i `null` spiega perché il dato manca |

Per `comuni_maggiore_estensione_sughereta` il valore è una lista di `{comune, slug, superficie_ha}` (slug kebab-case senza accenti secondo le convenzioni).

## Fonte

Parte 2, pagg. 15-18 (par. 1, 1.1, 1.2); pag. 20 (par. 2.2); pag. 27 (par. 3.1).

## Avvertenze

- La Parte 2 non contiene dati su produzione, imprese, addetti, export, quota mondiale: i relativi indicatori sono `null` con nota. Non integrare con stime esterne senza segnalarlo.
- 83.790,90 ha (pag. 27) e "circa 83.800 ettari" (pag. 20) sono lo stesso dato (30 comuni prioritari), non la superficie regionale totale.
- Il "90%" di pag. 16 è un ordine di grandezza ("circa") senza anno.

## Idee di rappresentazione

- KPI in testata: 90% delle sugherete italiane · 83.790,90 ha nei 30 comuni · 30 comuni prioritari.
- Barre orizzontali dei 7 comuni citati con maggiore estensione (collegabili alla mappa dei 30 comuni dell'Allegato I).
- Scheda "il sughero come biomateriale": chip con le proprietà e i settori applicativi citati.
