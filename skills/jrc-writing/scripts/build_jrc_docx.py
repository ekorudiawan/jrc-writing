#!/usr/bin/env python3
"""
Build a Journal of Robotics and Control (JRC) manuscript (.docx) on top of the
official JRC template (JRC_Template.docx, IEEE-conference-style, A4).

The template is used as-is: styles, header/footer, page setup and its three
section breaks (single-column title block -> two-column body -> closing section).
Only the title block text is replaced and the two-column body (Abstract ...
References) is regenerated with the template's own styles, so Word's automatic
numbering produces "I.", "A.", "1)", "TABLE I.", "Fig. 1." and "[1]".

Usage:
    python3 build_jrc_docx.py content.json output.docx --template JRC_Template.docx

content.json (strings accept light markup: **bold**, *italic*, ^{sup}, _{sub}):
{
  "title": "Full Title Without Acronyms",
  "running_title": "Short title for the footer (optional)",
  "authors": [{"name": "Eko Rudiawan Jamzuri", "affil": [1], "email": "eko@polibatam.ac.id",
               "corresponding": true}, ...],
  "affiliations": ["Department of ..., Politeknik Negeri Batam, Batam, Indonesia", ...],
  "abstract": "150-250 words, no citations",
  "keywords": ["k1", "k2", "k3", "k4", "k5"],
  "sections": [
    {"heading": "Introduction", "blocks": [
       {"type": "p", "text": "..."},
       {"type": "h2", "text": "Subheading"},          # auto "A."
       {"type": "h3", "text": "Sub-subheading"},      # auto "1)"
       {"type": "bullets", "items": ["...", "..."]},
       {"type": "equation", "text": "x = Ax + Bu"},   # auto "(1)"
       {"type": "figure", "image": "fig.png", "caption": "...", "width_cm": 8},
       {"type": "table", "caption": "...", "header": ["A", "B"], "rows": [["1", "2"]]}
    ]}
  ],
  "acknowledgment": "optional",
  "references": ["A. Author, \"Title,\" *J. Abbrev.*, vol. 1, no. 2, pp. 1-10, 2024, doi: 10.xxxx/xxxx.", ...]
}
Section headings are written in Title Case; the template style renders them in
small caps. Do not type numbers in headings or references — the template numbers them.
"""
import argparse
import json
import os
import re
import struct
import sys
import zipfile
from xml.dom import minidom

COL_WIDTH_TWIPS = 4865
WARNINGS = []


def xe(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))


TOKEN = re.compile(r"(\*\*.+?\*\*|\*.+?\*|\^\{.+?\}|_\{.+?\})")


def runs(text, base_rpr=""):
    out = []
    for tok in TOKEN.split(text):
        if not tok:
            continue
        extra = ""
        if tok.startswith("**") and tok.endswith("**") and len(tok) > 4:
            tok, extra = tok[2:-2], "<w:b/><w:bCs/>"
        elif tok.startswith("*") and tok.endswith("*") and len(tok) > 2:
            tok, extra = tok[1:-1], "<w:i/><w:iCs/>"
        elif tok.startswith("^{") and tok.endswith("}"):
            tok, extra = tok[2:-1], '<w:vertAlign w:val="superscript"/>'
        elif tok.startswith("_{") and tok.endswith("}"):
            tok, extra = tok[2:-1], '<w:vertAlign w:val="subscript"/>'
        rpr = base_rpr + extra
        rpr_xml = f"<w:rPr>{rpr}</w:rPr>" if rpr else ""
        inner = "<w:tab/>".join(f'<w:t xml:space="preserve">{xe(p)}</w:t>' for p in tok.split("\t"))
        out.append(f"<w:r>{rpr_xml}{inner}</w:r>")
    return "".join(out)


def styled(style, text, extra_ppr="", base_rpr=""):
    return f'<w:p><w:pPr><w:pStyle w:val="{style}"/>{extra_ppr}</w:pPr>{runs(text, base_rpr)}</w:p>'


def ptext(p):
    return "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))


def keep_ppr(p):
    tag = re.match(r"<w:p\b[^>]*>", p).group()
    ppr = re.search(r"<w:pPr>.*?</w:pPr>", p, re.S)
    return tag, (ppr.group() if ppr else "")


