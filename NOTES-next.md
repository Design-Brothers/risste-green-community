# Handoff — pagine mancanti + deploy (obiettivo corrente)

## Obiettivo
Completare le 4 pagine mancanti in `prototype/`, aggiornare le nav delle pagine esistenti, verificare, creare repo GitHub su org **Design-Brothers** (gh autenticato come fborgherodbsagency, scope repo), pubblicare su **Vercel via CLI** (`vercel whoami` = `fborghero-1524`) e dare URL all'utente.

## Deploy
- Deploy root: `prototype/` (statico, HTML+CSS+JS). Aggiungere `prototype/vercel.json` con `{"cleanUrls": true}` per URL senza .html.
- Comando: `cd prototype && vercel --prod --yes` (o `vercel deploy --prod`). Prima commit su GitHub: `gh repo create Design-Brothers/risste-green-community --public --source . --push` dalla root RISSTE.
- Link interni già usati in index/alta-gallura: `alta-gallura.html`, `#` con onclick disabilitati → aggiornare a progetto.html / strategia.html / sughero-sardegna.html / innovazione.html.

## Dati già consolidati (rigenerabili con build-data2.mjs)
- `assets/data-sughero.js` → `window.RISSTE_SUGHERO`:
  - `comuni[30]`: rank, comune, slug, sugherete_ha, peso_pct, ivp, classe_ivp, classe_incendio, quota_medioalto_alto_pct, classe_icr, n_complessi, quota_complesso_maggiore_pct, densita_frammentazione, profilo_ivp_x_incendio, profilo_integrato, indicazioni_operative, lettura_icr, distribuzione_pedologica[{unita_pedologica,superficie_ha,incidenza_pct,classe_ivp,punteggio_ivp}], distribuzione_incendio[{classe,superficie_ha,incidenza_pct,indice_classe}]
  - `sintesi` (oggetto): totali{sugherete_30_comuni_ha_testo 83790.9, quota_medioalto_alto_pct_sul_totale 71.82, n_complessi_totali 882, ivp_medio_ponderato_ha 3.361, ipi_medio_ponderato_ha 39.85...}, superficie_per_classe_incendio_ha{pentaval}, conteggi_classe_ivp{dataset[{classe,n_comuni,comuni[]}], testo_pag_27, differenze}, conteggi_classe_incendio, conteggi_classe_icr (Alta 9/Media 6/Bassa 8/Molto bassa 7), conteggi_profilo_integrato, top5_estensione, estremi, profili_estremi
  - `indici` = {indici:[{sigla IVP/IPI/ICR, nome, domanda, definizione...}]} — accedere `.indici`
  - `bibliografia[153]`: id, anno, paese, settore, materiale, trl, trl_min, trl_max, priorita, stelle, riferimento (lungo, autori+titolo+rivista)
  - `scouting` (oggetto): metodologia, n_pubblicazioni, per_paese, per_ambito, per_trl_documento, per_trl_database, evidenze[6{text}]
  - `direttrici[9]`: id, direttrice, driver_europeo, evidenze_emerse, ...
  - `certificazioni[14]`: id, strumento, nome_completo, tipo, cosa_certifica, rilevanza_filiera
  - `framework` (oggetto): acronimo{sigla, espansione_inglese, espansione_italiana, definizione}, step[8]{n,nome,sottotitolo,descrizione}, legenda_figura, modello_integrato{elemento_distintivo}, strategie_territoriali_per_profilo.profili[{profilo,...}], profili_integrati_allegato_1
  - `conclusioni` = {messaggi_chiave[8]{id,tema,testo}}
- `assets/data-strategia.js` → `window.RISSTE_STRATEGIA`:
  - `roadmap[44]`: tipo ∈ fase(4),azione,area_pilota,azione_prioritaria_baseline,governance_futura,contratto_filiera_ulteriore,living_lab_replicabilita; record azione: numero,titolo,fase,mese_inizio,mese_fine,prosegue_oltre_m36,area_pilota_comuni,responsabile,output_atteso; record fase: tipo,numero,nome,mese_inizio,mese_fine,obiettivo
  - `esg[56]`: id(E-T01),dimensione E/S/G,filiera,nome,cosa_misura,unita,pagina_pdf
  - `filiere[3]`: tipo:"filiera",nome,slug(bosco-sughero|...),descrizione (lunga), ...
  - `servizi[26]`: tipo,nome,descrizione,descrizione_fig_4b,pagina_pdf
  - `formazione[27]`: tipo,eqf,codice,profilo,settore_complessita,contesto_esercizio,descrizione_competenze,ore,pagina_pdf
  - `frameworkGreen[17]`: tipo,ordine,nome,slug,descrizione_breve,elementi,pagine_pdf
  - `obiettivi[15]`: tipo,pagina_pdf,testo
- Vecchio: `assets/data.js` → window.RISSTE_DATA (Alta Gallura, usato da alta-gallura.html).

## Figure in prototype/assets/figure/
fig-1a, fig-2a, fig-3a (parte1); fig-4a/4b/4c/4d/4e/4f (parte1, strategia); fig-2,fig-3,fig-4 (ranking 30 comuni IVP/IPI/ICR, parte2); fig-5 (Paesi), fig-6 (ambiti), fig-7 (framework S.U.G.H.E.R.A.). PDF in `prototype/pdf/`: RISSTE_CUP_..._Parte1_signed.pdf, Parte2_signed.pdf.

