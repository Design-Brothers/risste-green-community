# -*- coding: utf-8 -*-
"""Genera i dataset territoriali di data/alta-gallura/ dallo studio RISSTE Parte 1.
Tutti i numeri sono trascritti dalle tabelle/testo delle pagine PDF indicate."""
import csv, json, os

OUT = "/Users/uxfra/Code/RISSTE/data/alta-gallura"
os.makedirs(OUT, exist_ok=True)

CAP08 = "Allegato II – Sistema Informativo Territoriale, cartografia e analisi biofisica dello spazio rurale"
CAP03 = "Seconda parte – Ambiente e territorio"
CAP04 = "Terza parte – I Comuni dell'Unione"

COMUNI = [
    # slug, nome, pagine scheda Allegato II, pagine Parte 3
    ("aggius", "Aggius", [156, 157], [53, 54]),
    ("aglientu", "Aglientu", [158, 159], [56, 57]),
    ("badesi", "Badesi", [159, 160], [57, 58]),
    ("bortigiadas", "Bortigiadas", [161, 162], [58, 59]),
    ("calangianus", "Calangianus", [162, 163], [59, 60]),
    ("luogosanto", "Luogosanto", [163, 164, 165], [60, 61]),
    ("luras", "Luras", [165, 166], [62, 63]),
    ("santa-teresa-gallura", "Santa Teresa Gallura", [166, 167], [63, 64]),
    ("tempio-pausania", "Tempio Pausania", [168, 169], [64, 65]),
    ("trinita-d-agultu-e-vignola", "Trinità d'Agultu e Vignola", [169, 170], [65, 66]),
    ("viddalba", "Viddalba", [170, 171], [67, 68]),
]
NOME = {s: n for s, n, _, _ in COMUNI}
PAG_SCHEDA = {s: p for s, _, p, _ in COMUNI}
PAG_P3 = {s: p for s, _, _, p in COMUNI}

# ---------------------------------------------------------------- USO DEL SUOLO (tabelle "Sintesi dell'uso del suolo")
USO = {
    "aggius": (156, [("Prati artificiali", 1415, 17.0), ("Macchia mediterranea", 1258, 15.1), ("Bosco di latifoglie", 958, 11.5),
                     ("Gariga", 895, 10.7), ("Sugherete", 574, 6.9), ("Aree a pascolo naturale", 535, 6.4)]),
    "aglientu": (158, [("Macchia mediterranea", 3214, 21.7), ("Gariga", 3166, 21.3), ("Prati artificiali", 2494, 16.8),
                       ("Bosco di latifoglie", 1120, 7.6), ("Aree a pascolo naturale", 951, 6.4), ("Aree a ricolonizzazione naturale", 770, 5.2)]),
    "badesi": (159, [("Seminativi semplici e colture orticole", 437, 14.2), ("Macchia mediterranea", 417, 13.6), ("Gariga", 373, 12.1),
                     ("Vigneti", 357, 11.6), ("Bosco di latifoglie", 262, 8.5), ("Prati artificiali", 209, 6.8)]),
    "bortigiadas": (161, [("Bosco di latifoglie", 2204, 28.9), ("Macchia mediterranea", 1114, 14.6), ("Gariga", 878, 11.5),
                          ("Prati artificiali", 652, 8.5), ("Boschi misti di conifere e latifoglie", 498, 6.5), ("Seminativi semplici e colture orticole", 459, 6.0)]),
    "calangianus": (162, [("Bosco di latifoglie", 2745, 21.7), ("Macchia mediterranea", 2070, 16.4), ("Sugherete", 2014, 15.9),
                          ("Gariga", 1412, 11.2), ("Vegetazione rada", 1290, 10.2), ("Seminativi in aree non irrigue", 663, 5.2)]),
    "luogosanto": (163, [("Macchia mediterranea", 3487, 25.8), ("Prati artificiali", 2310, 17.1), ("Bosco di latifoglie", 2253, 16.7),
                         ("Gariga", 1252, 9.3), ("Aree agroforestali", 914, 6.8), ("Aree a pascolo naturale", 562, 4.2)]),
    "luras": (165, [("Seminativi in aree non irrigue", 1340, 15.3), ("Macchia mediterranea", 1271, 14.5), ("Gariga", 1119, 12.8),
                    ("Prati artificiali", 940, 10.7), ("Bosco di latifoglie", 865, 9.9), ("Aree a pascolo naturale", 854, 9.8)]),
    "santa-teresa-gallura": (166, [("Gariga", 2568, 25.3), ("Macchia mediterranea", 2315, 22.8), ("Prati artificiali", 1765, 17.4),
                                   ("Aree a ricolonizzazione naturale", 872, 8.6), ("Aree agricole con spazi naturali importanti", 457, 4.5), ("Aree agroforestali", 274, 2.7)]),
    "tempio-pausania": (168, [("Macchia mediterranea", 3475, 16.4), ("Bosco di latifoglie", 3350, 15.8), ("Prati artificiali", 2496, 11.8),
                              ("Sugherete", 1937, 9.1), ("Gariga", 1564, 7.4), ("Seminativi non irrigui", 1507, 7.1)]),
    "trinita-d-agultu-e-vignola": (169, [("Macchia mediterranea", 3646, 26.6), ("Gariga", 3561, 26.0), ("Prati artificiali", 1804, 13.2),
                                         ("Bosco di latifoglie", 1340, 9.8), ("Aree a pascolo naturale", 699, 5.1), ("Vegetazione rada", 491, 3.6)]),
    "viddalba": (170, [("Gariga", 1111, 22.4), ("Macchia mediterranea", 1055, 21.3), ("Bosco di latifoglie", 587, 11.9),
                       ("Prati artificiali", 422, 8.5), ("Aree a pascolo naturale", 346, 7.0), ("Aree a ricolonizzazione artificiale", 291, 5.9)]),
}
# pagina della riga se la tabella e' spezzata su due pagine
USO_PAG_RIGA = {("luogosanto", "Gariga"): 164, ("luogosanto", "Aree agroforestali"): 164, ("luogosanto", "Aree a pascolo naturale"): 164,
                ("viddalba", "Aree a ricolonizzazione artificiale"): 171}

# Sugherete citate solo nel testo (non tra le prime classi), con pagina e citazione
SUGHERETE_TESTO = {
    "aglientu": (159, 321, "Le sugherete risultano presenti ma limitate, circa 321 ha."),
    "badesi": (159, 0, "assenza di sugherete rilevata nelle tabelle (pag. 159); 'Le tabelle non evidenziano sugherete' (pag. 160)"),
    "bortigiadas": (161, 116, "Le sugherete ammontano a circa 116 ha."),
    "luogosanto": (164, 449, "Le sugherete risultano presenti per circa 449 ha."),
    "luras": (165, 645, "Le sugherete ammontano a circa 645 ha, valore significativo nel quadro comunale."),
    "santa-teresa-gallura": (167, 0, "'Le tabelle non riportano sugherete' (pag. 166); 'Non risultano sugherete nei dati comunali analizzati' (pag. 167)"),
    "trinita-d-agultu-e-vignola": (169, 211, "Le sugherete ammontano a circa 211 ha."),
    "viddalba": (171, 52, "Le sugherete risultano pari a circa 52 ha."),
}
SUGHERETE_TABELLA = {"aggius": (156, 574), "calangianus": (162, 2014), "tempio-pausania": (168, 1937)}

