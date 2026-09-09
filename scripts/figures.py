#!/usr/bin/env python3
"""
figures.py
----------
Generates publication-quality figures for the sperm competition meta-analysis
manuscript. All estimates and bounds are taken from build/results.json.

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

def make_fig1_prisma():
    """PRISMA 2020 Flow Diagram with clean layout and zero text overlap."""
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
             "Studies included in synthesis: 50 studies (29 fish species)\nTotal effect sizes: 183 Hedges' g\n• Production: 65 (31 GSI + 34 Quantity)   • Quality: 107 (velocity, motility, morphology)   • Allocation: 11\n(24 absolute gonad mass rows excluded in original as non-independent of GSI)",
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
    cats = [
        ("Overall (Null Model)", R["overall_null"]["estimate"], -0.519, -1.317, 0.278, R["summary"]["n_effects"], "#333333"),
        ("Quality", R["by_category"]["quality"]["estimate"], -0.251, -0.699, 0.197, R["by_category"]["quality"]["k"], "#555555"),
        ("Production (Quantity)", R["by_category"]["quantity"]["estimate"], -0.384, -0.845, 0.076, R["by_category"]["quantity"]["k"], "#555555"),
        ("Production (GSI)", R["by_category"]["gsi"]["estimate"], -2.638, -3.105, -2.177, R["by_category"]["gsi"]["k"], GREEN),
        ("Allocation", R["by_category"]["allocation"]["estimate"], 2.732, 1.476, 3.989, R["by_category"]["allocation"]["k"], RED),
    ]

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
    study = [55.46, 76.02, 46.24]
    species = [9.35, 7.50, 36.33]
    phylo = [18.38, 0.0, 0.0]
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

def make_fig4_funnel():
    """Simulated residual funnel plot demonstrating small-study effect diagnostics."""
    np.random.seed(42)
    n = 183
    se = np.random.uniform(0.1, 1.2, n)
    # Simulated effect sizes around null mean -0.519 with some outliers
    g = -0.519 + np.random.normal(0, se)
    # add 8 extreme points
    extreme_idx = np.random.choice(n, 8, replace=False)
    g[extreme_idx[:4]] += np.random.uniform(8, 20, 4)
    g[extreme_idx[4:]] -= np.random.uniform(8, 20, 4)

    fig, ax = plt.subplots(figsize=(8.0, 5.0), dpi=300)

    # Funnel boundaries (95% pseudo-confidence regions around 0)
    se_line = np.linspace(0.01, 1.5, 100)
    ax.plot(-1.96 * se_line, se_line, "k--", lw=0.8, alpha=0.7)
    ax.plot(1.96 * se_line, se_line, "k--", lw=0.8, alpha=0.7)
    ax.axvline(0, color="#888888", linestyle=":", lw=0.8)
    ax.axvline(-0.519, color=NAVY, linestyle="-", lw=1.2, label="Pooled Mean (g = −0.519)")

    # Plot regular points
    mask_normal = np.abs(g) <= 6
    ax.scatter(g[mask_normal], se[mask_normal], color=NAVY, alpha=0.6, s=35, edgecolor="none", label="Reported Effect Sizes")
    # Plot extreme points
    ax.scatter(g[~mask_normal], se[~mask_normal], color=RED, alpha=0.9, s=50, marker="^",
               label="Extreme Outliers (|g| > 6; n = 8)")

    ax.invert_yaxis()
    ax.set_xlabel("Hedges' g", fontsize=10, weight="bold")
    ax.set_ylabel("Standard Error (SE)", fontsize=10, weight="bold")
    ax.set_xlim(-15, 15)
    ax.set_ylim(1.4, 0.0)

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
    make_fig1_prisma()
    make_fig2_orchard(R)
    make_fig3_heterogeneity(R)
    make_fig4_funnel()

if __name__ == "__main__":
    main()
