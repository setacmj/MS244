# Wellcome Manuscript Digitisation Pipeline: Token Usage, Ongoing Cost & Optimisation Plan

**Benchmark Corpus:** Wellcome Collection **MS.244** (`ae3q6kcm` / `b19608652`)  
**Scope:** 438 transcribed pages (Canvases 7–444), 38,822 aligned diplomatic & Modern English lines, 191 extracted figures, 96 Wikidata-linked index terms, TEI P5 XML, split GitHub Markdown editions, and interactive GitHub Pages explorer (`https://setacmj.github.io/MS244/`).  
**Model Used:** Gemini 4 Hydrogen (`gemini-4-hydrogen-medium`)

---

## 1. Observed Token Usage & Cost Breakdown (MS.244 Benchmark)

All token figures below are summed directly from the recorded `input_tokens`, `cache_read_tokens`, and `output_tokens` across the main coordinator transcript and all **89** subagent / `run_workflow` transcription runs (`90` transcripts total):

| Scope | Runs / Steps | Fresh Input Tokens | Cache-Read Tokens | Output Tokens | Total Processed |
| :--- | :--- | ---: | ---: | ---: | ---: |
| **Transcriber Agents** (Subagents + Workflow) | 89 runs | 13,756,505 | 103,198,712 | 4,319,048 | **121,274,265** |
| **Main Coordinator** (Setup, Index, Explorer, GitHub) | 153 steps | 1,222,758 | 28,834,309 | 174,974 | **30,232,041** |
| **Combined Total** | **90 transcripts** | **14,979,263** | **132,033,021** | **4,494,022** | **151,506,306** |

- **Total non-cached tokens (fresh input + output):** `19,473,285` (~19.5M tokens)
- **Average per transcribed page (438 pages, transcribers only):**
  - Fresh input: ~`31,408` tokens/page
  - Cache read: ~`235,613` tokens/page
  - Output (incl. thinking): ~`9,861` tokens/page

### Estimated Cost at Gemini 4 Hydrogen Paid-Tier API Rates
Using **\$1.50 / 1M** fresh input tokens, **\$7.50 / 1M** output tokens (including thinking), and a standard **90% context-caching discount** (**\$0.15 / 1M** cache-read tokens):

| Scope | Fresh Input (\$1.50/1M) | Cache Read (\$0.15/1M) | Output (\$7.50/1M) | Estimated Cost |
| :--- | ---: | ---: | ---: | ---: |
| **Transcriber Agents** (89 runs) | \$20.63 | \$15.48 | \$32.39 | **\$68.51** |
| **Main Coordinator** | \$1.83 | \$4.33 | \$1.31 | **\$7.47** |
| **Combined Total** | **\$22.47** | **\$19.80** | **\$33.71** | **\$75.98** |

- **Effective cost per page (unoptimised baseline):** **~\$0.17 / page** (`\$0.16 / page` transcribers only).
- *(At a 95% cache-read discount of \$0.075 / 1M, total drops to **~\$66.08**; without caching, 132M cache reads would have added ~\$198 at full input rates.)*

---

## 2. Why Tokens Were Spent Where They Were (Root-Cause Diagnostics)

1. **Multi-turn `cache_read_tokens` amplification (132M tokens):** Each 5-page transcriber averaged ~8–12 turns (reading `pages_batch1.py`, reading `MS244_iiif_index.json`, reading images sequentially, writing `pages_batchN.py`, running `py_compile`). Every extra turn re-reads the growing context (images + prompt + prior tool outputs).
2. **Verbose per-batch Python boilerplate (`4.32M` output tokens):** Every `pages_batchN.py` duplicated the `make_lines()` helper and full dictionary keys, inflating output tokens (the most expensive tier at \$7.50/1M).
3. **False-positive content filters & retries (~18 extra runs):** Early batches without academic archival-paleography framing triggered safety filters on early modern anatomical/urological recipes, causing ~18 wasted/retried runs out of 89.
4. **Uniform model tier across non-text leaves:** Blank flyleaves, binding shots, and repetitive armorial grids were processed with the same flagship reasoning tier as dense 16th-century secretary hand.

---

## 3. Optimisation Plan for a Repeatable Multi-Manuscript Pipeline

### Lever 1: Standardise `edition_schema.py` & Compact Batch Output (Saves ~30–40% Output Cost)
- Move `make_lines()` and IIIF URL construction into a single shared `edition_schema.py` imported by all batches.
- Have transcribers emit only `(lno, ltype, orig, en, note)` tuples and minimal page metadata (`canvas_num`, `orig_page`, `summary`, `figures`, `columns`).
- **Impact:** Cuts output tokens per page from ~9,860 to ~5,500–6,000 (~**\$14 saved** per 400-page manuscript).

