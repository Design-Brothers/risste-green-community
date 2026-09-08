#!/usr/bin/env python3
"""Parsing dei 30 dossier comunali (Allegato I, pag. 52-141) e costruzione di
comuni-sughereta.json/.csv, indici-definizioni.json, sintesi-regionale.json.
Eseguire dalla radice della repo: python3 data/sughero-sardegna/parse_comuni_sughereta.py
Le righe PATCH e le tabelle FIG2/FIG3/FIG4 sono trascrizioni manuali dal PDF/figure."""
import re, json, sys, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "source/parte2-filiera-sughero-sardegna/capitoli/08-allegato1-studio-tecnico-sugherete.md"
text = SRC.read_text(encoding="utf-8")
lines = text.splitlines()

def num(s):
    """'5.801,29' -> 5801.29 ; '13,43%' -> 13.43"""
    s = s.strip().replace("ha", "").replace("%", "").replace("(", "").replace(")", "").strip()
    s = s.replace(".", "").replace(",", ".")
    return float(s)

def slugify(name):
    n = name.replace("'", "").replace("’", "")
    n = unicodedata.normalize("NFKD", n).encode("ascii", "ignore").decode()
    n = re.sub(r"[^a-zA-Z0-9]+", "-", n).strip("-").lower()
    return n

CLASSI = ["Molto bassa", "Alta", "Media", "Bassa"]
INC_CLASSI = ["Basso", "Mediobasso", "Medio", "Medioalto", "Alto"]

def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]

def is_sep(line):
    return re.fullmatch(r"\|(?:---\|)+", line.strip()) is not None

# ---- locate schede
sched_idx = [i for i, l in enumerate(lines) if l.startswith("#### Scheda comunale")]
assert len(sched_idx) == 30, len(sched_idx)

# page of each line
page_of = []
p = None
for l in lines:
    m = re.match(r"<!-- pagina (\d+) -->", l)
    if m:
        p = int(m.group(1))
    page_of.append(p)

