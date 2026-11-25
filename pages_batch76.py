#!/usr/bin/env python3
"""
Pages Batch 76 (Canvases 408-412, Armorial & Genealogical Pedigrees) for Wellcome MS.244.
Covers five pages of the Armorial and Pedigree section:
  - Canvas 408 (Verso): Blank verso showing bleed-through of preceding armorial grid
  - Canvas 409 (Recto): Armorial grid (5x6 shields) of families beginning with 'A' (9 emblazoned, 21 blank outlines)
  - Canvas 410 (Verso): Genealogical pedigree of the Percy family (Part 1: William Percy with the Conqueror to William Lord Percy & Isabel Bruce)
  - Canvas 411 (Recto): Blank pen-and-ink ruled pedigree grid (7 vertical x 8 horizontal lines)
  - Canvas 412 (Verso): Genealogical pedigree of the Percy family (Part 2: William Lord Percy & Ellen Spencer to Henry Percy, 1st Earl of Northumberland)
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


PAGES_BATCH76 = [
    {
        "page_id": "c0408_v",
        "canvas_num": 408,
        "jp2": "b19608652_MS_244_0408.JP2",
        "orig_page": "Unnumbered",
        "folio_side": "Verso",
        "width": 5649,
        "height": 7312,
        "frame_box": [1100, 250, 5350, 7000],
        "center_rule_x": None,
        "summary": "Armorial verso: Completely blank verso leaf showing faint bleed-through of the 5x6 armorial shield grid on the preceding recto (Canvas 407), scattered small wormholes, and a minor red pigment smudge near the upper gutter.",
        "figures": [],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 1100,
                "uly": 250,
                "lrx": 5350,
                "lry": 7000,
                "lines": make_lines("c0408_v", 408, "main", 1100, 250, 5350, 7000, [
                    (1, "marginalia", "[Blank verso]", "[Blank verso — no text on this side; shows bleed-through of the armorial grid on the preceding recto and minor wormholes.]", "Unnumbered blank verso in the armorial section."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0409_r",
        "canvas_num": 409,
        "jp2": "b19608652_MS_244_0409.JP2",
        "orig_page": "Unnumbered",
        "folio_side": "Recto",
        "width": 5132,
        "height": 7312,
        "frame_box": [350, 320, 4400, 6500],
        "center_rule_x": None,
        "summary": "Armorial recto: A 5x6 grid of 30 shield outlines for families beginning with the letter 'A'. Twenty shields in the top four rows carry family name headings above them, nine of which are emblazoned in watercolour and ink (Arden, Andbye, Aldrington/Almington, Anstie, Acworth, Annesley, Avenell, Andrewes, Aubemarle); the remaining eleven labelled shields and all ten shields in Rows 5-6 are blank outlines.",
        "figures": [
            {
                "fig_id": "fig_c409_row1",
                "label": "Armorial Shields Row 1 (4 emblazoned shields, 1 blank outline)",
                "desc": "Row 1 (L-R): Arden: ches: lan: (Gules, three cross-crosslets fitchée Or, a chief engrailed Or [tarnished]); Astley: (blank outline); Andbye (Gules, on a bend Or three martlets Sable); Aldrington / almington (Sable, three pairs of wings conjoined in lure Argent); Anstie: camb: (Or, a cross engrailed Gules between four martlets Gules).",
                "ulx": 380,
                "uly": 560,
                "lrx": 4300,
                "lry": 1460,
            },
            {
                "fig_id": "fig_c409_row2",
                "label": "Armorial Shields Row 2 (1 emblazoned shield, 4 blank outlines)",
                "desc": "Row 2 (L-R): Award of gipswich (blank outline); Aldwincle (blank outline); Austin norf: (blank outline); Acworth: suf: (Argent, a griffin segreant Sable armed and langued Gules); Aylmer (blank outline).",
                "ulx": 380,
                "uly": 1620,
                "lrx": 4300,
                "lry": 2520,
            },
            {
                "fig_id": "fig_c409_row3",
                "label": "Armorial Shields Row 3 (4 emblazoned shields, 1 blank outline)",
                "desc": "Row 3 (L-R): Apulderfelde kent: (blank outline); Annesley (Paly of six Argent and Purpure, a bend Gules); Auenell (Argent, a fess between six annulets Gules); Andrewes (Argent, a chevron engrailed Gules between three birds Sable); Aubemarle: (Gules, a bend of five lozenges conjoined Ermine).",
                "ulx": 380,
                "uly": 2680,
                "lrx": 4300,
                "lry": 3560,
            },
            {
                "fig_id": "fig_c409_row4",
                "label": "Armorial Shields Row 4 (5 blank shield outlines)",
                "desc": "Row 4 (L-R): Archas, Agmondesham, Aylewarde, Arnolde, Arderne (all five left as blank outlines).",
                "ulx": 380,
                "uly": 3720,
                "lrx": 4300,
                "lry": 4600,
            },
            {
                "fig_id": "fig_c409_row5",
                "label": "Armorial Shields Row 5 (5 blank shield outlines)",
                "desc": "Row 5 (L-R): Five blank unlabelled shield outlines.",
                "ulx": 380,
                "uly": 4720,
                "lrx": 4300,
                "lry": 5560,
            },
            {
                "fig_id": "fig_c409_row6",
                "label": "Armorial Shields Row 6 (5 blank shield outlines)",
                "desc": "Row 6 (L-R): Five blank unlabelled shield outlines.",
                "ulx": 380,
                "uly": 5660,
                "lrx": 4300,
                "lry": 6480,
            },
        ],
        "columns": [
            {
                "col_id": "col1",
                "col_label": "Shield Column 1 Labels",
                "ulx": 380,
                "uly": 340,
                "lrx": 1140,
                "lry": 3740,
                "lines": make_lines("c0409_r", 409, "col1", 380, 340, 1140, 3740, [
                    (1, "heading", "Arden: ches: lan:", "Arden (Cheshire, Lancashire)", "Row 1, Col 1: Gules, three cross-crosslets fitchée and a chief engrailed Or (chief tarnished)."),
                    (2, "heading", "Award of gipswich", "Award of Ipswich", "Row 2, Col 1: Blank shield outline."),
                    (3, "heading", "Apulderfelde kent:", "Apulderfelde (Kent)", "Row 3, Col 1: Blank shield outline; 'ul' in 'Apulderfelde' slightly blotted/corrected."),
                    (4, "heading", "Archas", "Archas", "Row 4, Col 1: Blank shield outline."),
                ]),
            },
            {
                "col_id": "col2",
                "col_label": "Shield Column 2 Labels",
                "ulx": 1140,
                "uly": 340,
                "lrx": 1920,
                "lry": 3740,
                "lines": make_lines("c0409_r", 409, "col2", 1140, 340, 1920, 3740, [
                    (1, "heading", "Astley:", "Astley", "Row 1, Col 2: Blank shield outline."),
                    (2, "heading", "Aldwincle", "Aldwincle", "Row 2, Col 2: Blank shield outline."),
                    (3, "heading", "Annesley", "Annesley", "Row 3, Col 2: Paly of six Argent and Purpure, a bend Gules."),
                    (4, "heading", "Agmondesham", "Agmondesham", "Row 4, Col 2: Blank shield outline."),
                ]),
            },
            {
                "col_id": "col3",
                "col_label": "Shield Column 3 Labels",
                "ulx": 1920,
                "uly": 340,
                "lrx": 2700,
                "lry": 3740,
                "lines": make_lines("c0409_r", 409, "col3", 1920, 340, 2700, 3740, [
                    (1, "heading", "Andbye", "Andbye", "Row 1, Col 3: Gules, on a bend Or three martlets Sable."),
                    (2, "heading", "Austin norf: o", "Austin (Norfolk)", "Row 2, Col 3: Blank shield outline."),
                    (3, "heading", "Auenell", "Avenell", "Row 3, Col 3: Argent, a fess between six annulets Gules."),
                    (4, "heading", "Aylewarde", "Aylewarde", "Row 4, Col 3: Blank shield outline."),
                ]),
            },
            {
                "col_id": "col4",
                "col_label": "Shield Column 4 Labels",
                "ulx": 2700,
                "uly": 340,
                "lrx": 3480,
                "lry": 3740,
                "lines": make_lines("c0409_r", 409, "col4", 2700, 340, 3480, 3740, [
                    (1, "heading", "Aldrington[e] / almington", "Aldrington / Almington", "Row 1, Col 4: Sable, three pairs of wings conjoined in lure Argent. Ending of 'Aldringtone' struck through and 'almington' written below."),
                    (2, "heading", "Acworth: suf:", "Acworth (Suffolk)", "Row 2, Col 4: Argent, a griffin segreant Sable armed and langued Gules."),
                    (3, "heading", "Andrewes", "Andrewes", "Row 3, Col 4: Argent, a chevron engrailed Gules between three birds Sable."),
                    (4, "heading", "Arnolde", "Arnolde", "Row 4, Col 4: Blank shield outline."),
                ]),
            },
            {
                "col_id": "col5",
                "col_label": "Shield Column 5 Labels",
                "ulx": 3480,
                "uly": 340,
                "lrx": 4300,
                "lry": 3740,
                "lines": make_lines("c0409_r", 409, "col5", 3480, 340, 4300, 3740, [
                    (1, "heading", "Anstie: camb:", "Anstie (Cambridgeshire)", "Row 1, Col 5: Or, a cross engrailed Gules between four martlets Gules."),
                    (2, "heading", "Aylmer", "Aylmer", "Row 2, Col 5: Blank shield outline."),
                    (3, "heading", "Aubemarle:", "Aubemarle", "Row 3, Col 5: Gules, a bend of five lozenges conjoined Ermine."),
                    (4, "heading", "Arderne", "Arderne", "Row 4, Col 5: Blank shield outline."),
                ]),
            },
        ],
    },
    {
        "page_id": "c0410_v",
        "canvas_num": 410,
        "jp2": "b19608652_MS_244_0410.JP2",
        "orig_page": "Unnumbered",
        "folio_side": "Verso",
        "width": 5649,
        "height": 7312,
        "frame_box": [1750, 500, 4950, 6500],
        "center_rule_x": None,
        "summary": "Genealogical pedigree (verso): Part 1 of the Percy family pedigree in pen-and-ink roundels and impaled shields, tracing five generations from William Percy ('came in with the Conqueror') and Emma de Porte through Alan Lord Percy, William Lord Percy, Agnes Percy (who married Joscelin of Louvain, 'for love of which lady he called his children Percy'), and Maud Percy (married to the Earl of Warwick), down to William Lord Percy and Isabel Bruce. Two shields feature tricked lions rampant.",
        "figures": [
            {
                "fig_id": "fig_c410_pedigree",
                "label": "Percy Family Pedigree Diagram (Part 1)",
                "desc": "Pen-and-ink genealogical chart of 10 linked marriage roundels and 6 impaled shields across 5 generations. Four shields are blank impaled outlines; the shield above Joscelin of Louvain & Agnes Percy shows a lion rampant in the dexter half, and the bottom shield below William Lord Percy & Isabel Bruce shows a lion rampant in the sinister half.",
                "ulx": 1750,
                "uly": 500,
                "lrx": 4950,
                "lry": 6500,
            }
        ],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Pedigree Roundels (Top to Bottom)",
                "ulx": 1750,
                "uly": 1280,
                "lrx": 4950,
                "lry": 5600,
                "lines": make_lines("c0410_v", 410, "main", 1750, 1280, 4950, 5600, [
                    (1, "body", "Will[ia]m Percy came in w[i]t[h] the Conq[ueror]", "William Percy came in with the Conqueror.", "Gen 1, left roundel. 'Willm' with macron; 'wt' with superscript 't'; 'Conqu' with suspension mark."),
                    (2, "body", "Emma de Porte Ladye of Scarborowe dau: of Hugh de Porte", "Emma de Porte, Lady of Scarborough, daughter of Hugh de Porte.", "Gen 1, right roundel."),
                    (3, "body", "Allen Lord Percye", "Alan Lord Percy", "Gen 2, left roundel."),
                    (4, "body", "Emma Sister of S[i]r Gilbert de gant", "Emma, sister of Sir Gilbert de Gant.", "Gen 2, right roundel."),
                    (5, "body", "Will[ia]m Lo Percy", "William Lord Percy", "Gen 3, left roundel."),
                    (6, "body", "Alice the daughter of Rosse", "Alice, the daughter of Rosse [Roos].", "Gen 3, right roundel."),
                    (7, "body", "Jocelyne Loueyne E. of Bruxels", "Joscelin [of] Louvain, Earl of Brussels.", "Gen 4, left branch, left roundel."),
                    (8, "body", "Agnes Percye for Love of w[hi]ch lady he called his Children percy", "Agnes Percy, for love of which lady he called his children Percy.", "Gen 4, left branch, right roundel."),
                    (9, "body", "Maude married to Earle off warwicke", "Maud, married to [the] Earl of Warwick.", "Gen 4, right branch, left roundel."),
                    (10, "body", "Maude", "Maud", "Gen 4, right branch, right roundel."),
                    (11, "body", "Will[ia]m Lo Percye", "William Lord Percy", "Gen 5, left roundel."),
                    (12, "body", "Issabell da. of S[i]r Ada[m] Bruse knight", "Isabel, daughter of Sir Adam Bruce, knight.", "Gen 5, right roundel. 'Ada[m]' with tilde over final 'a'."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0411_r",
        "canvas_num": 411,
        "jp2": "b19608652_MS_244_0411.JP2",
        "orig_page": "Unnumbered",
        "folio_side": "Recto",
        "width": 5132,
        "height": 7312,
        "frame_box": [350, 200, 4700, 6950],
        "center_rule_x": None,
        "summary": "Blank ruled pedigree grid (recto): Prepared in pen-and-ink with 7 vertical lines and 8 horizontal lines forming a grid for a genealogical pedigree or armorial chart, but left completely blank. Shows faint bleed-through of the Percy pedigree on Canvas 412 (verso) and minor wormholes.",
        "figures": [
            {
                "fig_id": "fig_c411_grid",
                "label": "Blank Ruled Pedigree Grid",
                "desc": "Pen-and-ink ruled grid (7 vertical lines, 8 horizontal lines) prepared for a genealogical pedigree or armorial chart, left unentered.",
                "ulx": 350,
                "uly": 200,
                "lrx": 4700,
                "lry": 6950,
            }
        ],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Full Page",
                "ulx": 350,
                "uly": 200,
                "lrx": 4700,
                "lry": 6950,
                "lines": make_lines("c0411_r", 411, "main", 350, 200, 4700, 6950, [
                    (1, "marginalia", "[Blank ruled grid]", "[Blank ruled grid — pen-and-ink pedigree/armorial grid with no text; shows bleed-through of the Percy pedigree on the verso (Canvas 412).]", "Prepared recto leaf left unused."),
                ]),
            }
        ],
    },
    {
        "page_id": "c0412_v",
        "canvas_num": 412,
        "jp2": "b19608652_MS_244_0412.JP2",
        "orig_page": "Unnumbered",
        "folio_side": "Verso",
        "width": 5649,
        "height": 7312,
        "frame_box": [1450, 250, 5050, 6900],
        "center_rule_x": None,
        "summary": "Genealogical pedigree (verso): Part 2 of the Percy family pedigree, continuing from Canvas 410. Traces five generations from William Lord Percy and Ellen Spencer, through Henry Lord Percy and Eleanor Warenne, their three sons (William, Henry 3rd son, John), Thomas Percy Bishop of Norwich (with a pen-and-ink bishop's mitre above his shield), Mary of Lancaster, Henry Lord Percy and Ida de Clifford, down to Henry Percy, 1st Earl of Northumberland, and his two wives (Margaret Neville and 'Jane' [recte Maud] Lucy, noting the condition of bearing the Lucy arms in the 2nd quarter).",
        "figures": [
            {
                "fig_id": "fig_c412_pedigree",
                "label": "Percy Family Pedigree Diagram (Part 2)",
                "desc": "Pen-and-ink genealogical chart of 16 linked roundels (13 inscribed, 3 blank) and 9 blank impaled shields across 5 generations, including a bishop's mitre drawn above the shield of Thomas Percy, Bishop of Norwich.",
                "ulx": 1450,
                "uly": 250,
                "lrx": 5050,
                "lry": 6900,
            }
        ],
        "columns": [
            {
                "col_id": "main",
                "col_label": "Pedigree Roundels (Top to Bottom)",
                "ulx": 1450,
                "uly": 380,
                "lrx": 5050,
                "lry": 6680,
                "lines": make_lines("c0412_v", 412, "main", 1450, 380, 5050, 6680, [
                    (1, "body", "Will[ia]m Lo Percy", "William Lord Percy", "Gen 1, left roundel (continuing from Canvas 410)."),
                    (2, "body", "Ellena daughter of spencer", "Ellen [Eleanor], daughter of [le De]spencer.", "Gen 1, right roundel."),
                    (3, "body", "Henrye Lord percy", "Henry Lord Percy", "Gen 2, left roundel."),
                    (4, "body", "Elionora daughter of Will[ia]m. Earle warren", "Eleanor, daughter of William, Earl Warenne.", "Gen 2, right roundel."),
                    (5, "body", "Will[ia]m Lo percy y[e] eldest sunne died sans issue", "William Lord Percy, the eldest son, died without issue.", "Gen 3, left branch, left roundel (paired with blank right roundel)."),
                    (6, "body", "Henrye Lo. percy. 3. Sunne", "Henry Lord Percy, 3rd son.", "Gen 3, middle branch, left roundel."),
                    (7, "body", "daughter off the Earle off Arondell", "Daughter of the Earl of Arundel.", "Gen 3, middle branch, right roundel."),
                    (8, "body", "Jhon Lord percy second su[n]n sanz issue", "John Lord Percy, second son, without issue.", "Gen 3, right branch, left roundel (paired with blank right roundel)."),
                    (9, "body", "Thomas Percy Busshopp of Norwiche 57.", "Thomas Percy, Bishop of Norwich, [13]57.", "Gen 4, left branch, right roundel (paired with blank left roundel); a bishop's mitre surmounts the blank shield below."),
                    (10, "body", "Marye y[e] daughter off the E. of Lancaster", "Mary, the daughter of the Earl of Lancaster.", "Gen 4, middle branch, left roundel."),
                    (11, "body", "Henrye Lord Percy", "Henry Lord Percy", "Gen 4, middle branch, right roundel."),
                    (12, "body", "Henry Lo Percy", "Henry Lord Percy", "Gen 4, right branch, left roundel."),
                    (13, "body", "Eda the daughter off the Lo. Clifford", "Ida [Eda], the daughter of the Lord Clifford.", "Gen 4, right branch, right roundel."),
                    (14, "body", "Margaret daughter off Raff first. E. of westmerland first wyf off Henry & had issue.", "Margaret, daughter of Ralph, first Earl of Westmorland, first wife of Henry, and had issue.", "Gen 5, left roundel."),
                    (15, "body", "Henry Lo percy the first. E. of Nortthumberland", "Henry Lord Percy, the first Earl of Northumberland.", "Gen 5, middle roundel."),
                    (16, "body", "Jane y[e] da. of Jeffray Lo. Lucy sans issue. gaue her land to her husband on condicon he shold beare Lucyes robe in y[e]. 2. quart[er] of y[e] field.", "Jane [recte Maud], the daughter of Geoffrey [recte Anthony] Lord Lucy, without issue; gave her land to her husband on condition he should bear Lucy's robe [recte luces/arms] in the 2nd quarter of the field.", "Gen 5, right roundel. Historically Maud Lucy (d. 1398), widow of Gilbert de Umfraville, who brought the Lucy lands to Henry Percy, 1st Earl of Northumberland."),
                ]),
            }
        ],
    },
]
