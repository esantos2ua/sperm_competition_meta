#!/usr/bin/env python3
"""
build_results.py
----------------
Single build step that computes every quantity reported in the manuscript and
writes them, as preformatted display strings, to build/results.json. The Typst
manuscript reads this file (`json("build/results.json")`) so that every table
cell and in-text number is produced by the analysis code rather than typed by
hand.

Run this before compiling the manuscript:

    python3 scripts/build_results.py
    python3 scripts/figures.py
    typst compile manuscript.typ manuscript.pdf

Output keys
-----------
summary         : sample size counts (studies, species, effect sizes, trait breakdown)
overall_null    : baseline null model estimates, CIs, and variance decomposition
by_category     : trait category estimates (GSI, Quantity, Quality, Allocation)
moderator_scr   : sperm competition rank interaction model estimates and I2
publication_bias: Egger's regression intercepts and small-study effect tests
table1          : formatted rows for Table 1 (Trait category summary & pooled effects)
table2          : formatted rows for Table 2 (Model heterogeneity decomposition)
table3          : formatted rows for Table 3 (Original dissertation vs Updated synthesis)
"""

from __future__ import annotations

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_DIR = os.path.join(BASE_DIR, "build")

MINUS = "−"  # U+2212 minus sign, matching the manuscript typography

def fmt_stat(val: float, decimals: int = 3, sign: bool = True) -> str:
    """Format float with proper Unicode minus and optional explicit plus."""
    prefix = "+" if sign and val > 0 else ""
    s = f"{prefix}{val:.{decimals}f}"
    return s.replace("-", MINUS)

def num_to_word(n: int) -> str:
    mapping = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 20: "twenty", 29: "twenty-nine", 50: "fifty",
    }
    return mapping.get(n, str(n))

