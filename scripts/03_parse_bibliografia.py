#!/usr/bin/env python3
"""Parsing del database bibliografico (Allegato II, pagine 142-194) dai CSV grezzi
`source/parte2-filiera-sughero-sardegna/tables/pNNN-t0.csv` -> JSON + CSV puliti.

Regole:
- prima riga di p142 = header (1,2,3,4,5,6,7,9,10,11,12) -> saltata
- righe con colonne 2 e 3 vuote = continuazione del record precedente (record spezzato su due pagine)
- 11 righe "inferenza" hanno una struttura diversa (10 valori invece di 11): mappate con euristica e flaggate
- pulizia interruzioni di riga dentro le celle tramite dizionario esplicito + regex conservative
"""
import csv, glob, json, os, re, sys, collections

SRC = "/Users/uxfra/Code/RISSTE/source/parte2-filiera-sughero-sardegna/tables"
OUT = "/Users/uxfra/Code/RISSTE/data/sughero-sardegna"

# --- dizionario di ricomposizione parole spezzate / refusi di estrazione (celle 3-12) -------------
FIX_CELLS = [
    ("Materiali/Inn ovazione", "Materiali/Innovazione"),
    ("Cosmesi/Far maceutico/Bi oattivi", "Cosmesi/Farmaceutico/Bioattivi"),
    ("Edilizia/Mater iali", "Edilizia/Materiali"),
    ("Edilizia/isola mento", "Edilizia/isolamento"),
    ("Acustica/isola mento", "Acustica/isolamento"),
    ("bio- based", "bio-based"),
    ("Automotive/A erospazio/Pro tezione", "Automotive/Aerospazio/Protezione"),
    ("Economia circolare/Gov ernance", "Economia circolare/Governance"),
    ("Compositi strutturali/en ergia assorbimento", "Compositi strutturali/energia assorbimento"),
    ("Agricoltura/Bi omassa", "Agricoltura/Biomassa"),
    ("Ambiente/Ac que/Adsorbi mento", "Ambiente/Acque/Adsorbimento"),
    ("Governance/ mercato/filier a", "Governance/mercato/filiera"),
    ("Batetrie", "Batterie"),
    ("Tessile/Footw ear", "Tessile/Footwear"),
    ("Forestale/mat eriali naturali", "Forestale/materiali naturali"),
    ("Additive manufacturin g", "Additive manufacturing"),
    ("giocatotli", "giocattoli"),
    ("Adsorbiment o/tratatment o", "Adsorbimento/trattamento"),
    ("Packaging/en ologia", "Packaging/enologia"),
    ("LCA/Sostenibi lità", "LCA/Sostenibilità"),
    ("Forestale/Svil uppo rurale", "Forestale/Sviluppo rurale"),
    ("funzionalizzaz ione", "funzionalizzazione"),
    ("Sughero/mate riale", "Sughero/materiale"),
    ("Scarti/sototpro dotti", "Scarti/sottoprodotti"),
    ("cork/aluminiu m", "cork/aluminium"),
    ("espanso/agglo merato/granul ato", "espanso/agglomerato/granulato"),
    ("espanso/agglo merato espanso", "espanso/agglomerato espanso"),
    ("naturale/agglo merato", "naturale/agglomerato"),
    ("sughero- polimero", "sughero-polimero"),
    ("agglomerato/c omposito", "agglomerato/composito"),
    ("Polvere/granul i", "Polvere/granuli"),
    ("Granulato/agg regati", "Granulato/aggregati"),
    ("vergine/cortec cia", "vergine/corteccia"),
    ("trasparente/m odificato", "trasparente/modificato"),
    ("sughero/prodo tti", "sughero/prodotti"),
    ("Sughero/attivit à", "Sughero/attività"),
    ("corteccia/sugh ero", "corteccia/sughero"),
    ("naturale/vergi ne", "naturale/vergine"),
    ("vergine/granul ato/agglomera to", "vergine/granulato/agglomerato"),
    ("Medio- Alto", "Medio-Alto"),
    ("Medio- basso", "Medio-basso"),
    ("(stima to)", "(stimato)"),
    ("ND/N on tecnol ogico", "ND/Non tecnologico"),
    ("ND/R eview", "ND/Review"),
    ("Valori zzazio ne e soste nibilit à", "Valorizzazione e sostenibilità"),
    ("★★★ ☆☆", "★★★☆☆"),
    ("★★★ ★★", "★★★★★"),
    ("Infer enza", "Inferenza"),
    ("rispetot", "rispetto"),
    ("distretot", "distretto"),
    ("tratatmento", "trattamento"),
    ("Prometetnte", "Promettente"),
    ("diretat", "diretta"),
    ("prodotot", "prodotto"),
    ("soprattutot", "soprattutto"),
    ("Polonia/Mala ysia", "Polonia/Malaysia"),
]

