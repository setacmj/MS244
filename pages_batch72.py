#!/usr/bin/env python3
"""
Pages Batch 72 (Canvases 390-393, Armorial & Genealogical Pedigrees) for Wellcome MS.244.
Covers four unnumbered pages in the Armorial section:
  - Canvas 390 (Unnumbered verso): Largely blank verso with stray ink pen-trials ('H', 'Det'),
    lower-left ink blot, and show-through from the quartered achievement on Canvas 389.
  - Canvas 391 (Unnumbered recto): Ordinary of Crosses — 30 emblazoned shields in a 6x5 grid
    with family labels above each shield and French mottoes ('Rien sans trauayle : Sans trauay Rien') at head.
  - Canvas 392 (Unnumbered verso): 5-line historical and heraldic note on Edgar Atheling
    (Earl of Oxford, arms blazoned '.b. a crosse fleury 4 m[ar]let[es] o.'), with show-through from Canvas 391.
  - Canvas 393 (Unnumbered recto): Ordinary of Crosses (continued) — 8 emblazoned shields with
    family labels (Burforde to Barrett) and 22 blank pencil-drawn shield outlines in a 6x5 grid.
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


PAGES_BATCH72 = [
    {
        "page_id": "c0390_unnum_v",
        "canvas_num": 390,
        "jp2": "b19608652_MS_244_0390.JP2",
        "orig_page": "Unnumbered",
        "folio_side": "Verso",
        "width": 5693,
        "height": 7312,
        "frame_box": [1100, 300, 5350, 6950],
        "center_rule_x": None,
        "summary": "Unnumbered verso in the Armorial section: largely blank, showing faint show-through from the quartered achievement of arms and scroll cartouche on the recto (Canvas 389). Contains two stray ink pen-trials ('H' and 'Det') on the left side and a heavy black ink smudge/blot in the lower left.",
        "figures": [],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 1400,
                "uly": 2100,
                "lrx": 2200,
                "lry": 3400,
                "lines": make_lines("c0390", 390, "main", 1400, 2100, 2200, 3400, [
                    (1, "marginalia", "H", "H [pen trial]", "Stray capital 'H' written in ink on the left side, with an ink smear beneath."),
                    (2, "marginalia", "Det", "Det [pen trial]", "Stray ink pen trial ('Det') below the 'H', above a heavy black ink smudge in the lower left."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0391_unnum_r",
        "canvas_num": 391,
        "jp2": "b19608652_MS_244_0391.JP2",
        "orig_page": "Unnumbered",
        "folio_side": "Recto",
        "width": 5130,
        "height": 7312,
        "frame_box": [350, 320, 4550, 6750],
        "center_rule_x": None,
        "summary": "Unnumbered recto in the Armorial section (Ordinary of Crosses): headed by the French mottoes 'Rien sans trauayle : Sans trauay Rien'. Below is a 6-row by 5-column grid of 30 emblazoned shields, all bearing crosses of various tinctures and differences, with family names or heraldic labels written above each shield.",
        "figures": [
            {
                "fig_id": "fig_c0391_1",
                "label": "Armorial Grid: 30 Emblazoned Shields (Ordinary of Crosses)",
                "desc": "Six rows of five painted coats of arms (30 shields total), each featuring a cross (plain, ermine, checky, bendy, or charged with annulets, mullets, martlets, fleurs-de-lis, cinquefoils, or labels), with family names inscribed above each shield.",
                "ulx": 380,
                "uly": 620,
                "lrx": 4420,
                "lry": 6700,
            }
        ],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 380,
                "uly": 350,
                "lrx": 4450,
                "lry": 5650,
                "lines": make_lines("c0391", 391, "main", 380, 350, 4450, 5650, [
                    (1, "heading", "Rien sans trauayle :   Sans trauay Rien", "Nothing without labour : Without labour, nothing", "French mottoes written at top centre."),
                    (2, "body", "Latina Rex | Aton | Aylesburye | Wydale | Bourgh & vlster", "Latina Rex | Aton | Aylesbury | Wydale | Burgh & Ulster", "Row 1 shield labels: Argent a cross gules; Or/tarnished a cross sable; Azure a cross argent; Argent a cross sable an annulet in canton; Or a cross gules."),
                    (3, "body", "Boys buks | Edwyn | Uendall | Corkerith | Eyleston", "Boys (Bucks) | Edwyn | Vendall | Corkerith | Eyleston", "Row 2 shield labels: Argent a cross sable a canton ermine; Or a cross azure; Argent a cross vert; Argent a cross sable a mullet argent; Argent a cross sable a fleur-de-lis gules in canton."),
                    (4, "body", "haydorke | hartlawe | hussey wilt[es] | hallome | hauenell Suff", "Haydock | Hartlawe | Hussey (Wilts) | Hallome | Havenell (Suffolk)", "Row 3 shield labels: Argent a cross sable a fleur-de-lis sable in canton; Argent a cross gules a mullet sable in canton; Or a cross vert; Sable a cross ermine; Sable a cross tarnished or/argent."),
                    (5, "body", "harlton | Letham v. | Lortys dors | moltrys | Moresby", "Harlton | Letham v. | Lortys (Dorset) | Moltrys | Moresby", "Row 4 shield labels: Argent a cross gules a martlet sable in canton; Gules a cross ermine; Azure a cross or a martlet gules; Argent a cross sable charged with five pears/drops or; Sable a cross argent a cinquefoil argent in canton."),
                    (6, "body", "Opsale | Pigott | Peydon | Pysmyr | Pentshall", "Opsale | Pigott | Peydon | Pysmyr | Pentshall", "Row 5 shield labels: Sable a cross argent; Quarterly gules and sable a cross argent; Chequy argent and gules a cross azure; Vert a cross or; Or/tarnished a cross gules a label of three points azure."),
                    (7, "body", "Shortdiche | Stetsbye | Stangrey | Shelton norff: | Trevor", "Shortditch | Stetsby | Stangrey | Shelton (Norfolk) | Trevor", "Row 6 shield labels: Argent a cross gules a canton ermine; Argent a cross bendy gules and azure; Four cantons azure billetty argent a cross argent; Azure a cross or; Quarterly gules and argent a fess vair."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0392_unnum_v",
        "canvas_num": 392,
        "jp2": "b19608652_MS_244_0392.JP2",
        "orig_page": "Unnumbered",
        "folio_side": "Verso",
        "width": 5500,
        "height": 7312,
        "frame_box": [1800, 620, 5050, 1650],
        "center_rule_x": None,
        "summary": "Unnumbered verso in the Armorial section: contains a 5-line historical and heraldic note in secretary hand concerning Edgar Atheling, Earl of Oxford, with a blazon of his attributed arms ('.b. a crosse fleury 4 m[ar]let[es] o.'). Strong show-through from the 30 painted shields on Canvas 391 is visible across the page.",
        "figures": [],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 1820,
                "uly": 640,
                "lrx": 5020,
                "lry": 1620,
                "lines": make_lines("c0392", 392, "main", 1820, 640, 5020, 1620, [
                    (1, "body", "Edgar Athelinge Sunne to Edward le Exule and cosyn", "Edgar Atheling, son to Edward the Exile and cousin", "Written in neat 16th-century secretary hand with a calligraphic capital 'E'."),
                    (2, "body", "and heire to St Edward the confessor was at the tyme", "and heir to St Edward the Confessor, was at the time", ""),
                    (3, "body", "of the Conqueste Earle of Oxenforde wh[ich] Earldome he had", "of the Conquest Earl of Oxford, which earldom he had", ""),
                    (4, "body", "by the gifte of Harrold who toke from him the kingdome", "by the gift of Harold, who took from him the kingdom.", ""),
                    (5, "body", "he died in Scotland sanz yssue / . b. a crosse fleury 4 m[ar]let[es] o.", "He died in Scotland without issue. [Arms:] Azure, a cross fleury [between] 4 martlets Or.", "Heraldic trick/blazon using 'b.' (blue/azure) and 'o.' (or/gold)."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0393_unnum_r",
        "canvas_num": 393,
        "jp2": "b19608652_MS_244_0393.JP2",
        "orig_page": "Unnumbered",
        "folio_side": "Recto",
        "width": 5126,
        "height": 7312,
        "frame_box": [320, 480, 4450, 6700],
        "center_rule_x": None,
        "summary": "Unnumbered recto in the Armorial section (Ordinary of Crosses continued): 6-row by 5-column grid of 30 drawn shield outlines, of which the first 8 shields (Row 1 and the first three of Row 2) are emblazoned and labelled with family names (Burforde, Bruges, Coupell, Whityngham, Woxand, Villers, Veer, Barrett); the remaining 22 shields are blank pencil outlines.",
        "figures": [
            {
                "fig_id": "fig_c0393_1",
                "label": "Armorial Grid: 8 Emblazoned Shields & 22 Blank Shield Outlines",
                "desc": "Six rows of five shield outlines (30 total): Row 1 (5 shields) and Row 2 cols 1-3 (3 shields) are painted with crosses and labelled; the remaining 22 shields are blank pencil outlines awaiting emblazonment.",
                "ulx": 350,
                "uly": 650,
                "lrx": 4380,
                "lry": 6680,
            }
        ],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 350,
                "uly": 500,
                "lrx": 4350,
                "lry": 1950,
                "lines": make_lines("c0393", 393, "main", 350, 500, 4350, 1950, [
                    (1, "body", "Burforde | Bruges | Coupell | Whityngham | Woxand", "Burforde | Bruges | Coupell | Whityngham | Woxand", "Row 1 shield labels: Quarterly azure and gules a cross argent; Argent a cross sable a leopard's face or; Argent a cross sable a mullet argent; Argent a cross sable a martlet gules in canton; Argent a cross sable two crescents gules in chief."),
                    (2, "body", "Villers | Veer / | Barrett | [blank] | [blank]", "Villers | Veer | Barrett | [blank] | [blank]", "Row 2 shield labels (cols 1-3): Gules semy of billets argent a cross or; Argent a cross gules a label of five points argent; Argent a cross sable pierced in bend. Cols 4-5 and Rows 3-6 (22 shields) are blank pencil outlines."),
                ]),
            }
        ],
    },
]
