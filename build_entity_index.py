#!/usr/bin/env python3
"""
Builds MS244_entity_index.json and MS244_figures_and_tables.json from MS244_edition_data.json.
Extracts curated Index Terms (Ingredients, Ailments, People & Authorities, Places,
Tables & Apparatus, Heraldry & Genealogies) and all 191 annotated Figures + Tables.
"""
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "MS244_edition_data.json"

ENTITY_DEFS = [
    # Ingredients & Materia Medica
    ("Ingredients", "Honey / Mel", "Clarified honey, wild honey, and honey of roses", r"\b(honey|hunny|mel|mellis)\b"),
    ("Ingredients", "Wine / Vinum", "White wine, red wine, Rhenish, Malmsey, sack, Rumney", r"\b(wine|wyne|vinum|vini|vino|malmsey|malvasia|sack|rhenish|rumney)\b"),
    ("Ingredients", "Vinegar / Acetum", "Wine vinegar and distilled vinegar", r"\b(vinegar|vineger|acetum|aceti|aceto)\b"),
    ("Ingredients", "Ale & Beer", "Stale ale, strong ale, wort, posset ale", r"\b(ale|wort|worte|posset|ceruisia)\b"),
    ("Ingredients", "Rose / Rosewater", "Red/damask roses, rosewater, oil of roses, conserve of roses", r"\b(rose|roses|rosewater|rosarum|rosat)\b"),
    ("Ingredients", "Butter / May Butter", "Fresh butter, May butter, clarified butter", r"\b(butter|butyrum)\b"),
    ("Ingredients", "Wax / Cera", "Beeswax, virgin wax, yellow/white wax", r"\b(wax|waxe|cera|cere)\b"),
    ("Ingredients", "Turpentine / Terebinthina", "Venice turpentine and common turpentine", r"\b(turpentine|terebint)\b"),
    ("Ingredients", "Sugar / Saccharum", "White sugar, sugar candy, Manus Christi", r"\b(sugar|suger|sacchar|zuccar)\b"),
    ("Ingredients", "Salt / Sal", "Common salt, bay salt, sal ammoniac, sal gemmae", r"\b(salt|salis|sal\s+armoniak|sal\s+gemmae)\b"),
    ("Ingredients", "Alum / Alumen", "Rock alum, burnt alum", r"\b(alum|alumen|allum)\b"),
    ("Ingredients", "Mercury / Quicksilver", "Quicksilver, sublimate, turbith mineral, cinnabar", r"\b(mercury|mercur|quicksilver|sublimate|cinnabar|turbith)\b"),
    ("Ingredients", "Vitriol / Copperas", "Oil of vitriol, white/green vitriol, copperas", r"\b(vitriol|vitrioll|copperas|coppras)\b"),
    ("Ingredients", "Lead / Litharge / Cerussa", "White lead, red lead, litharge of gold/silver, minium", r"\b(lead|litharge|litarge|cerussa|minium|plumb)\b"),
    ("Ingredients", "Bole Armenick", "Armenian bole (astringent clay)", r"\b(bole|bolus|boli\s+arm)\b"),
    ("Ingredients", "Dragon's Blood", "Sanguis draconis resin", r"\b(dragon.?s\s+blood|sanguis\s+draconis|sang\w*\s+drac)\b"),
    ("Ingredients", "Camphor", "Camphor resin", r"\b(camphor|camphire|camphora)\b"),
    ("Ingredients", "Myrrh", "Myrrh resin", r"\b(myrrh|myrrhe|mirre|myrr)\b"),
    ("Ingredients", "Mastic", "Mastic resin", r"\b(mastic|mastik|mastick|masticis)\b"),
    ("Ingredients", "Frankincense / Olibanum", "Frankincense and olibanum", r"\b(frankincense|frankensence|olibanum|oliban|thuris)\b"),
    ("Ingredients", "Aloes", "Hepatic and succotrine aloes", r"\b(aloes|aloe)\b"),
    ("Ingredients", "Saffron / Crocus", "Saffron stigmas", r"\b(saffron|safron|crocus|croci)\b"),
    ("Ingredients", "Rhubarb", "Choice rhubarb root", r"\b(rhubarb|rhabarb|rabarb)\b"),
    ("Ingredients", "Senna", "Senna leaves and pods", r"\b(senna|sene|diasena)\b"),
    ("Ingredients", "Comfrey / Consolida", "Greater comfrey (Consolida major)", r"\b(comfrey|comfery|comferie|consolida)\b"),
    ("Ingredients", "Wormwood / Absinthium", "Common and Roman wormwood", r"\b(wormwood|wormwod|absinth)\b"),
    ("Ingredients", "Betony", "Wood betony", r"\b(betony|betonye|betonica)\b"),
    ("Ingredients", "Sage", "Red and garden sage", r"\b(sage|salvia)\b"),
    ("Ingredients", "Rosemary", "Rosemary leaves and flowers", r"\b(rosemary|rosemarye|rosmar)\b"),
    ("Ingredients", "Plantain", "Greater plantain and ribwort", r"\b(plantain|plantin|plantago)\b"),
    ("Ingredients", "Celandine", "Greater celandine", r"\b(celandine|celendyne|chelidonia)\b"),
    ("Ingredients", "Elder / Sambucus", "Elder bark, leaves, berries, and danewort (Ebulus)", r"\b(elder|ellarne|sambucus|sambuci|ebulus|ebuli|danewort|walwort)\b"),
    ("Ingredients", "Polypody of the Oak", "Polypody fern root and leaves", r"\b(polypody|pollipody|polipodie)\b"),
    ("Ingredients", "Elecampane", "Elecampane root (Inula helenium)", r"\b(elecampane|enula)\b"),
    ("Ingredients", "Tobacco / Nicotiana", "Virginian tobacco leaves and smoke", r"\b(tobacco|tobac|nicotiana)\b"),
    ("Ingredients", "Guaiacum / Lignum Vitae", "Guaiacum wood for pox & diet drinks", r"\b(guaiac|lignum\s+vitae|lignum\s+sanctum)\b"),
    ("Ingredients", "Sarsaparilla", "Sarsaparilla root", r"\b(sarsaparilla|sarsa)\b"),
    ("Ingredients", "Earthworms", "Distilled or powdered earthworms (Lumbrici)", r"\b(earthworm|earth\s+worm|redworm|lumbric)\b"),
    ("Ingredients", "Snails", "Garden and red snails", r"\b(snail|snails|snayles)\b"),
    ("Ingredients", "Toads", "Dried/calcined toad remedies", r"\b(toad|toads|toade)\b"),

    # Ailments & Conditions
    ("Ailments", "Wounds, Ulcers & Old Sores", "Green wounds, foul ulcers, fistulas, proud flesh", r"\b(wound|wounds|ulcer|ulcers|vlcer|sores|sore|fistula|proud\s+flesh)\b"),
    ("Ailments", "Rupture / Hernia", "Inguinal, watery, and intestinal ruptures", r"\b(rupture|ruptures|hernia|hernias|bursten)\b"),
    ("Ailments", "Dropsy / Hydrops", "Anasarca, tympanites, and watery swellings", r"\b(dropsy|dropsie|dropsye|hidrop|hydrop)\b"),
    ("Ailments", "Gout / Podagra", "Gout, hot/cold gout, and joint swellings", r"\b(gout|gowte|podagra)\b"),
    ("Ailments", "Sciatica & Aches", "Sciatica, hip-ache, and sprains", r"\b(sciatica|sciattica|ache|sprain|spraines)\b"),
    ("Ailments", "Palsy & Cramp", "Paralysis, numbness, wry mouth, and cramp", r"\b(palsy|palsey|palsye|paralysis|cramp|crampe|benumed)\b"),
    ("Ailments", "Pox / Morbus Gallicus", "French pox and smallpox/measles", r"\b(pox|morbus\s+gallicus|morbo\s+gallico|lues\s+venerea|small\s+pox)\b"),
    ("Ailments", "Dysentery & Bloody Flux", "Flux, bloody flux, lientery, diarrhoea", r"\b(flux|flixe|bloody\s+flux|discenteria|dysenter|lienter)\b"),
    ("Ailments", "Stone & Strangury", "Kidney/bladder stone, gravel, strangury", r"\b(stone|strangury|strangurie|gravel)\b"),
    ("Ailments", "Colic & Iliac Passion", "Colic, iliac passion, belly pain", r"\b(colic|collica|illiaca)\b"),
    ("Ailments", "Jaundice (Yellow & Black)", "Yellow jaundice, black jaundice, icterus", r"\b(jaundice|jaundis|jaundies|icter)\b"),
    ("Ailments", "Green Sickness", "Chlorosis / green sickness", r"\b(green\s+sickness|greene\s+sickness)\b"),
    ("Ailments", "Canker & Sore Breasts", "Canker, breast abscesses, mastitis", r"\b(canker|sore\s+breast|brestes)\b"),
    ("Ailments", "King's Evil / Scrofula", "Scrofula, wens, and Morbus Regius", r"\b(king.?s\s+evil|scrophul|morbum\s+regium|wennes)\b"),
    ("Ailments", "Gangrene & Sphacelus", "Gangrene, mortification, cold fire", r"\b(gangrene|gangrena|spacellus|mortif)\b"),
    ("Ailments", "Epilepsy / Falling Sickness", "Epilepsia, analepsia, catalepsia", r"\b(epilep|falling\s+sickness|catalept|analept)\b"),
    ("Ailments", "Quinsy / Squinantia", "Throat inflammation and quinsy", r"\b(quinsy|quinsey|squinantia|angina)\b"),
    ("Ailments", "Burning & Scalding", "Fire, boiling water, and gunpowder burns", r"\b(burn|burning|burninge|scald|scalding|gunpowder)\b"),
    ("Ailments", "Deafness & Ear Ailments", "Deafness, tinnitus, ear ulcers, earwigs", r"\b(deaf|deffnes|ear|ears|eares|earwig)\b"),
    ("Ailments", "Eyes & Vision", "Sore eyes, webs, pearls, inflammation", r"\b(eye|eyes|sight|blind)\b"),
    ("Ailments", "Toothache", "Toothache, hollow teeth, gums", r"\b(tooth|teeth|toothache|toothe)\b"),
    ("Ailments", "Ague & Fevers", "Quartan, tertian, quotidian agues and fevers", r"\b(ague|agues|fever|fevers|febr)\b"),
    ("Ailments", "Cough, Asthma & Phthisis", "Cough, consumption, lung ulcers, asthma", r"\b(cough|tissike|tysik|asthma|astma|phthis|consumption)\b"),
    ("Ailments", "Plague / Pestilence", "Plague waters, antidotes, carbuncles", r"\b(plague|pestilence|pest)\b"),

    # People & Authorities
    ("People", "Henry Dineley / Dingley", "Primary compiler (fl. 1564–1633) of Hanley Castle", r"\b(henry\s+dingley|henry\s+dineley|henry\s+dyneley|h\.?\s*d\.?|dingley|dineley|dyneley)\b"),
    ("People", "Dr. John Sadler (1615–1664)", "Mid-17th-century physician contributor", r"\b(sadler)\b"),
    ("People", "Francis Dineley (1591/1592)", "Donor of the volume to Henry Dineley (3 Dec 1591)", r"\b(francis\s+dineley|frauncis\s+dyneley)\b"),
    ("People", "Elizabeth Ergas (Grandmother)", "Henry Dineley's maternal grandmother", r"\b(ergas|grandmother)\b"),
    ("People", "John Arderne", "14th-century English surgeon cited repeatedly", r"\b(arderne|ardern)\b"),
    ("People", "Leonardo Fioravanti", "16th-century Italian surgeon/iatrochemist", r"\b(fioravanti|phiorouant|phioravant)\b"),
    ("People", "Nicholas Culpeper (1649)", "Author of the London Dispensatory cited in later additions", r"\b(culpeper|london\s+dispensatory|lond:\s*disp)\b"),
    ("People", "Galen", "Classical Greek medical authority", r"\b(galen)\b"),
    ("People", "Paracelsus", "Renaissance iatrochemist", r"\b(paracels)\b"),
    ("People", "Rembert Dodoens", "Flemish botanist (Dodoneus)", r"\b(dodoens|dodoneus)\b"),
    ("People", "Pietro Andrea Mattioli", "Italian physician & Dioscorides commentator", r"\b(mattioli|mathiolus)\b"),
    ("People", "Joseph Quercetanus", "French Paracelsian physician (Du Chesne)", r"\b(quercetanus)\b"),
    ("People", "John Woodall", "English surgeon (The Surgions Mate)", r"\b(woodall)\b"),
    ("People", "Sir Thomas Bromley (1625)", "Subject of the 1625 dropsy sweat-tub case", r"\b(bromley)\b"),
    ("People", "Prince Charles (1630)", "Birth note of Charles II in June 1630 calendar", r"\b(prince\s+charles)\b"),

    # Places & Provenance
    ("Places", "Hanley Castle (Worcestershire)", "Seat of Henry Dineley", r"\b(hanley\s+castle|hanley\s+chastell)\b"),
    ("Places", "Tewkesbury (Gloucestershire)", "Family memory of grandfather, father & Henry Dineley", r"\b(tewkesbury)\b"),
    ("Places", "Evesham (Worcestershire)", "1633 clinical case note", r"\b(evesham)\b"),
    ("Places", "Church Lawford (Warwickshire)", "Town cited for rupture plaster", r"\b(church\s+lawford|shurts\s+lawford)\b"),
    ("Places", "London", "Source of apothecary goods & blue-black pin paper", r"\b(london)\b"),
    ("Places", "Bristol", "Cited for Mr. Robert Russell's black plaster", r"\b(bristol|bristoll)\b"),
    ("Places", "Isle of Rhé (1627)", "1627 expedition noted in flux/toad receipt", r"\b(isle\s+of\s+rh[eé]|rh[eé])\b"),

    # Tables, Calendars & Apparatus
    ("Apparatus & Tables", "Roman Catholic Calendar", "12-month liturgical calendar with Four Seasons regimens", r"\b(kalends|nones|ides|epiphany|purification|dominical)\b"),
    ("Apparatus & Tables", "Easter & Solar Cycle Tables", "Perpetual Easter and 1645–1668 solar cycle tables", r"\b(easter\s+table|solar\s+cycle|shrove|golden\s+number)\b"),
    ("Apparatus & Tables", "Sundials & Quadrant", "Horizontal/vertical sundials and astronomical quadrant", r"\b(sundial|diall|gnomon|stile|quadrant|zenith)\b"),
    ("Apparatus & Tables", "Weights & Measures (1564)", "Apothecary grains, scruples, drams, ounces, pounds", r"\b(scruple|dram|drachm|weights\s+and\s+measures|waightes)\b"),
    ("Apparatus & Tables", "Surgical Pipe & Syringe", "'A Pype to heale thrustes' and clyster/ear pipes", r"\b(pype|pipe|syringe|clyster|glister)\b"),
    ("Apparatus & Tables", "Surgical Tents & Probes", "Rolled tents, quill tents, whalebone/sinew probes", r"\b(tent|tents|tente|probe|suture|truss)\b"),
    ("Apparatus & Tables", "Angling & Fishing Gear", "Carp baits, rod-making, tin/brass bands, floats", r"\b(carp|carpe|angling|fishing\s+rod|hook|hocke)\b"),

    # Heraldry & Genealogies
    ("Heraldry & Pedigrees", "Dineley Arms (1613)", "Shield with arms of Dineley dated 1613", r"\b(dineley\s+arms|coat\s+of\s+arms|1613)\b"),
    ("Heraldry & Pedigrees", "Percy (Earls of Northumberland)", "Multi-page genealogical pedigree roundels", r"\b(percy|northumberland)\b"),
    ("Heraldry & Pedigrees", "Talbot (Earls of Shrewsbury)", "Talbot & Grafton genealogical pedigree (1601)", r"\b(talbot|shrewsbury|grafton)\b"),
    ("Heraldry & Pedigrees", "FitzAlan (Earls of Arundel)", "FitzAlan / Arundel genealogical pedigree", r"\b(fitzalan|fitz\s+allen|arundel|arondell)\b"),
    ("Heraldry & Pedigrees", "Armorial Grids (A–B)", "Partly emblazoned 5x6 shield grids", r"\b(armorial|shield|emblazoned|azure|gules|argent|or\b)"),
]