# ---------------------------------------------------------------- PEDOLOGIA
PEDO = {
    "aggius": (156, [("C2", 4732, 56.7), ("C1", 1941, 23.3), ("B2", 1565, 18.8), ("B3", 82, 1.0)]),
    "aglientu": (158, [("C2", 10902, 73.5), ("C1", 2550, 17.2), ("M1", 564, 3.8), ("I1", 425, 2.9), ("L1", 368, 2.5)]),
    "badesi": (160, [("M1", 1538, 50.1), ("C2", 1202, 39.1), ("L1", 260, 8.5), ("L2", 70, 2.3)]),
    "bortigiadas": (161, [("C1", 4430, 58.1), ("C2", 1971, 25.8), ("I1", 426, 5.6), ("G1", 356, 4.7), ("B1", 161, 2.1)]),
    "calangianus": (162, [("C1", 8076, 63.8), ("C2", 3471, 27.4), ("C5", 710, 5.6), ("C3", 351, 2.8)]),
    "luogosanto": (164, [("C2", 11359, 84.1), ("C1", 1982, 14.7), ("B2", 79, 0.6), ("L1", 72, 0.5)]),
    "luras": (165, [("C2", 6590, 75.3), ("C1", 1089, 12.5), ("B2", 622, 7.1), ("C3", 358, 4.1), ("L1", 59, 0.7)]),
    "santa-teresa-gallura": (167, [("C2", 5656, 55.6), ("C1", 3513, 34.5), ("B2", 331, 3.3), ("M1", 282, 2.8), ("L1", 139, 1.4)]),
    "tempio-pausania": (168, [("C2", 11026, 51.9), ("C1", 6546, 30.8), ("C5", 1447, 6.8), ("C3", 1275, 6.0), ("B2", 502, 2.4)]),
    "trinita-d-agultu-e-vignola": (169, [("C2", 6397, 46.7), ("C1", 4477, 32.7), ("B2", 1016, 7.4), ("I1", 903, 6.6), ("M1", 660, 4.8)]),
    "viddalba": (171, [("C2", 2329, 47.1), ("B2", 1129, 22.8), ("C1", 626, 12.6), ("M1", 418, 8.5), ("L1", 203, 4.1)]),
}
PEDO_COMMENTO = {
    "aggius": (156, "Prevalgono suoli su rocce intrusive e metamorfiti paleozoiche, spesso poco o mediamente profondi, con rocciosità, pietrosità, eccesso di scheletro e forte pericolo di erosione. Le unità C1 e B2 richiamano in particolare la necessità di conservazione della vegetazione naturale e riduzione o eliminazione del pascolamento nei contesti più fragili."),
    "aglientu": (158, "La grande prevalenza di C2 segnala suoli su rocce intrusive, da poco a mediamente profondi, con rocciosità, pietrosità e forte pericolo di erosione. La presenza di C1 aumenta la quota di aree a funzione protettiva. M1, I1 e L1 indicano situazioni più specifiche: sabbie eoliche, alluvioni o aree pianeggianti, da valutare separatamente."),
    "badesi": (160, "La prevalenza di M1 indica suoli su sabbie eoliche, profondi ma con drenaggio eccessivo e forte pericolo di erosione. C2 introduce le limitazioni tipiche delle rocce intrusive. L1 e L2 individuano aree più pianeggianti/alluvionali, con possibile attitudine agricola ma anche limiti legati a drenaggio o inondazione."),
    "bortigiadas": (161, "La forte incidenza di C1 segnala un territorio pedologicamente fragile, con aree aspre, pendenze elevate, rocciosità, pietrosità, scarsa profondità e forte pericolo di erosione. B1 presenta analoghe limitazioni su metamorfiti. I1 e G1 introducono condizioni più specifiche, ma non dominanti."),
    "calangianus": (162, "La prevalenza di C1 indica ampie superfici con forti limitazioni: pendenze, rocciosità, pietrosità, scarsa profondità, erosione. C5 e C3 possono indicare ambiti dove approfondire forestazione, infittimento e gestione razionale della vegetazione naturale."),
    "luogosanto": (164, "Prevale nettamente C2, con suoli su rocce intrusive, da poco a mediamente profondi, permeabili, ma con rocciosità, pietrosità, scheletro e forte pericolo di erosione a tratti. La quota C1 rappresenta gli ambiti più fragili."),
    "luras": (165, "Prevale C2, con limitazioni ricorrenti legate a pietrosità, rocciosità, scarsa profondità e pericolo di erosione. C3 può rappresentare ambiti da approfondire per uso più razionale della vegetazione naturale e pascolo regimato."),
    "santa-teresa-gallura": (167, "La presenza rilevante di C1 e C2 suggerisce condizioni di fragilità diffuse. Le unità M1 e L1 sono minoritarie ma importanti per ambiti sabbiosi o alluvionali."),
    "tempio-pausania": (168, "Prevalgono C2 e C1, quindi suoli su rocce intrusive con limitazioni diffuse. C5 e C3 possono offrire ambiti da approfondire per gestione forestale razionale, infittimento e pascolo regolato."),
    "trinita-d-agultu-e-vignola": (169, "Il quadro pedologico è articolato, ma dominato da C2 e C1. Sono presenti anche B2, I1 e M1, che richiedono letture specifiche a scala di dettaglio."),
    "viddalba": (171, "Il quadro pedologico è più diversificato rispetto ad altri Comuni, con C2 prevalente, B2 significativa, C1 meno dominante, e presenza di M1/L1."),
}
UNITA_PEDOLOGICHE = {
    "C1": {"descrizione": "Suoli su rocce intrusive (graniti) delle aree più aspre: pendenze elevate, rocciosità, pietrosità, scarsa profondità e forte pericolo di erosione; unità a prevalente funzione protettiva, che richiama la conservazione della vegetazione naturale e la riduzione o eliminazione del pascolamento nei contesti più fragili.", "pagine_pdf": [156, 158, 161, 162], "substrato": "rocce intrusive"},
    "C2": {"descrizione": "Suoli su rocce intrusive, da poco a mediamente profondi, permeabili, con rocciosità, pietrosità, eccesso di scheletro e forte pericolo di erosione a tratti; unità dominante nella maggior parte dei Comuni.", "pagine_pdf": [156, 158, 164, 165], "substrato": "rocce intrusive"},
    "C3": {"descrizione": "Unità su rocce intrusive citata come ambito da approfondire per un uso più razionale della vegetazione naturale, infittimento/forestazione e pascolo regimato.", "pagine_pdf": [162, 165, 168], "substrato": "rocce intrusive"},
    "C5": {"descrizione": "Unità su rocce intrusive citata, insieme a C3, come ambito dove approfondire forestazione, infittimento e gestione razionale della vegetazione naturale.", "pagine_pdf": [162, 168], "substrato": "rocce intrusive"},
    "B1": {"descrizione": "Suoli su metamorfiti paleozoiche con limitazioni analoghe a C1 (pendenze, rocciosità, pietrosità, scarsa profondità, erosione).", "pagine_pdf": [161], "substrato": "metamorfiti paleozoiche"},
    "B2": {"descrizione": "Suoli su metamorfiti paleozoiche, poco o mediamente profondi, con rischio erosivo; richiama conservazione della vegetazione naturale e riduzione del pascolamento nei contesti più fragili.", "pagine_pdf": [156, 171], "substrato": "metamorfiti paleozoiche"},
    "B3": {"descrizione": "Unità su metamorfiti paleozoiche presente solo ad Aggius (82 ha); il documento non ne fornisce una descrizione specifica.", "pagine_pdf": [156], "substrato": "metamorfiti paleozoiche"},
    "M1": {"descrizione": "Suoli su sabbie eoliche, profondi ma con drenaggio eccessivo e forte pericolo di erosione (ambiti sabbiosi costieri).", "pagine_pdf": [158, 160, 167], "substrato": "sabbie eoliche"},
    "L1": {"descrizione": "Aree pianeggianti/alluvionali con possibile attitudine agricola ma limiti legati a drenaggio o inondazione.", "pagine_pdf": [158, 160, 167], "substrato": "alluvioni / aree pianeggianti"},
    "L2": {"descrizione": "Come L1: aree pianeggianti/alluvionali con possibile attitudine agricola e limiti di drenaggio o inondazione; presente solo a Badesi (70 ha).", "pagine_pdf": [160], "substrato": "alluvioni / aree pianeggianti"},
    "I1": {"descrizione": "Unità citata insieme a M1 e L1 come 'situazioni più specifiche: sabbie eoliche, alluvioni o aree pianeggianti, da valutare separatamente' e come condizione 'più specifica, non dominante'; il documento non la descrive singolarmente.", "pagine_pdf": [158, 161, 169], "substrato": None},
    "G1": {"descrizione": "Unità citata solo a Bortigiadas come condizione 'più specifica, ma non dominante'; il documento non ne fornisce una descrizione.", "pagine_pdf": [161], "substrato": None},
}

# ---------------------------------------------------------------- MATRICE PEDOLOGIA x USO DEL SUOLO
MATRICE = {
    "aggius": (156, [("Prati artificiali su C2", 805, 9.6), ("Macchia mediterranea su C2", 644, 7.7), ("Prati artificiali su B2", 522, 6.3), ("Gariga su C2", 490, 5.9), ("Bosco di latifoglie su C2", 483, 5.8)],
               "Le sugherete ricadono soprattutto su C2, C1 e B2. Ciò suggerisce una possibile valorizzazione forestale, ma con forte attenzione al rischio erosivo e alla funzione protettiva delle coperture."),
    "aglientu": (158, [("Gariga su C2", 2402, 16.2), ("Macchia mediterranea su C2", 2270, 15.3), ("Prati artificiali su C2", 2051, 13.8), ("Bosco di latifoglie su C2", 832, 5.6), ("Macchia mediterranea su C1", 770, 5.2)],
                 "La matrice evidenzia che le principali superfici naturali e seminaturali insistono su C2 e C1. Questo rafforza la necessità di leggere il territorio come mosaico da gestire in equilibrio tra conservazione, prevenzione incendi, pascolo regolato e manutenzione della copertura vegetale."),
    "badesi": (160, [("Macchia mediterranea su C2", 377, 12.3), ("Gariga su C2", 359, 11.7), ("Vigneti su M1", 350, 11.4), ("Seminativi su L1", 221, 7.2), ("Bosco di latifoglie su C2", 184, 6.0)],
               "La matrice indica una distinzione tra ambiti agricoli su M1/L1 e superfici seminaturali su C2. La componente agricola appare più rilevante rispetto alla filiera forestale."),
    "bortigiadas": (161, [("Bosco di latifoglie su C1", 1489, 19.5), ("Macchia mediterranea su C1", 690, 9.0), ("Gariga su C1", 646, 8.5), ("Bosco di latifoglie su C2", 571, 7.5), ("Boschi misti su C1", 355, 4.7)],
                    "La matrice conferma la prevalenza di coperture forestali e seminaturali su unità pedologiche fragili. Il mantenimento della copertura vegetale ha qui una funzione protettiva centrale."),
    "calangianus": (163, [("Bosco di latifoglie su C1", 2038, 16.1), ("Macchia mediterranea su C1", 1640, 13.0), ("Sugherete su C1", 1166, 9.2), ("Gariga su C1", 1138, 9.0), ("Vegetazione rada su C1", 1082, 8.5)],
                    "La matrice mostra che una quota importante delle sugherete e delle coperture forestali insiste su C1. Questo non riduce l’importanza del Comune, ma suggerisce che la valorizzazione debba essere fondata su gestione sostenibile, protezione del suolo e miglioramento forestale, non su intensificazione."),
    "luogosanto": (164, [("Macchia mediterranea su C2", 2699, 20.0), ("Prati artificiali su C2", 2186, 16.2), ("Bosco di latifoglie su C2", 1956, 14.5), ("Gariga su C2", 985, 7.3), ("Aree agroforestali su C2", 870, 6.4)],
                   "La matrice mostra un forte mosaico agroforestale su C2. Questo rende il Comune interessante per valutazioni integrate, purché le limitazioni pedologiche siano considerate nella progettazione."),
    "luras": (165, [("Seminativi non irrigui su C2", 1244, 14.2), ("Prati artificiali su C2", 808, 9.2), ("Gariga su C2", 752, 8.6), ("Macchia mediterranea su C2", 737, 8.4), ("Pascolo naturale su C2", 710, 8.1)],
              "La matrice evidenzia un uso agricolo-pastorale consistente su C2, da leggere con cautela in termini di carichi, erosione e mantenimento della copertura vegetale."),
    "santa-teresa-gallura": (167, [("Prati artificiali su C2", 1469, 14.4), ("Gariga su C2", 1249, 12.3), ("Gariga su C1", 1177, 11.6), ("Macchia mediterranea su C1", 1102, 10.8), ("Macchia mediterranea su C2", 997, 9.8)],
                             "La matrice mostra ampie superfici seminaturali su unità fragili. La funzione protettiva e paesaggistica è centrale."),
    "tempio-pausania": (168, [("Prati artificiali su C2", 1986, 9.4), ("Macchia mediterranea su C1", 1830, 8.6), ("Bosco di latifoglie su C1", 1783, 8.4), ("Macchia mediterranea su C2", 1410, 6.6), ("Sugherete su C2", 1370, 6.5)],
                        "La matrice conferma la rilevanza di Tempio per sughero e gestione agroforestale. Una parte importante delle coperture forestali insiste però su C1, con funzione protettiva da considerare."),
    "trinita-d-agultu-e-vignola": (170, [("Macchia mediterranea su C1", 1822, 13.3), ("Gariga su C2", 1715, 12.5), ("Macchia mediterranea su C2", 1396, 10.2), ("Gariga su C1", 1020, 7.4), ("Prati artificiali su C2", 982, 7.2)],
                                   "La matrice mostra una forte presenza di coperture seminaturali su unità fragili. La funzione protettiva della vegetazione è rilevante."),
    "viddalba": (171, [("Gariga su C2", 636, 12.8), ("Macchia mediterranea su C2", 610, 12.3), ("Gariga su B2", 259, 5.2), ("Macchia mediterranea su B2", 257, 5.2), ("Bosco di latifoglie su B2", 244, 4.9)],
                 "La matrice evidenzia coperture seminaturali su C2 e B2, con possibile funzione protettiva e necessità di gestione prudente."),
}
# etichette abbreviate nelle combinazioni -> classe della tabella uso del suolo
CLASSE_NORMALIZZATA = {
    "Seminativi": "Seminativi semplici e colture orticole",
    "Boschi misti": "Boschi misti di conifere e latifoglie",
    "Seminativi non irrigui": "Seminativi in aree non irrigue",
    "Pascolo naturale": "Aree a pascolo naturale",
}

