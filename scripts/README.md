# Script di estrazione (passata 1)

Requisiti: Python 3.11+, `pip install pymupdf pdfplumber pillow`.

```bash
python3 scripts/01_extract_pdf.py      # PDF → source/*/full-text.md, tables/*.csv, images/*, headings.md
python3 scripts/02_finalize_source.py  # rinomina figure, elimina firme/loghi duplicati, split in capitoli/, README per parte
```

Eseguire dalla radice della repo. Il secondo script va lanciato una sola volta dopo il primo (sposta i file immagine).
