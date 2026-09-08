import os, re, csv, shutil, hashlib

ROOT = "source"
P1 = f"{ROOT}/parte1-green-community-alta-gallura"
P2 = f"{ROOT}/parte2-filiera-sughero-sardegna"
BRAND = f"{ROOT}/brand"
os.makedirs(BRAND, exist_ok=True)

# ---------- images ----------
IMG_MAP = {
 P1: {
  "p001-img0-812x1176.jpeg": ("brand", "copertina-sfondo.jpeg", "Sfondo copertina (gradiente verde con logo RISSTE)"),
  "p003-img0-456x155.png": ("brand", "logo-risste-orizzontale.png", "Logo R.I.S.S.T.E. orizzontale con payoff"),
  "p003-img3-1366x995.png": ("brand", "logo-risste-verticale.png", "Logo R.I.S.S.T.E. verticale con payoff"),
  "p029-img1-1480x1223.png": ("fig", "fig-1a-analisi-demografico-economica-imprese.png", "Figura 1a. Analisi demografico-economica sulle attività produttive degli 11 Comuni (grafici A–M)"),
  "p035-img1-1024x559.jpeg": ("fig", "fig-2a-framework-territoriale-integrato.jpeg", "Figura 2a. Framework territoriale integrato dell'Unione dei Comuni dell'Alta Gallura"),
  "p055-img1-1535x1024.jpeg": ("fig", "fig-3a-quadro-sinottico-comuni.jpeg", "Figura 3a. Schema sinottico dei comuni dell'Alta Gallura (mappa + schede)"),
  "p072-img1-1298x748.jpeg": ("fig", "fig-4a-framework-esg-data-management.jpeg", "Figura 4a. Framework ESG territoriale e flussi di interoperabilità dati"),
  "p075-img1-1298x712.jpeg": ("fig", "fig-4b-servizi-ecosistemici-carbon-farming.jpeg", "Figura 4b. Servizi ecosistemici, regolazione idrogeologica e carbon farming"),
  "p081-img1-1301x718.jpeg": ("fig", "fig-4c-filiera-bosco-sughero.jpeg", "Figura 4c. Schema integrato della filiera bosco-sughero"),
  "p084-img1-1261x718.jpeg": ("fig", "fig-4d-filiera-bovina-estensiva.jpeg", "Figura 4d. Schema integrato della filiera bovina estensiva"),
  "p087-img1-1265x697.jpeg": ("fig", "fig-4e-filiera-suinicola-agroforestale.jpeg", "Figura 4e. Schema concettuale della filiera suinicola agroforestale controllata"),
  "p090-img1-1234x695.jpeg": ("fig", "fig-4f-roadmap-operativa-36-mesi.jpeg", "Figura 4f. Roadmap operativa Green community Alta Gallura UCAG 193 (36 mesi)"),
  "p149-img1-712x219.jpeg": ("fig", "all2-fig1-carta-uso-suolo-2008.jpeg", "Allegato II, Fig. 1. Estratto Carta Uso del Suolo Sardegna 2008 (CORINE)"),
  "p150-img1-1130x599.jpeg": ("fig", "all2-fig2-carta-suoli-sardegna.jpeg", "Allegato II, Fig. 2. Stralcio Carta dei Suoli della Sardegna 1:250.000"),
  "p150-img2-724x244.jpeg": ("fig", "all2-fig3-limiti-amministrativi.jpeg", "Allegato II, Fig. 3. Limiti amministrativi comunali (DB geotopografico)"),
  "p151-img1-425x111.jpeg": ("fig", "all2-fig4-logo-qgis.jpeg", "Allegato II, Fig. 4. Logo QGIS (marchio terzo, non usare nel sito)"),
 },
 P2: {
  "p026-img1-1178x1335.jpeg": ("fig", "fig-1-workflow-analisi-integrata.jpeg", "Figura 1. Workflow metodologico dell'analisi integrata (filiera sughericola Sardegna)"),
  "p028-img1-1325x883.jpeg": ("fig", "fig-2-ivp-ranking-30-comuni.jpeg", "Figura 2. Indice di Vocazionalità Pedologica (IVP) – ranking dei 30 comuni"),
  "p029-img1-1385x923.jpeg": ("fig", "fig-3-ipi-pericolosita-incendio-30-comuni.jpeg", "Figura 3. Indice di Pericolosità da Incendio (IPI) – classi per comune"),
  "p030-img1-1386x858.jpeg": ("fig", "fig-4-icr-continuita-risorsa-30-comuni.jpeg", "Figura 4. Indice di Continuità della Risorsa (ICR) – classi per comune"),
  "p031-img1-1385x825.jpeg": ("fig", "fig-5-distribuzione-geografica-innovazione.jpeg", "Figura 5. Distribuzione geografica delle 153 pubblicazioni (Technology Scouting 2015–2025)"),
  "p032-img1-945x605.jpeg": ("fig", "fig-6-ambiti-innovazione-sughero.jpeg", "Figura 6. Principali ambiti di innovazione del sughero (153 pubblicazioni per settore)"),
  "p043-img1-1024x1459.jpeg": ("fig", "fig-7-framework-sughera.jpeg", "Figura 7. Framework S.U.G.H.E.R.A."),
 },
}
brand_rows, fig_rows = [], {P1: [], P2: []}
for part, mp in IMG_MAP.items():
    imgdir = f"{part}/images"
    old_manifest = {r["file"]: r for r in csv.DictReader(open(f"{imgdir}/manifest.csv"))}
    for fname in sorted(os.listdir(imgdir)):
        if fname == "manifest.csv": continue
        src = f"{imgdir}/{fname}"
        if fname in mp:
            kind, new, desc = mp[fname]
            r = old_manifest[fname]
            if kind == "brand":
                shutil.move(src, f"{BRAND}/{new}")
                brand_rows.append(dict(file=new, descrizione=desc, origine=f"{os.path.basename(part)} p.{r['page']}", dimensioni=f"{r['width']}x{r['height']}"))
            else:
                shutil.move(src, f"{imgdir}/{new}")
                fig_rows[part].append(dict(file=new, pagina_pdf=r["page"], dimensioni=f"{r['width']}x{r['height']}", descrizione=desc))
        else:
            os.remove(src)  # firme autografe, loghi duplicati, copertina duplicata
    os.remove(f"{imgdir}/manifest.csv")
    with open(f"{imgdir}/manifest.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["file", "pagina_pdf", "dimensioni", "descrizione"]); w.writeheader(); w.writerows(fig_rows[part])
with open(f"{BRAND}/manifest.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["file", "descrizione", "origine", "dimensioni"]); w.writeheader(); w.writerows(brand_rows)

# ---------- chapter split ----------
SPLITS = {
 P1: [
  ("00-frontespizio-indici.md", 1, 12, "Frontespizio, sommario, liste abbreviazioni e unità di misura"),
  ("01-premessa-e-quadro-metodologico.md", 13, 20, "I. Premessa – II. Quadro metodologico"),
  ("02-parte1-demografia.md", 21, 32, "Prima parte – Demografia"),
  ("03-parte2-ambiente-territorio.md", 33, 52, "Seconda parte – Ambiente e territorio"),
  ("04-parte3-comuni-unione.md", 53, 68, "Terza parte – I Comuni dell'Unione"),
  ("05-parte4-prospettive-green-communities.md", 69, 92, "Quarta parte – Prospettive Green Communities"),
  ("06-bibliografia.md", 93, 95, "Bibliografia"),
  ("07-allegato1-report-demografico-comuni.md", 96, 148, "Allegato I – Report demografico e socio-economico strutturale dei Comuni"),
  ("08-allegato2-sit-cartografia-analisi-biofisica.md", 149, 219, "Allegato II – Sistema Informativo Territoriale, cartografia e analisi biofisica"),
 ],
 P2: [
  ("00-frontespizio-indici.md", 1, 10, "Frontespizio, sommario, liste abbreviazioni e unità di misura"),
  ("01-premessa.md", 11, 14, "Premessa"),
  ("02-parte1-contesto-strategico.md", 15, 18, "Prima parte – Contesto strategico dello studio"),
  ("03-parte2-metodologia.md", 19, 26, "Seconda parte – Metodologia di analisi"),
  ("04-parte3-risultati.md", 27, 34, "Terza parte – Risultati"),
  ("05-parte4-interpretazione-prospettive.md", 35, 44, "Quarta parte – Interpretazione dei risultati e prospettive di sviluppo"),
  ("06-parte5-conclusioni.md", 45, 46, "Quinta parte – Conclusioni e prospettive"),
  ("07-bibliografia.md", 47, 48, "Bibliografia"),
  ("08-allegato1-studio-tecnico-sugherete.md", 49, 141, "Allegato I – Studio tecnico sugherete (dossier dei 30 comuni)"),
  ("09-allegato2-database-bibliografia-scientifica.md", 142, 196, "Allegato II – Database bibliografia scientifica"),
 ],
}
TITLES = {P1: "Green community UCAG 193 – Strategie territoriali integrate: gestione forestale e sviluppo sostenibile delle filiere locali (RISSTE, 2025)",
          P2: "Valorizzazione della filiera del sughero in Sardegna – Un framework multidisciplinare (RISSTE, 2025)"}
for part, splits in SPLITS.items():
    full = open(f"{part}/full-text.md").read()
    # fix false headings like "## 2025 180" (table fragments)
    full = re.sub(r'^#{1,6} (\d{4} \d{2,3})$', r'\1', full, flags=re.M)
    pages = re.split(r'\n<!-- pagina (\d+) -->\n', full)
    header, body = pages[0], pages[1:]
    by_page = {int(body[i]): body[i + 1] for i in range(0, len(body), 2)}
    open(f"{part}/full-text.md", "w").write(header + "".join(f"\n<!-- pagina {p} -->\n{by_page[p]}" for p in sorted(by_page)))
    os.makedirs(f"{part}/capitoli", exist_ok=True)
    index = [f"# {TITLES[part]}\n", "## File per capitolo\n", "| File | Pagine PDF | Contenuto |", "|---|---|---|"]
    for fname, a, b, title in splits:
        txt = "".join(f"\n<!-- pagina {p} -->\n{by_page.get(p, '')}" for p in range(a, b + 1))
        txt = re.sub(r'\n{3,}', '\n\n', txt)
        with open(f"{part}/capitoli/{fname}", "w") as f:
            f.write(f"# {title}\n\n> Fonte: {TITLES[part]}. Pagine PDF {a}–{b}. Estrazione automatica: i marcatori `<!-- pagina N -->` indicano la pagina fisica; le tabelle rimandano ai CSV in `../tables/`.\n{txt}")
        index.append(f"| [capitoli/{fname}](capitoli/{fname}) | {a}–{b} | {title} |")
    index += ["", "## Altri file", "", "- `full-text.md` – testo integrale con marcatori di pagina", "- `headings.md` – outline dei titoli rilevati con pagina",
              "- `tables/` – tutte le tabelle in CSV (`manifest.csv`: pagina, dimensioni, qualità, contesto)", "- `images/` – figure del documento rinominate (`manifest.csv`)", ""]
    open(f"{part}/README.md", "w").write("\n".join(index))
print("done")
