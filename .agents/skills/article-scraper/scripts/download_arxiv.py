#!/usr/bin/env python3
import sys
import os
import json
import urllib.request
from datetime import datetime

DOWNLOAD_DIR = os.environ.get("ARXIV_DOWNLOAD_DIR", "./artigos/")
REGISTRY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloaded.json")


def load_registry():
    if os.path.exists(REGISTRY_PATH):
        with open(REGISTRY_PATH, "r") as f:
            return json.load(f)
    return {}


def save_registry(registry):
    with open(REGISTRY_PATH, "w") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)


def download_paper(arxiv_id):
    if not arxiv_id:
        print("Error: Provide an arXiv ID.")
        return

    # Clean ID if it's a URL
    if "arxiv.org/pdf/" in arxiv_id:
        arxiv_id = arxiv_id.split("/pdf/")[-1].replace(".pdf", "")
    elif "arxiv.org/abs/" in arxiv_id:
        arxiv_id = arxiv_id.split("/abs/")[-1]

    registry = load_registry()

    if arxiv_id in registry:
        print(f"Already downloaded on {registry[arxiv_id]['date']}: {arxiv_id} — skipping.")
        return

    filename = f"{arxiv_id}.pdf"
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    filepath = os.path.join(DOWNLOAD_DIR, filename)

    print(f"Downloading {arxiv_id} to {filepath}...")

    try:
        headers = {'User-Agent': 'HermesAgent/1.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

        registry[arxiv_id] = {
            "date": datetime.now().isoformat(),
            "filename": filename
        }
        save_registry(registry)

        print(f"Successfully downloaded to: {filepath}")
    except Exception as e:
        print(f"Error downloading paper: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python download_arxiv.py <arxiv_id>")
        sys.exit(1)

    for aid in sys.argv[1:]:
        # Handle comma separated list
        for single_id in aid.split(','):
            download_paper(single_id.strip())
