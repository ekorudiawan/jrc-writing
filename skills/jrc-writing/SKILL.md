---
name: jrc-writing
description: Use this skill whenever the user wants to write, draft, format, review, improve, or check a manuscript for the Journal of Robotics and Control (JRC). Trigger this skill for any task involving JRC paper writing, abstract drafting, section structuring, reference formatting (IEEE style), title creation, generating a .docx on the official JRC template, or compliance checking against JRC author guidelines and the submission checklist. Also trigger when the user mentions "JRC", "Journal of Robotics and Control", or asks for help with a robotics/control journal paper submission. Always use this skill if the user wants to prepare, revise, or evaluate any part of a JRC manuscript — even if they don't explicitly say "JRC skill".
---

# JRC Writing: Journal of Robotics and Control Manuscript Assistant

Helps authors write, structure, review and format manuscripts for the **Journal of
Robotics and Control (JRC)**, Universitas Muhammadiyah Yogyakarta.

> **Rules last verified: 24 Nov 2026** against the JRC home page, Author Guidelines
> (`/jrc/AG`), Submission Checklist (`/jrc/about/submissions`) and the official
> `JRC_Template.docx`. The JRC site sits behind a bot "Security Check", so automated
> fetching can fail — if a later task depends on a rule changing, ask the author to
> confirm on the site or to attach the current template.

| Item | Detail |
|---|---|
| ISSN | p-ISSN 2715-5056 · e-ISSN 2715-5072 · DOI prefix 10.18196/jrc |
| Publisher | Universitas Muhammadiyah Yogyakarta |
| Indexing | Scopus, SCImago, EBSCO; metrics change yearly — check the current SJR/quartile on scimagojr.com rather than quoting a fixed value |
| Frequency / review | 6 issues per year (bi-monthly) · double-blind, ≥ 2 reviewers, Turnitin screening at desk |
| License | Creative Commons (CC BY-SA 4.0 per site footer) |
| Website | https://journal.umy.ac.id/index.php/jrc · Author Guidelines: https://journal.umy.ac.id/index.php/jrc/AG |
| Contact | jrc@umy.ac.id (template footer) |

---

## 0. Hard Rejection Triggers (from the Submission Checklist)

JRC states it **rejects without review** a paper that:
1. does not follow the **JRC article template**, or
2. does not have **≥ 60 journal references published within the last 5 years**, taken from
   **IEEE Xplore, ScienceDirect or Scopus**, in **IEEE style**.

Other checklist items:
- **Similarity ≤ 25 % overall and ≤ 4 % from any single main source** (Turnitin or iThenticate);
  upload the similarity report as a supplementary file.
- Submit a **Microsoft Word file ≤ 2 MB**. If larger, upload a PDF and email the Word file to the
  journal; also upload the paper as a supplementary file as backup.
- Not previously published or under review elsewhere (or explained in Comments to the Editor).

Check these first in any review — a beautifully written paper that misses one is still desk-rejected.

---

## Quick Compliance Checklist

Rules come in two layers. **[JRC]** = stated by the journal. **[house]** = this author's stricter
internal rules — always apply them too, but label them as such when reporting.

- [ ] [JRC] English throughout; **≥ 6 pages** in the JRC template
- [ ] [JRC] Built on the official **JRC_Template.docx** (A4, Times New Roman, two columns) — see Sections E and I
- [ ] [JRC] Title: aim + method/model + objective, **no acronyms/abbreviations**, no symbols/special characters/math
- [ ] [JRC] Abstract: **150–250 words**, no citations, no symbols/footnotes/math; Background 1–2 · Methodology 2–3 · **Results ≥ 8** · Conclusions 1–2 sentences
- [ ] [JRC] Sections: Introduction → Method → Results and Discussion → Conclusion
- [ ] [JRC] **≥ 60 references**, journal papers (target 100 %), **last 5 years**, from IEEE Xplore / ScienceDirect / Scopus, IEEE style, via Zotero/Mendeley/EndNote
- [ ] [JRC] Similarity ≤ 25 % overall, ≤ 4 % single source; report uploaded
- [ ] [JRC] Word file ≤ 2 MB
- [ ] [house] Every reference has a verified DOI
- [ ] [house] ≥ 80 % of references verifiable in Scopus/WoS
- [ ] [house] 1–2 relevant JRC papers cited
- [ ] [house] Self-citation ≤ 10 %

---

## A. Title Guidelines

