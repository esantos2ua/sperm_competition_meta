#!/usr/bin/env python3
"""
Generate publication-quality screening decision trees for sperm competition meta-analysis:
- Figure 1: Title/Abstract/Keywords decision tree (Stage 1)
- Figure 2: Full-text decision tree (Stage 2)
Outputs both high-DPI PNG and vector SVG formats.
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

def create_stage1_tree(output_prefix="figures/decision_tree_stage1"):
    fig, ax = plt.subplots(figsize=(10, 12.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 125)
    ax.axis("off")

    # Header badge
    header_box = FancyBboxPatch((4, 116), 38, 5.5,
                                boxstyle="round,pad=0.4,rounding_size=0.8",
                                ec="none", fc="#1e293b", zorder=3)
    ax.add_patch(header_box)
    ax.text(23, 118.75, "Title, abstract, keyword decision tree",
            ha="center", va="center", color="white", fontsize=11, fontweight="bold",
            family="DejaVu Sans", zorder=5)

    # Outer frame
    outer_frame = FancyBboxPatch((3, 3), 94, 114,
                                 boxstyle="square,pad=0",
                                 ec="#94a3b8", fc="#ffffff", lw=1.2, zorder=1)
    ax.add_patch(outer_frame)

    steps = [
        {
            "y": 103,
            "q": "Are the title, abstract, and keywords in English, Japanese, Polish,\nPortuguese, Russian, Spanish, or another accessible language?",
            "exc": "EXCLUDE\n(Not in a language that we can screen)",
            "arrow_label": "Yes / Likely"
        },
        {
            "y": 84,
            "q": "Is the publication a primary empirical study?\n(Investigating biological organisms with observational or experimental data)",
            "exc": "EXCLUDE\n(Review, theoretical model,\ncommentary, or opinion paper)",
            "arrow_label": "Yes / Likely"
        },
        {
            "y": 65,
            "q": "Is the study subject an animal species with male reproductive tactics?\n(Primary focus: Actinopterygii / fishes; Extension: other animals)",
            "exc": "EXCLUDE\n(Non-animal, plant, or female-only\npolymorphism)",
            "arrow_label": "Yes / Likely"
        },
        {
            "y": 46,
            "q": "Does the study investigate a species exhibiting discrete male alternative\nreproductive tactics (e.g., bourgeois/territorial vs. sneaker/satellite)?",
            "exc": "EXCLUDE\n(Monomorphic mating system / no\nalternative tactics described)",
            "arrow_label": "Yes / Likely"
        },
        {
            "y": 27,
            "q": "Does the study measure testes, sperm, ejaculate expenditure,\nor reproductive allocation between tactics?",
            "exc": "EXCLUDE\n(No reproductive or ejaculate\nexpenditure traits measured)",
            "arrow_label": "Yes / Likely"
        },
    ]

    q_x = 7
    q_w = 48
    box_h = 9.8
    exc_x = 64
    exc_w = 29

    for i, step in enumerate(steps):
        y = step["y"]

        # Blue question box
        q_patch = FancyBboxPatch((q_x, y - box_h/2), q_w, box_h,
                                 boxstyle="round,pad=0.3,rounding_size=1.2",
                                 ec="#0284c7", fc="#e0f2fe", lw=1.3, zorder=2)
        ax.add_patch(q_patch)
        ax.text(q_x + q_w/2, y, step["q"],
                ha="center", va="center", color="#0f172a", fontsize=8.6,
                family="DejaVu Sans", multialignment="center", linespacing=1.25, zorder=4)

        # Red dashed line and arrow to exclusion box
        line_start_x = q_x + q_w + 0.8
        line_end_x = exc_x - 3.2
        ax.plot([line_start_x, line_end_x], [y, y],
                color="#dc2626", lw=1.3, ls="--", zorder=3)

        arr = FancyArrowPatch((line_end_x, y), (exc_x - 0.5, y),
                               arrowstyle="-|>", mutation_scale=11,
                               color="#dc2626", lw=1.3, zorder=3)
        ax.add_patch(arr)

        ax.text((line_start_x + line_end_x)/2, y, "No",
                ha="center", va="center", color="#dc2626", fontsize=8.8,
                fontweight="bold", style="italic", family="DejaVu Sans", zorder=5,
                bbox=dict(boxstyle="square,pad=0.2", fc="#ffffff", ec="none"))

        # Yellow exclusion box
        exc_patch = FancyBboxPatch((exc_x, y - box_h/2), exc_w, box_h,
                                   boxstyle="round,pad=0.3,rounding_size=1.2",
                                   ec="#ca8a04", fc="#fef9c3", lw=1.2, zorder=2)
        ax.add_patch(exc_patch)
        ax.text(exc_x + exc_w/2, y, step["exc"],
                ha="center", va="center", color="#713f12", fontsize=8.3,
                family="DejaVu Sans", multialignment="center", linespacing=1.2, zorder=4)

        # Downward arrow to next step
        if i < len(steps) - 1:
            next_y = steps[i+1]["y"]
            arrow_start_y = y - box_h/2 - 0.4
            arrow_end_y = next_y + box_h/2 + 0.4
            down_arr = FancyArrowPatch((q_x + q_w/2, arrow_start_y),
                                       (q_x + q_w/2, arrow_end_y),
                                       arrowstyle="-|>", mutation_scale=11,
                                       color="#334155", lw=1.2, zorder=3)
            ax.add_patch(down_arr)
            ax.text(q_x + q_w/2, (arrow_start_y + arrow_end_y)/2, step["arrow_label"],
                    ha="center", va="center", color="#1e293b", fontsize=8.0,
                    fontweight="bold", style="italic", family="DejaVu Sans", zorder=5,
                    bbox=dict(boxstyle="square,pad=0.2", fc="#ffffff", ec="none"))

    # Terminal arrow & Green terminal box
    last_y = steps[-1]["y"]
    term_y = 10.5
    arrow_start_y = last_y - box_h/2 - 0.4
    arrow_end_y = term_y + box_h/2 + 0.4
    down_arr = FancyArrowPatch((q_x + q_w/2, arrow_start_y),
                               (q_x + q_w/2, arrow_end_y),
                               arrowstyle="-|>", mutation_scale=11,
                               color="#334155", lw=1.2, zorder=3)
    ax.add_patch(down_arr)
    ax.text(q_x + q_w/2, (arrow_start_y + arrow_end_y)/2, "Yes / Likely",
            ha="center", va="center", color="#1e293b", fontsize=8.0,
            fontweight="bold", style="italic", family="DejaVu Sans", zorder=5,
            bbox=dict(boxstyle="square,pad=0.2", fc="#ffffff", ec="none"))

    term_patch = FancyBboxPatch((q_x, term_y - box_h/2), q_w, box_h,
                                boxstyle="round,pad=0.3,rounding_size=1.2",
                                ec="#16a34a", fc="#dcfce7", lw=1.4, zorder=2)
    ax.add_patch(term_patch)
    ax.text(q_x + q_w/2, term_y, "INCLUDE for full-text screening",
            ha="center", va="center", color="#14532d", fontsize=10.2,
            fontweight="bold", family="DejaVu Sans", zorder=4)

    plt.tight_layout()
    os.makedirs("figures", exist_ok=True)
    plt.savefig(f"{output_prefix}.png", dpi=300, bbox_inches="tight")
    plt.savefig(f"{output_prefix}.svg", bbox_inches="tight")
    plt.close()
    print(f"Generated {output_prefix}.png and .svg successfully.")


def create_stage2_tree(output_prefix="figures/decision_tree_stage2"):
    fig, ax = plt.subplots(figsize=(10, 14), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 142)
    ax.axis("off")

    # Header badge
    header_box = FancyBboxPatch((4, 133), 25, 5.5,
                                boxstyle="round,pad=0.4,rounding_size=0.8",
                                ec="none", fc="#1e293b", zorder=3)
    ax.add_patch(header_box)
    ax.text(16.5, 135.75, "Fulltext decision tree",
            ha="center", va="center", color="white", fontsize=11, fontweight="bold",
            family="DejaVu Sans", zorder=5)

    # Outer frame
    outer_frame = FancyBboxPatch((3, 3), 94, 131,
                                 boxstyle="square,pad=0",
                                 ec="#94a3b8", fc="#ffffff", lw=1.2, zorder=1)
    ax.add_patch(outer_frame)

    steps = [
        {
            "y": 120,
            "q": "Is the full text available in English, Japanese, Polish, Portuguese,\nRussian, Spanish, or another accessible language?",
            "exc": "EXCLUDE\n(Full text unavailable or not in an\naccessible language)",
            "arrow_label": "Yes"
        },
        {
            "y": 101,
            "q": "Is the publication a primary empirical study?\n(Reports original observational or experimental data; not a review or duplicate)",
            "exc": "EXCLUDE\n(Secondary review, commentary, or\nduplicate publication)",
            "arrow_label": "Yes"
        },
        {
            "y": 82,
            "q": "Are male individuals explicitly categorized into at least two discrete\nalternative reproductive tactics (e.g., bourgeois/territorial vs. sneaker)?",
            "exc": "EXCLUDE\n(Pooled morphs, unassigned males, or\ncontinuous size variation without discrete tactics)",
            "arrow_label": "Yes"
        },
        {
            "y": 63,
            "q": "Is the species gonochoristic, or are discrete male tactics strictly distinguished\nin sequential / simultaneous hermaphrodites?",
            "exc": "EXCLUDE\n(Hermaphroditic species where male morphs\ncannot be unambiguously separated)",
            "arrow_label": "Yes"
        },
        {
            "y": 44,
            "q": "Are alternative male tactics compared directly for at least one target\nejaculate trait (testes mass/GSI, sperm quantity, quality, or allocation)?",
            "exc": "EXCLUDE\n(No direct between-morph comparison of\nejaculate traits)",
            "arrow_label": "Yes"
        },
        {
            "y": 25,
            "q": "Are quantitative contrast statistics reported or derivable?\n(Means + SD/SE + N, exact test statistics, or digitizable figures)",
            "exc": "EXCLUDE\n(Qualitative only, or insufficient numerical data\nafter author contact)",
            "arrow_label": "Yes"
        },
    ]

    q_x = 7
    q_w = 48
    box_h = 9.8
    exc_x = 64
    exc_w = 29

    for i, step in enumerate(steps):
        y = step["y"]

        # Blue question box
        q_patch = FancyBboxPatch((q_x, y - box_h/2), q_w, box_h,
                                 boxstyle="round,pad=0.3,rounding_size=1.2",
                                 ec="#0284c7", fc="#e0f2fe", lw=1.3, zorder=2)
        ax.add_patch(q_patch)
        ax.text(q_x + q_w/2, y, step["q"],
                ha="center", va="center", color="#0f172a", fontsize=8.4,
                family="DejaVu Sans", multialignment="center", linespacing=1.25, zorder=4)

        # Red dashed line and arrow to exclusion box
        line_start_x = q_x + q_w + 0.8
        line_end_x = exc_x - 3.2
        ax.plot([line_start_x, line_end_x], [y, y],
                color="#dc2626", lw=1.3, ls="--", zorder=3)

        arr = FancyArrowPatch((line_end_x, y), (exc_x - 0.5, y),
                               arrowstyle="-|>", mutation_scale=11,
                               color="#dc2626", lw=1.3, zorder=3)
        ax.add_patch(arr)

        ax.text((line_start_x + line_end_x)/2, y, "No",
                ha="center", va="center", color="#dc2626", fontsize=8.8,
                fontweight="bold", style="italic", family="DejaVu Sans", zorder=5,
                bbox=dict(boxstyle="square,pad=0.2", fc="#ffffff", ec="none"))

        # Yellow exclusion box
        exc_patch = FancyBboxPatch((exc_x, y - box_h/2), exc_w, box_h,
                                   boxstyle="round,pad=0.3,rounding_size=1.2",
                                   ec="#ca8a04", fc="#fef9c3", lw=1.2, zorder=2)
        ax.add_patch(exc_patch)
        ax.text(exc_x + exc_w/2, y, step["exc"],
                ha="center", va="center", color="#713f12", fontsize=8.0,
                family="DejaVu Sans", multialignment="center", linespacing=1.2, zorder=4)

        # Downward arrow to next step
        if i < len(steps) - 1:
            next_y = steps[i+1]["y"]
            arrow_start_y = y - box_h/2 - 0.4
            arrow_end_y = next_y + box_h/2 + 0.4
            down_arr = FancyArrowPatch((q_x + q_w/2, arrow_start_y),
                                       (q_x + q_w/2, arrow_end_y),
                                       arrowstyle="-|>", mutation_scale=11,
                                       color="#334155", lw=1.2, zorder=3)
            ax.add_patch(down_arr)
            ax.text(q_x + q_w/2, (arrow_start_y + arrow_end_y)/2, step["arrow_label"],
                    ha="center", va="center", color="#1e293b", fontsize=8.0,
                    fontweight="bold", style="italic", family="DejaVu Sans", zorder=5,
                    bbox=dict(boxstyle="square,pad=0.2", fc="#ffffff", ec="none"))

    # Terminal arrow & Green terminal box
    last_y = steps[-1]["y"]
    term_y = 10.0
    arrow_start_y = last_y - box_h/2 - 0.4
    arrow_end_y = term_y + box_h/2 + 0.4
    down_arr = FancyArrowPatch((q_x + q_w/2, arrow_start_y),
                               (q_x + q_w/2, arrow_end_y),
                               arrowstyle="-|>", mutation_scale=11,
                               color="#334155", lw=1.2, zorder=3)
    ax.add_patch(down_arr)
    ax.text(q_x + q_w/2, (arrow_start_y + arrow_end_y)/2, "Yes",
            ha="center", va="center", color="#1e293b", fontsize=8.0,
            fontweight="bold", style="italic", family="DejaVu Sans", zorder=5,
            bbox=dict(boxstyle="square,pad=0.2", fc="#ffffff", ec="none"))

    term_patch = FancyBboxPatch((q_x, term_y - box_h/2), q_w, box_h,
                                boxstyle="round,pad=0.3,rounding_size=1.2",
                                ec="#16a34a", fc="#dcfce7", lw=1.4, zorder=2)
    ax.add_patch(term_patch)
    ax.text(q_x + q_w/2, term_y + 1.4, "INCLUDE in master synthesis",
            ha="center", va="center", color="#14532d", fontsize=9.8,
            fontweight="bold", family="DejaVu Sans", zorder=4)
    ax.text(q_x + q_w/2, term_y - 1.8, "Actinopterygii (teleosts) -> Q1 update\nOther animal taxa -> Q1e taxonomic extension",
            ha="center", va="center", color="#166534", fontsize=7.8,
            family="DejaVu Sans", multialignment="center", zorder=4)

    plt.tight_layout()
    os.makedirs("figures", exist_ok=True)
    plt.savefig(f"{output_prefix}.png", dpi=300, bbox_inches="tight")
    plt.savefig(f"{output_prefix}.svg", bbox_inches="tight")
    plt.close()
    print(f"Generated {output_prefix}.png and .svg successfully.")

if __name__ == "__main__":
    create_stage1_tree()
    create_stage2_tree()
