# `comuni-sughereta.json` / `comuni-sughereta.csv`

I 30 comuni della "Sughereta Sardegna" (comuni prioritari per estensione delle superfici a sughera) con i tre indici territoriali dello studio RISSTE Parte 2: Indice di Vocazionalità Pedologica (IVP), pericolo incendio (IPI) e Indice di Continuità della Risorsa (ICR). Un record per comune, ordinato per `rank` (estensione decrescente).

**Fonte.** Parte 2, Allegato I "Studio tecnico sugherete – Dossier comunale integrato": quadro sinottico pag. 50-51 e schede comunali 01-30 pag. 52-141 (pagine fisiche del PDF; la numerazione stampata è inferiore di 17). File: `source/parte2-filiera-sughero-sardegna/capitoli/08-allegato1-studio-tecnico-sugherete.md`, CSV `tables/p050-t1.csv` … `p140-t2.csv`, figure `images/fig-2…`, `fig-3…`, `fig-4…` (pag. 28-30).

## Campi scalari (JSON e CSV)

| Campo | Tipo | Unità | Significato |
|---|---|---|---|
| `rank` | int | – | Posizione per estensione della sughereta (1 = Bitti, 30 = Bultei), come nel quadro sinottico |
| `comune` | string | – | Nome del comune come scritto nel dossier (es. `Ala' Dei Sardi`, `Budduso'`) |
| `nome_corrente` | string | – | Forma usata nel corpo del rapporto (`Alà dei Sardi`, `Buddusò`); uguale a `comune` per gli altri |
| `slug` | string | – | Identificativo kebab-case senza accenti (`ala-dei-sardi`, `budduso`, `villanova-monteleone`, …) |
| `provincia` | null | – | Non indicata nel documento: sempre `null` (vuoto nel CSV) |
| `sugherete_ha` | float | ha | Superficie a sughera del comune |
| `peso_pct_sughereta_sardegna` | float | % | Quota della superficie comunale sul totale dei 30 comuni (la somma è 99,98%) |
| `ivp` | float | indice 1-4 | IVP ponderato comunale (media dei punteggi delle unità pedologiche pesata per superficie) |
| `classe_ivp` | string | – | `Alta`, `Media`, `Bassa` (nessun comune `Molto bassa`) |
| `ipi` | float | indice 0-100 | "Indice incendio ponderato" della scheda = IPI comunale |
| `classe_incendio` | string | – | `Mediobasso`, `Medio`, `Medioalto`, `Alto` (classe ponderata comunale) |
| `quota_medioalto_alto_pct` | float | % | Quota della sughereta comunale nelle classi di pericolosità Medioalto + Alto |
| `quota_medioalto_alto_ha` | float | ha | Superficie corrispondente (dalla sintesi esecutiva) |
| `n_complessi` | int | n | Numero di complessi (patch) sughericoli del comune |
| `superficie_complesso_maggiore_ha` | float | ha | Superficie del complesso più esteso |
| `quota_complesso_maggiore_pct` | float | % | Quota del complesso maggiore sulla sughereta comunale (indicatore su cui è assegnata la classe ICR) |
| `superficie_media_complesso_ha` | float | ha | `sugherete_ha / n_complessi` |
| `densita_frammentazione` | float | complessi/100 ha | `n_complessi / sugherete_ha × 100` |
| `classe_densita` | string | – | Classe della densità di frammentazione: `Bassa`, `Media`, `Alta`, `Molto alta` |
| `classe_icr` | string | – | `Alta`, `Media`, `Bassa`, `Molto bassa` |
| `profilo_ivp_x_incendio` | string | – | Profilo a due fattori del quadro sintetico ("Profilo IVP x incendio"), 5 valori distinti |
| `profilo_integrato` | string | – | Profilo a tre fattori (IVP × incendio × ICR) della matrice integrata, 7 valori distinti |
| `combinazione` | string | – | Terna testuale `classe_ivp x classe_incendio x classe_icr` come scritta nella "Lettura integrata" |
| `pagine_fonte` | int[] (JSON) / `"52-55"` (CSV) | pag. PDF | Pagine fisiche del PDF occupate dalla scheda comunale |

## Campi solo JSON

