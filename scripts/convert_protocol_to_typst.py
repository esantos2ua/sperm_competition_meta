#!/usr/bin/env python3
"""
Convert protocol/02_update_protocol.md into protocol/02_update_protocol.typ
and compile with typst to protocol/02_update_protocol.pdf.
"""

import re
import os
import subprocess

def clean_cell_text(text):
    t = text.strip()
    # Math replacements
    t = t.replace("*g*", "$g$")
    t = t.replace("*N*", "$N$")
    t = t.replace("*I*²", "$I^2$")
    t = t.replace("|*g*|", "$|g|$")
    # Bold
    t = re.sub(r'\*\*([^*]+)\*\*', r'*\1*', t)
    # Italics
    t = re.sub(r'(?<!\*)\b\*([A-Za-z0-9_ -]+)\*\b(?!\*)', r'_\1_', t)
    # Citations in table
    def cite_repl(m):
        keys = re.findall(r'@([a-zA-Z0-9_-]+)', m.group(1))
        return " " + " ".join(f"@{k}" for k in keys)
    t = re.sub(r'\[(-?@[^\]]+)\]', cite_repl, t)
    return t

def md_table_to_typst(md_table_text, table_num):
    lines = [l.strip() for l in md_table_text.strip().split('\n') if l.strip()]
    if len(lines) < 3:
        return md_table_text
    
    raw_header = [c.strip() for c in lines[0].strip('|').split('|')]
    data_rows = []
    for line in lines[2:]:
        cols = [c.strip() for c in line.strip('|').split('|')]
        while len(cols) < len(raw_header):
            cols.append("")
        data_rows.append(cols[:len(raw_header)])

    if table_num == 1:
        col_spec = "(1.3fr, 1.9fr, 1.9fr, 2.2fr)"
        size_spec = "8pt"
        align_spec = "(left, left, left, left)"
    elif table_num == 2:
        col_spec = "(1.8fr, 2.6fr, 2.6fr)"
        size_spec = "7.5pt"
        align_spec = "(left, left, left)"
    else:
        col_spec = "(1.8fr, 5fr)"
        size_spec = "8pt"
        align_spec = "(left, left)"

    out = []
    out.append(f"// Table {table_num}")
    out.append("#align(center)[")
    out.append(f"  #set text(size: {size_spec})")
    out.append("  #table(")
    out.append(f"    columns: {col_spec},")
    out.append(f"    align: {align_spec},")
    out.append("    stroke: 0.4pt + rgb(\"#cbd5e1\"),")
    out.append("    fill: (col, row) => if row == 0 { rgb(\"#1a4f8a\") } else if calc.odd(row) { rgb(\"#f8fafc\") } else { white },")
    out.append("    inset: (x: 5pt, y: 4.5pt),")
    out.append("    table.header(")
    for h in raw_header:
        h_clean = h.replace("**", "").replace("*", "").strip()
        out.append(f"      text(fill: white, weight: \"bold\")[{h_clean}],")
    out.append("    ),")

    for row in data_rows:
        for c in row:
            c_typ = clean_cell_text(c)
            out.append(f"    [{c_typ}],")
    out.append("  )")
    out.append("]")
    return "\n".join(out)