# refusi di estrazione (legature tt/ff/fl) nei riferimenti bibliografici
FIX_REF = [
    ("potetd", "potted"), ("metofrmin", "metformin"), ("foloring", "flooring"),
    ("batetries", "batteries"), ("batetry", "battery"), ("difefrential", "differential"),
    ("difefrent", "different"), ("Senf,f", "Senff,"), ("Boukhatetm", "Boukhattem"),
    ("Letetrs", "Letters"), ("actviated", "activated"), ("Efefct", "Effect"),
    ("efefcts", "effects"), ("efefctive", "effective"), ("Dal Poggetot", "Dal Poggetto"),
    ("Otatviano", "Ottaviano"), ("Petetnella", "Pettenella"), ("Sufof,", "Suffo,"),
    ("Applie d Sciences", "Applied Sciences"), ("Cortés- Trivi\\\\~no", "Cortés-Triviño"),
    ("Cortés- Trivi\\~no", "Cortés-Triviño"),
]


def fix_cell(s):
    s = s.strip()
    for a, b in FIX_CELLS:
        s = s.replace(a, b)
    s = re.sub(r"\s+", " ", s)
    return s


def fix_ref(s):
    s = s.strip()
    for a, b in FIX_REF:
        s = s.replace(a, b)
    # trattini di fine riga dentro parole / intervalli numerici
    s = re.sub(r"(?<=[A-Za-zÀ-ÿ])- (?=[A-Za-zÀ-ÿ])", "-", s)
    s = re.sub(r"(?<=\d)- (?=\d)", "-", s)
    s = re.sub(r"(?<=\d)– (?=\d)", "–", s)
    # numeri di fascicolo spezzati: 17(1 2) -> 17(12); 10(4 ) -> 10(4); 17( 19) -> 17(19)
    s = re.sub(r"\((\d+) (\d+)\)", r"(\1\2)", s)
    s = re.sub(r"\((\d+) \)", r"(\1)", s)
    s = re.sub(r"\( (\d+)\)", r"(\1)", s)
    s = re.sub(r"\b1 3\(20\)", "13(20)", s)
    s = re.sub(r"\) , ", "), ", s)
    # URL doi spezzati nel testo del riferimento
    s = re.sub(r"(https?://doi\.org/\S+?) (?=[a-z0-9])", r"\1", s)
    s = re.sub(r"\s+", " ", s)
    return s


def fix_doi(s):
    raw = s.strip()
    if raw in ("", "ND"):
        return None, raw
    d = re.sub(r"\s+(\d+)\s+_\s*$", r"_\1", raw)     # "...-6 2 _" -> "..._2"
    d = re.sub(r"\s+", "", d)
    d = re.sub(r"^https?://", "", d)
    d = re.sub(r"^/?doi\.org/", "", d)
    d = d.lstrip("/")
    d = d.replace("%2F", "/")
    return d, raw


def year_of(ref):
    m = re.search(r"\b(20[0-2]\d)\b", ref)
    return (int(m.group(1)), m.start()) if m else (None, None)


