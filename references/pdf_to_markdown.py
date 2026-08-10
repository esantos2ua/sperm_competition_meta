# -*- coding: utf-8 -*-
"""High-fidelity PDF -> Markdown for LygiaMattoDissertationFinal.pdf

Fixes the specific failures found in the markitdown benchmark:
  * heading hierarchy from the font-size ladder (19.9pt -> #, 16.1pt -> ##)
  * italic / bold spans preserved as *...* / **...**
  * literal markdown metacharacters escaped (the * wildcards and reference flags)
  * rotated text read in correct order (PyMuPDF, not reversed)
  * the 4 tables rebuilt as valid single-header markdown tables
  * running footers stripped; page provenance kept as HTML comments
  * paragraphs re-flowed from first-line indent; line-break hyphens rejoined
  * raster images extracted to figures/ and linked; vector figures given placeholders
"""
import fitz, pdfplumber, re, os, json

PDF = "/sessions/busy-gallant-hypatia/mnt/uploads/LygiaMattoDissertationFinal.pdf"
OUT = "/sessions/busy-gallant-hypatia/mnt/outputs/hifi"
FIG = os.path.join(OUT, "figures")

# ---------------------------------------------------------------- table specs
# (physical page, y0, y1, column x-boundaries, header cells, merge rule)
TABLE1_COLS = [70, 175, 600]
APPX_COLS   = [70, 155, 212, 240, 275, 410, 466, 600]
APPX_HEADER = ["Species", "Hedges' g", "N", "SCR",
               "Original response variable", "Variable type", "Source"]

# y-ranges whose raw lines are suppressed because the table is supplied verbatim
SUPPRESS = {23: [(135, 305)], 26: [(175, 360)]}

TABLE_REGIONS = {
    19: [(630, 780, TABLE1_COLS, ["Category", "Response variables"], "table1")],
    20: [(70,  515, TABLE1_COLS, ["Category", "Response variables"], "table1")],
}
TABLE_REGIONS[39] = [(135, 790, APPX_COLS, APPX_HEADER, "appendix")]
for p in range(40, 53):
    # pp. 40-52 repeat the header at y~81 and the first data row sits at y~117
    TABLE_REGIONS[p] = [(75, 790, APPX_COLS, APPX_HEADER, "appendix")]

# Tables 2 and 3 are 3-row tables whose cells wrap across 3-4 physical lines each.
# Transcribed directly from the page (verified against the rendered page image),
# because no generic row-merge rule recovers them reliably.
TABLE2_MD = """| Model | Moderators | Random effects | I²study identity % (95% CI) | I²species identity % (95% CI) | I²phylogeny % (95% CI) | I²total % (95% CI) |
| --- | --- | --- | --- | --- | --- | --- |
| Null Model | NA | study identity + species + phylogeny | 55.46 (53.54 to 57.38) | 9.35 (7.43 to 11.28) | 18.38 (16.46 to 20.30) | 83.21 (81.60 to 85.44) |
| Meta-regression model 1 | variable type | study identity + species | 76.02 (74.10 to 77.94) | 7.50 (5.58 to 9.42) | NA | 83.52 (81.60 to 85.44) |
| Meta-regression model 2 | variable type : sperm competition rank | study identity + species | 46.24 (44.32 to 48.16) | 36.33 (34.41 to 38.25) | NA | 82.57 (80.65 to 84.50) |"""

TABLE3_MD = """| Model | Moderators | Random effects | Intercept | *t*-value | *p*-value |
| --- | --- | --- | --- | --- | --- |
| Null Model | NA | study identity + species + phylogeny | -0.323 | -0.633 | 0.528 |
| Meta-regression model 1 | variable type | study identity + species | -0.338 | -0.664 | 0.507 |
| Meta-regression model 2 | variable type : sperm competition rank | study identity + species | -0.610 | -1.067 | 0.288 |"""

# Vector figures: forest plots on physical pp. 24 and 25. Their axis/label text is
# emitted as orphan fragments; replace the fragment soup with a described placeholder.
VECTOR_FIG = {
    24: ("Figure 2", "Horizontal forest plot. y-axis categories (top to bottom): "
                     "Quality, Production (Quantity), Production (GSI), Allocation. "
                     "x-axis: Hedge's g, ticks at -2, 0, 2, 4; vertical dashed line at 0."),
    25: ("Figure 3", "Grouped forest plot. x-axis: Variable Type (Production (Quantity), "
                     "Production (GSI), Quality). y-axis: Hedge's g, ticks to -4. "
                     "Colour legend: Sperm Competition Rank 1-5; horizontal dashed line at 0."),
}