The title must describe the **research aim**, **method/model** and **objective**, written in
**full words** — no acronyms or abbreviations, and (per the template) no symbols, special
characters, footnotes or math.

**Bad:** "PID Control for UAV Stabilization" (acronyms PID, UAV)
**Good:** "Proportional-Integral-Derivative Controller Design for Unmanned Aerial Vehicle Attitude Stabilization Using Fuzzy Gain Scheduling"

Template capitalisation tip: capitalise "Using" only if "that uses" could replace it.

When crafting a title, ask: (1) main method/model? (2) system/object controlled or studied?
(3) goal or performance metric?

---

## B. Abstract Guidelines

- **150–250 words** (strict), **no citations**, no symbols, special characters, footnotes or math.
- Structure:

| Part | Length | Content |
|------|--------|---------|
| Background | 1–2 sentences | Context and problem motivation |
| Research Methodology | 2–3 sentences | Methods, tools, algorithms, datasets |
| Results | **≥ 8 sentences** | Quantitative findings, comparisons, metrics |
| Conclusions | 1–2 sentences | Main takeaway and significance |

> The **Results part is the most common failure point** — it needs at least 8 sentences with
> specific numbers, percentages, baseline comparisons and metrics.

```
[Background - 1-2 sentences: the problem and why it matters]
[Methodology - 2-3 sentences: proposed method/system/algorithm]
[Results - 8+ sentences: accuracy, error, comparisons with baselines, conditions, statistics]
[Conclusions - 1-2 sentences: significance and contribution]
```

In the template the abstract is one paragraph starting with the italic run-in head
"*Abstract*—", followed by "*Keywords*—" with keywords separated by **semicolons**.
Abbreviations defined in the abstract must be defined again at first use in the body.

---

## C. Manuscript Structure

### I. Introduction
Background and motivation · recent literature (last 5 years) · research gap / novelty ·
objectives · brief outline of the paper.

### II. Method
System design / algorithm / model architecture · hardware/software specifications ·
dataset · experimental setup · equations and parameters.

### III. Results and Discussion
Results in tables/figures · quantitative analysis · comparison with prior/baseline methods ·
discussion of findings, limitations, implications.

### IV. Conclusion
Key findings · contributions · future work.

Optional after Conclusion: **Acknowledgment** (no "e" after the g) and Appendix; then **References**.
Only introduce sub-headings when there are at least two of them at that level.

---

## D. References Guidelines

### D0. JRC requirements
- **Minimum 60 references**, journal papers (JRC: "primarily with 100% to journal papers")
- **Published within the last 5 years**
- From **IEEE Xplore, ScienceDirect or Scopus** databases
- **IEEE style**, numbered in order of first citation, managed with Zotero/Mendeley/EndNote
- Missing any of these is a stated **rejection** trigger (Section 0)

### D1. [house] Scopus/WoS indexing & DOI
1. ≥ **80 %** of references verifiable in Scopus or WoS (IEEE Xplore, Springer, Elsevier,
   Scopus-indexed MDPI, Taylor & Francis are fine). Not acceptable as primary sources:
   unindexed local journals, blogs, technical reports, websites, Wikipedia.
2. **Every reference has a valid DOI**, written `doi: 10.XXXX/XXXXX` at the end. No DOI →
   replace it. Never guess DOIs; verify at https://doi.org or Crossref.

Flag any entry that has no DOI, comes from a non-indexed/unknown journal, or cannot be found
in Scopus/WoS.

### D2. [house] Cite 1–2 JRC papers
Cite 1–2 **genuinely relevant** papers previously published in JRC (search the JRC site).
JRC papers also count toward the Scopus-indexed quota. Never force irrelevant citations. Proactively ask: "Have you checked JRC for recent related
papers you could cite?"

### D3. [house] Self-citation ≤ 10 %
60 refs → max 6; 70 refs → max 7. Self-citation = any paper (co-)authored by the submitting
authors. Self-citations are fine when directly relevant (e.g., prior work this paper extends),
but excessive self-citation may be flagged by reviewers as citation inflation. Count them and
warn if the limit is approached:
> "X of Y references (~Z %) appear to be self-citations; the recommended maximum is 10 %."

