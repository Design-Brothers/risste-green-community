#!/usr/bin/env python3
"""Structured extraction of the RISSTE PDF reports into Markdown + CSV + images."""
import fitz, pdfplumber, re, os, csv, sys, json, collections, hashlib

PARTS = {
    "Parte1": ("source/parte1-green-community-alta-gallura", "Documenti/RISSTE_CUP_E77G24000450002_Parte1_signed.pdf"),
    "Parte2": ("source/parte2-filiera-sughero-sardegna", "Documenti/RISSTE_CUP_E77G24000450002_Parte2_signed.pdf"),
}

FOOTER_PATTERNS = [
    re.compile(r'^_{8,}\s*$'),
    re.compile(r'^R\.I\.S\.S\.T\.E\. – Centro Studi'),
    re.compile(r'^IT 91065830902'),
    re.compile(r'^pag\.\s*\S+\s*$'),
    re.compile(r'^(risste\.life@gmail\.com \| )?centrostudirisste@pec\.it\s*$'),
]
BULLET_RE = re.compile(r'^([•\-–▪◦✓●○■]|[a-z]\)|\(?[ivx]+\)|\d{1,2}\))\s+')
CAPTION_RE = re.compile(r'^(Tabella|Figura|Fig\.|Tab\.)\s*\d+[a-z]?[\.:]?\s', re.I)
TOC_RE = re.compile(r'\.{6,}\s*\d+\s*$')

def clean(t):
    t = t.replace(' ', ' ')
    t = re.sub(r'[ \t]+', ' ', t).strip()
    return t

def is_footer(t):
    return any(p.search(t) for p in FOOTER_PATTERNS)

def heading_level(text, bold_ratio, caps_ratio):
    t = text.strip()
    if len(t) > 140: return 0
    if CAPTION_RE.match(t): return 0
    if re.match(r'^(PRIMA|SECONDA|TERZA|QUARTA|QUINTA|SESTA) PARTE', t): return 1
    if re.match(r'^(ALLEGATO\s+[IVX]+|ALLEGATI|BIBLIOGRAFIA|SOMMARIO|LISTA ABBREVIAZIONI|LISTA UNITA|PREMESSA|MATERIALI E METODI|RISULTATI|CONSIDERAZIONI FINALI)\b', t) and caps_ratio > 0.8: return 1
    numbered = re.match(r'^(\d+(?:\.\d+)*)\.?\s+\S', t)
    roman_up = re.match(r'^[IVX]+\.\s+\S', t)
    roman_lo = re.match(r'^[ivx]+\.\s+\S', t)
    strong = bold_ratio > 0.5 or caps_ratio > 0.7
    if roman_up and strong: return 2
    if roman_lo and strong: return 3
    if numbered and strong:
        depth = numbered.group(1).count('.') + 1
        return min(1 + depth, 5)
    if caps_ratio > 0.75 and len(t) >= 6 and not t.endswith(('.', ',', ';')) and sum(c.isalpha() for c in t) >= 6: return 3
    if bold_ratio > 0.85 and len(t) < 110 and not t.endswith(('.', ',', ';', ':')) and len(t.split()) >= 2: return 4
    return 0

def md_table(rows):
    rows = [[clean((c or '').replace('\n', ' ')) for c in r] for r in rows]
    # drop fully empty columns
    ncol = max(len(r) for r in rows)
    rows = [r + [''] * (ncol - len(r)) for r in rows]
    keep = [j for j in range(ncol) if any(r[j] for r in rows)]
    rows = [[r[j] for j in keep] for r in rows]
    rows = [r for r in rows if any(r)]
    if not rows: return '', rows
    # compact sparse tables (phantom columns from shading): keep non-empty cells per row
    ncol = len(rows[0])
    empties = sum(1 for r in rows for c in r if not c)
    if ncol >= 4 and empties / (ncol * len(rows)) > 0.3:
        counts = collections.Counter(sum(1 for c in r if c) for r in rows)
        modal = max(counts, key=lambda k: (counts[k], k))
        if modal >= 2 and counts[modal] >= max(2, len(rows) * 0.4):
            new_rows = []
            for r in rows:
                cells = [c for c in r if c]
                if len(cells) == modal:
                    new_rows.append(cells)
                elif len(cells) > modal:
                    new_rows.append(cells[:modal - 1] + [' '.join(cells[modal - 1:])])
                elif new_rows and len(cells) <= 2:
                    # continuation fragment (e.g. wrapped 'Molto / bassa'): append to last cell
                    new_rows[-1][-1] = (new_rows[-1][-1] + ' ' + ' '.join(cells)).strip()
                else:
                    new_rows.append(cells + [''] * (modal - len(cells)))
            rows = new_rows
    ncol = len(rows[0])
    out = ['| ' + ' | '.join(c.replace('|', '/') for c in rows[0]) + ' |', '|' + '---|' * ncol]
    for r in rows[1:]:
        out.append('| ' + ' | '.join(c.replace('|', '/') for c in r) + ' |')
    return '\n'.join(out), rows