records = []
problems = []
for k, start in enumerate(sched_idx):
    end = sched_idx[k + 1] if k + 1 < len(sched_idx) else len(lines)
    block = lines[start:end]
    # trim trailing "Riferimenti metodologici" in the last block
    for j, l in enumerate(block):
        if l.startswith("Riferimenti metodologici"):
            block = block[:j]
            break
    pages = sorted({page_of[i] for i in range(start, start + len(block)) if page_of[i]})
    rank = int(re.search(r"Scheda comunale (\d+)", block[0]).group(1))
    joined = "\n".join(block)

    # ---- comune name: line after heading up to "IVP, pericolo incendio"
    m = re.search(r"Scheda comunale \d+\s*\n+(?:#### )?(.+?)\s*\n*\s*IVP, pericolo incendio", joined)
    comune = m.group(1).strip()

    # ---- header table (first table)
    rec = {"rank": rank, "comune": comune, "slug": slugify(comune)}
    tbl_lines = [l for l in block if l.startswith("|") and not is_sep(l)]
    hdr = []
    for l in tbl_lines:
        c = cells(l)
        if c[0] == "Indicatore" and len(c) == 4:
            continue
        if len(c) == 4 and c[0] in ("Superficie sugherete", "IVP ponderato", "Indice incendio ponderato",
                                    "Medioalto + Alto", "N. complessi sughericoli", "Complesso", "maggiore"):
            hdr.append(c)
    hd = {c[0]: (c[1], c[2], c[3]) for c in hdr}
    try:
        rec["sugherete_ha"] = num(hd["Superficie sugherete"][0])
        rec["peso_pct_sughereta_sardegna"] = num(hd["Superficie sugherete"][2])
        rec["ivp"] = num(hd["IVP ponderato"][0])
        rec["classe_ivp"] = hd["IVP ponderato"][2]
        rec["ipi"] = num(hd["Indice incendio ponderato"][0])
        rec["classe_incendio"] = hd["Indice incendio ponderato"][2]
        rec["quota_medioalto_alto_pct"] = num(hd["Medioalto + Alto"][0])
        prof2 = hd["Medioalto + Alto"][2]
        if hd["Medioalto + Alto"][1] == "Profilo IVP x":  # etichetta spezzata: "incendio" e' finito nel valore
            prof2 = re.sub(r"\bincendio\b ?", "", prof2, count=1).replace("  ", " ").strip()
        rec["profilo_ivp_x_incendio"] = prof2
        rec["n_complessi"] = int(hd["N. complessi sughericoli"][0])
        rec["classe_icr"] = hd["N. complessi sughericoli"][2]
        rec["superficie_complesso_maggiore_ha"] = num(hd["Complesso"][0])
        rec["densita_frammentazione"] = num(hd["Complesso"][2].replace("n/100 ha", ""))
        rec["quota_complesso_maggiore_pct"] = num(hd["maggiore"][0])
    except Exception as e:
        problems.append((comune, "header", str(e), hd))

    # ---- sintesi esecutiva
    m = re.search(r"1\. Sintesi esecutiva(.*?)2\. Vocazionalità pedologica", joined, re.S)
    sintesi = re.sub(r"\s+", " ", m.group(1).replace("####", "")).strip()
    rec["sintesi_esecutiva"] = sintesi
    m = re.search(r"Il profilo integrato assegnato è: (.+?)\.?$", sintesi)
    rec["profilo_integrato"] = m.group(1).rstrip(".").strip()
    m = re.search(r"(?:pari a|e|Alto:) ([\d\.]+,\d+) ha \(([\d,]+)%\)", sintesi)
    rec["quota_medioalto_alto_ha"] = num(m.group(1)) if m else None
    if m and abs(num(m.group(2)) - rec["quota_medioalto_alto_pct"]) > 0.001:
        problems.append((comune, "quota_pct mismatch sintesi/header", m.group(2), rec["quota_medioalto_alto_pct"]))
    # check peso/ha in sintesi
    m = re.search(r"presenta ([\d\.]+,\d+) ha di sugherete, pari al ([\d,]+)%", sintesi)
    if m:
        if num(m.group(1)) != rec["sugherete_ha"] or num(m.group(2)) != rec["peso_pct_sughereta_sardegna"]:
            problems.append((comune, "ha/peso mismatch sintesi/header", m.group(0)))
    m = re.search(r"L'IVP ponderato è ([\d,]+), in classe (Molto bassa|Alta|Media|Bassa)", sintesi)
    if m and (num(m.group(1)) != rec["ivp"] or m.group(2) != rec["classe_ivp"]):
        problems.append((comune, "ivp mismatch sintesi/header", m.group(0)))
    m = re.search(r"La classe ICR è (Molto bassa|Alta|Media|Bassa): il complesso maggiore concentra il ([\d,]+)%", sintesi)
    if m and (m.group(1) != rec["classe_icr"] or num(m.group(2)) != rec["quota_complesso_maggiore_pct"]):
        problems.append((comune, "icr mismatch sintesi/header", m.group(0)))
    m = re.search(r"classe ponderata è (Mediobasso|Medioalto|Basso|Medio|Alto)|ricade in classe (Mediobasso|Medioalto|Basso|Medio|Alto)|complessivamente (Mediobasso|Medioalto|Basso|Medio|Alto)", sintesi)
    if m:
        cl = next(g for g in m.groups() if g)
        if cl != rec["classe_incendio"]:
            problems.append((comune, "classe incendio mismatch sintesi/header", cl, rec["classe_incendio"]))
    else:
        problems.append((comune, "classe incendio non trovata in sintesi", sintesi[:200]))

    # ---- segment helpers
    def segment(a, b):
        ia = joined.index(a)
        ib = joined.index(b, ia)
        return joined[ia:ib]

    def data_rows(seg, skip_first_cells):
        rows = []
        for l in seg.splitlines():
            if l.startswith("|") and not is_sep(l):
                c = cells(l)
                if c[0] in skip_first_cells:
                    continue
                rows.append(c)
        return rows

    # ---- IVP table
    seg = segment("2. Vocazionalità pedologica", "3. Pericolo incendio")
    ped = []
    for c in data_rows(seg, {"Unità"}):
        unita, sup, inc = c[0], c[1], c[2]
        rest = " ".join(x for x in c[3:] if x)
        # classe IVP
        classe = None
        for cl in CLASSI:
            if cl in rest:
                classe = cl; rest2 = rest.replace(cl, " "); break
        if classe is None and "Molto" in rest and "bassa" in rest:
            classe = "Molto bassa"; rest2 = rest.replace("Molto", " ").replace("bassa", " ")
        if classe is None:
            problems.append((comune, "IVP classe non trovata", c)); rest2 = rest
        m = re.search(r"(?<![\w-])([1-5])(?![\w,])", rest2)
        punteggio = int(m.group(1)) if m else None
        if punteggio is None:
            problems.append((comune, "IVP punteggio non trovato", c))
        else:
            rest2 = rest2[:m.start()] + " " + rest2[m.end():]
        uso = re.sub(r"\s+", " ", rest2).strip()
        uso = uso if uso else None
        if uso and not re.fullmatch(r"(?:[IVX]+)(?: - [IVX]+)*", uso):
            problems.append((comune, "IVP classe uso strana", uso, c))
        ped.append({"unita_pedologica": unita, "superficie_ha": num(sup), "incidenza_pct": num(inc),
                    "classe_capacita_uso": uso, "classe_ivp": classe, "punteggio_ivp": punteggio})
    rec["distribuzione_pedologica"] = ped

    # ---- incendio table
    seg = segment("3. Pericolo incendio", "4. Continuità")
    inc_rows = []
    for c in data_rows(seg, {"Classe", "Classe pericolosità", "pericolosità"}):
        if c[0] not in INC_CLASSI:
            problems.append((comune, "incendio riga strana", c)); continue
        if len(c) != 4:
            problems.append((comune, "incendio colonne", c))
        inc_rows.append({"classe": c[0], "superficie_ha": num(c[1]), "incidenza_pct": num(c[2]), "indice_classe": num(c[3])})
    PATCH = {"Telti": ("Alto", 1347.11, 47.67, 48.71, 86),
             "Chiaramonti": ("Alto", 887.25, 37.61, 49.14, 95),
             "Pozzomaggiore": ("Alto", 858.96, 46.76, 49.58, 110)}
    if comune in PATCH and not any(r["classe"] == "Alto" for r in inc_rows):
        cl, ha, pct, idx, pg = PATCH[comune]
        inc_rows.append({"classe": cl, "superficie_ha": ha, "incidenza_pct": pct, "indice_classe": idx})
        rec["_patch_incendio"] = f"Riga '{cl}' assente nell'estrazione Markdown/CSV (perdita a cavallo di pagina); reintegrata leggendo direttamente il PDF, pag. {pg}."
    rec["distribuzione_incendio"] = inc_rows

    # ---- ICR table
    seg = segment("4. Continuità", "5. Matrice integrata")
    icr = {}
    for c in data_rows(seg, {"Indicatore"}):
        icr[c[0]] = c[1:]
    try:
        n = int(icr["Numero di complessi sughericoli"][0])
        if n != rec["n_complessi"]: problems.append((comune, "n_complessi mismatch", n, rec["n_complessi"]))
        s = num(icr["Superficie"][0])
        if s != rec["superficie_complesso_maggiore_ha"]: problems.append((comune, "sup complesso mismatch", s))
        q = num(icr["Quota complesso maggiore"][0])
        if q != rec["quota_complesso_maggiore_pct"]: problems.append((comune, "quota complesso mismatch", q))
        m = re.search(r"Classe ICR (Molto bassa|Alta|Media|Bassa)", icr["Quota complesso maggiore"][1])
        if m.group(1) != rec["classe_icr"]: problems.append((comune, "classe ICR mismatch tabella", m.group(1)))
        rec["superficie_media_complesso_ha"] = num(icr["Superficie media per"][0])
        d = num(icr["Densità di frammentazione"][0].replace("complessi / 100 ha", ""))
        if d != rec["densita_frammentazione"]: problems.append((comune, "densita mismatch", d))
        m = re.search(r"Classe densità (Molto bassa|Molto alta|Alta|Media|Bassa)", icr["Densità di frammentazione"][1])
        rec["classe_densita"] = m.group(1)
        if icr["Classe ICR"][0] != rec["classe_icr"]: problems.append((comune, "classe ICR mismatch riga", icr["Classe ICR"][0]))
        rec["lettura_icr"] = icr["Classe ICR"][1]
    except Exception as e:
        problems.append((comune, "ICR", repr(e), icr))

    # ---- matrice
    seg = segment("5. Matrice integrata", "Lettura integrata")
    mat = [c for c in data_rows(seg, {"Classe IVP"})]
    if len(mat) != 1:
        problems.append((comune, "matrice righe", mat))
    else:
        c = [x for x in mat[0] if x]
        if len(c) != 4:
            problems.append((comune, "matrice celle", c))
        else:
            if c[0] != rec["classe_ivp"] or c[1] != rec["classe_incendio"] or c[2] != rec["classe_icr"]:
                problems.append((comune, "matrice classi mismatch", c))
            if c[3] != rec["profilo_integrato"]:
                problems.append((comune, "matrice profilo mismatch", c[3], rec["profilo_integrato"]))
    m = re.search(r"Il comune presenta una combinazione (.+?) x (.+?) x (.+?)\.", joined)
    rec["combinazione"] = f"{m.group(1)} x {m.group(2)} x {m.group(3)}"
    if (m.group(1), m.group(2), m.group(3)) != (rec["classe_ivp"], rec["classe_incendio"], rec["classe_icr"]):
        problems.append((comune, "combinazione mismatch", m.groups()))

    # ---- indicazioni operative
    seg = segment("Indicazioni operative preliminari", "6. Cautela metodologica")
    ind = []
    for l in seg.splitlines():
        if l.startswith("- "):
            ind.append(re.sub(r"\s+", " ", l[2:]).strip().rstrip(";.").strip())
    rec["indicazioni_operative"] = ind
    if len(ind) != 4:
        problems.append((comune, "indicazioni n", len(ind)))
    m = re.search(r"6\. Cautela metodologica\s*(?:<!-- pagina \d+ -->)?\s*(.+?)(?:\n\n|$)", joined, re.S)
    rec["cautela_metodologica"] = re.sub(r"\s+", " ", m.group(1)).strip() if m else None
    rec["pagine_fonte"] = pages

    # ---- arithmetic checks
    sp = sum(r["superficie_ha"] for r in ped)
    si = sum(r["superficie_ha"] for r in inc_rows)
    rec["_check"] = {"somma_ped_ha": round(sp, 2), "somma_inc_ha": round(si, 2),
                     "somma_ped_pct": round(sum(r["incidenza_pct"] for r in ped), 2),
                     "somma_inc_pct": round(sum(r["incidenza_pct"] for r in inc_rows), 2),
                     "ma_alto_ha": round(sum(r["superficie_ha"] for r in inc_rows if r["classe"] in ("Medioalto", "Alto")), 2),
                     "ivp_calc": round(sum(r["superficie_ha"] * r["punteggio_ivp"] for r in ped if r["punteggio_ivp"]) / sp, 3) if sp else None,
                     "ipi_calc": round(sum(r["superficie_ha"] * r["indice_classe"] for r in inc_rows) / si, 2) if si else None,
                     "media_calc": round(rec["sugherete_ha"] / rec["n_complessi"], 2),
                     "dens_calc": round(rec["n_complessi"] / rec["sugherete_ha"] * 100, 2),
                     "quota_calc": round(rec["superficie_complesso_maggiore_ha"] / rec["sugherete_ha"] * 100, 2)}
    records.append(rec)


