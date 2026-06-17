"""Extract the ORIGINAL ornate kilim corner ornament from the source deck art.

The corner motif lives baked into a full-slide parchment background
(assets/kilim_source.png == image19.png from "IAF - Session 1.pptx",
the "Let's start with introductions" slide). We crop the top-left
L-corner and chroma-key the parchment to transparent (saturation ramp),
so the navy/terracotta/gold/green cross-stitch drops cleanly onto our
flat cream with no seam.

Outputs (into the redesign folder):
  corner_real.png       — navy stitches, for cream slides
  corner_real_dark.png  — navy recolored to cream, for navy/dark slides
"""
from PIL import Image

SRC = "assets/kilim_source.png"
LIGHT = "corner_real.png"
DARK = "corner_real_dark.png"

# top-left ornament bbox in the 1376x768 source (measured), + pad
BBOX = (34, 30, 307, 277)
PAD = 8
# saturation key: cream ~0.13 sat, stitches >=0.46 sat -> ramp cleanly between
KEY_LO, KEY_HI = 0.20, 0.34
CREAM_LT = (0xF1, 0xE7, 0xCE)   # navy -> this on dark variant


def _sat(r, g, b):
    mx, mn = max(r, g, b), min(r, g, b)
    return 0.0 if mx == 0 else (mx - mn) / mx


def _is_navy(r, g, b):
    return (b >= r) and (b >= g - 10) and (max(r, g, b) < 150) and (b > 50)


def make_corners():
    im = Image.open(SRC).convert("RGB")
    x0, y0, x1, y1 = BBOX
    crop = im.crop((x0 - PAD, y0 - PAD, x1 + PAD, y1 + PAD)).convert("RGBA")
    px = crop.load()
    w, h = crop.size
    for y in range(h):
        for x in range(w):
            r, g, b, _ = px[x, y]
            s = _sat(r, g, b)
            if s <= KEY_LO:
                a = 0
            elif s >= KEY_HI:
                a = 255
            else:
                a = int(round(255 * (s - KEY_LO) / (KEY_HI - KEY_LO)))
            px[x, y] = (r, g, b, a)
    crop.save(LIGHT)

    dark = crop.copy()
    dpx = dark.load()
    for y in range(h):
        for x in range(w):
            r, g, b, a = dpx[x, y]
            if a > 0 and _is_navy(r, g, b):
                dpx[x, y] = (CREAM_LT[0], CREAM_LT[1], CREAM_LT[2], a)
    dark.save(DARK)
    return crop.size


if __name__ == "__main__":
    print("corner size:", make_corners())
