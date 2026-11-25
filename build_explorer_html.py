#!/usr/bin/env python3
"""
Builds the interactive Scholarly Explorer (docs/index.html & ms244_explorer.html)
for Wellcome Collection MS.244 (ae3q6kcm / b19608652).

Tabs:
1. Overview: Manuscript summary, corpus statistics, structural guide & illustrated highlights
2. Historical Study: Authorship, Henry Dineley's H.D. / crescent marks, 1564-1652 dating, Dr. John Sadler, sources
3. Facsimile Reader: Side-by-side zoomable IIIF facsimile + Diplomatic & Modern English parallel table
4. Full-Text Search: Instant cross-corpus search across all 438 pages & 38,822 lines
5. Index (96): Category-filtered entity index (Ingredients, Ailments, People, Places, Apparatus & Tables, Heraldry)
6. Figures & Tables (191): Visual gallery with IIIF pct: region crops + Tables & Calendars index
"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "MS244_edition_data.json"
INDEX_FILE = BASE_DIR / "MS244_entity_index.json"
FIGS_FILE = BASE_DIR / "MS244_figures_and_tables.json"
OUT_DOCS = BASE_DIR / "docs" / "index.html"
OUT_LOCAL = BASE_DIR / "ms244_explorer.html"

HIGHLIGHTS = [
    (8, "Prelim. 1v", "Sundials, Law Terms & Henry Dingley Signature", "Pen-and-ink 'trewe Est & weste erecte diall' alongside English law terms, carp baits, and Henry Dingley's signature."),
    (9, "Prelim. 2r", "Roman Catholic Calendar & Spring Regimen", "Red-and-black liturgical calendar for Jan–Mar paired with the 'Vere or springe time' humoral regimen."),
    (11, "Prelim. 3r", "1630 Historical Note: Prince Charles Born", "Liturgical calendar for Jun–Sep with contemporary note 'Prince Charles Borne 1630' and Autumn regimen."),
    (16, "Prelim. 5v", "Dineley Coat of Arms (1613)", "Hand-drawn armorial shield of the Dineley family dated 1613."),
    (36, "Prelim. 15v", "Angling Rods, Plumbs & Quill Floats", "Detailed instructions and sketches for jointed fishing rods, tin/brass bands, and quill floats."),
    (38, "Prelim. 16v", "'A Pype to heale thrustes' & Marks Key", "Surgical pipe of Henry Dineley's own invention (p. 71) and key to his personal empirical marks."),
    (106, "p. 68", "Dry-Stitching Plasters & Bandaged Legs", "Three surgical diagrams: laced triangular dry-stitching plasters, suture pins, and bandaged legs."),
    (208, "p. 170", "Hernia Truss & Standing Male Figure", "Illustrated 'Easy trusse & good' showing a male figure wearing the truss and a lettered technical diagram."),
    (384, "Endleaf", "1564 & 1592 Weather Chronicles", "Reversed endleaf recording 'the coldest sprynge' of 1564 and the 1592 death of bay trees across England."),
    (385, "Endleaf", "1591 Francis Dineley Gift Inscription", "'Liber henrici Dineley ex dono ffrancisci Dineley armigeri. Anno 1591 3 decembris' at Hanley Castle."),
    (404, "Armorial", "Emblazoned Heraldic Shields (Letter A)", "Partly emblazoned 5x6 armorial shield grid with family names and tinctures."),
    (428, "Pedigree", "Talbot Genealogical Pedigree (1601)", "Circular pedigree diagram of the Earls of Shrewsbury and Talbots of Grafton, dated 1601."),
]


def build_compact_pages(raw_pages):
    out = []
    for p in raw_pages:
        cols = []
        for c in p.get("columns", []):
            lines = [
                [
                    ln.get("line_num", ""),
                    ln.get("line_type", "body"),
                    ln.get("orig", ""),
                    ln.get("en", ""),
                    ln.get("note", ""),
                ]
                for ln in c.get("lines", [])
            ]
            cols.append({
                "label": c.get("col_label", c.get("col_id", "")),
                "lines": lines,
            })
        out.append({
            "c": p["canvas_num"],
            "p": p.get("orig_page", f"c{p['canvas_num']}"),
            "s": p.get("summary", ""),
            "cols": cols,
        })
    return out


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Wellcome MS.244 (ae3q6kcm) — Interactive IIIF Facsimile &amp; Parallel Edition Explorer</title>
  <style>
    :root {
      --bg: #f8f6f1;
      --card: #ffffff;
      --ink: #1e293b;
      --muted: #64748b;
      --accent: #7c2d12;
      --accent-soft: #fef3c7;
      --border: #e2e8f0;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Georgia, serif;
      background: var(--bg);
      color: var(--ink);
    }
    header {
      background: #1c1917;
      color: #fafaf9;
      padding: 12px 20px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      border-bottom: 3px solid #b45309;
    }
    header h1 {
      margin: 0;
      font-size: 1.1rem;
      font-weight: 700;
      letter-spacing: 0.01em;
    }
    header .sub {
      font-size: 0.8rem;
      color: #d6d3d1;
    }
    nav.tabs {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }
    nav.tabs button {
      background: #292524;
      color: #e7e5e4;
      border: 1px solid #44403c;
      padding: 7px 13px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.85rem;
      font-weight: 600;
    }
    nav.tabs button.active {
      background: #b45309;
      color: #fff;
      border-color: #d97706;
    }
    main {
      max-width: 1480px;
      margin: 0 auto;
      padding: 18px 20px 40px;
    }
    .tab-panel { display: none; }
    .tab-panel.active { display: block; }
    .card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 18px 22px;
      margin-bottom: 18px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .stats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
      gap: 12px;
      margin: 14px 0;
    }
    .stat-box {
      background: #fafaf9;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px;
      text-align: center;
    }
    .stat-box .num { font-size: 1.5rem; font-weight: 800; color: var(--accent); }
    .stat-box .lbl { font-size: 0.78rem; color: var(--muted); margin-top: 2px; }
    .highlights-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 14px;
    }
    .hl-card {
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 8px;
      overflow: hidden;
      cursor: pointer;
      transition: transform 0.12s ease, box-shadow 0.12s ease;
    }
    .hl-card:hover { transform: translateY(-2px); box-shadow: 0 6px 16px rgba(0,0,0,0.08); }
    .hl-card img { width: 100%; height: 190px; object-fit: cover; background: #1c1917; display: block; }
    .hl-card .body { padding: 10px 12px; }
    .hl-card .tag { font-size: 0.72rem; font-weight: 700; color: #b45309; text-transform: uppercase; }
    .hl-card h3 { margin: 4px 0 6px; font-size: 0.95rem; }
    .hl-card p { margin: 0; font-size: 0.8rem; color: var(--muted); line-height: 1.4; }

    /* Reader */
    .reader-bar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
      margin-bottom: 12px;
      background: #fff;
      padding: 10px 14px;
      border-radius: 8px;
      border: 1px solid var(--border);
    }
    .reader-bar button, .reader-bar select, .reader-bar input {
      padding: 6px 10px;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      font-size: 0.85rem;
      background: #fff;
    }
    .reader-bar button { cursor: pointer; font-weight: 600; background: #f1f5f9; }
    .reader-bar button:hover { background: #e2e8f0; }
    .reader-split {
      display: grid;
      grid-template-columns: 1fr 1.25fr;
      gap: 16px;
      align-items: start;
    }
    @media (max-width: 960px) {
      .reader-split { grid-template-columns: 1fr; }
    }
    .facsimile-pane {
      background: #1c1917;
      border-radius: 8px;
      padding: 10px;
      position: sticky;
      top: 12px;
      text-align: center;
    }
    .facsimile-pane img {
      max-width: 100%;
      max-height: 80vh;
      border-radius: 4px;
      cursor: zoom-in;
    }
    .facsimile-pane.zoomed img {
      max-height: none;
      width: 100%;
      cursor: zoom-out;
    }
    .text-pane {
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 16px;
      max-height: 84vh;
      overflow-y: auto;
    }
    table.parallel {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.84rem;
      margin-bottom: 16px;
    }
    table.parallel th, table.parallel td {
      border-bottom: 1px solid #e2e8f0;
      padding: 6px 8px;
      vertical-align: top;
      text-align: left;
    }
    table.parallel th { background: #f8fafc; font-size: 0.78rem; color: var(--muted); position: sticky; top: 0; }
    .badge {
      display: inline-block;
      padding: 1px 6px;
      border-radius: 4px;
      font-size: 0.7rem;
      font-weight: 700;
      background: #f1f5f9;
      color: #475569;
    }
    .badge.heading, .badge.rubric { background: #fee2e2; color: #991b1b; }
    .badge.marginalia, .badge.signature { background: #fef3c7; color: #92400e; }

    /* Search & Index */
    .search-box {
      display: flex;
      gap: 8px;
      margin-bottom: 14px;
    }
    .search-box input {
      flex: 1;
      padding: 10px 14px;
      font-size: 0.95rem;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
    }
    .pill-row { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 14px; }
    .pill {
      padding: 5px 12px;
      border-radius: 999px;
      border: 1px solid #cbd5e1;
      background: #fff;
      cursor: pointer;
      font-size: 0.8rem;
      font-weight: 600;
    }
    .pill.active { background: var(--accent); color: #fff; border-color: var(--accent); }
    .idx-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 12px;
    }
    .idx-card {
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px 14px;
    }
    .idx-card h4 { margin: 0 0 4px; font-size: 0.95rem; }
    .idx-card .meta { font-size: 0.76rem; color: var(--muted); margin-bottom: 8px; }
    .ref-btn {
      display: inline-block;
      margin: 2px 3px 2px 0;
      padding: 2px 7px;
      font-size: 0.74rem;
      background: #fef3c7;
      color: #7c2d12;
      border: 1px solid #fde68a;
      border-radius: 4px;
      cursor: pointer;
    }
    .ref-btn:hover { background: #fde68a; }
    .fig-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 14px;
    }
    .fig-card {
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 8px;
      overflow: hidden;
      cursor: pointer;
    }
    .fig-card img { width: 100%; height: 210px; object-fit: contain; background: #1c1917; display: block; }
    .fig-card .body { padding: 10px 12px; }
    .study-prose h2 { color: var(--accent); border-bottom: 1px solid var(--border); padding-bottom: 6px; margin-top: 22px; }
    .study-prose p, .study-prose li { line-height: 1.65; font-size: 0.95rem; }
    blockquote { border-left: 3px solid #b45309; margin: 12px 0; padding: 6px 14px; background: #fffbeb; font-style: italic; }
  </style>
</head>
<body>
  <header>
    <div>
      <h1>Wellcome Collection MS.244 — Henry Dineley's Medical Receipt Book &amp; Armorial (1564–1633)</h1>
      <div class="sub">Work ID: ae3q6kcm · Sierra ID: b19608652 · Accession: 44190 · 438 Transcribed Pages · 38,822 Aligned Lines</div>
    </div>
    <nav class="tabs" id="navTabs">
      <button class="active" data-tab="overview">Overview</button>
      <button data-tab="study">Historical Study</button>
      <button data-tab="reader">Facsimile Reader</button>
      <button data-tab="search">Full-Text Search</button>
      <button data-tab="index">Index (<span id="idxCount">0</span>)</button>
      <button data-tab="figures">Figures &amp; Tables (<span id="figCount">0</span>)</button>
    </nav>
  </header>

  <main>
    <!-- OVERVIEW -->
    <section id="tab-overview" class="tab-panel active">
      <div class="card">
        <h2 style="margin-top:0">Manuscript Overview</h2>
        <p>
          <strong>Wellcome Collection MS.244</strong> is a 41.5 × 27 cm Tudor and early Stuart folio compiled primarily by
          <strong>Henry Dineley (or Dingley)</strong> of <strong>Hanley Castle, Worcestershire</strong> (`1564–1633`),
          gifted to him by <strong>Francis Dineley</strong> on 3 December 1591, and augmented in the mid-17th century by
          <strong>Dr. John Sadler (1615–1664)</strong>. Alongside over 350 pages of English and Latin medical and surgical
          receipts, it preserves a Roman Catholic liturgical calendar, Four Seasons regimens, sundial and angling diagrams,
          1564–1598 weather chronicles, and an emblazoned Armorial with Percy, Talbot, and FitzAlan genealogical pedigrees.
        </p>
        <div class="stats-grid">
          <div class="stat-box"><div class="num">438</div><div class="lbl">Transcribed Pages (Canvases 7–444)</div></div>
          <div class="stat-box"><div class="num">38,822</div><div class="lbl">Aligned Diplomatic &amp; Modern Lines</div></div>
          <div class="stat-box"><div class="num" id="statIdx">96</div><div class="lbl">Curated Index Terms</div></div>
          <div class="stat-box"><div class="num" id="statFig">191</div><div class="lbl">Annotated Figures, Shields &amp; Pedigrees</div></div>
        </div>
      </div>

      <div class="card">
        <h2 style="margin-top:0">Illustrated Highlights (Click any card to open in Reader)</h2>
        <div class="highlights-grid" id="highlightsGrid"></div>
      </div>
    </section>

    <!-- HISTORICAL STUDY -->
    <section id="tab-study" class="tab-panel">
      <div class="card study-prose">
        <h2 style="margin-top:0">1. Codicological &amp; Physical Structure</h2>
        <p>Bound in its original blind-stamped calfskin over wooden boards with brass corner pieces and central diamond bosses (Canvases 1, 436–438), MS.244 comprises four structural units across 444 IIIF canvases:</p>
        <ul>
          <li><strong>Preliminary Leaves (Canvases 7–38, Fol. 1r–16v):</strong> English law terms, carp-angling and rod-making instructions, sundials and an astronomical quadrant, a Roman Catholic calendar paired with the Four Seasons regimens, 1564 weights &amp; measures, the 1613 Dineley arms, perpetual Easter &amp; 1645–1668 Solar Cycle tables, Fioravanti &amp; Boetius extracts, and Henry Dineley's invented surgical pipe (<em>"A Pype to heale thrustes"</em>).</li>
          <li><strong>Main Medical &amp; Surgical Compendium (Canvases 39–382, pp. 2–353):</strong> Double-column red-ruled pages organised systematically from repercusives, ulcers, fistulas, pox, gout, scrofula, dropsy, palsy, and hernia through gynaecology, restoratives, jaundice, spleen, stone, colic, stomach, burns, epilepsy, quinsy, cough, ears, gangrene, and pleurisy.</li>
          <li><strong>Reversed Endleaves &amp; Weather Chronicles (Canvases 383–387):</strong> Notes on the 1564 coldest spring, 1592 death of bay trees across England, 1598 fruit failure, and the 3 December 1591 gift inscription from Francis Dineley.</li>
          <li><strong>Armorial &amp; Genealogical Pedigrees (Canvases 388–430):</strong> Partly emblazoned 5×6 shield grids (A–B) interleaved with circular pedigrees of the FitzAlan (Arundel), Percy (Northumberland), and Talbot (Shrewsbury/Grafton, 1601) families.</li>
        </ul>

        <h2>2. Authorship, Family Network &amp; Empirical Marks (H.D. / ☾ ☾)</h2>
        <blockquote>"Liber henrici Dineley ex dono ffrancisci Dineley armigeri. Anno 1591 3 decembris." — Canvas 385</blockquote>
        <p>
          Henry Dineley of Hanley Castle anchors the volume in Worcestershire and Gloucestershire family memory, recalling <em>"my grandfather, my father and myself at Tewkesbury"</em> (p. 339), <em>"my father anno 1548"</em> (p. 335), and his grandmother <strong>Elizabeth Ergas</strong> (pp. 126, 130, 163). On Prelim. 16v (Canvas 38), he defines his double-crescent mark (<code>☾ ☾</code>) and <code>HD</code> cipher as markers of remedies he personally tested, recording dated clinical cases from 1608 to 1633 — including honest failures such as <em>"Tried this but yt failed"</em> (p. 207) on the 1627 Isle of Rhé toad cure.
        </p>

        <h2>3. Confessional Identity &amp; Later 17th-Century Strata</h2>
        <p>
          The preliminary Roman Catholic Calendar (Canvases 9–12) retains uncancelled pre-Reformation feasts including St. Thomas of Canterbury (29 December) and Corpus Christi. After 1633, <strong>Dr. John Sadler (1615–1664)</strong> added italic Latin prescriptions signed <code>D. Sadler</code> or <code>S</code> (e.g., pp. 66, 100, 181, 187, 193, 203, 207, 210, 217, 240, 280), while other mid-century hands cite <strong>Nicholas Culpeper's 1649 <em>London Dispensatory</em></strong> (p. 201) and add 1645–1652 notes.
        </p>

        <h2>4. Medical, Surgical &amp; Iatrochemical Authorities</h2>
        <p>
          Key authorities cited include <strong>John Arderne</strong>, <strong>John Woodall</strong>, <strong>Leonardo Fioravanti</strong>, <strong>Paracelsus</strong>, <strong>Joseph Quercetanus</strong>, <strong>Anselm Boetius</strong>, <strong>Rembert Dodoens</strong>, <strong>Pietro Andrea Mattioli</strong>, and <strong>Nicolás Monardes / Clusius</strong>.
        </p>
      </div>
    </section>

    <!-- FACSIMILE READER -->
    <section id="tab-reader" class="tab-panel">
      <div class="reader-bar">
        <button id="prevBtn">← Prev</button>
        <select id="pageSelect"></select>
        <button id="nextBtn">Next →</button>
        <span id="readerStatus" style="font-size:0.82rem;color:var(--muted);margin-left:auto"></span>
      </div>
      <div class="reader-split">
        <div class="facsimile-pane" id="facPane">
          <img id="facImg" src="" alt="Manuscript Facsimile" title="Click to toggle zoom" />
        </div>
        <div class="text-pane" id="textPane">
          <h3 id="pageTitle" style="margin-top:0"></h3>
          <p id="pageSummary" style="font-size:0.85rem;color:var(--muted);font-style:italic"></p>
          <div id="pageTables"></div>
        </div>
      </div>
    </section>

    <!-- SEARCH -->
    <section id="tab-search" class="tab-panel">
      <div class="card">
        <h2 style="margin-top:0">Cross-Corpus Full-Text Search (438 Pages / 38,822 Lines)</h2>
        <div class="search-box">
          <input id="searchInput" type="text" placeholder="Search diplomatic text, Modern English, or notes (e.g. Sadler, Dingley, dropsy, rosemary, 1630, Talbot)..." />
          <button id="searchBtn" style="padding:10px 18px;border-radius:8px;border:none;background:#b45309;color:#fff;font-weight:700;cursor:pointer">Search</button>
        </div>
        <div id="searchMeta" style="font-size:0.84rem;color:var(--muted);margin-bottom:10px"></div>
        <div id="searchResults"></div>
      </div>
    </section>

    <!-- INDEX -->
    <section id="tab-index" class="tab-panel">
      <div class="card">
        <h2 style="margin-top:0">Curated Manuscript Index</h2>
        <div class="pill-row" id="catPills"></div>
        <div class="search-box">
          <input id="idxFilter" type="text" placeholder="Filter index terms..." />
        </div>
        <div class="idx-grid" id="idxGrid"></div>
      </div>
    </section>

    <!-- FIGURES & TABLES -->
    <section id="tab-figures" class="tab-panel">
      <div class="card">
        <h2 style="margin-top:0">Structured Tables &amp; Calendars in MS.244</h2>
        <ul>
          <li><strong>English Law Terms</strong> — <button class="ref-btn" onclick="openCanvas(8)">Canvas 8 (Prelim. 1v)</button></li>
          <li><strong>Roman Catholic Calendar &amp; Four Seasons Regimens</strong> — <button class="ref-btn" onclick="openCanvas(9)">Jan–Mar (c9)</button> <button class="ref-btn" onclick="openCanvas(10)">Mar–Jun (c10)</button> <button class="ref-btn" onclick="openCanvas(11)">Jun–Sep (c11)</button> <button class="ref-btn" onclick="openCanvas(12)">Sep–Dec (c12)</button></li>
          <li><strong>Apothecary Weights &amp; Measures (1564 &amp; Prelim. 16v)</strong> — <button class="ref-btn" onclick="openCanvas(13)">Canvas 13 (Prelim. 4r)</button> <button class="ref-btn" onclick="openCanvas(38)">Canvas 38 (Prelim. 16v)</button></li>
          <li><strong>Perpetual Easter &amp; Solar Cycle Tables (1645–1668)</strong> — <button class="ref-btn" onclick="openCanvas(29)">Canvas 29 (Prelim. 12r)</button> <button class="ref-btn" onclick="openCanvas(30)">Canvas 30 (Prelim. 12v)</button></li>
          <li><strong>Armorial Shield Grids (Letters A–B)</strong> — <button class="ref-btn" onclick="openCanvas(391)">c391</button> <button class="ref-btn" onclick="openCanvas(404)">c404</button> <button class="ref-btn" onclick="openCanvas(413)">c413</button> <button class="ref-btn" onclick="openCanvas(429)">c429</button></li>
        </ul>
      </div>
      <div class="card">
        <h2 style="margin-top:0">Extracted Figures, Diagrams, Shields &amp; Pedigrees</h2>
        <div class="search-box">
          <input id="figFilter" type="text" placeholder="Filter figures by label or description (e.g. sundial, truss, Percy, Talbot, shield, manicule)..." />
        </div>
        <div class="fig-grid" id="figGrid"></div>
      </div>
    </section>
  </main>

  <script>
    const PAGES = __PAGES_JSON__;
    const INDEX = __INDEX_JSON__;
    const FIGURES = __FIGURES_JSON__;
    const HIGHLIGHTS = __HIGHLIGHTS_JSON__;

    let curIdx = 0;

    function esc(s) {
      return String(s || "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    }

    function iiifUrl(c, w) {
      return `https://iiif.wellcomecollection.org/image/b19608652_MS_244_${String(c).padStart(4, "0")}.JP2/full/${w},/0/default.jpg`;
    }

    function switchTab(tabId) {
      document.querySelectorAll("nav.tabs button").forEach(b => b.classList.toggle("active", b.dataset.tab === tabId));
      document.querySelectorAll(".tab-panel").forEach(p => p.classList.toggle("active", p.id === "tab-" + tabId));
    }

    document.querySelectorAll("nav.tabs button").forEach(btn => {
      btn.addEventListener("click", () => switchTab(btn.dataset.tab));
    });

    function openPageIdx(idx) {
      curIdx = Math.max(0, Math.min(PAGES.length - 1, idx));
      const p = PAGES[curIdx];
      document.getElementById("pageSelect").value = curIdx;
      document.getElementById("facImg").src = iiifUrl(p.c, 1200);
      document.getElementById("pageTitle").textContent = `Canvas ${p.c} — ${p.p}`;
      document.getElementById("pageSummary").textContent = p.s;
      const totalLines = p.cols.reduce((a, c) => a + c.lines.length, 0);
      document.getElementById("readerStatus").textContent = `${curIdx + 1} / ${PAGES.length} · ${totalLines} lines`;

      const container = document.getElementById("pageTables");
      container.innerHTML = "";
      p.cols.forEach(col => {
        const h4 = document.createElement("h4");
        h4.textContent = col.label;
        h4.style.margin = "12px 0 6px";
        container.appendChild(h4);

        const tbl = document.createElement("table");
        tbl.className = "parallel";
        tbl.innerHTML = "<thead><tr><th style='width:42px'>#</th><th style='width:72px'>Type</th><th>Diplomatic</th><th>Modern English</th><th>Notes</th></tr></thead>";
        const tb = document.createElement("tbody");
        col.lines.forEach(ln => {
          const tr = document.createElement("tr");
          tr.innerHTML = `<td>${esc(ln[0])}</td><td><span class="badge ${esc(ln[1])}">${esc(ln[1])}</span></td><td>${esc(ln[2])}</td><td>${esc(ln[3])}</td><td style="color:#64748b;font-size:0.78rem">${esc(ln[4])}</td>`;
          tb.appendChild(tr);
        });
        tbl.appendChild(tb);
        container.appendChild(tbl);
      });
      switchTab("reader");
    }

    window.openCanvas = function(c) {
      const idx = PAGES.findIndex(p => p.c === c);
      if (idx >= 0) openPageIdx(idx);
    };

    // Init reader controls
    const sel = document.getElementById("pageSelect");
    PAGES.forEach((p, idx) => {
      const opt = document.createElement("option");
      opt.value = idx;
      opt.textContent = `Canvas ${p.c} (${p.p})`;
      sel.appendChild(opt);
    });
    sel.addEventListener("change", () => openPageIdx(parseInt(sel.value, 10)));
    document.getElementById("prevBtn").addEventListener("click", () => openPageIdx(curIdx - 1));
    document.getElementById("nextBtn").addEventListener("click", () => openPageIdx(curIdx + 1));
    document.getElementById("facImg").addEventListener("click", () => {
      document.getElementById("facPane").classList.toggle("zoomed");
    });

    // Highlights
    const hlGrid = document.getElementById("highlightsGrid");
    HIGHLIGHTS.forEach(([c, tag, title, desc]) => {
      const div = document.createElement("div");
      div.className = "hl-card";
      div.innerHTML = `<img loading="lazy" src="${iiifUrl(c, 500)}" alt="${esc(title)}" /><div class="body"><div class="tag">Canvas ${c} · ${esc(tag)}</div><h3>${esc(title)}</h3><p>${esc(desc)}</p></div>`;
      div.addEventListener("click", () => window.openCanvas(c));
      hlGrid.appendChild(div);
    });

    // Search
    function runSearch() {
      const q = document.getElementById("searchInput").value.trim().toLowerCase();
      const resDiv = document.getElementById("searchResults");
      const metaDiv = document.getElementById("searchMeta");
      resDiv.innerHTML = "";
      if (q.length < 2) { metaDiv.textContent = "Enter at least 2 characters."; return; }
      const hits = [];
      for (let i = 0; i < PAGES.length; i++) {
        const p = PAGES[i];
        for (const col of p.cols) {
          for (const ln of col.lines) {
            if ((ln[2] + " " + ln[3] + " " + ln[4]).toLowerCase().includes(q)) {
              hits.push({ idx: i, c: p.c, p: p.p, orig: ln[2], en: ln[3] });
              if (hits.length >= 200) break;
            }
          }
          if (hits.length >= 200) break;
        }
        if (hits.length >= 200) break;
      }
      metaDiv.textContent = `Showing ${hits.length}${hits.length >= 200 ? "+" : ""} matching lines for "${q}"`;
      hits.forEach(h => {
        const row = document.createElement("div");
        row.style.cssText = "padding:8px 0;border-bottom:1px solid #e2e8f0;font-size:0.86rem";
        row.innerHTML = `<button class="ref-btn" onclick="openPageIdx(${h.idx})">Canvas ${h.c} (${esc(h.p)})</button> <strong>${esc(h.orig)}</strong> — <span style="color:#475569">${esc(h.en)}</span>`;
        resDiv.appendChild(row);
      });
    }
    document.getElementById("searchBtn").addEventListener("click", runSearch);
    document.getElementById("searchInput").addEventListener("keydown", e => { if (e.key === "Enter") runSearch(); });

    // Index
    document.getElementById("idxCount").textContent = INDEX.length;
    document.getElementById("statIdx").textContent = INDEX.length;
    const cats = ["All", ...new Set(INDEX.map(x => x.category))];
    let activeCat = "All";
    const pillsDiv = document.getElementById("catPills");
    cats.forEach(cat => {
      const b = document.createElement("button");
      b.className = "pill" + (cat === "All" ? " active" : "");
      b.textContent = cat;
      b.addEventListener("click", () => {
        activeCat = cat;
        pillsDiv.querySelectorAll(".pill").forEach(x => x.classList.toggle("active", x.textContent === cat));
        renderIndex();
      });
      pillsDiv.appendChild(b);
    });
    function renderIndex() {
      const q = document.getElementById("idxFilter").value.trim().toLowerCase();
      const grid = document.getElementById("idxGrid");
      grid.innerHTML = "";
      INDEX.filter(it => (activeCat === "All" || it.category === activeCat) && (!q || it.name.toLowerCase().includes(q) || it.desc.toLowerCase().includes(q)))
        .forEach(it => {
          const card = document.createElement("div");
          card.className = "idx-card";
          const refsHtml = it.refs.slice(0, 18).map(r => `<button class="ref-btn" onclick="openPageIdx(${r.pIdx})">c${r.canvas_num} (${esc(r.orig_page)})</button>`).join("");
          const more = it.refs.length > 18 ? `<span style="font-size:0.74rem;color:#64748b"> +${it.refs.length - 18} more</span>` : "";
          const wdHtml = it.qid ? `<a href="https://www.wikidata.org/wiki/${esc(it.qid)}" target="_blank" rel="noopener" style="display:inline-block;margin-left:6px;padding:1px 6px;font-size:0.7rem;background:#e0f2fe;color:#0369a1;border:1px solid #bae6fd;border-radius:4px;text-decoration:none;font-weight:700">Wikidata: ${esc(it.qid)} ↗</a>` : "";
          card.innerHTML = `<div style="font-size:0.7rem;color:#b45309;font-weight:700;text-transform:uppercase">${esc(it.category)}${wdHtml}</div><h4>${esc(it.name)}</h4><div class="meta">${esc(it.desc)} · ${it.page_hits} pages / ${it.line_hits} lines</div><div>${refsHtml}${more}</div>`;
          grid.appendChild(card);
        });
    }
    document.getElementById("idxFilter").addEventListener("input", renderIndex);
    renderIndex();

    // Figures
    document.getElementById("figCount").textContent = FIGURES.length;
    document.getElementById("statFig").textContent = FIGURES.length;
    function renderFigs() {
      const q = document.getElementById("figFilter").value.trim().toLowerCase();
      const grid = document.getElementById("figGrid");
      grid.innerHTML = "";
      FIGURES.filter(f => !q || f.label.toLowerCase().includes(q) || f.desc.toLowerCase().includes(q))
        .forEach(f => {
          const card = document.createElement("div");
          card.className = "fig-card";
          card.innerHTML = `<img loading="lazy" src="${f.iiif_crop}" alt="${esc(f.label)}" /><div class="body"><div style="font-size:0.72rem;color:#b45309;font-weight:700">Canvas ${f.canvas_num} (${esc(f.orig_page)})</div><h4 style="margin:4px 0">${esc(f.label)}</h4><p style="margin:0;font-size:0.8rem;color:#64748b">${esc(f.desc)}</p></div>`;
          card.addEventListener("click", () => openPageIdx(f.pIdx));
          grid.appendChild(card);
        });
    }
    document.getElementById("figFilter").addEventListener("input", renderFigs);
    renderFigs();

    // Load Canvas 8 (Prelim 1v) initially in Reader
    openPageIdx(1);
    switchTab("overview");
  </script>
</body>
</html>
"""


def main():
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    idx = json.loads(INDEX_FILE.read_text(encoding="utf-8"))
    figs = json.loads(FIGS_FILE.read_text(encoding="utf-8"))

    compact_pages = build_compact_pages(data["pages"])
    html_out = (
        HTML_TEMPLATE
        .replace("__PAGES_JSON__", json.dumps(compact_pages, ensure_ascii=False))
        .replace("__INDEX_JSON__", json.dumps(idx, ensure_ascii=False))
        .replace("__FIGURES_JSON__", json.dumps(figs, ensure_ascii=False))
        .replace("__HIGHLIGHTS_JSON__", json.dumps(HIGHLIGHTS, ensure_ascii=False))
    )

    OUT_DOCS.parent.mkdir(parents=True, exist_ok=True)
    OUT_DOCS.write_text(html_out, encoding="utf-8")
    OUT_LOCAL.write_text(html_out, encoding="utf-8")
    print(f"Wrote {OUT_DOCS} and {OUT_LOCAL} ({len(html_out):,} bytes)")


if __name__ == "__main__":
    main()