def convert():
    with open("protocol/02_update_protocol.md", "r") as f:
        raw = f.read()

    # Strip YAML frontmatter
    if raw.startswith("---"):
        parts = raw.split("---", 2)
        if len(parts) >= 3:
            content = parts[2].strip()
        else:
            content = raw
    else:
        content = raw

    # 1. Protect code blocks
    code_blocks = []
    def cb_repl(m):
        code_blocks.append(m.group(0))
        return f"__CODE_BLOCK_PLACEHOLDER_{len(code_blocks)-1}__"
    content = re.sub(r'```[\s\S]*?```', cb_repl, content)

    # 2. Protect tables
    tables = []
    def tbl_repl(m):
        tables.append(m.group(0))
        return f"__TABLE_PLACEHOLDER_{len(tables)-1}__"
    content = re.sub(r'(\|[^\n]+\|\n\|[- :|]+\|\n(?:\|[^\n]+\|\n)+)', tbl_repl, content)

    # 3. Math replacements across full text
    math_replacements = [
        (r'\*I\*²', r'$I^2$'),
        (r'\*I\*²_total', r'$I_"total"^2$'),
        (r'\|\*g\*\|', r'$|g|$'),
        (r'\*v\* = \(\*n\*₁\+\*n\*₂\)/\(\*n\*₁\*n\*₂\) \+ \*g\*²/\(2\(\*n\*₁\+\*n\*₂\)\) with \*n\*₁ = \*n\*₂ = \*N\*/2',
         r'$v = (n_1 + n_2)/(n_1 n_2) + g^2 / (2(n_1 + n_2))$ with $n_1 = n_2 = N/2$'),
        (r'\*p\* > 0\.28', r'$p > 0.28$'),
        (r'\*P\* ≤ 0\.05', r'$P <= 0.05$'),
        (r'\*r\* = 0\.5', r'$r = 0.5$'),
        (r'\*r\* = 0\.3', r'$r = 0.3$'),
        (r'\*r\* = 0\.7', r'$r = 0.7$'),
        (r'\*z\*-score', r'$z$-score'),
        (r'\*R\*²', r'$R^2$'),
        (r'\*g\*', r'$g$'),
        (r'\*N\*s', r'$N$s'),
        (r'\*N\*', r'$N$'),
        (r'\*n\*₁', r'$n_1$'),
        (r'\*n\*₂', r'$n_2$'),
        (r'\*SCR \+ SCR\*²', r'$"SCR" + "SCR"^2$'),
        (r'\$SCR \+ SCR\^2\$', r'$"SCR" + "SCR"^2$'),
        (r'\*p\*', r'$p$'),
    ]
    for pattern, repl in math_replacements:
        content = re.sub(pattern, repl, content)

    # 4. Citations: [@key] -> @key, [@key1; @key2] -> @key1 @key2
    def cite_repl(m):
        keys = re.findall(r'@([a-zA-Z0-9_-]+)', m.group(1))
        return " " + " ".join(f"@{k}" for k in keys) + " "
    content = re.sub(r'\[(-?@[^\]]+)\]', cite_repl, content)
    content = re.sub(r'\[-@([a-zA-Z0-9_-]+)\]', r'@\1', content)

    # 5. Superscripts: <sup>x</sup> -> #super[x]
    content = re.sub(r'<sup>([^<]+)</sup>', r'#super[\1]', content)

    # 6. Blockquotes
    # Collect lines starting with >
    lines = content.split('\n')
    new_lines = []
    in_quote = False
    quote_buf = []

    for line in lines:
        if line.startswith('>') and ('Note' in line or 'Pilot' in line or 'Additional' in line or in_quote):
            in_quote = True
            quote_buf.append(line.lstrip('>').strip())
        else:
            if in_quote:
                quote_text = " ".join(quote_buf)
                new_lines.append(f"\n#note[\n{quote_text}\n]\n")
                in_quote = False
                quote_buf = []
            new_lines.append(line)
    if in_quote:
        quote_text = " ".join(quote_buf)
        new_lines.append(f"\n#note[\n{quote_text}\n]\n")

    content = "\n".join(new_lines)

    # 7. Headings
    def heading_repl(m):
        level = len(m.group(1))
        title = m.group(2).strip()
        clean_title = re.sub(r'^[0-9]+(\.[0-9]+)*\.?\s*', '', title)
        return "\n" + ("=" * level) + f" {clean_title}\n"
    content = re.sub(r'^(#{1,4})\s+(.+)$', heading_repl, content, flags=re.MULTILINE)

    # 8. Bold and Italics across multiline spans:
    # First: bold with potential nested italics:
    def bold_repl(m):
        inner = m.group(1)
        # convert inner *italic* to _italic_
        inner = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'_\1_', inner)
        return f"*{inner}*"
    content = re.sub(r'\*\*(.+?)\*\*', bold_repl, content, flags=re.DOTALL)

    # Second: remaining single-asterisk italics
    content = re.sub(r'(?<!\*)\b\*([A-Za-z0-9_ -]+)\*\b(?!\*)', r'_\1_', content)

    # Horizontal rules
    content = re.sub(r'^---\s*$', r'#v(0.5em)\n#line(length: 100%, stroke: 0.5pt + rgb("#cbd5e1"))\n#v(0.5em)', content, flags=re.MULTILINE)

    # Restore tables
    for i, t_text in enumerate(tables):
        typ_tbl = md_table_to_typst(t_text, i + 1)
        content = content.replace(f"__TABLE_PLACEHOLDER_{i}__", typ_tbl)

    # Restore code blocks
    for i, c_text in enumerate(code_blocks):
        content = content.replace(f"__CODE_BLOCK_PLACEHOLDER_{i}__", c_text)

    # Clean up pandoc / markdown leftovers
    content = content.replace("::: {#refs}\n:::", "")
    content = re.sub(r'=\s+References\s*(\n.*)?$', '', content, flags=re.DOTALL)

    # Pre-clean any accidental unclosed * inside parentheses or words
    # e.g., (SCR 1 = *Gobius ... Neat @key*; no row...) -> make sure it's valid
    # In Typst, *bold* must have matching *
    # Let's fix specific edge cases:
    content = content.replace("*quality_ (−0.384, −0.845 to 0.076) and _quality*", "_quantity_ (−0.384, −0.845 to 0.076) and _quality_")
    content = content.replace("sperm *quantity_", "sperm _quantity_")
    content = content.replace("_quality*", "_quality_")
    content = content.replace("major faces *one** minor", "major faces *one* minor")
    content = content.replace("esantos2@ualberta.ca", "esantos2\\@ualberta.ca")

    # Document Header Preamble
    preamble = """// ─────────────────────────────────────────────────────────────────────────────
// Sperm competition games between majors and minors: Update & Reconciliation Protocol
// Typst Protocol Source (compiled to protocol/02_update_protocol.pdf)
// ─────────────────────────────────────────────────────────────────────────────

#set page(
  paper: "a4",
  margin: (top: 2.5cm, bottom: 2.5cm, left: 2.8cm, right: 2.8cm),
  header: context if counter(page).get().first() > 1 [
    #text(size: 8.5pt, fill: rgb("#718096"))[
      _Sperm Competition Games: Protocol for Update and Cross-Synthesis Reconciliation_
      #h(1fr)
      #counter(page).display("1")
    ]
  ],
  footer: context [
    #align(center)[#text(size: 9pt, fill: rgb("#718096"))[#counter(page).display("1")]]
  ]
)

#set text(font: "Libertinus Serif", size: 10pt, lang: "en", hyphenate: true)
#set heading(numbering: "1.1.")
#set par(justify: true, leading: 0.65em, spacing: 1.2em)

#let link-blue = rgb("#1a4f8a")
#show link: it => text(fill: link-blue, it)
#show ref: it => text(fill: link-blue, it)
#show cite: it => text(fill: link-blue, it)

#let note(body) = block(
  fill: rgb("#f8fafc"),
  stroke: 1pt + rgb("#cbd5e1"),
  inset: (x: 10pt, y: 8pt),
  radius: 4pt,
  width: 100%,
  [#text(size: 9.5pt)[#body]]
)

#align(center)[
  #v(0.5em)
  #text(size: 17pt, weight: "bold", fill: rgb("#1a365d"))[
    Sperm competition games between majors and minors: protocol for the update, cross-synthesis reconciliation, and publication of a meta-regression of species with alternative reproductive tactics
  ]
  #v(1em)
  #text(size: 11pt)[
    *Lygia Aguiar Del Matto*#super[b] & *Eduardo S. A. Santos*#super[a,1]
  ]
  #v(0.4em)
  #text(size: 9pt, fill: rgb("#4a5568"))[
    #super[a] Department of Biological Sciences, Faculty of Science, University of Alberta, Edmonton, AB, Canada \\
    #super[b] Departamento de Zoologia, Instituto de Biociências, Universidade de São Paulo, São Paulo, SP, Brazil \\
    #super[1] Corresponding author: #link("mailto:esantos2@ualberta.ca")[esantos2\\@ualberta.ca]
  ]
  #v(0.6em)
  #text(size: 9.5pt, weight: "bold", fill: rgb("#2b6cb0"))[
    PRISMA-EcoEvo Systematic Review & Meta-Analysis Protocol • Version 0.2 (September 2026)
  ]
  #v(0.8em)
  #line(length: 100%, stroke: 1.2pt + rgb("#1a4f8a"))
  #v(0.8em)
]

"""

    bib_section = """

#v(1em)
#line(length: 100%, stroke: 1pt + rgb("#1a4f8a"))
#v(0.5em)

= References

#set text(size: 9pt)
#bibliography("references.bib", style: "vancouver", title: none)
"""

    full_typst = preamble + content + bib_section

    with open("protocol/02_update_protocol.typ", "w") as f:
        f.write(full_typst)
    print("Wrote protocol/02_update_protocol.typ successfully.")

if __name__ == "__main__":
    convert()
