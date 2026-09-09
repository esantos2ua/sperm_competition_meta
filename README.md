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

## Key findings (baseline synthesis, 50 studies, 29 species, 183 effect sizes)

| Direction | Trait category | Hedges' $g$ (95% CI) | Interpretation |
|---|---|---|---|
| ↑ **Favours Majors** | **Allocation** | **+2.732 (+1.476 to +3.989)** | Majors allocate significantly more sperm per spawning act |
| ↓ **Favours Minors** | **Production / GSI** | **−2.638 (−3.105 to −2.177)** | Minors invest dramatically more in relative gonad size |
| ~ Indeterminate | Production / Quantity | −0.384 (−0.845 to +0.076) | Small non-significant trend towards minors (CI spans zero) |
| ~ Indeterminate | Quality | −0.251 (−0.699 to +0.197) | Small non-significant trend towards minors (CI spans zero) |
| ~ Indeterminate | Overall (Null Model) | −0.519 (−1.317 to +0.278) | Pooled mean overlaps zero ($I^2 = 83.21\%$) |

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
│   ├── build_results.py              # Compiles model stats & tables to build/results.json
│   ├── figures.py                    # Generates publication figures to figures/
│   └── generate_bib.py               # Generates references.bib from protocol table
├── protocol/
│   ├── 01_summary_DelMatto_2018.md   # Comprehensive summary of the 2018 dissertation baseline
│   └── 02_update_protocol.md         # Pre-registration protocol for the meta-analysis update
├── references/
│   ├── references.bib                # Primary BibTeX bibliography (74+ verified entries)
│   ├── sperm_competition_meta.bib    # Zotero / Better BibTeX synchronization target
│   ├── DelMatto_2018_dissertation.pdf# Archived original dissertation (USP, 2018)
│   ├── DelMatto2018_dissertation.md  # High-fidelity markdown extraction of dissertation
│   └── README_zotero.md              # Zotero setup instructions
├── data/
│   ├── input/                        # Raw / source datasets (read-only)
│   └── output/                       # Derived datasets and extracted effect sizes
└── analysis/                         # Extended R scripts and analytical notebooks
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
# Step 1: Compute statistics, format display strings, and write build/results.json
python3 scripts/build_results.py

# Step 2: Regenerate all publication figures (300 DPI)
python3 scripts/figures.py

# Step 3: Compile the Typst manuscript to PDF
typst compile manuscript.typ manuscript.pdf
```

---

## Note on data provenance & original dissertation

The original work is an unpublished MSc dissertation:
> Del Matto, L. A. (2018). *Sperm competition games between majors and minors: a meta-regression of fishes with alternative mating tactics.* Dissertação de Mestrado, Instituto de Biociências, Universidade de São Paulo. Supervisor: Eduardo S. A. Santos.

Key provenance details:
- **Supplementary Table 1 discrepancy resolved:** The original appendix records 207 rows. Excluding the 24 absolute gonad mass rows (dropped in the original Methods as non-independent of GSI) yields exactly the reported **183 effect sizes** (65 production = 31 GSI + 34 quantity; 107 quality; 11 allocation).
- **Variance reconstruction:** The original appendix archived no per-morph standard deviations or sample sizes. The update reconstructs sampling variances under stated assumptions for the reproduction, and re-extracts the 50 primary studies at the per-morph level for the updated synthesis.
- **Reporting checklist:** Reporting conforms to the PRISMA-EcoEvo guidelines detailed in [`PRISMA_EcoEvo_checklist.md`](PRISMA_EcoEvo_checklist.md).
