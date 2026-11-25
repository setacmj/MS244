#!/usr/bin/env python3
"""
Pages Batch 73 (Canvases 394-397, Armorial & Genealogical Pedigrees) for Wellcome MS.244.
Covers four pages of the Armorial section:
  - Canvas 394 (Verso): Blazon notes for Warwickshire/Midlands arms (Birmingham, Frevill, Astley, Marshall, Bromsley)
  - Canvas 395 (Recto): Armorial grid (5x6 shields) of arms featuring a plain cross charged with five charges
  - Canvas 396 (Verso): Blank verso showing bleed-through of Canvas 395's armorial grid
  - Canvas 397 (Recto): Armorial grid (5x6 shields) of arms featuring a plain cross between four charges
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


PAGES_BATCH73 = [
    {
        "page_id": "c0394_v",
        "canvas_num": 394,
        "jp2": "b19608652_MS_244_0394.JP2",
        "orig_page": "Unnumbered",
        "folio_side": "Verso",
        "width": 5500,
        "height": 7312,
        "frame_box": [2000, 480, 5150, 1280],
        "center_rule_x": None,
        "summary": "Armorial verso: Five lines of heraldic blazon notes in Early Modern English shorthand at the top of the leaf, recording arms in Birmingham (Birmingham quartering Frevill, Astley, Marshall, Birmingham 'the name off the towne', and Bromsley). The rest of the leaf is blank, showing bleed-through from the recto and pin-prick transfer holes.",
        "figures": [],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 2000,
                "uly": 480,
                "lrx": 5150,
                "lry": 1280,
                "lines": make_lines("c0394_v", 394, "main", 2000, 480, 5150, 1280, [
                    (1, "body", "In Birmingam Birmingha[m] q[ua]rter [with?] [Bo?] frevill . o. + flory gu . 5 lozenge very a b .", "In Birmingham: Birmingham quartering [with?] Frevill: Or, a cross flory Gules; 5 lozenges vair Argent and Azure.", "'In Birmingam' is underlined. Uses heraldic tricking abbreviations: 'o.' (Or), '+' (cross), 'gu.' (Gules), 'a b.' (Argent and Blue/Azure)."),
                    (2, "body", "Astley . B [5?] foyles or .", "Astley: Azure, [5?] cinquefoils Or.", "'B' denotes Blue (Azure)."),
                    (3, "body", "Marshall . B. S. losenge in bend o . on cheef a[rgent] iii gu .", "Marshall: Azure and Sable, lozengy in bend Or; on a chief Argent three [charges] Gules.", "Heraldic shorthand: 'B. S.' (Blue/Azure and Sable), 'o.' (Or), 'gu.' (Gules)."),
                    (4, "body", "Birmingham . a . b . indented per pale . the name off the towne /", "Birmingham: Argent and Azure, per pale indented; the name of the town.", "Refers to the canting/territorial arms of Bermingham/Birmingham."),
                    (5, "body", "Bromsley . a . on 2 bars g . 6 martlett[es] o . 3 . 3 .", "Bromsley: Argent, on 2 bars Gules 6 martlets Or, 3 and 3.", "Terminal '-es' on 'martlett[es]' indicated by suspension/tilde."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0395_r",
        "canvas_num": 395,
        "jp2": "b19608652_MS_244_0395.JP2",
        "orig_page": "Unnumbered",
        "folio_side": "Recto",
        "width": 5128,
        "height": 7312,
        "frame_box": [360, 450, 4450, 6680],
        "center_rule_x": None,
        "summary": "Armorial recto: A 5x6 grid of 30 shield outlines arranged thematically by ordinary (a plain cross charged with five charges). Twenty-one shields are emblazoned in watercolour/ink and nineteen bear family labels above; three shields in Row 5 are blank outlines (two with labels) and all five shields in Row 6 are blank outlines.",
        "figures": [
            {
                "fig_id": "fig_c395_row1",
                "label": "Armorial Shields Row 1 (5 emblazoned shields)",
                "desc": "Row 1 (L-R): [Unlabelled] Argent a cross Gules charged with 5 mullets Argent; Aboloyne (Argent a cross Sable charged with 5 eagles displayed Argent); Birlingham (Or a cross Gules charged with 5 fleurs-de-lis Argent); Boynton (Or a cross Sable charged with 5 bull's heads erased Argent); Bygod (Or a cross Gules charged with 5 plates).",
                "ulx": 380,
                "uly": 580,
                "lrx": 4380,
                "lry": 1520,
            },
            {
                "fig_id": "fig_c395_row2",
                "label": "Armorial Shields Row 2 (4 emblazoned shields, 1 blank outline)",
                "desc": "Row 2 (L-R): [Unlabelled] Or a cross Gules charged with 5 escallops Argent; Cornwall devon (Argent a cross Sable charged with 5 bezants); Criktoftes (Azure a cross Argent charged with 5 escallops Gules); Durtynt Essex (blank outline); Digges kent (Gules a cross Argent charged with 5 eagles displayed Sable).",
                "ulx": 380,
                "uly": 1680,
                "lrx": 4380,
                "lry": 2620,
            },
            {
                "fig_id": "fig_c395_row3",
                "label": "Armorial Shields Row 3 (5 emblazoned shields)",
                "desc": "Row 3 (L-R): Ellis (Or a cross Sable charged with 5 crescents Argent); fronyll wig (Or a cross Gules charged with 4 lozenges Argent and 1 lozenge vair); Lincolne (Argent a cross Azure charged with 5 estoiles Or); Lacer (Or a cross Azure charged with 5 roses Argent); newent (Sable a cross Argent charged with 5 eagles displayed Sable).",
                "ulx": 380,
                "uly": 2740,
                "lrx": 4380,
                "lry": 3680,
            },
            {
                "fig_id": "fig_c395_row4",
                "label": "Armorial Shields Row 4 (5 emblazoned shields)",
                "desc": "Row 4 (L-R): Randolph (Gules a cross Argent charged with 5 mullets Sable); Russell (Or a cross Sable charged with 5 mullets Argent); St Albons town (Ermine a cross Gules charged with 5 bezants); Thrimplington (Argent a cross Gules charged with 5 escallops Argent); Stoneham (Argent a cross Sable charged with 5 escallops Or).",
                "ulx": 380,
                "uly": 3800,
                "lrx": 4380,
                "lry": 4720,
            },
            {
                "fig_id": "fig_c395_row5",
                "label": "Armorial Shields Row 5 (2 emblazoned shields, 3 blank outlines)",
                "desc": "Row 5 (L-R): Weyland (blank outline); Wickforde (Or a cross Gules charged with 5 lions rampant Argent); wale (Argent a cross Sable charged with 5 lions rampant Argent); Verney (blank outline); [Unlabelled] (blank outline with faint sketched cross).",
                "ulx": 380,
                "uly": 4840,
                "lrx": 4380,
                "lry": 5760,
            },
            {
                "fig_id": "fig_c395_row6",
                "label": "Armorial Shields Row 6 (5 blank shield outlines)",
                "desc": "Row 6 (L-R): Five blank unlabelled shield outlines.",
                "ulx": 380,
                "uly": 5860,
                "lrx": 4380,
                "lry": 6660,
            },
        ],
        "columns": [
            {
                "col_id": "col1",
                "col_label": "Shield Column 1 Labels",
                "ulx": 380,
                "uly": 450,
                "lrx": 1160,
                "lry": 4900,
                "lines": make_lines("c0395_r", 395, "col1", 380, 450, 1160, 4900, [
                    (1, "marginalia", "[Unlabelled]", "[Unlabelled shield]", "Row 1, Col 1: Argent, on a cross Gules 5 mullets Argent (the uppermost pierced)."),
                    (2, "marginalia", "[Unlabelled]", "[Unlabelled shield]", "Row 2, Col 1: Or, on a cross Gules 5 escallops Argent."),
                    (3, "heading", "Ellis", "Ellis", "Row 3, Col 1: Or, on a cross Sable 5 crescents Argent."),
                    (4, "heading", "Randolph", "Randolph", "Row 4, Col 1: Gules, on a cross Argent 5 mullets Sable."),
                    (5, "heading", "Weyland .", "Weyland", "Row 5, Col 1: Blank shield outline."),
                ]),
            },
            {
                "col_id": "col2",
                "col_label": "Shield Column 2 Labels",
                "ulx": 1160,
                "uly": 450,
                "lrx": 1960,
                "lry": 4900,
                "lines": make_lines("c0395_r", 395, "col2", 1160, 450, 1960, 4900, [
                    (1, "heading", "Aboloyne", "Aboloyne", "Row 1, Col 2: Argent, on a cross Sable 5 eagles displayed Argent."),
                    (2, "heading", "Cornwall devo[n]", "Cornwall (Devon)", "Row 2, Col 2: Argent, on a cross Sable 5 bezants."),
                    (3, "heading", "fronyll . wig[orn]", "Fronyll (Worcestershire)", "Row 3, Col 2: Or, on a cross Gules 4 lozenges Argent and in chief 1 lozenge vair (cf. Frevill)."),
                    (4, "heading", "Russell", "Russell", "Row 4, Col 2: Or, on a cross Sable 5 mullets Argent."),
                    (5, "heading", "Wickforde", "Wickford", "Row 5, Col 2: Or, on a cross Gules 5 lions rampant Argent."),
                ]),
            },
            {
                "col_id": "col3",
                "col_label": "Shield Column 3 Labels",
                "ulx": 1960,
                "uly": 450,
                "lrx": 2760,
                "lry": 4900,
                "lines": make_lines("c0395_r", 395, "col3", 1960, 450, 2760, 4900, [
                    (1, "heading", "Birlingham", "Birlingham", "Row 1, Col 3: Or, on a cross Gules 5 fleurs-de-lis Argent."),
                    (2, "heading", "Criktoftes", "Criktoftes", "Row 2, Col 3: Azure, on a cross Argent 5 escallops Gules."),
                    (3, "heading", "Lincolne", "Lincoln", "Row 3, Col 3: Argent, on a cross Azure 5 estoiles Or."),
                    (4, "heading", "St Albons tow[n]", "St Albans Town", "Row 4, Col 3: Ermine, on a cross Gules 5 bezants."),
                    (5, "heading", "wale /", "Wale", "Row 5, Col 3: Argent, on a cross Sable 5 lions rampant Argent."),
                ]),
            },
            {
                "col_id": "col4",
                "col_label": "Shield Column 4 Labels",
                "ulx": 2760,
                "uly": 450,
                "lrx": 3560,
                "lry": 4900,
                "lines": make_lines("c0395_r", 395, "col4", 2760, 450, 3560, 4900, [
                    (1, "heading", "Boynton", "Boynton", "Row 1, Col 4: Or, on a cross Sable 5 bull's heads erased Argent."),
                    (2, "heading", "Durtynt Esse[x]", "Durtynt (Essex)", "Row 2, Col 4: Blank shield outline (cf. Durant of Essex)."),
                    (3, "heading", "Lacer", "Lacer", "Row 3, Col 4: Or, on a cross Azure 5 roses Argent."),
                    (4, "heading", "Thrimplington", "Thrimplington", "Row 4, Col 4: Argent, on a cross Gules 5 escallops Argent."),
                    (5, "heading", "Verney", "Verney", "Row 5, Col 4: Blank shield outline."),
                ]),
            },
            {
                "col_id": "col5",
                "col_label": "Shield Column 5 Labels",
                "ulx": 3560,
                "uly": 450,
                "lrx": 4380,
                "lry": 4900,
                "lines": make_lines("c0395_r", 395, "col5", 3560, 450, 4380, 4900, [
                    (1, "heading", "Bygod", "Bigod", "Row 1, Col 5: Or, on a cross Gules 5 plates."),
                    (2, "heading", "Digges kent", "Digges (Kent)", "Row 2, Col 5: Gules, on a cross Argent 5 eagles displayed Sable."),
                    (3, "heading", "newent .", "Newent", "Row 3, Col 5: Sable, on a cross Argent 5 eagles displayed Sable."),
                    (4, "heading", "Stoneham", "Stoneham", "Row 4, Col 5: Argent, on a cross Sable 5 escallops Or."),
                    (5, "marginalia", "[Unlabelled]", "[Unlabelled blank shield]", "Row 5, Col 5: Blank shield outline with faint sketched cross."),
                ]),
            },
        ],
    },
    {
        "page_id": "c0396_v",
        "canvas_num": 396,
        "jp2": "b19608652_MS_244_0396.JP2",
        "orig_page": "Unnumbered",
        "folio_side": "Verso",
        "width": 5647,
        "height": 7312,
        "frame_box": [1100, 350, 5250, 6850],
        "center_rule_x": None,
        "summary": "Blank armorial verso (back of Canvas 395): Contains no original writing or drawings, showing only heavy mirror-image bleed-through of the 5x6 armorial shield grid and labels from Canvas 395, along with pin-prick transfer holes.",
        "figures": [],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 1100,
                "uly": 350,
                "lrx": 5250,
                "lry": 6850,
                "lines": make_lines("c0396_v", 396, "main", 1100, 350, 5250, 6850, [
                    (1, "marginalia", "[Blank verso; bleed-through from Canvas 395]", "[Blank verso; bleed-through from Canvas 395]", "No original text on this verso; shows mirror-image bleed-through of the 5x6 shield grid from Canvas 395 and pin-prick holes."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0397_r",
        "canvas_num": 397,
        "jp2": "b19608652_MS_244_0397.JP2",
        "orig_page": "Unnumbered",
        "folio_side": "Recto",
        "width": 5127,
        "height": 7312,
        "frame_box": [360, 450, 4450, 6680],
        "center_rule_x": None,
        "summary": "Armorial recto: A 5x6 grid of 30 shield positions arranged thematically by ordinary (a plain cross between four charges). Twenty shields are emblazoned in watercolour/ink and twenty-one bear family labels above (with 'kingston' in Row 3 Col 5 left blank/unpainted); Row 5 Cols 2-5 and all of Row 6 are blank shield outlines.",
        "figures": [
            {
                "fig_id": "fig_c397_row1",
                "label": "Armorial Shields Row 1 (5 emblazoned shields)",
                "desc": "Row 1 (L-R): Burnham (Sable a cross Argent between 4 crescents Argent); Burye (Argent a cross Sable between 4 martlets Sable); Cockfielde (Azure a cross Or between 4 cocks Or); Coupland Lond. (Or on a cross Sable between 4 oak leaves Vert 5 mullets Argent); Coggeshall Essex (Argent a cross Sable between 4 escallops Sable).",
                "ulx": 380,
                "uly": 580,
                "lrx": 4380,
                "lry": 1520,
            },
            {
                "fig_id": "fig_c397_row2",
                "label": "Armorial Shields Row 2 (5 emblazoned shields)",
                "desc": "Row 2 (L-R): Dalton (Argent a cross Azure between 4 ducks Vert); Dokesworth (Azure a cross Argent between 4 lions rampant Argent); Doaldoone (Argent a cross Vert between 4 martlets/popinjays Vert); Dabeney norff (Argent a cross Gules between 4 lions rampant Gules); Dabeney camb (Azure a cross Or between 4 lions rampant Or).",
                "ulx": 380,
                "uly": 1680,
                "lrx": 4380,
                "lry": 2620,
            },
            {
                "fig_id": "fig_c397_row3",
                "label": "Armorial Shields Row 3 (4 emblazoned shields, 1 blank)",
                "desc": "Row 3 (L-R): Frebant Buks. (Gules a cross Or between 4 groups of 3 cross-crosslets Or); flammocke corn (Argent a cross Gules between 4 mullets Gules pierced Or); Flyed (Argent on a cross Or 6 gouttes de sang between 4 birds Argent); Flote (Argent a cross Gules between 4 suns Gules); kingston (blank/unpainted).",
                "ulx": 380,
                "uly": 2740,
                "lrx": 4380,
                "lry": 3680,
            },
            {
                "fig_id": "fig_c397_row4",
                "label": "Armorial Shields Row 4 (5 emblazoned shields)",
                "desc": "Row 4 (L-R): Lyster yorks (Argent on a cross Argent 5 roundels Gules charged with suns Or between 4 martlets Argent); Merbery (Sable a cross Argent between 4 tau crosses Argent); Smyth (Argent on a cross Gules between 4 roses Gules 5 mullets Or); Traylie (Argent a cross Gules between 4 martlets Gules); wodhowse (Or a cross Gules between 4 groups of 3 cross-crosslets Gules).",
                "ulx": 380,
                "uly": 3800,
                "lrx": 4380,
                "lry": 4720,
            },
            {
                "fig_id": "fig_c397_row5",
                "label": "Armorial Shields Row 5 (1 emblazoned shield, 4 blank outlines)",
                "desc": "Row 5 (L-R): wybill (Gules a cross Argent between 4 six-pointed mullets Argent); Cols 2-5 (4 blank unlabelled shield outlines).",
                "ulx": 380,
                "uly": 4840,
                "lrx": 4380,
                "lry": 5760,
            },
            {
                "fig_id": "fig_c397_row6",
                "label": "Armorial Shields Row 6 (5 blank shield outlines)",
                "desc": "Row 6 (L-R): Five blank unlabelled shield outlines.",
                "ulx": 380,
                "uly": 5860,
                "lrx": 4380,
                "lry": 6660,
            },
        ],
        "columns": [
            {
                "col_id": "col1",
                "col_label": "Shield Column 1 Labels",
                "ulx": 380,
                "uly": 450,
                "lrx": 1160,
                "lry": 4900,
                "lines": make_lines("c0397_r", 397, "col1", 380, 450, 1160, 4900, [
                    (1, "heading", "Burnham", "Burnham", "Row 1, Col 1: Sable, a cross Argent between 4 crescents Argent."),
                    (2, "heading", "Dalton", "Dalton", "Row 2, Col 1: Argent, a cross Azure between 4 ducks Vert (beaked and legged Gules)."),
                    (3, "heading", "Frebant Buks.", "Frebant (Buckinghamshire)", "Row 3, Col 1: Gules, a cross Or between 4 groups of 3 cross-crosslets Or."),
                    (4, "heading", "Lyster yorks", "Lister (Yorkshire)", "Row 4, Col 1: Argent, on a cross of the field 5 roundels Gules charged with suns Or, between 4 martlets Argent."),
                    (5, "heading", "wybill", "Wyvill / Wybill", "Row 5, Col 1: Gules, a cross Argent between 4 six-pointed mullets Argent."),
                ]),
            },
            {
                "col_id": "col2",
                "col_label": "Shield Column 2 Labels",
                "ulx": 1160,
                "uly": 450,
                "lrx": 1960,
                "lry": 3900,
                "lines": make_lines("c0397_r", 397, "col2", 1160, 450, 1960, 3900, [
                    (1, "heading", "Burye", "Bury", "Row 1, Col 2: Argent, a cross Sable between 4 martlets Sable."),
                    (2, "heading", "Dokesworth", "Dokesworth", "Row 2, Col 2: Azure, a cross Argent between 4 lions rampant Argent."),
                    (3, "heading", "flammocke corn", "Flamank / Flammock (Cornwall)", "Row 3, Col 2: Argent, a cross Gules between 4 mullets Gules pierced Or."),
                    (4, "heading", "Merbery", "Merbury / Marbury", "Row 4, Col 2: Sable, a cross Argent between 4 tau crosses Argent."),
                ]),
            },
            {
                "col_id": "col3",
                "col_label": "Shield Column 3 Labels",
                "ulx": 1960,
                "uly": 450,
                "lrx": 2760,
                "lry": 3900,
                "lines": make_lines("c0397_r", 397, "col3", 1960, 450, 2760, 3900, [
                    (1, "heading", "Cockfielde", "Cockfield", "Row 1, Col 3: Azure, a cross Or between 4 cocks Or (canting arms)."),
                    (2, "heading", "Doaldoone .", "Doaldoone", "Row 2, Col 3: Argent, a cross Vert between 4 popinjays/martlets Vert."),
                    (3, "heading", "Flyed", "Flyed", "Row 3, Col 3: Argent, on a cross Or 6 gouttes de sang, between 4 birds Argent."),
                    (4, "heading", "Smyth", "Smyth", "Row 4, Col 3: Argent, on a cross Gules between 4 roses Gules 5 mullets Or."),
                ]),
            },
            {
                "col_id": "col4",
                "col_label": "Shield Column 4 Labels",
                "ulx": 2760,
                "uly": 450,
                "lrx": 3560,
                "lry": 3900,
                "lines": make_lines("c0397_r", 397, "col4", 2760, 450, 3560, 3900, [
                    (1, "heading", "Coupland . Lond .", "Coupland (London)", "Row 1, Col 4: Or, on a cross Sable between 4 oak leaves Vert 5 mullets Argent."),
                    (2, "heading", "Dabeney norff", "Daubeney (Norfolk)", "Row 2, Col 4: Argent, a cross Gules between 4 lions rampant Gules."),
                    (3, "heading", "Flote", "Flote", "Row 3, Col 4: Argent, a cross Gules between 4 suns in splendour Gules."),
                    (4, "heading", "Traylie", "Trailly / Traylie", "Row 4, Col 4: Argent, a cross Gules between 4 martlets Gules."),
                ]),
            },
            {
                "col_id": "col5",
                "col_label": "Shield Column 5 Labels",
                "ulx": 3560,
                "uly": 450,
                "lrx": 4380,
                "lry": 3900,
                "lines": make_lines("c0397_r", 397, "col5", 3560, 450, 4380, 3900, [
                    (1, "heading", "Coggeshall Esse[x]", "Coggeshall (Essex)", "Row 1, Col 5: Argent, a cross Sable between 4 escallops Sable."),
                    (2, "heading", "Dabeney camb", "Daubeney (Cambridgeshire)", "Row 2, Col 5: Azure, a cross Or between 4 lions rampant Or."),
                    (3, "heading", "kingston", "Kingston", "Row 3, Col 5: Label only; shield left blank/unpainted."),
                    (4, "heading", "wodhowse /", "Woodhouse", "Row 4, Col 5: Or, a cross Gules between 4 groups of 3 cross-crosslets Gules."),
                ]),
            },
        ],
    },
]
