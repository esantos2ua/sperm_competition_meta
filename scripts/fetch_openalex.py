#!/usr/bin/env python3
"""
fetch_openalex.py
-----------------
Programmatic search and citation chasing via the OpenAlex REST API for the
sperm competition meta-analysis update.

Capabilities:
  1. Boolean search in title and abstract (expanded tactic x ejaculate terms).
  2. Date filtering (e.g. post-2017 for literature update, or full range for benchmarking).
  3. Snowballing / Forward citation chasing from seminal papers:
     - Parker (1990) "Raffles and roles" (W2156828557)
     - Parker (1990) "Sneaks and EPCs" (W2165074218)
     - Stockley et al. (1997) (W2012690962)
     - Taborsky (1998) (W2160913963)
     - Dougherty et al. (2022) (W4213348123)
     - Kustra & Alonzo (2020) (W3088267208)
  4. Exports deduplicated candidates with abstracts and DOIs to data/output/openalex_search_results.csv.

Usage:
    python3 scripts/fetch_openalex.py --mode update --min-year 2017
    python3 scripts/fetch_openalex.py --mode benchmark
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
import urllib.parse
import urllib.request

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "data", "output")
MAILTO = "esantos2@ualberta.ca"
BASE_URL = "https://api.openalex.org/works"

# Expanded Boolean query blocks
TACTIC_TERMS = [
    '"alternative mating"',
    '"alternative reproductive"',
    '"sneaker male"',
    '"sneaker males"',
    '"satellite male"',
    '"satellite males"',
    '"bourgeois male"',
    '"bourgeois males"',
    '"parasitic spawning"',
    '"cuckoldry"',
    '"alternative tactics"',
    '"alternative strategies"',
    '"jack male"',
    '"jack salmon"',
]

EJACULATE_TERMS = [
    '"sperm competition"',
    '"ejaculate"',
    '"testis size"',
    '"testes size"',
    '"testis mass"',
    '"testes mass"',
    '"gonadosomatic"',
    '"GSI"',
    '"sperm velocity"',
    '"sperm motility"',
    '"sperm number"',
    '"sperm count"',
    '"sperm allocation"',
    '"spermatocrit"',
    '"milt"',
]

SEMINAL_OPENALEX_IDS = [
    "W2090428386",  # Parker (1990) Sneaks and extra-pair copulations (Proc R Soc B)
    "W2003814361",  # Parker (1990) Raffles and roles (Proc R Soc B)
    "W2064108869",  # Stockley et al. (1997) Sperm competition in fishes (Am Nat)
    "W2166426124",  # Taborsky (1998) Sperm competition in fish: bourgeois males (TREE)
    "W4214734077",  # Dougherty et al. (2022) Male alternative reproductive tactics (Biol Rev)
    "W3093437048",  # Kustra & Alonzo (2020) Sperm and alternative reproductive tactics (Phil Trans B)
]

def build_search_query() -> str:
    tactic_str = " OR ".join(TACTIC_TERMS)
    ejac_str = " OR ".join(EJACULATE_TERMS)
    return f"({tactic_str}) AND ({ejac_str})"

def query_openalex(filter_param: str, per_page: int = 100, max_results: int = 1000) -> list[dict]:
    results = []
    cursor = "*"
    headers = {"User-Agent": f"SpermCompetitionMeta/1.0 (mailto:{MAILTO})"}

    while cursor and len(results) < max_results:
        encoded_filter = urllib.parse.quote(filter_param, safe=":,><=()-\"*")
        url = f"{BASE_URL}?filter={encoded_filter}&per-page={per_page}&cursor={cursor}&mailto={MAILTO}"
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            print(f"Error querying OpenAlex API: {e}", file=sys.stderr)
            break

        batch = data.get("results", [])
        if not batch:
            break
        results.extend(batch)
        cursor = data.get("meta", {}).get("next_cursor")
        print(f"  Retrieved {len(results)} / {data.get('meta', {}).get('count', 0)} works...")
        time.sleep(0.12)  # Polite pool spacing

    return results

def reconstruct_abstract(inverted_index: dict | None) -> str:
    if not inverted_index:
        return ""
    words = sorted([(pos, word) for word, positions in inverted_index.items() for pos in positions])
    return " ".join(word for pos, word in words)

def extract_work_record(w: dict, search_type: str) -> dict:
    source_obj = w.get("primary_location", {}) or {}
    source_name = source_obj.get("source", {}).get("display_name", "") if source_obj.get("source") else ""
    authors = [a.get("author", {}).get("display_name", "") for a in w.get("authorships", [])]
    
    return {
        "openalex_id": w.get("id", ""),
        "doi": w.get("doi", ""),
        "title": w.get("title", ""),
        "publication_year": w.get("publication_year", ""),
        "publication_date": w.get("publication_date", ""),
        "journal_or_venue": source_name,
        "authors": "; ".join(authors),
        "cited_by_count": w.get("cited_by_count", 0),
        "is_oa": w.get("open_access", {}).get("is_oa", False),
        "oa_url": w.get("open_access", {}).get("oa_url", ""),
        "search_type": search_type,
        "abstract": reconstruct_abstract(w.get("abstract_inverted_index")),
    }

def main():
    parser = argparse.ArgumentParser(description="Fetch literature candidates from OpenAlex API.")
    parser.add_argument("--mode", choices=["update", "benchmark", "citations"], default="update",
                        help="'update' (post-2016 search + citations), 'benchmark' (all years), 'citations' (forward citing only)")
    parser.add_argument("--min-year", type=int, default=2017, help="Minimum publication year for update mode.")
    parser.add_argument("--max-results", type=int, default=1500, help="Maximum records to retrieve per query.")
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    all_records = {}

    query_str = build_search_query()

    if args.mode in ["update", "benchmark"]:
        print(f"=== Running OpenAlex Boolean Query (Mode: {args.mode}) ===")
        date_filter = f",from_publication_date:{args.min_year}-01-01" if args.mode == "update" else ""
        filter_param = f"title_and_abstract.search:{query_str}{date_filter}"
        works = query_openalex(filter_param, max_results=args.max_results)
        for w in works:
            rec = extract_work_record(w, search_type="boolean_search")
            all_records[rec["openalex_id"]] = rec
        print(f"Retrieved {len(works)} records from Boolean query.")

    if args.mode in ["update", "citations"]:
        print("\n=== Running Forward Citation Chasing (Snowballing) on Seminal Works ===")
        for seed_id in SEMINAL_OPENALEX_IDS:
            date_filter = f",from_publication_date:{args.min_year}-01-01" if args.mode == "update" else ""
            filter_param = f"cites:{seed_id}{date_filter}"
            print(f"Fetching works citing {seed_id}...")
            citing_works = query_openalex(filter_param, max_results=400)
            for w in citing_works:
                rec = extract_work_record(w, search_type=f"cites_{seed_id}")
                if rec["openalex_id"] not in all_records:
                    all_records[rec["openalex_id"]] = rec
            print(f"  Total citing works: {len(citing_works)}")

    out_file = os.path.join(OUTPUT_DIR, f"openalex_{args.mode}_candidates.csv")
    fields = [
        "openalex_id", "doi", "title", "publication_year", "publication_date",
        "journal_or_venue", "authors", "cited_by_count", "is_oa", "oa_url",
        "search_type", "abstract"
    ]

    with open(out_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for rec in all_records.values():
            writer.writerow(rec)

    print(f"\nSuccessfully wrote {len(all_records)} unique records to {out_file}.")

if __name__ == "__main__":
    main()