| Campo | Tipo | Significato |
|---|---|---|
| `indicazioni_operative` | string[] | Le 4 indicazioni operative preliminari della scheda (punto 5), senza punteggiatura finale; 7 frasi ricorrenti in tutto il dossier |
| `lettura_icr` | string | Frase di lettura della classe ICR (tabella punto 4) |
| `sintesi_esecutiva` | string | Testo integrale del punto 1 della scheda |
| `distribuzione_pedologica` | oggetto[] | Una riga per unità pedologica: `unita_pedologica` (sigla Carta dei suoli, es. `C2`), `superficie_ha`, `incidenza_pct`, `classe_capacita_uso` (classi di capacità d'uso, es. `VII - VI - IV`; `null` per `O`, `SP`), `classe_ivp` (`Alta`/`Media`/`Bassa`/`Molto bassa`), `punteggio_ivp` (4/3/2/1) |
| `distribuzione_incendio` | oggetto[] | Una riga per classe di pericolosità presente: `classe` (`Basso`…`Alto`), `superficie_ha`, `incidenza_pct`, `indice_classe` (indice di pericolosità medio della classe nel comune) |
| `confronto_figure` | oggetto | Valori letti nelle Figure 2, 3, 4 (pag. 28-30): `ivp_fig2`, `classe_ivp_fig2`, `ipi_fig3`, `classe_incendio_fig3`, `classe_icr_fig4`, `n_complessi_fig4`, `quota_complesso_maggiore_fig4_pct` (`null` se il comune manca nella figura) e i flag `ivp_coerente`, `ipi_coerente`, `icr_coerente` (true se figura e dossier coincidono) |
| `note` | string[] | Avvertenze specifiche del record (righe reintegrate dal PDF, incoerenze di ricalcolo) |

## Avvertenze

- Tutti i valori scalari sono tratti dal quadro sintetico della scheda e coincidono con il quadro sinottico (pag. 50-51), con la sintesi esecutiva e con le tabelle interne; i ricalcoli (somme delle tabelle, IVP e IPI ponderati, media, densità, quota) tornano per tutti i comuni tranne l'IVP di **Bultei** (dichiarato 3,395, ricalcolato 3,448: mantenuto il valore dichiarato).
- **Telti, Chiaramonti, Pozzomaggiore**: la riga `Alto` della tabella incendio era andata perduta nell'estrazione automatica (cambio pagina); è stata reintegrata leggendo il PDF originale (pag. 86, 95, 110) e la somma torna al totale comunale.
- **Le Figure 2-4 non sono allineate con i dossier**: valori diversi per la maggior parte dei comuni, tre comuni estranei ai 30 (Oniferi, Dualchi, Noragugume) in Fig. 2, Nuoro duplicato e Ardara assente in Fig. 4. Per il sito usare i valori del dossier; `confronto_figure` serve solo a documentare la discrepanza.
- Il documento non esplicita le soglie numeriche delle classi; vedi `indici-definizioni.json` per le soglie di legenda delle figure (non coerenti con i dossier) e per gli intervalli osservati.
- `nome_corrente` e `slug` sono le chiavi consigliate per il join con basi cartografiche (confini comunali ISTAT): le forme `Ala' Dei Sardi` e `Budduso'` del dossier non corrispondono alla toponomastica ufficiale.

## Idee di rappresentazione

1. **Mappa coropletica/a bolle dei 30 comuni**: bolla proporzionale a `sugherete_ha`, colore per `classe_ivp` (o `classe_incendio`, `classe_icr` con selettore); tooltip con i tre indici e il `profilo_integrato`.
2. **Ranking bar chart** ordinabile per `sugherete_ha`, `ivp`, `ipi`, `quota_medioalto_alto_pct`, `quota_complesso_maggiore_pct`, con barre colorate per classe.
3. **Matrice IVP × incendio × ICR filtrabile**: griglia classe IVP (righe) × classe incendio (colonne), celle con i comuni e faccette per `classe_icr`; clic su una cella → elenco comuni e profilo integrato.
4. **Scheda comune**: KPI (ha, peso %, IVP, IPI, ICR), barra impilata `distribuzione_incendio` (Basso→Alto), barra impilata `distribuzione_pedologica` per classe IVP, tabella complessi, elenco `indicazioni_operative`, testo `sintesi_esecutiva`.
5. **Scatter** IPI (x) × quota complesso maggiore (y), dimensione = ettari, colore = classe IVP: mostra i comuni "vocati, esposti e governabili" vs "frammentati".