def first_author(ref):
    head = ref[:60]
    if "," in head:
        a = ref.split(",")[0].strip()
    else:
        a = ref.split(" ")[0].strip()
    a = re.sub(r"(\s+[A-Z]\.?)+$", "", a)        # 'Aroso I. M.' -> 'Aroso'; 'Zheliazkova M.' -> 'Zheliazkova'
    a = re.sub(r"\s+[A-Z]\.(?:[A-Z]\.)*$", "", a)   # 'De Almeida I.D.' -> 'De Almeida'
    a = re.sub(r"\s+[A-Z]{1,3}$", "", a)         # 'da Silva Morais A' -> 'da Silva Morais'
    return a.strip() or None


def title_of(ref):
    q = re.search(r"[“\"]([^”\"]{15,300})[”\"]", ref)
    if q:
        return q.group(1).strip()
    y, pos = year_of(ref)
    if y is None or pos > len(ref) * 0.75:
        return None
    rest = ref[pos + 4:]
    rest = re.sub(r"^\)?[.,;]?\s*", "", rest)
    parts = re.split(r"(?<![A-Z])[.?]\s+(?=[A-Z“\"]|https?://|e-Forum)|(?<![A-Z])\.(?=[A-Z][a-z])", rest, maxsplit=1)
    t = parts[0].strip().rstrip(".").strip()
    t = re.sub(r",\s*BioResources.*$", "", t)
    if len(t) < 10 or len(t) > 300 or t[0].isdigit():
        return None
    return t


def trl_range(s):
    if not s:
        return None, None
    m = re.search(r"(\d)\s*[–-]\s*(\d)", s)
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)


PAESE_NORM = {"Brazil": "Brasile", "Poland": "Polonia", "UK": "Regno Unito", "USA": "USA"}


def paesi_list(p):
    if p in ("ND", ""):
        return []
    out = []
    for x in re.split(r"\s*/\s*", p):
        x = x.strip()
        out.append(PAESE_NORM.get(x, x))
    return out


