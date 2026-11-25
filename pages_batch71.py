#!/usr/bin/env python3
"""
Pages Batch 71 (Canvases 386-389) for Wellcome MS.244.
Covers the final reversed endleaf and the opening of the Armorial & Genealogical Pedigrees:
  - Canvas 386 (Reversed Endleaf, blank verso): Blank verso with faint mirror-image bleed-through from Canvas 385
  - Canvas 387 (Endleaf, blank recto): Blank unnumbered recto with creases, wormholes, and faint grid show-through
  - Canvas 388 (Armorial, blank verso): Blank verso preceding the Armorial with faint diagonal 'X' mark
  - Canvas 389 (Armorial, recto): Unfinished 20-quartering heraldic achievement cartouche in yellow-ochre wash and pen-and-ink
"""


def make_lines(prefix, canvas_num, col_id, ulx, uly, lrx, lry, line_tuples):
    n = len(line_tuples)
    step = (lry - uly) / max(1, n)
    img_svc = f"https://iiif.wellcomecollection.org/image/b19608652_MS_244_{canvas_num:04d}.JP2"
    canvas_uri = f"https://iiif.wellcomecollection.org/presentation/b19608652/canvases/b19608652_MS_244_{canvas_num:04d}.JP2"
    out = []
    for idx, (lno, ltype, orig_text, en_text, note) in enumerate(line_tuples):
        y0 = int(round(uly + idx * step))
        y1 = int(round(uly + (idx + 1) * step))
        w = lrx - ulx
        h = y1 - y0
        xywh = f"{ulx},{y0},{w},{h}"
        line_id = f"{prefix}_{col_id}_l{lno:02d}" if isinstance(lno, int) else f"{prefix}_{col_id}_{lno}"
        out.append({
            "line_id": line_id,
            "line_num": str(lno),
            "line_type": ltype,
            "ulx": ulx,
            "uly": y0,
            "lrx": lrx,
            "lry": y1,
            "xywh": xywh,
            "iiif_canvas_xywh": f"{canvas_uri}#xywh={xywh}",
            "iiif_image_crop": f"{img_svc}/{xywh}/full/0/default.jpg",
            "orig": orig_text,
            "en": en_text,
            "note": note,
        })
    return out


