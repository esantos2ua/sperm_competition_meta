#!/usr/bin/env python3
"""
figures.py
----------
Generates publication-quality figures for the sperm competition meta-analysis
manuscript. All estimates and bounds are taken from build/results.json and
build/model_results.json; the funnel plot uses build/effect_sizes.csv (all
three produced by analysis/01_baseline_models.R and scripts/build_results.py).

Output:
  figures/fig1_prisma_flow.png       -- PRISMA 2020 flow diagram
  figures/fig2_orchard_categories.png -- Orchard / forest plot of trait categories
  figures/fig3_heterogeneity.png     -- Heterogeneity (I^2) variance partitioning
  figures/fig4_funnel_plot.png       -- Funnel plot of effect sizes vs precision

Usage:
    python3 scripts/figures.py
"""

from __future__ import annotations

import json
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG_DIR = os.path.join(BASE_DIR, "figures")
BUILD_DIR = os.path.join(BASE_DIR, "build")

# Aesthetics
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Helvetica", "Arial"]
plt.rcParams["axes.edgecolor"] = "#333333"
plt.rcParams["axes.linewidth"] = 0.8

# Palette
NAVY = "#1a4f8a"
GREEN = "#1a7a4a"
RED = "#c0392b"
DARK_GREY = "#2c3e50"
LIGHT_GREY = "#f8f9fa"
BORDER_GREY = "#cccccc"

def load_results():
    with open(os.path.join(BUILD_DIR, "results.json"), "r", encoding="utf-8") as f:
        return json.load(f)

def load_models():
    with open(os.path.join(BUILD_DIR, "model_results.json"), "r", encoding="utf-8") as f:
        return json.load(f)

