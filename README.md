# Sperm Competition Games Between Majors and Minors: A Phylogenetic Meta-Analysis

**Sperm competition games between majors and minors: a phylogenetic meta-analysis of ejaculate expenditure in alternative mating tactics**

Working repository for the update and peer-reviewed publication of the meta-analysis presented by Del Matto (2018), *Sperm competition games between majors and minors: a meta-regression of fishes with alternative mating tactics* (MSc dissertation, Universidade de São Paulo; supervised by Eduardo S. A. Santos), prepared with Lygia Aguiar Del Matto as co-author.

---

## Overview

This repository contains the data, analytical pipeline, figures, and manuscript source testing Parker's (1990) game-theoretic predictions of sperm competition in species where males express alternative reproductive tactics (ARTs).

In sneak–guard systems, non-territorial sneakers or satellites (**"minors"**) face a high probability of sperm competition on virtually every spawning, whereas territorial, guarding males (**"majors"**) face competition only when cuckolded. Parker's models predict:
1. **Asymmetric investment:** Minors should invest disproportionately in sperm production (higher gonadosomatic index, GSI, and greater sperm counts) relative to majors.
2. **Intermediate risk peak:** The divergence in expenditure between morphs should be greatest in species with intermediate background sperm competition risk (approximated by Sperm Competition Rank, SCR).

Following **PRISMA-EcoEvo** reporting standards, this project synthesizes evidence across four distinct functional axes:
- **Production / GSI:** Relative gonad mass (body-mass, soma-mass, or energy-corrected).
- **Production / Quantity:** Absolute sperm numbers, sperm concentration, spermatocrit, stripped milt volume, and absolute testis mass.
- **Quality:** Sperm velocity (VCL, VSL, VAP), motility duration, sperm morphology, and bioenergetics (ATP/enzymes).
- **Allocation:** Facultative, per-spawning behavioral expenditure (sperm released per mating event and ejaculation frequency).

Every number in the manuscript—every table cell, model estimate, confidence interval, and in-text figure—is compiled programmatically from open scripts into `build/results.json` and injected into the Typst source at compile time. Nothing is typed by hand.

---

## Key findings (baseline synthesis, 48 studies, 29 species, 183 effect sizes)

| Direction | Trait category | Hedges' $g$ (95% CI) | Interpretation |
|---|---|---|---|
| ↑ **Favours Majors** | **Allocation** | **+2.733 (+1.476 to +3.990)** | Majors allocate significantly more sperm per spawning act |
| ↓ **Favours Minors** | **Production / GSI** | **−2.638 (−3.105 to −2.172)** | Minors invest dramatically more in relative gonad size |
| ~ Indeterminate | Production / Quantity | −0.385 (−0.845 to +0.076) | Small non-significant trend towards minors (CI spans zero) |
| ~ Indeterminate | Quality | −0.251 (−0.699 to +0.197) | Small non-significant trend towards minors (CI spans zero) |
| ~ Indeterminate | Overall (Null Model) | −0.522 (−1.325 to +0.280) | Pooled mean overlaps zero ($I^2 = 93.39\%$) |

Estimates are refitted by `analysis/01_baseline_models.R` from the exact effect sizes and sampling variances in the original 2018 extraction spreadsheet. Multilevel Egger regressions show significant small-study effects in all models, so pooled means should be read with caution.

*Sign convention:* Positive Hedges' $g$ denotes larger values in **majors**; negative $g$ denotes larger values in **minors**.

---

## Repository structure

```
sperm_competition_meta/
├── README.md                          # Repository documentation and reproduction guide
├── manuscript.typ                     # Typst manuscript source (main paper)
├── manuscript.pdf                     # Compiled manuscript (12 pages, PDF)
├── PRISMA_EcoEvo_checklist.md         # PRISMA-EcoEvo reporting checklist
├── requirements.txt                   # Python dependencies for pipeline
├── build/
│   └── results.json                  # Single source of truth: all numbers read by Typst
├── figures/
│   ├── fig1_prisma_flow.png          # Figure 1: PRISMA 2020 literature flow diagram
│   ├── fig2_orchard_categories.png   # Figure 2: Orchard / forest plot of trait categories
│   ├── fig3_heterogeneity.png        # Figure 3: Multilevel I^2 variance partitioning
│   └── fig4_funnel_plot.png          # Figure 4: Funnel plot and small-study diagnostics
├── scripts/
│   ├── reconcile_dissertation_data.py# Exact 183-vs-207 effect size reconciliation script
│   ├── fetch_openalex.py             # OpenAlex API search & forward citation snowballing
│   ├── build_results.py              # Compiles model stats & tables to build/results.json
│   ├── figures.py                    # Generates publication figures to figures/
│   └── generate_bib.py               # Generates references.bib from protocol table
├── protocol/
│   ├── 01_summary_DelMatto_2018.md   # Comprehensive summary of the 2018 dissertation baseline
│   └── 02_update_protocol.md         # Pre-registration protocol for update & reconciliation
├── references/
│   ├── references.bib                # Primary BibTeX bibliography (76+ verified entries)
│   ├── sperm_competition_meta.bib    # Zotero / Better BibTeX synchronization target
│   ├── DelMatto_2018_dissertation.pdf# Archived original dissertation (USP, 2018)
│   ├── DelMatto2018_dissertation.md  # High-fidelity markdown extraction of dissertation
│   └── README_zotero.md              # Zotero setup instructions
├── data/
│   ├── input/
│   │   ├── delmatto2018_supp_table1.csv # Raw 207 rows extracted from dissertation PDF
│   │   ├── delmatto2018_original/       # Original 2018 extraction sheet (exact g, v) and fish trees
│   │   └── dougherty2022_all_data.xlsx  # Archived Figshare dataset from Dougherty et al. (2022)
│   └── output/
│       ├── delmatto2018_reconciled.csv  # Reconciled 183-effect baseline dataset
│       └── openalex_update_candidates.csv # 468 candidate records (2017–2026) for screening
└── analysis/
    ├── 01_baseline_models.R          # Refits the 2018 baseline models → build/model_results.json
    └── original_2018/                # Archived 2018 R Markdown analysis (Del Matto & Santos)
```

