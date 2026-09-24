#!/usr/bin/env python3
"""
build_results.py
----------------
Single build step that computes every quantity reported in the manuscript and
writes them, as preformatted display strings, to build/results.json. The Typst
manuscript reads this file (`json("build/results.json")`) so that every table
cell and in-text number is produced by the analysis code rather than typed by
hand.

Model quantities come from build/model_results.json, written by
analysis/01_baseline_models.R from the original 2018 extraction spreadsheet.
Run this before compiling the manuscript:

    Rscript analysis/01_baseline_models.R
    python3 scripts/build_results.py
    python3 scripts/figures.py
    typst compile manuscript.typ manuscript.pdf

Output keys
-----------
summary         : sample size counts (studies, species, effect sizes, trait breakdown)
overall_null    : baseline null model estimates, CIs, and variance decomposition
by_category     : trait category estimates (GSI, Quantity, Quality, Allocation)
moderator_scr   : sperm competition rank interaction model estimates and I2
publication_bias: multilevel Egger regression slopes (small-study effects)
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
        15: "fifteen", 20: "twenty", 28: "twenty-eight", 29: "twenty-nine",
        48: "forty-eight", 50: "fifty",
    }
    return mapping.get(n, str(n))

def fmt_p(p: float) -> str:
    """Format a P value for display ("= 0.202", "< 0.001")."""
    return "< 0.001" if p < 0.001 else f"= {p:.3f}"

def load_models() -> dict:
    path = os.path.join(BUILD_DIR, "model_results.json")
    if not os.path.exists(path):
        raise SystemExit(f"{path} not found; run `Rscript analysis/01_baseline_models.R` first.")
    with open(path, encoding="utf-8") as f:
        return json.load(f)

CATEGORY_META = {
    "allocation": ("Allocation", "Allocation"),
    "gsi": ("Production / GSI", "Production (GSI)"),
    "quantity": ("Production / Quantity", "Production (Quantity)"),
    "quality": ("Quality", "Quality"),
}

def interpret(slug: str, lo: float, hi: float) -> tuple[str, str, bool]:
    if lo > 0:
        return {"allocation": "Majors allocate significantly more sperm"}.get(
            slug, "Majors invest significantly more"), "Majors", True
    if hi < 0:
        return {"gsi": "Minors invest substantially more in relative gonad size"}.get(
            slug, "Minors invest significantly more"), "Minors", True
    trend = "minors" if lo + hi < 0 else "majors"
    return f"Trend towards {trend} (CI spans zero)", "Indeterminate", False

def main():
    M = load_models()
    SM = M["summary"]

    # ── Summary counts ────────────────────────────────────────────────────────
    n_studies = SM["n_studies"]
    n_species = SM["n_species"]
    n_effects = SM["n_effects"]
    n_appendix_rows = SM["n_rows_all"]
    n_gonad_mass_excluded = SM["n_abs_gonad_excluded"]

    n_gsi = SM["n_by_category"]["gsi"]
    n_quantity = SM["n_by_category"]["quantity"]
    n_production = n_gsi + n_quantity
    n_quality = SM["n_by_category"]["quality"]
    n_allocation = SM["n_by_category"]["allocation"]

    # ── Overall Null Model ───────────────────────────────────────────────────
    null = M["null"]["coef"]
    null_est, null_ci_low, null_ci_high = null["est"], null["ci_low"], null["ci_high"]

    null_i2 = M["null"]["i2"]["corrected"]
    null_i2_total = null_i2["total"]
    null_i2_study = null_i2["study"]
    null_i2_species = null_i2["species"]
    null_i2_phylo = null_i2["phylo"]

    # ── Trait Categories (Model 1) ───────────────────────────────────────────
    cat_data = {}
    for slug, (name, name_short) in CATEGORY_META.items():
        c = M["model1"]["coef"][f"category{slug}"]
        k = SM["n_by_category"][slug]
        interp, favours, sig = interpret(slug, c["ci_low"], c["ci_high"])
        cat_data[slug] = {
            "name": name,
            "name_short": name_short,
            "slug": slug,
            "k": k,
            "pct_k": f"{(k / n_effects * 100):.1f}%",
            "est": c["est"],
            "ci_low": c["ci_low"],
            "ci_high": c["ci_high"],
            "p": c["p"],
            "interpretation": interp,
            "favours": favours,
            "sig": sig,
        }

    # Format category records
    for slug, d in cat_data.items():
        d["estimate"] = fmt_stat(d["est"])
        d["ci"] = f"{fmt_stat(d['ci_low'])} to {fmt_stat(d['ci_high'])}"
        d["estimate_ci"] = f"{d['estimate']} (95% CI {d['ci']})"
        d["estimate_ci_tbl"] = f"{d['estimate']} [{fmt_stat(d['ci_low'])}, {fmt_stat(d['ci_high'])}]"

    # Model 1 heterogeneity
    m1_i2 = M["model1"]["i2"]["corrected"]
    m1_i2_total, m1_i2_study, m1_i2_species = m1_i2["total"], m1_i2["study"], m1_i2["species"]

    # ── Model 2 (SCR) ────────────────────────────────────────────────────────
    m2_i2 = M["model2"]["i2"]["corrected"]
    m2_i2_total, m2_i2_study, m2_i2_species = m2_i2["total"], m2_i2["study"], m2_i2["species"]
    lrt = M["model2"]["lrt_scr"]

    # ── Publication bias (multilevel Egger slopes) ───────────────────────────
    eggers = {key: M[key]["egger"] for key in ("null", "model1", "model2")}

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

    # ── Table 3 rows (3-Way Methodological Reconciliation) ───────────────────
    table3 = [
        {
            "dimension": "Scope & Taxa",
            "delmatto": f"Fishes only ({n_studies} studies, {n_species} species, {n_effects} effect sizes)",
            "dougherty": "All animals (92 studies, 67 species; 58 fish studies)",
            "our_update": "Reconciled fishes master set + post-2020 literature update + non-fish extension",
        },
        {
            "dimension": "Study Overlap & Gaps",
            "delmatto": "Archived 50 fish studies (1995–2017)",
            "dougherty": "Shared 31 fish studies; missed 19 fish studies present in Del Matto",
            "our_update": "Full reconciliation (31 shared + 19 Del Matto + 27 Dougherty fish + post-2020)",
        },
        {
            "dimension": "Behavioral Allocation",
            "delmatto": f"Formal category (k = {n_allocation}, g = {cat_data['allocation']['estimate']}; majors allocate more per spawn)",
            "dougherty": "Omitted / collapsed (focused only on stripped/stored sperm counts)",
            "our_update": "Core functional axis testing ejaculate economy during mating interactions",
        },
        {
            "dimension": "Testes & GSI Allometry",
            "delmatto": f"GSI only (k = {n_gsi}, g = {cat_data['gsi']['estimate']}); {n_gonad_mass_excluded} absolute mass rows excluded",
            "dougherty": "Argued GSI is an artifact; found no effect when excluding GSI",
            "our_update": "Bivariate meta-regression modeling body mass & dimorphism as continuous allometric covariates",
        },
        {
            "dimension": "Sperm Competition Proxy",
            "delmatto": "5-level categorical SCR (Stockley 1997); extreme ranks 1 & 5 confounded",
            "dougherty": "Sneaker frequency (linear test only); found no effect",
            "our_update": "Continuous quadratic polynomial testing Parker's intermediate peak + SCR",
        },
        {
            "dimension": "Phylogeny",
            "delmatto": f"Betancur-R et al. (2017) tree, Grafen branch lengths; {SM['n_tips_added_at_genus_root']} tips as congener placeholders; dropped from final models",
            "dougherty": "Open Tree of Life synthetic tree (rotl)",
            "our_update": "Calibrated Ray-finned fish tree (Rabosky / fishtree) with Grafen branch lengths",
        },
        {
            "dimension": "Variance & Provenance",
            "delmatto": "Exact g and sampling variances archived in the 2018 analysis repository; per-morph trait means not archived",
            "dougherty": "Re-extracted per-morph statistics for included subset",
            "our_update": "Complete re-extraction with exact variances via metafor::escalc; fully open data",
        },
    ]

    crosscheck = {
        "n_delmatto_studies": SM["n_studies_all_rows"],
        "n_dougherty_studies_total": 92,
        "n_dougherty_studies_fish": 58,
        "n_shared_studies": 31,
        "n_delmatto_missed_by_dougherty": 19,
        "n_dougherty_only_fish": 27,
    }

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
            "n_extreme_effects": SM["n_extreme"],
            "max_extreme_g": f"{SM['max_abs_g']:.1f}",
        },
        "overall_null": {
            "estimate": fmt_stat(null_est),
            "ci": f"{fmt_stat(null_ci_low)} to {fmt_stat(null_ci_high)}",
            "estimate_ci": f"{fmt_stat(null_est)} (95% CI {fmt_stat(null_ci_low)} to {fmt_stat(null_ci_high)})",
            "ci_lower": fmt_stat(null_ci_low),
            "ci_upper": fmt_stat(null_ci_high),
            "i2_total": f"{null_i2_total:.2f}%",
            "i2_study": f"{null_i2_study:.2f}%",
            "i2_species": f"{null_i2_species:.2f}%",
            "i2_phylogeny": f"{null_i2_phylo:.2f}%",
            "p_val": f"{null['p']:.3f}",
            "i2_total_original_2018": f"{M['null']['i2']['original_2018']['total']:.2f}%",
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
            "k": SM["k_model2"],
            "lrt_chi2": f"{lrt['chi2']:.2f}",
            "lrt_df": lrt["df"],
            "lrt_p": fmt_p(lrt["p"]),
        },
        "publication_bias": {
            key: {
                "slope": fmt_stat(e["slope"]),
                "z": fmt_stat(e["z"], 2, sign=False),
                "p": fmt_p(e["p"]),
            }
            for key, e in eggers.items()
        },
        "crosscheck": crosscheck,
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
