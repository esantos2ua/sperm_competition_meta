#!/usr/bin/env python3
"""
Reformat protocol/02_update_protocol.typ:
1. Unwrap lines within paragraphs and list items so each logical unit is on a single line.
2. Format Table 1 cleanly (4 cells per row on one line).
3. Preserve Table 2 exactly as formatted.
4. Clean up citation spacing and punctuation (e.g. '@key .' -> '@key.').
5. Fix any mismatched bold/italic syntax.
6. Compile to protocol/02_update_protocol.pdf and verify exit code 0.
"""

import re
import subprocess

def fix_mismatches_and_citations(t):
    replacements = [
        (r'\*Web of Knowledge_ and _Scopus_ last updated _16 May 2017\*', r'_Web of Knowledge_ and _Scopus_ last updated _16 May 2017_'),
        (r'\*50 sources_ and _29 species\*', r'_50 sources_ and _29 species_'),
        (r'\*Parablennius parvicornis_ and _Parablennius sanguinolentus parvicornis\*', r'_Parablennius parvicornis_ and _Parablennius sanguinolentus parvicornis_'),
        (r'\(observation\) ID_ and _species\*', r'(observation) ID* and *species*'),
        (r'\*effect-size \(observation\) ID and _species_', r'*effect-size (observation) ID* and *species*'),
        (r'`"male_ _morph\*"`', r'`"male* morph*"`'),
        (r'`"post\*copulato\*"`', r'`"post*copulato*"`'),
        (r'`"behavio\*r\*"`', r'`"behavio*r*"`'),
        (r'\*orchard_ and _bubble\*', r'*orchard* and *bubble*'),
        (r'\*index type_ and _body mass\*', r'*index type* and *body mass*'),
        (r'\*tactic plasticity_ and _minor tactic type\*', r'*tactic plasticity* and *minor tactic type*'),
        (r'\*leave-one-study-out_ and _leave-one-species-out\*', r'*leave-one-study-out* and *leave-one-species-out*'),
        (r'Quality \*107_ and Allocation _11\*', r'Quality *107* and Allocation *11*'),
        (r'\*ordered/continuous_ moderator with a _linear and quadratic term\*', r'*ordered/continuous* moderator with a *linear and quadratic term*'),
        (r'\*complete the original screening_ by retrieving and screening the _14 title/abstract-eligible', r'*complete the original screening* by retrieving and screening the *14 title/abstract-eligible*'),
        (r'substituted a \*species-level five-level rank_ and fitted it as an _unordered factor\*', r'substituted a _species-level five-level rank_ and fitted it as an _unordered factor_'),
        (r'\(\*SCR 1 = \*Gobius niger_ only, 15 effect sizes; SCR 5 = _Axoclinus nigricaudus\* only, 3 effect sizes, all from Neat @neatMaleParasiticSpawning2001 \*; no row has rank 0\)',
         r'(*SCR 1 = _Gobius niger_ only, 15 effect sizes; SCR 5 = _Axoclinus nigricaudus_ only, 3 effect sizes, all from Neat @neatMaleParasiticSpawning2001*; no row has rank 0)'),
        (r'\*sneak\\\*, _satellite_, \*parasitic spawn\\\*, \*bourgeois\*', r'*sneak\**, _satellite_, *parasitic spawn\**, *bourgeois*'),
        (r'\*Web of Knowledge_ and _Scopus\*', r'_Web of Knowledge_ and _Scopus_'),
    ]
    for pattern, repl in replacements:
        t = re.sub(pattern, repl, t)

    # Citation and punctuation cleanup:
    t = re.sub(r' +@([a-zA-Z0-9_-]+)', r' @\1', t)
    t = re.sub(r'(@[a-zA-Z0-9_-]+) +([.,;:!?])', r'\1\2', t)
    t = re.sub(r'(\w) +([.,;:!?])', r'\1\2', t)
    t = re.sub(r'[ \t]{2,}', ' ', t)
    return t

def reformat():
    with open('protocol/02_update_protocol.typ', 'r') as f:
        text = f.read()

    # Pre-defined clean preamble
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
  ],
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
  [#text(size: 9.5pt)[#body]],
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
]"""

    references = """= References