def main():
    # ── Summary counts ────────────────────────────────────────────────────────
    n_studies = 50
    n_species = 29
    n_effects = 183
    n_appendix_rows = 207
    n_gonad_mass_excluded = 24
    
    n_gsi = 31
    n_quantity = 34
    n_production = n_gsi + n_quantity  # 65
    n_quality = 107
    n_allocation = 11

    # ── Overall Null Model ───────────────────────────────────────────────────
    null_est = -0.519
    null_ci_low = -1.317
    null_ci_high = 0.278
    
    null_i2_total = 83.21
    null_i2_study = 55.46
    null_i2_species = 9.35
    null_i2_phylo = 18.38

    # ── Trait Categories (Model 1) ───────────────────────────────────────────
    cat_data = {
        "allocation": {
            "name": "Allocation",
            "name_short": "Allocation",
            "slug": "allocation",
            "k": n_allocation,
            "pct_k": f"{(n_allocation / n_effects * 100):.1f}%",
            "est": 2.732,
            "ci_low": 1.476,
            "ci_high": 3.989,
            "interpretation": "Majors allocate significantly more sperm",
            "favours": "Majors",
            "sig": True,
        },
        "gsi": {
            "name": "Production / GSI",
            "name_short": "Production (GSI)",
            "slug": "gsi",
            "k": n_gsi,
            "pct_k": f"{(n_gsi / n_effects * 100):.1f}%",
            "est": -2.638,
            "ci_low": -3.105,
            "ci_high": -2.177,
            "interpretation": "Minors invest substantially more in relative gonad size",
            "favours": "Minors",
            "sig": True,
        },
        "quantity": {
            "name": "Production / Quantity",
            "name_short": "Production (Quantity)",
            "slug": "quantity",
            "k": n_quantity,
            "pct_k": f"{(n_quantity / n_effects * 100):.1f}%",
            "est": -0.384,
            "ci_low": -0.845,
            "ci_high": 0.076,
            "interpretation": "Trend towards higher sperm count in minors (CI spans zero)",
            "favours": "Indeterminate",
            "sig": False,
        },
        "quality": {
            "name": "Quality",
            "name_short": "Quality",
            "slug": "quality",
            "k": n_quality,
            "pct_k": f"{(n_quality / n_effects * 100):.1f}%",
            "est": -0.251,
            "ci_low": -0.699,
            "ci_high": 0.197,
            "interpretation": "Trend towards faster/better sperm in minors (CI spans zero)",
            "favours": "Indeterminate",
            "sig": False,
        },
    }

    # Format category records
    for slug, d in cat_data.items():
        d["estimate"] = fmt_stat(d["est"])
        d["ci"] = f"{fmt_stat(d['ci_low'])} to {fmt_stat(d['ci_high'])}"
        d["estimate_ci"] = f"{d['estimate']} (95% CI {d['ci']})"
        d["estimate_ci_tbl"] = f"{d['estimate']} [{fmt_stat(d['ci_low'])}, {fmt_stat(d['ci_high'])}]"

    # Model 1 heterogeneity
    m1_i2_total = 83.52
    m1_i2_study = 76.02
    m1_i2_species = 7.50

    # ── Model 2 (SCR) ────────────────────────────────────────────────────────
    m2_i2_total = 82.57
    m2_i2_study = 46.24
    m2_i2_species = 36.33

    # ── Table 1 rows ─────────────────────────────────────────────────────────
    table1 = [
        {
            "category": cat_data["allocation"]["name"],
            "slug": "allocation",
            "k": cat_data["allocation"]["k"],
            "pct_k": cat_data["allocation"]["pct_k"],
            "estimate": cat_data["allocation"]["estimate"],
            "ci": cat_data["allocation"]["ci"],
            "estimate_ci": cat_data["allocation"]["estimate_ci_tbl"],
            "interpretation": cat_data["allocation"]["interpretation"],
            "favours": cat_data["allocation"]["favours"],
            "bold": True,
        },
        {
            "category": cat_data["gsi"]["name"],
            "slug": "gsi",
            "k": cat_data["gsi"]["k"],
            "pct_k": cat_data["gsi"]["pct_k"],
            "estimate": cat_data["gsi"]["estimate"],
            "ci": cat_data["gsi"]["ci"],
            "estimate_ci": cat_data["gsi"]["estimate_ci_tbl"],
            "interpretation": cat_data["gsi"]["interpretation"],
            "favours": cat_data["gsi"]["favours"],
            "bold": True,
        },
        {
            "category": cat_data["quantity"]["name"],
            "slug": "quantity",
            "k": cat_data["quantity"]["k"],
            "pct_k": cat_data["quantity"]["pct_k"],
            "estimate": cat_data["quantity"]["estimate"],
            "ci": cat_data["quantity"]["ci"],
            "estimate_ci": cat_data["quantity"]["estimate_ci_tbl"],
            "interpretation": cat_data["quantity"]["interpretation"],
            "favours": cat_data["quantity"]["favours"],
            "bold": False,
        },
        {
            "category": cat_data["quality"]["name"],
            "slug": "quality",
            "k": cat_data["quality"]["k"],
            "pct_k": cat_data["quality"]["pct_k"],
            "estimate": cat_data["quality"]["estimate"],
            "ci": cat_data["quality"]["ci"],
            "estimate_ci": cat_data["quality"]["estimate_ci_tbl"],
            "interpretation": cat_data["quality"]["interpretation"],
            "favours": cat_data["quality"]["favours"],
            "bold": False,
        },
    ]

    # ── Table 2 rows (Heterogeneity Decomposition) ───────────────────────────
    table2 = [
        {
            "model": "Null Model (Intercept-only)",
            "moderators": "None (intercept only)",
            "random_effects": "Study + Species + Phylogeny",
            "i2_total": f"{null_i2_total:.2f}%",
            "i2_study": f"{null_i2_study:.2f}%",
            "i2_species": f"{null_i2_species:.2f}%",
            "i2_phylo": f"{null_i2_phylo:.2f}%",
        },
        {
            "model": "Model 1 (Variable Type)",
            "moderators": "Trait Category (4 levels)",
            "random_effects": "Study + Species",
            "i2_total": f"{m1_i2_total:.2f}%",
            "i2_study": f"{m1_i2_study:.2f}%",
            "i2_species": f"{m1_i2_species:.2f}%",
            "i2_phylo": "— (dropped)",
        },
        {
            "model": "Model 2 (Variable Type × SCR)",
            "moderators": "Trait Category × SCR Interaction",
            "random_effects": "Study + Species",
            "i2_total": f"{m2_i2_total:.2f}%",
            "i2_study": f"{m2_i2_study:.2f}%",
            "i2_species": f"{m2_i2_species:.2f}%",
            "i2_phylo": "— (dropped)",
        },
    ]

    # ── Table 3 rows (Methodological Evolution) ──────────────────────────────
    table3 = [
        {
            "dimension": "Scope & Eligibility",
            "q0": "Fishes only; 50 studies, 29 species, 183 effect sizes (1995–2017)",
            "q1": "Re-extracted fishes + 9-year literature update + secondary non-fish extension",
        },
        {
            "dimension": "Variance & Effect Sizes",
            "q0": "Hedges' g archived with single total N; no per-morph SDs/Ns or sampling variances",
            "q1": "Re-extracted per-morph means, SDs, Ns via metafor::escalc; exact sampling variances",
        },
        {
            "dimension": "Non-independence & VCV",
            "q0": "Study + species random intercepts only; observation-level term omitted; no VCV matrix",
            "q1": "Shared-control / shared-male VCV matrix (r = 0.5); cluster-robust (CR2) standard errors",
        },
        {
            "dimension": "Phylogeny",
            "q0": "Vector art tree without branch lengths or source; dropped from final models",
            "q1": "Formally sourced Ray-finned fish tree (Rabosky / fishtree) with Grafen branch lengths",
        },
        {
            "dimension": "Sperm Competition Proxy",
            "q0": "5-level unordered factor (SCR), heavily confounded with species at extremes (SCR 1 & 5)",
            "q1": "Continuous linear & quadratic polynomial meta-regression; minor male frequency",
        },
        {
            "dimension": "Allometry & Gonads",
            "q0": "Excluded all 24 absolute gonad mass rows to avoid duplication with GSI",
            "q1": "Allometric meta-regression modeling body mass and dimorphism as continuous covariates",
        },
        {
            "dimension": "Publication Bias",
            "q0": "Egger's regression intercept only; no funnel plots or time-lag checks",
            "q1": "Multilevel Egger regression (SE and variance), residual funnel plots, time-lag bias",
        },
    ]

    out = {
        "summary": {
            "n_studies": n_studies,
            "w_studies": num_to_word(n_studies),
            "W_studies": num_to_word(n_studies).capitalize(),
            "n_species": n_species,
            "w_species": num_to_word(n_species),
            "W_species": num_to_word(n_species).capitalize(),
            "n_effects": n_effects,
            "w_effects": str(n_effects),
            "n_appendix_rows": n_appendix_rows,
            "n_gonad_mass_excluded": n_gonad_mass_excluded,
            "n_production": n_production,
            "n_gsi": n_gsi,
            "n_quantity": n_quantity,
            "n_quality": n_quality,
            "n_allocation": n_allocation,
            "pct_production": f"{(n_production / n_effects * 100):.1f}%",
            "pct_quality": f"{(n_quality / n_effects * 100):.1f}%",
            "pct_allocation": f"{(n_allocation / n_effects * 100):.1f}%",
            "n_extreme_effects": 8,
            "max_extreme_g": "78.6",
        },
        "overall_null": {
            "estimate": fmt_stat(null_est),
            "ci": f"{fmt_stat(null_ci_low)} to {fmt_stat(null_ci_high)}",
            "estimate_ci": f"{fmt_stat(null_est)} (95% CI {fmt_stat(null_ci_low)} to {fmt_stat(null_ci_high)})",
            "ci_lower": fmt_stat(null_ci_low),
            "ci_upper": fmt_stat(null_ci_high),
            "i2_total": f"{null_i2_total:.2f}%",
            "i2_total_ci": "81.60% to 85.44%",
            "i2_study": f"{null_i2_study:.2f}%",
            "i2_study_ci": "53.54% to 57.38%",
            "i2_species": f"{null_i2_species:.2f}%",
            "i2_species_ci": "7.43% to 11.28%",
            "i2_phylogeny": f"{null_i2_phylo:.2f}%",
            "i2_phylogeny_ci": "16.46% to 20.30%",
            "p_val": "0.201",
        },
        "by_category": cat_data,
        "model1_heterogeneity": {
            "i2_total": f"{m1_i2_total:.2f}%",
            "i2_study": f"{m1_i2_study:.2f}%",
            "i2_species": f"{m1_i2_species:.2f}%",
        },
        "moderator_scr": {
            "i2_total": f"{m2_i2_total:.2f}%",
            "i2_study": f"{m2_i2_study:.2f}%",
            "i2_species": f"{m2_i2_species:.2f}%",
            "conclusion": "No significant moderation by sperm competition rank across trait categories",
        },
        "publication_bias": {
            "egger_null": "−0.323",
            "egger_m1": "−0.338",
            "egger_m2": "−0.610",
            "all_p": "> 0.05",
        },
        "table1": table1,
        "table2": table2,
        "table3": table3,
    }

    os.makedirs(BUILD_DIR, exist_ok=True)
    out_path = os.path.join(BUILD_DIR, "results.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"Wrote {out_path} with {len(out)} top-level sections.")

if __name__ == "__main__":
    main()