# ---------------------------------------------------------------- SINTESI COMPARATIVA (pag. 172)
SINTESI = [
    ("aggius", "Medio-alta", "Medio, solo pilota", "Alta", "Alta"),
    ("aglientu", "Medio-bassa", "Medio prudenziale", "Medio-alta", "Media"),
    ("badesi", "Bassa", "Medio-bassa", "Media", "Media"),
    ("bortigiadas", "Medio-bassa", "Bassa/localizzata", "Alta", "Media"),
    ("calangianus", "Alta", "Basso-medio controllato", "Alta", "Molto alta"),
    ("luogosanto", "Media", "Medio-alta da verificare", "Medio-alta", "Alta"),
    ("luras", "Medio-alta", "Media", "Medio-alta", "Alta"),
    ("santa-teresa-gallura", "Bassa", "Basso-medio", "Medio-alta", "Media, soprattutto commerciale"),
    ("tempio-pausania", "Alta", "Medio-alta da verificare", "Medio-alta", "Molto alta"),
    ("trinita-d-agultu-e-vignola", "Medio-bassa", "Medio prudenziale", "Medio-alta", "Media"),
    ("viddalba", "Bassa", "Medio-bassa", "Media", "Media"),
]
GRUPPI_FUNZIONALI = [
    {"gruppo": "Comuni prioritari per filiera bosco-sughero", "comuni": ["calangianus", "tempio-pausania", "luras", "aggius"],
     "comuni_parziali": [], "descrizione": "Calangianus e Tempio Pausania, seguiti da Luras e Aggius. Qui la priorità è approfondire stato delle sugherete, gestione, decortica, proprietà, accessibilità e rapporto con trasformazione."},
    {"gruppo": "Comuni agroforestali integrabili", "comuni": ["luogosanto", "aggius", "luras"], "comuni_parziali": ["tempio-pausania"],
     "descrizione": "Luogosanto, Aggius, Luras e in parte Tempio. Sono i territori dove verificare con maggiore attenzione eventuali progetti pilota integrati tra gestione forestale, superfici agro-silvopastorali e filiera suinicola controllata."},
    {"gruppo": "Comuni con funzione ambientale, paesaggistica e commerciale", "comuni": ["aglientu", "santa-teresa-gallura", "trinita-d-agultu-e-vignola", "badesi"], "comuni_parziali": [],
     "descrizione": "Aglientu, Santa Teresa Gallura, Trinità d'Agultu e Vignola, Badesi. Qui il contributo alla Green Community può essere forte sul piano turistico, commerciale, paesaggistico e di sbocco dei prodotti, più che sulla produzione primaria del sughero."},
    {"gruppo": "Comuni a prevalente attenzione forestale/protettiva", "comuni": ["bortigiadas"], "comuni_parziali": ["calangianus", "aggius", "tempio-pausania"],
     "descrizione": "Bortigiadas e parte di Calangianus, Aggius e Tempio, dove la presenza di C1 e coperture forestali su suoli fragili impone una gestione prudenziale."},
]
QUADRO_VOCAZIONI = [  # pag. 178
    ("Sughericola primaria", "Calangianus, Tempio Pausania", ["calangianus", "tempio-pausania"], "Poli principali per approfondire gestione, valorizzazione, filiera, certificazioni e governance del sughero."),
    ("Sughericola integrata", "Luras, Aggius, Luogosanto", ["luras", "aggius", "luogosanto"], "Integrazione tra sugherete, mosaico agro-pastorale, gestione forestale, prevenzione incendi e filiere locali."),
    ("Forestale protettiva", "Bortigiadas, parti di Calangianus, Aggius, Tempio, Aglientu, Trinità, Viddalba", ["bortigiadas", "calangianus", "aggius", "tempio-pausania", "aglientu", "trinita-d-agultu-e-vignola", "viddalba"], "Conservazione del suolo, tutela della vegetazione, prevenzione erosione, gestione prudenziale."),
    ("Agro-silvo-pastorale", "Luogosanto, Luras, Aggius, Tempio, Aglientu, Viddalba", ["luogosanto", "luras", "aggius", "tempio-pausania", "aglientu", "viddalba"], "Possibile base per modelli rurali estensivi, gestione del paesaggio e progetti pilota controllati."),
    ("Suinicola agroforestale sperimentale", "Luogosanto, Tempio, Luras, Aggius", ["luogosanto", "tempio-pausania", "luras", "aggius"], "Da valutare solo con studi aziendali, pedologici, sanitari, faunistici e ambientali."),
    ("Turistico-commerciale", "Santa Teresa Gallura, Badesi, Trinità d'Agultu e Vignola, Aglientu", ["santa-teresa-gallura", "badesi", "trinita-d-agultu-e-vignola", "aglientu"], "Mercato di sbocco, ristorazione, turismo esperienziale, comunicazione, vendita e valorizzazione premium."),
    ("Agricola e agroalimentare complementare", "Badesi, Luras, Tempio, Luogosanto, Viddalba", ["badesi", "luras", "tempio-pausania", "luogosanto", "viddalba"], "Supporto a filiere locali, trasformazione, prodotti territoriali, integrazione con turismo."),
    ("Governance e servizi di filiera", "Tempio Pausania, Calangianus, con raccordo intercomunale", ["tempio-pausania", "calangianus"], "Coordinamento, cabina di regia, servizi tecnici, raccordo con operatori, monitoraggio, progettazione successiva."),
]

# ---------------------------------------------------------------- TAB. 2a (pag. 37)
TAB2A = {
    "calangianus": ("Calangianus – Tempio Pausania", "Entroterra", "Polo forestale e sughericolo", "Sugherete, sistemi forestali, paesaggi granitici", "Produzione sughericola, gestione forestale, tutela idrogeologica"),
    "tempio-pausania": ("Calangianus – Tempio Pausania", "Entroterra", "Polo forestale e sughericolo", "Sugherete, sistemi forestali, paesaggi granitici", "Produzione sughericola, gestione forestale, tutela idrogeologica"),
    "luogosanto": ("Luogosanto – Luras – Aggius", "Entroterra", "Sistema agroforestale multifunzionale", "Mosaici rurali, pascoli arborati, macchia mediterranea", "Conservazione del paesaggio storico, biodiversità diffusa, presidio territoriale"),
    "luras": ("Luogosanto – Luras – Aggius", "Entroterra", "Sistema agroforestale multifunzionale", "Mosaici rurali, pascoli arborati, macchia mediterranea", "Conservazione del paesaggio storico, biodiversità diffusa, presidio territoriale"),
    "aggius": ("Luogosanto – Luras – Aggius", "Entroterra", "Sistema agroforestale multifunzionale", "Mosaici rurali, pascoli arborati, macchia mediterranea", "Conservazione del paesaggio storico, biodiversità diffusa, presidio territoriale"),
    "bortigiadas": ("Bortigiadas", "Entroterra", "Ambito di protezione ambientale e fragilità pedologica", "Versanti acclivi, sistemi forestali interni", "Stabilità ecologica, conservazione del suolo, mitigazione erosiva"),
    "aglientu": ("Aglientu – Badesi", "Costa / Interfaccia entroterra-costa", "Interfaccia costa-entroterra", "Sistemi dunali, retroterra rurale, fasce costiere", "Connessione tra turismo costiero e filiere rurali interne"),
    "badesi": ("Aglientu – Badesi", "Costa / Interfaccia entroterra-costa", "Interfaccia costa-entroterra", "Sistemi dunali, retroterra rurale, fasce costiere", "Connessione tra turismo costiero e filiere rurali interne"),
    "santa-teresa-gallura": ("Santa Teresa Gallura", "Costa", "Polarità turistico-ambientale", "Paesaggi costieri, macchia mediterranea, sistemi rocciosi", "Accessibilità territoriale e valorizzazione ambientale"),
    "trinita-d-agultu-e-vignola": ("Trinità d'Agultu e Vignola", "Costa", "Ambito di integrazione ecosistemica e turistico-costiera", "Sistemi collinari e costieri integrati", "Connessione economica, ambientale e paesaggistica tra costa e aree interne"),
    "viddalba": ("Viddalba", "Interfaccia entroterra-costa", "Sistema fluviale e agricolo di connessione territoriale", "Piana del Coghinas, sistemi agricoli, corridoi ecologici fluviali", "Connessione ecologica e produttiva tra Alta Gallura, aree costiere e sistema del Coghinas"),
}
# fascia dal quadro sinottico Parte 3 (pag. 53)
FASCIA = {"aglientu": "costiera", "badesi": "costiera", "santa-teresa-gallura": "costiera", "trinita-d-agultu-e-vignola": "costiera",
          "aggius": "interna", "bortigiadas": "interna", "calangianus": "interna", "luogosanto": "interna", "luras": "interna", "tempio-pausania": "interna",
          "viddalba": "interna"}
POSIZIONE_P3 = {"viddalba": "cerniera idrografica e di transizione tra fascia costiera e interno (pag. 53); classificata 'interna'/entroterra nella lettura demografica dello studio (7 Comuni)"}

