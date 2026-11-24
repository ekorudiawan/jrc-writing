# jrc-writing — Agent Skill for Journal of Robotics and Control manuscripts

An [Agent Skills](https://agentskills.io) skill for writing, formatting and checking manuscripts for the
**Journal of Robotics and Control (JRC)**, Universitas Muhammadiyah Yogyakarta (e-ISSN 2715-5072).

Rules verified against the JRC Author Guidelines, Submission Checklist and the official `JRC_Template.docx` (24 Nov 2026).

## What it does
- Checks the JRC desk-rejection triggers first: official template, ≥ 60 journal references from the last 5 years (IEEE Xplore / ScienceDirect / Scopus), IEEE style
- Title without acronyms; abstract 150–250 words (Background 1–2, Method 2–3, Results ≥ 8, Conclusion 1–2 sentences)
- Similarity ≤ 25 % overall / ≤ 4 % per source, Word file ≤ 2 MB
- Optional stricter house rules: verified DOI for every reference, ≥ 80 % Scopus/WoS, 1–2 JRC citations, self-citation ≤ 10 %
- Generates a `.docx` on the official JRC template with `scripts/build_jrc_docx.py` (auto-numbered I./A./1), TABLE I., Fig. 1., [n])

## Install
```bash
npx skills add ekorudiawan/jrc-writing
```
Or copy `skills/jrc-writing/` into your agent's skills folder, e.g. `~/.claude/skills/`, `.agents/skills/`, `~/.cursor/skills/` or `~/.gemini/skills/`.

## Requirements for .docx generation
Python 3 (standard library only) and the official `JRC_Template.docx`, downloadable from
https://journal.umy.ac.id/index.php/jrc (the template belongs to JRC and is not redistributed here):

```bash
python3 skills/jrc-writing/scripts/build_jrc_docx.py content.json out.docx --template JRC_Template.docx
```

## License
MIT — see [LICENSE](LICENSE). Journal templates are not included and remain the property of their journals.

## Author
Eko Rudiawan Jamzuri — Politeknik Negeri Batam