if problems:
    for p in problems: print("PROBLEMA:", p)
    raise SystemExit("parsing incompleto")

# ============================================================ stage 2: build
import csv
from collections import Counter, OrderedDict
OUT = ROOT / "data/sughero-sardegna"
TAB = ROOT / "source/parte2-filiera-sughero-sardegna/tables"
OUT.mkdir(parents=True, exist_ok=True)

recs = records

def num(s):
    s = s.strip().replace("%", "").replace(".", "").replace(",", ".")
    return float(s)

# ------------------------------------------------------------------ quadro sinottico (pag. 50-51)
sin = {}
for f in ("p050-t1.csv", "p051-t0.csv"):
    with open(TAB / f, encoding="utf-8") as fh:
        rd = csv.reader(fh)
        for row in rd:
            if not row or not row[0].isdigit():
                continue
            sin[row[1]] = {"rank": int(row[0]), "sugherete_ha": num(row[2]), "ivp": num(row[3]), "classe_ivp": row[4],
                           "classe_incendio": row[5], "quota_medioalto_alto_pct": num(row[6]), "classe_icr": row[7]}
assert len(sin) == 30, len(sin)

# ------------------------------------------------------------------ figure (trascrizione manuale da images/fig-2,3,4)
FIG2 = {  # comune: (ivp, classe) – Figura 2, pag. 28
    "Oliena": (3.987, "Alta"), "Padru": (3.971, "Alta"), "Monti": (3.936, "Alta"), "Nuoro": (3.908, "Alta"),
    "Telti": (3.881, "Alta"), "Orune": (3.845, "Alta"), "Berchidda": (3.839, "Alta"), "Budduso'": (3.815, "Alta"),
    "Illorai": (3.798, "Alta"), "Oschiri": (3.768, "Alta"), "Bitti": (3.742, "Alta"), "Bono": (3.726, "Alta"),
    "Pattada": (3.689, "Alta"), "Bultei": (3.665, "Alta"), "Ala' Dei Sardi": (3.642, "Alta"), "Oniferi": (3.615, "Alta"),
    "Orani": (3.598, "Alta"), "Tempio Pausania": (3.582, "Alta"), "Chiaramonti": (3.549, "Alta"), "Iglesias": (3.521, "Alta"),
    "Ploaghe": (3.487, "Alta"), "Villanova Monteleone": (3.432, "Alta"), "Benetutti": (3.284, "Media"),
    "Pozzomaggiore": (3.192, "Media"), "Aidomaggiore": (3.108, "Media"), "Mores": (3.047, "Media"),
    "Abbasanta": (2.842, "Bassa"), "Ardara": (2.738, "Bassa"), "Dualchi": (2.702, "Bassa"), "Noragugume": (2.651, "Bassa"),
}
FIG3 = {  # comune: (ipi, classe) – Figura 3, pag. 29
    "Iglesias": (50.62, "Alto"), "Bono": (50.34, "Alto"), "Illorai": (49.75, "Alto"), "Oliena": (49.28, "Alto"),
    "Abbasanta": (49.16, "Alto"), "Aidomaggiore": (48.95, "Alto"), "Bultei": (46.15, "Alto"), "Berchidda": (45.64, "Alto"),
    "Calangianus": (45.42, "Alto"), "Villanova Monteleone": (44.40, "Medioalto"), "Pozzomaggiore": (44.71, "Medioalto"),
    "Padru": (43.98, "Medioalto"), "Telti": (43.87, "Medioalto"), "Benetutti": (42.48, "Medioalto"), "Ardara": (42.02, "Medioalto"),
    "Monti": (41.74, "Medioalto"), "Olbia": (41.08, "Medioalto"), "Tempio Pausania": (41.20, "Medioalto"), "Mores": (40.18, "Medioalto"),
    "Ploaghe": (39.65, "Medioalto"), "Ozieri": (39.14, "Medioalto"), "Chiaramonti": (39.02, "Medioalto"), "Orani": (38.34, "Medioalto"),
    "Pattada": (38.15, "Medioalto"), "Oschiri": (37.05, "Medioalto"), "Nuoro": (35.20, "Medioalto"), "Budduso'": (28.84, "Medio"),
    "Orune": (26.66, "Medio"), "Bitti": (27.93, "Medio"), "Ala' Dei Sardi": (19.56, "Mediobasso"),
}
FIG4 = {  # comune: (classe ICR, n complessi, % nucleo maggiore) – Figura 4, pag. 30 (Nuoro compare due volte)
    "Berchidda": ("Alta", 12, 94.74), "Budduso'": ("Alta", 13, 94.41), "Ala' Dei Sardi": ("Alta", 5, 99.52), "Telti": ("Alta", 6, 95.59),
    "Illorai": ("Alta", 7, 95.26), "Pozzomaggiore": ("Alta", 7, 94.56), "Abbasanta": ("Alta", 5, 99.35), "Iglesias": ("Alta", 9, 94.24),
    "Bitti": ("Media", 20, 74.37), "Oschiri": ("Media", 15, 76.90), "Tempio Pausania": ("Media", 13, 71.95), "Oliena": ("Media", 11, 70.98),
    "Bono": ("Media", 10, 73.62), "Bultei": ("Media", 12, 65.78), "Nuoro": ("Media", 16, 55.31),
    "Orune": ("Bassa", 9, 63.39), "Orani": ("Bassa", 8, 62.07), "Chiaramonti": ("Bassa", 8, 64.31), "Padru": ("Bassa", 8, 66.60),
    "Pattada": ("Bassa", 9, 63.52), "Monti": ("Bassa", 7, 63.77), "Ploaghe": ("Bassa", 7, 62.76),
    "Calangianus": ("Molto bassa", 25, 29.83), "Ozieri": ("Molto bassa", 24, 32.46), "Villanova Monteleone": ("Molto bassa", 27, 29.92),
    "Mores": ("Molto bassa", 22, 35.26), "Olbia": ("Molto bassa", 25, 33.84), "Benetutti": ("Molto bassa", 21, 32.58), "Aidomaggiore": ("Molto bassa", 17, 30.18),
}
FIG4_NUORO_BIS = ("Molto bassa", 33, 37.28)

NOMI_CORRENTI = {"Ala' Dei Sardi": "Alà dei Sardi", "Budduso'": "Buddusò"}  # forme usate nel testo, pag. 27-29

# ------------------------------------------------------------------ record finali
SCALARI = ["rank", "comune", "nome_corrente", "slug", "provincia", "sugherete_ha", "peso_pct_sughereta_sardegna",
           "ivp", "classe_ivp", "ipi", "classe_incendio", "quota_medioalto_alto_pct", "quota_medioalto_alto_ha",
           "n_complessi", "superficie_complesso_maggiore_ha", "quota_complesso_maggiore_pct", "superficie_media_complesso_ha",
           "densita_frammentazione", "classe_densita", "classe_icr", "profilo_ivp_x_incendio", "profilo_integrato", "pagine_fonte"]