# ------------------------------------------------------------------ blocks
def table_xml(caption, header, rows):
    n = len(header)
    w = COL_WIDTH_TWIPS // n
    bd = ('<w:tblBorders>' + "".join(f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
          for s in ("top", "left", "bottom", "right", "insideH", "insideV")) + "</w:tblBorders>")

    def cell(t, style):
        return (f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/><w:vAlign w:val="center"/></w:tcPr>'
                f'<w:p><w:pPr><w:pStyle w:val="{style}"/><w:jc w:val="center"/></w:pPr>{runs(str(t))}</w:p></w:tc>')

    out = [styled("tablehead", caption)]
    out.append(f'<w:tbl><w:tblPr><w:tblW w:w="0" w:type="auto"/><w:jc w:val="center"/>{bd}'
               '<w:tblLayout w:type="autofit"/></w:tblPr><w:tblGrid>' + f'<w:gridCol w:w="{w}"/>' * n + "</w:tblGrid>")
    out.append('<w:tr><w:trPr><w:tblHeader/></w:trPr>' + "".join(cell(h, "tablecolhead") for h in header) + "</w:tr>")
    for r in rows:
        out.append("<w:tr>" + "".join(cell(c, "tablecopy") for c in r) + "</w:tr>")
    out.append("</w:tbl>")
    out.append('<w:p><w:pPr><w:pStyle w:val="BodyText"/><w:spacing w:after="0"/></w:pPr></w:p>')
    return "".join(out)


def equation_xml(text, n, omml=None):
    """Template style: borderless 2-cell table, math left/centre, (n) right."""
    # Plain Times New Roman text by default (renders everywhere); pass "omml" for real Word equations.
    math = omml or runs(text)
    return ('<w:tbl><w:tblPr><w:tblW w:w="4860" w:type="dxa"/><w:tblLayout w:type="fixed"/></w:tblPr>'
            '<w:tblGrid><w:gridCol w:w="4230"/><w:gridCol w:w="630"/></w:tblGrid><w:tr>'
            '<w:tc><w:tcPr><w:tcW w:w="4230" w:type="dxa"/><w:vAlign w:val="center"/></w:tcPr>'
            f'<w:p><w:pPr><w:spacing w:before="60" w:after="60"/><w:jc w:val="center"/></w:pPr>{math}</w:p></w:tc>'
            '<w:tc><w:tcPr><w:tcW w:w="630" w:type="dxa"/><w:vAlign w:val="center"/></w:tcPr>'
            f'<w:p><w:pPr><w:spacing w:before="60" w:after="60"/><w:jc w:val="right"/></w:pPr>{runs(f"({n})")}</w:p></w:tc>'
            "</w:tr></w:tbl>")


def image_size(path):
    with open(path, "rb") as f:
        data = f.read()
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", data[16:24])
    i = 2
    while i < len(data) - 9:
        if data[i] != 0xFF:
            i += 1
            continue
        if data[i + 1] in (0xC0, 0xC1, 0xC2):
            h, w = struct.unpack(">HH", data[i + 5:i + 9])
            return w, h
        i += 2 + struct.unpack(">H", data[i + 2:i + 4])[0]
    return 1600, 1000


def figure_xml(rid, n, w_cm, path):
    w_cm = min(w_cm, 8.5)  # one column is ~8.6 cm wide
    pw, ph = image_size(path)
    cx = int(w_cm * 360000)
    cy = int(cx * ph / pw)
    return ('<w:p><w:pPr><w:keepNext/><w:spacing w:before="120"/><w:jc w:val="center"/></w:pPr><w:r><w:drawing>'
            f'<wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="{cx}" cy="{cy}"/>'
            f'<wp:docPr id="{2000 + n}" name="Figure {n}"/>'
            '<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
            '<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            '<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            f'<pic:nvPicPr><pic:cNvPr id="{2000 + n}" name="fig{n}"/><pic:cNvPicPr/></pic:nvPicPr>'
            f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
            f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
            '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>'
            "</a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>")