def main():
    files = sorted(f for f in glob.glob(os.path.join(SRC, "p1[4-9][0-9]-t0.csv"))
                   if 142 <= int(os.path.basename(f)[1:4]) <= 194)
    records = []
    for f in files:
        page = int(os.path.basename(f)[1:4])
        for row in csv.reader(open(f, encoding="utf-8")):
            if row[0] == "1" and row[1] == "2":
                continue  # header
            if row[1] == "" and row[2] == "":
                # continuazione del record precedente
                prev = records[-1]
                prev["_ref_raw"] += " " + row[0]
                if row[3]:
                    sep = "" if (prev["_cells"][3][-1:].isalpha() and row[3][:1].islower()) else " "
                    prev["_cells"][3] = prev["_cells"][3] + sep + row[3]
                extra = [i for i in range(4, 11) if row[i]]
                if extra:
                    print("ATTENZIONE continuazione con celle extra", f, row, file=sys.stderr)
                prev["_pages"].append(page)
                continue
            records.append({"_ref_raw": row[0], "_cells": list(row), "_pages": [page]})

    out = []
    for i, r in enumerate(records, 1):
        c = [fix_cell(x) for x in r["_cells"]]
        ref = fix_ref(r["_ref_raw"])
        doi, doi_raw = fix_doi(c[1])
        note = []
        anomala = "★" not in c[8]
        if anomala:
            # struttura: paese, settore, livello, trl, "Valorizzazione e sostenibilità", stelle, "inferenza", priorita, "Inferenza"
            paese, settore, materiale = c[2], c[3], None
            livello, trl, pot_ind = c[4], c[5], None
            stelle_cell, val_cell, prio = c[7], c[8], c[9]
            note.append("Riga con struttura anomala nella fonte (10 valori invece di 11, marcata 'Inferenza'): "
                        "manca la tipologia di materiale; il campo potenziale industriale contiene 'Valorizzazione e sostenibilità' "
                        "e la valutazione scientifica 'inferenza' (non numerica). Mappatura euristica; celle originali in `celle_originali`.")
        else:
            paese, settore, materiale = c[2], c[3], c[4]
            livello, trl, pot_ind = c[5], c[6], c[7]
            stelle_cell, val_cell, prio = c[8], c[9], c[10]

        stelle = stelle_cell.count("★") if "★" in stelle_cell else None
        commento = None
        if "★" in stelle_cell:
            m = re.match(r"^[★☆]+\s*[-–]?\s*(.*)$", stelle_cell)
            commento = m.group(1).strip() or None
        val = int(val_cell) if val_cell.isdigit() else None
        if val is None and val_cell:
            note.append(f"Valutazione scientifica non numerica nella fonte: '{val_cell}'.")

        anno, _ = year_of(ref)
        anno_inferito = False
        if anno is None:
            if ref.startswith("Blanc, S.018"):
                anno, anno_inferito = 2018, True
                note.append("Anno ricostruito: nella fonte compare 'S.018' (refuso) e il record è collocato tra quelli del 2018.")
            elif ref.startswith("Aroso"):
                anno, anno_inferito = 2017, True
                note.append("Anno assente nel riferimento; ricostruito dalla posizione cronologica (tra i record 2017; ACS Sustainable Chem. Eng. vol. 5 = 2017).")
            else:
                note.append("Anno non individuabile nel riferimento.")
        if doi is None:
            note.append("DOI: 'ND' nella fonte." if doi_raw == "ND" else "Cella DOI vuota nella fonte.")
        if len(r["_pages"]) > 1:
            note.append(f"Record spezzato su due pagine ({r['_pages'][0]}-{r['_pages'][1]}) e ricomposto.")

        tmin, tmax = trl_range(trl)
        rec = {
            "id": i,
            "riferimento": ref,
            "anno": anno,
            "anno_inferito": anno_inferito,
            "autore_primo": first_author(ref),
            "titolo": title_of(ref),
            "doi": doi,
            "paese": paese,
            "paesi": paesi_list(paese),
            "settore_applicativo": settore,
            "materiale": materiale,
            "livello_innovazione": livello,
            "trl": trl or None,
            "trl_min": tmin,
            "trl_max": tmax,
            "trl_stimato": "stimato" in (trl or ""),
            "potenziale_industriale": pot_ind,
            "potenziale_sardegna_stelle": stelle,
            "potenziale_sardegna_commento": commento,
            "valutazione_scientifica": val,
            "priorita": prio or None,
            "inferenza": anomala,
            "pagine_pdf": r["_pages"],
            "note": note,
        }
        if anomala:
            rec["celle_originali"] = r["_cells"]
        out.append(rec)

    # ---------------- aggregati ----------------
    def count(key, items=None):
        cnt = collections.Counter()
        for rec in out:
            v = rec[key]
            if items and isinstance(v, list):
                for x in v:
                    cnt[x] += 1
            else:
                cnt["(null)" if v is None else v] += 1
        return dict(cnt.most_common())

    first_listed = collections.Counter(rec["paesi"][0] if rec["paesi"] else "ND" for rec in out)
    trl_bands = collections.Counter()
    for rec in out:
        if rec["trl_min"] is None:
            trl_bands["non quantificato (ND/NA/non tecnologico/review)"] += 1
        else:
            trl_bands[f"{rec['trl_min']}–{rec['trl_max']}"] += 1

    agg = {
        "n_record": len(out),
        "per_anno": dict(sorted(count("anno").items(), key=lambda kv: str(kv[0]))),
        "per_paese_stringa_originale": count("paese"),
        "per_paese_primo_elencato": dict(first_listed.most_common()),
        "per_paese_qualsiasi_menzione": count("paesi", items=True),
        "per_settore_applicativo": count("settore_applicativo"),
        "per_livello_innovazione": count("livello_innovazione"),
        "per_trl": dict(trl_bands.most_common()),
        "per_trl_stringa_originale": count("trl"),
        "per_potenziale_industriale": count("potenziale_industriale"),
        "per_potenziale_sardegna_stelle": dict(sorted(count("potenziale_sardegna_stelle").items(), key=lambda kv: str(kv[0]))),
        "per_valutazione_scientifica": dict(sorted(count("valutazione_scientifica").items(), key=lambda kv: str(kv[0]))),
        "per_priorita": count("priorita"),
        "n_inferenza": sum(1 for rec in out if rec["inferenza"]),
        "n_doi_null": sum(1 for rec in out if rec["doi"] is None),
        "n_record_su_due_pagine": sum(1 for rec in out if len(rec["pagine_pdf"]) > 1),
    }

    os.makedirs(OUT, exist_ok=True)
    doc = {
        "titolo": "Database bibliografico del Technology Scouting sul sughero (Allegato II) – 153 record, 2015-2026",
        "fonte": {"documento": "parte2", "capitolo": "Allegato II – Database bibliografia scientifica",
                  "pagine_pdf": list(range(142, 195)),
                  "file_grezzi": "source/parte2-filiera-sughero-sardegna/tables/p142-t0.csv … p194-t0.csv",
                  "script": "data/sughero-sardegna/parse_bibliografia.py"},
        "note": [
            "Record contati nel database: 153 (il testo a pag. 29 e 32 parla di 166 pubblicazioni, la Figura 5 e la Figura 6 di 153: vedi bibliografia-scientifica.schema.md).",
            "Legenda originale (pag. 142): 1 riferimento bibliografico; 2 DOI; 3 Paese (area di studio); 4 settore applicativo; 5 tipologia di sughero/materiale; 6 livello di innovazione; 7 TRL; 9 potenziale industriale (nella legenda numerato 8); 10 potenziale per la Sardegna (stelle + commento); 11 valutazione scientifica; 12 priorità.",
            "Le celle sono state ripulite dalle interruzioni di riga (es. 'Cosmesi/Far maceutico' -> 'Cosmesi/Farmaceutico') e dai refusi di estrazione delle legature (es. 'distretot' -> 'distretto'); i testi restano altrimenti come nell'originale, inclusi refusi d'autore e doppioni.",
            "17 record spezzati su due pagine sono stati ricomposti (campo pagine_pdf con due valori).",
            "11 record hanno una struttura anomala nella fonte (marcati 'Inferenza'): campo inferenza=true, mappatura euristica, celle originali conservate.",
            "Campi derivati (non presenti come tali nella fonte): anno, autore_primo, titolo (best effort), paesi, trl_min/trl_max/trl_stimato, potenziale_sardegna_stelle (conteggio delle ★), potenziale_sardegna_commento.",
            "DOI normalizzati (spazi rimossi, prefisso https://doi.org/ eliminato, '%2F' -> '/'); null dove la fonte riporta 'ND' o cella vuota.",
        ],
        "aggregati": agg,
        "dati": out,
    }
    json.dump(doc, open(os.path.join(OUT, "bibliografia-scientifica.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    cols = ["id", "riferimento", "anno", "anno_inferito", "autore_primo", "titolo", "doi", "paese", "paesi",
            "settore_applicativo", "materiale", "livello_innovazione", "trl", "trl_min", "trl_max", "trl_stimato",
            "potenziale_industriale", "potenziale_sardegna_stelle", "potenziale_sardegna_commento",
            "valutazione_scientifica", "priorita", "inferenza", "pagine_pdf", "note"]
    with open(os.path.join(OUT, "bibliografia-scientifica.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for rec in out:
            row = []
            for c in cols:
                v = rec[c]
                if isinstance(v, list):
                    v = " | ".join(str(x) for x in v)
                elif isinstance(v, bool):
                    v = "true" if v else "false"
                elif v is None:
                    v = ""
                row.append(v)
            w.writerow(row)
    print(json.dumps(agg, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