# ---------------------------------------------------------------- SCHEDE (testi fedeli Allegato II + Parte 3)
SCHEDE = {
 "aggius": dict(
    inquadramento=["Aggius presenta un assetto territoriale a forte componente rurale, forestale, seminaturale e agro-silvopastorale. La scheda evidenzia una buona rilevanza per la filiera bosco-sughero, ma anche fragilità pedologiche diffuse che impongono cautela per eventuali utilizzi zootecnici estensivi.",
                  "Il Comune di Aggius si configura come un sistema territoriale ad alta densità identitaria, situato nel settore centro-occidentale dell’Alta Gallura; tra il 2001 e il 2023 ha perso oltre il 16 % dei propri abitanti. Il territorio presenta un assetto a forte componente rurale e seminaturale, dominato da sugherete, leccete e macchia mediterranea evoluta, storicamente organizzate attraverso il modello insediativo e produttivo dello stazzo."],
    bosco_sughero="Aggius presenta un interesse preliminare medio-alto per la filiera bosco-sughero, con circa 574 ha di sugherete. La presenza su unità C2 e B2 consente di ipotizzare approfondimenti su gestione sostenibile e recupero forestale; la quota su C1 richiede invece prudenza, privilegiando funzioni protettive.",
    suinicola="Il Comune può essere considerato da approfondire solo in chiave pilota e controllata. Prati artificiali, pascoli naturali e alcune superfici agroforestali costituiscono potenziali ambiti di verifica, ma le limitazioni pedologiche sono rilevanti. Le aree su C1 dovrebbero essere considerate tendenzialmente non prioritarie per usi suinicoli.",
    criticita=["erosione", "rocciosità", "pietrosità", "suoli poco profondi", "vulnerabilità della copertura vegetale", "compatibilità del pascolo con unità pedologiche fragili"],
    opportunita=["mappatura aggiornata delle sugherete", "stato vegetativo e fitosanitario", "proprietà", "accessibilità", "aziende interessate", "vincoli", "habitat", "fauna", "verifica di eventuali aree pilota"],
    valutazione="vocazione sughericola medio-alta; interesse suinicolo medio ma solo sperimentale; fragilità pedologica alta",
    identitari=["Monti di Aggius e Piana dei Grandi Massi (Valle della Luna), geosito", "centro storico in granito, Borgo Autentico d’Italia", "Nuraghe Agnu", "Museo del Banditismo e Museo Etnografico Oliva Carta Cannas", "canto polifonico e tessitura artigianale", "stazzi", "Sughereta Sperimentale di Cusseddu-Miali-Parapinta"]),
 "aglientu": dict(
    inquadramento=["Aglientu presenta una forte componente seminaturale e agro-pastorale, con ampia presenza di macchia, gariga, prati artificiali, boschi e pascoli. La vocazione sughericola appare più limitata rispetto ad altri Comuni interni, mentre il tema suinicolo può essere valutato solo con molta cautela, soprattutto per l’elevata diffusione di unità C2 e C1.",
                  "Aglientu si configura come un territorio di transizione tra l’entroterra collinare e il litorale settentrionale; il Rio Vignola costituisce la principale direttrice ecologica e idrologica. La fascia costiera si estende per circa diciotto chilometri e trova la sua massima espressione nell’area di Monte Russu, Zona Speciale di Conservazione della rete Natura 2000."],
    bosco_sughero="Le sugherete risultano presenti ma limitate, circa 321 ha. Aglientu non appare, in questa fase, tra i Comuni più forti per la filiera produttiva del sughero, ma può avere interesse per la gestione forestale multifunzionale, il recupero di superfici seminaturali e la prevenzione incendi.",
    suinicola="La presenza di prati artificiali e pascoli naturali rende il Comune meritevole di approfondimento, ma l’elevata incidenza di C2 e C1 richiede forte prudenza. Eventuali ipotesi suinicole dovrebbero concentrarsi su superfici aziendali effettivamente gestibili, recintabili, con suoli meno fragili e fuori dagli ambiti di maggiore sensibilità.",
    criticita=["ampie superfici di gariga e macchia su suoli con rischio erosivo", "possibile fragilità della copertura vegetale", "rischio di degrado da carichi non controllati", "necessità di verifica dei vincoli ambientali e costieri"],
    opportunita=["gestione del mosaico macchia-gariga-pascolo", "prevenzione incendi", "verifica di aree agro-pastorali controllate", "connessione con il mercato turistico costiero"],
    valutazione="vocazione sughericola medio-bassa; interesse suinicolo medio ma prudenziale; fragilità pedologica medio-alta",
    identitari=["Rio Vignola", "circa 18 km di costa ad alta naturalità (spiagge, dune, ginepreti)", "Monte Russu (ZSC)", "resti nuragici di Finucchjaglia e nuraghe Tuttusoni", "chiesa campestre di San Pancrazio", "stazzi"]),
 "badesi": dict(
    inquadramento=["Badesi presenta un profilo diverso rispetto ai Comuni più interni: maggiore presenza di seminativi, vigneti, macchia, gariga e boschi, ma assenza di sugherete rilevata nelle tabelle. Il ruolo del Comune appare più connesso a filiere agricole, paesaggio rurale-costiero e possibili mercati di sbocco, piuttosto che alla produzione primaria di sughero.",
                  "Badesi si configura come un fondamentale territorio di transizione tra il sistema fluviale del Coghinas, gli ambienti dunali litoranei e le aree agricole retro-costiere; l’assetto paesaggistico deriva storicamente dall’evoluzione degli stazzi di Muntiggioni e La Tozza. Il continuum costiero è integralmente inserito nel sito Natura 2000 “Foci del Coghinas”."],
    bosco_sughero="Le tabelle non evidenziano sugherete. Badesi non deve quindi essere presentato come Comune produttivo sughericolo, almeno sulla base dei dati disponibili. Può però contribuire alla strategia territoriale attraverso paesaggio rurale, turismo, agricoltura, viticoltura e possibili mercati di valorizzazione.",
    suinicola="Il potenziale suinicolo è da valutare con cautela. Le superfici agricole e prative possono offrire spazi di approfondimento, ma M1 presenta rischio erosivo e drenaggio eccessivo. Eventuali iniziative dovranno essere aziendali, controllate, con attenzione a suoli sabbiosi, disponibilità idrica e compatibilità con il contesto turistico-costiero.",
    criticita=["erosione su sabbie eoliche", "pressione costiera/turistica", "compatibilità paesaggistica", "limitata presenza forestale sughericola", "necessità di verifiche ambientali e urbanistiche"],
    opportunita=["Comune di collegamento tra filiere rurali e mercato turistico-costiero", "trasformazione", "vendita diretta", "ristorazione", "turismo rurale", "prodotti locali"],
    valutazione="vocazione sughericola bassa; interesse suinicolo medio-basso e aziendale; ruolo potenziale commerciale/turistico",
    identitari=["fiume Coghinas e Foci del Coghinas (Natura 2000)", "sistemi dunali e cordoni retro-dunali", "stazzi di Muntiggioni e La Tozza", "viticoltura di qualità e seminativi della piana alluvionale", "enoturismo e blue-green economy"]),
 "bortigiadas": dict(
    inquadramento=["Bortigiadas presenta una forte componente forestale, con boschi di latifoglie, macchia, gariga e boschi misti. La presenza di sugherete è contenuta, ma il Comune appare rilevante per gestione forestale, protezione del suolo e recupero del mosaico agroforestale.",
                  "Bortigiadas rappresenta uno dei contesti demograficamente più fragili dell’intero sistema territoriale dell’Alta Gallura, in posizione strategica di cerniera tra i sistemi collinari granitici dell’interno e la valle del Coghinas, verso il comparto di Casteldoria. Il paesaggio è dominato da versanti acclivi, profonde incisioni vallive, rilievi granitici articolati e diffuse emergenze rocciose."],
    bosco_sughero="Le sugherete ammontano a circa 116 ha. La filiera sughericola appare meno rilevante in termini quantitativi rispetto a Calangianus, Tempio o Luras, ma il Comune può avere un ruolo nella gestione forestale sostenibile, nella manutenzione del paesaggio e nella prevenzione del degrado.",
    suinicola="L’interesse per la filiera suinicola è limitato e da trattare con forte cautela. L’elevata presenza di C1 rende poco opportuna una pressione zootecnica diffusa. Eventuali verifiche dovrebbero concentrarsi solo su aree agricole o prative più stabili, fuori dagli ambiti boschivi fragili.",
    criticita=["pendenza", "erosione", "rocciosità", "suoli superficiali", "coperture forestali su unità fragili", "rischio di alterazione della funzione protettiva"],
    opportunita=["gestione forestale protettiva", "recupero e infittimento della vegetazione naturale", "prevenzione incendi", "verifica puntuale delle piccole aree sughericole", "esclusione delle aree più fragili da usi zootecnici intensivi"],
    valutazione="vocazione forestale alta; vocazione sughericola medio-bassa; interesse suinicolo basso o solo molto localizzato; fragilità alta",
    identitari=["versanti acclivi e rilievi granitici verso la valle del Coghinas e Casteldoria", "nucleo urbano in granito integrato con la roccia affiorante", "nuclei rurali storici di Case Pedru Malu e Multa Bianca (stazzi)", "sugherete, leccete e macchia evoluta", "serbatoio di carbonio e biodiversità (Carbon Farming)"]),
 "calangianus": dict(
    inquadramento=["Calangianus emerge come uno dei Comuni chiave per la filiera bosco-sughero. Presenta la maggiore superficie di sugherete tra i Comuni analizzati, oltre a boschi di latifoglie, macchia e gariga. Tuttavia, la forte presenza di C1 impone una lettura molto prudente della componente produttiva e zootecnica.",
                  "Calangianus rappresenta il principale polo industriale della filiera sughericola dell’Alta Gallura e si colloca come uno dei più rilevanti distretti europei specializzati nella lavorazione di questa risorsa; tra il 2001 e il 2023 ha perso oltre il 18 % dei propri abitanti. Ospita la più estesa superficie di sugherete dell’Alta Gallura."],
    bosco_sughero="Calangianus è un Comune prioritario per la filiera sughericola. Le circa 2.014 ha di sugherete indicano una rilevanza territoriale elevata. Le successive fasi dovranno verificare stato vegetativo, turni di decortica, qualità del sughero, proprietà, accessibilità, operatori e connessioni con trasformazione e distretto produttivo esistente.",
    suinicola="Il suino agroforestale deve essere trattato come tema secondario e molto controllato. La presenza di vaste aree forestali e sugherete non implica automaticamente idoneità al pascolo suino. Al contrario, la diffusione di C1 e vegetazione rada rende prioritaria la tutela del suolo e della rinnovazione.",
    criticita=["sugherete su suoli fragili", "rischio erosione", "vegetazione rada su C1", "necessità di protezione della rinnovazione", "possibile conflitto tra funzione produttiva e funzione protettiva"],
    opportunita=["piano di gestione delle sugherete", "mappatura di dettaglio", "distretto rurale del sughero", "formazione operatori", "certificazioni", "filiera corta", "integrazione con artigianato, bioedilizia, design e turismo esperienziale"],
    valutazione="vocazione sughericola alta; priorità forestale alta; interesse suinicolo basso-medio solo come sperimentazione controllata; fragilità alta",
    identitari=["polo industriale del sughero, distretto europeo della lavorazione", "altopiani granitici e rilievi collinari", "ex convento settecentesco sede della Mostra del Sughero", "complessi megalitici", "saperi artigianali e manifatturieri del sughero", "hub del Distretto Rurale del Sughero"]),
 "luogosanto": dict(
    inquadramento=["Luogosanto presenta una matrice agroforestale molto rilevante, con macchia mediterranea, prati artificiali, boschi, gariga, aree agroforestali e pascoli. È un Comune interessante sia per la gestione forestale sia per eventuali verifiche su modelli agro-silvo-pastorali controllati.",
                  "Luogosanto si colloca nel settore centro-settentrionale dell’Alta Gallura e rappresenta uno dei principali poli storico-devozionali e paesaggistico-culturali dell’intero sistema gallurese, con una delle più elevate concentrazioni di emergenze religiose rurali della Sardegna settentrionale. L’assetto territoriale mostra una marcata dominanza di sistemi silvo-pastorali estensivi, formazioni arbustive mediterranee e coperture forestali stabili."],
    bosco_sughero="Le sugherete risultano presenti per circa 449 ha. Luogosanto ha un interesse preliminare medio per la filiera sughero, ma soprattutto per gestione agroforestale, continuità ecologica, prevenzione incendi e possibili interventi multifunzionali.",
    suinicola="Luogosanto è uno dei Comuni più interessanti da approfondire per una possibile sperimentazione suinicola agroforestale controllata, grazie alla presenza combinata di prati artificiali, aree agroforestali e pascoli naturali. Tuttavia, la prevalenza di C2 impone bassi carichi, rotazioni, monitoraggio del suolo e protezione della copertura vegetale.",
    criticita=["erosione a tratti su C2", "presenza di C1", "possibile vulnerabilità della macchia e della gariga", "necessità di verificare accessibilità, proprietà, aziende e disponibilità idrica"],
    opportunita=["aree pilota agroforestali", "integrazione tra gestione del sottobosco e allevamento controllato", "recupero di superfici rurali", "prevenzione incendi", "connessione con prodotti locali"],
    valutazione="vocazione agroforestale alta; vocazione sughericola media; interesse suinicolo medio-alto da verificare; fragilità medio-alta",
    identitari=["polo devozionale: chiese campestri, santuari, percorsi di pellegrinaggio", "Basilica di Nostra Signora di Luogosanto", "tafoni e ripari granitici", "stazzi", "alberi monumentali e sughere secolari, quercia di Crisciuleddu", "mobilità dolce e turismo rigenerativo"]),
 "luras": dict(
    inquadramento=["Luras presenta un equilibrio tra seminativi, macchia, gariga, prati artificiali, boschi, pascoli e sugherete. È un Comune interessante per filiera sughero e per eventuali approfondimenti agro-silvo-pastorali, ma con limitazioni pedologiche ricorrenti.",
                  "Luras è collocato nel settore nord-orientale dell’Alta Gallura, in una posizione strategica di connessione tra il massiccio granitico del Limbara e il sistema idrografico del Lago Liscia, con un sistema economico diversificato legato all’agricoltura specializzata, alla viticoltura di qualità e al turismo ambientale e culturale. Il vertice del valore ambientale e identitario è il complesso degli Olivastri Millenari di Santu Baltolu con il Patriarca d’Europa (S’Ozzastru)."],
    bosco_sughero="Luras presenta un interesse medio-alto per la filiera sughericola. Le sugherete sono significative e inserite in un mosaico agricolo, pastorale e forestale. Sarà necessario distinguere aree produttive, protettive e da recuperare, verificando accessibilità e gestione.",
    suinicola="Luras può essere approfondito per la filiera suinicola agroforestale, soprattutto in relazione a prati artificiali, pascoli e seminativi non irrigui. Tuttavia, la prevalenza di C2 richiede una progettazione prudente, con priorità a superfici già agricole o pascolive e non alle coperture forestali più sensibili.",
    criticita=["rischio erosivo su C2", "pascoli su suoli con limitazioni", "possibile pressione su gariga/macchia", "necessità di proteggere sugherete e rinnovazione"],
    opportunita=["sugherete", "aziende agro-zootecniche", "superfici pilota", "integrazione tra prodotti agricoli, sughero, carni locali e turismo rurale"],
    valutazione="vocazione sughericola medio-alta; interesse suinicolo medio; fragilità medio-alta",
    identitari=["Lago Liscia", "Olivastri Millenari di Santu Baltolu e S’Ozzastru (Patriarca d’Europa)", "dolmen e tombe a circolo di Ladas, Billella, Alzoledda e Ciuledda", "centro urbano compatto in granito", "viticoltura e olivicoltura di qualità", "tomba dei giganti di Pascaredda"]),
 "santa-teresa-gallura": dict(
    inquadramento=["Santa Teresa Gallura presenta una forte componente seminaturale e costiera, con gariga, macchia mediterranea, prati artificiali e aree a ricolonizzazione. Le tabelle non riportano sugherete. Il ruolo del Comune appare più legato a paesaggio, turismo, mercato di sbocco e gestione ambientale che alla produzione primaria di sughero.",
                  "Santa Teresa Gallura rappresenta uno dei principali poli demografici e funzionali dell’Alta Gallura costiera, principale nodo costiero settentrionale della subregione e gateway territoriale e transfrontaliero tra la Gallura, le Bocche di Bonifacio e le reti di mobilità marittima. Il valore ecologico è suggellato dalla Zona Speciale di Conservazione di Capo Testa e dall’Area Marina Protetta Capo Testa – Punta Falcone."],
    bosco_sughero="Non risultano sugherete nei dati comunali analizzati. Santa Teresa Gallura non va quindi letta come Comune produttivo sughericolo, ma come possibile area di connessione commerciale e turistica per prodotti territoriali provenienti dagli altri Comuni.",
    suinicola="Il tema suinicolo va trattato con cautela. La presenza di prati artificiali può essere oggetto di verifica, ma la forte componente di gariga e macchia su C1/C2, insieme al contesto turistico-costiero, suggerisce di evitare modelli estensivi non controllati.",
    criticita=["sensibilità paesaggistica e ambientale", "fragilità dei suoli", "pressione turistica", "possibile presenza di habitat costieri", "rischio di conflitto tra attività zootecnica e fruizione turistica"],
    opportunita=["mercato di sbocco", "luogo di ristorazione identitaria", "vetrina turistica", "nodo commerciale per carni locali e prodotti legati alla Green Community"],
    valutazione="vocazione sughericola bassa; interesse suinicolo basso-medio solo aziendale; ruolo turistico-commerciale alto",
    identitari=["porto e gateway sulle Bocche di Bonifacio", "impianto urbano ottocentesco sabaudo a maglia ortogonale", "complesso nuragico di Lu Brandali", "tafoni e sistemi rocciosi di Capo Testa", "ZSC Capo Testa e Area Marina Protetta Capo Testa – Punta Falcone", "blue-green economy"]),
 "tempio-pausania": dict(
    inquadramento=["Tempio Pausania è uno dei Comuni centrali del progetto per dimensione territoriale, presenza forestale, sugherete, prati artificiali, seminativi e potenziale ruolo di governance. Presenta una forte vocazione bosco-sughero, ma anche rilevanti criticità pedologiche.",
                  "Tempio Pausania rappresenta il principale polo urbano e amministrativo dell’Alta Gallura interna, centro di riferimento sovracomunale per servizi pubblici, funzioni scolastiche, attività sanitarie e governance territoriale. Il territorio comunale è impostato sulla struttura granitica del massiccio del Limbara, in gran parte Zona Speciale di Conservazione della rete Natura 2000."],
    bosco_sughero="Tempio Pausania è un Comune prioritario per la filiera sughero, con circa 1.937 ha di sugherete. La presenza di sugherete su C2 suggerisce possibilità di approfondimento gestionale; quelle su C1 richiedono maggiore cautela. Tempio può inoltre assumere un ruolo di coordinamento territoriale per filiera, governance, servizi e trasformazione.",
    suinicola="Tempio presenta interesse per approfondimenti suinicoli, soprattutto per la presenza di prati artificiali e seminativi. Tuttavia, l’uso delle aree forestali e delle sugherete dovrà essere molto selettivo. Eventuali progetti pilota dovranno privilegiare superfici agricole e agro-silvo-pastorali gestibili, con esclusione delle aree fragili.",
    criticita=["ampia superficie su C1", "rischio erosione", "necessità di distinguere sugherete produttive e protettive", "complessità gestionale dovuta alla dimensione comunale"],
    opportunita=["cabina di regia", "mappatura sugherete", "gestione forestale integrata", "aree pilota", "raccordo con trasformazione", "possibile collegamento con mattatoio/trasformazione", "governance delle filiere"],
    valutazione="vocazione sughericola alta; interesse suinicolo medio-alto da verificare; ruolo governance alto; fragilità medio-alta",
    identitari=["massiccio del Limbara (1359 m) e ZSC Monte Limbara", "centro storico in granito grigio e rosa", "chiese monumentali e palazzi nobiliari", "tradizioni corali e Carnevale", "Nuraghe Majori e Nuraghe Budas", "polo AGRIS per la sughericoltura", "mattatoio di Tempio"]),
 "trinita-d-agultu-e-vignola": dict(
    inquadramento=["Trinità d'Agultu e Vignola presenta una forte componente di macchia, gariga, prati artificiali, boschi e pascoli, con presenza limitata di sugherete. Il Comune appare rilevante per gestione del paesaggio mediterraneo, prevenzione incendi, connessione costa-interno e possibili sbocchi turistico-commerciali.",
                  "Trinità d'Agultu e Vignola presenta una struttura fortemente influenzata dalla dicotomia territoriale tra la fascia costiera turistica e l’entroterra rurale, nell’Alta Gallura nord-occidentale, dove rilievi granitici, sistemi vallivi, falesie costiere e cale sabbiose generano un paesaggio ad alta complessità. Il Rio Vignola è la principale direttrice idrologica; il litorale è tutelato in parte dalla ZPS “Da Capo Testa all’Isola Rossa”."],
    bosco_sughero="La presenza di sugherete è limitata ma non assente. Il Comune non appare prioritario per produzione sughericola primaria, ma può contribuire alla rete territoriale attraverso gestione forestale, prevenzione incendi e valorizzazione paesaggistica.",
    suinicola="La presenza di prati artificiali e pascoli naturali suggerisce un possibile approfondimento, ma da condurre con cautela. Il contesto costiero/turistico e l’ampia diffusione di C1/C2 rendono preferibili eventuali sperimentazioni aziendali molto controllate e non diffuse.",
    criticita=["gariga e macchia su suoli fragili", "rischio erosione", "vegetazione rada", "pressione turistica", "necessità di verificare habitat e vincoli costieri"],
    opportunita=["connessione con turismo e ristorazione", "gestione del mosaico mediterraneo", "prevenzione incendi", "valorizzazione di prodotti territoriali", "eventuali aziende pilota in aree non fragili"],
    valutazione="vocazione sughericola medio-bassa; interesse suinicolo medio ma prudenziale; ruolo turistico-commerciale medio-alto",
    identitari=["Rio Vignola", "falesie, cale sabbiose e sistemi dunali", "Domus de Janas di Conca di Li Fati", "Torre aragonese di Vignola", "ZPS Da Capo Testa all’Isola Rossa", "stazzi dell’entroterra", "porto di Isola Rossa"]),
 "viddalba": dict(
    inquadramento=["Viddalba presenta un territorio con gariga, macchia mediterranea, boschi di latifoglie, prati artificiali e pascoli naturali. La presenza di sugherete è molto limitata. Il Comune appare interessante per gestione del mosaico rurale-seminaturale e per eventuali approfondimenti agro-pastorali, ma non come asse primario della filiera sughericola.",
                  "Viddalba si colloca nel settore sud-occidentale dell’Alta Gallura come territorio di transizione tra il sistema collinare interno e la piana alluvionale del medio corso del fiume Coghinas; l’acqua rappresenta l’elemento identitario e funzionale dominante del paesaggio. L’elemento di maggiore spicco è costituito dalle sorgenti termali di Casteldoria; la bassa valle del Coghinas ricade parzialmente nel sito Natura 2000 “Foci del Coghinas”."],
    bosco_sughero="La presenza di sugherete è marginale. Viddalba non appare Comune prioritario per la filiera sughero produttiva, ma può rientrare in una strategia più ampia di gestione forestale, paesaggio rurale e connessione con economie locali.",
    suinicola="Il Comune può essere oggetto di approfondimento limitato per la filiera suinicola, soprattutto in relazione a prati artificiali e pascoli naturali. La presenza di B2 e C2 richiede cautela per rischio erosivo e condizioni di suoli poco o mediamente profondi. Le aree su C1 devono essere trattate con maggiore prudenza.",
    criticita=["gariga e macchia su unità con limitazioni", "rischio erosione", "sugherete marginali", "necessità di verificare disponibilità aziendali, idrica e infrastrutturale"],
    opportunita=["aziende agro-pastorali", "gestione del mosaico macchia-gariga-pascolo", "possibili superfici pilota controllate", "connessione con trasformazione e vendita locale"],
    valutazione="vocazione sughericola bassa; interesse suinicolo medio-basso; fragilità media; ruolo agro-pastorale da approfondire",
    identitari=["piana alluvionale e terrazzi del fiume Coghinas", "sorgenti termali di Casteldoria", "necropoli puniche e romane con stele figurate (museo civico)", "Foci del Coghinas (Natura 2000, parziale)", "corridoio ecologico fluviale", "porta d’accesso ecologica all’Alta Gallura"]),
}