def build_body(c, media):
    out = []
    # Abstract & keywords live in the two-column section in this template
    out.append('<w:p><w:pPr><w:pStyle w:val="Abstract"/></w:pPr>'
               + runs("Abstract", "<w:i/>") + runs("—" + c["abstract"]) + "</w:p>")
    out.append(styled("Keywords", "Keywords—" + "; ".join(c["keywords"])))
    fig_n = eq_n = 0
    for sec in c.get("sections", []):
        out.append(styled("Heading1", sec["heading"]))
        for b in sec.get("blocks", []):
            t = b.get("type", "p")
            if t == "p":
                out.append(styled("BodyText", b["text"]))
            elif t == "h2":
                out.append(styled("Heading2", b["text"]))
            elif t == "h3":
                out.append(styled("Heading3", b["text"], '<w:numPr><w:ilvl w:val="2"/><w:numId w:val="9"/></w:numPr>'))
            elif t == "bullets":
                out += [styled("bulletlist", "•\t" + it) for it in b["items"]]
            elif t == "equation":
                eq_n += 1
                out.append(equation_xml(b.get("text", ""), eq_n, b.get("omml")))
            elif t == "figure":
                fig_n += 1
                img = b.get("image")
                if img and os.path.exists(img):
                    ext = os.path.splitext(img)[1].lower().lstrip(".")
                    rid = f"rIdJrcFig{fig_n}"
                    media.append((rid, f"media/jrc_fig{fig_n}.{ext}", img, ext))
                    out.append(figure_xml(rid, fig_n, float(b.get("width_cm", 8)), img))
                else:
                    if img:
                        WARNINGS.append(f"Figure {fig_n}: image '{img}' not found — placeholder inserted.")
                    out.append('<w:p><w:pPr><w:keepNext/><w:jc w:val="center"/></w:pPr>'
                               + runs(f"[INSERT FIGURE {fig_n} HERE]", '<w:highlight w:val="yellow"/>') + "</w:p>")
                out.append(styled("figurecaption", b.get("caption", "")))
            elif t == "table":
                out.append(table_xml(b.get("caption", ""), b["header"], b["rows"]))
            else:
                WARNINGS.append(f"Unknown block type '{t}' skipped.")
    if c.get("acknowledgment"):
        out += [styled("Heading5", "Acknowledgment"), styled("BodyText", c["acknowledgment"])]
    out.append(styled("Heading5", "References"))
    refs = c.get("references", [])
    if len(refs) < 60:
        WARNINGS.append(f"Only {len(refs)} references — JRC rejects papers with fewer than 60 journal references (last 5 years).")
    for r in refs:
        out.append(styled("references", re.sub(r"^\s*\[\d+\]\s*", "", r)))
    return "".join(out)


def build_header(head, c):
    authors = c["authors"]
    paras = list(re.finditer(r"<w:p\b[^>]*?(?:/>|>.*?</w:p>)", head, re.S))
    repl = {}
    for m in paras:
        p, t = m.group(), ptext(m.group())
        span = (m.start(), m.end())
        if '<w:pStyle w:val="papertitle"/>' in p:
            tag, ppr = keep_ppr(p)
            repl[span] = f"{tag}{ppr}{runs(c['title'])}</w:p>"
        elif '<w:pStyle w:val="Author"/>' in p:
            tag, ppr = keep_ppr(p)
            parts = []
            for i, a in enumerate(authors):
                sup = ",".join(str(x) for x in a.get("affil", [1])) + ("*" if a.get("corresponding") else "")
                parts.append(runs(a["name"] + " ") + runs("^{" + sup + "}") + (runs(", ") if i < len(authors) - 1 else ""))
            repl[span] = f"{tag}{ppr}{''.join(parts)}</w:p>"
        elif '<w:pStyle w:val="Affiliation"/>' in p:
            tag, ppr = keep_ppr(p)
            repl[span] = "".join(f"{tag}{ppr}{runs('^{' + str(i) + '}')}{runs(' ' + a)}</w:p>"
                                 for i, a in enumerate(c["affiliations"], start=1))
        elif t.startswith("Email:"):
            tag, ppr = keep_ppr(p)
            bits = [runs("Email: ", '<w:color w:val="000000"/>')]
            for i, a in enumerate(authors, start=1):
                bits.append(runs("^{" + str(i) + " }") + runs(a.get("email", "[EMAIL]"), '<w:color w:val="000000"/>'))
                if i < len(authors):
                    bits.append(runs(", ", '<w:color w:val="000000"/>'))
            repl[span] = f"{tag}{ppr}{''.join(bits)}</w:p>"
    if not any(a.get("corresponding") for a in authors):
        WARNINGS.append("No author marked \"corresponding\": true — the '*Corresponding Author' line has no target.")
    if any(not a.get("email") for a in authors):
        WARNINGS.append("Some authors have no email — [EMAIL] placeholder inserted.")
    out, last = [], 0
    for (s, e) in sorted(repl):
        out += [head[last:s], repl[(s, e)]]
        last = e
    out.append(head[last:])
    return "".join(out)


