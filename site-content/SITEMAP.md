# Sitemap del mini-sito

6 pagine. Le schede comune (11 + 30) si aprono in un pannello laterale con URL `?comune=slug`, non sono pagine.

```mermaid
flowchart TD
  H["Landing  /<br/>hero fluttuante · 5 messaggi · 4 KPI"]
  H --> P["Progetto  /progetto<br/>metodo · team · PDF · dataset · glossario"]
  H --> AG["Alta Gallura  /alta-gallura<br/>demografia · ambiente · 11 comuni"]
  H --> SS["Sughereta  /sughero-sardegna<br/>30 comuni · IVP · IPI · ICR"]
  AG --> ST["Strategia  /alta-gallura/strategia<br/>ESG · 3 filiere · roadmap 36 mesi"]
  SS --> IN["Innovazione  /sughero-sardegna/innovazione<br/>scouting · certificazioni · S.U.G.H.E.R.A."]
  AG -.-> D1(["Pannello comune × 11<br/>?comune=slug"])
  SS -.-> D2(["Pannello comune × 30<br/>?comune=slug"])
  D1 <-. "Calangianus, Tempio Pausania" .-> D2

  classDef grey fill:#F1EFE8,stroke:#5F5E5A,color:#2C2C2A;
  classDef teal fill:#E1F5EE,stroke:#0F6E56,color:#04342C;
  classDef coral fill:#FAECE7,stroke:#993C1D,color:#4A1B0C;
  classDef gen stroke-dasharray:4 3;
  class H,P grey;
  class AG,ST,D1 teal;
  class SS,IN,D2 coral;
  class D1,D2 gen;
```

Mappa dei testi già scritti (`pagine/`) sulle 6 pagine:

| Pagina | File di contenuto |
|---|---|
| `/` | `00-home.md` |
| `/progetto` | `01-progetto.md` + `12-documenti.md` |
| `/alta-gallura` | `02-alta-gallura-hub.md` + `03-alta-gallura-territorio.md` + `04-alta-gallura-comuni.md` + `04b-…-comune-template.md` (pannello) |
| `/alta-gallura/strategia` | `05-alta-gallura-green-community.md` + `06-alta-gallura-roadmap.md` |
| `/sughero-sardegna` | `07-sughero-hub.md` + `08-sughero-sughereta.md` + `08b-sughero-comune-template.md` (pannello) |
| `/sughero-sardegna/innovazione` | `09-sughero-innovazione.md` + `10-sughero-framework.md` |

`seo.md` elenca ancora le 12 pagine della prima versione: per le pagine accorpate valgono title e description della prima riga del gruppo.