dati = []
incoerenze = []
for r in recs:
    c = r["_check"]
    d = OrderedDict()
    d["rank"] = r["rank"]
    d["comune"] = r["comune"]
    d["nome_corrente"] = NOMI_CORRENTI.get(r["comune"], r["comune"])
    d["slug"] = r["slug"]
    d["provincia"] = None
    for k in ["sugherete_ha", "peso_pct_sughereta_sardegna", "ivp", "classe_ivp", "ipi", "classe_incendio",
              "quota_medioalto_alto_pct", "quota_medioalto_alto_ha", "n_complessi", "superficie_complesso_maggiore_ha",
              "quota_complesso_maggiore_pct", "superficie_media_complesso_ha", "densita_frammentazione", "classe_densita",
              "classe_icr", "profilo_ivp_x_incendio", "profilo_integrato", "combinazione"]:
        d[k] = r[k]
    d["indicazioni_operative"] = r["indicazioni_operative"]
    d["lettura_icr"] = r["lettura_icr"]
    d["sintesi_esecutiva"] = r["sintesi_esecutiva"]
    d["distribuzione_pedologica"] = r["distribuzione_pedologica"]
    d["distribuzione_incendio"] = r["distribuzione_incendio"]
    d["pagine_fonte"] = r["pagine_fonte"]
    # confronto sinottico
    s = sin[r["comune"]]
    diff_sin = {k: (s[k], r[k]) for k in s if s[k] != r[k]}
    # confronto figure
    f2 = FIG2.get(r["comune"]); f3 = FIG3.get(r["comune"]); f4 = FIG4.get(r["comune"])
    d["confronto_figure"] = {
        "ivp_fig2": f2[0] if f2 else None, "classe_ivp_fig2": f2[1] if f2 else None,
        "ipi_fig3": f3[0] if f3 else None, "classe_incendio_fig3": f3[1] if f3 else None,
        "classe_icr_fig4": f4[0] if f4 else None, "n_complessi_fig4": f4[1] if f4 else None,
        "quota_complesso_maggiore_fig4_pct": f4[2] if f4 else None,
        "ivp_coerente": (f2 is not None and abs(f2[0] - r["ivp"]) < 0.0005 and f2[1] == r["classe_ivp"]),
        "ipi_coerente": (f3 is not None and abs(f3[0] - r["ipi"]) < 0.005 and f3[1] == r["classe_incendio"]),
        "icr_coerente": (f4 is not None and f4[0] == r["classe_icr"] and f4[1] == r["n_complessi"] and abs(f4[2] - r["quota_complesso_maggiore_pct"]) < 0.005),
    }
    note = []
    if diff_sin:
        note.append("Differenze rispetto al quadro sinottico (pag. 50-51): " + "; ".join(f"{k} sinottico={a} dossier={b}" for k, (a, b) in diff_sin.items()))
        incoerenze.append({"comune": r["comune"], "tipo": "sinottico_vs_dossier", "dettaglio": diff_sin})
    if r.get("_patch_incendio"):
        note.append(r["_patch_incendio"])
    if abs(c["ivp_calc"] - r["ivp"]) > 0.002:
        note.append(f"IVP dichiarato {r['ivp']} non coincide con la media ponderata dei punteggi della tabella pedologica ({c['ivp_calc']}); mantenuto il valore dichiarato.")
        incoerenze.append({"comune": r["comune"], "tipo": "ivp_dichiarato_vs_ricalcolato", "dettaglio": {"dichiarato": r["ivp"], "ricalcolato": c["ivp_calc"]}})
    if abs(c["ipi_calc"] - r["ipi"]) > 0.02:
        note.append(f"IPI dichiarato {r['ipi']} vs ricalcolato {c['ipi_calc']}.")
        incoerenze.append({"comune": r["comune"], "tipo": "ipi_dichiarato_vs_ricalcolato", "dettaglio": {"dichiarato": r["ipi"], "ricalcolato": c["ipi_calc"]}})
    if abs(c["somma_ped_ha"] - r["sugherete_ha"]) > 0.05 or abs(c["somma_inc_ha"] - r["sugherete_ha"]) > 0.05:
        note.append(f"Somme tabelle: pedologica {c['somma_ped_ha']} ha, incendio {c['somma_inc_ha']} ha vs totale {r['sugherete_ha']} ha.")
    d["note"] = note
    dati.append(d)