# =====================================================================================================
def num(x):
    return x

def write_json(name, obj):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")

def write_csv(name, header, rows):
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            w.writerow(["" if v is None else v for v in r])

incoerenze = []

# ---------------------------------------------------------------- 1. USO DEL SUOLO
uso_rows, uso_csv = [], []
for slug, nome, _, _ in COMUNI:
    pag, righe = USO[slug]
    for i, (classe, ha, pct) in enumerate(righe, 1):
        p = USO_PAG_RIGA.get((slug, classe), pag)
        uso_rows.append({"comune": nome, "slug": slug, "classe_uso_suolo": classe, "rango": i, "superficie_ha": ha, "incidenza_pct": pct,
                         "origine": "tabella", "pagina_pdf": p, "nota": None})
    if slug in SUGHERETE_TESTO:
        p, ha, cit = SUGHERETE_TESTO[slug]
        uso_rows.append({"comune": nome, "slug": slug, "classe_uso_suolo": "Sugherete", "rango": None, "superficie_ha": ha, "incidenza_pct": None,
                         "origine": "testo", "pagina_pdf": p, "nota": cit if ha else "Valore 0: " + cit})
# quadro sugherete per comune
sugherete = []
for slug, nome, _, _ in COMUNI:
    if slug in SUGHERETE_TABELLA:
        p, ha = SUGHERETE_TABELLA[slug]
        pct = [r[2] for r in USO[slug][1] if r[0] == "Sugherete"][0]
        sugherete.append({"comune": nome, "slug": slug, "superficie_ha": ha, "incidenza_pct": pct, "origine": "tabella", "pagina_pdf": p, "nota": None})
    else:
        p, ha, cit = SUGHERETE_TESTO[slug]
        sugherete.append({"comune": nome, "slug": slug, "superficie_ha": ha, "incidenza_pct": None, "origine": "testo", "pagina_pdf": p,
                          "nota": cit if ha else "Valore 0 attribuito perché il documento dichiara che le tabelle non riportano sugherete: " + cit})

# controllo coerenza ha/pct -> superficie implicita
for slug, nome, _, _ in COMUNI:
    impl = []
    for classe, ha, pct in USO[slug][1]:
        impl.append(ha / pct * 100)
    for u, ha, pct in PEDO[slug][1]:
        if pct >= 1.0:
            impl.append(ha / pct * 100)
    spread = (max(impl) - min(impl)) / min(impl) * 100
    if spread > 3:
        incoerenze.append(f"{nome}: superficie comunale implicita (ha/%) variabile del {spread:.1f}% tra le righe")

