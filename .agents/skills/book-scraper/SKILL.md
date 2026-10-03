---
name: book-scraper
description: "Search and programmatically download best-sellers, non-fiction, and academic books from LibGen in clean EPUB format, optimizing them for RAG and semantic slicing."
version: 1.0.0
author: Antigravity Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  antigravity:
    tags: [Books, Scraper, LibGen, EPUB, RAG, Ebook, CLI, Zero-Dependency]
    related_skills: [academic-research-hub, ocr-and-documents]
---

# Book Scraper Skill (LibGen non-fiction)

This skill provides a unified, zero-dependency command-line interface to search and download books (non-fiction, self-help, technical, academic) from Library Genesis.

> [!IMPORTANT]
> **THE EPUB PITCH:** Always prioritize `.epub` files over `.pdf`.
> PDFs have fixed layout styling, margins, headers, footers with page numbers, and page-breaking hyphenation that clutter the text. EPUB contains clean reflowable HTML, providing clean, pure text ideal for embeddings, semantic chunking, and RAG pipelines (the future "Bibliotecária").

---

## Quick Reference

| Action | CLI Command | Notes |
|--------|-------------|-------|
| **Interactive Search** | `python3 scripts/libgen_scraper.py` | Prompts for query and selection in a beautiful table |
| **Silent Search (JSON/text)** | `python3 scripts/libgen_scraper.py -q "QUERY"` | Runs search, displays results, waits for choice |
| **Download specific result** | `python3 scripts/libgen_scraper.py -q "QUERY" -i INDEX` | Directly downloads the specified index (1-based) |
| **Auto-download first match** | `python3 scripts/libgen_scraper.py -q "QUERY" -y` | Bypasses menu and downloads the top result |
| **Specify output directory** | `python3 scripts/libgen_scraper.py -q "QUERY" -y -o "PATH"` | Downloads to custom destination folder |
| **Filter extension (pdf/all)** | `python3 scripts/libgen_scraper.py -q "QUERY" -e pdf` | Changes preferred extension priority |

---

## 1. Downloading Books Autonomously (For AI Agents)

If you are an AI agent running inside this workspace, you can search and download books directly on behalf of the user using the `--index` or `--yes` options to avoid blocking on stdin prompts.

### Step 1: Perform Search & Selection
Run a search with a capped list of results to inspect options:
```bash
python3 scripts/libgen_scraper.py -q "Atomic Habits" -n 5
```

### Step 2: Download the Best Match
Once you select the best index (e.g., an EPUB with a reasonable size and clear metadata), download it directly using:
```bash
python3 scripts/libgen_scraper.py -q "Atomic Habits" -i 1
```

Or, if the first result is already perfect, download it directly:
```bash
python3 scripts/libgen_scraper.py -q "Neuroscience" -y
```

---

## 2. Directory Destination

All books are downloaded to the standard drive path:
📁 `./livros/`

The script handles folder creation automatically if it does not exist.

---

## 3. Scraper CLI Options

```bash
python3 scripts/libgen_scraper.py --help
```

- `-q, --query TEXT`: Search terms or book title (mandatory if not run interactively).
- `-e, --ext {epub,pdf,all}`: Preferred file extension format. Default: `epub`.
- `-o, --output-dir PATH`: Target output directory. Default: `./livros/`.
- `-n, --max-results INT`: Maximum number of search results to fetch and print. Default: `10`.
- `-i, --index INT`: Bypasses prompts and downloads the given result index immediately.
- `-y, --yes`: Auto-selects and downloads the top match immediately.

---

## 4. Troubleshooting

- **Connection Timeouts:** Some standard mirrors (`libgen.is`, `libgen.rs`) are blocked or throttle connections. The scraper is hardcoded to query `libgen.li`, which is highly unblocked, resilient, and fast.
- **Empty Sizes:** The scraper extracts nested size metadata from the table. If sizes appear empty, verify table column layouts in the mirror output.
- **Corrupted Downloads:** If direct streaming fails due to a network interruption, delete the partial file in `./livros/` and retry.
