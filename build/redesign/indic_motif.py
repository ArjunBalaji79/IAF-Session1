"""Generate the indic kilim corner ornament as a crisp high-res transparent PNG.
Pure axis-aligned stitches -> razor sharp at any size, recolorable.
Charted from the Discovery-Day source art: navy stepped chevrons, terracotta
lotus florets at the peaks, a gold dotted line, gold 'stupa' accents in valleys.
"""
from PIL import Image, ImageDraw

# --- brand palette (from memory design system) ---
NAVY  = (0x1F, 0x3A, 0x5F)
TERRA = (0xB8, 0x50, 0x42)
GOLD  = (0xC8, 0xA0, 0x4A)
GREEN = (0x4A, 0x6B, 0x3A)

A = 2            # chevron amplitude (stitches)
T = 2            # chevron line thickness
PER = 2 * A      # zigzag period
CORNER = 6       # corner-block size
RUN = 14         # how far runs extend from the corner


def _chevron_h(i):
    """height of zigzag at step i: 0 at peaks (i=A,3A..), A at valleys (i=0,2A..)"""
    return abs((i % PER) - A)


def make_corner(stitch=26, run=RUN, pad=1, navy=NAVY):
    cells = {}

    def put(c, r, col):
        cells[(c, r)] = navy if col == NAVY else col

    def floret(cc, cr):                 # small lotus: + with gold heart
        put(cc, cr - 1, TERRA); put(cc, cr + 1, TERRA)
        put(cc - 1, cr, TERRA); put(cc + 1, cr, TERRA)
        put(cc, cr, GOLD)

    DOT = A + T                        # dotted-line sits just under valleys

    # ---- horizontal run (top edge), starting CORNER cols out ----
    for i in range(run + 1):
        c = CORNER + i
        h = _chevron_h(i)
        for t in range(T):
            put(c, h + t, NAVY)
        if h == 0:
            floret(c, -2)              # floret above each peak
    for c in range(CORNER + 1, CORNER + run + 1, 2):
        put(c, DOT, GOLD)             # clean dotted gold line below band

    # ---- vertical run (left edge): mirror of the horizontal run ----
    for j in range(run + 1):
        r = CORNER + j
        h = _chevron_h(j)
        for t in range(T):
            put(h + t, r, NAVY)
        if h == 0:
            floret(-2, r)
    for r in range(CORNER + 1, CORNER + run + 1, 2):
        put(DOT, r, GOLD)

    # ---- corner joint: a navy peak pointing into the outer corner ----
    # connect horiz valley (col CORNER, rows A..A+T-1) to vert valley
    # (cols A..A+T-1, row CORNER) with a stepped diagonal navy bracket.
    for k in range(0, CORNER - A + 1):
        rr = A + k
        cc = A + k
        for t in range(T):
            put(CORNER - k, rr + t, NAVY)   # descends toward vertical leg
            put(cc + t, CORNER - k, NAVY)   # descends toward horizontal leg
    # outer knee accent + inner lotus
    floret(CORNER + 1, CORNER + 1)
    put(CORNER + 1, CORNER - 1, GREEN)
    put(CORNER - 1, CORNER + 1, GREEN)

    # ---- rasterize ----
    cols = [c for c, r in cells]; rows = [r for c, r in cells]
    cmin, cmax, rmin, rmax = min(cols), max(cols), min(rows), max(rows)
    W = (cmax - cmin + 1 + 2 * pad) * stitch
    H = (rmax - rmin + 1 + 2 * pad) * stitch
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    dr = ImageDraw.Draw(img)
    for (c, r), color in cells.items():
        x = (c - cmin + pad) * stitch
        y = (r - rmin + pad) * stitch
        dr.rectangle([x, y, x + stitch - 1, y + stitch - 1], fill=color + (255,))
    return img


if __name__ == "__main__":
    corner = make_corner(stitch=40, run=6)
    corner.save("corner_tl.png")
    print("corner_tl.png", corner.size)
    CREAM = (0xF4, 0xEC, 0xD8)
    # big single-corner view
    big = Image.new("RGB", (corner.width + 120, corner.height + 120), CREAM)
    big.paste(corner, (40, 40), corner)
    big.save("corner_solo.png"); print("corner_solo.png", big.size)
    # 4-corner slide preview at slide scale (1600x900 ~ 13.33x7.5)
    W, H = 1600, 900
    canvas = Image.new("RGB", (W, H), CREAM)
    sc = 0.62  # display corner ~ 1.6in on a 13.33in slide
    corner = corner.resize((int(corner.width * sc), int(corner.height * sc)))
    m = 58
    tl = corner
    tr = corner.transpose(Image.FLIP_LEFT_RIGHT)
    bl = corner.transpose(Image.FLIP_TOP_BOTTOM)
    br = corner.transpose(Image.ROTATE_180)
    canvas.paste(tl, (m, m), tl)
    canvas.paste(tr, (W - m - tr.width, m), tr)
    canvas.paste(bl, (m, H - m - bl.height), bl)
    canvas.paste(br, (W - m - br.width, H - m - br.height), br)
    canvas.save("motif_preview.png"); print("motif_preview.png", canvas.size)
