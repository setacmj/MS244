#!/usr/bin/env python3
"""
Pages Batch 82 (Canvases 439-444) for Wellcome MS.244.
Covers the final binding edge views and end-of-volume reference / colour-checker shots:
  - Canvas 439: Book-block head edge view (spine at left, brass corner-pieces and bosses)
  - Canvas 440: Book-block tail edge view (spine at left, brass corner-pieces and bosses)
  - Canvas 441: End reference shot — Front cover with Wellcome Library scale bar and X-Rite ColorChecker Classic
  - Canvas 442: End reference shot — Manuscript page 7 ('Pultesses') with Wellcome Library scale bar and X-Rite ColorChecker Classic
  - Canvas 443: End reference shot — Front cover (blind-tooled calf with brass corner-pieces and central boss)
  - Canvas 444: End reference shot — Back cover (blind-tooled calf with brass corner-pieces and central boss, spine at right)
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


PAGES_BATCH82 = [
    {
        "page_id": "c0439_edge_head",
        "canvas_num": 439,
        "jp2": "b19608652_MS_244_0439.JP2",
        "orig_page": "Binding: Book-Block Edge (1)",
        "folio_side": "Binding: Book-Block Head Edge",
        "width": 5103,
        "height": 1585,
        "frame_box": [250, 180, 4850, 1420],
        "center_rule_x": None,
        "summary": "Book-block head edge view: horizontal photograph showing the leather spine at the left, the upper and lower boards fitted with brass corner-pieces and bosses, and the wavy, deckled paper edges of the text block.",
        "figures": [
            {
                "fig_id": "fig_c439_1",
                "label": "Book-Block Head Edge",
                "desc": "Horizontal photograph of the book-block head edge showing the leather spine, brass corner-pieces and bosses, and the wavy paper edges of the text block.",
                "ulx": 250,
                "uly": 180,
                "lrx": 4850,
                "lry": 1420,
            }
        ],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 250,
                "uly": 180,
                "lrx": 4850,
                "lry": 1420,
                "lines": make_lines("c0439", 439, "main", 250, 180, 4850, 1420, [
                    (1, "body", "[Book-block head edge view: leather spine at left, brass corner-pieces and bosses on boards, wavy paper edges]", "Book-block head edge view showing the leather spine at left, brass corner-pieces and bosses on the upper and lower boards, and the wavy paper edges of the text block.", "Digitisation binding and book-block edge photograph."),
                    (2, "note", "[No manuscript text visible]", "No manuscript text visible.", "End-of-volume binding documentation."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0440_edge_tail",
        "canvas_num": 440,
        "jp2": "b19608652_MS_244_0440.JP2",
        "orig_page": "Binding: Book-Block Edge (2)",
        "folio_side": "Binding: Book-Block Tail Edge",
        "width": 5103,
        "height": 1585,
        "frame_box": [250, 180, 4850, 1420],
        "center_rule_x": None,
        "summary": "Book-block tail edge view: horizontal photograph showing the leather spine at the left, the upper and lower boards fitted with brass corner-pieces and bosses, and the wavy paper edges of the text block.",
        "figures": [
            {
                "fig_id": "fig_c440_1",
                "label": "Book-Block Tail Edge",
                "desc": "Horizontal photograph of the book-block tail edge showing the leather spine, brass corner-pieces and bosses, and the wavy paper edges of the text block.",
                "ulx": 250,
                "uly": 180,
                "lrx": 4850,
                "lry": 1420,
            }
        ],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 250,
                "uly": 180,
                "lrx": 4850,
                "lry": 1420,
                "lines": make_lines("c0440", 440, "main", 250, 180, 4850, 1420, [
                    (1, "body", "[Book-block tail edge view: leather spine at left, brass corner-pieces and bosses on boards, wavy paper edges]", "Book-block tail edge view showing the leather spine at left, brass corner-pieces and bosses on the upper and lower boards, and the wavy paper edges of the text block.", "Digitisation binding and book-block edge photograph."),
                    (2, "note", "[No manuscript text visible]", "No manuscript text visible.", "End-of-volume binding documentation."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0441_ref_cover",
        "canvas_num": 441,
        "jp2": "b19608652_MS_244_0441.JP2",
        "orig_page": "Reference: Front Cover with Colour Checker",
        "folio_side": "End Reference: Front Cover & Colour Checker",
        "width": 5103,
        "height": 7312,
        "frame_box": [200, 180, 4900, 7180],
        "center_rule_x": None,
        "summary": "End reference shot: blind-tooled brown calf front cover (with five raised spine bands at left, brass corner-pieces, and central lozenge boss) overlaid with a Wellcome Library 25 cm / 10 inch scale ruler and an X-Rite ColorChecker Classic calibration chart.",
        "figures": [
            {
                "fig_id": "fig_c441_1",
                "label": "Front Cover with Colour Checker & Scale",
                "desc": "Front cover of the binding overlaid with 'The Wellcome Library' 25 cm / 10 inch scale bar and 'xrite colorchecker CLASSIC' 24-patch colour target.",
                "ulx": 200,
                "uly": 180,
                "lrx": 4900,
                "lry": 7180,
            }
        ],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 1250,
                "uly": 2900,
                "lrx": 2900,
                "lry": 7150,
                "lines": make_lines("c0441", 441, "main", 1250, 2900, 2900, 7150, [
                    (1, "body", "[End reference shot: front cover with 'The Wellcome Library' 25 cm / 10 inch scale bar and 'xrite colorchecker CLASSIC' target]", "End reference photograph of the front cover with the Wellcome Library 25 cm / 10 inch scale ruler and X-Rite ColorChecker Classic calibration chart.", "Digitisation colour and scale calibration shot."),
                    (2, "marginalia", "0 Cm 1 ... 25 / 0 Inch ... 10 / The Wellcome Library / xrite colorchecker CLASSIC", "0–25 cm / 0–10 inch / The Wellcome Library / X-Rite ColorChecker Classic", "Printed labels on the photographic scale ruler and colour calibration target."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0442_ref_page7",
        "canvas_num": 442,
        "jp2": "b19608652_MS_244_0442.JP2",
        "orig_page": "Reference: Page 7 with Colour Checker",
        "folio_side": "End Reference: Page 7 (Pultesses) & Colour Checker",
        "width": 5103,
        "height": 7312,
        "frame_box": [200, 150, 4900, 7180],
        "center_rule_x": None,
        "summary": "End reference shot: manuscript page 7 ('Pultesses', opening of the main recipe book) overlaid with a Wellcome Library 25 cm / 10 inch scale ruler and an X-Rite ColorChecker Classic calibration chart for colour and dimensional calibration.",
        "figures": [
            {
                "fig_id": "fig_c442_1",
                "label": "Page 7 ('Pultesses') with Colour Checker & Scale",
                "desc": "Reference shot of manuscript page 7 ('Pultesses') with 'The Wellcome Library' 25 cm / 10 inch scale bar and 'xrite colorchecker CLASSIC' target placed over the left and lower-centre area.",
                "ulx": 700,
                "uly": 2800,
                "lrx": 2400,
                "lry": 7150,
            }
        ],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 700,
                "uly": 2800,
                "lrx": 2400,
                "lry": 7150,
                "lines": make_lines("c0442", 442, "main", 700, 2800, 2400, 7150, [
                    (1, "body", "[End reference shot: manuscript page 7 ('Pultesses') with 'The Wellcome Library' 25 cm / 10 inch scale bar and 'xrite colorchecker CLASSIC' target]", "End reference photograph of manuscript page 7 ('Pultesses') with the Wellcome Library 25 cm / 10 inch scale ruler and X-Rite ColorChecker Classic calibration chart.", "Digitisation colour and scale calibration shot over page 7 (transcribed in full in its main sequence)."),
                    (2, "marginalia", "0 Cm 1 ... 25 / 0 Inch ... 10 / The Wellcome Library / xrite colorchecker CLASSIC", "0–25 cm / 0–10 inch / The Wellcome Library / X-Rite ColorChecker Classic", "Printed labels on the photographic scale ruler and colour calibration target."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0443_ref_front_cover",
        "canvas_num": 443,
        "jp2": "b19608652_MS_244_0443.JP2",
        "orig_page": "Reference: Front Cover",
        "folio_side": "End Reference: Front Cover",
        "width": 5103,
        "height": 7312,
        "frame_box": [240, 180, 4880, 7140],
        "center_rule_x": None,
        "summary": "End reference shot: full view of the blind-tooled dark brown calf front cover (with five raised spine bands at left), fitted with brass corner-pieces with bosses and a central lozenge-shaped brass boss.",
        "figures": [
            {
                "fig_id": "fig_c443_1",
                "label": "Front Cover (Full View)",
                "desc": "Blind-tooled dark brown calf front cover with five raised bands on the spine at left, four brass corner-pieces with bosses, and a central diamond-shaped brass boss.",
                "ulx": 240,
                "uly": 180,
                "lrx": 4880,
                "lry": 7140,
            }
        ],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 240,
                "uly": 180,
                "lrx": 4880,
                "lry": 7140,
                "lines": make_lines("c0443", 443, "main", 240, 180, 4880, 7140, [
                    (1, "body", "[End reference shot: blind-tooled brown calf front cover with brass corner-pieces and central lozenge boss, spine at left]", "End reference photograph of the blind-tooled brown calf front cover with brass corner-pieces and central lozenge boss, spine at left.", "Digitisation binding reference photograph."),
                    (2, "note", "[No manuscript text visible]", "No manuscript text visible.", "End-of-volume binding documentation."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0444_ref_back_cover",
        "canvas_num": 444,
        "jp2": "b19608652_MS_244_0444.JP2",
        "orig_page": "Reference: Back Cover",
        "folio_side": "End Reference: Back Cover",
        "width": 5103,
        "height": 7312,
        "frame_box": [240, 180, 4880, 7140],
        "center_rule_x": None,
        "summary": "End reference shot: full view of the blind-tooled dark brown calf back cover (with five raised spine bands at right), fitted with brass corner-pieces with bosses and a central lozenge-shaped brass boss.",
        "figures": [
            {
                "fig_id": "fig_c444_1",
                "label": "Back Cover (Full View)",
                "desc": "Blind-tooled dark brown calf back cover with five raised bands on the spine at right, four brass corner-pieces with bosses, and a central diamond-shaped brass boss.",
                "ulx": 240,
                "uly": 180,
                "lrx": 4880,
                "lry": 7140,
            }
        ],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 240,
                "uly": 180,
                "lrx": 4880,
                "lry": 7140,
                "lines": make_lines("c0444", 444, "main", 240, 180, 4880, 7140, [
                    (1, "body", "[End reference shot: blind-tooled brown calf back cover with brass corner-pieces and central lozenge boss, spine at right]", "End reference photograph of the blind-tooled brown calf back cover with brass corner-pieces and central lozenge boss, spine at right.", "Digitisation binding reference photograph."),
                    (2, "note", "[No manuscript text visible]", "No manuscript text visible.", "End-of-volume binding documentation."),
                ]),
            }
        ],
    },
]
