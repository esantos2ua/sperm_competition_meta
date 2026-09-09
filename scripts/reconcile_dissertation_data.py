#!/usr/bin/env python3
"""
reconcile_dissertation_data.py
------------------------------
Extracts Supplementary Table 1 from references/DelMatto2018_dissertation.md,
applies the exact reconciliation rule documented in the protocol, and saves:
  1. data/input/delmatto2018_supp_table1.csv  -- Full raw table (207 rows)
  2. data/output/delmatto2018_reconciled.csv   -- Reconciled dataset (183 analyzed rows, with audit flags)
"""

import os
import re
import csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_PATH = os.path.join(BASE_DIR, "references", "DelMatto2018_dissertation.md")
INPUT_CSV = os.path.join(BASE_DIR, "data", "input", "delmatto2018_supp_table1.csv")
OUTPUT_CSV = os.path.join(BASE_DIR, "data", "output", "delmatto2018_reconciled.csv")

def main():
    os.makedirs(os.path.dirname(INPUT_CSV), exist_ok=True)
    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)

    with open(MD_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    start_idx = -1
    for i, line in enumerate(lines):
        if "**Supplementary Table 1.**" in line:
            start_idx = i
            break
    if start_idx == -1:
        raise ValueError("Could not find Supplementary Table 1 in markdown.")

    raw_rows = []
    for line in lines[start_idx:]:
        line = line.strip()
        if not line.startswith("|"):
            continue
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if not parts or parts[0] == "---" or "Species" in parts[0]:
            continue
        # Handle line-wrap fragments
        if parts[0] == "" and any(parts[1:]):
            raw_rows[-1][-1] = raw_rows[-1][-1] + " " + " ".join(p for p in parts if p)
            continue
        raw_rows.append(parts)

    print(f"Parsed {len(raw_rows)} raw rows from dissertation appendix.")

    # Clean up sources
    for r in raw_rows:
        r[-1] = re.sub(r"\s+", " ", r[-1]).strip()
        r[-1] = r[-1].replace("Leach & Montgomeri e", "Leach & Montgomerie")
        r[-1] = r[-1].replace("Hurtado- Gonzales", "Hurtado-Gonzales")

    # Write raw CSV
    header_raw = ["species", "hedges_g", "sample_size_n", "scr", "original_response_variable", "variable_type", "source"]
    with open(INPUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header_raw)
        writer.writerows(raw_rows)
    print(f"Wrote {INPUT_CSV} ({len(raw_rows)} rows)")

    # Reconciliation rule
    reconciled_rows = []
    excluded_count = 0
    gsi_count = 0
    qty_count = 0
    quality_count = 0
    alloc_count = 0

    header_out = header_raw + ["sub_category", "is_retained", "exclusion_reason"]

    for r in raw_rows:
        species, g_str, n_str, scr_str, resp, vtype, source = r
        vtype_lwr = vtype.lower()
        resp_lwr = resp.lower()

        # Check absolute gonad mass
        p1 = re.search(r'(gonad|testis|testes).*(mass|weight)', resp_lwr)
        p2 = re.search(r'(mass|weight).*(gonad|testis|testes)', resp_lwr)
        is_absolute_gonad = False
        if vtype_lwr == "production" and (p1 or p2):
            if "corrected" not in resp_lwr and "relative" not in resp_lwr and "gsi" not in resp_lwr:
                is_absolute_gonad = True

        if is_absolute_gonad:
            excluded_count += 1
            reconciled_rows.append(r + ["Absolute gonad mass", "FALSE", "Excluded in original Methods: non-independent of GSI"])
        else:
            if vtype_lwr == "production":
                if any(k in resp_lwr for k in ["gsi", "adjusted ig"]):
                    subcat = "Production / GSI"
                    gsi_count += 1
                else:
                    subcat = "Production / Quantity"
                    qty_count += 1
            elif vtype_lwr == "quality":
                subcat = "Quality"
                quality_count += 1
            elif vtype_lwr == "allocation":
                subcat = "Allocation"
                alloc_count += 1
            else:
                subcat = "Other"

            reconciled_rows.append(r + [subcat, "TRUE", ""])

    with open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header_out)
        writer.writerows(reconciled_rows)

    retained_count = len(raw_rows) - excluded_count
    print(f"Wrote {OUTPUT_CSV} ({len(reconciled_rows)} total rows: {retained_count} retained, {excluded_count} excluded).")
    print(f"  GSI: {gsi_count}")
    print(f"  Quantity: {qty_count}")
    print(f"  Quality: {quality_count}")
    print(f"  Allocation: {alloc_count}")
    assert excluded_count == 24
    assert retained_count == 183
    assert gsi_count == 31
    assert qty_count == 34
    assert quality_count == 107
    assert alloc_count == 11
    print("Reconciliation checks PASSED with 100% precision.")

if __name__ == "__main__":
    main()
