#!/usr/bin/env python3
"""
Pages Batch 80 (Canvases 428-432) for Wellcome MS.244.
Covers the end of the Armorial & Genealogical Pedigrees section and the opening back flyleaves:
  - Canvas 428: Genealogical pedigree of the Talbot family (Earls of Shrewsbury & Talbots of Grafton, dated 1601) with a central note on the Beaufort/Somerset coheirs
  - Canvas 429: Armorial grid ('B' surnames: Bray to Batayll), with 9 emblazoned coats of arms and 1 faint sketch
  - Canvas 430: Blank verso of the 'B' Armorial leaf (with show-through from Canvas 429 and conservation repairs)
  - Canvas 431: Blank back flyleaf (recto)
  - Canvas 432: Blank back flyleaf (verso)
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


PAGES_BATCH80 = [
    {
        "page_id": "c0428_pedigree_talbot",
        "canvas_num": 428,
        "jp2": "b19608652_MS_244_0428.JP2",
        "orig_page": "Unnumbered (Pedigree)",
        "folio_side": "Verso (unnumbered)",
        "width": 5656,
        "height": 7312,
        "frame_box": [1250, 380, 5350, 6680],
        "center_rule_x": None,
        "summary": "Genealogical pedigree of the Talbot family (Earls of Shrewsbury and Talbots of Grafton, dated 1601 at the foot), drawn in pen-and-ink roundels linked by marriage and descent lines (including a hatched/crenellated descent line for the Grafton/Albrighton branch). Includes 5 blank roundels in the upper-middle area and a 7-line historical note in the centre detailing the marriage and coheirs of Edmund Beaufort, Duke of Somerset, and Eleanor, daughter of Richard Beauchamp, Earl of Warwick. No original page number is visible.",
        "figures": [
            {
                "fig_id": "fig_c428_1",
                "label": "Talbot Genealogical Pedigree Diagram",
                "desc": "Full-page pen-and-ink genealogical tree of 36 circular roundels (31 inscribed, 5 left blank) tracing the descendants of John Talbot, Earl of Shrewsbury, through the Earls of Shrewsbury (left) and the Talbots of Grafton and Albrighton down to 1601 (right).",
                "ulx": 1350,
                "uly": 420,
                "lrx": 5320,
                "lry": 6640,
            }
        ],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Pedigree Roundels & Central Note",
                "ulx": 1350,
                "uly": 1000,
                "lrx": 5320,
                "lry": 6640,
                "lines": make_lines("c428", 428, "main", 1350, 1000, 5320, 6640, [
                    (1, "body", "James Talbot. 2. Su[n]ne of Jhon E of Sallop.", "James Talbot, 2nd son of John, Earl of Salop [Shrewsbury].", "Upper row, roundel 1 (leftmost)."),
                    (2, "body", "Jhon Earle off Swewesbury", "John, Earl of Shrewsbury.", "Upper row, roundel 2; 'Swewesbury' is a scribal spelling of Shrewsbury."),
                    (3, "body", "daughter of the Duk off Buckinghame", "Daughter of the Duke of Buckingham.", "Upper row, roundel 3; married to John, Earl of Shrewsbury."),
                    (4, "body", "Elizabeth daughter of Randall Baro[n] of Greystock.", "Elizabeth, daughter of Randall [Ranulph], Baron of Greystoke.", "Upper row, roundel 4; first wife of Gilbert Talbot."),
                    (5, "body", "Gilberte Talbott. 3. Su[n] of John. E. of Sallop", "Gilbert Talbot, 3rd son of John, Earl of Salop [Shrewsbury].", "Upper row, roundel 5."),
                    (6, "body", "daughter of Cotton esquier.", "Daughter of Cotton, esquire.", "Upper row, roundel 6; second wife of Gilbert Talbot."),
                    (7, "body", "Cristopher 4 Sunne", "Christopher, 4th son.", "Row 2, roundel below John, Earl of Shrewsbury."),
                    (8, "body", "George Talbott. 5. Sunne", "George Talbot, 5th son.", "Row 2, rightmost roundel."),
                    (9, "body", "Gibert Talbot off Grafton", "Gilbert Talbot of Grafton.", "Row 3, below Gilbert Talbot & Elizabeth Greystoke; 'Gibert' for Gilbert."),
                    (10, "body", "Anne daughter & heyre of Sir Will[ia]m Paston", "Anne, daughter and heir of Sir William Paston.", "Row 3, married to Gilbert Talbot of Grafton."),
                    (11, "body", "Elizabeth marryed to John Littleto[n]", "Elizabeth, married to John Littleton.", "Row 4, daughter of Gilbert Talbot of Grafton."),
                    (12, "body", "Marye to Asley of Pateshall in Stafforde sheare", "Mary, [married] to Astley of Patshull in Staffordshire.", "Row 4, daughter of Gilbert Talbot of Grafton."),
                    (13, "body", "ma[r]garet to Roberte Newporte", "Margaret, [married] to Robert Newport.", "Row 4, daughter of Gilbert Talbot of Grafton."),
                    (14, "marginalia", "Edmu[n]d Duke of Su[m]merset mar[ied] Aelionar widowe of Tho. Lo. Rose", "Edmund, Duke of Somerset, married Eleanor, widow of Thomas, Lord Ros,", "Central genealogical note, line 1 (in a smaller annotating hand)."),
                    (15, "marginalia", "daughter and Coheire to Ri. Beauchamp E. of War. by whom he had", "daughter and coheir to Richard Beauchamp, Earl of Warwick, by whom he had", "Central genealogical note, line 2."),
                    (16, "marginalia", "issue Henry D of Su[m]merset. and. 5 daughters y[a]t were his heires vizt.", "issue Henry, Duke of Somerset, and 5 daughters that were his heirs, namely:", "Central genealogical note, line 3."),
                    (17, "marginalia", "1 Marg[are]t mar[ied] to Hu[m]ph. Duke of Buck. Eliz. 2 to Sr Robert Lowis kn[ight]", "1. Margaret, married to Humphrey, Duke of Buckingham; Elizabeth, 2nd, to Sir Robert [Henry] Lewis, knight,", "Central genealogical note, line 4."),
                    (18, "marginalia", "of whom Ro. markam 3. to Sr Wm Paston. of whom Littleton", "of whom Robert Markham; 3rd, to Sir William Paston, of whom Littleton,", "Central genealogical note, line 5."),
                    (19, "marginalia", "Co. ut supra. 4 Aelinor to Sr Rob. Spencer of whom Hen. Cary Lo. Hunsdon", "coheir as above; 4th, Eleanor, to Sir Robert Spencer, of whom Henry Carey, Lord Hunsdon;", "Central genealogical note, line 6."),
                    (20, "marginalia", "5 Joan. to Lo hooth Irla[n]d:", "5th, Joan, to Lord Howth [of] Ireland.", "Central genealogical note, line 7."),
                    (21, "body", "daughter of Will[ia]m Lo Hastinges", "Daughter of William, Lord Hastings.", "Lower pedigree, left branch, first wife of George, Earl of Shrewsbury."),
                    (22, "body", "George Lo Talbott Earle of salop", "George, Lord Talbot, Earl of Salop [Shrewsbury].", "Lower pedigree, left branch, centre."),
                    (23, "body", "daughter and heyer of Sr Rich. Walden", "Daughter and heir of Sir Richard Walden.", "Lower pedigree, left branch, second wife of George, Earl of Shrewsbury."),
                    (24, "body", "margaret daughter and heyer of Addam Troutebeck.", "Margaret, daughter and heir of Adam Troutbeck.", "Lower pedigree, right branch, first wife of Sir John Talbot of Albrighton."),
                    (25, "body", "John Talbot of Aubrighton knight", "John Talbot of Albrighton, knight.", "Lower pedigree, right branch."),
                    (26, "body", "Elizabeth daughter of Wrotesly off wrottesley.", "Elizabeth, daughter of Wrottesley of Wrottesley.", "Lower pedigree, right branch, second wife of Sir John Talbot."),
                    (27, "body", "marryed to Henry perry E of Northu[m]berlande", "Married to Henry Percy, Earl of Northumberland.", "Child of George, Earl of Shrewsbury; 'perry' is a scribal slip for Percy."),
                    (28, "body", "margaret maryed to Henry. Earle off Cumberla[n]d", "Margaret, married to Henry, Earl of Cumberland.", "Child of George, Earl of Shrewsbury."),
                    (29, "body", "Annie", "Anne.", "Daughter of George, Earl of Shrewsbury and his second wife."),
                    (30, "body", "Sr [Will[ia]m struck through; John above] knighte Compton knighte", "Sir John [originally William] Compton, knight.", "'Willm' is struck through and 'John' interlined above in brown-red ink."),
                    (31, "body", "marye Daughter of the Lord Dacre of Gill esland.", "Mary, daughter of the Lord Dacre of Gilsland.", "First wife of Francis, Earl of Shrewsbury."),
                    (32, "body", "ffrauncis Earle off Shrewesbury", "Francis, Earl of Shrewsbury.", "Son of George, Earl of Shrewsbury."),
                    (33, "body", "Grace ye Daughter of Shakerley Esquier.", "Grace, the daughter of Shakerley, esquire.", "Second wife of Francis, Earl of Shrewsbury."),
                    (34, "body", "Elizabeth marryed to ye lo Dacres of Gilleslande", "Elizabeth, married to the Lord Dacres of Gilsland.", "Daughter of George, Earl of Shrewsbury."),
                    (35, "body", "Syr Jhon Talbot off Grafton knight", "Sir John Talbot of Grafton, knight.", "Right branch, son of Sir John Talbot of Albrighton."),
                    (36, "body", "ffraunce daughter of Gifford", "Frances, daughter of Gifford.", "Wife of Sir John Talbot of Grafton."),
                    (37, "body", "Jane marryed to sr George Bowes knight", "Jane, married to Sir George Bowes, knight.", "Right branch, daughter of Sir John Talbot of Grafton."),
                    (38, "body", "Jhon Talbot of Grafton anno d[o]m[ini] 1601.", "John Talbot of Grafton, A.D. 1601.", "Bottom-right roundel, dated 1601."),
                    (39, "body", "daughter of Sr Will[ia]m. Peter knight", "Daughter of Sir William Petre, knight.", "Bottom-right roundel, wife of John Talbot of Grafton."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0429_armorial_b",
        "canvas_num": 429,
        "jp2": "b19608652_MS_244_0429.JP2",
        "orig_page": "Unnumbered (Armorial B)",
        "folio_side": "Recto (unnumbered)",
        "width": 5082,
        "height": 7312,
        "frame_box": [430, 290, 4660, 6810],
        "center_rule_x": None,
        "summary": "Armorial grid (5 columns by 6 rows, 30 cells) for families beginning with 'B' (Bray to Batayll). Nine cells contain painted/emblazoned coats of arms in black and faded red/pink (Bracy, Bekeringe, Bamnue, Burgoyne, Banke, Bourgilam, Belsted, Blaknham, Borgat, Barkesworth — 10 painted cells in total) and one cell (Bemclere) contains a faint pencil/ink sketch of a beast. Top-right and bottom-right corners are torn and repaired with conservation paper.",
        "figures": [
            {
                "fig_id": "fig_c429_1",
                "label": "Arms of Bracy",
                "desc": "Painted coat of arms in Row 3, Col 4: quarterly per fess indented argent and sable, in the first quarter a martlet argent.",
                "ulx": 2770,
                "uly": 2580,
                "lrx": 3480,
                "lry": 3450,
            },
            {
                "fig_id": "fig_c429_2",
                "label": "Arms of Bekeringe",
                "desc": "Painted coat of arms in Row 4, Col 1: argent, a bend gules (faded pink/red).",
                "ulx": 500,
                "uly": 3530,
                "lrx": 1180,
                "lry": 4420,
            },
            {
                "fig_id": "fig_c429_3",
                "label": "Arms of Bamnue",
                "desc": "Painted coat of arms in Row 4, Col 2: argent, on a chief indented sable two cranes/storks argent.",
                "ulx": 1220,
                "uly": 3530,
                "lrx": 1950,
                "lry": 4100,
            },
            {
                "fig_id": "fig_c429_4",
                "label": "Arms of Burgoyne",
                "desc": "Painted coat of arms in Row 4, Col 3: gules (faded pink/red), a talbot passant argent.",
                "ulx": 2010,
                "uly": 3550,
                "lrx": 2700,
                "lry": 4420,
            },
            {
                "fig_id": "fig_c429_5",
                "label": "Arms of Banke",
                "desc": "Painted coat of arms in Row 4, Col 4: sable, a cross argent.",
                "ulx": 2780,
                "uly": 3550,
                "lrx": 3480,
                "lry": 4420,
            },
            {
                "fig_id": "fig_c429_6",
                "label": "Arms of Bourgilam",
                "desc": "Painted coat of arms in Row 5, Col 3: argent, a bend sable.",
                "ulx": 2030,
                "uly": 4540,
                "lrx": 2720,
                "lry": 5430,
            },
            {
                "fig_id": "fig_c429_7",
                "label": "Arms of Belsted",
                "desc": "Painted coat of arms in Row 5, Col 4: argent, three bars sable.",
                "ulx": 2780,
                "uly": 4540,
                "lrx": 3500,
                "lry": 5430,
            },
            {
                "fig_id": "fig_c429_8",
                "label": "Arms of Blakenham",
                "desc": "Painted coat of arms in Row 5, Col 5: argent, three bars gules (faded pink/red).",
                "ulx": 3550,
                "uly": 4540,
                "lrx": 4280,
                "lry": 5430,
            },
            {
                "fig_id": "fig_c429_9",
                "label": "Sketch of Arms of Bemclere",
                "desc": "Faint pencil/ink sketch of a lion or talbot in Row 6, Col 1.",
                "ulx": 500,
                "uly": 5560,
                "lrx": 1150,
                "lry": 6350,
            },
            {
                "fig_id": "fig_c429_10",
                "label": "Arms of Borgat",
                "desc": "Painted coat of arms in Row 6, Col 2: argent, three pallets sable.",
                "ulx": 1240,
                "uly": 5530,
                "lrx": 1950,
                "lry": 6430,
            },
            {
                "fig_id": "fig_c429_11",
                "label": "Arms of Barkesworth",
                "desc": "Painted coat of arms in Row 6, Col 4: argent, a bend gules (faded pink/red).",
                "ulx": 2800,
                "uly": 5530,
                "lrx": 3520,
                "lry": 6430,
            },
        ],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Armorial Grid (B Surnames)",
                "ulx": 450,
                "uly": 450,
                "lrx": 4350,
                "lry": 6400,
                "lines": make_lines("c429", 429, "main", 450, 450, 4350, 6400, [
                    (1, "heading", "Bray | Badyfforde | Blaby | Belesbye | Braunflete", "Bray | Badyfforde | Blaby | Belesbye | Braunflete", "Row 1 headers (all 5 shield cells blank)."),
                    (2, "heading", "Busett | Bensted | Bermingham | Braunspath | Bugge", "Busett | Bensted | Bermingham | Braunspath | Bugge", "Row 2 headers (all 5 shield cells blank)."),
                    (3, "heading", "Butuillen | Belaale | Besny | Bracy | Brasse wig.", "Butvillen | Belaale | Besny | Bracy | Brasse wig.", "Row 3 headers; Bracy has painted arms."),
                    (4, "heading", "Bekeringe | Bamnue | Burgoyne | Banke | Bekard", "Bekeringe | Bamnue | Burgoyne | Banke | Bekard", "Row 4 headers; Bekeringe, Bamnue, Burgoyne, and Banke have painted arms."),
                    (5, "heading", "Bremeffielde vide Gifford | Beche | Bourgilam | Belsted | Blak Blaknham", "Bremefield (see Gifford) | Beche | Bourgilam | Belsted | Blak[enham] Blakenham", "Row 5 headers; Bourgilam, Belsted, and Blakenham have painted arms."),
                    (6, "heading", "Bemclere Suf | Borgat Suff | Boytone Suff | Barkesworth Suff | Batayll", "Bemclere (Suffolk) | Borgat (Suffolk) | Boytone (Suffolk) | Barkesworth (Suffolk) | Batayll", "Row 6 headers; Bemclere has a faint sketch, Borgat and Barkesworth have painted arms."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0430_armorial_b_verso",
        "canvas_num": 430,
        "jp2": "b19608652_MS_244_0430.JP2",
        "orig_page": "Unnumbered (Armorial B verso)",
        "folio_side": "Verso (unnumbered, blank)",
        "width": 5657,
        "height": 7312,
        "frame_box": [1050, 220, 5400, 7100],
        "center_rule_x": None,
        "summary": "Blank verso of the 'B' Armorial leaf (Canvas 429). Shows heavy bleed-through of the ruled grid and painted coats of arms (Bracy, Banke, Burgoyne, Bamnue, Bekeringe, Belsted, Bourgilam, Borgat, Barkesworth) from the recto. Fore-edge tears at top-left and bottom-left are repaired with conservation paper.",
        "figures": [],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page (Blank)",
                "ulx": 1050,
                "uly": 220,
                "lrx": 5400,
                "lry": 7100,
                "lines": make_lines("c430", 430, "main", 1050, 220, 5400, 7100, [
                    (1, "note", "[Blank verso of the 'B' Armorial leaf, with heavy show-through from Canvas 429 and conservation paper repairs at the outer corners.]", "[Blank verso of the 'B' Armorial leaf, with heavy show-through from Canvas 429 and conservation paper repairs at the outer corners.]", "No manuscript text on this side."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0431_back_flyleaf_1r",
        "canvas_num": 431,
        "jp2": "b19608652_MS_244_0431.JP2",
        "orig_page": "Back Flyleaf 1r",
        "folio_side": "Back Flyleaf 1r (blank)",
        "width": 5086,
        "height": 7312,
        "frame_box": [350, 220, 4750, 7100],
        "center_rule_x": None,
        "summary": "Blank back flyleaf (recto) of unruled cream laid paper. Completely blank except for a tiny ink/rust speck near the centre and faint show-through of the armorial grid along the left gutter.",
        "figures": [],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page (Blank)",
                "ulx": 350,
                "uly": 220,
                "lrx": 4750,
                "lry": 7100,
                "lines": make_lines("c431", 431, "main", 350, 220, 4750, 7100, [
                    (1, "note", "[Blank back flyleaf (recto).]", "[Blank back flyleaf (recto).]", "Unruled laid paper, no text."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0432_back_flyleaf_1v",
        "canvas_num": 432,
        "jp2": "b19608652_MS_244_0432.JP2",
        "orig_page": "Back Flyleaf 1v",
        "folio_side": "Back Flyleaf 1v (blank)",
        "width": 5679,
        "height": 7312,
        "frame_box": [1100, 220, 5400, 7100],
        "center_rule_x": None,
        "summary": "Blank back flyleaf (verso) of unruled cream laid paper, with the fore-edge of the text block visible at the left and faint show-through from preceding leaves.",
        "figures": [],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page (Blank)",
                "ulx": 1100,
                "uly": 220,
                "lrx": 5400,
                "lry": 7100,
                "lines": make_lines("c432", 432, "main", 1100, 220, 5400, 7100, [
                    (1, "note", "[Blank back flyleaf (verso).]", "[Blank back flyleaf (verso).]", "Unruled laid paper, no text."),
                ]),
            }
        ],
    },
]