def make_fig1_prisma(R):
    """PRISMA 2020 Flow Diagram with clean layout and zero text overlap."""
    S, C = R["summary"], R["crosscheck"]
    fig, ax = plt.subplots(figsize=(9.0, 9.5), dpi=300)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    def draw_box(x, y, w, h, title, text, bg="#ffffff", border=BORDER_GREY, title_col=DARK_GREY):
        rect = patches.FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.012,rounding_size=0.02",
            facecolor=bg, edgecolor=border, linewidth=1.2
        )
        ax.add_patch(rect)
        # Title centered near top
        ax.text(x + w / 2, y + h - 0.024, title, ha="center", va="center",
                fontsize=10, weight="bold", color=title_col)
        # Subtle horizontal dividing line
        ax.plot([x + 0.02, x + w - 0.02], [y + h - 0.045, y + h - 0.045], color=border, lw=0.7, alpha=0.6)
        # Body text below line, aligned from top
        ax.text(x + w / 2, y + h - 0.062, text, ha="center", va="top",
                fontsize=8.5, color="#333333", linespacing=1.35)

    # 1. Identification
    draw_box(0.08, 0.79, 0.39, 0.16, "Identification",
             "Records identified from:\nWeb of Knowledge (n = 1,023)\nScopus (n = 659)\nTotal identified: n = 1,682",
             bg="#f0f4f8", border=NAVY, title_col=NAVY)

    draw_box(0.53, 0.79, 0.39, 0.16, "Deduplication",
             "Duplicate records removed\nbefore screening:\n(n = 579)",
             bg="#ffffff", border=BORDER_GREY)

    # 2. Screening
    draw_box(0.08, 0.55, 0.39, 0.16, "Screening",
             "Records screened on\ntitle and abstract:\n(n = 1,103)",
             bg="#ffffff", border=BORDER_GREY)

    draw_box(0.53, 0.55, 0.39, 0.16, "Screening Exclusions",
             "Records excluded:\nNot relevant to fish alternative\nmating tactics (n = 898)",
             bg="#fff5f5", border="#e0a8a8", title_col=RED)

    # 3. Eligibility
    draw_box(0.08, 0.30, 0.39, 0.17, "Full-Text Eligibility",
             "Reports assessed for eligibility:\n(n = 191 retrieved of 205 eligible)\n(14 unscreened in 2018 baseline)",
             bg="#ffffff", border=BORDER_GREY)

    draw_box(0.53, 0.30, 0.39, 0.17, "Eligibility Exclusions",
             "Reports excluded with reasons (n = 141):\n• No male morph comparison (n = 82)\n• No ejaculate traits reported (n = 37)\n• Inadequate statistical data (n = 22)",
             bg="#fff5f5", border="#e0a8a8", title_col=RED)

    # 4. Included
    draw_box(0.08, 0.04, 0.84, 0.19, "Included in Quantitative Synthesis (Baseline)",
             f"Studies included: {C['n_delmatto_studies']} ({S['n_studies']} contributing to analysed effect sizes; {S['n_species']} fish species)\n"
             f"Total effect sizes: {S['n_effects']} Hedges' g\n"
             f"• Production: {S['n_production']} ({S['n_gsi']} GSI + {S['n_quantity']} Quantity)   • Quality: {S['n_quality']} (velocity, motility, morphology)   • Allocation: {S['n_allocation']}\n"
             f"({S['n_gonad_mass_excluded']} absolute gonad mass rows excluded in original as non-independent of GSI)",
             bg="#f0f9f4", border=GREEN, title_col=GREEN)

    # Connecting arrows
    ak = dict(arrowstyle="->", lw=1.3, color="#444444")
    # Downward workflow
    ax.annotate("", xy=(0.275, 0.71), xytext=(0.275, 0.79), arrowprops=ak)
    ax.annotate("", xy=(0.275, 0.47), xytext=(0.275, 0.55), arrowprops=ak)
    ax.annotate("", xy=(0.275, 0.23), xytext=(0.275, 0.30), arrowprops=ak)

    # Rightward exclusion arrows
    ax.annotate("", xy=(0.53, 0.87), xytext=(0.47, 0.87), arrowprops=ak)
    ax.annotate("", xy=(0.53, 0.63), xytext=(0.47, 0.63), arrowprops=ak)
    ax.annotate("", xy=(0.53, 0.385), xytext=(0.47, 0.385), arrowprops=ak)

    plt.tight_layout()
    out_path = os.path.join(FIG_DIR, "fig1_prisma_flow.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"Generated {out_path}")

def make_fig2_orchard(R):
    """Orchard / forest plot of trait categories."""
    M = load_models()
    null = M["null"]["coef"]
    C = R["by_category"]
    cats = [("Overall (Null Model)", R["overall_null"]["estimate"], null["est"], null["ci_low"],
             null["ci_high"], R["summary"]["n_effects"], "#333333")]
    for slug, label, col in [("quality", "Quality", "#555555"), ("quantity", "Production (Quantity)", "#555555"),
                             ("gsi", "Production (GSI)", GREEN), ("allocation", "Allocation", RED)]:
        c = C[slug]
        cats.append((label, c["estimate"], c["est"], c["ci_low"], c["ci_high"], c["k"], col))

    fig, ax = plt.subplots(figsize=(8.5, 4.8), dpi=300)

    y_positions = np.arange(len(cats))
    
    # Reference line at zero
    ax.axvline(0, color="#888888", linestyle="--", linewidth=1.0, alpha=0.8)

    for i, (name, est_txt, est, ci_low, ci_high, k, col) in enumerate(cats):
        # CI bar
        ax.plot([ci_low, ci_high], [i, i], color=col, linewidth=2.5, solid_capstyle="round")
        # Point estimate
        ax.scatter(est, i, color=col, s=80, zorder=5, edgecolor="black", linewidth=0.5)
        # Text label with estimate
        label_side = est + 0.2 if est >= 0 else est - 0.2
        ha = "left" if est >= 0 else "right"
        ax.text(label_side, i + 0.18, f"{est_txt} [{ci_low:.2f}, {ci_high:.2f}] (k = {k})",
                va="center", ha=ha, fontsize=8.5, weight="bold" if col in [GREEN, RED] else "normal", color=col)

    ax.set_yticks(y_positions)
    ax.set_yticklabels([c[0] for c in cats], fontsize=10, weight="medium")
    ax.set_xlabel("Standardized Mean Difference (Hedges' g) [± 95% CI]", fontsize=10, weight="bold")
    ax.set_xlim(-4.2, 5.0)

    # Direction annotations
    ax.text(-3.0, -0.85, "← Favours Minors (Sneakers / Parasites)", ha="center", fontsize=9, color=GREEN, weight="bold")
    ax.text(3.0, -0.85, "Favours Majors (Bourgeois / Guards) →", ha="center", fontsize=9, color=RED, weight="bold")

    ax.grid(axis="x", linestyle=":", alpha=0.6)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    out_path = os.path.join(FIG_DIR, "fig2_orchard_categories.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"Generated {out_path}")

def make_fig3_heterogeneity(R):
    """Heterogeneity (I^2) variance partitioning."""
    fig, ax = plt.subplots(figsize=(8.0, 4.0), dpi=300)

    models = ["Null Model", "Model 1 (Variable Type)", "Model 2 (Type × SCR)"]
    M = load_models()
    i2s = [M[key]["i2"]["corrected"] for key in ("null", "model1", "model2")]
    study = [d["study"] for d in i2s]
    species = [d["species"] for d in i2s]
    phylo = [d.get("phylo", 0.0) for d in i2s]
    residual = [100 - (s + sp + ph) for s, sp, ph in zip(study, species, phylo)]

    y_pos = np.arange(len(models))
    height = 0.5

    p1 = ax.barh(y_pos, study, height, color="#2b5c8f", label="Study Identity (Paper)", edgecolor="white")
    p2 = ax.barh(y_pos, species, height, left=study, color="#48a9a6", label="Species Identity", edgecolor="white")
    p3 = ax.barh(y_pos, phylo, height, left=[s + sp for s, sp in zip(study, species)],
                 color="#d4b483", label="Phylogenetic Signal", edgecolor="white")
    p4 = ax.barh(y_pos, residual, height, left=[s + sp + ph for s, sp, ph in zip(study, species, phylo)],
                 color="#e4e4e4", label="Residual (Sampling Variance)", edgecolor="white")

    # Add text labels on the bars
    for i in range(len(models)):
        total_explained = study[i] + species[i] + phylo[i]
        ax.text(total_explained + 1.5, i, f"Total I² = {total_explained:.1f}%",
                va="center", fontsize=9, weight="bold", color="#333333")

    ax.set_yticks(y_pos)
    ax.set_yticklabels(models, fontsize=10, weight="medium")
    ax.set_xlabel("Percentage of Total Variance (%)", fontsize=10, weight="bold")
    ax.set_xlim(0, 105)
    ax.legend(loc="lower right", frameon=True, fontsize=8.5, edgecolor=BORDER_GREY)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    out_path = os.path.join(FIG_DIR, "fig3_heterogeneity.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"Generated {out_path}")

def make_fig4_funnel(R):
    """Funnel plot of observed effect sizes against their standard errors."""
    es = pd.read_csv(os.path.join(BUILD_DIR, "effect_sizes.csv"))
    g = es["yi"].to_numpy()
    se = np.sqrt(es["vi"].to_numpy())
    null_est = load_models()["null"]["coef"]["est"]
    x_lim = 15
    extreme = np.abs(g) > 8

    fig, ax = plt.subplots(figsize=(8.0, 5.0), dpi=300)

    # Funnel boundaries (95% pseudo-confidence regions around 0)
    se_max = float(np.ceil(se.max() * 10) / 10)
    se_line = np.linspace(0.0, se_max, 100)
    ax.plot(-1.96 * se_line, se_line, "k--", lw=0.8, alpha=0.7)
    ax.plot(1.96 * se_line, se_line, "k--", lw=0.8, alpha=0.7)
    ax.axvline(0, color="#888888", linestyle=":", lw=0.8)
    ax.axvline(null_est, color=NAVY, linestyle="-", lw=1.2,
               label=f"Pooled Mean (g = {R['overall_null']['estimate']})")

    ax.scatter(g[~extreme], se[~extreme], color=NAVY, alpha=0.6, s=35, edgecolor="none",
               label="Reported Effect Sizes")
    # Extreme values are drawn at the plot edge so the bulk of the data stays legible
    ax.scatter(np.clip(g[extreme], -x_lim + 0.4, x_lim - 0.4), se[extreme], color=RED, alpha=0.9,
               s=50, marker="^", label=f"Extreme Effects (|g| > 8; n = {extreme.sum()}; shown at edge)")

    ax.set_xlabel("Hedges' g", fontsize=10, weight="bold")
    ax.set_ylabel("Standard Error (SE)", fontsize=10, weight="bold")
    ax.set_xlim(-x_lim, x_lim)
    ax.set_ylim(se_max, 0.0)

    ax.legend(loc="lower left", frameon=True, fontsize=8.5, edgecolor=BORDER_GREY)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    out_path = os.path.join(FIG_DIR, "fig4_funnel_plot.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"Generated {out_path}")

def main():
    os.makedirs(FIG_DIR, exist_ok=True)
    R = load_results()
    make_fig1_prisma(R)
    make_fig2_orchard(R)
    make_fig3_heterogeneity(R)
    make_fig4_funnel(R)

if __name__ == "__main__":
    main()
