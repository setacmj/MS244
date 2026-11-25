#!/usr/bin/env python3
"""
Rectifies figure bounding boxes in MS244_figures_and_tables.json based on direct visual
inspection of the manuscript canvases, and pads tiny manicule boxes so they always
frame the pointing hand and adjacent text line cleanly.
"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FIGS_FILE = BASE_DIR / "MS244_figures_and_tables.json"

# Exact verified (x%, y%, w%, h%) overrides from visual inspection
PCT_OVERRIDES = {
    "fig_c016_1": (18.0, 84.0, 10.0, 9.0),
    "fig_c036_2": (15.5, 55.0, 13.0, 18.0),
    "fig_c036_3": (15.5, 83.0, 46.5, 13.5),
    "fig_c038_1": (51.0, 65.0, 38.0, 9.0),
    "fig_c064_1": (17.5, 23.0, 34.5, 5.5),
    "fig_c064_2": (17.5, 82.0, 32.0, 5.5),
    "fig_c064_3": (47.0, 33.5, 6.5, 5.0),
    "fig_c064_4": (13.0, 89.5, 8.0, 5.0),
    "fig_c082_1": (16.5, 5.5, 8.0, 5.0),
    "fig_c082_2": (50.0, 81.5, 11.0, 4.5),
    "fig_c105_1": (74.0, 11.0, 12.0, 6.0),
    "fig_c105_2": (73.5, 23.0, 12.5, 6.5),
    "fig_c106_1": (24.5, 77.5, 17.5, 12.0),
    "fig_c106_2": (55.0, 61.5, 14.5, 7.0),
    "fig_c106_3": (55.0, 68.0, 18.5, 21.0),
    "fig_c109_1": (21.0, 57.5, 23.0, 4.5),
    "fig_c113_1": (77.5, 35.0, 9.0, 5.5),
    "fig_c117_1": (75.0, 61.0, 11.0, 9.0),
    "fig_c117_2": (75.0, 72.5, 11.0, 9.5),
    "fig_c321_1": (19.0, 65.5, 22.0, 5.0),
    "fig_c349_1": (51.0, 18.0, 25.0, 17.0),
    "fig_c365_1": (15.0, 7.0, 17.0, 23.0),
}


def main():
    figs = json.loads(FIGS_FILE.read_text(encoding="utf-8"))
    fixed = 0
    padded = 0
    for f in figs:
        fid = f["fig_id"]
        c = f["canvas_num"]
        svc = f"https://iiif.wellcomecollection.org/image/b19608652_MS_244_{c:04d}.JP2"
        if fid in PCT_OVERRIDES:
            px, py, pw, ph = PCT_OVERRIDES[fid]
            f["iiif_crop"] = f"{svc}/pct:{px:.2f},{py:.2f},{pw:.2f},{ph:.2f}/800,/0/default.jpg"
            fixed += 1
        elif "manicule" in f["label"].lower() or "pointing hand" in f["label"].lower():
            pct = f["iiif_crop"].split("/pct:")[1].split("/")[0]
            px, py, pw, ph = [float(x) for x in pct.split(",")]
            if pw < 9.0 or ph < 5.0:
                cx = px + pw / 2.0
                cy = py + ph / 2.0
                nw = max(pw, 9.0)
                nh = max(ph, 5.0)
                nx = max(0.0, min(100.0 - nw, cx - nw / 2.0))
                ny = max(0.0, min(100.0 - nh, cy - nh / 2.0))
                f["iiif_crop"] = f"{svc}/pct:{nx:.2f},{ny:.2f},{nw:.2f},{nh:.2f}/800,/0/default.jpg"
                padded += 1

    FIGS_FILE.write_text(json.dumps(figs, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Rectified {fixed} figure boxes and padded {padded} manicule boxes in {FIGS_FILE.name}.")


if __name__ == "__main__":
    main()
