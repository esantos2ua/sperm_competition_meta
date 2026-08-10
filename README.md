# Sperm competition between majors and minors meta-analysis — update

Working repository for an **update of the meta-analysis** presented by Del Matto (2018),
*Sperm competition games between majors and minors: a meta-regression of fishes with alternative mating
tactics* (MSc dissertation, Instituto de Biociências, Universidade de São Paulo; supervisor Eduardo S. A.
Santos). The dissertation is **unpublished**, so this update is also the route by which the synthesis will be
brought to publication, with Lygia Aguiar Del Matto as a co-author.

## Folder structure

| Folder            | Contents                                                                 |
|-------------------|--------------------------------------------------------------------------|
| `protocol/`       | Review/meta-analysis protocol and the summary of the original study.     |
| `references/`     | Bibliography (`sperm_competition_meta.bib`, Zotero/Better BibTeX), the source PDF and its markdown conversion, `pdf_to_markdown.py`, and `README_zotero.md`. |
| `data/input/`     | Raw / source datasets (treated as read-only).                            |
| `data/output/`    | Processed datasets, effect-size tables, derived results.                 |
| `analysis/`       | Analysis scripts (R), notebooks, and code.                              |
| `manuscript/`     | Manuscript drafts, figures, tables, supplementary materials.            |

## Status

- [x] Repository and folder structure created; version control initialized.
- [x] Source dissertation archived in [`references/`](references/) as
      [`DelMatto_2018_dissertation.pdf`](references/DelMatto_2018_dissertation.pdf) plus a high-fidelity
      markdown conversion (see *Note on the source conversion*).
- [x] Summary of the original 2018 meta-analysis drafted — see
      [`protocol/01_summary_DelMatto_2018.md`](protocol/01_summary_DelMatto_2018.md).
- [x] Update protocol drafted (v0.1) — see
      [`protocol/02_update_protocol.md`](protocol/02_update_protocol.md). Contains `[TBD]` placeholders
      (co-authors beyond ESAS and LADM, ORCID for LADM, author order, funding, pilot search results,
      decision trees, registration DOI) to resolve before pre-registration.
- [x] Effect-size count difference in the original appendix identified **and resolved**
      (**183 effect sizes reported vs. 207 rows in Supplementary Table 1**: the appendix is the full
      extraction sheet, and excluding the 24 rows recording an absolute gonad/testis mass — the class the
      Methods say was dropped as non-independent of GSI, while retaining body-mass-corrected indices —
      recovers the reported counts exactly, 183 total = 65 production (31 GSI + 34 quantity) + 107 quality
      + 11 allocation; see
      [`protocol/01_summary_DelMatto_2018.md`](protocol/01_summary_DelMatto_2018.md) §7 and protocol §3.1,
      step 2). The remaining, independent gap is that no per-morph means, SDs or *N*s were archived, so
      sampling variances cannot be recomputed exactly.
- [ ] Create the Zotero collection and `references/sperm_competition_meta.bib` from the citation-key
      appendix at the end of the update protocol (**the `.bib` does not exist yet** — see *References*).
- [ ] Transcribe Supplementary Table 1 into `data/input/` and reproduce the published estimates
      (see protocol §3.1).
- [ ] Re-extract per-morph means, SDs and sample sizes from the 50 original studies (the appendix archives
      none of these).
- [ ] Audit the eight archived effect sizes with |*g*| > 8 against their source articles.
- [ ] Build benchmark set and run/report pilot searches; develop screening decision trees.

## Note on the source conversion

