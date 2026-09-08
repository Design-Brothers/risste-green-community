# Allegato II – Sistema Informativo Territoriale, cartografia e analisi biofisica

> Fonte: Green community UCAG 193 – Strategie territoriali integrate: gestione forestale e sviluppo sostenibile delle filiere locali (RISSTE, 2025). Pagine PDF 149–219. Estrazione automatica: i marcatori `<!-- pagina N -->` indicano la pagina fisica; le tabelle rimandano ai CSV in `../tables/`.

<!-- pagina 149 -->

#### Allegato II: Sistema Informativo Territoriale (SIT), cartografia e analisi biofisica dello spazio

rurale

#### Elaborazioni gis per la costruzione delle basi dati territoriali statistiche

La presente relazione descrive le attività di elaborazione GIS svolte nell’ambito del progetto GREEN COMMUNITIES Alta Gallura — UCAG 193, finalizzate alla costruzione di una base territoriale statistica utile alle successive analisi agro-forestali ed economiche. Il lavoro svolto ha finalità preliminari e conoscitive, con l’obiettivo di produrre dati omogenei e confrontabili a scala comunale e sovracomunale relativamente all’uso del suolo, alle caratteristiche pedologiche e alle loro reciproche relazioni spaziali. Le elaborazioni prodotte non hanno finalità catastali, topografiche o progettuali di dettaglio, ma costituiscono uno strumento di analisi territoriale a scala vasta.

#### Materiali e metodi

In questo capitolo vengono illustrati i dati territoriali e i flussi di lavoro GIS impiegati per produrre le elaborazioni statistiche e le tabelle finali utilizzate come base per le successive analisi del territorio.

### 2.1 Materiali utilizzati

Di seguito si riporta una descrizione dei dataset territoriali di partenza impiegati per le elaborazioni GIS sviluppate nell’ambito del lavoro.

#### 2.1.1 Carta dell’Uso del Suolo 2008

La Carta dell’Uso del Suolo 2008 costituisce l’ultimo aggiornamento disponibile del dataset regionale relativo all’uso del suolo. Si tratta di uno strato informativo vettoriale poligonale, in scala 1:25.000, rappresentante gli elementi territoriali secondo classificazione CORINE Land Cover, articolata fino al quarto e quinto livello di dettaglio.

*Figura 1 – Estratto della Carta dell’Uso del Suolo della Sardegna 2008 (CORINE Land Cover) utilizzata*

nelle elaborazioni GIS.

Il dato deriva dall’aggiornamento della Carta dell’Uso del Suolo 2003 ed è stato realizzato mediante fotointerpretazione, digitalizzazione a video e integrazione di differenti basi informative territoriali, tra cui ortofoto, dati AGEA e immagini satellitari Ikonos. La classificazione degli elementi è stata inoltre supportata da materiali ausiliari e da sopralluoghi distribuiti sul territorio regionale.

