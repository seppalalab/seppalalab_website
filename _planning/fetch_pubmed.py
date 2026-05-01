"""
Fetch publications from PubMed and create HugoBlox publication files.

Usage:
    python3 _planning/fetch_pubmed.py

Requirements:
    pip3 install biopython --break-system-packages

This script:
1. Searches PubMed for a given author query
2. Exports results as BibTeX to a temp file
3. Uses the `academic` tool to import them into content/publication/
"""

import os
import subprocess
import sys
import time
from Bio import Entrez, Medline

# ── Configuration ──────────────────────────────────────────────────────────────
AUTHOR_QUERY = "Seppala TT[Author]"
EMAIL = "emmihama@gmail.com"     # required by NCBI (identifies your requests)
MAX_RESULTS = 200                # increase if the author has more publications
START_DATE = "2021/01/01"        # fetch only publications on or after this date (YYYY/MM/DD), or set to None for all
OUTPUT_BIB = "_planning/pubmed_export.bib"
CONTENT_DIR = "content/publication"
# ──────────────────────────────────────────────────────────────────────────────

Entrez.email = EMAIL


def search_pubmed(query, max_results, start_date=None):
    date_info = f" from {start_date}" if start_date else ""
    print(f"Searching PubMed: {query}{date_info}")
    kwargs = dict(db="pubmed", term=query, retmax=max_results)
    if start_date:
        kwargs["datetype"] = "pdat"       # filter by publication date
        kwargs["mindate"] = start_date
        kwargs["maxdate"] = "3000/12/31"  # no upper limit
    handle = Entrez.esearch(**kwargs)
    record = Entrez.read(handle)
    handle.close()
    ids = record["IdList"]
    print(f"Found {len(ids)} records")
    return ids


def fetch_records(pmids):
    print(f"Fetching {len(pmids)} records from PubMed...")
    handle = Entrez.efetch(db="pubmed", id=pmids, rettype="medline", retmode="text")
    records = list(Medline.parse(handle))
    handle.close()
    return records


def pubtype_to_hugo(pub_types):
    """Map PubMed publication types to HugoBlox publication_types numbers."""
    if not pub_types:
        return "2"
    pt = " ".join(pub_types).lower()
    if "review" in pt:
        return "2"
    if "letter" in pt or "editorial" in pt or "comment" in pt:
        return "0"
    if "clinical trial" in pt:
        return "2"
    if "preprint" in pt:
        return "3"
    return "2"  # default: journal article


def sanitize_slug(text):
    """Create a filesystem-safe folder name."""
    import re
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text[:60].strip("-")


def author_list(record):
    authors = record.get("AU", [])
    return [a.replace(",", "").strip() for a in authors]


def create_hugo_publication(record, output_dir):
    pmid = record.get("PMID", "unknown")
    title = record.get("TI", "").rstrip(".")
    authors = author_list(record)
    journal = record.get("TA", record.get("JT", ""))
    abstract = record.get("AB", "")
    doi = record.get("LID", "").replace(" [doi]", "").split(" ")[0] if record.get("LID") else ""
    pub_types = record.get("PT", [])

    # Parse date — EDAT or DP
    date_str = record.get("DP", record.get("EDAT", "2000"))
    year = date_str[:4]
    date = f"{year}-01-01"

    # Folder name: firstauthor-year-firstword
    first_author = sanitize_slug(authors[0].split()[0]) if authors else "unknown"
    title_slug = sanitize_slug(title.split()[0] if title else "paper")
    folder_name = f"{first_author}-{year}-{title_slug}"
    folder_path = os.path.join(output_dir, folder_name)

    if os.path.exists(folder_path):
        print(f"  Skipping (already exists): {folder_name}")
        return

    os.makedirs(folder_path, exist_ok=True)

    # Format authors as YAML list
    authors_yaml = "\n".join(f"  - {a}" for a in authors)
    pub_type = pubtype_to_hugo(pub_types)

    content = f"""---
title: '{title.replace("'", "''")}'
date: '{date}'
draft: false

authors:
{authors_yaml}

publication_types: ['{pub_type}']

publication: '*{journal}*'
publication_short: ''

abstract: '{abstract.replace("'", "''")}'

featured: false

doi: '{doi}'
url_pdf: ''
url_code: ''
url_dataset: ''

tags: []
---
"""

    with open(os.path.join(folder_path, "index.md"), "w") as f:
        f.write(content)

    print(f"  Created: {folder_name}")


def main():
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    pmids = search_pubmed(AUTHOR_QUERY, MAX_RESULTS, START_DATE)
    if not pmids:
        print("No results found. Check the author query.")
        sys.exit(1)

    records = fetch_records(pmids)

    print(f"\nCreating Hugo publication files in {CONTENT_DIR}/")
    os.makedirs(CONTENT_DIR, exist_ok=True)

    for record in records:
        create_hugo_publication(record, CONTENT_DIR)
        time.sleep(0.1)  # be polite to NCBI servers

    print(f"\nDone. {len(records)} publications processed.")
    print("Review the files in content/publication/, then commit and push.")


if __name__ == "__main__":
    main()