PAGES_BATCH71 = [
    {
        "page_id": "c0386_endleaf_v",
        "canvas_num": 386,
        "jp2": "b19608652_MS_244_0386.JP2",
        "orig_page": "Unnumbered",
        "folio_side": "Reversed Endleaf (blank verso)",
        "width": 5698,
        "height": 7312,
        "frame_box": [1100, 350, 5350, 6950],
        "center_rule_x": None,
        "summary": "Blank verso of the reversed endleaf (Canvas 386): No direct writing appears on this side of the leaf. Mirror-image ink bleed-through from the preceding recto (Canvas 385, reversed 1564/1592/1598 weather chronicles and Dineley provenance) is faintly visible in the central area, along with scattered small brown stains, wormholes/pinholes, damp-staining along the bottom edge, and old paper repair at the top-left corner.",
        "figures": [],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 1100,
                "uly": 350,
                "lrx": 5350,
                "lry": 6950,
                "lines": make_lines("c0386", 386, "main", 1100, 350, 5350, 6950, [
                    (1, "note", "[Blank page]", "[Blank page — verso of reversed endleaf]", "No direct writing on this side; mirror-image bleed-through from Canvas 385 is faintly visible in the centre, together with minor staining, wormholes, damp-staining at the foot, and top-left corner repair."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0387_endleaf_r",
        "canvas_num": 387,
        "jp2": "b19608652_MS_244_0387.JP2",
        "orig_page": "Unnumbered",
        "folio_side": "Endleaf (blank recto)",
        "width": 5133,
        "height": 7312,
        "frame_box": [350, 350, 4650, 6950],
        "center_rule_x": None,
        "summary": "Blank recto (Canvas 387): No written text appears on this leaf. Visible physical features include vertical crease lines on the left side, scattered tiny wormholes/pinholes, a small cluster of dark ink flecks in the upper-right quadrant, damp-staining at the lower-left gutter edge, and very faint show-through of the ruled heraldic grid from Canvas 389.",
        "figures": [],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 350,
                "uly": 350,
                "lrx": 4650,
                "lry": 6950,
                "lines": make_lines("c0387", 387, "main", 350, 350, 4650, 6950, [
                    (1, "note", "[Blank page]", "[Blank page — unnumbered recto]", "No written text; shows vertical creases on the left, scattered wormholes, small dark flecks at upper right, damp-staining at lower-left gutter, and faint show-through of the heraldic grid on Canvas 389."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0388_armorial_v",
        "canvas_num": 388,
        "jp2": "b19608652_MS_244_0388.JP2",
        "orig_page": "Unnumbered",
        "folio_side": "Armorial (blank verso)",
        "width": 5699,
        "height": 7312,
        "frame_box": [1100, 350, 5350, 6950],
        "center_rule_x": None,
        "summary": "Blank verso preceding the Armorial (Canvas 388): No written text appears on this page. Visible features include a faint dry-point or pencil diagonal 'X' mark in the lower-left/centre, vertical crease lines on the right, old paper repair at the top-left corner, scattered tiny pinholes/wormholes, damp-staining along the bottom-right gutter edge, and a sliver of the yellow heraldic cartouche on Canvas 389 visible in the gutter at the far right.",
        "figures": [],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 1100,
                "uly": 350,
                "lrx": 5350,
                "lry": 6950,
                "lines": make_lines("c0388", 388, "main", 1100, 350, 5350, 6950, [
                    (1, "note", "[Blank page]", "[Blank page — verso preceding the Armorial]", "No written text; shows a faint diagonal 'X' mark in the lower-left area, vertical creases on the right, top-left corner repair, minor wormholes, and damp-staining at the lower-right gutter."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0389_armorial_r",
        "canvas_num": 389,
        "jp2": "b19608652_MS_244_0389.JP2",
        "orig_page": "Unnumbered",
        "folio_side": "Armorial (recto)",
        "width": 5126,
        "height": 7312,
        "frame_box": [760, 2300, 3740, 5820],
        "center_rule_x": None,
        "summary": "Opening leaf of the Armorial & Genealogical Pedigrees (Canvas 389): Contains no written text, only a large, unfinished pen-and-ink and yellow-ochre wash Renaissance strapwork heraldic cartouche enclosing a 5x4 grid of twenty quarterings. Six quarterings contain pen-and-ink tricked charges (with tiny red tricking dots): Row 1 Col 2 (two engrailed bendlets), Row 1 Col 4 (two lions passant in pale with a crescent in sinister chief), Row 2 Col 1 (three chess rooks, 2 and 1), Row 2 Col 2 (a saltire engrailed between four mullets), Row 2 Col 4 (two faint diagonal strokes), Row 3 Col 1 (a plain voided cross with a faint sketch in sinister chief), and Row 3 Col 4 (a lion rampant).",
        "figures": [
            {
                "fig_id": "fig_c389_1",
                "label": "Unfinished 20-Quartering Heraldic Achievement Cartouche",
                "desc": "Large pen-and-ink and yellow-ochre wash Renaissance strapwork cartouche enclosing a 5-column by 4-row grid of 20 quarterings. Most quarters are blank; tricked pen-and-ink charges appear in Row 1 Col 2 (two engrailed bendlets), Row 1 Col 4 (two lions passant in pale with a crescent in sinister chief), Row 2 Col 1 (three chess rooks, 2 and 1), Row 2 Col 2 (a saltire engrailed between four mullets), Row 2 Col 4 (two faint diagonal strokes), Row 3 Col 1 (a voided cross with a faint sketch in sinister chief), and Row 3 Col 4 (a lion rampant), with occasional red tricking dots.",
                "ulx": 760,
                "uly": 2300,
                "lrx": 3740,
                "lry": 5820,
            }
        ],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 760,
                "uly": 2300,
                "lrx": 3740,
                "lry": 5820,
                "lines": make_lines("c0389", 389, "main", 760, 2300, 3740, 5820, [
                    (1, "note", "[No text — heraldic shield cartouche only]", "[No text — unfinished 20-quartering heraldic achievement cartouche only]", "Pen-and-ink and yellow-ochre wash Renaissance strapwork cartouche with a 5x4 grid of 20 quarterings, 6-7 of which contain tricked heraldic charges (see figures)."),
                ]),
            }
        ],
    },
]