[`references/DelMatto2018_dissertation.md`](references/DelMatto2018_dissertation.md) is a **high-fidelity
markdown conversion** of the source PDF, produced by
[`references/pdf_to_markdown.py`](references/pdf_to_markdown.py) (a custom PyMuPDF + pdfplumber pipeline).
Headings are real `#`/`##`, italics are preserved, and every table block is valid markdown. The four
dissertation tables come out as **18 table blocks**, each individually valid: Table 1 is split across two
blocks (physical pp. 19–20, the second block's first data row opening with an empty *Category* cell), Tables 2
and 3 are one block
each, and Supplementary Table 1 is 14 blocks with a repeating header (one per printed appendix page). Raster
figures are extracted to `references/figures/` and linked; the two vector forest plots (Figs 2 and 3) could not
be extracted as text and are represented by descriptive placeholders.

- Page provenance is recorded with `<!-- physical page N (printed M) -->` comments. **The printed folios run
  two behind the physical page indices** (physical page 13 = printed page 11), because the PDF carries two
  unnumbered cover pages.
- Known conversion artefacts to be aware of when working with the appendix: Supplementary Table 1 spans 14
  printed pages, so its header row repeats; three rows are line-wrap fragments of a split *Source* cell
  (Leach & Montgomerie 2000, Koseki & Maekawa 2002, Hurtado-Gonzales & Uy 2009) and must be merged before
  counting — merging those three, and nothing else, takes the 53 raw *Source* strings to the reported 50
  studies; one source is additionally printed parenthetically ("(Serrano et al., 2006)"), but that is purely
  cosmetic and does not affect any count. Figures 1–3 and Supplementary Figure 1 are images or vector plots —
  the numbers quoted in `protocol/01_summary_DelMatto_2018.md` come from the prose and tables, never from the
  figures.
- Always verify any row-level value against the PDF before entering it into `data/input/`.

## Note on data availability

The original is an **unpublished MSc dissertation with no data availability statement, no analysis code, and
no reference to any repository** (no OSF, Dryad, Zenodo, figshare or GitHub). The only recoverable primary
artefacts are in its *Supplementary Material*:

- **Supplementary Table 1** — one row per effect size with seven columns: species, Hedges' *g*, a single
  sample size *N* ("number of males investigated"), sperm competition rank, the original response-variable
  name, the variable type (production / quality / allocation), and the source study. It contains **no
  per-morph means, no standard deviations or standard errors, and no per-morph sample sizes**, hence **no
  recoverable sampling variances**; it also omits the Production/Quantity-vs-GSI sub-category and the
  observational-vs-experimental flag that the original's models needed.
- **Supplementary Figure 1** — a 29-tip species phylogeny whose **branches are vector art**, so the topology
  itself is not machine-readable; the **tip labels do extract as text**, and a raster of the page is available
  at [`references/figures/p38_img0.png`](references/figures/p38_img0.png). There is no tree file, no branch
  lengths, and no stated source topology.

The reproduction step therefore **reconstructs** the analysis dataset from Supplementary Table 1,
**approximates** the sampling variances under a stated assumption about morph sample sizes, **rebuilds** the
derived fields and the phylogeny, and **re-implements** the three `metafor::rma.mv` models in R before
updating — rather than re-executing archived data and code, which do not exist. The update then **re-extracts
all 50 original studies at the per-morph level**, so that the published version rests on computed rather than
approximated variances. Publishing open data and code is an explicit deliverable of this project.

## References

Citations are managed in **Zotero** with the **Better BibTeX** extension, auto-exported to
`references/sperm_competition_meta.bib`. **That file does not exist yet.** Every citation key used in the
protocol is listed with its full reference in the appendix at the end of
[`protocol/02_update_protocol.md`](protocol/02_update_protocol.md) (*Appendix: citation keys used (to be
entered in Zotero)*), so the collection can be created and the keys pinned to those exact strings; until then
the protocol will render `[@key]` markers unresolved. The protocol cites with Pandoc `[@key]` syntax and
generates its reference list on render — do not edit the `.bib` or the list by hand. Setup and rendering
instructions are in [`references/README_zotero.md`](references/README_zotero.md).

## Conventions

- Treat `data/input/` as immutable; all transformations write to `data/output/`.
- **Sign convention (retained from the original):** positive Hedges' *g* = larger value in **majors**;
  negative *g* = larger value in **minors**. This is the reverse of the intuitive "more expenditure"
  direction, so it is stated in every figure caption.
- Analyses are scripted in R. The original used **`metafor::rma.mv`** under **R 3.4.0**, with figure
  digitising in **GraphClick v. 3.0.3** or **metaDigitise**, and effect sizes from inferential statistics via
  the **Practical Meta-Analysis Effect Size Calculator** (Wilson 2018); the update re-implements and extends
  these in R (`metafor`, `orchaRd`, `rotl`, `fishtree`, `ape`), following the lab's `ecoevo-meta-pipeline`
  config-driven workflow.
- Numbers quoted from the dissertation cite the **physical page index** of
  `references/DelMatto2018_dissertation.md`, not the printed folio; remember the two-page offset.
