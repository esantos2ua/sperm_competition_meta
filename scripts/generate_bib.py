#!/usr/bin/env python3
"""
generate_bib.py
---------------
Generates references/references.bib from the citation key table in protocol/02_update_protocol.md.
Ensures all 74 citation keys resolve properly during Typst compilation.
"""

import re
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROTOCOL_FILE = os.path.join(BASE_DIR, "protocol", "02_update_protocol.md")
BIB_FILE = os.path.join(BASE_DIR, "references", "references.bib")

def main():
    with open(PROTOCOL_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    entries = re.findall(r'\| \`([^\`]+)\` \| ([^\|]+) \|', text)
    print(f"Found {len(entries)} citation entries in protocol.")

    bib_records = []
    
    header = """% =============================================================================
% Bibliography: Sperm competition games between majors and minors: a meta-analysis
% Single source of truth for citations: manuscript.typ cites these keys with
% @Key and Typst renders the reference list.
% =============================================================================
"""
    bib_records.append(header)

    for key, raw in entries:
        raw = raw.strip()
        year_match = re.search(r'(\d{4})', key)
        year = year_match.group(1) if year_match else "2020"

        # Check entry type
        if " In: " in raw or " in: " in raw:
            # Book chapter
            split_in = re.split(r'\. [Ii]n: ', raw, maxsplit=1)
            before_in = split_in[0]
            after_in = split_in[1]

            author_title = before_in.split(". ")
            author = author_title[0]
            title = ". ".join(author_title[1:]) if len(author_title) > 1 else ""

            book_match = re.search(r'\*(.*?)\*', after_in)
            booktitle = book_match.group(1) if book_match else after_in.split(".")[0]

            pages_match = re.search(r'p\.\s*([0-9–-]+)', after_in)
            pages = pages_match.group(1) if pages_match else ""

            entry = f"""@incollection{{{key},
  author    = {{{author}}},
  title     = {{{ornament_strip(title)}}},
  booktitle = {{{ornament_strip(booktitle)}}},
  year      = {{{year}}},
  pages     = {{{pages}}}
}}"""
        elif "dissertation" in raw.lower() or "thesis" in raw.lower():
            author = raw.split(".")[0]
            title_match = re.search(r'\*(.*?)\*', raw)
            title = title_match.group(1) if title_match else raw
            entry = f"""@phdthesis{{{key},
  author = {{{author}}},
  title  = {{{ornament_strip(title)}}},
  school = {{Instituto de Biociências, Universidade de São Paulo}},
  year   = {{{year}}}
}}"""
        elif "R Core Team" in raw or "Software" in raw or "online calculator" in raw:
            author = raw.split(".")[0]
            title_match = re.search(r'\*(.*?)\*', raw)
            title = title_match.group(1) if title_match else "Software package"
            entry = f"""@manual{{{key},
  author = {{{author}}},
  title  = {{{ornament_strip(title)}}},
  year   = {{{year}}}
}}"""
        elif "*" in raw and (";" not in raw or "Publisher" in raw or "Press" in raw or "Wiley" in raw or "Springer" in raw):
            # Book
            parts = raw.split(". *")
            if len(parts) >= 2:
                author = parts[0]
                rest = parts[1]
                title_match = re.search(r'^(.*?)\*', rest)
                title = title_match.group(1) if title_match else rest
                publisher_match = re.search(r'\*.*?\s*([A-Za-z]+:\s*[^;.]+)', raw)
                publisher = publisher_match.group(1) if publisher_match else ""
            else:
                author = raw.split(".")[0]
                title_match = re.search(r'\*(.*?)\*', raw)
                title = title_match.group(1) if title_match else raw
                publisher = ""
            entry = f"""@book{{{key},
  author    = {{{author}}},
  title     = {{{ornament_strip(title)}}},
  publisher = {{{publisher}}},
  year      = {{{year}}}
}}"""
        else:
            # Journal article
            parts = raw.split(". ")
            author = parts[0]
            rest = ". ".join(parts[1:])

            j_match = re.search(r'\*(.*?)\*', rest)
            if j_match:
                journal = j_match.group(1).rstrip(".")
                title = rest[:j_match.start()].strip(". ")
                post_j = rest[j_match.end():].strip(". ")

                vp_match = re.search(r'(\d{4})?;?\s*(\d+)\s*:\s*([0-9–A-Za-z-]+)', post_j)
                volume = vp_match.group(2) if vp_match else ""
                pages = vp_match.group(3) if vp_match else ""
            else:
                journal = ""
                title = rest
                volume = ""
                pages = ""

            entry = f"""@article{{{key},
  author  = {{{author}}},
  title   = {{{ornament_strip(title)}}},
  journal = {{{journal}}},
  year    = {{{year}}},
  volume  = {{{volume}}},
  pages   = {{{pages}}}
}}"""

        bib_records.append(entry)

    with open(BIB_FILE, "w", encoding="utf-8") as f:
        f.write("\n\n".join(bib_records) + "\n")
    print(f"Wrote {len(bib_records)-1} references to {BIB_FILE}")

def ornament_strip(s):
    return s.strip("*. \t\n\r")

if __name__ == "__main__":
    main()