### D4. IEEE format (as used by the JRC template)
```
Journal:    [1] A. Author, B. Author, and C. Author, "Title of paper," Abbrev. Journal Name,
                vol. X, no. Y, pp. ZZZ–ZZZ, Mon. Year, doi: 10.XXXX/XXXXX.
Conference: [2] A. Author and B. Author, "Title of paper," in Proc. Conf. Name (ACRONYM),
                City, Country, Year, pp. ZZZ–ZZZ, doi: 10.XXXX/XXXXX.
Book:       [3] A. Author, Title of Book, Xth ed. City, Country: Publisher, Year, doi: ...
```
Template rules: list **all** authors unless there are **six or more** (then "et al."); capitalise
only the first word of a paper title (plus proper nouns); "unpublished" / "in press" for
unpublished or accepted work (avoid both under the house rules); give the English citation first
for translated journals.
In-text: "[3]" — not "Ref. [3]" or "reference [3]" except at sentence start ("Reference [3] was…").
Sentence punctuation goes after the bracket. See `references/ieee-examples.md` for more cases.

### D5. Zotero workflow (author preference)
- Style **IEEE**; insert with the Word plugin's **Insert Citation** — never type `[n]` by hand.
- Fill the **DOI field** of every item (right-click → Lookup / CrossRef).
- After adding/removing references click **Refresh** so citations and bibliography renumber together.
- If Zotero wasn't used, audit every in-text citation against the list after any reordering
  (parsing `word/document.xml` catches mismatches invisible in Word).

---

## E. Formatting Rules (from JRC_Template.docx)

**Page:** A4. Title block single column; body (from Abstract to References) **two columns**,
each 8.58 cm with 0.64 cm gap. Body margins: top 1.9 cm, bottom 2.54 cm, left/right 1.6 cm.
Don't change margins, column widths, line spacing or fonts; don't add page numbers.

| Element | Template style | Format |
|---|---|---|
| Title | *paper title* | Times New Roman 24 pt, centered |
| Authors | *Author* | 10 pt, superscript affiliation numbers; `*` marks the corresponding author |
| Affiliations | *Affiliation* | 10 pt; one line per institution |
| Emails | — | "Email: ¹ a@x, ² b@y …" then "*Corresponding Author" |
| Abstract | *Abstract* | 9 pt bold, justified; italic run-in "*Abstract*—" |
| Keywords | *Keywords* | 9 pt bold italic, "*Keywords*—k1; k2; k3" |
| Heading 1 | *Heading 1* | Small caps, centered, auto Roman: **I. INTRODUCTION** |
| Heading 2 | *Heading 2* | Italic, auto letter: *A. Subheading* |
| Heading 3 | *Heading 3* | Italic run-in, auto "1)" |
| Heading 4 | *Heading 4* | Italic run-in, auto "a)" |
| Acknowledgment / References heads | *Heading 5* | Small caps, unnumbered |
| Body text | *Body Text* | 10 pt, justified, first-line indent 0.51 cm |
| Bullets | *bullet list* | 10 pt |
| Table title | *table head* | 8 pt small caps, auto "**TABLE I.**", **above** the table |
| Table text | *table col head* / *table copy* | 8 pt |
| Figure caption | *figure caption* | 8 pt, auto "**Fig. 1.**", **below** the figure |
| References | *references* | 8 pt, auto "[1]", hanging indent |

**Do not type numbers** for headings, tables, figures or references — the template styles
number them automatically.

**Figures and tables:** place at the top or bottom of columns, after they are cited; large ones
may span both columns. Write "Fig. 1" even at the start of a sentence. Axis labels in words with
units in parentheses — "Temperature (K)", not "Temperature/K"; figure label text 8 pt.

**Equations:** numbered consecutively "(1)" flush right; the template puts each equation in a
borderless two-cell table (equation | number). Italicise Roman variables, not Greek; define
symbols right before or after. In text write "(1)", not "Eq. (1)" — except "Equation (1) is…"
at sentence start.

**Other template conventions:** SI units (English units only in parentheses), "0.25" not ".25",
define abbreviations at first use in the body even if defined in the abstract (IEEE, SI, DC, RMS
need no definition), "data" is plural, "et al." has no period after "et", no footnotes in the
abstract or reference list.

---

## F. Common Mistakes to Avoid