def process(part, outdir, pdfpath):
    os.makedirs(f"{outdir}/tables", exist_ok=True)
    os.makedirs(f"{outdir}/images", exist_ok=True)
    doc = fitz.open(pdfpath)
    plumb = pdfplumber.open(pdfpath)

    # --- running headers: lines in top region repeated on >=4 pages
    top_lines = collections.Counter()
    page_lines = []
    for pno, page in enumerate(doc):
        d = page.get_text("dict")
        lines = []
        for b in d["blocks"]:
            if b["type"] != 0: continue
            for l in b["lines"]:
                text = clean("".join(s["text"] for s in l["spans"]))
                if not text: continue
                nb = sum(len(s["text"]) for s in l["spans"] if "Bold" in s["font"])
                nt = sum(len(s["text"]) for s in l["spans"]) or 1
                letters = [c for c in text if c.isalpha()]
                caps = sum(c.isupper() for c in letters) / len(letters) if letters else 0
                x0, y0, x1, y1 = l["bbox"]
                lines.append(dict(text=text, bold=nb / nt, caps=caps, x0=x0, y0=y0, x1=x1, y1=y1, size=l["spans"][0]["size"]))
        page_lines.append(lines)
        first = [l for l in lines if not is_footer(l["text"]) and l["y0"] < 140]
        if first: top_lines[first[0]["text"]] += 1
    running = set()
    print(part, "running headers:", running)

    md_pages = []
    table_manifest = []
    headings = []
    seen_running = set()
    for pno, page in enumerate(doc):
        pnum = pno + 1
        lines = page_lines[pno]
        # tables
        tables = []
        try:
            found = page.find_tables(strategy="lines").tables
        except Exception as e:
            found = []
        if not found:
            try:
                found = plumb.pages[pno].find_tables()
            except Exception:
                found = []
        for ti, tb in enumerate(found):
            try:
                data = tb.extract()
            except Exception:
                continue
            if not data or len(data) < 2: continue
            md, rows = md_table(data)
            if not rows or len(rows) < 2 or len(rows[0]) < 2: continue
            nnone = sum(1 for r in data for c in r if c in (None, ''))
            ntot = sum(len(r) for r in data) or 1
            quality = 'ok' if nnone / ntot < 0.35 else 'sparse'
            fname = f"p{pnum:03d}-t{ti}.csv"
            with open(f"{outdir}/tables/{fname}", 'w', newline='') as f:
                csv.writer(f).writerows(rows)
            tables.append(dict(bbox=tb.bbox, md=md, fname=fname, quality=quality, rows=len(rows), cols=len(rows[0])))
        # drop lines inside table bboxes
        def in_table(l):
            cx, cy = (l["x0"] + l["x1"]) / 2, (l["y0"] + l["y1"]) / 2
            return any(t["bbox"][0] - 2 <= cx <= t["bbox"][2] + 2 and t["bbox"][1] - 2 <= cy <= t["bbox"][3] + 2 for t in tables)
        body = []
        for l in lines:
            t = l["text"]
            if is_footer(t): continue
            if t in running and l["y0"] < 140:
                if t in seen_running: continue
                seen_running.add(t)
            if in_table(l): continue
            body.append(l)
        body.sort(key=lambda l: (round(l["y0"] / 3), l["x0"]))
        merged = []
        i = 0
        while i < len(body):
            l = body[i]
            if i + 1 < len(body) and re.fullmatch(r'(\d+(\.\d+)*\.?|[IVXivx]+\.)', l["text"]) and abs(body[i + 1]["y0"] - l["y0"]) < 4:
                n = body[i + 1]
                l = dict(l, text=l["text"] + ' ' + n["text"], x1=n["x1"], bold=max(l["bold"], n["bold"]), caps=n["caps"])
                i += 1
            merged.append(l)
            i += 1
        body = merged
        is_toc = sum(1 for l in body if TOC_RE.search(l["text"])) >= 4
        # left margin
        xs = [round(l["x0"]) for l in body if len(l["text"]) > 40]
        margin = collections.Counter(xs).most_common(1)[0][0] if xs else 70
        items = []  # (y, kind, payload)
        for t in tables:
            items.append((t["bbox"][1], 'table', t))
        # paragraphs
        paras = []
        cur = None
        prev = None
        for l in body:
            t = l["text"]
            lvl = 0 if is_toc else heading_level(t, l["bold"], l["caps"])
            is_caption = bool(CAPTION_RE.match(t)) and (l["bold"] > 0.5 or l["size"] < 10.5)
            bullet = bool(BULLET_RE.match(t)) or t in ('•', '-', '–')
            gap = (l["y0"] - prev["y1"]) if prev else 0
            indent = l["x0"] > margin + 10
            new_para = (cur is None or lvl or is_caption or bullet or is_toc or gap > 9 or
                        (indent and cur["kind"] == 'p' and re.search(r'[.:;!?]$', cur["text"])) or
                        (cur["kind"] in ('h', 'caption')) or (cur["kind"] == 'li' and indent is False and re.search(r'[.;]$', cur["text"]) and gap > 3))
            if new_para:
                kind = 'h' if lvl else 'caption' if is_caption else 'li' if bullet else 'toc' if is_toc else 'p'
                cur = dict(kind=kind, level=lvl, text=t, y=l["y0"])
                paras.append(cur)
            else:
                if cur["text"].endswith('-') and t[:1].islower():
                    cur["text"] = cur["text"][:-1] + t
                else:
                    cur["text"] += ' ' + t
            prev = l
        for p in paras:
            items.append((p["y"], 'para', p))
        items.sort(key=lambda x: x[0])
        out = [f"\n<!-- pagina {pnum} -->\n"]
        last_heading = None
        for y, kind, pl in items:
            if kind == 'table':
                cap = last_heading or ''
                table_manifest.append(dict(file=pl["fname"], page=pnum, rows=pl["rows"], cols=pl["cols"], quality=pl["quality"], context=cap))
                out.append(f"\n{pl['md']}\n\n<!-- tabella: tables/{pl['fname']} ({pl['quality']}) -->\n")
            else:
                t = pl["text"]
                if pl["kind"] == 'h':
                    out.append(f"\n{'#' * pl['level']} {t}\n")
                    headings.append((pl["level"], t, pnum))
                    last_heading = t
                elif pl["kind"] == 'caption':
                    out.append(f"\n*{t}*\n")
                    last_heading = t
                elif pl["kind"] == 'li':
                    tt = BULLET_RE.sub('', t) if BULLET_RE.match(t) else t.lstrip('•-– ')
                    out.append(f"- {tt}")
                elif pl["kind"] == 'toc':
                    out.append(t + '  ')
                else:
                    out.append(f"\n{t}\n")
        md_pages.append('\n'.join(out))
    with open(f"{outdir}/full-text.md", 'w') as f:
        f.write(f"# {part} – testo integrale estratto\n\nFonte: `{pdfpath}`. Marcatori `<!-- pagina N -->` = pagina fisica del PDF.\n")
        f.write('\n'.join(md_pages))
    with open(f"{outdir}/tables/manifest.csv", 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['file', 'page', 'rows', 'cols', 'quality', 'context'])
        w.writeheader(); w.writerows(table_manifest)
    with open(f"{outdir}/headings.md", 'w') as f:
        f.write(f"# Outline rilevato – {part}\n\n(livello, titolo, pagina PDF)\n\n")
        for lvl, t, p in headings:
            f.write(f"{'  ' * (lvl - 1)}- [H{lvl}] {t} — p.{p}\n")
    # --- images
    usage = collections.Counter()
    for page in doc:
        for img in page.get_images(full=True): usage[img[0]] += 1
    img_manifest = []
    done = set()
    for pno, page in enumerate(doc):
        for i, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            if xref in done: continue
            done.add(xref)
            info = doc.extract_image(xref)
            w, h = info["width"], info["height"]
            kind = 'logo' if usage[xref] > 3 else 'figura' if w >= 600 else 'piccola'
            if w < 200 or h < 100: continue
            fname = f"p{pno + 1:03d}-img{i}-{w}x{h}.{info['ext']}"
            with open(f"{outdir}/images/{fname}", 'wb') as f: f.write(info["image"])
            img_manifest.append(dict(file=fname, page=pno + 1, width=w, height=h, uses=usage[xref], kind=kind))
    with open(f"{outdir}/images/manifest.csv", 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['file', 'page', 'width', 'height', 'uses', 'kind'])
        w.writeheader(); w.writerows(img_manifest)
    print(part, "pages", len(doc), "tables", len(table_manifest), "headings", len(headings), "images", len(img_manifest))

if __name__ == '__main__':
    for part, (outdir, pdfpath) in PARTS.items():
        process(part, outdir, pdfpath)
