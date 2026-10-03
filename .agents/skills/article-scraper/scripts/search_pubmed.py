#!/usr/bin/env python3
"""Search PubMed (NCBI) — the premier database for biology, medicine, and psychology.

Usage:
    python search_pubmed.py "human ethology"
    python search_pubmed.py "evolutionary psychology" --max 10
    python search_pubmed.py "homo sapiens behavior" --max 5

No API key required for basic use. Free and highly reliable.
"""
import sys
import json
import urllib.request
import urllib.parse

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

def make_request(url):
    req = urllib.request.Request(url, headers={"User-Agent": "HermesAgent/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
        sys.exit(1)

def search_pubmed(query, max_results=5):
    q = urllib.parse.quote(query)
    # Step 1: Search to get IDs
    search_url = f"{BASE_URL}/esearch.fcgi?db=pubmed&term={q}&retmode=json&retmax={max_results}"
    search_data = make_request(search_url)
    
    id_list = search_data.get("esearchresult", {}).get("idlist", [])
    total = search_data.get("esearchresult", {}).get("count", 0)
    
    print(f"Found {total} results (showing {len(id_list)})\n")
    
    if not id_list:
        return

    # Step 2: Fetch summaries for those IDs
    ids_str = ",".join(id_list)
    summary_url = f"{BASE_URL}/esummary.fcgi?db=pubmed&id={ids_str}&retmode=json"
    summary_data = make_request(summary_url)
    
    result_dict = summary_data.get("result", {})
    
    for i, pmid in enumerate(id_list, 1):
        if pmid not in result_dict:
            continue
        paper = result_dict[pmid]
        
        title = paper.get("title", "No title")
        pubdate = paper.get("pubdate", "?")
        source = paper.get("source", "")
        
        authors_list = paper.get("authors", [])
        authors = ", ".join(a.get("name", "") for a in authors_list[:5])
        
        doi = ""
        for article_id in paper.get("articleids", []):
            if article_id.get("idtype") == "doi":
                doi = article_id.get("value")
                break
                
        print(f"{i}. {title} ({pubdate})")
        print(f"   Authors: {authors}")
        print(f"   Journal: {source}")
        if doi:
            print(f"   DOI: https://doi.org/{doi}")
        print(f"   PubMed: https://pubmed.ncbi.nlm.nih.gov/{pmid}/")
        print()

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    max_results = 5
    i = 0
    positional = []

    while i < len(args):
        if args[i] == "--max" and i + 1 < len(args):
            max_results = int(args[i + 1]); i += 2
        else:
            positional.append(args[i]); i += 1

    if positional:
        search_pubmed(" ".join(positional), max_results)