# ------------------------------------------------------------------ comuni-sughereta.json
sum_ha = round(sum(d["sugherete_ha"] for d in dati), 2)
sum_peso = round(sum(d["peso_pct_sughereta_sardegna"] for d in dati), 2)
comuni_json = OrderedDict([
    ("titolo", "Sughereta Sardegna – i 30 comuni prioritari con IVP, pericolo incendio (IPI) e ICR"),
    ("fonte", OrderedDict([
        ("documento", "parte2"),
        ("capitolo", "Allegato I – Studio tecnico sugherete: dossier comunale integrato (quadro sinottico pag. 50-51; schede comunali 01-30 pag. 52-141)"),
        ("pagine_pdf", list(range(50, 142))),
        ("file", ["source/parte2-filiera-sughero-sardegna/capitoli/08-allegato1-studio-tecnico-sugherete.md",
                  "source/parte2-filiera-sughero-sardegna/tables/p050-t1.csv … p140-t2.csv",
                  "source/parte2-filiera-sughero-sardegna/images/fig-2-ivp-ranking-30-comuni.jpeg",
                  "source/parte2-filiera-sughero-sardegna/images/fig-3-ipi-pericolosita-incendio-30-comuni.jpeg",
                  "source/parte2-filiera-sughero-sardegna/images/fig-4-icr-continuita-risorsa-30-comuni.jpeg"]),
    ])),
    ("note", [
        "Un record per comune (30). Tutti i valori scalari provengono dal quadro sintetico in testa a ciascuna scheda comunale e sono stati verificati contro la sintesi esecutiva, le tabelle interne (pedologica, incendio, ICR, matrice) e il quadro sinottico di pag. 50-51: nessuna differenza tra sinottico e schede.",
        "`pagine_fonte` sono pagine fisiche del PDF (i marcatori `<!-- pagina N -->`); la numerazione stampata a piè di pagina è inferiore di 17 (es. PDF 86 = 'pag. 69').",
        "`comune` riporta il nome come scritto nel dossier (es. \"Ala' Dei Sardi\", \"Budduso'\"); `nome_corrente` la forma usata nel testo delle Parti 2-3 (\"Alà dei Sardi\", \"Buddusò\").",
        "`provincia` è null per tutti i comuni: il documento non la indica; nel testo (pag. 27) compaiono solo i comprensori storici (Gallura, Monte Acuto, Nuorese, Goceano, Marghine, Logudoro, Sulcis-Iglesiente) senza attribuzione per comune.",
        "`ipi` è l'\"Indice incendio ponderato\" della scheda comunale (media delle superfici per l'indice di pericolosità di ciascuna classe): coincide con l'IPI definito al par. 2.2. I valori riportati nella Figura 3 (pag. 29) differiscono per 24 comuni su 30 e sono conservati a parte in `confronto_figure`.",
        "`confronto_figure` riporta i valori letti nelle Figure 2, 3 e 4 (pag. 28-30). Le figure derivano evidentemente da una versione diversa dell'elaborazione: la Fig. 2 include Oniferi, Dualchi e Noragugume (non tra i 30 comuni) e omette Ozieri, Calangianus e Olbia; la Fig. 4 elenca Nuoro due volte (Media 16/55,31% e Molto bassa 33/37,28%) e omette Ardara. Per il sito fare fede ai valori dei dossier.",
        "`quota_medioalto_alto_ha` è tratta dalla sintesi esecutiva della scheda; coincide (±0,01 ha di arrotondamento) con la somma delle righe Medioalto+Alto di `distribuzione_incendio`.",
        "`densita_frammentazione` è espressa in complessi per 100 ha di sughereta (n. complessi / sugherete_ha × 100). `superficie_media_complesso_ha` = sugherete_ha / n_complessi.",
        "Tre tabelle incendio (Telti, Chiaramonti, Pozzomaggiore) avevano perso la riga 'Alto' nell'estrazione automatica a cavallo di pagina: la riga è stata reintegrata leggendo il PDF originale (pag. 86, 95, 110); vedi `note` del record.",
        "Bultei: l'IVP dichiarato (3,395) non coincide con la media ponderata ricalcolata dai punteggi della tabella pedologica (3,448); per gli altri 29 comuni il ricalcolo coincide al millesimo. Mantenuto il valore dichiarato.",
        "La 'Cautela metodologica' (punto 6) è identica per tutte le schede: \"La scheda è una sintesi comunale. Per individuare puntualmente le porzioni di sughereta più strategiche e vulnerabili è opportuno procedere con overlay GIS diretto tra unità pedologiche riclassificate, classi di pericolosità incendio e complessi sughericoli.\"",
        "Somma delle superfici dei 30 comuni: " + f"{sum_ha:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") + f" ha (testo pag. 27: 83.790,90 ha); somma dei pesi: {sum_peso}%.".replace("99.98", "99,98"),
    ]),
    ("dati", dati),
])
(OUT / "comuni-sughereta.json").write_text(json.dumps(comuni_json, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# ------------------------------------------------------------------ CSV (solo scalari)
csv_fields = [f for f in SCALARI if f != "pagine_fonte"] + ["combinazione", "pagine_fonte"]
with open(OUT / "comuni-sughereta.csv", "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=csv_fields)
    w.writeheader()
    for d in dati:
        row = {k: d[k] for k in csv_fields}
        row["pagine_fonte"] = "-".join(str(p) for p in (d["pagine_fonte"][0], d["pagine_fonte"][-1]))
        row["provincia"] = ""
        w.writerow(row)

# ------------------------------------------------------------------ indici-definizioni.json
def rng(key, cls):
    g = {}
    for d in dati:
        g.setdefault(d[cls], []).append(d[key])
    return {k: {"min": min(v), "max": max(v), "n_comuni": len(v)} for k, v in g.items()}

profili2 = sorted({(d["classe_ivp"], d["classe_incendio"], d["profilo_ivp_x_incendio"]) for d in dati})
profili3 = sorted({(d["classe_ivp"], d["classe_incendio"], d["classe_icr"], d["profilo_integrato"]) for d in dati})
letture_ivp = {
    "Alta": "La risorsa mostra una buona coerenza pedologica complessiva con la sughereta, pur con limitazioni locali legate alle unità pedologiche specifiche.",
    "Media": "La risorsa è pedologicamente compatibile, ma presenta limitazioni che richiedono attenzione nella gestione e nella selezione di aree pilota.",
    "Bassa": "La vocazionalità pedologica appare più limitante e suggerisce un approccio selettivo agli investimenti e agli interventi di valorizzazione.",
}
letture_icr = {d["classe_icr"]: d["lettura_icr"].split(". ", 1)[1] for d in dati}
letture_inc = {
    "Mediobasso": "Il profilo incendio ponderato ricade in classe Mediobasso. La quota Medioalto+Alto […] indica criticità localizzate più che diffuse.",
    "Medio": "Il profilo incendio ponderato ricade in classe Medio; la quota Medioalto+Alto indica criticità localizzate più che diffuse (Bitti, Buddusò) oppure, se non trascurabile, richiede una selezione puntuale delle aree più esposte (Orune).",
    "Medioalto": "Il profilo incendio evidenzia una criticità elevata: la classe ponderata è Medioalto e la maggior parte delle superfici ricade nelle classi Medioalto e Alto. Queste superfici richiedono priorità nella pianificazione antincendio e nella gestione attiva.",
    "Alto": "Il profilo incendio evidenzia una criticità elevata: la classe ponderata è Alto […]. Queste superfici richiedono priorità nella pianificazione antincendio e nella gestione attiva.",
}
indice_classi_inc = {}
for d in dati:
    for r in d["distribuzione_incendio"]:
        indice_classi_inc.setdefault(r["classe"], []).append(r["indice_classe"])
indice_classi_inc = {k: {"min": min(v), "max": max(v), "n_occorrenze": len(v)} for k, v in indice_classi_inc.items()}
punteggi = {}
for d in dati:
    for r in d["distribuzione_pedologica"]:
        punteggi.setdefault(r["classe_ivp"], set()).add(r["punteggio_ivp"])
punteggi = {k: sorted(v) for k, v in punteggi.items()}
unita = {}
for d in dati:
    for r in d["distribuzione_pedologica"]:
        u = unita.setdefault(r["unita_pedologica"], {"classe_ivp": set(), "punteggio_ivp": set(), "classe_capacita_uso": set(), "n_comuni": 0, "superficie_ha": 0.0})
        u["classe_ivp"].add(r["classe_ivp"]); u["punteggio_ivp"].add(r["punteggio_ivp"]); u["n_comuni"] += 1
        u["superficie_ha"] = round(u["superficie_ha"] + r["superficie_ha"], 2)
        if r["classe_capacita_uso"]: u["classe_capacita_uso"].add(r["classe_capacita_uso"])
unita_list = [OrderedDict([("unita_pedologica", k), ("classe_ivp", sorted(v["classe_ivp"])), ("punteggio_ivp", sorted(v["punteggio_ivp"])),
                           ("classe_capacita_uso", sorted(v["classe_capacita_uso"])), ("n_comuni", v["n_comuni"]), ("superficie_ha_30_comuni", v["superficie_ha"])])
              for k, v in sorted(unita.items(), key=lambda kv: -kv[1]["superficie_ha"])]

indici = OrderedDict([
    ("titolo", "Definizione degli indici territoriali IVP, IPI e ICR e legenda dei profili integrati"),
    ("fonte", OrderedDict([
        ("documento", "parte2"),
        ("capitolo", "Par. 2.2 Analisi territoriale (pag. 19-21); par. 3.2 (pag. 27-29); par. 4.1-4.2 (pag. 35-37); Allegato I nota metodologica (pag. 50) e schede comunali (pag. 52-141); Figure 2-4 (pag. 28-30)"),
        ("pagine_pdf", [19, 20, 21, 27, 28, 29, 30, 35, 36, 37, 50, 51, 141]),
    ])),
    ("note", [
        "Il documento NON esplicita le soglie numeriche delle classi né nel par. 2.2 né nell'Allegato I. Le uniche soglie scritte sono nelle legende delle Figure 2 e 4, ma non sono coerenti con la classificazione adottata nei dossier (es. Bitti IVP 3,317 è 'Alta' nel dossier, mentre la legenda di Fig. 2 richiede IVP ≥ 3,50; Bitti quota nucleo 74,37% è 'Media' nel dossier, mentre la legenda di Fig. 4 assegna 'Alta' a ICR ≥ 70). Per ogni indice riportiamo quindi: (a) le soglie di legenda delle figure, con avvertenza; (b) gli intervalli empirici min-max osservati nei 30 dossier per ciascuna classe (`intervalli_osservati`), che sono ciò su cui il sito può fare affidamento.",
        "Il pericolo incendio non ha un nome esplicito nell'Allegato I ('Indice incendio ponderato', 'Pericolo incendio'); nel corpo del rapporto (par. 2.2, 3.2.2, 4.1.2) è l'Indice di Pericolosità da Incendio (IPI). La classe comunale nei dossier si chiama 'Classe incendio' e le classi elementari della carta regionale sono Basso, Mediobasso, Medio, Medioalto, Alto.",
        "Profili integrati: il documento non fornisce una tabella di legenda; le combinazioni sotto riportate sono ricavate dalle 30 matrici integrate (17 combinazioni distinte osservate → 7 profili). Le combinazioni non osservate non hanno profilo assegnato.",
        "`profili_ivp_x_incendio` è il profilo a due fattori riportato nel quadro sintetico di ogni scheda ('Profilo IVP x incendio'), distinto dal profilo integrato a tre fattori.",
        "Le unità pedologiche (B2, C2, …) sono quelle della Carta dei suoli della Sardegna (Aru, Baldaccini, Vacca) riclassificate dallo studio con un punteggio 1-4 (Molto bassa=1, Bassa=2, Media=3, Alta=4); nei 30 dossier non compare alcun punteggio 5, benché la Fig. 2 indichi una scala 'da 1 a 5'.",
    ]),
    ("dati", OrderedDict([
        ("indici", [
            OrderedDict([
                ("sigla", "IVP"),
                ("nome", "Indice di Vocazionalità Pedologica"),
                ("domanda", "Su quali suoli insiste la sughereta?"),
                ("definizione", "Esprime il grado di idoneità dei suoli alla presenza e allo sviluppo della quercia da sughero. Costruito mediante la riclassificazione delle unità pedologiche in funzione delle principali caratteristiche fisiche e morfologiche dei suoli, successivamente sintetizzate in un valore ponderato riferito a ciascun territorio comunale (par. 2.2). Nel par. 4.1.1 è interpretato come misura della 'resilienza potenziale del sito'."),
                ("metodo", "Ogni unità pedologica presente sotto sughereta riceve una classe (Molto bassa/Bassa/Media/Alta) e un punteggio (1-4); l'IVP comunale è la media dei punteggi ponderata per la superficie a sughera di ciascuna unità. Il ricalcolo dalle tabelle dei dossier riproduce il valore dichiarato al millesimo per 29 comuni su 30 (eccezione: Bultei)."),
                ("scala", "indice da 1 a 4 nei dossier (la Fig. 2 indica 'da 1 a 5')"),
                ("classi", ["Alta", "Media", "Bassa", "Molto bassa"]),
                ("soglie_dichiarate", {"fonte": "Legenda Figura 2, pag. 28 (non coerente con i dossier, vedi note)", "Alta": "IVP ≥ 3,50", "Media": "2,50 ≤ IVP < 3,50", "Bassa": "IVP < 2,50"}),
                ("intervalli_osservati", rng("ivp", "classe_ivp")),
                ("punteggi_unita", punteggi),
                ("lettura_classi", letture_ivp),
                ("output", "indice ponderato e classe Alta/Media/Bassa/Molto bassa"),
                ("pagine_fonte", [20, 27, 28, 35, 36, 50]),
            ]),
            OrderedDict([
                ("sigla", "IPI"),
                ("nome", "Indice di Pericolosità da Incendio"),
                ("domanda", "Quanto è esposta al fuoco la risorsa?"),
                ("definizione", "Elaborato mediante l'intersezione tra le superfici a sughereta e la cartografia regionale del pericolo di incendio (Piano regionale di previsione, prevenzione e lotta attiva contro gli incendi boschivi 2023-2025, Allegato 5), consente di stimare il livello di esposizione della risorsa forestale e di individuare i territori maggiormente vulnerabili (par. 2.2). Nel par. 4.1.2 è il 'principale fattore di pressione'."),
                ("metodo", "Le sugherete comunali sono ripartite nelle cinque classi di pericolosità della carta regionale (Basso, Mediobasso, Medio, Medioalto, Alto), ciascuna con un indice di pericolosità di classe; l'indice incendio ponderato comunale è la media di tali indici pesata per le superfici. Il ricalcolo dalle tabelle riproduce il valore dichiarato per tutti i 30 comuni. Accanto all'indice, ogni scheda riporta la quota di superficie nelle classi Medioalto+Alto."),
                ("scala", "indice 0-100 (valori di classe osservati da 11,24 a 50,34; valori comunali da 25,02 a 48,02)"),
                ("classi", ["Basso", "Mediobasso", "Medio", "Medioalto", "Alto"]),
                ("soglie_dichiarate", {"fonte": "nessuna soglia esplicitata nel documento", "nota": "Dalla distribuzione degli indici di classe nei dossier, le classi elementari cadono in fasce di circa 10 punti (Basso ≈ 11-15, Mediobasso ≈ 22-25, Medio ≈ 29-32, Medioalto ≈ 38-40, Alto ≈ 48-50)."}),
                ("intervalli_osservati", {"indice_ponderato_comunale": rng("ipi", "classe_incendio"), "quota_medioalto_alto_pct": rng("quota_medioalto_alto_pct", "classe_incendio"), "indice_di_classe_nelle_tabelle": indice_classi_inc}),
                ("lettura_classi", letture_inc),
                ("output", "indice ponderato, classe e quota Medioalto+Alto"),
                ("pagine_fonte", [20, 28, 29, 36, 50]),
            ]),
            OrderedDict([
                ("sigla", "ICR"),
                ("nome", "Indice di Continuità della Risorsa"),
                ("domanda", "Quanto è continua o frammentata la sughereta?"),
                ("definizione", "Descrive il grado di continuità spaziale delle superfici a sughereta attraverso la valutazione della frammentazione del paesaggio forestale e della presenza di nuclei maggiormente accorpati (par. 2.2). Nel par. 4.1.3 la continuità è rilevante sia ecologicamente sia per la possibilità di pianificare interventi coordinati."),
                ("metodo", "Per ogni comune si individuano i complessi (patch) sughericoli e si calcolano: numero di complessi, superficie e quota del complesso maggiore, superficie media per complesso (= sugherete_ha / n_complessi), densità di frammentazione (= n_complessi / 100 ha). La classe ICR dei dossier è associata alla quota del complesso maggiore; la densità ha una propria classe (Bassa/Media/Alta/Molto alta)."),
                ("scala", "Fig. 4: 'da 0 a 100'; nei dossier l'indicatore numerico è la quota % del complesso maggiore"),
                ("classi", ["Alta", "Media", "Bassa", "Molto bassa"]),
                ("soglie_dichiarate", {"fonte": "Legenda Figura 4, pag. 30 (non coerente con i dossier, vedi note)", "Alta": "ICR ≥ 70", "Media": "50 ≤ ICR < 70", "Bassa": "30 ≤ ICR < 50", "Molto bassa": "ICR < 30"}),
                ("intervalli_osservati", {"quota_complesso_maggiore_pct": rng("quota_complesso_maggiore_pct", "classe_icr"), "n_complessi": rng("n_complessi", "classe_icr"), "densita_frammentazione_per_classe_densita": rng("densita_frammentazione", "classe_densita")}),
                ("lettura_classi", letture_icr),
                ("output", "numero complessi, nucleo maggiore, densità e classe ICR"),
                ("pagine_fonte", [20, 28, 29, 30, 36, 50]),
            ]),
        ]),
        ("profili_ivp_x_incendio", [OrderedDict([("classe_ivp", a), ("classe_incendio", b), ("profilo", c),
                                                ("comuni", [d["slug"] for d in dati if (d["classe_ivp"], d["classe_incendio"]) == (a, b)])]) for a, b, c in profili2]),
        ("profili_integrati", [OrderedDict([("classe_ivp", a), ("classe_incendio", b), ("classe_icr", c), ("profilo_integrato", p),
                                            ("comuni", [d["slug"] for d in dati if (d["classe_ivp"], d["classe_incendio"], d["classe_icr"]) == (a, b, c)])]) for a, b, c, p in profili3]),
        ("profili_integrati_distinti", [OrderedDict([("profilo_integrato", p), ("n_comuni", n),
                                                     ("comuni", [d["slug"] for d in dati if d["profilo_integrato"] == p])])
                                        for p, n in Counter(d["profilo_integrato"] for d in dati).most_common()]),
        ("indicazioni_operative_ricorrenti", [OrderedDict([("testo", t), ("n_comuni", n)]) for t, n in Counter(i for d in dati for i in d["indicazioni_operative"]).most_common()]),
        ("unita_pedologiche", unita_list),
    ])),
])
(OUT / "indici-definizioni.json").write_text(json.dumps(indici, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# ------------------------------------------------------------------ sintesi-regionale.json
def conta(key):
    c = Counter(d[key] for d in dati)
    return [OrderedDict([("classe", k), ("n_comuni", v), ("comuni", [d["slug"] for d in dati if d[key] == k])]) for k, v in c.most_common()]

top5 = [OrderedDict([("rank", d["rank"]), ("comune", d["comune"]), ("slug", d["slug"]), ("sugherete_ha", d["sugherete_ha"]), ("peso_pct_sughereta_sardegna", d["peso_pct_sughereta_sardegna"])]) for d in dati[:5]]
by = lambda key, rev: sorted(dati, key=lambda d: d[key], reverse=rev)
fig_diff = {
    "fig2_ivp_comuni_non_coerenti": [d["slug"] for d in dati if not d["confronto_figure"]["ivp_coerente"]],
    "fig3_ipi_comuni_non_coerenti": [d["slug"] for d in dati if not d["confronto_figure"]["ipi_coerente"]],
    "fig4_icr_comuni_non_coerenti": [d["slug"] for d in dati if not d["confronto_figure"]["icr_coerente"]],
    "fig2_comuni_estranei_ai_30": ["Oniferi", "Dualchi", "Noragugume"],
    "fig2_comuni_dei_30_assenti": ["ozieri", "calangianus", "olbia"],
    "fig4_comuni_dei_30_assenti": ["ardara"],
    "fig4_duplicati": {"nuoro": [{"classe_icr": "Media", "n_complessi": 16, "quota_pct": 55.31}, {"classe_icr": "Molto bassa", "n_complessi": 33, "quota_pct": 37.28}]},
}
ivp_cnt = Counter(d["classe_ivp"] for d in dati); icr_cnt = Counter(d["classe_icr"] for d in dati)
sintesi = OrderedDict([
    ("titolo", "Sughereta Sardegna – sintesi regionale dei 30 comuni prioritari"),
    ("fonte", OrderedDict([
        ("documento", "parte2"),
        ("capitolo", "Par. 2.2 (pag. 20), par. 3.1-3.2 (pag. 27-29), Allegato I (pag. 50-141); conteggi ricalcolati da comuni-sughereta.json"),
        ("pagine_pdf", [20, 27, 28, 29, 50, 51]),
    ])),
    ("note", [
        "I conteggi per classe sono calcolati dal dataset dei 30 dossier e confrontati con quanto scrive il testo (par. 3.2). Differenze: IVP – testo '22 Alta, 4 Media, 4 Bassa' vs dossier 21/4/5 (il testo stesso elenca cinque comuni a vocazionalità inferiore: Abbasanta, Pozzomaggiore, Aidomaggiore, Mores e Ardara, che nei dossier sono tutti 'Bassa'); ICR – testo '8 comuni a continuità elevata' (Berchidda, Buddusò, Alà dei Sardi, Telti, Illorai, Pozzomaggiore, Abbasanta, Iglesias) vs dossier 9 (in più Aidomaggiore, ICR Alta con quota del complesso maggiore 93,42%). Per il pericolo incendio il testo non dà conteggi.",
        "Il totale 83.790,90 ha (pag. 27) e 'circa 83.800 ettari' (pag. 20) si riferiscono ai 30 comuni; la somma delle 30 superfici dei dossier è riportata in `totali.somma_sugherete_30_comuni_ha`. La somma dei pesi percentuali dei 30 comuni è ≈100%: la 'Sughereta Sardegna' su cui è calcolato il peso coincide quindi con l'insieme dei 30 comuni (non è indicato un totale regionale più ampio).",
        "Il documento non usa una graduatoria esplicita di 'profilo più favorevole/critico': `profili_estremi` riprende le parole dei dossier (profilo integrato e indicazioni operative) e del par. 3.2 (comuni più/meno esposti; continuità più/meno favorevole).",
        "`confronto_figure` elenca le discrepanze tra le Figure 2-4 (pag. 28-30) e i dossier: le figure vanno considerate non allineate con l'Allegato I.",
    ]),
    ("dati", OrderedDict([
        ("totali", OrderedDict([
            ("sugherete_30_comuni_ha_testo", 83790.90),
            ("sugherete_30_comuni_ha_testo_arrotondato", 83800),
            ("somma_sugherete_30_comuni_ha", sum_ha),
            ("somma_peso_pct", sum_peso),
            ("n_comuni", len(dati)),
            ("n_complessi_totali", sum(d["n_complessi"] for d in dati)),
            ("superficie_medioalto_alto_ha", round(sum(d["quota_medioalto_alto_ha"] for d in dati), 2)),
            ("quota_medioalto_alto_pct_sul_totale", round(sum(d["quota_medioalto_alto_ha"] for d in dati) / sum_ha * 100, 2)),
            ("ivp_medio_ponderato_ha", round(sum(d["ivp"] * d["sugherete_ha"] for d in dati) / sum_ha, 3)),
            ("ipi_medio_ponderato_ha", round(sum(d["ipi"] * d["sugherete_ha"] for d in dati) / sum_ha, 2)),
        ])),
        ("superficie_per_classe_incendio_ha", OrderedDict((k, round(v, 2)) for k, v in sorted(
            Counter({}).items()))),
        ("conteggi_classe_ivp", OrderedDict([("dataset", conta("classe_ivp")), ("testo_pag_27", {"Alta": 22, "Media": 4, "Bassa": 4}),
                                             ("differenze", f"dataset Alta={ivp_cnt['Alta']}, Media={ivp_cnt['Media']}, Bassa={ivp_cnt['Bassa']} vs testo 22/4/4")])),
        ("conteggi_classe_incendio", OrderedDict([("dataset", conta("classe_incendio")), ("testo_pag_28", None),
                                                  ("differenze", "il testo non riporta conteggi per classe; cita gli 8 comuni con oltre il 90% in Medioalto+Alto (Iglesias, Bono, Aidomaggiore, Abbasanta, Oliena, Illorai, Berchidda, Calangianus) e i 3 meno esposti (Alà dei Sardi, Bitti, Buddusò): coerenti con i dossier, nei quali però i comuni con oltre il 90% in Medioalto+Alto sono " + str(sum(1 for d in dati if d["quota_medioalto_alto_pct"] > 90)))])),
        ("conteggi_classe_icr", OrderedDict([("dataset", conta("classe_icr")), ("testo_pag_28_29", {"Alta": 8}),
                                             ("differenze", f"dataset Alta={icr_cnt['Alta']} vs testo 8 (il testo non elenca Aidomaggiore); i 7 comuni 'a frammentazione decisamente più accentuata' del testo coincidono con i 7 'Molto bassa' dei dossier")])),
        ("conteggi_classe_densita", conta("classe_densita")),
        ("conteggi_profilo_integrato", conta("profilo_integrato")),
        ("top5_estensione", top5),
        ("estremi", OrderedDict([
            ("ivp_max", [{"slug": d["slug"], "ivp": d["ivp"]} for d in by("ivp", True)[:5]]),
            ("ivp_min", [{"slug": d["slug"], "ivp": d["ivp"]} for d in by("ivp", False)[:5]]),
            ("quota_medioalto_alto_max", [{"slug": d["slug"], "quota_medioalto_alto_pct": d["quota_medioalto_alto_pct"]} for d in by("quota_medioalto_alto_pct", True)[:8]]),
            ("quota_medioalto_alto_min", [{"slug": d["slug"], "quota_medioalto_alto_pct": d["quota_medioalto_alto_pct"]} for d in by("quota_medioalto_alto_pct", False)[:3]]),
            ("quota_complesso_maggiore_max", [{"slug": d["slug"], "quota_complesso_maggiore_pct": d["quota_complesso_maggiore_pct"]} for d in by("quota_complesso_maggiore_pct", True)[:5]]),
            ("quota_complesso_maggiore_min", [{"slug": d["slug"], "quota_complesso_maggiore_pct": d["quota_complesso_maggiore_pct"]} for d in by("quota_complesso_maggiore_pct", False)[:5]]),
            ("n_complessi_max", [{"slug": d["slug"], "n_complessi": d["n_complessi"]} for d in by("n_complessi", True)[:5]]),
        ])),
        ("profili_estremi", OrderedDict([
            ("piu_favorevoli", OrderedDict([
                ("criterio", "IVP Alta con pericolo incendio Medio/Mediobasso e ICR Alta o Media: profilo integrato 'Area vocata e relativamente governabile' (unico profilo senza richiamo a criticità)"),
                ("comuni", [d["slug"] for d in dati if d["profilo_integrato"] == "Area vocata e relativamente governabile"]),
                ("riferimento_testo", "par. 3.2.2: Alà dei Sardi (3,58%), Bitti (13,43%) e Buddusò (16,94%) mostrano un'incidenza decisamente inferiore delle aree ad elevato rischio incendio"),
            ])),
            ("priorita_alta_governabili", OrderedDict([
                ("criterio", "profilo 'Priorità alta: risorsa vocata, esposta e territorialmente governabile' (IVP Alta, incendio Medioalto/Alto, ICR Alta o Media)"),
                ("comuni", [d["slug"] for d in dati if d["profilo_integrato"].startswith("Priorità alta:")]),
            ])),
            ("piu_critici", OrderedDict([
                ("criterio", "profili che combinano esposizione al fuoco con vocazionalità bassa/media o forte frammentazione: 'Area critica/marginale esposta: priorità selettiva' (IVP Bassa), 'Risorsa compatibile ma fragile e frammentata' (IVP Media, ICR Bassa/Molto bassa), 'Priorità alta ma gestione complessa: risorsa vocata, esposta e frammentata' (IVP Alta, ICR Bassa/Molto bassa)"),
                ("area_critica_marginale", [d["slug"] for d in dati if d["profilo_integrato"].startswith("Area critica")]),
                ("compatibile_fragile_frammentata", [d["slug"] for d in dati if d["profilo_integrato"] == "Risorsa compatibile ma fragile e frammentata"]),
                ("vocata_esposta_frammentata", [d["slug"] for d in dati if d["profilo_integrato"].startswith("Priorità alta ma")]),
                ("riferimento_testo", "par. 3.2.2: oltre il 90% in Medioalto+Alto per Iglesias, Bono, Aidomaggiore, Abbasanta, Oliena, Illorai, Berchidda, Calangianus; par. 3.2.3: frammentazione più accentuata per Nuoro, Calangianus, Ozieri, Villanova Monteleone, Mores, Olbia e Benetutti"),
            ])),
        ])),
        ("comprensori_citati", ["Gallura", "Monte Acuto", "Nuorese", "Goceano", "Marghine", "Logudoro", "Sulcis-Iglesiente"]),
        ("incoerenze_fonte", OrderedDict([
            ("sinottico_vs_dossier", [i for i in incoerenze if i["tipo"] == "sinottico_vs_dossier"] or "nessuna"),
            ("ricalcoli", [i for i in incoerenze if i["tipo"] != "sinottico_vs_dossier"]),
            ("testo_vs_dossier", [
                "Par. 3.2.1: '22 Alta, 4 Media, 4 Bassa' vs dossier 21/4/5.",
                "Par. 3.2.3: '8 comuni a continuità elevata' vs dossier 9 (Aidomaggiore non citato).",
                "Par. 3.2.1 cita 'Tabella 1' e 'Figura 2' per l'IVP, e la didascalia a pag. 28 è numerata 'Figura 6': refusi di numerazione.",
                "Par. 3.2 ripete integralmente il primo capoverso del par. 3.1.",
            ]),
            ("confronto_figure", fig_diff),
            ("estrazione", [
                "Righe 'Alto' delle tabelle incendio perse a cavallo di pagina per Telti (pag. 86), Chiaramonti (pag. 95), Pozzomaggiore (pag. 110): reintegrate dal PDF.",
                "Nelle tabelle pedologiche la classe 'Molto bassa' è spesso spezzata su due celle ('Molto' | '1 bassa'): ricomposta dal parser.",
            ]),
        ])),
    ])),
])
# superficie per classe incendio
sup_cls = Counter()
for d in dati:
    for r in d["distribuzione_incendio"]:
        sup_cls[r["classe"]] += r["superficie_ha"]
order = ["Basso", "Mediobasso", "Medio", "Medioalto", "Alto"]
sintesi["dati"]["superficie_per_classe_incendio_ha"] = OrderedDict((k, round(sup_cls[k], 2)) for k in order)
sintesi["dati"]["superficie_per_classe_incendio_pct"] = OrderedDict((k, round(sup_cls[k] / sum_ha * 100, 2)) for k in order)
sup_ivp = Counter()
for d in dati:
    for r in d["distribuzione_pedologica"]:
        sup_ivp[r["classe_ivp"]] += r["superficie_ha"]
sintesi["dati"]["superficie_per_classe_ivp_unita_ha"] = OrderedDict((k, round(sup_ivp[k], 2)) for k in ["Alta", "Media", "Bassa", "Molto bassa"])
(OUT / "sintesi-regionale.json").write_text(json.dumps(sintesi, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print("OK", sum_ha, sum_peso)
print("IVP", dict(ivp_cnt), "ICR", dict(icr_cnt), "INC", dict(Counter(d["classe_incendio"] for d in dati)))
print("incoerenze:", json.dumps(incoerenze, ensure_ascii=False))
print("fig diff:", json.dumps(fig_diff, ensure_ascii=False, indent=1))
print("Aidomaggiore quota:", [d["quota_complesso_maggiore_pct"] for d in dati if d["slug"] == "aidomaggiore"])
print(">90%:", [d["slug"] for d in dati if d["quota_medioalto_alto_pct"] > 90])
