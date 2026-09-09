# PRISMA-EcoEvo Statement — Reporting Checklist

Reporting checklist for *"Sperm competition games between majors and minors: a phylogenetic meta-analysis of ejaculate expenditure in alternative mating tactics"*. Item numbers and guidance follow O'Dea et al. (2021), *Biological Reviews* 96:1695–1722, extending PRISMA 2020 (Page et al. 2021) for ecology and evolutionary biology. Section and paragraph references refer to `manuscript.typ`.

| Section / Topic | # | PRISMA-EcoEvo Item | Addressed in `manuscript.typ` |
|---|---|---|---|
| **TITLE** | 1 | Identify the report as a systematic review and meta-analysis | Title and Subtitle ("a phylogenetic meta-analysis of ejaculate expenditure") |
| **ABSTRACT** | 2 | Structured summary (Background, Methods, Results, Discussion) | Abstract (Structured sections with dynamic stats from `build/results.json`) |
| **INTRODUCTION** | | | |
| Rationale | 3 | Describe rationale for review in context of existing knowledge | §1 Introduction (Parker's sperm competition games, sneaks vs guards) |
| Objectives | 4 | Explicit statement of questions/hypotheses being addressed | §1 Introduction (Testing trade-offs: GSI vs sperm count vs quality vs allocation) |
| **METHODS** | | | |
| Eligibility criteria | 5 | Specify inclusion and exclusion criteria (PECOS framework) | §2.1 PECOS scope and eligibility criteria |
| Information sources | 6 | Describe all information sources (databases, registers, grey literature) | §2.2 Information sources and search strategy (WoS, Scopus, forward/backward citations) |
| Search strategy | 7 | Present full search strategies with limits and Boolean syntax | §2.2 Information sources and search strategy; protocol §3.4 |
| Selection process | 8 | State screening mechanisms (software, dual screening, deduplication) | §2.3 Study selection and screening (Figure 1: PRISMA flow diagram) |
| Data collection | 9 | Describe data extraction methods and variables obtained | §2.4 Data extraction and trait classification |
| Data items | 10 | List and define all outcomes, moderators, and covariates | §2.4 (Trait categories: Allocation, GSI, Quantity, Quality; SCR) |
| Risk of bias | 11 | Methods used to assess internal validity and risk of bias | §2.6 Quality assessment and publication bias diagnostics |
| Effect measures | 12 | Specify effect-size metric and rationale (e.g. Hedges' g) | §2.5 Effect-size calculation and variance formulation (Hedges' g) |
| Synthesis methods | 13a | Criteria for determining eligibility for quantitative synthesis | §2.5 Synthesis criteria |
| Synthesis methods | 13b | Data handling (approximations, unit conversions, missing data) | §2.5 Handling missing variances and extreme effect sizes |
| Synthesis methods | 13c | Description of meta-analytic models and software (`metafor::rma.mv`) | §2.5 Multilevel phylogenetic meta-analytic models |
| Synthesis methods | 13d | Methods for exploring heterogeneity (I², orchard plots, moderators) | §2.5 Heterogeneity decomposition and multilevel I²; Table 2 |
| Synthesis methods | 13e | Sensitivity analyses (leave-one-out, outlier removal, provenance) | §2.5 Sensitivity analyses and influence diagnostics |
| Synthesis methods | 13f | Publication and dissemination bias assessment | §2.6 Publication bias (Egger regressions, funnel plots, precision) |
| **RESULTS** | | | |
| Study selection | 16a | Flow of studies through the review (PRISMA flow diagram) | §3.1 Study selection and dataset composition; Figure 1 |
| Study characteristics | 17 | Characteristics of included studies, species, and traits | §3.1; Table 1; summary stats (#S.n_studies, #S.n_species, #S.n_effects) |
| Risk of bias | 18 | Results of quality assessments and outlier audits | §3.1 Audit of extreme effect sizes (|g| > 8) |
| Individual results | 19 | Forest and orchard plots of individual and pooled effect sizes | §3.2 Pooled estimates by trait category; Figure 2 |
| Synthesis results | 20a | Overall meta-analytic pooled estimate and precision | §3.2 Baseline null model and category meta-regressions |
| Synthesis results | 20b | Heterogeneity decomposition across random effects | §3.3 Variance decomposition (Study, Species, Phylogeny); Table 2; Figure 3 |
| Subgroups & moderators | 20c | Results of moderator analyses (trait type, sperm competition rank) | §3.2 Trait categories; §3.4 Sperm competition rank (SCR) |
| Sensitivity analyses | 20d | Robustness checks and sensitivity model refits | §3.5 Robustness and sensitivity analyses |
| Reporting biases | 21 | Evidence of publication and reporting biases | §3.6 Small-study effects and publication bias; Figure 4 |
| **DISCUSSION** | | | |
| Interpretation | 23 | Interpretation of results in context of theory and evidence | §4.1 Principal findings; §4.2 The GSI vs sperm number paradox |
| Limitations | 24 | Discussion of limitations of the evidence base and review methods | §4.4 Strengths and limitations |
| Implications | 25 | Implications for theory, empirical design, and future research | §4.5 Theoretical and empirical implications |
| **OTHER INFORMATION** | | | |
| Registration | 26 | Registration information and protocol availability | Declarations; Protocol in `protocol/` |
| Support & funding | 27 | Sources of financial or in-kind support | Declarations (No external funding received) |
| Conflicts of interest | 28 | Conflict of interest disclosures | Declarations (The authors declare no competing interests) |
| Data & code | 29 | Data and code availability statements | Declarations (All code in `scripts/`, data in `data/`, open repository) |

**Reproducibility note.** Every numerical result, model estimate, confidence interval, table cell, and figure annotation in the manuscript is generated programmatically from the source data via `scripts/build_results.py` and `scripts/figures.py` into `build/results.json` and read at compile time by `manuscript.typ`. No numerical value is entered by hand.
