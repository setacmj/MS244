# Wellcome Collection MS.244 — Digital Diplomatic Edition & Modern English Parallel Corpus

A complete digital diplomatic transcription, Modern English normalisation/translation, TEI P5 XML edition, and parallel edition for **Wellcome Collection MS.244** (*Collection of medical receipts*, compiled `1564–1633` by **Henry Dineley / Dingley** of Hanley Castle, Worcestershire, with a gift inscription from **Francis Dineley** dated `3 December 1591`, later additions by **Dr. John Sadler** (`1615–1664`), a Roman Catholic Calendar, Four Seasons regimens, and an Armorial & Genealogical Pedigree), derived from the Wellcome IIIF digitisation (`b19608652` / `ae3q6kcm`).

## Browse the Parallel Editions & Historical Study Online
- **Parallel Facsimile Explorer (GitHub Pages):** https://setacmj.github.io/MS244/ — includes an **Overview** landing page with illustrated highlights, an interactive **Historical Study** tab, a side-by-side **Parallel Facsimile Reader** across all **438 transcribed pages (38,822 aligned lines)**, cross-corpus **Full-Text Search**, a curated **Index** of **96** ingredients, ailments, people, places, apparatus/tables, and heraldic pedigrees, and a **Figures & Tables (191)** gallery with IIIF `pct:` region crops.
- **Historical Provenance, Authorship & Printed Sources Study:** [MS244_Historical_Sources_and_Research_Study.md](MS244_Historical_Sources_and_Research_Study.md)
- **Parallel Diplomatic–Modern English Markdown (Browsable in GitHub):** [editions/parallel/README.md](editions/parallel/README.md) (split into ~20-page sections so every page renders directly inside GitHub's web viewer)

## Downloadable Full-Corpus Files
- **TEI P5 XML Edition:** `MS244_tei.xml` (438 pages, 38,822 aligned diplomatic/Modern English lines)
- **Structured JSON Dataset (29 MB):** `MS244_edition_data.json` (attached to Release `v1.0.0`)
- **Entity & Figure Indexes:** `MS244_entity_index.json`, `MS244_figures_and_tables.json`, `MS244_iiif_index.json`
- **Monolithic Parallel & Monolingual Editions:** `MS244_parallel_edition.md`, `MS244_transcription.txt`, `MS244_modern_english.txt`
- **Build Pipeline:** `generate_edition_outputs.py`, `build_entity_index.py`, `build_explorer_html.py`, `build_parallel_md.py`, `extract_iiif_structure.py`, and batch modules `pages_batch1.py`–`pages_batch82.py`

## Note on Facsimile Images
Local facsimile JPEGs (`*.jpg`, `images/`) are excluded from Git; the HTML explorer and Markdown editions automatically resolve images via Wellcome Collection's public IIIF endpoints.
