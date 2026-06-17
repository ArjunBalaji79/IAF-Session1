#!/bin/bash
# render.sh PPTX [DPI]  ->  PNGs in ./render/
set -e
SOFFICE="/Applications/LibreOffice.app/Contents/MacOS/soffice"
PPTX="${1:-prototype.pptx}"
DPI="${2:-150}"
OUT="render"
mkdir -p "$OUT"
rm -f "$OUT"/*.png "$OUT"/*.pdf 2>/dev/null || true
"$SOFFICE" --headless --convert-to pdf --outdir "$OUT" "$PPTX" >/dev/null 2>&1
PDF="$OUT/$(basename "${PPTX%.pptx}").pdf"
pdftoppm -png -r "$DPI" "$PDF" "$OUT/slide"
echo "rendered $(ls "$OUT"/slide-*.png | wc -l | tr -d ' ') slides at ${DPI}dpi -> $OUT/"
ls "$OUT"/slide-*.png