def main():
    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    pages = data["pages"]

    compiled = [
        (cat, name, desc, re.compile(pat, re.IGNORECASE))
        for cat, name, desc, pat in ENTITY_DEFS
    ]

    index_out = []
    for cat, name, desc, rx in compiled:
        refs = []
        total_line_hits = 0
        for p_idx, p in enumerate(pages):
            p_hits = 0
            for col in p.get("columns", []):
                for ln in col.get("lines", []):
                    blob = f"{ln.get('orig', '')} {ln.get('en', '')} {ln.get('note', '')}"
                    if rx.search(blob):
                        p_hits += 1
            if p_hits > 0:
                total_line_hits += p_hits
                refs.append({
                    "pIdx": p_idx,
                    "canvas_num": p["canvas_num"],
                    "orig_page": p.get("orig_page", ""),
                    "lines": p_hits,
                })
        if refs:
            index_out.append({
                "category": cat,
                "name": name,
                "desc": desc,
                "line_hits": total_line_hits,
                "page_hits": len(refs),
                "refs": refs,
            })

    index_out.sort(key=lambda x: (-x["page_hits"], -x["line_hits"], x["name"]))
    out_idx = BASE_DIR / "MS244_entity_index.json"
    out_idx.write_text(json.dumps(index_out, indent=2, ensure_ascii=False), encoding="utf-8")

    # Extract all figures & tables
    figures_out = []
    for p_idx, p in enumerate(pages):
        c = p["canvas_num"]
        w = max(1, p.get("width", 5200))
        h = max(1, p.get("height", 7300))
        svc = f"https://iiif.wellcomecollection.org/image/b19608652_MS_244_{c:04d}.JP2"
        for fig in p.get("figures", []):
            ulx = fig.get("ulx", 0)
            uly = fig.get("uly", 0)
            lrx = fig.get("lrx", w)
            lry = fig.get("lry", h)
            px = max(0.0, min(99.0, 100.0 * ulx / w))
            py = max(0.0, min(99.0, 100.0 * uly / h))
            pw = max(1.0, min(100.0 - px, 100.0 * (lrx - ulx) / w))
            ph = max(1.0, min(100.0 - py, 100.0 * (lry - uly) / h))
            pct = f"pct:{px:.2f},{py:.2f},{pw:.2f},{ph:.2f}"
            figures_out.append({
                "pIdx": p_idx,
                "canvas_num": c,
                "orig_page": p.get("orig_page", ""),
                "fig_id": fig.get("fig_id", f"fig_c{c:03d}"),
                "label": fig.get("label", "Figure"),
                "desc": fig.get("desc", ""),
                "iiif_crop": f"{svc}/{pct}/800,/0/default.jpg",
                "iiif_full": f"{svc}/full/1400,/0/default.jpg",
            })

    out_fig = BASE_DIR / "MS244_figures_and_tables.json"
    out_fig.write_text(json.dumps(figures_out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {out_idx.name} ({len(index_out)} index terms) and {out_fig.name} ({len(figures_out)} figures).")


if __name__ == "__main__":
    main()
