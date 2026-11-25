#!/usr/bin/env python3
"""
Splits MS244_edition_data.json into ~20-page Markdown chunks under editions/parallel/
so every section renders directly in GitHub's web viewer.
"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "MS244_edition_data.json"
OUT_DIR = BASE_DIR / "editions" / "parallel"
CHUNK_SIZE = 20


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    pages = data["pages"]

    toc_lines = [
        "# Wellcome Collection MS.244 — Parallel Diplomatic & Modern English Editions",
        "",
        f"Total transcribed pages: **{len(pages)}** (Canvases 7–444). Split into {CHUNK_SIZE}-page sections for direct browsing in GitHub:",
        "",
        "| Section | Canvases | Original Pages / Folios | Link |",
        "| :--- | :--- | :--- | :--- |",
    ]

    for i in range(0, len(pages), CHUNK_SIZE):
        chunk = pages[i : i + CHUNK_SIZE]
        c_start = chunk[0]["canvas_num"]
        c_end = chunk[-1]["canvas_num"]
        p_start = chunk[0].get("orig_page", f"c{c_start}")
        p_end = chunk[-1].get("orig_page", f"c{c_end}")
        fname = f"canvases_{c_start:04d}_{c_end:04d}.md"

        md = [
            f"# MS.244 Parallel Edition: Canvases {c_start}–{c_end} ({p_start} – {p_end})",
            "",
            "[Back to Parallel Edition Index](README.md)",
            "",
            "---",
            "",
        ]
        for p in chunk:
            c = p["canvas_num"]
            orig_p = p.get("orig_page", f"c{c}")
            svc = f"https://iiif.wellcomecollection.org/image/b19608652_MS_244_{c:04d}.JP2"
            md.append(f"## Canvas {c} — {orig_p}")
            md.append("")
            md.append(f"[![Canvas {c}]({svc}/full/600,/0/default.jpg)]({svc}/full/1400,/0/default.jpg)")
            md.append("")
            if p.get("summary"):
                md.append(f"*{p['summary']}*")
                md.append("")
            for col in p.get("columns", []):
                md.append(f"### {col.get('col_label', col['col_id'])}")
                md.append("")
                md.append("| Line | Diplomatic | Modern English | Notes |")
                md.append("| :--- | :--- | :--- | :--- |")
                for ln in col.get("lines", []):
                    o = ln["orig"].replace("|", "\\|")
                    e = ln["en"].replace("|", "\\|")
                    n = ln.get("note", "").replace("|", "\\|")
                    md.append(f"| {ln['line_num']} | {o} | {e} | {n} |")
                md.append("")
            md.append("---")
            md.append("")

        (OUT_DIR / fname).write_text("\n".join(md), encoding="utf-8")
        sec_no = i // CHUNK_SIZE + 1
        toc_lines.append(f"| Part {sec_no} | Canvases {c_start}–{c_end} | {p_start} – {p_end} | [{fname}]({fname}) |")

    (OUT_DIR / "README.md").write_text("\n".join(toc_lines), encoding="utf-8")
    print(f"Wrote {len(toc_lines) - 6} split Markdown sections to {OUT_DIR}")


if __name__ == "__main__":
    main()