#set text(size: 9pt)
#bibliography("references.bib", style: "vancouver", title: none)"""

    # Locate body
    preamble_end = text.find('= Study Protocol')
    ref_start = text.find('= References')

    if preamble_end == -1 or ref_start == -1:
        print("Error: Could not find '= Study Protocol' or '= References'!")
        return

    body = text[preamble_end:ref_start].strip()

    # Extract tables
    m1 = re.search(r'(// Table 1\n#align\(center\)\[[\s\S]*?\n\]\n)', body)
    m2 = re.search(r'(// Table 2\n#align\(center\)\[[\s\S]*?\n\]\n)', body)

    if not m1 or not m2:
        print("Error: Could not locate Table 1 or Table 2 in body!")
        return

    t1 = m1.group(1)
    t2 = m2.group(1)

    t1_clean = """// Table 1
#align(center)[
  #set text(size: 8pt)
  #table(
    columns: (1.3fr, 1.9fr, 1.9fr, 2.2fr),
    align: (left, left, left, left),
    stroke: 0.4pt + rgb("#cbd5e1"),
    fill: (col, row) => if row == 0 { rgb("#1a4f8a") } else if calc.odd(row) { rgb("#f8fafc") } else { white },
    inset: (x: 5pt, y: 4.5pt),
    table.header(
      text(fill: white, weight: "bold")[Methodological Dimension],
      text(fill: white, weight: "bold")[Del Matto (2018) (Q0a Baseline)],
      text(fill: white, weight: "bold")[Dougherty et al. (2022) Benchmark (Q0b)],
      text(fill: white, weight: "bold")[This Updated Synthesis (Q1 Publication)],
    ),
    [*Scope & Taxa*], [Fishes only (50 studies, 29 species, 183 effect sizes)], [All animals (92 studies, 67 species; 58 fish studies)], [Reconciled fishes master set + post-2020 literature update + non-fish extension],
    [*Study Overlap & Scope*], [Archived 50 fish studies (1995–2017)], [Shared 31 fish studies; 27 fish studies unique to broad search (19 fish studies unique to Del Matto)], [Full synthesis uniting both scopes (31 shared + 19 fish Del Matto + 27 fish Dougherty + post-2020)],
    [*Behavioral Allocation*], [Formal category ($k = 11, g = +2.732$; majors allocate more per spawn)], [Not evaluated (focused on standardized static ejaculate metrics across phyla)], [Core functional axis testing ejaculate economy during mating interactions],
    [*Testes & GSI Allometry*], [GSI only ($k = 31, g = -2.638$); 24 absolute mass rows excluded], [Focused on absolute testis mass to avoid ratio scaling artifacts], [Bivariate meta-regression modeling body mass & dimorphism as continuous allometric covariates],
    [*Sperm Competition Proxy*], [5-level categorical SCR (Stockley 1997); extreme ranks 1 & 5 confounded], [Sneaker frequency (linear test); evaluated cross-taxa gradient], [Continuous quadratic polynomial testing Parker's intermediate peak + continuous frequency],
    [*Phylogeny*], [Vector art tree without branch lengths; dropped from final models], [Open Tree of Life synthetic tree (`rotl`)], [Calibrated Ray-finned fish tree (Rabosky / `fishtree`) with Grafen branch lengths],
    [*Variance & Provenance*], [Single total $N$ per row; sampling variances not archived], [Re-extracted per-morph statistics for included subset], [Complete re-extraction with exact variances via `metafor::escalc`; fully open data],
    [*Overall Goal*], [Original MSc dissertation (unpublished)], [Landmark broad-taxa animal benchmark (*Biol Rev*)], [Definitive, reproducible publication resolving allometry & non-linear risk],
  )
]"""

    temp = body.replace(t1, '\n\n@@@TABLE_1@@@\n\n').replace(t2, '\n\n@@@TABLE_2@@@\n\n')
    chunks = re.split(r'\n{2,}', temp)

    out_chunks = []
    for chunk in chunks:
        c = chunk.strip()
        if not c:
            continue
        if '@@@TABLE_1@@@' in c:
            out_chunks.append(t1_clean)
            continue
        if '@@@TABLE_2@@@' in c:
            out_chunks.append(t2.strip())
            continue
        if c.startswith('='):
            out_chunks.append(c)
            continue
        if c.startswith('#line') or c.startswith('#v'):
            out_chunks.append(c)
            continue
        if c.startswith('#note['):
            inner = c[len('#note['):]
            if inner.endswith(']'):
                inner = inner[:-1].strip()
            inner_unwrapped = ' '.join(l.strip() for l in inner.splitlines() if l.strip())
            inner_clean = fix_mismatches_and_citations(inner_unwrapped)
            out_chunks.append(f'#note[\n  {inner_clean}\n]')
            continue

        # Check if list block
        lines = c.splitlines()
        is_list = any(re.match(r'^\s*([-*]|\d+\.)\s+', l) for l in lines)
        if is_list:
            items = []
            cur_pfx = ''
            cur_lines = []
            for l in lines:
                m = re.match(r'^(\s*[-*]|\s*\d+\.)\s+(.*)$', l)
                if m:
                    if cur_lines:
                        full = fix_mismatches_and_citations(' '.join(cur_lines))
                        items.append(f'{cur_pfx} {full}')
                    cur_pfx = m.group(1)
                    cur_content = m.group(2).strip()
                    cur_lines = [cur_content] if cur_content else []
                else:
                    cur_lines.append(l.strip())
            if cur_lines:
                full = fix_mismatches_and_citations(' '.join(cur_lines))
                items.append(f'{cur_pfx} {full}')
            out_chunks.append('\n'.join(items))
            continue

        # Regular paragraph: unwrap all lines into a single line
        p = ' '.join(l.strip() for l in lines if l.strip())
        p_clean = fix_mismatches_and_citations(p)
        out_chunks.append(p_clean)

    reformatted_body = '\n\n'.join(out_chunks)
    result = preamble + '\n\n' + reformatted_body + '\n\n' + references + '\n'

    with open('protocol/02_update_protocol.typ', 'w') as f:
        f.write(result)
    print("Reformatted protocol/02_update_protocol.typ successfully.")

if __name__ == "__main__":
    reformat()
