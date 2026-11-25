#!/usr/bin/env python3
"""
Edition Output Generator for Wellcome Collection MS.244 (ae3q6kcm / b19608652).
Imports all pages_batch*.py modules in numeric order and builds:
  - MS244_edition_data.json
  - MS244_parallel_edition.md
  - MS244_transcription.txt
  - MS244_modern_english.txt
  - MS244_tei.xml
"""
import importlib
import json
import re
import xml.sax.saxutils as sax
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def load_all_pages():
    batch_files = sorted(
        BASE_DIR.glob("pages_batch*.py"),
        key=lambda p: int(re.search(r"(\d+)", p.stem).group(1)),
    )
    pages = []
    for bf in batch_files:
        mod_name = bf.stem
        mod = importlib.import_module(mod_name)
        num = re.search(r"(\d+)", mod_name).group(1)
        var_name = f"PAGES_BATCH{num}"
        batch_pages = getattr(mod, var_name, [])
        pages.extend(batch_pages)
    pages.sort(key=lambda p: p["canvas_num"])
    return pages


def build_json(pages):
    data = {
        "work_id": "ae3q6kcm",
        "sierra_id": "b19608652",
        "shelfmark": "MS.244",
        "title": "Collection of medical receipts",
        "contributors": [
            "Dineley/Dyneley (or Dingley/Dyngley), Henry (& others)",
            "Sadler, John (1615-1664)",
        ],
        "date": "1564-1633",
        "total_pages_transcribed": len(pages),
        "pages": pages,
    }
    out = BASE_DIR / "MS244_edition_data.json"
    out.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    return out


def build_parallel_md(pages):
    lines_out = [
        "# Wellcome Collection MS.244 — Parallel Diplomatic & Modern English Edition",
        "",
        "**Title:** Collection of medical receipts  ",
        "**Authors / Contributors:** Henry Dineley / Dingley (& others); later additions by Dr. John Sadler  ",
        "**Date:** 1564–1633 | **Work ID:** `ae3q6kcm` | **Sierra ID:** `b19608652`",
        "",
        "---",
        "",
    ]
    for p in pages:
        c = p["canvas_num"]
        orig_p = p.get("orig_page", f"c{c}")
        lines_out.append(f"## Canvas {c} — {orig_p}")
        lines_out.append("")
        if p.get("summary"):
            lines_out.append(f"*{p['summary']}*")
            lines_out.append("")
        if p.get("figures"):
            lines_out.append("**Figures / Diagrams:**")
            for fig in p["figures"]:
                lines_out.append(f"- **{fig['label']}** (`{fig['fig_id']}`): {fig['desc']}")
            lines_out.append("")
        for col in p.get("columns", []):
            lines_out.append(f"### {col.get('col_label', col['col_id'])}")
            lines_out.append("")
            lines_out.append("| Line | Type | Diplomatic Transcription | Modern English | Notes |")
            lines_out.append("| :--- | :--- | :--- | :--- | :--- |")
            for ln in col.get("lines", []):
                orig = ln["orig"].replace("|", "\\|")
                en = ln["en"].replace("|", "\\|")
                note = ln.get("note", "").replace("|", "\\|")
                lines_out.append(f"| {ln['line_num']} | {ln['line_type']} | {orig} | {en} | {note} |")
            lines_out.append("")
        lines_out.append("---")
        lines_out.append("")
    out = BASE_DIR / "MS244_parallel_edition.md"
    out.write_text("\n".join(lines_out), encoding="utf-8")
    return out


def build_plain_texts(pages):
    orig_lines = []
    en_lines = []
    for p in pages:
        hdr = f"=== Canvas {p['canvas_num']} ({p.get('orig_page', '')}) ==="
        orig_lines.append(hdr)
        en_lines.append(hdr)
        for col in p.get("columns", []):
            orig_lines.append(f"[{col.get('col_label', col['col_id'])}]")
            en_lines.append(f"[{col.get('col_label', col['col_id'])}]")
            for ln in col.get("lines", []):
                orig_lines.append(ln["orig"])
                en_lines.append(ln["en"])
            orig_lines.append("")
            en_lines.append("")
    out_orig = BASE_DIR / "MS244_transcription.txt"
    out_en = BASE_DIR / "MS244_modern_english.txt"
    out_orig.write_text("\n".join(orig_lines), encoding="utf-8")
    out_en.write_text("\n".join(en_lines), encoding="utf-8")
    return out_orig, out_en


def build_tei(pages):
    xml = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<TEI xmlns="http://www.tei-c.org/ns/1.0">',
        "  <teiHeader>",
        "    <fileDesc>",
        "      <titleStmt>",
        "        <title>Collection of medical receipts (Wellcome Collection MS.244)</title>",
        "        <author>Henry Dineley / Dingley (&amp; others)</author>",
        "      </titleStmt>",
        "      <publicationStmt>",
        "        <p>Digital diplomatic and Modern English parallel edition derived from Wellcome IIIF manifest b19608652.</p>",
        "      </publicationStmt>",
        "      <sourceDesc>",
        "        <msDesc>",
        "          <msIdentifier>",
        "            <repository>Wellcome Collection</repository>",
        "            <idno type=\"shelfmark\">MS.244</idno>",
        "            <idno type=\"sierra\">b19608652</idno>",
        "          </msIdentifier>",
        "        </msDesc>",
        "      </sourceDesc>",
        "    </fileDesc>",
        "  </teiHeader>",
        "  <text>",
        "    <body>",
    ]
    for p in pages:
        c = p["canvas_num"]
        orig_p = sax.escape(str(p.get("orig_page", "")))
        xml.append(f'      <pb n="{orig_p}" xml:id="{p["page_id"]}" facs="https://iiif.wellcomecollection.org/presentation/b19608652/canvases/b19608652_MS_244_{c:04d}.JP2"/>')
        for col in p.get("columns", []):
            xml.append(f'      <div type="column" n="{sax.escape(col["col_id"])}">')
            for ln in col.get("lines", []):
                orig = sax.escape(ln["orig"])
                en = sax.escape(ln["en"])
                xml.append(f'        <ab xml:id="{ln["line_id"]}" type="{sax.escape(ln["line_type"])}" facs="#{ln["xywh"]}">')
                xml.append(f'          <seg type="diplomatic">{orig}</seg>')
                xml.append(f'          <seg type="modern">{en}</seg>')
                xml.append("        </ab>")
            xml.append("      </div>")
    xml.extend([
        "    </body>",
        "  </text>",
        "</TEI>",
    ])
    out = BASE_DIR / "MS244_tei.xml"
    out.write_text("\n".join(xml), encoding="utf-8")
    return out


if __name__ == "__main__":
    pages = load_all_pages()
    total_lines = sum(len(col["lines"]) for p in pages for col in p.get("columns", []))
    j = build_json(pages)
    m = build_parallel_md(pages)
    t1, t2 = build_plain_texts(pages)
    x = build_tei(pages)
    print(f"Generated outputs for {len(pages)} pages ({total_lines} lines):")
    for p in (j, m, t1, t2, x):
        print(f"  - {p.name} ({p.stat().st_size} bytes)")
