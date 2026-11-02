#!/usr/bin/env bash
# Régénère le PDF d'un fichier .md du JDR Runeterra.
# Chaîne : pandoc (.md -> HTML + style.html) -> fix_toc_links.py prepare
#          -> wkhtmltopdf (HTML -> PDF) -> fix_toc_links.py fix (liens du sommaire)
#
# Usage : ./build_pdf.sh chemin/vers/fichier.md "Titre affiché en tête du PDF"
# Le PDF est écrit à côté du .md, avec le même nom.
set -euo pipefail
export LANG=C.UTF-8 LC_ALL=C.UTF-8

MD="$1"
TITLE="$2"
TOOLS="$(cd "$(dirname "$0")" && pwd)"
PDF="${MD%.md}.pdf"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

pandoc "$MD" -f markdown+ascii_identifiers -s --toc --toc-depth=3 \
  --metadata title="$TITLE" -H "$TOOLS/style.html" -o "$WORK/page.html"
python3 "$TOOLS/fix_toc_links.py" prepare "$WORK/page.html" "$WORK/page-prete.html"
wkhtmltopdf -q --enable-local-file-access --encoding utf-8 -s A4 \
  -T 15 -B 15 -L 12 -R 12 "$WORK/page-prete.html" "$WORK/brut.pdf" 2>/dev/null || true
test -s "$WORK/brut.pdf" || { echo "wkhtmltopdf n'a pas produit de PDF" >&2; exit 1; }
python3 "$TOOLS/fix_toc_links.py" fix "$WORK/brut.pdf" "$PDF" "$WORK/page-prete.html"
echo "PDF : $PDF"
