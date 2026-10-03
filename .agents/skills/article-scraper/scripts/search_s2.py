#!/usr/bin/env python3
"""Search Semantic Scholar — covers all disciplines (not just CS/Physics like arXiv).

Usage:
    python search_s2.py "human ethology"
    python search_s2.py "sociobiology" --max 10
    python search_s2.py --id arXiv:2402.03300
    python search_s2.py --citations arXiv:2402.03300
    python search_s2.py --references arXiv:2402.03300
    python search_s2.py --author "Eibl-Eibesfeldt" --max 5

API key is read from SEMANTIC_SCHOLAR_API_KEY env var (optional, increases rate limit).
"""
import sys
import os
import json
import time
import urllib.request
import urllib.parse

S2_BASE = "https://api.semanticscholar.org"
API_KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")

FIELDS = "title,authors,year,citationCount,influentialCitationCount,externalIds,openAccessPdf,abstract,fieldsOfStudy"

def make_request(url):
    headers = {"User-Agent": "HermesAgent/1.0"}
    if API_KEY:
        headers["x-api-key"] = API_KEY
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
        sys.exit(1)


def print_paper(p, i=None):
    prefix = f"{i}. " if i else "   "
    title = p.get("title", "No title")
    year = p.get("year", "?")
    citations = p.get("citationCount", 0)
    influential = p.get("influentialCitationCount", 0)
    authors = ", ".join(a.get("name", "") for a in (p.get("authors") or [])[:5])
    abstract = (p.get("abstract") or "")[:300]
    fields = ", ".join(p.get("fieldsOfStudy") or [])
    pdf = (p.get("openAccessPdf") or {}).get("url", "")

    ext_ids = p.get("externalIds") or {}
    arxiv_id = ext_ids.get("ArXiv", "")
    doi = ext_ids.get("DOI", "")
    s2_id = p.get("paperId", "")

    print(f"{prefix}{title} ({year})")
    print(f"   Authors: {authors}")
    print(f"   Citations: {citations} ({influential} influential) | Fields: {fields}")
    if abstract:
        print(f"   Abstract: {abstract}{'...' if len(p.get('abstract','')) > 300 else ''}")
    if pdf:
        print(f"   Open Access PDF: {pdf}")
    if arxiv_id:
        print(f"   arXiv: https://arxiv.org/abs/{arxiv_id}")
    if doi:
        print(f"   DOI: https://doi.org/{doi}")
    print(f"   S2: https://www.semanticscholar.org/paper/{s2_id}")
    print()


def search_papers(query, max_results=5):
    q = urllib.parse.quote(query)
    url = f"{S2_BASE}/graph/v1/paper/search?query={q}&limit={max_results}&fields={FIELDS}"
    data = make_request(url)
    papers = data.get("data", [])
    total = data.get("total", 0)
    print(f"Found {total} results (showing {len(papers)})\n")
    for i, p in enumerate(papers, 1):
        print_paper(p, i)


def get_paper(paper_id):
    url = f"{S2_BASE}/graph/v1/paper/{urllib.parse.quote(paper_id)}?fields={FIELDS}"
    p = make_request(url)
    print_paper(p)


def get_citations(paper_id, max_results=10):
    url = f"{S2_BASE}/graph/v1/paper/{urllib.parse.quote(paper_id)}/citations?fields=title,authors,year,citationCount&limit={max_results}"
    data = make_request(url)
    papers = [item.get("citingPaper", {}) for item in data.get("data", [])]
    print(f"Papers citing {paper_id} (showing {len(papers)}):\n")
    for i, p in enumerate(papers, 1):
        print_paper(p, i)


def get_references(paper_id, max_results=10):
    url = f"{S2_BASE}/graph/v1/paper/{urllib.parse.quote(paper_id)}/references?fields=title,authors,year,citationCount&limit={max_results}"
    data = make_request(url)
    papers = [item.get("citedPaper", {}) for item in data.get("data", [])]
    print(f"References from {paper_id} (showing {len(papers)}):\n")
    for i, p in enumerate(papers, 1):
        print_paper(p, i)


def search_author(name, max_results=5):
    q = urllib.parse.quote(name)
    url = f"{S2_BASE}/graph/v1/author/search?query={q}&fields=name,hIndex,citationCount,paperCount&limit={max_results}"
    data = make_request(url)
    authors = data.get("data", [])
    print(f"Authors matching '{name}':\n")
    for i, a in enumerate(authors, 1):
        print(f"{i}. {a.get('name')} | h-index: {a.get('hIndex')} | Citations: {a.get('citationCount')} | Papers: {a.get('paperCount')}")
        print(f"   S2: https://www.semanticscholar.org/author/{a.get('authorId')}")
        print()


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    if not API_KEY:
        print("⚠️  SEMANTIC_SCHOLAR_API_KEY not set — using unauthenticated (1 req/sec limit).\n")

    max_results = 5
    i = 0
    positional = []

    while i < len(args):
        if args[i] == "--max" and i + 1 < len(args):
            max_results = int(args[i + 1]); i += 2
        elif args[i] == "--id" and i + 1 < len(args):
            get_paper(args[i + 1]); sys.exit(0)
        elif args[i] == "--citations" and i + 1 < len(args):
            get_citations(args[i + 1], max_results); sys.exit(0)
        elif args[i] == "--references" and i + 1 < len(args):
            get_references(args[i + 1], max_results); sys.exit(0)
        elif args[i] == "--author" and i + 1 < len(args):
            search_author(args[i + 1], max_results); sys.exit(0)
        else:
            positional.append(args[i]); i += 1

    if positional:
        search_papers(" ".join(positional), max_results)
