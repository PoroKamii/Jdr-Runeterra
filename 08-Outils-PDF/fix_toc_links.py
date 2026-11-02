#!/usr/bin/env python3
"""Répare les liens du sommaire d'un PDF produit par wkhtmltopdf.

Problème : wkhtmltopdf (Qt non patché) transforme les liens internes (#ancre) en
liens "file:///...html#ancre", inutilisables dans le PDF, et ne crée pas de signets.

Solution en deux temps :
  1. prepare : glisse dans chaque titre (h1-h6) un repère invisible contenant son id ;
  2. fix     : retrouve chaque repère dans le PDF (page + position), puis remplace
               chaque lien "...#ancre" par un saut interne vers cette position.

Usage :
  python3 fix_toc_links.py prepare page.html page-prete.html
  wkhtmltopdf ... page-prete.html brut.pdf
  python3 fix_toc_links.py fix brut.pdf final.pdf page-prete.html

Dépendances : pypdf, pypdfium2 (pip install pypdf pypdfium2)
"""
import re
import sys
from urllib.parse import unquote, urlparse

MARK = "QQZ{}ZQQ"
MARK_RE = re.compile(r"QQZ(\d+)ZQQ")
SPAN = '<span style="color:#ffffff;font-size:2px;">{}</span>'


def prepare(html_in, html_out):
    with open(html_in, encoding="utf-8") as f:
        html = f.read()
    ids = []

    def add_mark(m):
        ids.append(m.group(2))
        return m.group(0) + SPAN.format(MARK.format(len(ids) - 1))

    html = re.sub(r'<(h[1-6])\b[^>]*\bid="([^"]+)"[^>]*>', add_mark, html)
    # Table id <-> numéro, gardée dans le HTML (commentaire) pour l'étape fix.
    table = "\n".join(f"{i}\t{a}" for i, a in enumerate(ids))
    html = html.replace("</body>", f"<!--TOCMAP\n{table}\nTOCMAP-->\n</body>")
    with open(html_out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{len(ids)} titre(s) marqué(s).")


def locate_marks(pdf_path):
    import pypdfium2 as pdfium

    pdf = pdfium.PdfDocument(pdf_path)
    found = {}
    for page_index in range(len(pdf)):
        page = pdf[page_index]
        height = page.get_height()
        text_page = page.get_textpage()
        text = text_page.get_text_range()
        for m in MARK_RE.finditer(text):
            num = int(m.group(1))
            if num in found:
                continue
            # Position verticale du repère (haut de la boîte du 1er caractère).
            try:
                box = text_page.get_charbox(m.start())
                top = min(box[3] + 24, height)
            except Exception:
                top = None
            found[num] = (page_index, top)
    return found


def fix(pdf_in, pdf_out, html_with_map):
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import ArrayObject, FloatObject, NameObject, NullObject

    with open(html_with_map, encoding="utf-8") as f:
        block = re.search(r"<!--TOCMAP\n(.*?)\nTOCMAP-->", f.read(), re.S)
    if not block:
        sys.exit("Table des repères introuvable : lancer d'abord l'étape prepare.")
    ids = {}
    for line in block.group(1).splitlines():
        num, anchor = line.split("\t", 1)
        ids[anchor] = int(num)

    positions = locate_marks(pdf_in)
    writer = PdfWriter(clone_from=PdfReader(pdf_in))
    fixed, broken = 0, []
    for page in writer.pages:
        annots = page.get("/Annots")
        if not annots:
            continue
        for ref in annots.get_object():
            annot = ref.get_object()
            action = annot.get("/A")
            if not action or action.get("/S") != "/URI":
                continue
            url = urlparse(str(action.get("/URI")))
            if not url.fragment or url.scheme not in ("file", ""):
                continue
            anchor = unquote(url.fragment)
            num = ids.get(anchor)
            if num is None or num not in positions:
                broken.append(anchor)
                continue
            page_num, top = positions[num]
            annot[NameObject("/Dest")] = ArrayObject([
                writer.pages[page_num].indirect_reference,
                NameObject("/XYZ"),
                NullObject(),
                FloatObject(top) if top is not None else NullObject(),
                NullObject(),
            ])
            del annot["/A"]
            fixed += 1
    writer.write(pdf_out)
    print(f"{fixed} lien(s) réparé(s), {len(broken)} sans cible.")
    if broken:
        print("Sans cible :", ", ".join(broken[:10]))
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "prepare":
        prepare(sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 5 and sys.argv[1] == "fix":
        fix(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        sys.exit(__doc__ + "\n(fix : python3 fix_toc_links.py fix brut.pdf final.pdf page-prete.html)")