Il dataset è stato scaricato dal sito SardegnaGeoportale (https://webgis2.regione.sardegna.it/geonetwork/srv/ita/catalog.search#/metadata/R_SARDEG:WBM EW) nel sistema di riferimento Monte Mario / Italy zone 1 (EPSG 3003).

#### 2.1.2 Carta dei Suoli della Sardegna

La Carta dei Suoli della Sardegna è una cartografia tematica in scala 1:250.000 rappresentante le principali caratteristiche pedologiche del territorio regionale.

<!-- pagina 150 -->

Il dato deriva dalla Carta dei Suoli della Sardegna realizzata nel 1991 da Angelo Aru, Paolo Baldaccini e Andrea Vacca e costituisce una sintesi delle caratteristiche pedologiche regionali derivate in parte da rilievi di dettaglio. La cartografia è stata realizzata mediante l’analisi integrata delle principali caratteristiche territoriali, geomorfologiche e ambientali del territorio regionale.

*Figura 2 – Stralcio della Carta dei Suoli della Sardegna in scala 1:250.000, utilizzata come base*

cartografica pedologica per le elaborazioni GIS sviluppate nel presente lavoro.

La carta descrive i suoli attraverso informazioni relative a substrato, profilo, caratteri pedologici, limitazioni d’uso, capacità d’uso e principali fenomeni di degradazione.

Il dataset è stato scaricato dal Portale de Suolo (https://www.sardegnaportalesuolo.it/webgis/) nel sistema di riferimento WGS84 / UTM zone 32 N (EPSG 32632).

#### 2.1.3 Layer dei limiti amministrativi comunali

Il layer dei limiti amministrativi comunali è un dataset vettoriale rappresentante i confini amministrativi dell’intero territorio regionale della Sardegna.

Il dato deriva dal Database Geotopografico Regionale alla scala 1:10.000 (DBGT 10K) ed è stato realizzato a partire dalle entità geometriche contenute nella Carta Tecnica Regionale, successivamente aggiornate sulla base delle modifiche relative ai limiti amministrativi comunali.

<!-- pagina 151 -->

*Figura 3 – Esempi di rappresentazione dei limiti amministrativi comunali derivati dal Database*

Geotopografico Regionale (DBGT 10K) utilizzato nelle elaborazioni GIS.

Il dataset è stato scaricato dal portale SardegnaGeoportale (https://webgis2.regione.sardegna.it/geonetwork/srv/ita/catalog.search#/metadata/R_SARDEG:WBM EW) nel sistema di riferimento RDN2008 / UTM zone 32 N (EPSG 7791).

#### 2.1.4 Software QGIS

Le operazioni di elaborazione, gestione e analisi dei dati territoriali sono state sviluppate mediante il software GIS open source QGIS, versione 3.34.13-Prizren.

*Figura 4 – Logo del software open source QGIS*

Il software è stato utilizzato per la gestione dei layer vettoriali, la visualizzazione cartografica, le operazioni di geoprocessing e l’elaborazione delle informazioni territoriali necessarie alla costruzione delle basi dati statistiche del lavoro.

### 2.2 Metodi utilizzati

#### 2.2.1 Preparazione dei dati

Le elaborazioni GIS sono state sviluppate mediante una preliminare uniformazione dei dataset territoriali utilizzati. Tutti i layer sono stati convertiti nel sistema di riferimento EPSG 32632, utilizzato come sistema di riferimento del progetto. Successivamente, dal layer regionale dei limiti amministrativi comunali sono stati estratti i Comuni appartenenti all’Unione dei Comuni dell’Alta Gallura.

La Carta dell’Uso del Suolo 2008 è stata inoltre preliminarmente sottoposta a dissoluzione geometrica delle classi di uso del suolo, aggregando i poligoni appartenenti alla medesima classe tematica.

#### 2.2.2 Intersezione spaziale dei layer

Le elaborazioni territoriali sono state sviluppate mediante operazioni di intersezione spaziale tra i diversi layer. L’operazione di intersezione consente di generare un nuovo layer contenente esclusivamente le porzioni territoriali comuni agli strati intersecati, associando a ciascuna geometria risultante gli attributi informativi provenienti dai dataset di origine.

In una prima fase, il layer dei Comuni è stato intersecato con la Carta dell’Uso del Suolo 2008. Successivamente, il risultato ottenuto è stato a sua volta intersecato con la Carta dei Suoli della Sardegna.

Questa operazione ha permesso di ottenere una nuova geometria territoriale derivata, nella quale ciascun record risulta identificato univocamente dalla combinazione tra:

Comune;

Classe di uso del suolo;

Unità pedologica.

Il risultato finale rappresenta pertanto il primo elaborato derivato dall’intersezione completa dei tre dataset.

L’utilizzo della procedura di intersezione spaziale tra tutti e tre i dataset di partenza ha consentito di costruire una base territoriale di riferimento, costituita esclusivamente dalle porzioni cartografiche condivise dai diversi strati di partenza. In corrispondenza della linea di costa i layer utilizzati presentano localmente lievi differenze di estensione geometrica dovute a differenti scale cartografiche, differenti sistemi di riferimento di origine e differenti modalità di restituzione dei dati. Il processo di intersezione spaziale ha pertanto escluso automaticamente tali limitate porzioni non coincidenti, mantenendo nelle elaborazioni esclusivamente le aree contemporaneamente presenti in tutti i layer utilizzati.

<!-- pagina 152 -->

L’estensione territoriale derivata dall’intersezione tra i tre dataset è stata utilizzata come superficie di riferimento anche per le successive elaborazioni relative alle sole classi di uso del suolo e alle sole unità pedologiche.

A tal fine, i layer originari della Carta dell’Uso del Suolo 2008 e della Carta dei Suoli della Sardegna sono stati preliminarmente ritagliati utilizzando l’estensione territoriale derivata dall’elaborazione precedente al fine di garantire la perfetta coerenza statistica, l'omogeneità spaziale e la quadratura geometrica delle superfici tra tutti gli elaborati finali, evitando discrepanze nei totali comunali.

#### 2.2.3 Calcolo delle superfici

Le superfici sono state calcolate mediante la funzione “$area” disponibile nel calcolatore di campi di QGIS, che restituisce l’area ellissoidica delle geometrie sulla base delle impostazioni geodetiche definite nel progetto GIS.

Per il layer derivato dall’intersezione tra Comuni, Carta dell’Uso del Suolo e Carta dei Suoli, il risultato finale dell’elaborazione è costituito da geometrie multipart, nelle quali ciascun record rappresenta l’insieme dei poligoni aventi la medesima combinazione di:

Comune;

Classe di uso del suolo;

Unità pedologica.

Analogamente, per le elaborazioni relative alle sole classi di uso del suolo e alle sole unità pedologiche, ciascun record rappresenta l’insieme dei poligoni aventi rispettivamente la medesima combinazione tra:

Comune e classe di uso del suolo;

Comune e unità pedologica.

I valori di superficie associati ai record risultano riferiti all’intera estensione territoriale rappresentata dalle rispettive geometrie multipart.

Le tre tabelle degli attributi associate ai layer elaborati sono state successivamente esportate in formato CSV ed elaborate in ambiente Microsoft Excel mediante operazioni di organizzazione, controllo e predisposizione dei dati, costituendo gli elaborati statistici finali utilizzati nelle successive analisi territoriali.

<!-- pagina 153 -->

Risultati Le elaborazioni GIS sviluppate hanno consentito la costruzione di tre elaborati tabellari derivati dalle operazioni di intersezione spaziale descritte nel capitolo precedente, ovvero: Comuni intersezione UdS-Pedologia; Comuni intersezione UdS; Comuni intersezione Pedologia.

### 3.1 Comuni intersezione UdS-Pedologia

La tabella “Comuni intersezione UdS-Pedologia” rappresenta l’elaborato derivato dall’intersezione spaziale tra layer comunale, Carta dell’Uso del Suolo 2008 e Carta dei Suoli della Sardegna. La tabella contiene, per ciascuna combinazione territoriale individuata, sia informazioni relative alle classi di uso del suolo sia informazioni di carattere pedologico e territoriale derivanti dalla Carta dei Suoli della Sardegna, associate alla relativa superficie territoriale e alla relativa incidenza percentuale sul territorio comunale considerato.

| Campo | Descrizione |
|---|---|
| Comune | Comune di appartenenza del poligono |
| Codice UdS | Codice identificativo della classe di uso del suolo |
| Descrizione UdS | Descrizione della classe di uso del suolo |
| Unità cartografica | Codice dell’unità cartografica pedologica |
| Unità pedologica | Codice identificativo dell’unità pedologica |
| Substrato | Descrizione del substrato geologico prevalente |
| Morfologia | Descrizione morfologica dell’area |
| Descrizione pedologica | Descrizione sintetica delle caratteristiche pedologiche |
| Tassonomia | Classificazione tassonomica dei suoli |
| Classi | Classe di capacità d’uso del suolo |
| Copertura | Descrizione della copertura territoriale |
| Limitazione | Principali limitazioni territoriali e pedologiche |
| Attitudine | Indicazioni di attitudine e uso territoriale |
| Superficie [ha] | Superficie territoriale espressa in ettari |
| Superficie [%] | Percentuale della superficie rispetto al territorio comunale |

<!-- tabella: tables/p153-t0.csv (sparse) -->

*Tabella 1 – Struttura dei campi presenti nell’elaborato “Comuni intersezione UdS-Pedologia”.*

### 3.2 Comuni intersezione UdS

La tabella “Comuni intersezione UdS” rappresenta l’elaborato derivato dall’intersezione spaziale tra layer comunale e Carta dell’Uso del Suolo 2008. La tabella contiene, per ciascuna combinazione territoriale individuata, informazioni relative alle classi di uso del suolo, associate alla relativa superficie territoriale e alla relativa incidenza percentuale sul territorio comunale considerato.

| Campo | Descrizione |
|---|---|
| Comune | Comune di appartenenza del poligono |
| Codice UdS | Codice identificativo della classe di uso del suolo |
| Descrizione UdS | Descrizione della classe di uso del suolo |

<!-- tabella: tables/p153-t1.csv (sparse) -->

<!-- pagina 154 -->

| Superficie [ha] | Superficie territoriale espressa in ettari |
|---|---|
| Superficie [%] | Percentuale della superficie rispetto al territorio comunale |

<!-- tabella: tables/p154-t0.csv (ok) -->

*Tabella 2 – Struttura dei campi presenti nell’elaborato “Comuni intersezione UdS”.*

### 3.3 Comuni intersezione Pedologia

La tabella “Comuni intersezione Pedologia” rappresenta l’elaborato derivato dall’intersezione spaziale tra layer comunale e Carta dei Suoli della Sardegna. La tabella contiene, per ciascuna combinazione territoriale individuata, informazioni di carattere pedologico e territoriale derivanti dalla Carta dei Suoli della Sardegna, associate alla relativa superficie territoriale e alla relativa incidenza percentuale sul territorio comunale considerato.

| Campo | Descrizione |
|---|---|
| Comune | Comune di appartenenza del poligono |
| Unità cartografica | Codice dell’unità cartografica pedologica |
| Unità pedologica | Codice identificativo dell’unità pedologica |
| Substrato | Descrizione del substrato geologico prevalente |
| Morfologia | Descrizione morfologica dell’area |
| Descrizione pedologica | Descrizione sintetica delle caratteristiche pedologiche |
| Tassonomia | Classificazione tassonomica dei suoli |
| Classi | Classe di capacità d’uso del suolo |
| Copertura | Descrizione della copertura territoriale |
| Limitazione | Principali limitazioni territoriali e pedologiche |
| Attitudine | Indicazioni di attitudine e uso territoriale |
| Superficie [ha] | Superficie territoriale espressa in ettari |
| Superficie [%] | Percentuale della superficie rispetto al territorio comunale |

<!-- tabella: tables/p154-t1.csv (sparse) -->

*Tabella 3 – Struttura dei campi presenti nell’elaborato “Comuni intersezione Pedologia”.*

<!-- pagina 155 -->

#### Considerazioni finali

Le elaborazioni sviluppate hanno consentito di costruire una base territoriale omogenea e statisticamente confrontabile tra tutti i layer utilizzati, mediante l’uso di procedure di intersezione spaziale applicate ai diversi dataset territoriali di partenza. Le limitate porzioni territoriali escluse automaticamente dalle operazioni di intersezione risultano riconducibili a marginali differenze di rappresentazione della linea di costa tra i diversi strati informativi. Tali superfici hanno un’estensione ridottissima rispetto alla superficie dei singoli Comuni e dell’intero territorio dell’Unione dei Comuni dell’Alta Gallura, risultando trascurabili ai fini delle elaborazioni sviluppate e non influenzando in maniera significativa i risultati ottenuti, anche in considerazione della limitata rilevanza di tali aree rispetto alle finalità agro-forestali, territoriali ed economiche del lavoro complessivo.

È importante sottolineare che i dataset territoriali utilizzati derivano da fonti cartografiche differenti e sono stati prodotti in epoche, scale cartografiche e sistemi di riferimento differenti. Inoltre le operazioni di trasformazione dei sistemi di riferimento sono state effettuate mediante gli algoritmi disponibili nel software QGIS. Tali condizioni determinano inevitabili differenze geometriche tra i diversi layer cartografici. Di conseguenza, le operazioni di intersezione spaziale possono generare localmente superfici che non rappresentano in maniera perfettamente coincidente la reale disposizione territoriale degli elementi cartografici di partenza.

La completa verifica e correzione manuale di tali discrepanze risulterebbe estremamente complessa in relazione all’estensione territoriale del lavoro e non proporzionata rispetto alle finalità statistiche, conoscitive e territoriali delle elaborazioni sviluppate.

Inoltre la diversa scala di produzione delle cartografie (1:25.000 per la Carta dell’Uso del Suolo 2008 e 1:250.000 per la Carta dei Suoli della Sardegna) determina differenti livelli di dettaglio del dato cartografico. I dataset utilizzati costituiscono tuttavia le principali cartografie disponibili e utilizzabili per questo tipo di elaborazioni territoriali, non essendo disponibili basi cartografiche omogenee di maggiore dettaglio per l’intero territorio analizzato.

Le elaborazioni sviluppate risultano pertanto adeguate alle finalità statistiche, conoscitive e territoriali del progetto, costituendo una base informativa coerente e utilizzabile per le successive analisi agro-forestali, pedologiche e territoriali previste dal lavoro.

<!-- pagina 156 -->

#### Schede comunali preliminari

## 1. Comune di Aggius

### 1.1 Inquadramento sintetico

Aggius presenta un assetto territoriale a forte componente rurale, forestale, seminaturale e agro-silvopastorale. La scheda evidenzia una buona rilevanza per la filiera bosco-sughero, ma anche fragilità pedologiche diffuse che impongono cautela per eventuali utilizzi zootecnici estensivi.

### 1.2 Sintesi dell’uso del suolo

Le principali classi di uso del suolo sono:

| Classe | Superficie | Incidenza |
|---|---|---|
| Prati artificiali | 1.415 ha | 17,0% |
| Macchia mediterranea | 1.258 ha | 15,1% |
| Bosco di latifoglie | 958 ha | 11,5% |
| Gariga | 895 ha | 10,7% |
| Sugherete | 574 ha | 6,9% |
| Aree a pascolo naturale | 535 ha | 6,4% |

<!-- tabella: tables/p156-t0.csv (ok) -->

L’assetto comunale indica una matrice agroforestale significativa, con presenza documentata di sugherete, boschi, macchia, gariga, pascoli e prati artificiali.

### 1.3 Sintesi pedologica

Le principali unità pedologiche sono:

| Unità | Superficie | Incidenza |
|---|---|---|
| C2 | 4.732 ha | 56,7% |
| C1 | 1.941 ha | 23,3% |
| B2 | 1.565 ha | 18,8% |
| B3 | 82 ha | 1,0% |

<!-- tabella: tables/p156-t1.csv (ok) -->

Prevalgono suoli su rocce intrusive e metamorfiti paleozoiche, spesso poco o mediamente profondi, con rocciosità, pietrosità, eccesso di scheletro e forte pericolo di erosione. Le unità C1 e B2 richiamano in particolare la necessità di conservazione della vegetazione naturale e riduzione o eliminazione del pascolamento nei contesti più fragili.

### 1.4 Lettura della matrice pedologia × uso del suolo

Le combinazioni principali sono:

| Combinazione | Superficie | Incidenza |
|---|---|---|
| Prati artificiali su C2 | 805 ha | 9,6% |
| Macchia mediterranea su C2 | 644 ha | 7,7% |
| Prati artificiali su B2 | 522 ha | 6,3% |
| Gariga su C2 | 490 ha | 5,9% |
| Bosco di latifoglie su C2 | 483 ha | 5,8% |

<!-- tabella: tables/p156-t2.csv (ok) -->

Le sugherete ricadono soprattutto su C2, C1 e B2. Ciò suggerisce una possibile valorizzazione forestale, ma con forte attenzione al rischio erosivo e alla funzione protettiva delle coperture.

<!-- pagina 157 -->

### 1.5 Implicazioni per la filiera bosco-sughero

Aggius presenta un interesse preliminare medio-alto per la filiera bosco-sughero, con circa 574 ha di sugherete. La presenza su unità C2 e B2 consente di ipotizzare approfondimenti su gestione sostenibile e recupero forestale; la quota su C1 richiede invece prudenza, privilegiando funzioni protettive.

### 1.6 Implicazioni per la filiera suinicola agroforestale

Il Comune può essere considerato da approfondire solo in chiave pilota e controllata. Prati artificiali, pascoli naturali e alcune superfici agroforestali costituiscono potenziali ambiti di verifica, ma le limitazioni pedologiche sono rilevanti. Le aree su C1 dovrebbero essere considerate tendenzialmente non prioritarie per usi suinicoli.

### 1.7 Criticità e condizioni di attenzione

Le principali criticità riguardano erosione, rocciosità, pietrosità, suoli poco profondi, vulnerabilità della copertura vegetale e compatibilità del pascolo con unità pedologiche fragili.

### 1.8 Opportunità e approfondimenti successivi

Prioritari: mappatura aggiornata delle sugherete, stato vegetativo e fitosanitario, proprietà, accessibilità, aziende interessate, vincoli, habitat, fauna e verifica di eventuali aree pilota. Valutazione preliminare: vocazione sughericola medio-alta; interesse suinicolo medio ma solo sperimentale; fragilità pedologica alta.

<!-- pagina 158 -->

## 2. Comune di Aglientu

### 2.1 Inquadramento sintetico

Aglientu presenta una forte componente seminaturale e agro-pastorale, con ampia presenza di macchia, gariga, prati artificiali, boschi e pascoli. La vocazione sughericola appare più limitata rispetto ad altri Comuni interni, mentre il tema suinicolo può essere valutato solo con molta cautela, soprattutto per l’elevata diffusione di unità C2 e C1.

### 2.2 Sintesi dell’uso del suolo

| Classe | Superficie | Incidenza |
|---|---|---|
| Macchia mediterranea | 3.214 ha | 21,7% |
| Gariga | 3.166 ha | 21,3% |
| Prati artificiali | 2.494 ha | 16,8% |
| Bosco di latifoglie | 1.120 ha | 7,6% |
| Aree a pascolo naturale | 951 ha | 6,4% |
| Aree a ricolonizzazione naturale | 770 ha | 5,2% |

<!-- tabella: tables/p158-t0.csv (ok) -->

Il territorio è dominato da coperture naturali e seminaturali, con una componente agro-pastorale rilevante.

### 2.3 Sintesi pedologica

| Unità | Superficie | Incidenza |
|---|---|---|
| C2 | 10.902 ha | 73,5% |
| C1 | 2.550 ha | 17,2% |
| M1 | 564 ha | 3,8% |
| I1 | 425 ha | 2,9% |
| L1 | 368 ha | 2,5% |

<!-- tabella: tables/p158-t1.csv (ok) -->

La grande prevalenza di C2 segnala suoli su rocce intrusive, da poco a mediamente profondi, con rocciosità, pietrosità e forte pericolo di erosione. La presenza di C1 aumenta la quota di aree a funzione protettiva. M1, I1 e L1 indicano situazioni più specifiche: sabbie eoliche, alluvioni o aree pianeggianti, da valutare separatamente.

### 2.4 Lettura della matrice pedologia × uso del suolo

| Combinazione | Superficie | Incidenza |
|---|---|---|
| Gariga su C2 | 2.402 ha | 16,2% |
| Macchia mediterranea su C2 | 2.270 ha | 15,3% |
| Prati artificiali su C2 | 2.051 ha | 13,8% |
| Bosco di latifoglie su C2 | 832 ha | 5,6% |
| Macchia mediterranea su C1 | 770 ha | 5,2% |

<!-- tabella: tables/p158-t2.csv (ok) -->

La matrice evidenzia che le principali superfici naturali e seminaturali insistono su C2 e C1. Questo rafforza la necessità di leggere il territorio come mosaico da gestire in equilibrio tra conservazione, prevenzione incendi, pascolo regolato e manutenzione della copertura vegetale.

<!-- pagina 159 -->

### 2.5 Implicazioni per la filiera bosco-sughero

Le sugherete risultano presenti ma limitate, circa 321 ha. Aglientu non appare, in questa fase, tra i Comuni più forti per la filiera produttiva del sughero, ma può avere interesse per la gestione forestale multifunzionale, il recupero di superfici seminaturali e la prevenzione incendi.

### 2.6 Implicazioni per la filiera suinicola agroforestale

La presenza di prati artificiali e pascoli naturali rende il Comune meritevole di approfondimento, ma l’elevata incidenza di C2 e C1 richiede forte prudenza. Eventuali ipotesi suinicole dovrebbero concentrarsi su superfici aziendali effettivamente gestibili, recintabili, con suoli meno fragili e fuori dagli ambiti di maggiore sensibilità.

### 2.7 Criticità e condizioni di attenzione

Criticità principali: ampie superfici di gariga e macchia su suoli con rischio erosivo, possibile fragilità della copertura vegetale, rischio di degrado da carichi non controllati, necessità di verifica dei vincoli ambientali e costieri.

### 2.8 Opportunità e approfondimenti successivi

Aglientu può essere approfondito per gestione del mosaico macchia-gariga-pascolo, prevenzione incendi, verifica di aree agro-pastorali controllate e connessione con il mercato turistico costiero. Valutazione preliminare: vocazione sughericola medio-bassa; interesse suinicolo medio ma prudenziale; fragilità pedologica medio-alta.

## 3. Comune di Badesi

### 3.1 Inquadramento sintetico

Badesi presenta un profilo diverso rispetto ai Comuni più interni: maggiore presenza di seminativi, vigneti, macchia, gariga e boschi, ma assenza di sugherete rilevata nelle tabelle. Il ruolo del Comune appare più connesso a filiere agricole, paesaggio rurale-costiero e possibili mercati di sbocco, piuttosto che alla produzione primaria di sughero.

### 3.2 Sintesi dell’uso del suolo

| Classe | Superficie | Incidenza |
|---|---|---|
| Seminativi semplici e colture orticole | 437 ha | 14,2% |
| Macchia mediterranea | 417 ha | 13,6% |
| Gariga | 373 ha | 12,1% |
| Vigneti | 357 ha | 11,6% |
| Bosco di latifoglie | 262 ha | 8,5% |
| Prati artificiali | 209 ha | 6,8% |

<!-- tabella: tables/p159-t0.csv (ok) -->

Badesi mostra una matrice agricola e seminaturale articolata, con presenza significativa di vigneti, seminativi e coperture mediterranee.

<!-- pagina 160 -->

### 3.3 Sintesi pedologica

| Unità | Superficie | Incidenza |
|---|---|---|
| M1 | 1.538 ha | 50,1% |
| C2 | 1.202 ha | 39,1% |
| L1 | 260 ha | 8,5% |
| L2 | 70 ha | 2,3% |

<!-- tabella: tables/p160-t0.csv (ok) -->

La prevalenza di M1 indica suoli su sabbie eoliche, profondi ma con drenaggio eccessivo e forte pericolo di erosione. C2 introduce le limitazioni tipiche delle rocce intrusive. L1 e L2 individuano aree più pianeggianti/alluvionali, con possibile attitudine agricola ma anche limiti legati a drenaggio o inondazione.

### 3.4 Lettura della matrice pedologia × uso del suolo

| Combinazione | Superficie | Incidenza |
|---|---|---|
| Macchia mediterranea su C2 | 377 ha | 12,3% |
| Gariga su C2 | 359 ha | 11,7% |
| Vigneti su M1 | 350 ha | 11,4% |
| Seminativi su L1 | 221 ha | 7,2% |
| Bosco di latifoglie su C2 | 184 ha | 6,0% |

<!-- tabella: tables/p160-t1.csv (ok) -->

La matrice indica una distinzione tra ambiti agricoli su M1/L1 e superfici seminaturali su C2. La componente agricola appare più rilevante rispetto alla filiera forestale.

### 3.5 Implicazioni per la filiera bosco-sughero

Le tabelle non evidenziano sugherete. Badesi non deve quindi essere presentato come Comune produttivo sughericolo, almeno sulla base dei dati disponibili. Può però contribuire alla strategia territoriale attraverso paesaggio rurale, turismo, agricoltura, viticoltura e possibili mercati di valorizzazione.

### 3.6 Implicazioni per la filiera suinicola agroforestale

Il potenziale suinicolo è da valutare con cautela. Le superfici agricole e prative possono offrire spazi di approfondimento, ma M1 presenta rischio erosivo e drenaggio eccessivo. Eventuali iniziative dovranno essere aziendali, controllate, con attenzione a suoli sabbiosi, disponibilità idrica e compatibilità con il contesto turistico-costiero.

### 3.7 Criticità e condizioni di attenzione

Criticità: erosione su sabbie eoliche, pressione costiera/turistica, compatibilità paesaggistica, limitata presenza forestale sughericola, necessità di verifiche ambientali e urbanistiche.

### 3.8 Opportunità e approfondimenti successivi

Badesi può essere approfondito come Comune di collegamento tra filiere rurali e mercato turisticocostiero, più che come ambito primario bosco-sughero. Interessanti le connessioni con trasformazione, vendita diretta, ristorazione, turismo rurale e prodotti locali. Valutazione preliminare: vocazione sughericola bassa; interesse suinicolo medio-basso e aziendale; ruolo potenziale commerciale/turistico.

<!-- pagina 161 -->

## 4. Comune di Bortigiadas

### 4.1 Inquadramento sintetico

Bortigiadas presenta una forte componente forestale, con boschi di latifoglie, macchia, gariga e boschi misti. La presenza di sugherete è contenuta, ma il Comune appare rilevante per gestione forestale, protezione del suolo e recupero del mosaico agroforestale.

### 4.2 Sintesi dell’uso del suolo

| Classe | Superficie | Incidenza |
|---|---|---|
| Bosco di latifoglie | 2.204 ha | 28,9% |
| Macchia mediterranea | 1.114 ha | 14,6% |
| Gariga | 878 ha | 11,5% |
| Prati artificiali | 652 ha | 8,5% |
| Boschi misti di conifere e latifoglie | 498 ha | 6,5% |
| Seminativi semplici e colture orticole | 459 ha | 6,0% |

<!-- tabella: tables/p161-t0.csv (ok) -->

L’assetto è nettamente forestale-seminaturale, con componente agricola/pascoliva secondaria.

### 4.3 Sintesi pedologica

| Unità | Superficie | Incidenza |
|---|---|---|
| C1 | 4.430 ha | 58,1% |
| C2 | 1.971 ha | 25,8% |
| I1 | 426 ha | 5,6% |
| G1 | 356 ha | 4,7% |
| B1 | 161 ha | 2,1% |

<!-- tabella: tables/p161-t1.csv (ok) -->

La forte incidenza di C1 segnala un territorio pedologicamente fragile, con aree aspre, pendenze elevate, rocciosità, pietrosità, scarsa profondità e forte pericolo di erosione. B1 presenta analoghe limitazioni su metamorfiti. I1 e G1 introducono condizioni più specifiche, ma non dominanti.

### 4.4 Lettura della matrice pedologia × uso del suolo

| Combinazione | Superficie | Incidenza |
|---|---|---|
| Bosco di latifoglie su C1 | 1.489 ha | 19,5% |
| Macchia mediterranea su C1 | 690 ha | 9,0% |
| Gariga su C1 | 646 ha | 8,5% |
| Bosco di latifoglie su C2 | 571 ha | 7,5% |
| Boschi misti su C1 | 355 ha | 4,7% |

<!-- tabella: tables/p161-t2.csv (ok) -->

La matrice conferma la prevalenza di coperture forestali e seminaturali su unità pedologiche fragili. Il mantenimento della copertura vegetale ha qui una funzione protettiva centrale.

### 4.5 Implicazioni per la filiera bosco-sughero

Le sugherete ammontano a circa 116 ha. La filiera sughericola appare meno rilevante in termini quantitativi rispetto a Calangianus, Tempio o Luras, ma il Comune può avere un ruolo nella gestione forestale sostenibile, nella manutenzione del paesaggio e nella prevenzione del degrado.

<!-- pagina 162 -->

### 4.6 Implicazioni per la filiera suinicola agroforestale

L’interesse per la filiera suinicola è limitato e da trattare con forte cautela. L’elevata presenza di C1 rende poco opportuna una pressione zootecnica diffusa. Eventuali verifiche dovrebbero concentrarsi solo su aree agricole o prative più stabili, fuori dagli ambiti boschivi fragili.

### 4.7 Criticità e condizioni di attenzione

Criticità elevate: pendenza, erosione, rocciosità, suoli superficiali, coperture forestali su unità fragili, rischio di alterazione della funzione protettiva.

### 4.8 Opportunità e approfondimenti successivi

Prioritari: gestione forestale protettiva, recupero e infittimento della vegetazione naturale, prevenzione incendi, verifica puntuale delle piccole aree sughericole, esclusione delle aree più fragili da usi zootecnici intensivi. Valutazione preliminare: vocazione forestale alta; vocazione sughericola medio-bassa; interesse suinicolo basso o solo molto localizzato; fragilità alta.

## 5. Comune di Calangianus

### 5.1 Inquadramento sintetico

Calangianus emerge come uno dei Comuni chiave per la filiera bosco-sughero. Presenta la maggiore superficie di sugherete tra i Comuni analizzati, oltre a boschi di latifoglie, macchia e gariga. Tuttavia, la forte presenza di C1 impone una lettura molto prudente della componente produttiva e zootecnica.

### 5.2 Sintesi dell’uso del suolo

| Classe | Superficie | Incidenza |
|---|---|---|
| Bosco di latifoglie | 2.745 ha | 21,7% |
| Macchia mediterranea | 2.070 ha | 16,4% |
| Sugherete | 2.014 ha | 15,9% |
| Gariga | 1.412 ha | 11,2% |
| Vegetazione rada | 1.290 ha | 10,2% |
| Seminativi in aree non irrigue | 663 ha | 5,2% |

<!-- tabella: tables/p162-t0.csv (ok) -->

La componente forestale e sughericola è molto rilevante. Calangianus deve essere considerato un Comune centrale per il tema sughero.

### 5.3 Sintesi pedologica

| Unità | Superficie | Incidenza |
|---|---|---|
| C1 | 8.076 ha | 63,8% |
| C2 | 3.471 ha | 27,4% |
| C5 | 710 ha | 5,6% |
| C3 | 351 ha | 2,8% |

<!-- tabella: tables/p162-t1.csv (ok) -->

La prevalenza di C1 indica ampie superfici con forti limitazioni: pendenze, rocciosità, pietrosità, scarsa profondità, erosione. C5 e C3 possono indicare ambiti dove approfondire forestazione, infittimento e gestione razionale della vegetazione naturale.

<!-- pagina 163 -->

### 5.4 Lettura della matrice pedologia × uso del suolo

| Combinazione | Superficie | Incidenza |
|---|---|---|
| Bosco di latifoglie su C1 | 2.038 ha | 16,1% |
| Macchia mediterranea su C1 | 1.640 ha | 13,0% |
| Sugherete su C1 | 1.166 ha | 9,2% |
| Gariga su C1 | 1.138 ha | 9,0% |
| Vegetazione rada su C1 | 1.082 ha | 8,5% |

<!-- tabella: tables/p163-t0.csv (ok) -->

La matrice mostra che una quota importante delle sugherete e delle coperture forestali insiste su C1. Questo non riduce l’importanza del Comune, ma suggerisce che la valorizzazione debba essere fondata su gestione sostenibile, protezione del suolo e miglioramento forestale, non su intensificazione.

### 5.5 Implicazioni per la filiera bosco-sughero

Calangianus è un Comune prioritario per la filiera sughericola. Le circa 2.014 ha di sugherete indicano una rilevanza territoriale elevata. Le successive fasi dovranno verificare stato vegetativo, turni di decortica, qualità del sughero, proprietà, accessibilità, operatori e connessioni con trasformazione e distretto produttivo esistente.

### 5.6 Implicazioni per la filiera suinicola agroforestale

Il suino agroforestale deve essere trattato come tema secondario e molto controllato. La presenza di vaste aree forestali e sugherete non implica automaticamente idoneità al pascolo suino. Al contrario, la diffusione di C1 e vegetazione rada rende prioritaria la tutela del suolo e della rinnovazione.

### 5.7 Criticità e condizioni di attenzione

Criticità: sugherete su suoli fragili, rischio erosione, vegetazione rada su C1, necessità di protezione della rinnovazione, possibile conflitto tra funzione produttiva e funzione protettiva.

### 5.8 Opportunità e approfondimenti successivi

Calangianus è prioritario per piano di gestione delle sugherete, mappatura di dettaglio, distretto rurale del sughero, formazione operatori, certificazioni, filiera corta e integrazione con artigianato, bioedilizia, design e turismo esperienziale. Valutazione preliminare: vocazione sughericola alta; priorità forestale alta; interesse suinicolo bassomedio solo come sperimentazione controllata; fragilità alta.

## 6. Comune di Luogosanto

### 6.1 Inquadramento sintetico

Luogosanto presenta una matrice agroforestale molto rilevante, con macchia mediterranea, prati artificiali, boschi, gariga, aree agroforestali e pascoli. È un Comune interessante sia per la gestione forestale sia per eventuali verifiche su modelli agro-silvo-pastorali controllati.

### 6.2 Sintesi dell’uso del suolo

| Classe | Superficie | Incidenza |
|---|---|---|
| Macchia mediterranea | 3.487 ha | 25,8% |
| Prati artificiali | 2.310 ha | 17,1% |
| Bosco di latifoglie | 2.253 ha | 16,7% |

<!-- tabella: tables/p163-t1.csv (ok) -->

<!-- pagina 164 -->

| Classe | Superficie | Incidenza |
|---|---|---|
| Gariga | 1.252 ha | 9,3% |
| Aree agroforestali | 914 ha | 6,8% |
| Aree a pascolo naturale | 562 ha | 4,2% |

<!-- tabella: tables/p164-t0.csv (ok) -->

Il Comune mostra una forte integrazione tra coperture forestali/seminaturali e superfici agro-pastorali.

### 6.3 Sintesi pedologica

| Unità | Superficie | Incidenza |
|---|---|---|
| C2 | 11.359 ha | 84,1% |
| C1 | 1.982 ha | 14,7% |
| B2 | 79 ha | 0,6% |
| L1 | 72 ha | 0,5% |

<!-- tabella: tables/p164-t1.csv (ok) -->

Prevale nettamente C2, con suoli su rocce intrusive, da poco a mediamente profondi, permeabili, ma con rocciosità, pietrosità, scheletro e forte pericolo di erosione a tratti. La quota C1 rappresenta gli ambiti più fragili.

### 6.4 Lettura della matrice pedologia × uso del suolo

| Combinazione | Superficie | Incidenza |
|---|---|---|
| Macchia mediterranea su C2 | 2.699 ha | 20,0% |
| Prati artificiali su C2 | 2.186 ha | 16,2% |
| Bosco di latifoglie su C2 | 1.956 ha | 14,5% |
| Gariga su C2 | 985 ha | 7,3% |
| Aree agroforestali su C2 | 870 ha | 6,4% |

<!-- tabella: tables/p164-t2.csv (ok) -->

La matrice mostra un forte mosaico agroforestale su C2. Questo rende il Comune interessante per valutazioni integrate, purché le limitazioni pedologiche siano considerate nella progettazione.

### 6.5 Implicazioni per la filiera bosco-sughero

Le sugherete risultano presenti per circa 449 ha. Luogosanto ha un interesse preliminare medio per la filiera sughero, ma soprattutto per gestione agroforestale, continuità ecologica, prevenzione incendi e possibili interventi multifunzionali.

### 6.6 Implicazioni per la filiera suinicola agroforestale

Luogosanto è uno dei Comuni più interessanti da approfondire per una possibile sperimentazione suinicola agroforestale controllata, grazie alla presenza combinata di prati artificiali, aree agroforestali e pascoli naturali. Tuttavia, la prevalenza di C2 impone bassi carichi, rotazioni, monitoraggio del suolo e protezione della copertura vegetale.

### 6.7 Criticità e condizioni di attenzione

Criticità: erosione a tratti su C2, presenza di C1, possibile vulnerabilità della macchia e della gariga, necessità di verificare accessibilità, proprietà, aziende e disponibilità idrica.

<!-- pagina 165 -->

### 6.8 Opportunità e approfondimenti successivi

Luogosanto merita approfondimenti su aree pilota agroforestali, integrazione tra gestione del sottobosco e allevamento controllato, recupero di superfici rurali, prevenzione incendi e connessione con prodotti locali. Valutazione preliminare: vocazione agroforestale alta; vocazione sughericola media; interesse suinicolo medio-alto da verificare; fragilità medio-alta.

## 7. Comune di Luras

### 7.1 Inquadramento sintetico

Luras presenta un equilibrio tra seminativi, macchia, gariga, prati artificiali, boschi, pascoli e sugherete. È un Comune interessante per filiera sughero e per eventuali approfondimenti agro-silvo-pastorali, ma con limitazioni pedologiche ricorrenti.

### 7.2 Sintesi dell’uso del suolo

| Classe | Superficie | Incidenza |
|---|---|---|
| Seminativi in aree non irrigue | 1.340 ha | 15,3% |
| Macchia mediterranea | 1.271 ha | 14,5% |
| Gariga | 1.119 ha | 12,8% |
| Prati artificiali | 940 ha | 10,7% |
| Bosco di latifoglie | 865 ha | 9,9% |
| Aree a pascolo naturale | 854 ha | 9,8% |

<!-- tabella: tables/p165-t0.csv (ok) -->

Le sugherete ammontano a circa 645 ha, valore significativo nel quadro comunale.

### 7.3 Sintesi pedologica

| Unità | Superficie | Incidenza |
|---|---|---|
| C2 | 6.590 ha | 75,3% |
| C1 | 1.089 ha | 12,5% |
| B2 | 622 ha | 7,1% |
| C3 | 358 ha | 4,1% |
| L1 | 59 ha | 0,7% |

<!-- tabella: tables/p165-t1.csv (ok) -->

Prevale C2, con limitazioni ricorrenti legate a pietrosità, rocciosità, scarsa profondità e pericolo di erosione. C3 può rappresentare ambiti da approfondire per uso più razionale della vegetazione naturale e pascolo regimato.

#### Lettura della matrice pedologia × uso del suolo

| Combinazione | Superficie | Incidenza |
|---|---|---|
| Seminativi non irrigui su C2 | 1.244 ha | 14,2% |
| Prati artificiali su C2 | 808 ha | 9,2% |
| Gariga su C2 | 752 ha | 8,6% |
| Macchia mediterranea su C2 | 737 ha | 8,4% |
| Pascolo naturale su C2 | 710 ha | 8,1% |

<!-- tabella: tables/p165-t2.csv (ok) -->

<!-- pagina 166 -->

La matrice evidenzia un uso agricolo-pastorale consistente su C2, da leggere con cautela in termini di carichi, erosione e mantenimento della copertura vegetale.

### 7.5 Implicazioni per la filiera bosco-sughero

Luras presenta un interesse medio-alto per la filiera sughericola. Le sugherete sono significative e inserite in un mosaico agricolo, pastorale e forestale. Sarà necessario distinguere aree produttive, protettive e da recuperare, verificando accessibilità e gestione.

### 7.6 Implicazioni per la filiera suinicola agroforestale

Luras può essere approfondito per la filiera suinicola agroforestale, soprattutto in relazione a prati artificiali, pascoli e seminativi non irrigui. Tuttavia, la prevalenza di C2 richiede una progettazione prudente, con priorità a superfici già agricole o pascolive e non alle coperture forestali più sensibili.

### 7.7 Criticità e condizioni di attenzione

Criticità: rischio erosivo su C2, pascoli su suoli con limitazioni, possibile pressione su gariga/macchia, necessità di proteggere sugherete e rinnovazione.

### 7.8 Opportunità e approfondimenti successivi

Approfondire: sugherete, aziende agro-zootecniche, superfici pilota, possibilità di integrazione tra prodotti agricoli, sughero, carni locali e turismo rurale. Valutazione preliminare: vocazione sughericola medio-alta; interesse suinicolo medio; fragilità medioalta.

## 8. Comune di Santa Teresa Gallura

### 8.1 Inquadramento sintetico

Santa Teresa Gallura presenta una forte componente seminaturale e costiera, con gariga, macchia mediterranea, prati artificiali e aree a ricolonizzazione. Le tabelle non riportano sugherete. Il ruolo del Comune appare più legato a paesaggio, turismo, mercato di sbocco e gestione ambientale che alla produzione primaria di sughero.

### 8.2 Sintesi dell’uso del suolo

| Classe | Superficie | Incidenza |
|---|---|---|
| Gariga | 2.568 ha | 25,3% |
| Macchia mediterranea | 2.315 ha | 22,8% |
| Prati artificiali | 1.765 ha | 17,4% |
| Aree a ricolonizzazione naturale | 872 ha | 8,6% |
| Aree agricole con spazi naturali importanti | 457 ha | 4,5% |
| Aree agroforestali | 274 ha | 2,7% |

<!-- tabella: tables/p166-t0.csv (ok) -->

Il Comune è dominato da coperture seminaturali mediterranee e da un mosaico rurale-costiero.

<!-- pagina 167 -->

### 8.3 Sintesi pedologica

| Unità | Superficie | Incidenza |
|---|---|---|
| C2 | 5.656 ha | 55,6% |
| C1 | 3.513 ha | 34,5% |
| B2 | 331 ha | 3,3% |
| M1 | 282 ha | 2,8% |
| L1 | 139 ha | 1,4% |

<!-- tabella: tables/p167-t0.csv (ok) -->

La presenza rilevante di C1 e C2 suggerisce condizioni di fragilità diffuse. Le unità M1 e L1 sono minoritarie ma importanti per ambiti sabbiosi o alluvionali.

### 8.4 Lettura della matrice pedologia × uso del suolo

| Combinazione | Superficie | Incidenza |
|---|---|---|
| Prati artificiali su C2 | 1.469 ha | 14,4% |
| Gariga su C2 | 1.249 ha | 12,3% |
| Gariga su C1 | 1.177 ha | 11,6% |
| Macchia mediterranea su C1 | 1.102 ha | 10,8% |
| Macchia mediterranea su C2 | 997 ha | 9,8% |

<!-- tabella: tables/p167-t1.csv (ok) -->

La matrice mostra ampie superfici seminaturali su unità fragili. La funzione protettiva e paesaggistica è centrale.

### 8.5 Implicazioni per la filiera bosco-sughero

Non risultano sugherete nei dati comunali analizzati. Santa Teresa Gallura non va quindi letta come Comune produttivo sughericolo, ma come possibile area di connessione commerciale e turistica per prodotti territoriali provenienti dagli altri Comuni.

### 8.6 Implicazioni per la filiera suinicola agroforestale

Il tema suinicolo va trattato con cautela. La presenza di prati artificiali può essere oggetto di verifica, ma la forte componente di gariga e macchia su C1/C2, insieme al contesto turistico-costiero, suggerisce di evitare modelli estensivi non controllati.

### 8.7 Criticità e condizioni di attenzione

Criticità: sensibilità paesaggistica e ambientale, fragilità dei suoli, pressione turistica, possibile presenza di habitat costieri, rischio di conflitto tra attività zootecnica e fruizione turistica.

### 8.8 Opportunità e approfondimenti successivi

Santa Teresa Gallura può avere un ruolo strategico come mercato di sbocco, luogo di ristorazione identitaria, vetrina turistica, nodo commerciale per carni locali e prodotti legati alla Green Community. Valutazione preliminare: vocazione sughericola bassa; interesse suinicolo basso-medio solo aziendale; ruolo turistico-commerciale alto.

<!-- pagina 168 -->

## 9. Comune di Tempio Pausania

### 9.1 Inquadramento sintetico

Tempio Pausania è uno dei Comuni centrali del progetto per dimensione territoriale, presenza forestale, sugherete, prati artificiali, seminativi e potenziale ruolo di governance. Presenta una forte vocazione bosco-sughero, ma anche rilevanti criticità pedologiche.

### 9.2 Sintesi dell’uso del suolo

| Classe | Superficie | Incidenza |
|---|---|---|
| Macchia mediterranea | 3.475 ha | 16,4% |
| Bosco di latifoglie | 3.350 ha | 15,8% |
| Prati artificiali | 2.496 ha | 11,8% |
| Sugherete | 1.937 ha | 9,1% |
| Gariga | 1.564 ha | 7,4% |
| Seminativi non irrigui | 1.507 ha | 7,1% |

<!-- tabella: tables/p168-t0.csv (ok) -->

Il Comune mostra una matrice ampia e complessa, con forte presenza forestale, agro-pastorale e sughericola.

### 9.3 Sintesi pedologica

| Unità | Superficie | Incidenza |
|---|---|---|
| C2 | 11.026 ha | 51,9% |
| C1 | 6.546 ha | 30,8% |
| C5 | 1.447 ha | 6,8% |
| C3 | 1.275 ha | 6,0% |
| B2 | 502 ha | 2,4% |

<!-- tabella: tables/p168-t1.csv (ok) -->

Prevalgono C2 e C1, quindi suoli su rocce intrusive con limitazioni diffuse. C5 e C3 possono offrire ambiti da approfondire per gestione forestale razionale, infittimento e pascolo regolato.

### 9.4 Lettura della matrice pedologia × uso del suolo

| Combinazione | Superficie | Incidenza |
|---|---|---|
| Prati artificiali su C2 | 1.986 ha | 9,4% |
| Macchia mediterranea su C1 | 1.830 ha | 8,6% |
| Bosco di latifoglie su C1 | 1.783 ha | 8,4% |
| Macchia mediterranea su C2 | 1.410 ha | 6,6% |
| Sugherete su C2 | 1.370 ha | 6,5% |

<!-- tabella: tables/p168-t2.csv (ok) -->

La matrice conferma la rilevanza di Tempio per sughero e gestione agroforestale. Una parte importante delle coperture forestali insiste però su C1, con funzione protettiva da considerare.

### 9.5 Implicazioni per la filiera bosco-sughero

Tempio Pausania è un Comune prioritario per la filiera sughero, con circa 1.937 ha di sugherete. La presenza di sugherete su C2 suggerisce possibilità di approfondimento gestionale; quelle su C1 richiedono maggiore cautela. Tempio può inoltre assumere un ruolo di coordinamento territoriale per filiera, governance, servizi e trasformazione.

<!-- pagina 169 -->

### 9.6 Implicazioni per la filiera suinicola agroforestale

Tempio presenta interesse per approfondimenti suinicoli, soprattutto per la presenza di prati artificiali e seminativi. Tuttavia, l’uso delle aree forestali e delle sugherete dovrà essere molto selettivo. Eventuali progetti pilota dovranno privilegiare superfici agricole e agro-silvo-pastorali gestibili, con esclusione delle aree fragili.

### 9.7 Criticità e condizioni di attenzione

Criticità: ampia superficie su C1, rischio erosione, necessità di distinguere sugherete produttive e protettive, complessità gestionale dovuta alla dimensione comunale.

### 9.8 Opportunità e approfondimenti successivi

Tempio è prioritario per: cabina di regia, mappatura sugherete, gestione forestale integrata, aree pilota, raccordo con trasformazione, possibile collegamento con mattatoio/trasformazione e governance delle filiere. Valutazione preliminare: vocazione sughericola alta; interesse suinicolo medio-alto da verificare; ruolo governance alto; fragilità medio-alta.

## 10. Comune di Trinità d’Agultu e Vignola

### 10.1 Inquadramento sintetico

Trinità d’Agultu e Vignola presenta una forte componente di macchia, gariga, prati artificiali, boschi e pascoli, con presenza limitata di sugherete. Il Comune appare rilevante per gestione del paesaggio mediterraneo, prevenzione incendi, connessione costa-interno e possibili sbocchi turistico-commerciali.

### 10.2 Sintesi dell’uso del suolo

| Classe | Superficie | Incidenza |
|---|---|---|
| Macchia mediterranea | 3.646 ha | 26,6% |
| Gariga | 3.561 ha | 26,0% |
| Prati artificiali | 1.804 ha | 13,2% |
| Bosco di latifoglie | 1.340 ha | 9,8% |
| Aree a pascolo naturale | 699 ha | 5,1% |
| Vegetazione rada | 491 ha | 3,6% |

<!-- tabella: tables/p169-t0.csv (ok) -->

Le sugherete ammontano a circa 211 ha.

### 10.3 Sintesi pedologica

| Unità | Superficie | Incidenza |
|---|---|---|
| C2 | 6.397 ha | 46,7% |
| C1 | 4.477 ha | 32,7% |
| B2 | 1.016 ha | 7,4% |
| I1 | 903 ha | 6,6% |
| M1 | 660 ha | 4,8% |

<!-- tabella: tables/p169-t1.csv (ok) -->

Il quadro pedologico è articolato, ma dominato da C2 e C1. Sono presenti anche B2, I1 e M1, che richiedono letture specifiche a scala di dettaglio.

### 10.4 Lettura della matrice pedologia × uso del suolo

<!-- pagina 170 -->

| Combinazione | Superficie | Incidenza |
|---|---|---|
| Macchia mediterranea su C1 | 1.822 ha | 13,3% |
| Gariga su C2 | 1.715 ha | 12,5% |
| Macchia mediterranea su C2 | 1.396 ha | 10,2% |
| Gariga su C1 | 1.020 ha | 7,4% |
| Prati artificiali su C2 | 982 ha | 7,2% |

<!-- tabella: tables/p170-t0.csv (ok) -->

La matrice mostra una forte presenza di coperture seminaturali su unità fragili. La funzione protettiva della vegetazione è rilevante.

### 10.5 Implicazioni per la filiera bosco-sughero

La presenza di sugherete è limitata ma non assente. Il Comune non appare prioritario per produzione sughericola primaria, ma può contribuire alla rete territoriale attraverso gestione forestale, prevenzione incendi e valorizzazione paesaggistica.

### 10.6 Implicazioni per la filiera suinicola agroforestale

La presenza di prati artificiali e pascoli naturali suggerisce un possibile approfondimento, ma da condurre con cautela. Il contesto costiero/turistico e l’ampia diffusione di C1/C2 rendono preferibili eventuali sperimentazioni aziendali molto controllate e non diffuse.

### 10.7 Criticità e condizioni di attenzione

Criticità: gariga e macchia su suoli fragili, rischio erosione, vegetazione rada, pressione turistica, necessità di verificare habitat e vincoli costieri.

### 10.8 Opportunità e approfondimenti successivi

Approfondire: connessione con turismo e ristorazione, gestione del mosaico mediterraneo, prevenzione incendi, valorizzazione di prodotti territoriali, eventuali aziende pilota in aree non fragili. Valutazione preliminare: vocazione sughericola medio-bassa; interesse suinicolo medio ma prudenziale; ruolo turistico-commerciale medio-alto.

## 11. Comune di Viddalba

### 11.1 Inquadramento sintetico

Viddalba presenta un territorio con gariga, macchia mediterranea, boschi di latifoglie, prati artificiali e pascoli naturali. La presenza di sugherete è molto limitata. Il Comune appare interessante per gestione del mosaico rurale-seminaturale e per eventuali approfondimenti agro-pastorali, ma non come asse primario della filiera sughericola.

### 11.2 Sintesi dell’uso del suolo

| Classe | Superficie | Incidenza |
|---|---|---|
| Gariga | 1.111 ha | 22,4% |
| Macchia mediterranea | 1.055 ha | 21,3% |
| Bosco di latifoglie | 587 ha | 11,9% |
| Prati artificiali | 422 ha | 8,5% |
| Aree a pascolo naturale | 346 ha | 7,0% |

<!-- tabella: tables/p170-t1.csv (ok) -->

<!-- pagina 171 -->

| Classe | Superficie | Incidenza |
|---|---|---|
| Aree a ricolonizzazione artificiale | 291 ha | 5,9% |

<!-- tabella: tables/p171-t0.csv (ok) -->

Le sugherete risultano pari a circa 52 ha.

### 11.3 Sintesi pedologica

| Unità | Superficie | Incidenza |
|---|---|---|
| C2 | 2.329 ha | 47,1% |
| B2 | 1.129 ha | 22,8% |
| C1 | 626 ha | 12,6% |
| M1 | 418 ha | 8,5% |
| L1 | 203 ha | 4,1% |

<!-- tabella: tables/p171-t1.csv (ok) -->

Il quadro pedologico è più diversificato rispetto ad altri Comuni, con C2 prevalente, B2 significativa, C1 meno dominante, e presenza di M1/L1.

### 11.4 Lettura della matrice pedologia × uso del suolo

| Combinazione | Superficie | Incidenza |
|---|---|---|
| Gariga su C2 | 636 ha | 12,8% |
| Macchia mediterranea su C2 | 610 ha | 12,3% |
| Gariga su B2 | 259 ha | 5,2% |
| Macchia mediterranea su B2 | 257 ha | 5,2% |
| Bosco di latifoglie su B2 | 244 ha | 4,9% |

<!-- tabella: tables/p171-t2.csv (ok) -->

La matrice evidenzia coperture seminaturali su C2 e B2, con possibile funzione protettiva e necessità di gestione prudente.

### 11.5 Implicazioni per la filiera bosco-sughero

La presenza di sugherete è marginale. Viddalba non appare Comune prioritario per la filiera sughero produttiva, ma può rientrare in una strategia più ampia di gestione forestale, paesaggio rurale e connessione con economie locali.

### 11.6 Implicazioni per la filiera suinicola agroforestale

Il Comune può essere oggetto di approfondimento limitato per la filiera suinicola, soprattutto in relazione a prati artificiali e pascoli naturali. La presenza di B2 e C2 richiede cautela per rischio erosivo e condizioni di suoli poco o mediamente profondi. Le aree su C1 devono essere trattate con maggiore prudenza.

### 11.7 Criticità e condizioni di attenzione

Criticità: gariga e macchia su unità con limitazioni, rischio erosione, sugherete marginali, necessità di verificare disponibilità aziendali, idrica e infrastrutturale.

### 11.8 Opportunità e approfondimenti successivi

Approfondire: aziende agro-pastorali, gestione del mosaico macchia-gariga-pascolo, possibili superfici pilota controllate, connessione con trasformazione e vendita locale. Valutazione preliminare: vocazione sughericola bassa; interesse suinicolo medio-basso; fragilità media; ruolo agro-pastorale da approfondire.

<!-- pagina 172 -->

#### Sintesi comparativa preliminare

| Comune | Vocazione sughericola | Interesse suinicolo agroforestale | Fragilità pedologica | Priorità di approfondimento |
|---|---|---|---|---|
| Aggius | Medio-alta | Medio, solo pilota | Alta | Alta |
| Aglientu | Medio- bassa | Medio prudenziale | Medio- alta | Media |
| Badesi | Bassa | Medio-bassa | Media | Media |
| Bortigiadas | Medio- bassa | Bassa/localizzata | Alta | Media |
| Calangianus | Alta | Basso-medio controllato | Alta | Molto alta |
| Luogosanto | Media | Medio-alta da verificare | Medio- alta | Alta |
| Luras | Medio-alta | Media | Medio- alta | Alta |
| Santa Teresa Gallura | Bassa | Basso-medio | Medio- alta | Media, soprattutto commerciale |
| Tempio Pausania | Alta | Medio-alta da verificare | Medio- alta | Molto alta |
| Trinità d’Agultu e Vignola | Medio- bassa | Medio prudenziale | Medio- alta | Media |
| Viddalba | Bassa | Medio-bassa | Media | Media |

<!-- tabella: tables/p172-t0.csv (ok) -->

#### Lettura conclusiva preliminare

Dalle schede emergono quattro gruppi funzionali.

Comuni prioritari per filiera bosco-sughero: Calangianus e Tempio Pausania, seguiti da Luras e Aggius. Qui la priorità è approfondire stato delle sugherete, gestione, decortica, proprietà, accessibilità e rapporto con trasformazione.

Comuni agroforestali integrabili: Luogosanto, Aggius, Luras e in parte Tempio. Sono i territori dove verificare con maggiore attenzione eventuali progetti pilota integrati tra gestione forestale, superfici agro-silvopastorali e filiera suinicola controllata.

Comuni con funzione ambientale, paesaggistica e commerciale: Aglientu, Santa Teresa Gallura, Trinità d’Agultu e Vignola, Badesi. Qui il contributo alla Green Community può essere forte sul piano turistico, commerciale, paesaggistico e di sbocco dei prodotti, più che sulla produzione primaria del sughero.

Comuni a prevalente attenzione forestale/protettiva: Bortigiadas e parte di Calangianus, Aggius e Tempio, dove la presenza di C1 e coperture forestali su suoli fragili impone una gestione prudenziale.

Per la filiera suinicola, la linea tecnica da mantenere è netta: nessun Comune va dichiarato idoneo in modo definitivo in questa fase. Le schede consentono solo di individuare ambiti da approfondire, privilegiando superfici agricole, pascolive o agroforestali già gestite, con esclusione preliminare delle aree più fragili, acclivi, erodibili o ambientalmente sensibili.

<!-- pagina 173 -->

#### Sintesi delle principali vocazioni territoriali

#### Premessa metodologica

La lettura integrata delle schede comunali e della matrice intercomunale consente di individuare alcune vocazioni territoriali prevalenti all’interno dell’area UCAG 193. Tali vocazioni non devono essere interpretate come classificazioni definitive o come zonizzazioni prescrittive. Esse rappresentano piuttosto una prima sintesi tecnico-orientativa, utile a comprendere il ruolo potenziale dei diversi Comuni nelle successive fasi di progettazione. La valutazione deriva dall’incrocio preliminare tra: uso del suolo; presenza di superfici forestali, seminaturali, agricole e pascolive; distribuzione delle sugherete rilevate; principali unità pedologiche; matrice pedologia × uso del suolo; fragilità o limitazioni dei suoli; possibile relazione con filiera bosco-sughero; possibile relazione con filiera suinicola agroforestale; ruolo turistico-commerciale dei Comuni costieri; necessità di successivi approfondimenti ambientali, faunistici, aziendali e socioeconomici. La finalità della sintesi è aiutare il gruppo di lavoro a distinguere ruoli territoriali diversi e complementari, evitando di applicare lo stesso modello progettuale a tutti i Comuni.

#### Vocazione forestale e sughericola

La vocazione forestale e sughericola rappresenta uno degli assi principali del progetto. Essa riguarda i Comuni nei quali la presenza di superfici boscate, sugherete, macchia mediterranea e coperture seminaturali suggerisce un ruolo rilevante nella gestione del capitale forestale locale. Dalla lettura preliminare emergono tre livelli. Comuni a vocazione sughericola primaria. Rientrano in questa categoria soprattutto: Calangianus; Tempio Pausania. Questi Comuni mostrano la maggiore rilevanza per la filiera bosco-sughero, sia per la presenza significativa di sugherete, sia per il ruolo territoriale che possono assumere nella governance della filiera. Per questi ambiti, la priorità successiva non è ancora la definizione di interventi puntuali, ma l’approfondimento di: distribuzione effettiva delle sugherete; stato vegetativo e fitosanitario; produttività potenziale; turni di decortica; assetti proprietari; accessibilità; imprese e operatori attivi; collegamento con trasformazione, artigianato, distretto produttivo esistente e possibili certificazioni. In questi Comuni la filiera bosco-sughero può costituire il nucleo identitario e produttivo principale della Green Community. Comuni a vocazione sughericola integrata. Rientrano in questa categoria: Luras; Aggius; Luogosanto.

<!-- pagina 174 -->

In questi territori la presenza di sugherete si inserisce in un mosaico più articolato di superfici agricole, pascolive, forestali e seminaturali. La vocazione sughericola non va quindi letta solo in senso produttivo, ma come parte di una più ampia strategia agroforestale. Questi Comuni sono particolarmente interessanti per approfondire: gestione multifunzionale delle sugherete; integrazione tra bosco, pascolo e superfici rurali; prevenzione incendi; recupero di aree agroforestali; manutenzione del paesaggio rurale; eventuali sperimentazioni controllate con attività zootecniche compatibili; valorizzazione di prodotti territoriali integrati. La vocazione qui è meno concentrata sulla sola produzione di sughero e più orientata alla multifunzionalità agroforestale. Comuni a vocazione forestale protettiva o secondaria. Rientrano in questa categoria: Bortigiadas; parti di Aggius; parti di Calangianus; parti di Tempio Pausania; in misura più limitata Aglientu, Trinità d’Agultu e Vignola e Viddalba. In questi ambiti la presenza di boschi, macchia, gariga o vegetazione seminaturale va letta soprattutto in rapporto alla protezione del suolo, alla stabilità dei versanti, alla biodiversità, alla prevenzione incendi e alla conservazione del paesaggio. La presenza diffusa di unità pedologiche fragili suggerisce che, in molte aree, la funzione forestale debba essere interpretata prima di tutto come funzione protettiva, evitando carichi gestionali eccessivi. Gli approfondimenti successivi dovranno distinguere: aree forestali produttive; aree forestali protettive; aree degradate o da recuperare; superfici da mantenere a copertura naturale; aree non adatte a incremento della pressione zootecnica; superfici utili a interventi di prevenzione incendi e gestione del combustibile.

#### Vocazione agro-silvo-pastorale

La vocazione agro-silvo-pastorale riguarda i Comuni nei quali il mosaico di prati artificiali, pascoli naturali, seminativi, aree agroforestali e superfici seminaturali può costituire una base per ragionare su modelli produttivi estensivi e multifunzionali. I Comuni che emergono con maggiore interesse preliminare sono: Luogosanto; Luras; Aggius; Tempio Pausania; in parte Aglientu; in parte Viddalba; in forma più prudenziale Trinità d’Agultu e Vignola. In questi territori l’uso del suolo suggerisce la presenza di sistemi rurali articolati, nei quali attività agricole, pascolive, forestali e seminaturali possono potenzialmente dialogare. Tuttavia, la vocazione agrosilvo-pastorale deve essere interpretata con cautela, perché molte superfici ricadono su unità pedologiche con limitazioni legate a: superficialità dei suoli;

<!-- pagina 175 -->

pietrosità; rocciosità; pendenza; suscettibilità all’erosione; rischio di compattamento; fragilità della copertura vegetale. Questa vocazione non implica quindi automaticamente la possibilità di aumentare i carichi animali o introdurre nuove attività zootecniche. Al contrario, suggerisce la necessità di definire, nelle fasi successive, modelli di gestione a bassa pressione. Le linee di approfondimento potranno riguardare: pascolo regolato; rotazione delle superfici; recupero di aree rurali sottoutilizzate; gestione del cotico erboso; protezione della rinnovazione forestale; integrazione tra aziende agricole e proprietari forestali; prevenzione incendi attraverso gestione della biomassa; verifica di eventuali aree pilota. Questa vocazione è particolarmente importante per costruire un modello di Green Community non solo forestale, ma anche rurale, produttivo e presidiato.

#### Vocazione alla filiera suinicola agroforestale controllata

La possibile filiera suinicola agroforestale deve essere trattata come vocazione sperimentale e condizionata, non come vocazione territoriale già accertata. Dalla lettura preliminare non emergono Comuni da dichiarare idonei in modo definitivo. Emergono, invece, Comuni nei quali può essere utile approfondire la fattibilità di progetti pilota. I territori più interessanti da approfondire sono: Luogosanto; Tempio Pausania; Luras; Aggius. In seconda battuta, con maggiore cautela: Aglientu; Trinità d’Agultu e Vignola; Viddalba; Badesi, più per eventuali aziende specifiche e rapporto con il mercato che per uso agroforestale estensivo. I Comuni meno prioritari, sulla base della lettura preliminare, sono: Bortigiadas, per la forte funzione forestale protettiva e la fragilità pedologica; Calangianus, dove la priorità deve restare la tutela e valorizzazione delle sugherete; Santa Teresa Gallura, dove il ruolo appare più commerciale e turistico che produttivo-zootecnico. La vocazione suinicola deve essere subordinata ad alcuni criteri minimi: utilizzo solo di superfici effettivamente gestibili; esclusione preliminare delle aree più fragili, acclivi, erodibili o ambientalmente sensibili; preferenza per superfici agricole, pascolive o agroforestali già gestite; recintabilità; disponibilità idrica; accessibilità; biosicurezza;

<!-- pagina 176 -->

controllo sanitario; assenza di conflitti rilevanti con habitat e fauna; protezione della rinnovazione forestale; definizione di carichi sostenibili solo a scala aziendale o di area pilota. In questo senso, la filiera suinicola non va proposta come “pascolo nel bosco”, ma come filiera agroforestale controllata, fondata su qualità, tracciabilità, basso impatto e connessione con trasformazione locale e mercato turistico premium.

#### Vocazione ambientale, paesaggistica e protettiva

Una parte rilevante del territorio UCAG 193 presenta una chiara vocazione ambientale, paesaggistica e protettiva. Questa vocazione emerge soprattutto dove macchia mediterranea, gariga, vegetazione rada, boschi e aree seminaturali insistono su suoli fragili o su contesti sensibili. I Comuni nei quali questa componente assume particolare rilievo sono: Bortigiadas; Aglientu; Santa Teresa Gallura; Trinità d’Agultu e Vignola; parti di Aggius; parti di Calangianus; parti di Tempio Pausania; parti di Viddalba. In questi territori, le coperture naturali e seminaturali non devono essere lette come superfici “inattive” o disponibili a nuovi usi, ma come componenti fondamentali del capitale naturale locale. La loro funzione può riguardare: protezione dei suoli dall’erosione; stabilizzazione dei versanti; conservazione della biodiversità; continuità ecologica; mitigazione del rischio incendio; valore paesaggistico; attrattività turistica; identità rurale e mediterranea; regolazione idrologica; mantenimento dei servizi ecosistemici. Questa vocazione richiede che le future progettazioni distinguano con attenzione tra: aree produttive; aree multifunzionali; aree protettive; aree da recuperare; aree da escludere da usi intensivi. La Green Community dovrà quindi valorizzare anche le funzioni non direttamente produttive del territorio, integrandole nei futuri strumenti di governance, monitoraggio e comunicazione.

#### Vocazione turistico-commerciale e di mercato

I Comuni costieri e turistici assumono una funzione strategica diversa rispetto ai Comuni più interni. In alcuni casi non rappresentano il cuore produttivo della filiera bosco-sughero o della filiera suinicola, ma possono costituire i principali punti di connessione con il mercato. I Comuni più rilevanti sotto questo profilo sono:

<!-- pagina 177 -->

Santa Teresa Gallura; Badesi; Trinità d’Agultu e Vignola; Aglientu. Questi territori possono contribuire alla Green Community attraverso: ristorazione; hotellerie; mercati turistici stagionali; vendita diretta; comunicazione territoriale; turismo esperienziale; eventi locali; collegamento tra costa e interno; valorizzazione del racconto identitario; promozione di prodotti locali di qualità. Il loro ruolo è particolarmente importante per la filiera suinicola, qualora questa venga sviluppata in forma controllata, perché il mercato turistico e ristorativo può assorbire produzioni limitate ma ad alto valore aggiunto. Allo stesso modo, questi Comuni possono contribuire alla valorizzazione del sughero non solo come materia prima, ma anche attraverso: artigianato; design; packaging sostenibile; bioedilizia; esperienze turistiche legate alla cultura del sughero; itinerari territoriali; narrazione del paesaggio rurale e forestale gallurese. La vocazione turistico-commerciale non deve quindi essere considerata secondaria: essa rappresenta il possibile ponte tra produzione interna e mercati premium.

#### Vocazione alla governance territoriale e ai servizi di filiera

Alcuni Comuni, per dimensione, centralità territoriale, presenza di filiere o dotazione di servizi, possono assumere un ruolo più rilevante nella governance della Green Community. In particolare: Tempio Pausania; Calangianus. A questi si possono affiancare, per funzioni specifiche: Luogosanto, per la componente agroforestale e rurale; Luras e Aggius, per la componente sughericola-agro-pastorale; Santa Teresa Gallura, Badesi e Trinità d’Agultu e Vignola, per la componente commerciale, turistica e di mercato. La governance territoriale dovrà evitare una divisione rigida tra Comuni produttivi e Comuni commerciali. Il modello più coerente sembra essere quello di una rete funzionale intercomunale, nella quale ciascun Comune contribuisce con il proprio ruolo prevalente: produzione e gestione forestale; presidio rurale; sperimentazione agro-zootecnica controllata; trasformazione;

<!-- pagina 178 -->

commercializzazione; turismo; comunicazione; tutela ambientale; monitoraggio e governance. La vocazione alla governance riguarda quindi l’intero sistema UCAG 193, ma con alcune polarità territoriali da approfondire.

#### Quadro sintetico delle vocazioni territoriali

| Vocazione prevalente | Comuni maggiormente interessati | Ruolo preliminare |
|---|---|---|
| Sughericola primaria | Calangianus, Tempio Pausania | Poli principali per approfondire gestione, valorizzazione, filiera, certificazioni e governance del sughero. |
| Sughericola integrata | Luras, Aggius, Luogosanto | Integrazione tra sugherete, mosaico agro-pastorale, gestione forestale, prevenzione incendi e filiere locali. |
| Forestale protettiva | Bortigiadas, parti di Calangianus, Aggius, Tempio, Aglientu, Trinità, Viddalba | Conservazione del suolo, tutela della vegetazione, prevenzione erosione, gestione prudenziale. |
| Agro-silvo- pastorale | Luogosanto, Luras, Aggius, Tempio, Aglientu, Viddalba | Possibile base per modelli rurali estensivi, gestione del paesaggio e progetti pilota controllati. |
| Suinicola agroforestale sperimentale | Luogosanto, Tempio, Luras, Aggius | Da valutare solo con studi aziendali, pedologici, sanitari, faunistici e ambientali. |
| Turistico- commerciale | Santa Teresa Gallura, Badesi, Trinità d’Agultu e Vignola, Aglientu | Mercato di sbocco, ristorazione, turismo esperienziale, comunicazione, vendita e valorizzazione premium. |
| Agricola e agroalimentare complementare | Badesi, Luras, Tempio, Luogosanto, Viddalba | Supporto a filiere locali, trasformazione, prodotti territoriali, integrazione con turismo. |
| Governance e servizi di filiera | Tempio Pausania, Calangianus, con raccordo intercomunale | Coordinamento, cabina di regia, servizi tecnici, raccordo con operatori, monitoraggio, progettazione successiva. |

<!-- tabella: tables/p178-t0.csv (ok) -->

#### Lettura conclusiva

La sintesi delle vocazioni territoriali mostra che l’area UCAG 193 non deve essere trattata come un territorio omogeneo. I Comuni svolgono ruoli differenziati e potenzialmente complementari. La filiera bosco-sughero trova i propri poli principali in Calangianus e Tempio Pausania, ma può essere integrata con i territori di Luras, Aggius e Luogosanto, dove il mosaico agroforestale consente di ragionare su modelli più multifunzionali.

<!-- pagina 179 -->

La filiera suinicola agroforestale, invece, deve essere considerata una possibilità sperimentale da verificare, con maggiore interesse preliminare per Luogosanto, Tempio Pausania, Luras e Aggius, ma sempre con approccio prudenziale e sito-specifico.

I Comuni costieri, pur non essendo necessariamente centrali per la produzione primaria, assumono un ruolo strategico nella connessione con il mercato turistico, la ristorazione, la comunicazione e la valorizzazione commerciale dei prodotti locali.

Infine, la forte presenza di aree con funzione ambientale, paesaggistica e protettiva impone che ogni successivo progetto di dettaglio sia costruito sulla distinzione tra aree da valorizzare produttivamente, aree da gestire in modo multifunzionale e aree da conservare prioritariamente.

La principale vocazione complessiva della Green Community può quindi essere sintetizzata come segue:

costruire una rete territoriale integrata nella quale i Comuni interni contribuiscano alla gestione sostenibile del bosco, delle sugherete e del mosaico agro-silvo-pastorale, mentre i Comuni costieri e turistici rafforzino la commercializzazione, la narrazione e il valore di mercato delle filiere locali, in un quadro di tutela del suolo, biodiversità e identità territoriale.

#### Prima indicazione degli ambiti più coerenti con successive progettazioni di dettaglio

Premessa Le schede comunali, la matrice intercomunale e la sintesi delle vocazioni territoriali consentono di individuare alcuni ambiti tematici e territoriali che appaiono più coerenti con lo sviluppo di successive progettazioni di dettaglio.

Anche in questo caso, l’indicazione non ha valore localizzativo definitivo. Non si individuano ancora particelle, aziende, superfici operative o carichi gestionali. Si propongono invece ambiti prioritari di approfondimento, da verificare attraverso rilievi di campo, confronto con gli operatori, analisi vincolistiche, verifiche pedologiche, valutazioni ambientali, studi economici e progettazione aziendale.

La finalità è orientare il gruppo di lavoro verso i temi e i territori nei quali sembra più opportuno concentrare le fasi successive, evitando dispersione e mantenendo coerenza con le vocazioni emerse.

#### Ambito 1 — Gestione sostenibile e valorizzazione delle sugherete

#### Comuni prioritari

Calangianus Tempio Pausania Luras Aggius Luogosanto Questo ambito è il più coerente con l’identità territoriale e produttiva del progetto. Le analisi preliminari evidenziano che la risorsa sughericola è particolarmente rilevante nei Comuni di Calangianus e Tempio Pausania, seguiti da Luras, Aggius e Luogosanto. In questi Comuni la presenza di sugherete, boschi di latifoglie, macchia mediterranea e mosaici agroforestali suggerisce la possibilità di sviluppare successivi progetti di dettaglio finalizzati alla gestione sostenibile della risorsa. La progettazione dovrà però distinguere con attenzione:

sugherete produttive;

sugherete con funzione protettiva;

sugherete degradate o abbandonate;

aree da recuperare;

aree non idonee a incrementi di pressione gestionale;

superfici in cui la tutela del suolo deve prevalere sulla funzione produttiva.

<!-- pagina 180 -->

Possibili progettazioni successive Piano intercomunale di conoscenza e classificazione delle sugherete. Piano di gestione sostenibile delle sugherete. Progetto pilota di recupero di sugherete degradate. Programma di formazione per operatori della decortica. Studio di fattibilità per certificazioni forestali. Schema di contratto di filiera per il sughero. Analisi di complementarità con il distretto produttivo del sughero. Progetto di valorizzazione del sughero locale in artigianato, bioedilizia, packaging, design e turismo esperienziale.

Soggetti da coinvolgere Comuni e UCAG. Proprietari forestali pubblici e privati. Imprese sughericole. Estrattori e operatori forestali. Trasformatori. Tecnici forestali, agronomi e pedologi. Enti regionali competenti. Organismi di certificazione. Operatori turistici e culturali.

Condizioni di fattibilità Mappatura aggiornata delle sugherete. Verifica dello stato vegetativo e fitosanitario. Analisi della rinnovazione naturale. Accessibilità e viabilità forestale. Chiarezza degli assetti proprietari. Presenza o attivazione di operatori qualificati. Compatibilità con vincoli ambientali e forestali. Sostenibilità economica delle operazioni di gestione.

Output attesi Carta funzionale delle sugherete. Classificazione delle superfici per funzione produttiva, protettiva, multifunzionale o di recupero. Elenco di aree candidate a interventi pilota. Linee guida preliminari di gestione. Prima ipotesi di accordo o contratto di filiera. Indicatori per monitorare stato delle sugherete, produzione, qualità e gestione.

#### Ambito 2 — Recupero e gestione multifunzionale del mosaico agroforestale

#### Comuni prioritari

Luogosanto Luras Aggius Tempio Pausania Aglientu

<!-- pagina 181 -->

Trinità d’Agultu e Vignola Viddalba La matrice territoriale mostra la presenza diffusa di macchia mediterranea, gariga, prati artificiali, pascoli naturali, boschi di latifoglie, aree agroforestali e superfici in ricolonizzazione. Questo mosaico rappresenta una componente chiave della Green Community perché svolge funzioni produttive, paesaggistiche, protettive, ecologiche e di presidio rurale. Gli ambiti più coerenti con successive progettazioni sono quelli in cui la gestione del mosaico può contribuire a: mantenere la copertura vegetale protettiva; ridurre il rischio di abbandono; prevenire fenomeni erosivi; contenere la biomassa combustibile; sostenere attività agricole e pastorali compatibili; recuperare superfici rurali sottoutilizzate; integrare gestione forestale e valorizzazione economica locale.

Possibili progettazioni successive Progetto pilota di gestione integrata macchia-gariga-pascolo. Piano di manutenzione del mosaico agroforestale. Interventi dimostrativi di recupero di aree in ricolonizzazione. Modelli di gestione combinata meccanica, pastorale e forestale della biomassa. Linee guida per pascolo regolato in aree agro-silvo-pastorali. Progetti di prevenzione incendi integrati con attività rurali. Azioni di monitoraggio della copertura vegetale e del suolo.

Soggetti da coinvolgere Aziende agricole e zootecniche. Proprietari forestali. Comuni. Tecnici forestali e agronomi. Pedologi. Operatori antincendio e protezione civile. Enti ambientali. Associazioni locali.

Condizioni di fattibilità Verifica delle condizioni pedologiche e morfologiche. Esclusione delle aree più fragili. Disponibilità dei proprietari. Accessibilità delle superfici. Presenza di aziende interessate. Compatibilità con vincoli ambientali e paesaggistici. Definizione di carichi e modalità gestionali solo a scala di dettaglio. Monitoraggio degli effetti su suolo e vegetazione.

Output attesi Individuazione di aree agroforestali candidate. Schede tecniche per aree pilota. Protocollo preliminare di gestione del mosaico agroforestale.

<!-- pagina 182 -->

Indicatori di monitoraggio su copertura vegetale, erosione, biomassa e biodiversità. Modello replicabile in altri Comuni.

#### Ambito 3 — Sperimentazione controllata della filiera suinicola agroforestale

#### Comuni prioritari per approfondimento

Luogosanto Tempio Pausania Luras Aggius

#### Comuni da valutare con maggiore cautela

Aglientu Trinità d’Agultu e Vignola Viddalba Badesi

#### Comuni non prioritari per la fase pilota produttiva

Bortigiadas Calangianus Santa Teresa Gallura

La filiera suinicola agroforestale rappresenta un ambito potenzialmente innovativo, ma anche il più delicato sotto il profilo pedologico, ambientale, faunistico e sanitario. Le analisi preliminari indicano che alcuni Comuni presentano superfici agricole, pascolive o agroforestali che potrebbero essere approfondite per eventuali sperimentazioni. Tuttavia, la presenza diffusa di unità pedologiche con limitazioni, la sensibilità di molte coperture vegetali e le possibili interazioni con fauna selvatica impongono un approccio estremamente prudente. La progettazione di dettaglio dovrà riguardare solo aree: effettivamente gestibili; recintabili; accessibili; non soggette a fragilità pedologica elevata; non ricadenti in habitat sensibili; compatibili con biosicurezza e controllo sanitario; disponibili per adesione volontaria degli operatori.

Possibili progettazioni successive Studio di prefattibilità della filiera suinicola agroforestale. Individuazione di 1-2 aree pilota aziendali o interaziendali. Piano sanitario e di biosicurezza. Studio sui carichi sostenibili a scala aziendale. Disciplinare preliminare di produzione. Progetto di trasformazione e commercializzazione delle carni. Analisi di mercato verso ristorazione, hotellerie e turismo premium. Sistema di tracciabilità territoriale.

Soggetti da coinvolgere

<!-- pagina 183 -->

Aziende agricole e allevatori. Servizi veterinari. Faunisti. Pedologi e agronomi. Tecnici forestali. Comuni interessati. Trasformatori alimentari. Macelli e laboratori di sezionamento/trasformazione. Ristoratori e operatori turistici. Associazioni di categoria.

Condizioni di fattibilità Verifica sanitaria e normativa. Disponibilità di aziende pilota. Superfici gestibili e controllabili. Recinzioni adeguate. Disponibilità idrica. Esclusione delle aree fragili. Compatibilità con vincoli ambientali. Piano di biosicurezza. Controllo delle interazioni con fauna selvatica. Definizione dei carichi solo dopo rilievi di dettaglio. Presenza di un canale di trasformazione e vendita.

Output attesi Studio di prefattibilità. Selezione di aree pilota. Protocollo gestionale. Protocollo sanitario. Bozza di disciplinare. Piano di tracciabilità. Prima ipotesi di modello economico e commerciale.

#### Ambito 4 — Prevenzione incendi e gestione della biomassa

#### Comuni prioritari

Calangianus Tempio Pausania Luogosanto Aggius Luras Aglientu Trinità d’Agultu e Vignola La presenza diffusa di macchia mediterranea, gariga, boschi, vegetazione rada, aree in ricolonizzazione e sugherete rende il tema della prevenzione incendi trasversale all’intera strategia. La gestione della biomassa deve essere considerata un ambito di progettazione specifico, da integrare con la valorizzazione forestale e, dove compatibile, con attività agro-silvo-pastorali. Non è corretto assumere automaticamente che l’allevamento, e in particolare quello suino, costituisca una soluzione al rischio incendio. Può contribuire solo in contesti limitati e controllati, insieme ad altri strumenti gestionali.

<!-- pagina 184 -->

Possibili progettazioni successive Carta preliminare delle aree a maggiore accumulo di biomassa. Piano dimostrativo di gestione del sottobosco in sughereta. Interventi integrati di manutenzione forestale e rurale. Studio su viabilità forestale e accessibilità antincendio. Progetti pilota di gestione combinata meccanica e pastorale. Monitoraggio degli effetti sulla copertura vegetale.

Soggetti da coinvolgere Comuni. Protezione civile. Forestas o soggetti competenti. Proprietari forestali. Aziende agricole. Tecnici forestali. Operatori antincendio. Associazioni locali.

Condizioni di fattibilità Coerenza con piani antincendio esistenti. Compatibilità con suolo e vegetazione. Accessibilità delle aree. Disponibilità dei proprietari. Presenza di operatori qualificati. Monitoraggio dei risultati. Esclusione di interventi che aumentino erosione o degrado.

Output attesi Mappa delle priorità di gestione biomassa. Aree dimostrative. Linee guida per gestione del sottobosco. Collegamento con piano di gestione delle sugherete. Indicatori di rischio e monitoraggio.

#### Ambito 5 — Tutela del suolo, contrasto all’erosione e gestione delle aree fragili

#### Comuni prioritari

Bortigiadas Calangianus Aggius Tempio Pausania Aglientu Santa Teresa Gallura Trinità d’Agultu e Vignola Luogosanto Luras La lettura pedologica evidenzia la presenza diffusa di unità con limitazioni legate a suoli poco profondi, rocciosità, pietrosità, scheletro, pendenza e suscettibilità all’erosione. In molti casi, boschi, macchia e gariga

<!-- pagina 185 -->

svolgono una funzione protettiva essenziale. Per questo motivo, una parte significativa del territorio deve essere oggetto di progettazioni orientate non alla produzione diretta, ma alla conservazione e alla gestione prudenziale del suolo.

Possibili progettazioni successive Carta delle aree a fragilità pedologica elevata. Linee guida per gestione delle aree su C1 e altre unità limitanti. Progetti di recupero vegetazionale in aree degradate. Interventi antierosivi leggeri. Monitoraggio di aree a vegetazione rada. Regolazione o esclusione del pascolo in aree vulnerabili. Verifica del ruolo protettivo delle coperture forestali e arbustive.

Soggetti da coinvolgere Pedologi. Agronomi. Tecnici forestali. Comuni. Proprietari. Aziende agricole. Enti ambientali. Protezione civile.

Condizioni di fattibilità Rilievi di campo. Cartografia di dettaglio. Integrazione con dati di pendenza e idrologia. Compatibilità con habitat e vincoli. Disponibilità dei proprietari. Monitoraggio pluriennale.

Output attesi Carta di fragilità del suolo. Criteri di esclusione o limitazione. Schede per aree fragili. Piano di monitoraggio erosione/copertura vegetale. Linee guida per gestione prudenziale.

#### Ambito 6 — Valorizzazione turistica e commerciale delle filiere territoriali

#### Comuni prioritari

Santa Teresa Gallura Badesi Trinità d’Agultu e Vignola Aglientu Comuni produttivi da collegare Calangianus Tempio Pausania Luras

<!-- pagina 186 -->

Aggius Luogosanto La Green Community può generare valore se riesce a collegare le produzioni interne con i mercati costieri e turistici. I Comuni costieri non sono necessariamente i principali produttori di sughero o di carni locali, ma possono svolgere una funzione strategica come luoghi di consumo, vendita, narrazione e promozione. Questo ambito è particolarmente rilevante per costruire una relazione tra: paesaggio forestale; sugherete; prodotti agroalimentari; carni locali; artigianato; turismo esperienziale; ristorazione identitaria; mercato premium della Costa Smeralda e dell’area nord-orientale.

Possibili progettazioni successive Piano commerciale preliminare per prodotti della Green Community. Accordi esplorativi con ristoranti, hotel, resort e botteghe locali. Itinerari turistici sughero-territorio-gastronomia. Eventi di degustazione e promozione. Concept di marchio territoriale. Packaging sostenibile collegato al sughero. Narrazione integrata del prodotto locale. Collegamento con turismo rurale e artigianato.

Soggetti da coinvolgere Ristoratori. Hotel e resort. Operatori turistici. Comuni costieri. Produttori agroalimentari. Imprese sughericole. Artigiani. Agenzie di promozione territoriale. Associazioni locali.

Condizioni di fattibilità Disponibilità di prodotti tracciati. Quantità compatibili con mercati di qualità. Standard igienico-sanitari e commerciali. Identità territoriale chiara. Coordinamento tra Comuni interni e costieri. Comunicazione professionale. Accordi commerciali realistici.

Output attesi Mappa dei potenziali operatori commerciali. Piano di valorizzazione turistica.

<!-- pagina 187 -->

Concept di prodotto territoriale. Eventi pilota. Prime manifestazioni di interesse. Schema di accordo tra produttori e operatori turistici.

#### Ambito 7 —Governance intercomunale e strumenti di filiera

#### Comuni e soggetti prioritari

UCAG / soggetto capofila Tempio Pausania Calangianus tutti gli altri Comuni con ruoli funzionali differenziati La complessità del progetto richiede una governance intercomunale stabile. Le filiere bosco-sughero e suinicola non possono essere sviluppate attraverso iniziative isolate, ma necessitano di coordinamento tra Comuni, proprietari, imprese, aziende agricole, trasformatori, tecnici, enti pubblici e operatori commerciali. La governance dovrà gestire il passaggio da analisi preliminare a progettazione di dettaglio.

Possibili progettazioni successive Cabina di regia tecnico-istituzionale. Tavolo permanente filiera sughero. Tavolo esplorativo filiera suinicola. Living Lab territoriale. Schema di contratto di filiera. Accordo intercomunale per il monitoraggio dei dati. Sistema GIS condiviso. Protocollo per aggiornamento delle schede comunali.

Soggetti da coinvolgere UCAG. Comuni. Regione ed enti strumentali. AGRIS, Laore, Forestas o soggetti competenti. Proprietari forestali. Imprese. Aziende agricole. Associazioni di categoria. Tecnici. Operatori turistici. Organismi di certificazione.

Condizioni di fattibilità Ruoli chiari. Coordinamento tecnico. Condivisione dei dati. Disponibilità degli attori. Programma di lavoro progressivo. Risorse per studi successivi. Capacità di tradurre gli indirizzi in progetti candidabili a finanziamento.

<!-- pagina 188 -->

Output attesi Modello di governance preliminare. Cabina di regia. Calendario dei tavoli tecnici. Schema di partenariato. Elenco di progetti candidabili. Sistema informativo territoriale aggiornabile.

#### Ambito 8 — Sistema conoscitivo, GIS territoriale e monitoraggio

#### Comuni interessati

Tutti i Comuni UCAG 193 Uno dei risultati più utili del lavoro preliminare può essere la costruzione di un sistema conoscitivo replicabile e aggiornabile. Le tabelle QGIS, l’uso del suolo, la pedologia e la matrice pedologia × uso del suolo costituiscono una base iniziale, ma devono essere organizzate in un sistema territoriale condiviso. Questo ambito è trasversale e sostiene tutti gli altri.

Possibili progettazioni successive Database territoriale intercomunale. Atlante comunale uso del suolo/pedologia/vocazioni. Sistema GIS condiviso. Carta delle sugherete. Carta delle aree agro-silvo-pastorali. Carta delle fragilità pedologiche. Carta dei vincoli e habitat. Carta delle aree pilota. Sistema di indicatori ambientali, produttivi ed economici.

Soggetti da coinvolgere Gruppo tecnico. Comuni. UCAG. Tecnici GIS. Agronomi, pedologi, forestali. Enti regionali. Eventuali università o centri di ricerca.

Condizioni di fattibilità Standardizzazione dei dati. Aggiornamento periodico. Validazione tecnica. Integrazione con rilievi di campo. Accessibilità al gruppo di lavoro. Compatibilità con formati GIS esistenti.

Output attesi GIS territoriale UCAG.

<!-- pagina 189 -->

Schede comunali aggiornabili. Matrici di valutazione. Cruscotto di indicatori. Supporto alle future candidature progettuali.

#### Quadro sintetico degli ambiti coerenti con progettazioni di dettaglio

| Ambito di progettazione | Comuni prioritari | Tipo di progetto successivo | Livello di urgenza |
|---|---|---|---|
| Gestione sostenibile delle sugherete | Calangianus, Tempio, Luras, Aggius, Luogosanto | Piano gestione, mappatura, filiera, certificazione | Molto alto |
| Mosaico agroforestale | Luogosanto, Luras, Aggius, Tempio, Aglientu, Trinità, Viddalba | Aree pilota, gestione biomassa, recupero rurale | Alto |
| Filiera suinicola agroforestale | Luogosanto, Tempio, Luras, Aggius | Studio prefattibilità e progetto pilota | Alto ma condizionato |
| Prevenzione incendi | Calangianus, Tempio, Luogosanto, Aggius, Luras, Aglientu, Trinità | Piano biomassa, sottobosco, viabilità, aree dimostrative | Alto |
| Tutela suolo e aree fragili | Bortigiadas, Calangianus, Aggius, Tempio, Aglientu, Santa Teresa, Trinità | Carta fragilità, linee guida, monitoraggio | Molto alto |
| Turismo e mercato | Santa Teresa, Badesi, Trinità, Aglientu | Piano commerciale, accordi, turismo esperienziale | Medio- alto |
| Governance e filiere | UCAG, Tempio, Calangianus, tutti i Comuni | Cabina regia, contratti filiera, living lab | Molto alto |
| GIS e monitoraggio | Tutti | Database, cartografie, KPI, aggiornamento schede | Molto alto |

<!-- tabella: tables/p189-t0.csv (ok) -->

#### Indicazione conclusiva

Gli ambiti più coerenti con successive progettazioni di dettaglio possono essere organizzati secondo una logica progressiva. In una prima fase, appare prioritario consolidare il quadro conoscitivo: mappatura delle sugherete, carta delle fragilità pedologiche, quadro dei vincoli, GIS territoriale e ricognizione degli attori locali. In una seconda fase, potranno essere selezionate aree pilota per gestione sostenibile delle sugherete, recupero del mosaico agroforestale, prevenzione incendi e sperimentazione suinicola controllata. In una terza fase, sarà possibile sviluppare strumenti di filiera: contratti, disciplinari, tracciabilità, certificazioni, accordi commerciali e modello di governance stabile.

<!-- pagina 190 -->

La logica da proporre al tavolo tecnico è quindi la seguente: non partire da interventi puntuali già predefiniti, ma costruire un percorso di progettazione progressiva che trasformi le vocazioni territoriali emerse in progetti di dettaglio verificati, sostenibili, condivisi e coerenti con le caratteristiche pedologiche, forestali, ambientali ed economiche dei diversi Comuni.

#### Nota preliminare di posizionamento del contributo agro-forestale, pedologico e territoriale

#### Finalità del contributo

Il presente contributo tecnico si inserisce nel percorso di elaborazione del report preliminare del progetto GREEN COMMUNITIES Alta Gallura — UCAG 193, con particolare riferimento alla componente agroforestale, pedologica, ambientale e produttiva collegata alla valorizzazione della filiera bosco-sughero e alla possibile integrazione con una filiera suinicola agroforestale locale. Il lavoro ha natura preliminare, orientativa e propedeutica. La sua finalità non è definire strategie operative puntuali, localizzazioni definitive, carichi gestionali o modelli aziendali già applicabili, ma costruire un primo quadro tecnico utile a supportare le successive fasi di approfondimento progettuale. In questa prospettiva, il contributo intende fornire al gruppo di lavoro: una prima lettura integrata del territorio; criteri tecnici per interpretare uso del suolo, pedologia e assetti agro-forestali; elementi utili a distinguere vocazioni, limiti e condizioni di attenzione; indirizzi preliminari per individuare ambiti potenzialmente meritevoli di approfondimento; input per futuri studi di dettaglio, piani di gestione, progetti pilota, contratti di filiera e strumenti di governance territoriale. Il contributo non deve quindi essere interpretato come uno strumento prescrittivo, ma come una base tecnica di orientamento per le successive decisioni del gruppo di lavoro e degli attori territoriali.

#### Perimetro territoriale e tecnico del lavoro

Il lavoro riguarda i Comuni di: Aggius, Aglientu, Badesi, Bortigiadas, Calangianus, Luogosanto, Luras, Santa Teresa Gallura, Tempio Pausania, Trinità d’Agultu e Vignola e Viddalba. Per ciascun Comune, l’analisi preliminare è impostata attraverso una lettura integrata dei materiali disponibili, con particolare attenzione a: dati di uso del suolo; dati pedologici; matrici di intersezione tra pedologia e uso del suolo; tabelle ed elaborazioni GIS; documentazione tecnica e progettuale disponibile; eventuali ulteriori materiali ambientali, forestali, faunistici o territoriali che potranno essere integrati nelle fasi successive.

#### Uso del suolo

Il primo livello riguarda l’analisi delle principali coperture territoriali e degli usi attuali del suolo: superfici forestali, aree agro-silvo-pastorali, pascoli, seminativi, colture permanenti, aree naturali o seminaturali, ambiti urbanizzati e infrastrutturali. Questa analisi consente di definire una prima fotografia dell’assetto territoriale comunale e di individuare le principali funzioni presenti: produttive, forestali, pastorali, conservazionistiche, paesaggistiche o insediative.

<!-- pagina 191 -->

Pedologia Il secondo livello riguarda la lettura delle principali unità pedologiche e delle relative limitazioni d’uso. In questa fase, la pedologia viene utilizzata per comprendere in via preliminare: profondità utile dei suoli; tessitura; pietrosità e rocciosità; drenaggio; fertilità potenziale; suscettibilità all’erosione; rischio di compattamento; capacità di sostenere usi agro-silvo-pastorali; limitazioni per interventi forestali, agricoli o zootecnici. La scala delle informazioni disponibili consente una valutazione generale delle condizioni territoriali, ma non sostituisce indagini sito-specifiche, rilievi di campo o verifiche aziendali.

#### Matrice pedologia × uso del suolo

Il terzo livello riguarda l’interpretazione degli incroci tra classi pedologiche e uso attuale del suolo. Questo passaggio è particolarmente utile perché permette di valutare non soltanto quali coperture siano presenti, ma anche se tali coperture risultino coerenti, compatibili, fragili o potenzialmente migliorabili rispetto alle caratteristiche dei suoli. La matrice pedologia × uso del suolo rappresenta quindi uno strumento conoscitivo preliminare per orientare valutazioni successive su: coerenza tra uso attuale e potenzialità del suolo; aree forestali o agroforestali con condizioni favorevoli; superfici soggette a limitazioni; ambiti in cui il mantenimento della copertura vegetale ha valore protettivo; aree che potrebbero richiedere azioni di recupero, riqualificazione o gestione prudenziale.

#### Vocazionalità e compatibilità preliminare

Il quarto livello consiste nella traduzione dei dati territoriali in una prima lettura di vocazionalità e compatibilità. In questa fase non vengono definite idoneità definitive, ma vengono individuati orientamenti preliminari relativi a: valorizzazione delle sugherete; gestione forestale sostenibile; recupero di aree agroforestali; integrazione con attività agro-silvo-pastorali; possibile sperimentazione di modelli suinicoli controllati; tutela degli habitat e della biodiversità; prevenzione del degrado dei suoli; prevenzione incendi e gestione della biomassa; valorizzazione delle economie rurali locali.

#### Ruolo della pedologia nella costruzione del quadro preliminare

La pedologia rappresenta una delle basi tecniche principali per impostare correttamente il ragionamento territoriale. Le caratteristiche dei suoli condizionano direttamente: stabilità e produttività delle formazioni forestali; capacità di rinnovazione delle sugherete; compatibilità con il pascolo; rischio di erosione; rischio di compattamento;

<!-- pagina 192 -->

capacità di trattenere acqua; vulnerabilità al degrado; possibilità di sostenere interventi agro-silvo-pastorali; limiti all’intensificazione produttiva. Nel presente lavoro, la pedologia non viene utilizzata per formulare prescrizioni definitive, ma per individuare condizioni generali di attenzione e per orientare le successive verifiche di dettaglio. A livello preliminare, il territorio può essere interpretato secondo tre grandi categorie operative.

#### Ambiti potenzialmente favorevoli

Sono ambiti nei quali l’uso attuale del suolo e le caratteristiche pedologiche sembrano indicare una possibile compatibilità con interventi di valorizzazione forestale, agroforestale o agro-silvo-pastorale. Rientrano in questa categoria le aree che, sulla base dei dati disponibili, possono costituire oggetto di ulteriori approfondimenti per: gestione sostenibile delle sugherete; recupero di superfici forestali o agroforestali; miglioramento della funzionalità ecologica e produttiva; eventuali progetti pilota connessi a filiere locali.

#### Ambiti con limitazioni

Sono ambiti nei quali la presenza di limitazioni pedologiche, morfologiche, ambientali o gestionali richiede cautela. In questi casi, eventuali interventi futuri dovranno essere valutati con attenzione e potranno richiedere: bassi livelli di pressione gestionale; rotazioni; esclusioni stagionali; tutela della copertura vegetale; interventi antierosivi; protezione della rinnovazione forestale; monitoraggio del suolo; verifiche ambientali e faunistiche. Questi ambiti non sono necessariamente da escludere, ma richiedono una progettazione più prudente e sito-specifica.

#### Ambiti da trattare con prevalente funzione protettiva

Sono ambiti nei quali le condizioni pedologiche, morfologiche o ambientali suggeriscono di privilegiare finalità conservative, protettive o di rinaturalizzazione. Possono rientrare in questa categoria aree con: suoli superficiali; forte rocciosità o pietrosità; elevata pendenza; suscettibilità all’erosione; condizioni idromorfe; habitat sensibili; coperture vegetali da mantenere per finalità protettive; elevata vulnerabilità ambientale. Per tali aree, il presente contributo non propone interventi produttivi, ma segnala la necessità di approfondimenti specifici e di una gestione coerente con la conservazione del capitale naturale.

#### Contributo preliminare alla filiera bosco-sughero

<!-- pagina 193 -->

La filiera bosco-sughero rappresenta uno degli assi identitari e strategici del progetto GREEN COMMUNITIES Alta Gallura. Il contributo agro-forestale e pedologico può supportare questa filiera fornendo una prima lettura territoriale utile a distinguere: aree forestali già interessate da sugherete; aree potenzialmente compatibili con la gestione della quercia da sughero; superfici forestali o agroforestali da recuperare; ambiti in cui la funzione protettiva o paesaggistica prevale su quella produttiva; aree in cui sono necessari approfondimenti sullo stato vegetativo, fitosanitario e gestionale. In questa fase non si intende definire un piano puntuale di gestione delle sugherete, ma fornire indicazioni preliminari per orientare successivi studi su: distribuzione effettiva delle sugherete; stato produttivo e fitosanitario; rinnovazione naturale; accessibilità; proprietà; turni di decortica; presenza di operatori; rapporti tra produzione primaria, trasformazione e mercato. Il messaggio tecnico centrale è che la sughereta non deve essere interpretata esclusivamente come risorsa estrattiva, ma come sistema territoriale multifunzionale. La sughereta svolge infatti funzioni: produttive; ecologiche; paesaggistiche; identitarie; climatiche; antierosive; di presidio rurale; di potenziale integrazione con turismo, artigianato e prodotti locali. Per questo motivo, ogni futura strategia di valorizzazione dovrà essere costruita a partire da una conoscenza più puntuale della risorsa, evitando generalizzazioni e distinguendo gli ambiti realmente produttivi da quelli da recuperare, proteggere o gestire con finalità prevalentemente conservative.

#### Contributo preliminare alla filiera suinicola agroforestale

La possibile filiera suinicola agroforestale costituisce un tema di interesse per la Green Community, soprattutto se collegata alla valorizzazione delle aree rurali interne, alla gestione controllata di superfici agrosilvo-pastorali, alla produzione di carni locali di qualità e al rapporto con il mercato turistico e ristorativo. Tuttavia, in questa fase il tema deve essere trattato come ipotesi progettuale da approfondire, non come strategia già definita. Il presente contributo può fornire input preliminari per valutare, nelle fasi successive, la compatibilità tra allevamento suino controllato e: uso attuale del suolo; caratteristiche pedologiche; copertura vegetale; presenza di sugherete; aree pascolive o agroforestali; vulnerabilità dei suoli; rischio di erosione;

<!-- pagina 194 -->

rischio di compattamento; tutela della rinnovazione forestale; habitat sensibili; fauna selvatica; biosicurezza; accessibilità e gestione aziendale. L’allevamento suino in ambiente agroforestale può generare opportunità, ma anche criticità. Per questo motivo, la sua eventuale introduzione dovrà essere valutata soltanto attraverso progetti pilota controllati, con verifiche tecniche, sanitarie, ambientali ed economiche.

.

#### Ambiti potenzialmente approfondibili

Sono aree agro-silvo-pastorali, forestali rade o rurali sottoutilizzate che, sulla base delle informazioni disponibili, potrebbero essere valutate in futuro per sperimentazioni controllate. La loro eventuale idoneità dovrà comunque essere verificata attraverso rilievi di campo, analisi aziendali, verifiche sanitarie, valutazioni faunistiche e approfondimenti sulla gestione dei suoli.

#### Ambiti utilizzabili solo con forti cautele

Sono aree nelle quali la presenza di limitazioni pedologiche, morfologiche o vegetazionali impone una valutazione molto prudente. In questi casi, eventuali sperimentazioni dovranno prevedere: bassi carichi; rotazioni; periodi di permanenza limitati; recinzioni adeguate; protezione della rinnovazione; punti di alimentazione e abbeverata gestiti; monitoraggio del suolo; controllo sanitario; raccordo con competenze veterinarie e faunistiche.

#### Ambiti da escludere in via preliminare

Sono aree che, per condizioni di fragilità, sensibilità ambientale o incompatibilità potenziale, non dovrebbero essere considerate nella fase iniziale per progetti suinicoli agroforestali. Possono rientrare in questa categoria: aree a elevata pendenza; suoli superficiali o fortemente erodibili; zone umide; habitat sensibili; superfici con rinnovazione forestale vulnerabile; aree a elevata valenza conservazionistica; ambiti in cui la gestione sanitaria e faunistica risulti particolarmente complessa.

#### Output tecnico proposto per il gruppo di lavoro

Il contributo agro-forestale e pedologico può essere finalizzato in quattro output operativi, coerenti con la natura preliminare del lavoro.

#### Nota metodologica

La nota metodologica serve a chiarire che il lavoro fornisce indirizzi e non decisioni operative definitive. Deve descrivere: fonti utilizzate;

<!-- pagina 195 -->

scala di analisi; metodo di lettura; limiti del quadro conoscitivo; criteri di interpretazione; significato preliminare delle valutazioni.

#### Schede comunali preliminari

Per ciascun Comune può essere predisposta una scheda con struttura omogenea, articolata in: sintesi dell’uso del suolo; principali caratteri pedologici; lettura della matrice pedologia × uso del suolo; implicazioni preliminari per la filiera bosco-sughero; implicazioni preliminari per la filiera suinicola agroforestale; criticità o condizioni di attenzione; opportunità da approfondire; indicazioni per successive verifiche. Le schede non dovranno attribuire idoneità definitive, ma fornire una base comparabile per orientare il confronto tra Comuni.

#### Matrice preliminare di vocazionalità e compatibilità

La matrice avrà la funzione di confrontare i Comuni rispetto ad alcune dimensioni tecniche: vocazione forestale e sughericola; presenza di aree agro-silvo-pastorali; potenziale interesse per progetti pilota; fragilità pedologica; sensibilità ambientale; necessità di approfondimento; priorità preliminare di attenzione. La matrice dovrà essere costruita come strumento di orientamento, non come graduatoria rigida.

#### Linee di indirizzo per successive progettazioni

Il contributo potrà infine indicare alcune linee di lavoro da sviluppare successivamente, riferite a: gestione sostenibile delle sugherete; recupero di aree forestali e agroforestali; eventuali progetti pilota suinicoli controllati; raccordo con operatori locali; verifiche ambientali e faunistiche; governance di filiera; tracciabilità e valorizzazione commerciale; connessione con turismo rurale, ristorazione e mercato premium. Anche in questo caso, le linee proposte dovranno essere intese come input da sviluppare, non come strategie già definite.

#### Aspetti da approfondire nelle successive fasi progettuali

Il presente contributo, per sua natura, non esaurisce il quadro conoscitivo necessario alla progettazione attuativa. Gli aspetti che risultano ancora preliminari o non pienamente definiti non rappresentano una criticità del lavoro, ma costituiscono il naturale sviluppo di un’analisi orientativa finalizzata a successivi progetti di dettaglio. Le analisi su uso del suolo, pedologia e matrici territoriali consentono di individuare tendenze, condizioni favorevoli, criticità potenziali e ambiti meritevoli di attenzione. Tuttavia, la

<!-- pagina 196 -->

scala e la natura dei dati disponibili non consentono, in questa fase, di assumere decisioni operative sitospecifiche. Pertanto, gli elementi emersi dal presente lavoro devono essere intesi come input tecnici preliminari per: studi di fattibilità; piani di gestione forestale; progetti pilota; contratti di filiera; disciplinari produttivi; approfondimenti aziendali; verifiche ambientali e faunistiche; analisi economiche; strumenti di governance territoriale.

#### Approfondimenti sulla filiera bosco-sughero

Le valutazioni preliminari relative alla filiera sughericola dovranno essere integrate, nelle fasi successive, con analisi specifiche su: distribuzione effettiva delle sugherete; delimitazione cartografica aggiornata; stato vegetativo, fitosanitario e produttivo; presenza di rinnovazione naturale; accessibilità delle superfici; assetti proprietari; presenza di piani di gestione; turni di decortica; operatori attivi; rapporto tra produzione primaria, trasformazione e commercializzazione. Tali approfondimenti saranno necessari per passare da una lettura territoriale generale a eventuali programmi operativi di gestione e valorizzazione.

#### Approfondimenti sulla filiera suinicola agroforestale

Le ipotesi relative alla filiera suinicola agroforestale dovranno essere oggetto di verifiche successive. Nel presente lavoro non vengono definiti carichi, localizzazioni puntuali o modelli gestionali rigidi. Vengono invece individuate condizioni da verificare per eventuali sperimentazioni successive. In particolare, sarà necessario approfondire: presenza di aziende agricole e zootecniche interessate; disponibilità di superfici effettivamente gestibili; compatibilità pedologica e vegetazionale a scala aziendale; sostenibilità dei carichi animali; rischio di erosione e compattamento; protezione della rinnovazione forestale; disponibilità idrica; infrastrutture minime; biosicurezza; interazioni con fauna selvatica; possibilità di macellazione, trasformazione e commercializzazione; costruzione di un eventuale disciplinare produttivo.

#### Approfondimenti ambientali, faunistici e vincolistici

<!-- pagina 197 -->

La compatibilità tra filiere produttive, tutela ambientale e biodiversità dovrà essere oggetto di specifici approfondimenti nelle successive fasi progettuali. Tali aspetti devono essere considerati condizioni tecniche da affrontare prima di qualunque progettazione attuativa. Sarà necessario verificare: presenza e delimitazione di siti Natura 2000, ZPS, ZSC o altre aree tutelate; habitat presenti e relativo stato di conservazione; specie faunistiche di interesse conservazionistico; interazioni tra allevamento, fauna selvatica e rischio sanitario; vincoli forestali, paesaggistici, idrogeologici, urbanistici e sanitari; rischio incendio; possibili misure di mitigazione; sistemi di monitoraggio ambientale.

#### Approfondimenti pedologici e agronomici a scala di dettaglio

Le informazioni pedologiche disponibili consentono una lettura territoriale generale, ma non sostituiscono rilievi sito-specifici. Per eventuali interventi operativi sarà necessario approfondire: verifica in campo delle unità pedologiche; profondità utile; tessitura; pietrosità e rocciosità; drenaggio; suscettibilità all’erosione; rischio di compattamento; capacità di sostenere pascolo o allevamento estensivo; compatibilità tra suolo, copertura vegetale e pendenza; necessità di opere di protezione del suolo o regimazione idrica. Questi approfondimenti saranno particolarmente importanti nelle aree che il presente lavoro individua come potenzialmente favorevoli o meritevoli di sperimentazione.

#### Approfondimenti socioeconomici e di governance

Le indicazioni relative alla valorizzazione economica delle filiere dovranno essere integrate con analisi specifiche sugli attori locali, sui mercati e sui modelli organizzativi. In particolare, sarà necessario approfondire: censimento di proprietari forestali, aziende agricole, allevatori, trasformatori e imprese sughericole; disponibilità degli operatori a partecipare a percorsi di filiera; sostenibilità economica dei progetti pilota; domanda potenziale del mercato turistico e ristorativo; rapporti con operatori della Costa Smeralda, Santa Teresa Gallura e Palau; strumenti di governance; eventuali accordi territoriali; contratti di filiera; disciplinari; marchio territoriale; indicatori economici, ambientali e sociali per il monitoraggio. Anche in questo caso, il presente lavoro non definisce un assetto organizzativo definitivo, ma fornisce elementi preliminari per impostare il confronto con gli attori territoriali.

#### Messaggio tecnico da portare al tavolo di lavoro

Il contributo agro-forestale e pedologico propone di fondare la strategia della Green Community su una lettura integrata del territorio, evitando interventi indifferenziati e costruendo invece un quadro di

<!-- pagina 198 -->

orientamento basato su dati territoriali, vocazioni, limitazioni e condizioni di compatibilità. La filiera boscosughero rappresenta l’asse identitario, forestale e produttivo principale. La filiera suinicola agroforestale può costituire una possibile integrazione, ma solo se progettata in modo controllato, tracciato, compatibile con i suoli, coerente con gli habitat e sostenibile sotto il profilo sanitario, ambientale ed economico. Il valore del presente contributo non consiste nel definire soluzioni già chiuse, ma nel fornire: una prima base tecnica condivisa; criteri per leggere il territorio; elementi per individuare priorità; indicazioni per selezionare temi da approfondire; input per progetti pilota; supporto alla costruzione di una governance territoriale informata. In questa prospettiva, il documento deve essere inteso come strumento preliminare di orientamento, utile al gruppo di lavoro per impostare le successive fasi progettuali con maggiore consapevolezza tecnica e territoriale.

#### Metodo per le schede comunali e matrice preliminare di valutazione

#### Finalità del documento

Il presente documento definisce il metodo preliminare per la costruzione delle schede comunali agroforestali, pedologiche e territoriali e della relativa matrice comparativa di valutazione nell’ambito del progetto GREEN COMMUNITIES Alta Gallura — UCAG 193. L’obiettivo non è attribuire idoneità definitive ai diversi territori comunali, ma predisporre uno strumento omogeneo di lettura capace di: organizzare le informazioni disponibili per ciascun Comune; confrontare i territori secondo criteri comuni; evidenziare vocazioni, limiti e condizioni di attenzione; individuare ambiti tematici e territoriali meritevoli di approfondimento; fornire input preliminari per successive progettazioni di dettaglio. Le schede comunali e la matrice comparativa dovranno quindi essere considerate strumenti di orientamento tecnico, utili al gruppo di lavoro per passare da una lettura descrittiva del territorio a una prima interpretazione funzionale rispetto alle filiere bosco-sughero, suinicola agroforestale e alle più ampie strategie di sviluppo rurale sostenibile.

#### Fonti informative utilizzate

La costruzione delle schede comunali si basa prioritariamente sui materiali forniti nell’ambito del lavoro, con particolare riferimento a: tabelle di uso del suolo per Comune; tabelle pedologiche per Comune; matrici di intersezione tra pedologia e uso del suolo; elaborazioni GIS disponibili; documentazione tecnica e progettuale caricata; nota illustrativa alla carta dei suoli della Sardegna; ulteriori materiali ambientali, forestali, faunistici o socioeconomici che potranno essere acquisiti nelle fasi successive. Le informazioni vengono utilizzate con un approccio coerente con la natura preliminare del lavoro. Quando i dati disponibili consentono solo valutazioni generali, le schede dovranno riportare formulazioni prudenziali quali:

<!-- pagina 199 -->

“potenzialmente favorevole”; “da approfondire”; “compatibile solo con limitazioni”; “da verificare a scala di dettaglio”; “informazione non disponibile nei materiali analizzati”. Questo accorgimento è importante per evitare che la scheda comunale venga interpretata come uno strumento prescrittivo o localizzativo definitivo.

#### Struttura standard della scheda comunale

Per garantire omogeneità, ogni Comune dovrà essere analizzato attraverso una scheda strutturata secondo otto sezioni.

#### Identificazione del Comune

Contenuti da inserire: nome del Comune; collocazione nel sistema territoriale dell’Alta Gallura; eventuale ruolo prevalente nel progetto, se desumibile dai dati disponibili; elementi territoriali distintivi, se documentati.

#### Funzione della sezione

Questa parte introduce il Comune e ne colloca sinteticamente il ruolo all’interno del quadro intercomunale.

#### Formula tipo

Il Comune di [nome] viene analizzato nell’ambito del quadro territoriale UCAG 193 con riferimento alle componenti di uso del suolo, pedologia e potenziali relazioni con le filiere bosco-sughero e suinicola agroforestale. Le valutazioni riportate hanno carattere preliminare e dovranno essere verificate nelle successive fasi di dettaglio.

#### Sintesi dell’uso del suolo

Contenuti da inserire: principali classi di uso del suolo presenti; peso relativo delle superfici forestali; presenza di aree agro-silvo-pastorali; presenza di pascoli, seminativi o colture permanenti; superfici naturali o seminaturali; ambiti urbanizzati o infrastrutturali; eventuali elementi di frammentazione o continuità territoriale.

Lettura da sviluppare: Questa sezione deve rispondere a tre domande: Qual è l’assetto territoriale prevalente del Comune? Il Comune presenta una struttura più forestale, agricola, pastorale, costiera, interna o mista? Esistono usi del suolo potenzialmente rilevanti per filiera sughero o filiera suinicola agroforestale? Formula tipo: Dai dati di uso del suolo emerge un assetto comunale caratterizzato dalla presenza di [classi prevalenti]. Tali elementi indicano una possibile rilevanza del Comune rispetto a [gestione forestale / superfici agro-silvo-pastorali / aree rurali / ambiti da tutelare], da approfondire nelle successive fasi progettuali.

<!-- pagina 200 -->

### 3.3 Sintesi delle principali unità pedologiche

Contenuti da inserire: principali classi o unità pedologiche presenti; caratteristiche generali dei suoli; eventuali limitazioni; presenza di suoli superficiali, rocciosi, pietrosi, erodibili o poco evoluti; presenza di suoli più profondi o potenzialmente favorevoli a usi agro-silvo-pastorali; condizioni di drenaggio o idromorfia, se disponibili; implicazioni generali per forestazione, pascolo e gestione del suolo. Lettura da sviluppare: Questa sezione deve chiarire quali condizioni pedologiche possono favorire o limitare le attività oggetto del progetto. Formula tipo: Le informazioni pedologiche disponibili indicano la presenza prevalente di [unità/classi]. Tali condizioni suggeriscono [potenzialità/limitazioni] rispetto alla gestione forestale, alla stabilità delle coperture vegetali e all’eventuale utilizzo agro-silvo-pastorale. La valutazione resta preliminare e richiede verifiche di campo per eventuali interventi puntuali.

#### Lettura della matrice pedologia × uso del suolo

Contenuti da inserire: principali combinazioni tra suolo e uso attuale; superfici forestali su determinate classi pedologiche; pascoli o aree agro-silvo-pastorali su suoli fragili o favorevoli; aree naturali su suoli con funzione protettiva; eventuali usi potenzialmente incoerenti con le caratteristiche dei suoli; condizioni da mantenere, migliorare o approfondire. Lettura da sviluppare: Questa è la sezione più importante dal punto di vista interpretativo. Non basta elencare i dati: occorre leggere se l’uso del suolo appare coerente con la pedologia. Domande guida: Le aree forestali insistono su suoli che suggeriscono funzione produttiva, protettiva o mista? Le aree pascolive si trovano su suoli potenzialmente vulnerabili? Le aree agro-silvo-pastorali possono sostenere usi integrati o richiedono limitazioni? Esistono combinazioni che suggeriscono opportunità di recupero o riqualificazione? Esistono combinazioni che sconsigliano pressioni produttive aggiuntive? Formula tipo: L’incrocio tra pedologia e uso del suolo evidenzia la presenza di [combinazioni principali]. Tali combinazioni suggeriscono una prevalente funzione [produttiva/protettiva/mista] delle superfici analizzate. In particolare, gli ambiti in cui [uso del suolo] insiste su [classe pedologica] dovranno essere considerati con attenzione nelle successive fasi, soprattutto in relazione a rischio erosivo, compattamento, gestione della copertura vegetale e compatibilità con eventuali usi agro-zootecnici.

#### Implicazioni preliminari per la filiera bosco-sughero

Contenuti da inserire: presenza documentata o potenziale di superfici forestali compatibili con sugherete; eventuale ruolo del Comune nella filiera sughericola; condizioni favorevoli alla gestione forestale; superfici da recuperare, qualificare o mantenere con funzione protettiva;

<!-- pagina 201 -->

necessità di dati integrativi su stato vegetativo, produttività e decortica; possibili relazioni con trasformazione, artigianato, turismo o paesaggio. Lettura da sviluppare: La valutazione deve restare preliminare. Non va dichiarata l’idoneità produttiva della sughereta se non documentata. Formula tipo: In relazione alla filiera bosco-sughero, il Comune presenta elementi di interesse connessi a [aree forestali / continuità agroforestale / potenziale presenza di sugherete / ruolo territoriale]. Le informazioni disponibili consentono di segnalare una potenziale rilevanza del Comune, ma non permettono ancora di definire stato produttivo, turni di decortica, qualità del sughero o organizzazione della proprietà. Tali aspetti dovranno essere oggetto di successivi approfondimenti.

#### Implicazioni preliminari per la filiera suinicola agroforestale

Contenuti da inserire: presenza di aree agro-silvo-pastorali; superfici potenzialmente gestibili in modo controllato; limiti pedologici all’allevamento semibrado; rischi di erosione, compattamento o degrado del cotico erboso; eventuali interferenze con rinnovazione forestale o habitat sensibili; necessità di verifiche sanitarie, faunistiche e aziendali; possibilità di sviluppo come progetto pilota. Lettura da sviluppare: La scheda non deve “assegnare” il suino a un Comune, ma indicare se esistono condizioni che meritano approfondimento. Formula tipo: Per quanto riguarda la possibile filiera suinicola agroforestale, il Comune presenta [condizioni potenzialmente favorevoli / condizioni da valutare con cautela / limitazioni significative]. L’eventuale utilizzo di superfici agroforestali o pascolive dovrà essere verificato a scala aziendale, considerando caratteristiche dei suoli, accessibilità, recintabilità, disponibilità idrica, biosicurezza, interazioni faunistiche e compatibilità con la copertura vegetale.

#### Criticità e condizioni di attenzione

Contenuti da inserire: fragilità pedologiche; rischio erosione; suoli superficiali o rocciosi; pendenza; sensibilità ambientale; habitat o aree tutelate; rischio incendio; pressione antropica o turistica; frammentazione fondiaria; carenza di dati specifici; limiti infrastrutturali o gestionali. Formula tipo:

<!-- pagina 202 -->

Le principali condizioni di attenzione riguardano [criticità]. Tali aspetti non precludono necessariamente lo sviluppo di interventi futuri, ma richiedono verifiche dedicate e una progettazione prudenziale, soprattutto nel caso di iniziative agro-zootecniche, gestione forestale attiva o interventi in aree sensibili.

#### Opportunità e indirizzi per successive fasi progettuali

Contenuti da inserire: temi da approfondire; possibili aree pilota, se desumibili solo in modo generale; soggetti da coinvolgere; dati da acquisire; verifiche tecniche necessarie; eventuali connessioni con filiera sughero, suino, turismo, artigianato o servizi ecosistemici.

Formula tipo: Alla luce delle informazioni disponibili, il Comune può essere considerato meritevole di approfondimento rispetto a [tema]. Le successive fasi progettuali dovranno verificare [dati/condizioni], coinvolgendo [soggetti] e valutando la fattibilità tecnica, economica, ambientale e gestionale degli interventi.

#### Modello sintetico di scheda comunale

Di seguito si propone un modello standard utilizzabile per ciascun Comune.

#### Scheda comunale preliminare — Comune di [Nome Comune]

#### Inquadramento sintetico

Il Comune di [Nome] viene analizzato nell’ambito del progetto GREEN COMMUNITIES Alta Gallura — UCAG 193 con riferimento alle componenti di uso del suolo, pedologia, assetto agro-forestale e possibili relazioni con le filiere bosco-sughero e suinicola agroforestale. Le valutazioni riportate hanno carattere preliminare e sono finalizzate a orientare successive verifiche progettuali.

#### Sintesi dell’uso del suolo

Dai dati disponibili emerge la presenza prevalente di: [classe uso suolo 1]; [classe uso suolo 2]; [classe uso suolo 3]; [classe uso suolo 4]. L’assetto territoriale appare caratterizzato da [prevalenza forestale / agro-silvo-pastorale / agricola / costiera / mista], con possibili implicazioni per [gestione forestale / filiera sughericola / pascolo / filiera suinicola / tutela ambientale].

#### Sintesi pedologica

Le principali unità pedologiche rilevate sono: [unità pedologica 1]; [unità pedologica 2]; [unità pedologica 3]. Tali condizioni suggeriscono [potenzialità / limitazioni / necessità di cautela] rispetto agli usi agro-silvopastorali e forestali.

#### Lettura della matrice pedologia × uso del suolo

Le principali combinazioni emerse dall’intersezione tra pedologia e uso del suolo sono: [combinazione 1];

<!-- pagina 203 -->

[combinazione 2]; [combinazione 3]. La lettura preliminare suggerisce che [interpretazione tecnica], con particolare attenzione a [erosione / compattamento / rinnovazione forestale / funzione protettiva / recupero agroforestale].

#### Implicazioni per la filiera bosco-sughero

Il Comune presenta [elevato / medio / limitato / da verificare] interesse preliminare per la filiera boscosughero in relazione a: [elemento 1]; [elemento 2]; [elemento 3]. Le successive fasi dovranno approfondire distribuzione effettiva delle sugherete, stato vegetativo, accessibilità, proprietà, gestione e rapporti con gli operatori della filiera.

#### Implicazioni per la filiera suinicola agroforestale

Il Comune presenta [condizioni potenzialmente favorevoli / condizioni da verificare / limitazioni rilevanti] per eventuali sperimentazioni suinicole agroforestali controllate. Gli aspetti da verificare riguardano: compatibilità pedologica; accessibilità e recintabilità; disponibilità idrica; rischio di erosione e compattamento; tutela della rinnovazione forestale; biosicurezza; interazioni con fauna selvatica; disponibilità di operatori aziendali.

#### Criticità e condizioni di attenzione

Le principali condizioni di attenzione riguardano: [criticità 1]; [criticità 2]; [criticità 3]. Tali aspetti dovranno essere considerati nelle successive fasi progettuali prima di definire interventi puntuali.

#### Opportunità e approfondimenti successivi

Il Comune può essere oggetto di approfondimento per: [opportunità 1]; [opportunità 2]; [opportunità 3]. Le verifiche successive dovranno riguardare [dati da acquisire / rilievi di campo / coinvolgimento operatori / analisi economiche / verifiche faunistiche / vincoli ambientali].

#### Matrice preliminare di valutazione intercomunale

La matrice preliminare ha la funzione di sintetizzare e confrontare i Comuni secondo criteri comuni. Non deve essere interpretata come una graduatoria definitiva, ma come strumento di supporto al confronto tecnico.

#### Criteri proposti

Si propongono i seguenti criteri di lettura.

<!-- pagina 204 -->

| Criterio | Significato | Fonte principale | Tipo di valutazione |
|---|---|---|---|
| Vocazione forestale/sughericola preliminare | Presenza o potenziale presenza di aree forestali e agroforestali rilevanti per la filiera bosco-sughero | Uso del suolo, matrice UdS × pedologia, dati forestali successivi | Alta / Media / Bassa / Da verificare |
| Presenza di aree agro-silvo-pastorali | Rilevanza di pascoli, aree agricole estensive, mosaici rurali e superfici seminaturali | Uso del suolo | Alta / Media / Bassa / Da verificare |
| Compatibilità pedologica preliminare | Condizioni generali dei suoli rispetto a usi forestali, pascolivi o agro-zootecnici | Pedologia, matrice UdS × pedologia | Favorevole / Limitata / Critica / Da verificare |
| Fragilità del suolo | Presenza di limitazioni quali erosione, superficialità, rocciosità, pendenza, compattamento potenziale | Pedologia, cartografia, rilievi successivi | Alta / Media / Bassa / Da verificare |
| Interesse per filiera suinicola agroforestale | Presenza di condizioni da approfondire per eventuali progetti pilota controllati | Uso del suolo, pedologia, dati aziendali successivi | Alto / Medio / Basso / Da verificare |
| Sensibilità ambientale | Presenza o possibile presenza di habitat, vincoli, aree tutelate o elementi di biodiversità | Dati ambientali e faunistici da integrare | Alta / Media / Bassa / Da verificare |
| Priorità di approfondimento | Necessità di ulteriori verifiche per trasformare l’indicazione preliminare in progetto di dettaglio | Sintesi tecnica | Prioritaria / Ordinaria / Bassa |

<!-- tabella: tables/p204-t0.csv (ok) -->

#### Scala di valutazione

Per evitare una falsa precisione, si propone una scala qualitativa semplice. Alta Indica una condizione chiaramente rilevante sulla base dei dati disponibili. Non equivale a idoneità definitiva, ma segnala un tema prioritario da approfondire. Media Indica una condizione presente ma non dominante, oppure un potenziale che necessita di verifiche ulteriori. Bassa Indica una condizione limitata o marginale rispetto al tema considerato.

#### Da verificare

Indica che i dati disponibili non consentono una valutazione attendibile, oppure che l’informazione deve essere integrata con fonti aggiuntive. Critica Indica la presenza di condizioni che richiedono particolare cautela e che potrebbero limitare o escludere alcuni usi nelle successive fasi progettuali.

<!-- pagina 205 -->

#### Modello di matrice intercomunale

| Com une | Vocazi one forestale/sug hericola preliminare | A ree agro- silvo- pastora li | Comp atibilità pedologica preliminare | Fr agilità del suolo | Inte resse per filiera suinicola agroforest ale | Sen sibilità ambientale | Prio rità di approfondi mento |
|---|---|---|---|---|---|---|---|
| Aggiu s | Da compilare | D a compilar e | Da compilare | Da compilare | Da compilare | Da compilare | Da compilare |
| Aglie ntu | Da compilare | D a compilar e | Da compilare | Da compilare | Da compilare | Da compilare | Da compilare |
| Bade si | Da compilare | D a compilar e | Da compilare | Da compilare | Da compilare | Da compilare | Da compilare |
| Borti giadas | Da compilare | D a compilar e | Da compilare | Da compilare | Da compilare | Da compilare | Da compilare |
| Cala ngianus | Da compilare | D a compilar e | Da compilare | Da compilare | Da compilare | Da compilare | Da compilare |
| Luog osanto | Da compilare | D a compilar e | Da compilare | Da compilare | Da compilare | Da compilare | Da compilare |
| Luras | Da compilare | D a compilar e | Da compilare | Da compilare | Da compilare | Da compilare | Da compilare |
| Sant a Teresa Gallura | Da compilare | D a compilar e | Da compilare | Da compilare | Da compilare | Da compilare | Da compilare |
| Temp io Pausania | Da compilare | D a compilar e | Da compilare | Da compilare | Da compilare | Da compilare | Da compilare |

<!-- tabella: tables/p205-t0.csv (ok) -->

<!-- pagina 206 -->

| Com une | Vocazi one forestale/sug hericola preliminare | A ree agro- silvo- pastora li | Comp atibilità pedologica preliminare | Fr agilità del suolo | Inte resse per filiera suinicola agroforest ale | Sen sibilità ambientale | Prio rità di approfondi mento |
|---|---|---|---|---|---|---|---|
| Trinit à d’Agultu e Vignola | Da compilare | D a compilar e | Da compilare | Da compilare | Da compilare | Da compilare | Da compilare |
| Vidda lba | Da compilare | D a compilar e | Da compilare | Da compilare | Da compilare | Da compilare | Da compilare |

<!-- tabella: tables/p206-t0.csv (ok) -->

#### Criteri interpretativi per filiera bosco-sughero

Per la filiera bosco-sughero, la valutazione preliminare dovrà considerare: presenza di superfici forestali; presenza documentata o potenziale di sugherete; coerenza tra copertura forestale e caratteristiche pedologiche; stabilità della copertura vegetale; eventuale funzione protettiva dei boschi; accessibilità; continuità territoriale delle aree forestali; possibilità di integrazione con trasformazione, artigianato e turismo; necessità di dati specifici su stato produttivo e fitosanitario. La classificazione dovrà essere prudente. Esempio di formulazione: Il Comune mostra una vocazione preliminare di interesse per la filiera bosco-sughero in relazione alla presenza di superfici forestali e agroforestali. Tuttavia, la definizione di una reale idoneità produttiva richiede approfondimenti sulla distribuzione effettiva delle sugherete, sullo stato vegetativo, sulla proprietà, sui turni di decortica e sugli operatori presenti.

#### Criteri interpretativi per filiera suinicola agroforestale

Per la filiera suinicola agroforestale, la valutazione preliminare dovrà considerare: presenza di aree agro-silvo-pastorali; presenza di pascoli o mosaici rurali; compatibilità pedologica generale; rischio di erosione; rischio di compattamento; vulnerabilità della copertura vegetale; presenza di rinnovazione forestale; possibilità di recinzione e controllo; accessibilità; disponibilità idrica; potenziali interferenze con habitat sensibili; necessità di valutazioni sanitarie e faunistiche.

<!-- pagina 207 -->

La valutazione non dovrà definire carichi animali, numero di capi o superfici puntuali. Tali aspetti appartengono a successive fasi progettuali e aziendali. Esempio di formulazione: Il Comune presenta condizioni che potrebbero essere approfondite in relazione a una possibile filiera suinicola agroforestale controllata. Tale indicazione non equivale a idoneità operativa, poiché la fattibilità dovrà essere verificata a scala aziendale, con particolare attenzione a suolo, copertura vegetale, recintabilità, biosicurezza, disponibilità idrica e interazioni con la fauna selvatica.

#### Utilizzo operativo delle schede e della matrice

Le schede comunali e la matrice intercomunale dovranno essere utilizzate come strumenti di lavoro progressivi. Nella prima fase, serviranno a: organizzare le informazioni disponibili; individuare i Comuni con maggiore interesse preliminare; distinguere temi territoriali ricorrenti; evidenziare le principali condizioni di attenzione; selezionare gli approfondimenti prioritari. Nelle fasi successive, potranno essere integrate con: rilievi di campo; dati forestali di dettaglio; dati aziendali; dati faunistici; vincoli ambientali; informazioni economiche; confronto con proprietari e operatori locali; analisi di mercato; verifiche tecnico-sanitarie. Il loro valore principale consiste nel fornire una base metodologica comune al gruppo di lavoro, evitando valutazioni frammentarie o non confrontabili tra Comuni.

#### Output atteso

L’applicazione del presente metodo dovrà produrre: una scheda preliminare per ciascun Comune; una matrice intercomunale comparativa; una sintesi delle principali vocazioni territoriali; una lista di temi prioritari da approfondire; una prima indicazione degli ambiti più coerenti con successive progettazioni di dettaglio; una base tecnica condivisa per il confronto con enti, imprese, proprietari, allevatori, operatori della filiera sughericola e soggetti del sistema turistico-ristorativo. Il risultato finale non sarà una zonizzazione definitiva, ma un quadro preliminare di orientamento territoriale, utile per sostenere successive decisioni progettuali più puntuali, documentate e condivise

#### Prime linee operative su filiera sughero e filiera suinicola agroforestale

#### Finalità del documento

Il presente documento definisce una prima traccia operativa per due assi tematici del progetto GREEN COMMUNITIES Alta Gallura — UCAG 193: la valorizzazione della filiera bosco-sughero;

<!-- pagina 208 -->

la verifica preliminare di una possibile filiera suinicola agroforestale controllata. Il documento ha carattere preliminare e orientativo. Non definisce interventi localizzati, carichi animali, piani di gestione puntuali o strategie definitive. Fornisce invece una prima organizzazione delle linee di lavoro da sottoporre al gruppo tecnico e da sviluppare in successive fasi di progettazione. L’impostazione è coerente con la finalità dell’incarico, che prevede la produzione di un report tecnicostrategico di sviluppo sostenibile per il territorio UCAG 193, con focus su filiera bosco-sughero, sviluppo territoriale integrato, pianificazione ambientale e socioeconomica e strumenti replicabili per successive progettualità territoriali.

#### Parte I — Filiera bosco-sughero

#### Significato strategico della filiera bosco-sughero

La filiera bosco-sughero rappresenta l’asse più identitario del contributo agro-forestale. Non deve essere letta esclusivamente come filiera produttiva legata all’estrazione del sughero, ma come sistema territoriale multifunzionale. La sughereta svolge infatti funzioni diverse: produzione di materia prima; presidio del paesaggio rurale e forestale; tutela del suolo; conservazione della biodiversità; prevenzione del degrado e dell’abbandono; contenimento del rischio incendio, se gestita in modo attivo; identità culturale e territoriale; connessione con artigianato, design, bioedilizia, packaging e turismo esperienziale. Il progetto prevede esplicitamente, tra gli obiettivi secondari, il rafforzamento e la chiusura della filiera sughero, con possibile sviluppo di uno specifico distretto rurale del sughero, da valutare in termini di complementarità e non sovrapposizione rispetto al distretto produttivo esistente.

#### Obiettivo operativo preliminare

L’obiettivo operativo preliminare non è ancora predisporre un piano di gestione delle sugherete, ma costruire le condizioni conoscitive e organizzative per farlo in una fase successiva. La linea proposta è: passare dal dato territoriale generale sulla presenza di sugherete a una classificazione funzionale della risorsa, distinguendo superfici produttive, protettive, degradate, abbandonate, recuperabili e multifunzionali. Questa impostazione consente di evitare interventi indistinti e di costruire una strategia aderente alle condizioni reali dei territori comunali.

#### Comuni prioritari per la filiera bosco-sughero

Sulla base delle schede e della matrice preliminare, i Comuni possono essere distinti in tre gruppi funzionali.

| Gruppo | Comuni | Ruolo preliminare |
|---|---|---|
| Poli prioritari della filiera sughericola | Calangianus, Tempio Pausania | Comuni cardine per consistenza della risorsa, ruolo territoriale e possibile governance della filiera. |

<!-- tabella: tables/p208-t0.csv (ok) -->

<!-- pagina 209 -->

| Gruppo | Comuni | Ruolo preliminare |
|---|---|---|
| Comuni sughericoli integrabili | Luras, Aggius, Luogosanto | Ambiti utili per gestione multifunzionale, integrazione agroforestale, recupero e sperimentazioni mirate. |
| Comuni con ruolo forestale, paesaggistico o commerciale secondario | Bortigiadas, Aglientu, Trinità d’Agultu e Vignola, Viddalba, Badesi, Santa Teresa Gallura | Ruolo differenziato: gestione forestale protettiva, paesaggio, turismo, mercato, comunicazione territoriale. |

<!-- tabella: tables/p209-t0.csv (ok) -->

Questa classificazione resta preliminare e deve essere validata con dati più puntuali su distribuzione delle sugherete, stato vegetativo, proprietà, accessibilità e operatori attivi.

#### Linee operative preliminari per il sughero

#### Mappatura aggiornata delle sugherete

Finalità Costruire una base cartografica aggiornata e affidabile della risorsa sughericola.

#### Attività preliminari

Verifica delle superfici classificate come sugherete nelle tabelle di uso del suolo. Incrocio con pedologia, pendenza, accessibilità e copertura forestale. Distinzione tra sugherete continue, frammentate, degradate o miste. Verifica con eventuali dati AGRIS, Forestas, Comuni e operatori locali. Controlli di campo su aree campione.

#### Soggetti coinvolti

UCAG e Comuni. Tecnici GIS. Agronomi e forestali. Pedologi. Proprietari forestali. Operatori della filiera.

#### Output atteso

Carta aggiornata delle sugherete. Prima classificazione per Comune. Base tecnica per successive aree pilota.

#### Classificazione funzionale delle sugherete

Finalità Distinguere le diverse funzioni delle sugherete, evitando di considerarle tutte come superfici produttive equivalenti.

#### Categorie preliminari proposte

| Categoria | Descrizione | Indirizzo successivo |
|---|---|---|
| Sugherete produttive | Formazioni potenzialmente idonee a gestione produttiva regolare | Verifica turni, qualità, operatori, accessibilità |
| Sugherete protettive | Formazioni su suoli fragili, versanti o aree sensibili | Gestione conservativa, tutela del suolo, prevenzione degrado |

<!-- tabella: tables/p209-t1.csv (ok) -->

<!-- pagina 210 -->

| Categoria | Descrizione | Indirizzo successivo |
|---|---|---|
| Sugherete da recuperare | Formazioni degradate, sottoutilizzate o abbandonate | Interventi di miglioramento, rinnovazione, gestione del sottobosco |
| Sugherete multifunzionali | Formazioni con valore produttivo, paesaggistico, turistico o didattico | Integrazione con turismo, educazione, artigianato, prevenzione incendi |
| Aree non prioritarie | Superfici marginali o non gestibili nella fase iniziale | Monitoraggio o esclusione temporanea |

<!-- tabella: tables/p210-t0.csv (ok) -->

#### Output atteso

Carta funzionale delle sugherete. Elenco delle superfici candidate a progettazione di dettaglio. Criteri di priorità per interventi futuri.

#### Verifica dello stato vegetativo, fitosanitario e produttivo

Finalità Comprendere se le sugherete siano effettivamente in condizioni tali da sostenere interventi di valorizzazione.

#### Aspetti da approfondire

Vitalità delle piante. Densità e struttura del soprassuolo. Presenza di rinnovazione naturale. Eventuali deperimenti. Qualità del fusto. Stato della corteccia. Presenza di danni da incendio, pascolo, fauna o pratiche errate. Storia gestionale e turni di decortica.

#### Output atteso

Schede tecniche di valutazione per aree campione. Classificazione preliminare dello stato gestionale. Priorità di intervento.

#### Organizzazione degli attori della filiera

Finalità Capire se la risorsa sughero sia sostenuta da una filiera organizzata o se esistano colli di bottiglia gestionali, proprietari o commerciali.

#### Attori da censire

Proprietari forestali pubblici e privati. Imprese di utilizzazione forestale. Estrattori. Trasformatori. Artigiani. Imprese del design e packaging. Operatori turistici. Associazioni di categoria. Enti tecnici e di ricerca.

#### Temi da verificare

Disponibilità alla gestione coordinata.

<!-- pagina 211 -->

Presenza di manodopera qualificata. Fabbisogni formativi. Rapporti con il distretto produttivo esistente. Interesse verso certificazioni. Interesse verso accordi o contratti di filiera.

#### Output atteso

Mappa degli attori. Analisi dei fabbisogni. Prime ipotesi di accordo territoriale.

#### Valorizzazione del sughero locale

Finalità Ampliare il valore della filiera oltre la sola materia prima.

#### Ambiti di valorizzazione da approfondire

Trasformazione locale. Artigianato tradizionale. Design contemporaneo. Packaging sostenibile. Bioedilizia. Oggettistica e merchandising territoriale. Turismo esperienziale legato alla decortica. Eventi e percorsi didattici. Narrazione del paesaggio sughericolo.

#### Output atteso

Concept preliminare di valorizzazione territoriale. Individuazione di prodotti o servizi dimostrativi. Ipotesi di collegamento con turismo e ristorazione.

### 5.6 Certificazioni, tracciabilità e marchio territoriale

Finalità Costruire le condizioni per una riconoscibilità del sughero locale e della gestione sostenibile.

#### Temi da valutare

Certificazioni forestali. Tracciabilità della materia prima. Disciplinare territoriale. Marchio di Green Community. Collegamento con carbon farming e servizi ecosistemici. Indicatori ESG territoriali. L’indice dello studio prevede espressamente, nella parte sugli output e prospettive Green Communities, la valorizzazione delle filiere, il contratto di filiera, il distretto rurale del sughero, il GIS territoriale, le cartografie tematiche, le matrici uso del suolo/vincoli/vocazioni, carbon footprint, water footprint, carbon farming e servizi ecosistemici.

#### Output atteso

Schema preliminare di tracciabilità. Ipotesi di disciplinare. Valutazione di fattibilità per certificazioni.

<!-- pagina 212 -->

#### Filiera suinicola agroforestale

#### Significato strategico della filiera suinicola agroforestale

La filiera suinicola agroforestale è un tema potenzialmente innovativo, ma deve essere affrontato con impostazione prudenziale. La call operativa collega lo sviluppo di una filiera suinicola integrata alla gestione del sottobosco, alla riduzione della biomassa, alla prevenzione incendi e alla qualità delle sugherete, secondo una logica di integrazione tra gestione forestale e allevamento. Prevede inoltre la valorizzazione commerciale del suino sardo locale/gallurese verso mercati target come resort e turismo premium su Palau e Santa Teresa Gallura. Questa impostazione deve però essere tradotta in termini tecnici corretti: la filiera suinicola non deve essere proposta come uso generalizzato del bosco, ma come eventuale sperimentazione controllata, aziendale o interaziendale, compatibile con suoli, coperture vegetali, habitat, fauna, biosicurezza e capacità gestionale degli operatori.

#### Obiettivo operativo preliminare

L’obiettivo della fase attuale è verificare se esistano le condizioni per sviluppare uno o più progetti pilota. Non si devono ancora definire: superfici puntuali; numero di capi; carichi animali; localizzazioni definitive; disciplinari conclusivi; investimenti aziendali. Si devono invece individuare: Comuni e ambiti da approfondire; criteri minimi di compatibilità; condizioni di esclusione; soggetti da coinvolgere; dati mancanti; modello di verifica per eventuali progetti pilota.

#### Comuni prioritari per approfondimenti sulla filiera suinicola

| Categoria | Comuni | Lettura preliminare |
|---|---|---|
| Prioritari per verifica pilota | Luogosanto, Tempio Pausania, Luras, Aggius | Presenza di mosaici agro-silvo-pastorali, superfici agricole/pascolive e possibile integrazione con filiere territoriali. |
| Da valutare con cautela | Aglientu, Trinità d’Agultu e Vignola, Viddalba, Badesi | Presenza di superfici rurali o agricole, ma anche limiti ambientali, pedologici, paesaggistici o costieri. |
| Non prioritari per fase pilota produttiva | Bortigiadas, Calangianus, Santa Teresa Gallura | Bortigiadas per prevalente funzione forestale protettiva; Calangianus per priorità alla tutela/valorizzazione delle sugherete; Santa Teresa per ruolo prevalentemente turistico-commerciale. |

<!-- tabella: tables/p212-t0.csv (ok) -->

Questa distinzione non esclude future valutazioni puntuali, ma orienta la prima fase di approfondimento.

#### Linee operative preliminari per la filiera suinicola

#### Studio di prefattibilità tecnico-territoriale

<!-- pagina 213 -->

Finalità Verificare se il territorio disponga di condizioni minime per una filiera suinicola agroforestale controllata.

#### Attività preliminari

Individuazione di aziende agricole o zootecniche interessate. Verifica delle superfici disponibili. Analisi di accessibilità e recintabilità. Verifica della disponibilità idrica. Lettura pedologica a scala aziendale. Verifica di pendenze, erosione, compattamento e copertura vegetale. Prima analisi di vincoli, habitat e fauna. Valutazione preliminare della sostenibilità economica.

#### Output atteso

Studio di prefattibilità. Elenco di aziende o aree candidate. Criteri minimi per passare alla progettazione pilota.

#### Criteri minimi per le aree candidate

Le aree candidate dovranno possedere almeno alcune condizioni di base.

| Criterio | Indicazione preliminare |
|---|---|
| Gestibilità | Superfici controllabili, preferibilmente aziendali o interaziendali |
| Recintabilità | Possibilità di separare suini allevati e fauna selvatica |
| Accessibilità | Presenza di viabilità sufficiente per gestione e controllo |
| Disponibilità idrica | Acqua disponibile e gestibile |
| Compatibilità pedologica | Esclusione di suoli molto superficiali, erodibili o compattabili |
| Copertura vegetale | Evitare aree con rinnovazione forestale vulnerabile |
| Vincoli | Verifica preventiva di habitat, aree tutelate e norme urbanistiche |
| Biosicurezza | Possibilità di applicare protocolli sanitari rigorosi |
| Mercato | Collegamento realistico con trasformazione e vendita |

<!-- tabella: tables/p213-t0.csv (ok) -->

#### Criteri preliminari di esclusione

Dovranno essere escluse, almeno nella fase iniziale: aree a elevata pendenza; suoli superficiali, rocciosi o fortemente erodibili; aree con vegetazione rada su suoli fragili; zone umide o aree idromorfe; habitat sensibili; aree Natura 2000 senza verifica specifica; superfici con rinnovazione forestale vulnerabile; sugherete giovani o in fase di recupero; aree non recintabili; aree con elevato rischio di contatto con fauna selvatica; contesti nei quali non sia garantibile la biosicurezza.

<!-- pagina 214 -->

#### Modello gestionale da approfondire

Il modello più coerente, in questa fase, non è l’allevamento brado diffuso, ma un sistema estensivo controllato o semibrado regolato, con forte presidio aziendale. Elementi da approfondire: rotazione delle superfici; permanenza limitata degli animali; carichi molto contenuti e definiti solo a scala aziendale; recinzioni perimetrali e interne; punti di alimentazione e abbeverata mobili o gestiti; protezione della rinnovazione forestale; esclusione stagionale delle aree più vulnerabili; monitoraggio di suolo e cotico erboso; registro gestionale aziendale; controllo sanitario costante; tracciabilità degli animali e dei prodotti.

#### Biosicurezza, fauna e sanità animale

Finalità Evitare che la filiera generi rischi sanitari o conflitti con fauna selvatica.

#### Attività da sviluppare

Verifica presenza e distribuzione del cinghiale. Analisi del rischio di contatto tra suini allevati e fauna selvatica. Definizione di recinzioni idonee. Protocolli di ingresso/uscita animali. Gestione alimenti e acqua. Piano sanitario aziendale. Gestione carcasse e sottoprodotti. Controllo movimentazioni. Raccordo con servizi veterinari.

#### Soggetti coinvolti

Servizi veterinari. Faunisti. Allevatori. Agronomi. Tecnici forestali. Comuni. Enti competenti.

#### Output atteso

Protocollo preliminare di biosicurezza. Criteri sanitari per selezione aree pilota. Piano di monitoraggio.

#### Trasformazione e commercializzazione

La filiera suinicola ha senso solo se collegata a trasformazione e mercato. Non va impostata come aumento generico della produzione zootecnica, ma come produzione limitata, tracciata, identitaria e ad alto valore aggiunto.

#### Temi da approfondire

<!-- pagina 215 -->

Disponibilità di macellazione autorizzata. Laboratori di sezionamento e trasformazione. Stagionatura. Standard igienico-sanitari. Prodotti trasformati tipici. Marchio territoriale. Tracciabilità. Packaging. Canali di vendita. Ristorazione locale. Resort e hotellerie. Mercati premium della costa.

#### Output atteso

Schema preliminare di filiera prodotto. Analisi dei canali commerciali. Prime manifestazioni di interesse degli operatori.

#### Parte III — Sinergie tra filiera sughero e filiera suinicola

#### Possibili sinergie operative

Le due filiere non devono essere sovrapposte meccanicamente. La relazione tra sughero e suino è possibile solo se costruita su criteri tecnici precisi. Le sinergie più coerenti sono:

| Sinergia | Descrizione | Condizione |
|---|---|---|
| Gestione del mosaico agroforestale | Interventi coordinati su aree rurali, pascolive e forestali | Esclusione delle aree fragili e monitoraggio |
| Prevenzione incendi | Gestione biomassa tramite interventi forestali e, dove compatibile, pascolo controllato | Non attribuire al suino una funzione antincendio generalizzata |
| Valorizzazione paesaggio | Sugherete, pascoli e prodotti locali come identità territoriale | Connessione con turismo e comunicazione |
| Prodotti integrati | Sughero, carni locali, artigianato e gastronomia | Tracciabilità e standard qualitativi |
| Turismo esperienziale | Decortica, visite in sughereta, degustazioni, laboratori | Organizzazione, sicurezza e qualità dell’esperienza |
| Governance comune | Tavoli di filiera collegati ma distinti | Cabina di regia unica con competenze specialistiche |

<!-- tabella: tables/p215-t0.csv (ok) -->

#### Principio guida

La linea tecnica da mantenere è la seguente: il sughero rappresenta la filiera identitaria e forestale principale; il suino può rappresentare una filiera integrativa e sperimentale, da sviluppare solo dove le condizioni pedologiche, ambientali, aziendali, sanitarie ed economiche risultino compatibili. Questo principio consente di evitare due errori: ridurre la filiera sughero a semplice fondale paesaggistico; utilizzare il suino come soluzione generica per la gestione del bosco.

<!-- pagina 216 -->

#### Parte IV — Roadmap operativa preliminare

#### Azioni a breve termine

| Azione | Finalità | Soggetti coinvolti | Output |
|---|---|---|---|
| Verifica dati GIS su sugherete | Consolidare base conoscitiva | Tecnici GIS, agronomi, Comuni | Carta preliminare sugherete |
| Classificazione funzionale sugherete | Distinguere produttive/protettive/recupero | Forestali, pedologi, proprietari | Matrice funzionale |
| Censimento attori sughero | Capire filiera reale | Comuni, imprese, estrattori, trasformatori | Mappa attori |
| Individuazione aziende suinicole interessate | Valutare disponibilità alla sperimentazione | Allevatori, associazioni, Comuni | Elenco manifestazioni interesse |
| Verifica preliminare vincoli | Evitare conflitti ambientali | Tecnici, Comuni, enti competenti | Carta vincoli preliminare |
| Tavolo tecnico sughero | Avviare confronto dedicato | UCAG, Calangianus, Tempio, operatori | Verbale e agenda |
| Tavolo esplorativo suino | Valutare condizioni minime | UCAG, veterinari, allevatori, faunisti | Agenda di prefattibilità |

<!-- tabella: tables/p216-t0.csv (ok) -->

#### Azioni a medio termine

| Azione | Finalità | Output |
|---|---|---|
| Piano conoscitivo delle sugherete | Passare da uso del suolo a gestione | Atlante sugherete UCAG |
| Progetti pilota di recupero sugherete | Testare interventi sostenibili | Aree pilota e monitoraggio |
| Studio prefattibilità filiera suinicola | Valutare fattibilità reale | Documento tecnico-economico |
| Protocollo biosicurezza suino | Ridurre rischi sanitari | Linee guida e criteri minimi |
| Analisi economica filiere | Verificare sostenibilità | Business model preliminare |
| Disciplinare preliminare | Costruire qualità e identità | Bozza disciplinare sughero/suino |
| Accordi commerciali esplorativi | Collegare produzione e mercato | Manifestazioni interesse ristorazione/hotellerie |
| Sistema GIS condiviso | Aggiornare dati e decisioni | Database territoriale |

<!-- tabella: tables/p216-t1.csv (ok) -->

<!-- pagina 217 -->

#### Azioni a lungo termine

| Azione | Finalità | Output |
|---|---|---|
| Contratto di filiera sughero | Coordinare proprietari e operatori | Accordo territoriale |
| Distretto rurale del sughero | Rafforzare identità e governance | Studio di fattibilità |
| Filiera suinicola territoriale | Passare da pilota a modello stabile | Filiera tracciata e disciplinata |
| Marchio Green Community | Valorizzare prodotti e territorio | Marchio/disciplinare |
| Certificazioni | Aumentare valore e credibilità | Certificazione gestione/prodotto |
| Turismo esperienziale | Collegare territorio e mercato | Itinerari, eventi, pacchetti |
| Monitoraggio permanente | Misurare effetti | KPI ambientali, economici e sociali |

<!-- tabella: tables/p217-t0.csv (ok) -->

#### Indicatori preliminari di monitoraggio

#### Indicatori per la filiera bosco-sughero

| Ambito | Indicatore |
|---|---|
| Risorsa | Ettari di sugherete mappate e classificate |
| Gestione | Ettari con piano o intervento di gestione |
| Produzione | Quantità e qualità del sughero estratto |
| Conservazione | Presenza di rinnovazione naturale |
| Formazione | Numero operatori formati |
| Filiera | Numero imprese/proprietari coinvolti |
| Valore | Incremento valore prodotto locale |
| Sostenibilità | Aree certificate o in percorso di certificazione |

<!-- tabella: tables/p217-t1.csv (ok) -->

#### Indicatori per la filiera suinicola agroforestale

| Ambito | Indicatore |
|---|---|
| Aziende | Numero aziende candidate o aderenti |
| Superfici | Ettari verificati e classificati |
| Compatibilità | Aree escluse per fragilità o vincoli |
| Gestione | Presenza di recinzioni e rotazioni |
| Biosicurezza | Adozione protocolli sanitari |
| Ambiente | Monitoraggio erosione/compattamento |
| Produzione | Numero capi/prodotti solo dopo fase pilota |
| Mercato | Accordi con trasformatori e ristoratori |

<!-- tabella: tables/p217-t2.csv (ok) -->

<!-- pagina 218 -->

| Ambito | Indicatore |
|---|---|
| Tracciabilità | Sistema di identificazione prodotto |

<!-- tabella: tables/p218-t0.csv (ok) -->

#### Sintesi conclusiva

Le prime linee operative indicano due traiettorie distinte ma integrabili.

La filiera bosco-sughero rappresenta l’asse prioritario e più maturo del progetto. Le azioni successive dovranno concentrarsi su mappatura, classificazione funzionale, gestione sostenibile, organizzazione degli attori, valorizzazione della materia prima e raccordo con trasformazione, certificazioni, turismo e governance.

La filiera suinicola agroforestale rappresenta invece un’ipotesi da verificare con prudenza. Può diventare un elemento innovativo della Green Community solo se costruita come filiera pilota, controllata, tracciata, compatibile con suoli e habitat, sostenuta da protocolli sanitari rigorosi e collegata a trasformazione e mercato premium. La proposta operativa complessiva è quindi: partire dal consolidamento dei dati e dalla selezione di ambiti pilota, procedere con verifiche tecniche e coinvolgimento degli attori, e solo successivamente definire strumenti di filiera, disciplinari, accordi commerciali e governance stabile. In questo modo il contributo mantiene la propria natura preliminare, ma offre al gruppo di lavoro una traiettoria chiara per passare dalla lettura territoriale alla progettazione di dettaglio.

<!-- pagina 219 -->
