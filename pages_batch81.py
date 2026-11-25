#!/usr/bin/env python3
"""
Pages Batch 81 (Canvases 433-438) for Wellcome MS.244.
Covers the blank back flyleaves, inside back pastedown, and exterior binding views:
  - Canvas 433: Blank back flyleaf (recto)
  - Canvas 434: Blank back flyleaf (verso) with fore-edge of book-block
  - Canvas 435: Inside back cover pastedown (blank)
  - Canvas 436: Binding: Back cover (blind-tooled leather with brass corner and centre bosses)
  - Canvas 437: Binding: Spine (five raised bands)
  - Canvas 438: Binding: Fore-edge of book-block
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


PAGES_BATCH81 = [
    {
        "page_id": "c0433_back_flyleaf_r",
        "canvas_num": 433,
        "jp2": "b19608652_MS_244_0433.JP2",
        "orig_page": "Back flyleaf (recto)",
        "folio_side": "Back flyleaf (recto)",
        "width": 5070,
        "height": 7312,
        "frame_box": [350, 380, 4700, 7100],
        "center_rule_x": None,
        "summary": "Blank modern conservation back flyleaf (recto). Clean cream paper with no text or foliation; brown leather turn-ins of the back board are visible at the top, right, and bottom edges.",
        "figures": [],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 350,
                "uly": 380,
                "lrx": 4700,
                "lry": 7100,
                "lines": make_lines("c0433", 433, "main", 350, 380, 4700, 7100, [
                    (1, "blank", "[Blank page]", "[Blank page]", "Modern conservation back flyleaf (recto); no manuscript text or page number."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0434_back_flyleaf_v",
        "canvas_num": 434,
        "jp2": "b19608652_MS_244_0434.JP2",
        "orig_page": "Back flyleaf (verso)",
        "folio_side": "Back flyleaf (verso)",
        "width": 5735,
        "height": 7312,
        "frame_box": [1100, 250, 5350, 7100],
        "center_rule_x": None,
        "summary": "Blank modern conservation back flyleaf (verso), with the fore-edge of the manuscript book-block visible along the left margin. No text or foliation.",
        "figures": [],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 1100,
                "uly": 250,
                "lrx": 5350,
                "lry": 7100,
                "lines": make_lines("c0434", 434, "main", 1100, 250, 5350, 7100, [
                    (1, "blank", "[Blank page]", "[Blank page]", "Modern conservation back flyleaf (verso); fore-edge of the book-block visible on the left."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0435_back_pastedown",
        "canvas_num": 435,
        "jp2": "b19608652_MS_244_0435.JP2",
        "orig_page": "Inside back pastedown",
        "folio_side": "Inside back pastedown",
        "width": 5085,
        "height": 7312,
        "frame_box": [420, 300, 4800, 7050],
        "center_rule_x": None,
        "summary": "Inside back cover pastedown of modern conservation paper, bordered by brown leather turn-ins at head, fore-edge, and tail. Completely blank.",
        "figures": [],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 420,
                "uly": 300,
                "lrx": 4800,
                "lry": 7050,
                "lines": make_lines("c0435", 435, "main", 420, 300, 4800, 7050, [
                    (1, "blank", "[Blank pastedown]", "[Blank pastedown]", "Inside back cover pastedown (modern conservation paper); no text or marks."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0436_back_cover",
        "canvas_num": 436,
        "jp2": "b19608652_MS_244_0436.JP2",
        "orig_page": "Binding: Back Cover",
        "folio_side": "Back Cover",
        "width": 5103,
        "height": 7312,
        "frame_box": [230, 220, 4880, 7110],
        "center_rule_x": None,
        "summary": "Exterior of the back cover: dark brown blind-tooled leather over boards with concentric rectangular fillets and roll-tooled borders, four brass L-shaped corner pieces with circular bosses, and a central lozenge-shaped brass boss.",
        "figures": [
            {
                "fig_id": "fig_c436_1",
                "label": "Back Cover Binding (Blind-Tooled Leather & Brass Bosses)",
                "desc": "Dark brown blind-tooled calfskin over boards, featuring concentric panel tooling, four brass corner bosses, and a central diamond/lozenge brass boss.",
                "ulx": 230,
                "uly": 220,
                "lrx": 4880,
                "lry": 7110,
            }
        ],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 230,
                "uly": 220,
                "lrx": 4880,
                "lry": 7110,
                "lines": make_lines("c0436", 436, "main", 230, 220, 4880, 7110, [
                    (1, "binding", "[Binding: Back cover]", "[Binding: Back cover]", "Dark brown blind-tooled leather over boards with brass corner pieces and central lozenge boss; no text."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0437_spine",
        "canvas_num": 437,
        "jp2": "b19608652_MS_244_0437.JP2",
        "orig_page": "Binding: Spine",
        "folio_side": "Spine",
        "width": 1932,
        "height": 7312,
        "frame_box": [500, 150, 1450, 7080],
        "center_rule_x": None,
        "summary": "Exterior view of the spine: reddish-brown leather with five raised bands forming six unlabelled compartments, with brass bosses projecting slightly at the board edges.",
        "figures": [
            {
                "fig_id": "fig_c437_1",
                "label": "Binding Spine",
                "desc": "Reddish-brown leather spine with five raised bands and six plain compartments.",
                "ulx": 500,
                "uly": 150,
                "lrx": 1450,
                "lry": 7080,
            }
        ],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 500,
                "uly": 150,
                "lrx": 1450,
                "lry": 7080,
                "lines": make_lines("c0437", 437, "main", 500, 150, 1450, 7080, [
                    (1, "binding", "[Binding: Spine]", "[Binding: Spine]", "Brown leather spine with five raised bands; no spine title or shelfmark label."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0438_fore_edge",
        "canvas_num": 438,
        "jp2": "b19608652_MS_244_0438.JP2",
        "orig_page": "Binding: Fore-edge",
        "folio_side": "Fore-edge",
        "width": 1932,
        "height": 7312,
        "frame_box": [380, 150, 1580, 7080],
        "center_rule_x": None,
        "summary": "Fore-edge view of the book-block showing the deckled/trimmed paper edges between the leather-covered boards and brass corner fittings.",
        "figures": [
            {
                "fig_id": "fig_c438_1",
                "label": "Book-Block Fore-Edge",
                "desc": "Fore-edge of the manuscript paper leaves between the front and back boards with brass corner fittings.",
                "ulx": 380,
                "uly": 150,
                "lrx": 1580,
                "lry": 7080,
            }
        ],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 380,
                "uly": 150,
                "lrx": 1580,
                "lry": 7080,
                "lines": make_lines("c0438", 438, "main", 380, 150, 1580, 7080, [
                    (1, "binding", "[Binding: Fore-edge of book-block]", "[Binding: Fore-edge of book-block]", "Fore-edge view of the paper leaves between the boards; no fore-edge title or markings."),
                ]),
            }
        ],
    },
]
