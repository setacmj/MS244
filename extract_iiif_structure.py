#!/usr/bin/env python3
"""
IIIF Structural & Coordinate Extractor for Wellcome Collection MS.244 (ae3q6kcm / b19608652)
Collection of medical receipts — Henry Dineley/Dyneley (or Dingley/Dyngley) (& others), 1564-1633

Anchors manuscript page structures, columns, rubrics, illustrations,
and individual text line bounding boxes (#xywh=x,y,w,h) to the
Wellcome IIIF Presentation v2/v3 and Image v2 APIs.
"""
from __future__ import annotations
import json
from pathlib import Path

WORK_ID = "ae3q6kcm"
SIERRA_ID = "b19608652"
MANIFEST_V2_URL = f"https://iiif.wellcomecollection.org/presentation/v2/{SIERRA_ID}"
MANIFEST_V3_URL = f"https://iiif.wellcomecollection.org/presentation/{SIERRA_ID}"


def compute_line_zones(ulx: int, uly: int, lrx: int, lry: int, num_lines: int):
    """Subdivides a column or text block region into calibrated horizontal line zones."""
    zones = []
    total_h = lry - uly
    step = total_h / max(1, num_lines)
    for idx in range(num_lines):
        y0 = int(round(uly + idx * step))
        y1 = int(round(uly + (idx + 1) * step))
        zones.append({
            "line": idx + 1,
            "ulx": ulx,
            "uly": y0,
            "lrx": lrx,
            "lry": y1,
            "xywh": f"{ulx},{y0},{lrx - ulx},{y1 - y0}",
        })
    return zones


def build_manifest_index(manifest_path: str | None = None):
    if manifest_path is None:
        manifest_path = str(Path(__file__).resolve().parent / "manifest_v3.json")
    with open(manifest_path, "r", encoding="utf-8") as f:
        m3 = json.load(f)

    items = m3.get("items", [])
    canvas_records = []
    for idx, c in enumerate(items):
        c_num = idx + 1
        c_id = c.get("id")
        w = c.get("width")
        h = c.get("height")
        body = c["items"][0]["items"][0]["body"]
        service_list = body.get("service", [{}])
        service_id = service_list[0].get("id") or service_list[0].get("@id") or ""
        jp2_name = service_id.split("/")[-1] if service_id else f"b19608652_MS_244_{c_num:04d}.JP2"

        # Structural classification across all 444 canvases
        if c_num == 1:
            section = "Binding: Front Cover (Recto)"
        elif c_num == 2:
            section = "Front Pastedown: Wellcome Bookplate (MS.244 / Acc. 44190) & Pencil Note"
        elif 3 <= c_num <= 6:
            section = f"Modern Binder's Front Flyleaf (Canvas {c_num})"
        elif 7 <= c_num <= 38:
            leaf_no = (c_num - 7) // 2 + 1
            side = "r" if (c_num - 7) % 2 == 0 else "v"
            section = f"Preliminary Leaves: Fol. {leaf_no}{side} (Calendar, Sundials, Weights & Measures, Angling & Surgical Receipts)"
        elif 39 <= c_num <= 382:
            section = f"Main Compendium: Medical & Surgical Receipts (Canvas {c_num})"
        elif 383 <= c_num <= 387:
            section = f"Reversed Endleaves: Weather Chronicles (1564, 1592, 1598) & Dineley Provenance (Canvas {c_num})"
        elif 388 <= c_num <= 430:
            section = f"Armorial & Genealogical Pedigrees (Canvas {c_num})"
        elif 431 <= c_num <= 435:
            section = f"Back Flyleaves & Inside Back Pastedown (Canvas {c_num})"
        elif c_num == 436:
            section = "Binding: Back Cover"
        elif 437 <= c_num <= 440:
            section = f"Binding: Spine & Book-Block Edges (Canvas {c_num})"
        else:
            section = f"End Reference / Colour Checker Shots (Canvas {c_num})"

        canvas_records.append({
            "canvas_number": c_num,
            "canvas_id": c_id,
            "image_service": service_id,
            "jp2_filename": jp2_name,
            "width": w,
            "height": h,
            "section": section,
        })

    return {
        "work_id": WORK_ID,
        "sierra_id": SIERRA_ID,
        "shelfmark": "MS.244",
        "title": "Collection of medical receipts",
        "contributors": ["Dineley/Dyneley (or Dingley/Dyngley), Henry (& others)", "Sadler, John (1615-1664)"],
        "date": "1564-1633",
        "language": "en-1564 / la (Early Modern English with Latin medical receipts and calendar)",
        "manifest_v2": MANIFEST_V2_URL,
        "manifest_v3": MANIFEST_V3_URL,
        "total_canvases": len(canvas_records),
        "canvases": canvas_records,
    }


if __name__ == "__main__":
    out_dir = Path(__file__).resolve().parent
    index_data = build_manifest_index()
    out_file = out_dir / "MS244_iiif_index.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
    print(f"Wrote {out_file} with {index_data['total_canvases']} canvases indexed.")
