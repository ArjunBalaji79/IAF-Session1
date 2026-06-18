"""Build IAF-Session4-Redesigned.pptx from S2 records, using S2 media."""
import json, sys
import archetypes
# point the renderer at the S2 media set
archetypes.MEDIA = "s4_assets/media"
try:
    archetypes._REMAP = json.load(open("s4_media_remap.json"))
except Exception:
    archetypes._REMAP = {}
from deck_build import build

if __name__ == "__main__":
    rp = sys.argv[1] if len(sys.argv) > 1 else "s4_deck_records.json"
    op = sys.argv[2] if len(sys.argv) > 2 else "IAF-Session4-Redesigned.pptx"
    build(rp, op, hide_srcs=())   # S2 has no hidden slides
