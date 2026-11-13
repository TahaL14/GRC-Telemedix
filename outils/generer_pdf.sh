#!/usr/bin/env bash
# Génère pdf/dossier-complet.pdf à partir des fichiers Markdown (pandoc + Chrome/Chromium).
set -euo pipefail
export LC_ALL=C.UTF-8
cd "$(dirname "$0")/.."

CHROME="${CHROME:-$(command -v google-chrome || command -v chromium || command -v chromium-browser)}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

cat > "$TMP/style.css" <<'CSS'
@page { size: A4 landscape; margin: 14mm 12mm; }
body { font-family: "DejaVu Sans", "Helvetica Neue", Arial, sans-serif; font-size: 9.5pt; line-height: 1.4; color: #111827; max-width: none; margin: 0; padding: 0; }
h1 { font-size: 19pt; color: #0f3d5c; border-bottom: 2px solid #0f3d5c; padding-bottom: 4px; page-break-before: always; }
h1:first-of-type { page-break-before: avoid; }
h2 { font-size: 13.5pt; color: #0f3d5c; margin-top: 18px; page-break-after: avoid; }
h3 { font-size: 11pt; color: #1f2937; page-break-after: avoid; }
table { border-collapse: collapse; width: 100%; margin: 8px 0 14px; font-size: 8.4pt; }
th { background: #0f3d5c; color: #fff; text-align: left; padding: 4px 6px; }
td { border: 1px solid #cbd5e1; padding: 3px 6px; vertical-align: top; }
tr { page-break-inside: avoid; }
tr:nth-child(even) td { background: #f5f8fa; }
thead { display: table-header-group; }
blockquote { border-left: 4px solid #d97706; background: #fffbeb; margin: 8px 0; padding: 4px 12px; }
code, pre { font-family: "DejaVu Sans Mono", monospace; font-size: 8.4pt; background: #f1f5f9; }
pre { padding: 8px; }
img { max-width: 78%; display: block; margin: 8px auto; }
a { color: #0f3d5c; text-decoration: none; }
hr { border: 0; border-top: 1px solid #cbd5e1; }
CSS

pandoc README.md 01-cadrage.md 02-ebios-rm.md 03-aipd-registre.md 04-dda-iso27001.md \
       05-ecarts-hds-nis2.md 06-plan-actions.md 07-pssi.md annexes/sources-et-points-a-verifier.md \
  --from gfm --to html5 --standalone --embed-resources --resource-path=. \
  --metadata pagetitle="Dossier de conformité : plateforme de téléconsultation (cas fictif)" \
  --metadata lang=fr --css "$TMP/style.css" -o "$TMP/dossier.html"

mkdir -p pdf
"$CHROME" --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="pdf/dossier-complet.pdf" "file://$TMP/dossier.html" 2>/dev/null

# PSSI seule, au format portrait (2 pages)
sed 's/A4 landscape; margin: 14mm 12mm/A4 portrait; margin: 14mm 15mm/; s/font-size: 9.5pt/font-size: 9pt/' "$TMP/style.css" > "$TMP/style-portrait.css"
pandoc 07-pssi.md --from gfm --to html5 --standalone --embed-resources \
  --metadata pagetitle="PSSI Télémédix (cas fictif)" --metadata lang=fr \
  --css "$TMP/style-portrait.css" -o "$TMP/pssi.html"
"$CHROME" --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="pdf/pssi.pdf" "file://$TMP/pssi.html" 2>/dev/null
echo "PDF générés : pdf/dossier-complet.pdf, pdf/pssi.pdf"