AXIS_LABELS = {
    "Hedge's g", "s'egdeH", "Variable Type", "Quality", "Allocation",
    "Production", "(GSI)", "(Quantity)", "Production (GSI)",
    "Production (Quantity)", "Sperm Competition Rank", "g",
}

MD_ESCAPE = re.compile(r"([*_`\[\]<>#|~\\])")


def esc(s):
    return MD_ESCAPE.sub(r"\\\1", s)


def span_md(text, font):
    """Wrap a span in emphasis markers, escaping its literal content first."""
    f = font.lower()
    ital = ("italic" in f) or ("oblique" in f)
    bold = "bold" in f
    lead = len(text) - len(text.lstrip())
    trail = len(text) - len(text.rstrip())
    core = text.strip()
    if not core:
        return text
    body = esc(core)
    if bold and ital:
        body = f"***{body}***"
    elif bold:
        body = f"**{body}**"
    elif ital:
        body = f"*{body}*"
    return text[:lead] + body + (" " * trail if trail else "")


# ------------------------------------------------------------------- tables
def build_table(page, y0, y1, cols, header, rule):
    words = [w for w in page.extract_words(x_tolerance=1.5, y_tolerance=2)
             if y0 <= w["top"] <= y1]
    if not words:
        return None
    # greedy y-clustering (fixed-modulus bucketing collapses adjacent table rows)
    rows = {}
    order = []
    for w in sorted(words, key=lambda z: z["top"]):
        placed = False
        for k in order:
            if abs(w["top"] - k) <= 4.0:
                rows[k].append(w); placed = True; break
        if not placed:
            order.append(w["top"]); rows[w["top"]] = [w]

    def cellify(ws):
        cells = [[] for _ in range(len(cols) - 1)]
        for w in sorted(ws, key=lambda z: z["x0"]):
            for i in range(len(cols) - 1):
                if cols[i] <= w["x0"] < cols[i + 1]:
                    cells[i].append(w["text"])
                    break
        return [" ".join(c).strip() for c in cells]

    raw = [cellify(rows[k]) for k in sorted(rows)]
    # drop the printed header lines and the running footer
    raw = [r for r in raw if not (len(" ".join(r).strip()) <= 3 and " ".join(r).strip().isdigit())]
    hdr_words = {h.lower() for h in header}
    raw = [r for r in raw if not (set(x.lower() for x in r if x) & hdr_words
                                  and len([x for x in r if x]) >= 2)]
    raw = [r for r in raw if any(r)]
    # drop header remnants ("type" from the wrapped "Variable type" header)
    raw = [r for r in raw if not (len([x for x in r if x]) == 1
                                  and " ".join(r).strip().lower() in {"type", "g", "variable"})]

    recs = []
    for r in raw:
        if rule == "table1":
            # every line is its own response variable; carry the category forward
            if not r[0] and recs:
                r[0] = recs[-1][0]
            recs.append(r)
        else:  # appendix: a new record is a line carrying a numeric Hedges' g
            new = bool(re.fullmatch(r"-?\d+\.\d+", r[1].strip()))
            if new or not recs:
                recs.append(r)
            else:
                for i, v in enumerate(r):
                    if v:
                        recs[-1][i] = (recs[-1][i] + " " + v).strip()
    if not recs:
        return None
    out = ["| " + " | ".join(esc(h) for h in header) + " |",
           "| " + " | ".join("---" for _ in header) + " |"]
    for r in recs:
        out.append("| " + " | ".join(esc(c) for c in r) + " |")
    return "\n".join(out)


# ------------------------------------------------------------------ main
doc = fitz.open(PDF)
plumb = pdfplumber.open(PDF)