uso = {
    "titolo": "Uso del suolo per Comune dell'Unione Alta Gallura (principali classi CORINE, Carta dell'Uso del Suolo 2008) e superficie delle sugherete",
    "fonte": {"documento": "parte1", "capitolo": CAP08 + " – Schede comunali preliminari, par. 'Sintesi dell’uso del suolo'", "pagine_pdf": list(range(156, 172))},
    "note": [
        "Le schede riportano solo le prime 6 classi di uso del suolo per Comune (le 'principali classi'); l'elenco completo per Comune non è pubblicato nel documento (le tabelle finali pag. 173-219 contengono vocazioni, ambiti e roadmap, non tabelle estese di uso del suolo). Le percentuali quindi non sommano a 100.",
        "incidenza_pct è la 'Percentuale della superficie rispetto al territorio comunale' (pag. 153); la superficie di riferimento è l'area comunale risultante dall'intersezione GIS Comuni × Uso del Suolo 2008 × Carta dei Suoli (esclude piccole porzioni costiere non coincidenti tra i layer, pag. 151-152).",
        "La superficie comunale totale NON è riportata nel documento: campo superficie_comunale_ha assente/null. Il rapporto superficie_ha/incidenza_pct restituisce un valore indicativo ma non è un dato del documento.",
        "Righe con origine='testo': superficie delle sugherete citata nel testo delle schede quando le sugherete non rientrano tra le prime 6 classi ('circa N ha'); incidenza_pct non riportata. Per Badesi e Santa Teresa Gallura il documento dichiara che le tabelle non evidenziano sugherete: valore 0 con nota.",
        "Etichette delle classi mantenute come nel documento; nota che 'Seminativi in aree non irrigue' (Calangianus, Luras) e 'Seminativi non irrigui' (Tempio Pausania) indicano verosimilmente la stessa classe CORINE.",
        "Fonte cartografica: Carta dell'Uso del Suolo della Sardegna 2008 (CORINE Land Cover, scala 1:25.000), elaborata in QGIS 3.34 (pag. 149-152).",
        "Nome di Trinità d'Agultu e Vignola scritto con apostrofo semplice (nel PDF è tipografico) per coerenza con gli altri dataset della cartella.",
    ],
    "dati": uso_rows,
    "sugherete_per_comune": sugherete,
}
write_json("uso-suolo-comuni.json", uso)
write_csv("uso-suolo-comuni.csv", ["comune", "slug", "classe_uso_suolo", "rango", "superficie_ha", "incidenza_pct", "origine", "pagina_pdf", "nota"],
          [[r["comune"], r["slug"], r["classe_uso_suolo"], r["rango"], r["superficie_ha"], r["incidenza_pct"], r["origine"], r["pagina_pdf"], r["nota"]] for r in uso_rows])

# ---------------------------------------------------------------- 2. PEDOLOGIA
pedo_rows = []
for slug, nome, _, _ in COMUNI:
    pag, righe = PEDO[slug]
    for i, (u, ha, pct) in enumerate(righe, 1):
        pedo_rows.append({"comune": nome, "slug": slug, "unita_pedologica": u, "rango": i, "superficie_ha": ha, "incidenza_pct": pct, "pagina_pdf": pag})
somme = {slug: round(sum(r[2] for r in PEDO[slug][1]), 1) for slug in PEDO}
pedo = {
    "titolo": "Unità pedologiche per Comune dell'Unione Alta Gallura (Carta dei Suoli della Sardegna 1:250.000)",
    "fonte": {"documento": "parte1", "capitolo": CAP08 + " – Schede comunali preliminari, par. 'Sintesi pedologica'", "pagine_pdf": [156, 158, 160, 161, 162, 164, 165, 167, 168, 169, 171]},
    "note": [
        f"Le schede riportano le 'principali unità pedologiche' (4-5 per Comune). La somma delle incidenze per Comune è compresa tra il {str(min(somme.values())).replace('.', ',')}% e il {str(max(somme.values())).replace('.', ',')}%: " + "; ".join(f"{NOME[s]} {somme[s]}%" for s in somme) + ". La quota residua non è dettagliata nel documento.",
        "I codici unità (C1, C2, B2, M1...) sono quelli della Carta dei Suoli della Sardegna (Aru, Baldaccini, Vacca, 1991; pag. 150). Il documento non riporta la legenda ufficiale: le descrizioni in unita_pedologiche sono ricavate dai commenti delle schede (pagine indicate) e per B3, G1, I1 il documento non fornisce una descrizione specifica.",
        "commenti_per_comune riporta il testo interpretativo della scheda sul quadro pedologico comunale.",
        "Superficie di riferimento: vedi note di uso-suolo-comuni.json (intersezione GIS, pag. 151-152).",
    ],
    "dati": pedo_rows,
    "unita_pedologiche": UNITA_PEDOLOGICHE,
    "commenti_per_comune": [{"comune": NOME[s], "slug": s, "pagina_pdf": PEDO_COMMENTO[s][0], "testo": PEDO_COMMENTO[s][1]} for s, _, _, _ in COMUNI],
}
write_json("pedologia-comuni.json", pedo)
write_csv("pedologia-comuni.csv", ["comune", "slug", "unita_pedologica", "rango", "superficie_ha", "incidenza_pct", "pagina_pdf"],
          [[r["comune"], r["slug"], r["unita_pedologica"], r["rango"], r["superficie_ha"], r["incidenza_pct"], r["pagina_pdf"]] for r in pedo_rows])

# ---------------------------------------------------------------- 3. MATRICE
mat = []
for slug, nome, _, _ in COMUNI:
    pag, righe, lettura = MATRICE[slug]
    combos = []
    for i, (c, ha, pct) in enumerate(righe, 1):
        classe, unita = c.rsplit(" su ", 1)
        combos.append({"combinazione": c, "classe_uso_suolo": classe, "classe_uso_suolo_normalizzata": CLASSE_NORMALIZZATA.get(classe, classe),
                       "unita_pedologica": unita, "rango": i, "superficie_ha": ha, "incidenza_pct": pct})
    mat.append({"comune": nome, "slug": slug, "pagina_pdf": pag, "combinazioni": combos, "lettura": lettura})
matrice = {
    "titolo": "Matrice pedologia × uso del suolo: principali combinazioni per Comune (Alta Gallura)",
    "fonte": {"documento": "parte1", "capitolo": CAP08 + " – Schede comunali preliminari, par. 'Lettura della matrice pedologia × uso del suolo'", "pagine_pdf": [156, 158, 160, 161, 163, 164, 165, 167, 168, 170, 171]},
    "note": [
        "Per ogni Comune il documento pubblica solo le 5 combinazioni principali (classe di uso del suolo su unità pedologica) con superficie in ha e incidenza % sul territorio comunale; la matrice completa (tabella 'Comuni intersezione UdS-Pedologia', pag. 153) non è riprodotta nel documento.",
        "Il campo combinazione è la stringa originale; classe_uso_suolo e unita_pedologica sono ricavati separando su ' su '. Alcune etichette sono abbreviate rispetto alla tabella dell'uso del suolo (es. 'Seminativi', 'Boschi misti', 'Pascolo naturale', 'Seminativi non irrigui'): classe_uso_suolo_normalizzata le riporta alla dicitura della tabella di uso del suolo della stessa scheda.",
        "lettura è il commento interpretativo della scheda (testo fedele).",
    ],
    "dati": mat,
}
write_json("matrice-pedologia-uso-suolo.json", matrice)

# ---------------------------------------------------------------- 4. SINTESI COMPARATIVA
sint_rows = [{"comune": NOME[s], "slug": s, "vocazione_sughericola": a, "interesse_suinicolo_agroforestale": b, "fragilita_pedologica": c, "priorita_approfondimento": d}
             for s, a, b, c, d in SINTESI]
gruppi = [dict(g, comuni_nomi=[NOME[c] for c in g["comuni"]], comuni_parziali_nomi=[NOME[c] for c in g["comuni_parziali"]], pagina_pdf=172) for g in GRUPPI_FUNZIONALI]
quadro = [{"vocazione_prevalente": v, "comuni_testo": ct, "comuni": cs, "comuni_nomi": [NOME[c] for c in cs], "ruolo_preliminare": r, "pagina_pdf": 178} for v, ct, cs, r in QUADRO_VOCAZIONI]
sintesi = {
    "titolo": "Sintesi comparativa preliminare dei Comuni: vocazione sughericola, interesse suinicolo agroforestale, fragilità pedologica, priorità di approfondimento; gruppi funzionali e quadro delle vocazioni territoriali",
    "fonte": {"documento": "parte1", "capitolo": CAP08 + " – Sintesi comparativa preliminare, Lettura conclusiva preliminare, Quadro sintetico delle vocazioni territoriali", "pagine_pdf": [172, 178]},
    "note": [
        "Categorie qualitative mantenute come nel documento; le forme spezzate dall'estrazione PDF ('Medio- bassa', 'Medio- alta') sono state ricomposte in 'Medio-bassa', 'Medio-alta'.",
        "Nella tabella la fragilità pedologica di Badesi (Media), Santa Teresa Gallura (Medio-alta) e Trinità d'Agultu e Vignola (Medio-alta) compare solo qui: le relative schede comunali (pag. 160, 167, 170) non esplicitano un giudizio di fragilità nella valutazione preliminare.",
        "gruppi_funzionali: i quattro gruppi della 'Lettura conclusiva preliminare' (pag. 172); un Comune può appartenere a più gruppi (Aggius a tre, Tempio Pausania e Calangianus a due, Luras a due). comuni_parziali indica i Comuni citati come 'in parte'/'parte di'.",
        "quadro_vocazioni_territoriali: tabella di pag. 178 (8 vocazioni prevalenti) che riorganizza gli stessi giudizi; qui Luogosanto è incluso tra i Comuni 'sughericola integrata', mentre a pag. 172 il gruppo prioritario bosco-sughero cita 'Calangianus e Tempio Pausania, seguiti da Luras e Aggius' senza Luogosanto (che compare nell'Ambito 1 di pag. 179 con i 5 Comuni).",
        "Il documento avverte che la matrice 'non deve essere interpretata come una graduatoria definitiva' e che per la filiera suinicola 'nessun Comune va dichiarato idoneo in modo definitivo in questa fase' (pag. 172).",
    ],
    "dati": sint_rows,
    "gruppi_funzionali": gruppi,
    "quadro_vocazioni_territoriali": quadro,
}
write_json("sintesi-comparativa-comuni.json", sintesi)
write_csv("sintesi-comparativa-comuni.csv", ["comune", "slug", "vocazione_sughericola", "interesse_suinicolo_agroforestale", "fragilita_pedologica", "priorita_approfondimento"],
          [[r["comune"], r["slug"], r["vocazione_sughericola"], r["interesse_suinicolo_agroforestale"], r["fragilita_pedologica"], r["priorita_approfondimento"]] for r in sint_rows])