## Componenti disponibili (site.js, funzioni globali)
`fmt{int,dec,pct}`, `initOrbs(el, palette)`, `ORB_PALETTES{landing, alta-gallura-hero, sughero}`, `initChapters(el, chapters, skipTo)` (chapters: title,context,value,unit,valueLabel,source,ghost,tone green|cyan|blue|cork,orbPos{x,y,s},prefix,dec), `initSubnav(navEl, afterEl)`, `slopeRows(el, rows)`, `divergeRows`, `sparkline(points)`, `landStack(el, classi)`, `openLightbox(id)`, `initComuniGrid`, `initComuneDrawer`, `decorticaRings`.
Classi CSS pronte: kpi-row/kpi-card, chart-block, doors, scenari, comuni-grid, filter-bar/chip, drawer (overlay+aside), deep-dive/table-wrap/table.data, figure.infografica+dialog.lightbox, section-head, reveal, micro, ghost, orbs.
Pagine esistenti linkano anche nature.css/nature.js (solo landing/alta-gallura); le nuove pagine bastano con site.css/site.js.

## Colori classi (COMPONENTI.md §9d)
IVP/ICR ordinali: Alta #2E7D32, Media #F0B800, Bassa #F08800, "Molto bassa" #D84315.
Incendio: Basso #2E7D32, Mediobasso #8BC34A, Medio #F0B800, Medioalto #F08800, Alto #D84315.

## Pagine da creare (copy in site-content/pagine/, già letti)
1. **progetto.html** — hero semplice (1 orbo verde-blu grande quasi fermo, ghost "RISSTE"); sezioni: Perché una Green community (+fig-2a lightbox), Come abbiamo lavorato (3 pilastri card + KPI 415 pagine/11+30 comuni/153 pubblicazioni), Gruppo di lavoro (4 persone: Maria Fais coord. scientifica biologa; Nicola Garippa e Vincenzo Sechi agronomi; Gianfranco Sanna economista presidente RISSTE; Fabrizio Mureddu avvocato direttore RISSTE), Documenti (card: PDF Studio 1 219pp, PDF Studio 2 196pp → link pdf/, 16 infografiche, 36 dataset), Limiti dello studio, Contatti (Via Basilicata 3, 07026 Olbia · centrostudirisste@pec.it). Nav attiva "Progetto".
2. **strategia.html** — hero con anelli verdi spin + ghost "STRATEGIA" (no capitoli); sottomenu; sezioni: Il framework (KPI 56 indicatori/3 filiere/36 mesi + fig-4a), Tre filiere (3 card da filiere[]: bosco-sughero, bovina estensiva, suinicola agroforestale + fig-4c/4d/4e), Il contratto di filiera, **Roadmap timeline** (4 fasi × 36 mesi, azioni come pill posizionate; click → pannello dettaglio con output_atteso; da roadmap[]), Approfondimenti: esg (tabella 56 per dimensione), servizi, formazione, fig-4b/4f.
3. **sughero-sardegna.html** — hero: 30 sferette ambra/terracotta grandi ∝ ettari (initOrbs con palette generata dai dati), ghost "SUGHERETA"; 4 capitoli (≈90% / 83.790 ha / 21 su 30 / 16 su 30, toni cork/green); sezioni: Tre indici (3 card da indici.indici), Dove sta la risorsa (barre top 10 ha + fig-2/3/4 lightbox "elaborazione grafica dello studio"), **Esploratore** (UNICA interazione: select indicatore [ha/IVP/%pericolo/ICR quota complesso], select classe IVP, ordine; 30 barre orizzontali; click → drawer 30 comuni), Leggere i tre indici insieme (conteggi da sintesi: matrice profili), Approfondimenti (indici definizioni, conteggi classe, contesto).
   Drawer sughero (nuovo, nel page script, riusa .drawer CSS): rank, ha, peso; badge IVP/IPI-%, ICR; barra pedologica (impilata per unità, colori = classe_ivp); barra incendio (colori classe); ICR stats (n_complessi, quota complesso maggiore, densità); profilo_integrato + indicazioni_operative; nota sintesi; cross-link per calangianus/tempio-pausania → alta-gallura.html?comune=slug.
4. **innovazione.html** — hero: anelli ambra spin + ghost "S.U.G.H.E.R.A."; sezioni: Una ricerca che accelera (KPI 153/12 ambiti/66 compositi + barre per Paese da scouting.per_paese + fig-5), Maturità (TRL: fasce da bibliografia trl o scouting.per_trl_database), Nove direttrici (card da direttrici), Certificare per valere di più (tabella certificazioni[14] + fig-6?), S.U.G.H.E.R.A. (stepper 7-8 step da framework.step + fig-7 + strategie per profilo), In sintesi (8 messaggi conclusioni.messaggi_chiave), **Database bibliografico** (UNICA interazione: ricerca testuale + filtri settore/paese/priorità + tabella 153, export CSV opzionale).
   NB: dataset dice 153 record (non 166); da scouting.evidenze/n_pubblicazioni per i numeri corretti (Portogallo 38%, materiali 66).

## Verifica
`node shoot.mjs` (playwright-core + Chrome di sistema) estendere con le nuove pagine; controllare overflow-x=0 e zero pageerror. Screenshot in prototype/shots/.

## Stato attuale
- build-data2.mjs eseguito OK: data-sughero.js (258KB), data-strategia.js (100KB).
- Prossimo passo: append CSS nuovi componenti a site.css, poi le 4 pagine, poi nav update, poi shoot, poi repo+deploy.