| Mistake | Correction |
|--------|------------|
| Not using the JRC template | Rebuild on JRC_Template.docx — otherwise desk rejection |
| < 60 journal references / older than 5 years | Add recent journal papers from IEEE Xplore, ScienceDirect, Scopus |
| Similarity > 25 % or > 4 % from one source | Paraphrase/cite properly; re-run Turnitin before submitting |
| Word file > 2 MB | Compress images, or upload PDF + email the Word file |
| Acronyms or math in title | Spell out all terms |
| Abstract < 150 or > 250 words | Adjust; Results needs ≥ 8 sentences |
| Citations in abstract | Remove them |
| Manually typed heading/table/figure numbers | Use the template styles (auto-numbering) |
| "Eq. (1)", "Ref. [3]" mid-sentence | Write "(1)" and "[3]" |
| Non-IEEE citation format | Reformat with Zotero IEEE style |
| [house] Missing DOI / non-indexed sources > 20 % | Replace with indexed journal papers with DOI |
| [house] No JRC citation | Cite 1–2 relevant JRC papers |
| [house] Self-citation > 10 % | Replace with other authors' work |

---

## G. Workflow for Assisting Authors

1. **Identify the topic** — system, method, contributions, authors/affiliations/emails, corresponding author.
2. **Title** — no acronyms/symbols; aim + method + objective.
3. **Abstract** — word count, structure, Results depth.
4. **Sections** — Introduction, Method, Results and Discussion, Conclusion.
5. **References** — Section D (JRC + house rules); count, recency, sources, DOI, JRC citations, self-citation.
6. **Build the .docx** on the template (Section I) when a file is wanted.
7. **Final check** — Section 0 rejection triggers first, then the Quick Compliance Checklist.

### Versioned copies after major updates
After a significant revision of a manuscript .docx, save `<BaseName>_v<N>.docx` next to the main
file (start at `_v1`). Major = structural changes, rewritten paragraphs/new results, multi-part
compliance fixes, or anything the author asks to preserve. Typos and formatting-only tweaks don't
need a new version. Save to the author's connected folder when available.

---

## H. Reference Files

- `references/ieee-examples.md` — more IEEE examples
- `references/abstract-examples.md` — sample JRC-compliant abstracts

---

*Skill created for Polibatam Robotics Engineering Technology lecturers preparing manuscripts for JRC submission.*

---

## I. Generating the .docx from JRC_Template.docx

Always build on the **official template file** — recreating it from scratch loses its styles,
auto-numbering, header/footer and three section breaks, and an off-template paper is rejected.

**Template:** the JRC site's bot check usually blocks automated downloads, so get
`JRC_Template.docx` from the author (attachment or connected folder); if none is available,
ask for it. Use `scripts/build_jrc_docx.py` if bundled; otherwise write Appendix A to
`build_jrc_docx.py`.

```bash
python3 build_jrc_docx.py content.json "JRC_Manuscript_<Topic>_v1.docx" --template JRC_Template.docx
```

1. Write `content.json` (schema in the script docstring): title, running_title, authors (name,
   affil numbers, email, `"corresponding": true`), affiliations, abstract, keywords, `sections`
   (blocks `p`, `h2`, `h3`, `bullets`, `equation`, `figure`, `table`), acknowledgment, references.
   Headings in Title Case without numbers; references without "[n]". Inline markup:
   `**bold**`, `*italic*`, `^{sup}`, `_{sub}`.
2. Run it. It fills the title block, regenerates the two-column body with the template's own
   styles (auto I./A./1), TABLE I., Fig. 1., [n]), places equations in the template's two-cell
   table, and updates the "Author, Title" footer.
3. Relay its **WARNING** lines (abstract outside 150–250 words, < 60 references, missing
   emails/corresponding author, missing images → yellow `[INSERT FIGURE n HERE]`).
4. Verify: `soffice --headless --convert-to pdf out.docx`, rasterise with `pdftoppm -r 70 -png`,
   look at the pages and count them (≥ 6). LibreOffice doesn't draw Word OMML equations — the
   script writes equations as plain text by default; pass `"omml"` for native Word equations.
5. Check the file is ≤ 2 MB (compress figures if not), save a versioned copy, deliver.

Figures are limited to one column width (~8.5 cm). The header's volume/issue/DOI lines are left
for the editor.

**Template facts (troubleshooting):** three `<w:sectPr>` — (1) end of the single-column title
block, (2) inside the last body paragraph's `pPr`, `<w:cols w:num="2">`, (3) body-level closing
section. Body = from the *Abstract* paragraph up to the paragraph holding sectPr 2; keep that
paragraph. Heading 1/2 use `numId 1`; the template's Heading 3/4 use `numId 9`.

---

## Appendix A — `build_jrc_docx.py`

Tested 24 Nov 2026 against the official JRC_Template.docx (renders correctly in LibreOffice). Write it to disk unchanged when no bundled copy exists.

```python
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
```