# ---------------------------------------------------------------- 5. SCHEDE
schede = []
sint_by = {r["slug"]: r for r in sint_rows}
sugh_by = {r["slug"]: r for r in sugherete}
for slug, nome, pag_s, pag_p3 in COMUNI:
    s = SCHEDE[slug]
    ambito, tipologia, funzione, elementi, ruolo = TAB2A[slug]
    schede.append({
        "slug": slug, "comune": nome, "fascia": FASCIA[slug], "posizione_parte3": POSIZIONE_P3.get(slug, "fascia costiera ed estuariale" if FASCIA[slug]=="costiera" else "settore collinare e montano dell'interno"),
        "tab_2a": {"ambito_territoriale": ambito, "tipologia_territoriale": tipologia, "funzione_territoriale": funzione,
                   "elementi_paesaggistici_dominanti": elementi, "ruolo_strategico": ruolo, "pagina_pdf": 37},
        "funzione_territoriale": funzione,
        "ruolo_paesaggistico": elementi + " – " + ruolo,
        "inquadramento": s["inquadramento"],
        "sugherete_ha": sugh_by[slug]["superficie_ha"],
        "implicazioni_bosco_sughero": s["bosco_sughero"],
        "implicazioni_suinicola": s["suinicola"],
        "criticita": s["criticita"],
        "opportunita": s["opportunita"],
        "valutazione_preliminare": s["valutazione"],
        "sintesi_comparativa": {k: sint_by[slug][k] for k in ("vocazione_sughericola", "interesse_suinicolo_agroforestale", "fragilita_pedologica", "priorita_approfondimento")},
        "elementi_identitari": s["identitari"],
        "pagine_fonte": {"scheda_preliminare": pag_s, "quadro_sinottico_parte3": pag_p3, "tabella_2a": [37], "sintesi_comparativa": [172]},
    })
schede_json = {
    "titolo": "Schede territoriali dei Comuni dell'Unione Alta Gallura (funzione territoriale, inquadramento, implicazioni per le filiere, criticità, opportunità, elementi identitari)",
    "fonte": {"documento": "parte1", "capitolo": f"{CAP03} (Tab. 2a, pag. 37); {CAP04} (pag. 53-68); {CAP08} – Schede comunali preliminari (pag. 156-172)", "pagine_pdf": [37] + list(range(53, 69)) + list(range(156, 173))},
    "note": [
        "fascia: costiera (Aglientu, Badesi, Santa Teresa Gallura, Trinità d'Agultu e Vignola) / interna (gli altri 7 Comuni), coerente con la classificazione costa/entroterra usata dallo studio e dagli altri dataset della cartella. posizione_parte3 riporta la lettura del quadro sinottico (pag. 53), che colloca Viddalba 'in posizione di cerniera idrografica e di transizione' tra le due macro-aree.",
        "tab_2a: la Tabella 2a (pag. 37) è per ambiti territoriali, alcuni pluricomunali ('Calangianus – Tempio Pausania', 'Luogosanto – Luras – Aggius', 'Aglientu – Badesi'): i valori sono ripetuti per ciascun Comune dell'ambito. Per 'Aglientu – Badesi' la cella tipologia riporta 'Costa Interfaccia entroterra-costa' (probabile fusione di due valori nell'estrazione), resa qui come 'Costa / Interfaccia entroterra-costa'. Il titolo della tabella parla di 'ruolo paesaggistico': il campo ruolo_paesaggistico concatena le colonne 'Elementi paesaggistici dominanti' e 'Ruolo strategico'.",
        "inquadramento: prima frase/e = 'Inquadramento sintetico' della scheda preliminare (Allegato II), fedele al testo; ultima frase = sintesi fedele del quadro sinottico della Terza parte.",
        "implicazioni_bosco_sughero e implicazioni_suinicola: testo integrale dei par. X.5 e X.6 delle schede. criticita e opportunita: elenchi ricavati spezzando i par. X.7 e X.8 sulle virgole del testo originale. valutazione_preliminare: frase conclusiva del par. X.8, con ricomposizione delle parole spezzate ('bassomedio' → 'basso-medio', 'medioalta' → 'medio-alta').",
        "sugherete_ha: come in uso-suolo-comuni.json (0 = il documento dichiara che le tabelle non riportano sugherete).",
        "elementi_identitari: elenco redazionale di luoghi, beni e caratteri citati nel quadro sinottico della Terza parte (e, per Luras e Tempio, nella Seconda parte pag. 38 e 47); non è una lista esaustiva del documento.",
        "Incoerenza narrativa: la Terza parte descrive Bortigiadas con 'sugherete, leccete e macchia mediterranea evoluta [che] occupano la maggior parte della superficie comunale' (pag. 59), mentre le tabelle GIS attribuiscono a Bortigiadas solo circa 116 ha di sugherete (pag. 161); analogamente per Aggius ('dominato da sugherete, leccete e macchia', pag. 54) le sugherete sono il 6,9% del territorio.",
    ],
    "dati": schede,
}
write_json("schede-comuni.json", schede_json)

# ---------------------------------------------------------------- 6. NATURA 2000 E VINCOLI
natura = {
    "titolo": "Siti Natura 2000 e altre aree tutelate, vincoli, vulnerabilità ambientali e rischio incendio nell'Unione Alta Gallura",
    "fonte": {"documento": "parte1", "capitolo": f"{CAP03} par. 2.2.1, 2.2.6-2.2.9 (pag. 39-46); {CAP04} (pag. 56-68); Quarta parte par. 4.4.1-4.4.2 (pag. 75-77); {CAP08} (pag. 197, 213)", "pagine_pdf": [39, 40, 43, 44, 45, 46, 56, 58, 64, 65, 66, 67, 75, 76, 77, 197, 213]},
    "note": [
        "Il documento non riporta i codici ufficiali (ITB...) dei siti Natura 2000 né un elenco tabellare: i siti sono quelli citati nel testo, con la tipologia indicata dal documento (null se non specificata). L'unica superficie riportata è quella del Monte Limbara (16588 ha, pag. 44).",
        "comuni_interessati: solo i Comuni esplicitamente associati al sito nel testo; [] se il documento non li indica (es. 'Isola Rossa – Costa Paradiso' citato a pag. 44 senza riferimento comunale).",
        "Il documento indica a pag. 44 che i SIC sono 'divenuti ormai Zone Speciali di Conservazione (ZSC)'.",
        "Rischio incendio: il documento non fornisce classi di rischio né statistiche di eventi per Comune; i soli dati numerici sono l'intensità di fuoco simulata (>1600 kW/m, pag. 40) e i parametri climatici del bilancio idrico (pag. 40 e 48). I 'Comuni prioritari per prevenzione incendi' provengono dall'Ambito 4 dell'Allegato II (pag. 183, 189).",
        "I parametri climatici di pag. 48 sono riferiti alla stazione di Caddau (557 m s.l.m.), Unità Gestionale di Base Limbara Sud (comune di Berchidda, esterno all'Unione), usata come riferimento per il massiccio del Limbara.",
    ],
    "dati": {
        "siti_natura_2000": [
            {"nome": "Monte Limbara", "tipologia": "ZSC", "codice": None, "superficie_ha": 16588, "comuni_interessati": ["tempio-pausania"], "comuni_interessati_nomi": ["Tempio Pausania"],
             "descrizione": "Habitat forestali montani e formazioni granitiche di elevato pregio naturalistico; corridoio ecologico di rango regionale per numerose specie endemiche vegetali e animali; il massiccio ospita habitat prioritari 'inseriti in gran parte all'interno della relativa Zona Speciale di Conservazione'.", "pagine_pdf": [44, 65]},
            {"nome": "Monte Russu", "tipologia": "ZSC", "codice": None, "superficie_ha": None, "comuni_interessati": ["aglientu"], "comuni_interessati_nomi": ["Aglientu"],
             "descrizione": "Habitat prioritari e sistemi psammofili (spiagge, dune, ginepreti, ambienti retrodunali) di eccezionale valore fitogeografico.", "pagine_pdf": [56]},
            {"nome": "Foci del Coghinas", "tipologia": None, "codice": None, "superficie_ha": None, "comuni_interessati": ["badesi", "viddalba"], "comuni_interessati_nomi": ["Badesi", "Viddalba"],
             "descrizione": "Aree umide della foce del Coghinas; tutela habitat psammofili di interesse comunitario e comunità arbustive costiere. Il continuum costiero di Badesi è 'integralmente inserito' nel sito; la bassa valle del Coghinas in territorio di Viddalba 'ricade parzialmente' nel sito.", "pagine_pdf": [44, 58, 67]},
            {"nome": "Capo Testa", "tipologia": "ZSC", "codice": None, "superficie_ha": None, "comuni_interessati": ["santa-teresa-gallura"], "comuni_interessati_nomi": ["Santa Teresa Gallura"],
             "descrizione": "Sistemi rocciosi granitici e tafoni di Capo Testa, geosistema di valore internazionale.", "pagine_pdf": [63, 64]},
            {"nome": "Da Capo Testa all’Isola Rossa", "tipologia": "ZPS", "codice": None, "superficie_ha": None, "comuni_interessati": ["trinita-d-agultu-e-vignola"], "comuni_interessati_nomi": ["Trinità d'Agultu e Vignola"],
             "descrizione": "Area cardine per la salvaguardia dell'avifauna marina e l'integrità ecologica del litorale; spiagge e dune con habitat prioritari e praterie di Posidonia oceanica. Tutela 'in parte' gli ambienti costieri del Comune.", "pagine_pdf": [66]},
            {"nome": "Isola Rossa – Costa Paradiso", "tipologia": None, "codice": None, "superficie_ha": None, "comuni_interessati": [], "comuni_interessati_nomi": [],
             "descrizione": "Sistemi costieri citati tra i siti della Rete Natura 2000 dell'Unione; il documento non ne specifica tipologia né Comuni.", "pagine_pdf": [44]},
        ],
        "altre_aree_tutelate": [
            {"nome": "Area Marina Protetta Capo Testa – Punta Falcone", "tipologia": "Area Marina Protetta", "comuni_interessati": ["santa-teresa-gallura"], "comuni_interessati_nomi": ["Santa Teresa Gallura"],
             "descrizione": "Istituita per la salvaguardia di habitat prioritari quali il coralligeno e le praterie di Posidonia oceanica; nodo strategico per la tutela dell'avifauna e dei cetacei nel corridoio delle Bocche di Bonifacio.", "pagine_pdf": [64]},
        ],
        "habitat_prioritari_citati": [
            {"habitat": "Sugherete a Quercus suber", "pagine_pdf": [44, 76]},
            {"habitat": "Macchie mediterranee", "pagine_pdf": [44, 76]},
            {"habitat": "Formazioni riparie", "pagine_pdf": [44]},
            {"habitat": "Sistemi dunali costieri / habitat psammofili", "pagine_pdf": [44, 56, 58]},
            {"habitat": "Ambienti rupicoli", "pagine_pdf": [76]},
            {"habitat": "Zone umide temporanee", "pagine_pdf": [76]},
            {"habitat": "Coralligeno e praterie di Posidonia oceanica (marini)", "pagine_pdf": [64, 66]},
        ],
        "vincoli": [
            {"vincolo": "Disciplina paesaggistica regionale (Piano Paesaggistico Regionale – PPR; NTA artt. 5 e 9 sui caratteri identitari)", "ambito": "intera Unione", "pagine_pdf": [34, 44]},
            {"vincolo": "Tutela della fascia costiera dei 300 m", "ambito": "Comuni costieri", "pagine_pdf": [44]},
            {"vincolo": "Prescrizioni associate ai siti Natura 2000 (misure di conservazione; Valutazione di Incidenza Ambientale)", "ambito": "siti elencati", "pagine_pdf": [18, 43, 44]},
            {"vincolo": "Piano Stralcio per l'Assetto Idrogeologico (PAI): aree a pericolosità idraulica e geomorfologica", "ambito": "intera Unione", "pagine_pdf": [44, 45]},
            {"vincolo": "Piano di Gestione del Rischio Alluvioni (PGRA) e cartografie di pericolosità PAI per il monitoraggio del rischio", "ambito": "intera Unione", "pagine_pdf": [45]},
            {"vincolo": "Vincoli idraulici e paesaggistici degli ambienti retrodunali", "ambito": "Aglientu (fascia costiera)", "pagine_pdf": [56]},
            {"vincolo": "Vincoli idraulici e rischio di inondazione delle aree alluvionali della foce/valle del Coghinas", "ambito": "Badesi, Viddalba", "pagine_pdf": [58, 67]},
            {"vincolo": "Vincoli forestali, paesaggistici, idrogeologici, urbanistici e sanitari da verificare prima di progettazioni attuative", "ambito": "intera Unione (indicazione metodologica)", "pagine_pdf": [197]},
            {"vincolo": "Esclusione preliminare delle aree Natura 2000 senza verifica specifica per la sperimentazione suinicola", "ambito": "filiera suinicola", "pagine_pdf": [213]},
        ],
        "vulnerabilita": [
            {"vulnerabilita": "Erosione marina e regressione delle dune sabbiose; instabilità dei sistemi dunali e alterazione degli equilibri sedimentari, accentuate da pressione turistica stagionale ed eventi meteorologici estremi", "ambito": "sistemi costieri, in particolare Badesi e Trinità d'Agultu e Vignola", "pagine_pdf": [45]},
            {"vulnerabilita": "Versanti interni a matrice granitica con suoli poco profondi, elevata erodibilità e suscettibilità al dissesto superficiale; processi erosivi amplificati da perdita di copertura vegetale, sovraccarico di superfici pascolive e abbandono delle sistemazioni agrarie tradizionali", "ambito": "entroterra", "pagine_pdf": [45]},
            {"vulnerabilita": "Ruscellamento concentrato ed erosione superficiale da canalizzazione (pendenze, superficialità pedologica, eventi meteorici estremi)", "ambito": "intera Unione", "pagine_pdf": [40]},
            {"vulnerabilita": "Frammentazione degli ecotoni costieri e alterazione della vegetazione pioniera per calpestio e frequentazione estiva", "ambito": "Aglientu, Badesi, Trinità d'Agultu e Vignola", "pagine_pdf": [56, 58, 66]},
            {"vulnerabilita": "Deficit idrico estivo: riserva utile del suolo azzerata a settembre, periodo arido di circa 99 giorni cumulativi/anno", "ambito": "intera Unione (clima)", "pagine_pdf": [40, 48]},
        ],
        "rischio_incendio": {
            "sintesi": "Il rischio incendio è definito 'la minaccia ambientale più immediata e sistemica' per il patrimonio dell'Alta Gallura; gli effetti citati sono perdita di biomassa, compromissione degli habitat, riduzione del sequestro di carbonio, incremento dell'erosione e danni alle filiere. Le sugherete sono asset strategico e vulnerabile: eventi ripetuti o intensi ne compromettono la capacità produttiva. La prevenzione proposta è la gestione attiva del combustibile e il presidio produttivo (manutenzione del sottobosco, fasce tagliafuoco, viabilità forestale, gestione delle interfacce urbano-rurali, monitoraggio) integrata con il pascolo controllato bovino e suinicolo, incluso il pascolo ghiandatico regolato nelle sugherete. L'Allegato II precisa che l'allevamento suino non va assunto automaticamente come soluzione al rischio incendio.",
            "classi_rischio": None,
            "dati_numerici": [
                {"indicatore": "Intensità lineare del fuoco simulata (modelli pirologici predittivi, FlamMap) in presenza di macchia alta e continua", "valore": 1600, "operatore": ">", "unita": "kW/m", "nota": "preclude l'attacco manuale diretto", "pagina_pdf": 40},
                {"indicatore": "Periodo arido cumulativo annuo (bilancio idrico di Thornthwaite)", "valore": 99, "operatore": "circa", "unita": "giorni/anno", "nota": "concentrati tra metà maggio e metà ottobre; riserva utile azzerata a settembre", "pagina_pdf": 40},
                {"indicatore": "Deficit idrico reale annuo", "valore": 269, "operatore": "=", "unita": "mm", "nota": "riserva utile standard del suolo 100 mm; stazione di Caddau (Limbara Sud)", "pagina_pdf": 48},
                {"indicatore": "Piovosità media annua (stazione di Caddau, 557 m s.l.m.)", "valore": 954.1, "operatore": "=", "unita": "mm", "nota": "massimo dicembre 135,9 mm; trimestre estivo 70,1 mm; minimo luglio 8,4 mm", "pagina_pdf": 48},
                {"indicatore": "Surplus idrico annuo", "valore": 435, "operatore": "=", "unita": "mm", "nota": None, "pagina_pdf": 48},
            ],
            "pratiche_prevenzione": ["manutenzione del sottobosco", "realizzazione e mantenimento di fasce tagliafuoco", "miglioramento della viabilità forestale", "gestione delle interfacce urbano-rurali", "monitoraggio periodico delle aree maggiormente esposte", "pascolo controllato bovino e suinicolo per la riduzione della biomassa combustibile fine", "pascolo ghiandatico regolato nelle sugherete", "selvicoltura preventiva"],
            "comuni_prioritari_prevenzione_incendi": {"slugs": ["calangianus", "tempio-pausania", "luogosanto", "aggius", "luras", "aglientu", "trinita-d-agultu-e-vignola"], "nomi": ["Calangianus", "Tempio Pausania", "Luogosanto", "Aggius", "Luras", "Aglientu", "Trinità d'Agultu e Vignola"], "livello_urgenza": "Alto", "pagine_pdf": [183, 189]},
            "pagine_pdf": [40, 45, 46, 77, 183],
        },
    },
}
write_json("natura-2000-e-vincoli.json", natura)

