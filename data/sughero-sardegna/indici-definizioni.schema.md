# `indici-definizioni.json`

Definizione dei tre indici territoriali dello studio (IVP, IPI, ICR), classi e soglie, legenda dei profili a due e tre fattori usati nei dossier comunali, indicazioni operative ricorrenti e catalogo delle unità pedologiche riclassificate.

**Fonte.** Parte 2: par. 2.2 "Analisi territoriale" (pag. 19-21, definizioni), par. 3.2 (pag. 27-29, risultati per indice), par. 4.1-4.2 (pag. 35-37, interpretazione), Allegato I nota metodologica (pag. 50) e schede comunali (pag. 52-141), legende delle Figure 2 e 4 (pag. 28, 30).

## Struttura di `dati`

### `dati.indici[]` (3 oggetti: IVP, IPI, ICR)

| Campo | Tipo | Significato |
|---|---|---|
| `sigla` | string | `IVP`, `IPI`, `ICR` |
| `nome` | string | Nome completo |
| `domanda` | string | "Domanda a cui risponde" (tabella nota metodologica, pag. 50) |
| `definizione` | string | Definizione testuale dal par. 2.2 e interpretazione dal par. 4.1 |
| `metodo` | string | Come è calcolato l'indice comunale, ricostruito dalle tabelle dei dossier |
| `scala` | string | Intervallo dell'indice |
| `classi` | string[] | Nomi delle classi, ordinate dalla più favorevole/alta |
| `soglie_dichiarate` | oggetto | Soglie testuali presenti nel documento (solo legende Fig. 2 e Fig. 4) con `fonte` e avvertenza; per l'IPI nessuna soglia |
| `intervalli_osservati` | oggetto | Per ogni classe `{min, max, n_comuni}` dei valori dei 30 dossier (IVP: `ivp`; IPI: indice comunale, quota Medioalto+Alto e indice di classe nelle tabelle; ICR: quota complesso maggiore, n. complessi, densità per classe densità) |
| `punteggi_unita` | oggetto | (solo IVP) classe unità → punteggi osservati (`Alta` 4, `Media` 3, `Bassa` 2, `Molto bassa` 1) |
| `lettura_classi` | oggetto | Frase standard usata nei dossier per ciascuna classe |
| `output` | string | Colonna "Output" della nota metodologica |
| `pagine_fonte` | int[] | Pagine PDF |

### `dati.profili_ivp_x_incendio[]`
Combinazioni `classe_ivp` × `classe_incendio` → `profilo` (campo "Profilo IVP x incendio" del quadro sintetico) con l'elenco `comuni` (slug). 7 combinazioni osservate, 5 profili distinti.

### `dati.profili_integrati[]`
Combinazioni `classe_ivp` × `classe_incendio` × `classe_icr` → `profilo_integrato` con `comuni`. 17 combinazioni osservate, 7 profili distinti. Le combinazioni non presenti nei 30 comuni non hanno un profilo nel documento.

### `dati.profili_integrati_distinti[]`
I 7 profili con `n_comuni` e `comuni`, in ordine di frequenza.

### `dati.indicazioni_operative_ricorrenti[]`
Le 7 frasi delle "Indicazioni operative preliminari" con il numero di comuni in cui compaiono.

### `dati.unita_pedologiche[]`
Catalogo delle unità pedologiche (sigla Carta dei suoli della Sardegna) presenti sotto sughereta nei 30 comuni: `classe_ivp`, `punteggio_ivp`, `classe_capacita_uso` (insiemi osservati), `n_comuni`, `superficie_ha_30_comuni`; ordinato per superficie decrescente.

## Avvertenze

- **Le soglie numeriche delle classi non sono esplicitate nel testo.** Le uniche soglie scritte (legende Fig. 2: IVP ≥ 3,50 Alta; Fig. 4: ICR ≥ 70 Alta) **non riproducono** la classificazione dei dossier (Bitti IVP 3,317 è `Alta`; Bitti quota nucleo 74,37% è `Media`). Gli `intervalli_osservati` sono l'unica base coerente con il dataset: IVP Alta 3,257-3,987 / Media 2,569-2,988 / Bassa 2,000-2,480; quota complesso maggiore Alta 80,43-97,02 / Media 61,21-78,05 / Bassa 42,61-58,64 / Molto bassa 28,20-37,35; densità Bassa ≤0,43 / Media 0,51-1,47 / Alta 1,54-2,63 / Molto alta 3,18-3,96.
- Le classi elementari di pericolosità incendio (Basso…Alto) sono quelle della carta regionale (Piano AIB 2023-2025, All. 5); la classe comunale è quella dell'indice ponderato.
- La scala "da 1 a 5" indicata in Fig. 2 non trova riscontro nei dossier (punteggi 1-4).

## Idee di rappresentazione

1. **Legenda interattiva** a tre pannelli (IVP / IPI / ICR): domanda, definizione breve, scala con le fasce osservate per classe e i comuni posizionati sulla scala.
2. **Matrice dei profili integrati**: heatmap classe IVP × classe incendio con faccette ICR, cella colorata per profilo e conteggio comuni (fonte `profili_integrati`).
3. **Treemap/barre delle unità pedologiche** per superficie totale, colorate per `classe_ivp`, con tooltip sulle classi di capacità d'uso.
4. **Glossario** dei 7 profili integrati e delle 7 indicazioni operative, con link alle schede comunali che li adottano.