def build_footer(xml, c):
    first = c["authors"][0]["name"].split()[-1]
    who = first + (" et al." if len(c["authors"]) > 2 else
                   f" and {c['authors'][1]['name'].split()[-1]}" if len(c["authors"]) == 2 else "")
    title = c.get("running_title") or c["title"]
    return xml.replace("<w:t>Author, Title</w:t>", f'<w:t xml:space="preserve">{xe(who)}, {xe(title)}</w:t>')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("content")
    ap.add_argument("output")
    ap.add_argument("--template", required=True, help="Official JRC_Template.docx")
    a = ap.parse_args()
    c = json.load(open(a.content, encoding="utf8"))
    for k in ("title", "authors", "affiliations", "abstract", "keywords"):
        if not c.get(k):
            sys.exit(f"content.json is missing required field '{k}'")
    words = len(c["abstract"].split())
    if not 150 <= words <= 250:
        WARNINGS.append(f"Abstract has {words} words — JRC requires 150–250.")

    zin = zipfile.ZipFile(a.template)
    doc = zin.read("word/document.xml").decode("utf8")
    sects = [m.start() for m in re.finditer("<w:sectPr", doc)]
    if len(sects) != 3 or '<w:pStyle w:val="Abstract"/>' not in doc:
        sys.exit("Template not recognised: expected the JRC template with 3 section breaks and an Abstract paragraph.")
    i = doc.find('<w:pStyle w:val="Abstract"/>')
    body_start = max(doc.rfind("<w:p ", 0, i), doc.rfind("<w:p>", 0, i))
    s2 = sects[1]  # two-column section break, inside the last body paragraph's pPr
    body_end = max(doc.rfind("<w:p ", 0, s2), doc.rfind("<w:p>", 0, s2))

    media = []
    new = build_header(doc[:body_start], c) + build_body(c, media) + doc[body_end:]
    minidom.parseString(new.encode("utf8"))

    rels = zin.read("word/_rels/document.xml.rels").decode("utf8")
    for rid, target, _, _ in media:
        rels = rels.replace("</Relationships>", f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/'
                            f'officeDocument/2006/relationships/image" Target="{target}"/></Relationships>')
    ctypes = zin.read("[Content_Types].xml").decode("utf8")
    for ext, mime in (("jpg", "image/jpeg"), ("jpeg", "image/jpeg"), ("png", "image/png")):
        if any(m[3] == ext for m in media) and f'Extension="{ext}"' not in ctypes:
            ctypes = ctypes.replace("<Default ", f'<Default Extension="{ext}" ContentType="{mime}"/><Default ', 1)

    with zipfile.ZipFile(a.output, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml":
                data = new.encode("utf8")
            elif item.filename == "word/_rels/document.xml.rels":
                data = rels.encode("utf8")
            elif item.filename == "[Content_Types].xml":
                data = ctypes.encode("utf8")
            elif item.filename == "word/footer1.xml":
                data = build_footer(data.decode("utf8"), c).encode("utf8")
            zout.writestr(item, data)
        for _, target, src, _ in media:
            zout.write(src, "word/" + target)
    print(f"Wrote {a.output}")
    for w in WARNINGS:
        print("WARNING:", w)


if __name__ == "__main__":
    main()
