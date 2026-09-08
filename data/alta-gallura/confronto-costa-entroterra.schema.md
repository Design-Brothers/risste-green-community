# confronto-costa-entroterra.json

La tabella comparativa fascia costiera (4 comuni) vs entroterra (7 comuni) del par. 1.7 (Tabella 1c), integrata con tre indicatori economici del par. 1.10, e la sintesi delle quattro dinamiche 1.7.1-1.7.4. `dati` = 11 indicatori; `dinamiche` = 4 record.

## Campi (`dati`)

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `indicatore` | string | – | Chiave snake_case |
| `etichetta` | string | – | Etichetta della Tabella 1c (o del par. 1.10) |
| `fascia_costiera` | number | vedi `unita` | Valore per Aglientu, Badesi, Santa Teresa Gallura, Trinità d'Agultu e Vignola |
| `entroterra` | number | vedi `unita` | Valore per Aggius, Bortigiadas, Calangianus, Luogosanto, Luras, Tempio Pausania, Viddalba |
| `unita` | string | – | abitanti, unità, %, imprese, indici |
| `dinamica_prevalente` | string | – | Colonna "Dinamica territoriale prevalente" della tabella |
| `pagine_pdf` | int[] | – | Pagine PDF |

## Campi (`dinamiche`)

| Campo | Tipo | Significato |
|---|---|---|
| `paragrafo` | string | 1.7.1 ... 1.7.4 |
| `titolo` | string | Titolo del paragrafo |
| `sintesi` | string | Una frase fedele ma sintetica con i numeri chiave |
| `pagine_pdf` | int[] | Pagine PDF |

## Fonte
Parte 1: par. 1.7 e Tabella 1c (pag. 25-26), par. 1.7.1-1.7.4 (pag. 25-27), par. 1.10 (pag. 29-30).

## Avvertenze
- La Tabella 1c porta nel PDF lo stesso titolo della 1b ("Saldo naturale e saldo migratorio...") ed è spezzata su due pagine.
- Indice di vecchiaia medio (316,5 / 291,6) e indice di dipendenza entroterra (58,1) non sono riproducibili dai dati comunali (né media semplice né rapporto aggregato); il 59,9 costiero è la media semplice dei 4 indici comunali. Riportati come scritti.
- Utenza scolastica 1.177 / 3.118 differisce dalla somma delle schede (1.167 / 3.128).
- Nel par. 1.7.3 i componenti medi di Badesi e Trinità sono invertiti rispetto alle schede.

## Idee per il sito
- Layout "due colonne" costa vs entroterra con barre specchiate per ciascun indicatore.
- Quattro card per le dinamiche 1.7.1-1.7.4 con il numero chiave in evidenza.
- Mappa a due colori dell'Unione (4 costieri / 7 interni) come navigazione verso le schede comunali.