# ---------------------------------------------------------------- 7. SUPERFICI UNIONE
sup = {
    "titolo": "Superfici e grandezze territoriali di scala sovracomunale riportate nello studio (Unione Alta Gallura, distretti forestali, Limbara)",
    "fonte": {"documento": "parte1", "capitolo": f"{CAP03} par. 2.2.1-2.2.6 (pag. 39-44), 2.3.3 (pag. 47-48)", "pagine_pdf": [39, 40, 41, 42, 44, 48]},
    "note": [
        "Il documento NON riporta la superficie complessiva dell'Unione né totali di superfici agricole, pascolive, forestali o di sugherete a scala di Unione: i relativi indicatori sono presenti con valore null.",
        "La somma dei valori comunali di sugherete pubblicati nelle schede (uso-suolo-comuni.json) è calcolabile ma non compare nel documento e quindi non è riportata come dato.",
        "Il Distretto forestale 01 'Alta Gallura' (150.251 ha) non coincide con il territorio dell'Unione: i distretti 'non sempre coincidono con i confini amministrativi comunali' (pag. 42) e la porzione meridionale di Tempio Pausania (Limbara Sud) ricade nel Distretto 04.",
        "I dati di Berchidda (UGB Limbara Sud, 3.630,1 ha; macchia evoluta 51%) e della stazione di Caddau riguardano un'area esterna all'Unione, usata dallo studio come riferimento per il massiccio del Limbara.",
    ],
    "dati": [
        {"indicatore": "Superficie complessiva dell'Unione dei Comuni dell'Alta Gallura", "valore": None, "unita": "ha", "ambito": "Unione", "pagina_pdf": None, "nota": "non riportata nel documento"},
        {"indicatore": "Superficie agricola totale dell'Unione", "valore": None, "unita": "ha", "ambito": "Unione", "pagina_pdf": None, "nota": "non riportata nel documento"},
        {"indicatore": "Superficie pascoliva totale dell'Unione", "valore": None, "unita": "ha", "ambito": "Unione", "pagina_pdf": None, "nota": "non riportata nel documento"},
        {"indicatore": "Superficie forestale totale dell'Unione / quota boscata", "valore": None, "unita": "ha", "ambito": "Unione", "pagina_pdf": None, "nota": "non riportata nel documento"},
        {"indicatore": "Estensione complessiva delle sugherete dell'Unione", "valore": None, "unita": "ha", "ambito": "Unione", "pagina_pdf": None, "nota": "non riportata; valori per Comune in uso-suolo-comuni.json (sugherete_per_comune)"},
        {"indicatore": "Quota del sughero lavorato a livello nazionale presidiata/gestita dall'Alta Gallura", "valore": 80, "unita": "%", "operatore": "oltre", "ambito": "Alta Gallura", "pagina_pdf": 42, "nota": "ripetuto a pag. 43 ('Oltre l’80 % del sughero lavorato a livello nazionale deriva infatti da questo sistema territoriale')"},
        {"indicatore": "Superficie del Distretto forestale 01 Alta Gallura", "valore": 150251, "unita": "ha", "ambito": "Distretto forestale 01", "pagina_pdf": 42, "nota": "6,2 % della superficie regionale"},
        {"indicatore": "Quota del Distretto forestale 01 sulla superficie regionale", "valore": 6.2, "unita": "%", "ambito": "Distretto forestale 01", "pagina_pdf": 42, "nota": None},
        {"indicatore": "Superficie del Distretto forestale 04 Coghinas-Limbara", "valore": 123387, "unita": "ha", "ambito": "Distretto forestale 04", "pagina_pdf": 42, "nota": "5,1 % del territorio regionale; include il Limbara Sud (porzione meridionale di Tempio Pausania)"},
        {"indicatore": "Quota del Distretto forestale 04 sulla superficie regionale", "valore": 5.1, "unita": "%", "ambito": "Distretto forestale 04", "pagina_pdf": 42, "nota": None},
        {"indicatore": "Superficie del sito Natura 2000 Monte Limbara", "valore": 16588, "unita": "ha", "ambito": "Monte Limbara", "pagina_pdf": 44, "nota": None},
        {"indicatore": "Quota altimetrica del Monte Limbara", "valore": 1359, "unita": "m s.l.m.", "ambito": "Monte Limbara", "pagina_pdf": 39, "nota": "principale nodo morfologico dell'area"},
        {"indicatore": "Superfici a elevata fertilità specifica nel Distretto di Calangianus", "valore": 67, "unita": "%", "operatore": "oltre", "ambito": "Distretto di Calangianus", "pagina_pdf": 41, "nota": "il documento non precisa la superficie di riferimento"},
        {"indicatore": "Provvigione legnosa media delle leccete mature", "valore": 145.96, "unita": "m3/ha", "ambito": "Limbara / complesso forestale", "pagina_pdf": 40, "nota": None},
        {"indicatore": "Turno di estrazione del sughero", "valore": 12, "unita": "anni", "ambito": "Alta Gallura", "pagina_pdf": 42, "nota": "'cicli di decortica decennali e turni di estrazione ottimizzati a dodici anni'"},
        {"indicatore": "Lunghezza della fascia costiera di Aglientu", "valore": 18, "unita": "km", "operatore": "circa", "ambito": "Aglientu", "pagina_pdf": 56, "nota": None},
        {"indicatore": "Superficie dell'Unità Gestionale di Base Limbara Sud (Forestas, comune di Berchidda)", "valore": 3630.1, "unita": "ha", "ambito": "Limbara Sud (esterno all'Unione)", "pagina_pdf": 48, "nota": "macchia evoluta 51 % della superficie"},
        {"indicatore": "Quota della macchia evoluta nell'UGB Limbara Sud", "valore": 51, "unita": "%", "ambito": "Limbara Sud (esterno all'Unione)", "pagina_pdf": 48, "nota": "a pag. 40 il testo parla di 'oltre la metà del territorio demaniale'"},
    ],
}
write_json("superfici-unione.json", sup)

print("incoerenze ha/%:", incoerenze or "nessuna oltre 3%")
print("uso:", len(uso_rows), "pedo:", len(pedo_rows), "matrice:", sum(len(m["combinazioni"]) for m in mat), "sintesi:", len(sint_rows), "schede:", len(schede),
      "siti:", len(natura["dati"]["siti_natura_2000"]), "superfici:", len(sup["dati"]))