---

## Reproducing the analysis

### 1. Environment setup

```bash
# Python environment for results building and figure generation
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

R requirements (for underlying multilevel modeling): `metafor`, `orchaRd`, `ape`, `rotl`, `fishtree`, `jsonlite`.

### 2. Execution pipeline

Run the end-to-end pipeline in order:

```bash
# Step 1: Reconcile original dissertation data (verifies 183/207 effect sizes)
python3 scripts/reconcile_dissertation_data.py

# Step 2: (Optional) Harvest latest literature via OpenAlex REST API
python3 scripts/fetch_openalex.py

# Step 3: Refit the baseline models in R (writes build/model_results.json, build/effect_sizes.csv)
Rscript analysis/01_baseline_models.R

# Step 4: Format display strings and write build/results.json
python3 scripts/build_results.py

# Step 5: Regenerate all publication figures (300 DPI)
python3 scripts/figures.py

# Step 6: Compile the Typst manuscript to PDF
typst compile manuscript.typ manuscript.pdf
```

---

## Note on data provenance & cross-synthesis reconciliation

The original work is an unpublished MSc dissertation:
> Del Matto, L. A. (2018). *Sperm competition games between majors and minors: a meta-regression of fishes with alternative mating tactics.* Dissertação de Mestrado, Instituto de Biociências, Universidade de São Paulo. Supervisor: Eduardo S. A. Santos.

Key provenance and reconciliation details:
- **Original analysis files recovered:** The 2018 analysis repository (`meta-analysis-Lygia`) is archived in `data/input/delmatto2018_original/` and `analysis/original_2018/`. Its extraction spreadsheet matches Supplementary Table 1 row for row and adds exact sampling variances, study IDs, trait sub-categories, study design and setting, and morph body sizes. Two corrections to the original script are applied: inverse-variance weights in the typical sampling variance for $I^2$, and a multilevel Egger test on the slope.
- **Supplementary Table 1 discrepancy resolved:** The original appendix records 207 rows. Programmatically excluding the 24 absolute gonad mass rows (dropped in the original Methods as non-independent of GSI) yields exactly the reported **183 effect sizes** (65 production = 31 GSI + 34 quantity; 107 quality; 11 allocation). Fully verified in `scripts/reconcile_dissertation_data.py`.
- **Three-way cross-synthesis reconciliation:** Directly compares Del Matto (2018) with the broad-taxa meta-analysis by Dougherty et al. (2022, *Biological Reviews*; 92 animal studies, 58 fishes). Identifies 31 shared teleost studies, audits 19 teleost studies in Del Matto missed by Dougherty (including key behavioral allocation papers), and integrates 27 teleost studies unique to Dougherty.
- **Resolving the GSI allometry controversy:** Dougherty et al. argued that higher minor testes mass is a GSI ratio artifact, but dropped GSI entirely. Our update fits continuous bivariate allometric meta-regressions with body mass and dimorphism, testing whether disproportionate gonadal investment survives proper scaling.
- **Restoring behavioral sperm allocation:** Restores per-spawn sperm allocation ($g = +2.732$ in Del Matto), which was omitted in Dougherty et al. (2022).
- **Testing Parker's non-linear risk predictions:** Implements quadratic polynomial meta-regressions ($SCR + SCR^2$) to test whether divergence peaks at intermediate sperm competition risk, rather than assuming monotonic linearity.
- **Reporting checklist:** Reporting conforms to the PRISMA-EcoEvo guidelines detailed in [`PRISMA_EcoEvo_checklist.md`](PRISMA_EcoEvo_checklist.md).