# extract raster images
img_by_page = {}
for pno in range(1, len(doc) + 1):
    for i, im in enumerate(doc[pno - 1].get_images(full=True)):
        xref = im[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n > 4:
            pix = fitz.Pixmap(fitz.csRGB, pix)
        name = f"p{pno:02d}_img{i}.png"
        dst = os.path.join(FIG, name)
        if not os.path.exists(dst):
            pix.save(dst)
        img_by_page.setdefault(pno, []).append(name)

body = []
for pno in range(1, len(doc) + 1):
    page = doc[pno - 1]
    regions = TABLE_REGIONS.get(pno, [])
    tbl_spans = [(r[0], r[1]) for r in regions] + SUPPRESS.get(pno, [])

    body.append(f"\n<!-- physical page {pno} (printed {pno-2 if pno>2 else '-'}) -->\n")

    if pno in VECTOR_FIG:
        tag, desc = VECTOR_FIG[pno]
        body.append(f"> **[{tag} — vector plot, not extractable as text]** {desc}\n")

    for nm in img_by_page.get(pno, []):
        body.append(f"![Embedded image, page {pno}](figures/{nm})\n")

    lines = []
    for blk in page.get_text("dict")["blocks"]:
        for ln in blk.get("lines", []):
            txt = "".join(s["text"] for s in ln["spans"]).strip()
            if not txt:
                continue
            y = ln["bbox"][1]
            x0 = ln["bbox"][0]
            size = max(s["size"] for s in ln["spans"])
            # running footer
            if y > 740 and re.fullmatch(r"\d{1,3}", txt):
                continue
            # inside a rebuilt table region -> skip (rebuilt separately)
            if any(a - 8 <= y <= b for a, b in tbl_spans):
                continue
            # vector-figure label soup
            if pno in VECTOR_FIG and not txt.startswith("Figure") and (
                    "●" in txt
                    or re.fullmatch(r"[\s\-−0-9.]+", txt)
                    or txt.strip() in AXIS_LABELS):
                continue
            md = "".join(span_md(s["text"], s["font"]) for s in ln["spans"]).strip()
            lines.append({"y": y, "x0": x0, "size": size, "md": md, "raw": txt})

    lines.sort(key=lambda l: l["y"])

    para = []
    pending = []

    def flush():
        if not para:
            return
        t = ""
        for i, s in enumerate(para):
            if not t:
                t = s
            elif t.endswith("-") and not t.endswith("--"):
                # Join across the break but KEEP the hyphen. In this document every
                # line-final hyphen is a compound ("meta-regression"), a URL, a page
                # range, a unit exponent, or a minus sign -- none is true word
                # hyphenation, so dropping it corrupts text and numbers
                # (e.g. "-3.105 to -" + "2.177" must not become "to 2.177").
                t = t + s.lstrip()
            else:
                t = t.rstrip() + " " + s.lstrip()
        body.append(re.sub(r"\s{2,}", " ", t).strip() + "\n")
        para.clear()
        while pending:
            body.append(pending.pop(0) + "\n")

    for l in lines:
        sz, md, raw = l["size"], l["md"], l["raw"]
        if sz >= 19:
            flush(); body.append(f"# {esc(raw)}\n"); continue
        if 15.5 <= sz < 19:
            flush(); body.append(f"## {esc(raw)}\n"); continue
        if sz >= 13.5 and pno <= 2:
            flush(); body.append(f"**{esc(raw)}**\n"); continue
        if re.match(r"^(Table|Figure|Supplementary Table)\s+\d", raw):
            flush(); para.append(md)
            if pno == 23 and raw.startswith("Table 2."):
                pending.append(TABLE2_MD)
            if pno == 26 and raw.startswith("Table 3."):
                pending.append(TABLE3_MD)
            continue
        if l["x0"] > 100 and para:                # first-line indent = new paragraph
            flush()
        para.append(md)
    flush()

    for (y0, y1, cols, header, rule) in regions:
        t = build_table(plumb.pages[pno - 1], y0, y1, cols, header, rule)
        if t:
            body.append(t + "\n")


plumb.close()

txt = "\n".join(body)
txt = re.sub(r"\n{3,}", "\n\n", txt)
hdr = ("<!-- Converted from LygiaMattoDissertationFinal.pdf with a custom\n"
       "     PyMuPDF + pdfplumber pipeline (see hifi.py). Headings, italics,\n"
       "     escaped literals, table structure and figure placeholders preserved.\n"
       "     Page comments give PHYSICAL page indices; printed folios run 2 behind. -->\n\n")
open(os.path.join(OUT, "DelMatto2018_dissertation.md"), "w").write(hdr + txt)
print("written", len(hdr + txt), "chars")
