#!/usr/bin/env python3
"""Bulk download Open Access papers from Semantic Scholar.

Usage:
    python bulk_download_s2.py "sociobiology" --max 20
    python bulk_download_s2.py "human ethology" --max 50 --year 2020-
    python bulk_download_s2.py "evolutionary psychology" --min-citations 100 --year 2010-2020
"""
import sys
import os
import json
import urllib.request
import urllib.parse
from datetime import datetime

S2_BASE = "https://api.semanticscholar.org"
API_KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")
DOWNLOAD_DIR = os.environ.get("ARXIV_DOWNLOAD_DIR", "./artigos/")
REGISTRY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloaded.json")
FIELDS = "title,externalIds,openAccessPdf,citationCount"

def load_registry():
    if os.path.exists(REGISTRY_PATH):
        with open(REGISTRY_PATH, "r") as f:
            return json.load(f)
    return {}

def save_registry(registry):
    with open(REGISTRY_PATH, "w") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

def make_request(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    if API_KEY:
        headers["x-api-key"] = API_KEY
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except Exception as e:
        print(f"API Error: {e}")
        return {}

def download_pdf(url, filepath):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as response, open(filepath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        
        # Verify it's actually a PDF (starts with %PDF)
        with open(filepath, 'rb') as f:
            header = f.read(4)
            if header != b'%PDF':
                os.remove(filepath)
                return False, "Not a valid PDF (likely an HTML redirect or paywall)"
        return True, "Success"
    except Exception as e:
        return False, str(e)

def bulk_download(query, max_results=20, year_filter=None, min_citations=0):
    print(f"Searching Semantic Scholar for: '{query}'...")
    q = urllib.parse.quote(query)
    
    url = f"{S2_BASE}/graph/v1/paper/search?query={q}&limit={max_results}&fields={FIELDS}&openAccessPdf=true"
    if year_filter:
        url += f"&year={year_filter}"
        
    data = make_request(url)
    papers = data.get("data", [])
    
    if not papers:
        print("No results found.")
        return

    registry = load_registry()
    success_count = 0
    
    for p in papers:
        s2_id = p.get("paperId", "")
        title = p.get("title", "Unknown Title")
        pdf_info = p.get("openAccessPdf")
        
        if not pdf_info or not pdf_info.get("url"):
            continue
            
        citations = p.get("citationCount", 0)
        if citations < min_citations:
            continue
            
        pdf_url = pdf_info.get("url")
        
        # Check registry
        if s2_id in registry:
            print(f"Skipping (already downloaded): {title[:50]}...")
            continue
            
        filename = f"{s2_id}.pdf"
        filepath = os.path.join(DOWNLOAD_DIR, filename)
        
        print(f"Attempting to download: {title[:50]}...")
        print(f"  URL: {pdf_url}")
        
        success, msg = download_pdf(pdf_url, filepath)
        
        if success:
            print(f"  ✅ SUCCESS! Saved as {filename}")
            registry[s2_id] = {
                "date": datetime.now().isoformat(),
                "filename": filename,
                "title": title
            }
            save_registry(registry)
            success_count += 1
        else:
            print(f"  ❌ FAILED: {msg}")
            
    print(f"\nBulk download complete! Successfully downloaded {success_count} papers.")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    max_results = 20
    year_filter = None
    min_citations = 0
    i = 0
    positional = []

    while i < len(args):
        if args[i] == "--max" and i + 1 < len(args):
            max_results = int(args[i + 1]); i += 2
        elif args[i] == "--year" and i + 1 < len(args):
            year_filter = args[i + 1]; i += 2
        elif args[i] == "--min-citations" and i + 1 < len(args):
            min_citations = int(args[i + 1]); i += 2
        else:
            positional.append(args[i]); i += 1

    if positional:
        bulk_download(" ".join(positional), max_results, year_filter, min_citations)