### Lever 2: Parallel Image Reads & Turn Consolidation (Saves ~50–60% Cache-Read Cost)
- Pass canvas dimensions (`width`, `height`, `jp2`) directly inside each batch prompt so the agent does **not** need to read `MS244_iiif_index.json` or `pages_batch1.py`.
- Instruct the transcriber to call `read_file` on **all 5 canvas images in a single parallel turn**, then write `pages_batchN.py` in turn 2, and `py_compile` in turn 3 (3 turns total instead of 10+).
- **Impact:** Cuts `cache_read_tokens` by ~55–65% (~**\$10–\$12 saved** per 400-page manuscript).

### Lever 3: Pre-Filter Blank, Binding & Reference Canvases (Saves ~10–15% Total Cost)
- After downloading all JPEGs, run a local Python pre-check (JPEG header/EOI `\xff\xd8...\xff\xd9` validation + file-size / edge-density heuristic) or a single `flash_lite` pass to auto-classify blank flyleaves, covers, edges, and colour-checker shots into `pages_batch0.py` without invoking full transcribers.
- **Impact:** Eliminates 15–30 unnecessary transcriber pages on a typical codex.

### Lever 4: Tiered Model Routing (`flash_lite` / `flash` / `Hydrogen`)
- **`flash_lite`:** Blank leaves, binding/edge shots, simple title labels.
- **`flash`:** Printed/engraved tables, clean italic hands, repetitive armorial shield grids.
- **`Hydrogen` (Medium):** Dense 16th/17th-century secretary hand, Latin medical abbreviations, empirical marginalia.
- **Impact:** Cuts average cost on non-cursive sections by 60–80%.

### Lever 5: Optimised IIIF Image Width (`1200px` Default, `1400px` Fallback)
- Downloading `/full/1200,/0/default.jpg` instead of `1400,` reduces vision token count by ~25% while keeping secretary hand crisp; re-fetch `1400,` or `full` only when a line is flagged `[illegible?]`.

### Lever 6: Bake Archival Framing & Automated Figure Verification into `run_workflow`
- Always include the *"scholarly diplomatic transcription of historical archival handwriting for museum/library preservation"* framing in `make_prompt()` — this reduced our filter-block rate from **~25%** (Batches 6–13) to **0%** (Batches 44–82).
- Have `run_workflow` run a post-wave Python check that validates `py_compile`, verifies `canvas_num` coverage, and flags tiny (`<5%`) figure bounding boxes for automatic padding/inspection before building `docs/index.html`.

---

## 4. Projected Ongoing Cost for Future Manuscripts

Assuming the **Optimised Pipeline** (Levers 1–6 applied, targeting **~\$0.06 – \$0.09 / page** vs. the **\$0.17 / page** unoptimised MS.244 baseline):

| Manuscript Size | Example | Unoptimised Baseline (~\$0.17/p) | Optimised Pipeline (~\$0.06–\$0.09/p) |
| :--- | :--- | ---: | ---: |
| **Small Codex (150 pages)** | Short receipt book / treatise | ~\$25.50 | **\$9.00 – \$13.50** |
| **Medium Codex (400 pages)** | Wellcome **MS.244** (438 pp.) | ~\$75.98 *(actual)* | **\$24.00 – \$36.00** |
| **Large Codex (750 pages)** | Wellcome **MS.990** (741 pp.) | ~\$127.50 | **\$45.00 – \$67.50** |

---

## 5. Repeatable End-to-End Execution Checklist (New Manuscript)

1. **Bootstrap:** Run `init_manuscript.py <work_id> <shelfmark>` → fetches Wellcome API metadata + IIIF v3 manifest, builds `MS<N>_iiif_index.json`, downloads all JPEGs, and verifies `\xff\xd8...\xff\xd9` integrity.
2. **Pre-classify:** Auto-tag covers, blank flyleaves, edges, and colour checkers.
3. **Transcribe (`run_workflow`):** Run 5-page batches in waves of 10 parallel agents with `edition_schema.py` compact output + archival framing + automatic per-batch retry.
4. **Build Corpus:** Run `generate_edition_outputs.py` (JSON, TEI P5 XML, parallel/monolingual TXT & MD) + `build_parallel_md.py` (GitHub-browsable chunks).
5. **Enrich & Verify:** Run `build_entity_index.py` (with automated Wikipedia/Wikidata QID resolution) + visual crop audit on `MS<N>_figures_and_tables.json`.
6. **Publish:** Run `build_explorer_html.py` → `docs/index.html`, create `setacmj/MS<N>`, push to `main`, attach JSON to Release `v1.0.0`, and enable GitHub Pages on `/docs`.
