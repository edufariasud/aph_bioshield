---
name: academic-research-hub
description: "Search and retrieve papers from multiple academic databases: arXiv (Physics/CS), PubMed (Biology/Medicine), Semantic Scholar (All disciplines). DO NOT search all at once. Choose the right one based on the topic."
version: 1.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Research, Arxiv, PubMed, Semantic Scholar, Academic, Science, API]
    related_skills: [ocr-and-documents]
---

# Academic Research Hub (arXiv, PubMed, Semantic Scholar)

This skill provides a unified interface for academic research. 
**CRITICAL RULE (THE ROUTER):** Never search all databases at once. Choose the correct database based on the topic:

- 🧠 **PubMed:** Use for Biology, Medicine, Psychology, Ethology, Neuroscience, Health.
- 💻 **arXiv:** Use for Physics, Math, Computer Science (AI/ML), Statistics.
- 🌐 **Semantic Scholar:** Use as a fallback for Humanities, Social Sciences, or broad interdisciplinary searches.

## ⭐ Novo: Busca Top Articles (Modo Curado)

Use `fetch_top_articles.py` quando quiser baixar os artigos **mais impactantes** sobre um tema sem precisar decidir quais são. O script divide automaticamente a busca em dois batches:
- **Mais citados dos últimos 24 meses** (o que é relevante agora)
- **Mais citados de todos os tempos** (os clássicos do campo)

A quantidade pedida é **arredondada para baixo ao par mais próximo** (ex: 7 → 6) pois metade vai para cada batch.

```bash
# Baixar os 6 melhores artigos sobre etologia humana (3 recentes + 3 clássicos)
python scripts/fetch_top_articles.py "etologia humana" --n 6

# Múltiplas palavras-chave separadas por ";" — a quantidade se aplica a cada uma
python scripts/fetch_top_articles.py "sociobiologia;apego;trauma" --n 6
```

---

## Quick Reference

| Action | Command | Database |
|--------|---------|----------|
| **Busca curada (top citados)** | `python scripts/fetch_top_articles.py "TEMA" --n N` | Semantic Scholar |
| **Busca curada (multi-tema)** | `python scripts/fetch_top_articles.py "TEMA1;TEMA2" --n N` | Semantic Scholar |
| Search Biology/Medicine | `python scripts/search_pubmed.py "QUERY"` | PubMed |
| Search CS/Math/Physics | `python scripts/search_arxiv.py "QUERY"` | arXiv |
| Search All Disciplines | `python scripts/search_s2.py "QUERY"` | Semantic Scholar |
| Download PDF | `python scripts/download_arxiv.py ID` | arXiv only |
| Read abstract (web) | `web_extract(urls=["https://arxiv.org/abs/ID"])` | arXiv only |


## Searching Papers

The API returns Atom XML. Parse with `grep`/`sed` or pipe through `python3` for clean output.

### Basic search

```bash
curl -s "https://export.arxiv.org/api/query?search_query=all:GRPO+reinforcement+learning&max_results=5"
```

### Clean output (parse XML to readable format)

```bash
curl -s "https://export.arxiv.org/api/query?search_query=all:GRPO+reinforcement+learning&max_results=5&sortBy=submittedDate&sortOrder=descending" | python3 -c "
import sys, xml.etree.ElementTree as ET
ns = {'a': 'http://www.w3.org/2005/Atom'}
root = ET.parse(sys.stdin).getroot()
for i, entry in enumerate(root.findall('a:entry', ns)):
    title = entry.find('a:title', ns).text.strip().replace('\n', ' ')
    arxiv_id = entry.find('a:id', ns).text.strip().split('/abs/')[-1]
    published = entry.find('a:published', ns).text[:10]
    authors = ', '.join(a.find('a:name', ns).text for a in entry.findall('a:author', ns))
    summary = entry.find('a:summary', ns).text.strip()[:200]
    cats = ', '.join(c.get('term') for c in entry.findall('a:category', ns))
    print(f'{i+1}. [{arxiv_id}] {title}')
    print(f'   Authors: {authors}')
    print(f'   Published: {published} | Categories: {cats}')
    print(f'   Abstract: {summary}...')
    print(f'   PDF: https://arxiv.org/pdf/{arxiv_id}')
    print()
"
```

## Search Query Syntax

| Prefix | Searches | Example |
|--------|----------|---------|
| `all:` | All fields | `all:transformer+attention` |
| `ti:` | Title | `ti:large+language+models` |
| `au:` | Author | `au:vaswani` |
| `abs:` | Abstract | `abs:reinforcement+learning` |
| `cat:` | Category | `cat:cs.AI` |
| `co:` | Comment | `co:accepted+NeurIPS` |

### Boolean operators

```
# AND (default when using +)
search_query=all:transformer+attention

# OR
search_query=all:GPT+OR+all:BERT

# AND NOT
search_query=all:language+model+ANDNOT+all:vision

# Exact phrase
search_query=ti:"chain+of+thought"

# Combined
search_query=au:hinton+AND+cat:cs.LG
```

## Sort and Pagination

| Parameter | Options |
|-----------|---------|
| `sortBy` | `relevance`, `lastUpdatedDate`, `submittedDate` |
| `sortOrder` | `ascending`, `descending` |
| `start` | Result offset (0-based) |
| `max_results` | Number of results (default 10, max 30000) |

```bash
# Latest 10 papers in cs.AI
curl -s "https://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending&max_results=10"
```

## Fetching Specific Papers

```bash
# By arXiv, Semantic Scholar ID
curl -s "https://export.arxiv.org/api/query?id_list=2402.03300"

# Multiple papers
curl -s "https://export.arxiv.org/api/query?id_list=2402.03300,2401.12345,2403.00001"
```

## BibTeX Generation

After fetching metadata for a paper, generate a BibTeX entry:

{% raw %}
```bash
curl -s "https://export.arxiv.org/api/query?id_list=1706.03762" | python3 -c "
import sys, xml.etree.ElementTree as ET
ns = {'a': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}
root = ET.parse(sys.stdin).getroot()
entry = root.find('a:entry', ns)
if entry is None: sys.exit('Paper not found')
title = entry.find('a:title', ns).text.strip().replace('\n', ' ')
authors = ' and '.join(a.find('a:name', ns).text for a in entry.findall('a:author', ns))
year = entry.find('a:published', ns).text[:4]
raw_id = entry.find('a:id', ns).text.strip().split('/abs/')[-1]
cat = entry.find('arxiv:primary_category', ns)
primary = cat.get('term') if cat is not None else 'cs.LG'
last_name = entry.find('a:author', ns).find('a:name', ns).text.split()[-1]
print(f'@article{{{last_name}{year}_{raw_id.replace(\".\", \"\")},')
print(f'  title     = {{{title}}},')
print(f'  author    = {{{authors}}},')
print(f'  year      = {{{year}}},')
print(f'  eprint    = {{{raw_id}}},')
print(f'  archivePrefix = {{arXiv, Semantic Scholar}},')
print(f'  primaryClass  = {{{primary}}},')
print(f'  url       = {{https://arxiv.org/abs/{raw_id}}}')
print('}')
"
```
{% endraw %}

## Downloading Papers

All papers are downloaded to the standard drive path: `./artigos/`

### Using Helper Script (Recommended)
```bash
python scripts/download_arxiv.py 2402.03300
python scripts/download_arxiv.py 2402.03300,2401.12345
```

### Using curl manually
```bash
curl -s -o "./artigos/2402.03300.pdf" "https://arxiv.org/pdf/2402.03300.pdf"
```

## Reading Paper Content

After finding a paper, read it inline without downloading:

```
# Abstract page (fast, metadata + abstract)
web_extract(urls=["https://arxiv.org/abs/2402.03300"])

# Full paper (PDF → markdown)
web_extract(urls=["https://arxiv.org/pdf/2402.03300"])
```

For local PDF processing, see the `ocr-and-documents` skill.

## Common Categories

| Category | Field |
|----------|-------|
| `cs.AI` | Artificial Intelligence |
| `cs.CL` | Computation and Language (NLP) |
| `cs.CV` | Computer Vision |
| `cs.LG` | Machine Learning |
| `cs.CR` | Cryptography and Security |
| `stat.ML` | Machine Learning (Statistics) |
| `math.OC` | Optimization and Control |
| `physics.comp-ph` | Computational Physics |

Full list: https://arxiv.org/category_taxonomy

## Helper Scripts

### search_arxiv.py — arXiv (CS, Physics, Math, Stats)

```bash
python scripts/search_arxiv.py "GRPO reinforcement learning"
python scripts/search_arxiv.py "transformer attention" --max 10 --sort date
python scripts/search_arxiv.py --author "Yann LeCun" --max 5
python scripts/search_arxiv.py --category cs.AI --sort date
python scripts/search_arxiv.py --id 2402.03300
python scripts/search_arxiv.py --id 2402.03300,2401.12345
```

### search_s2.py — Semantic Scholar (ALL disciplines)

Better for: broad interdisciplinary searches.
Requires `SEMANTIC_SCHOLAR_API_KEY` env var for reliable rate limits.

```bash
python scripts/search_s2.py "human ethology" --max 5
python scripts/search_s2.py "sociobiology" --max 10
python scripts/search_s2.py --author "Eibl-Eibesfeldt" --max 5
python scripts/search_s2.py --id arXiv:2402.03300
python scripts/search_s2.py --citations arXiv:2402.03300
python scripts/search_s2.py --references arXiv:2402.03300
```

### search_pubmed.py — PubMed (Biology, Medicine, Psychology)

The gold standard for life sciences and human behavior. No API key required.

```bash
python scripts/search_pubmed.py "human ethology" --max 5
python scripts/search_pubmed.py "evolutionary psychology" --max 10
```

No external dependencies — uses only Python stdlib.

---

## Semantic Scholar (Citations, Related Papers, Author Profiles)

arXiv doesn't provide citation data or recommendations. Use the **Semantic Scholar API** for that — free, no key needed for basic use (1 req/sec), returns JSON.

### Get paper details + citations

```bash
# By arXiv ID
curl -s "https://api.semanticscholar.org/graph/v1/paper/arXiv:2402.03300?fields=title,authors,citationCount,referenceCount,influentialCitationCount,year,abstract" | python3 -m json.tool

# By Semantic Scholar paper ID or DOI
curl -s "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1234/example?fields=title,citationCount"
```

### Get citations OF a paper (who cited it)

```bash
curl -s "https://api.semanticscholar.org/graph/v1/paper/arXiv:2402.03300/citations?fields=title,authors,year,citationCount&limit=10" | python3 -m json.tool
```

### Get references FROM a paper (what it cites)

```bash
curl -s "https://api.semanticscholar.org/graph/v1/paper/arXiv:2402.03300/references?fields=title,authors,year,citationCount&limit=10" | python3 -m json.tool
```

### Search papers (alternative to arXiv search, returns JSON)

```bash
curl -s "https://api.semanticscholar.org/graph/v1/paper/search?query=GRPO+reinforcement+learning&limit=5&fields=title,authors,year,citationCount,externalIds" | python3 -m json.tool
```

### Get paper recommendations

```bash
curl -s -X POST "https://api.semanticscholar.org/recommendations/v1/papers/" \
  -H "Content-Type: application/json" \
  -d '{"positivePaperIds": ["arXiv:2402.03300"], "negativePaperIds": []}' | python3 -m json.tool
```

### Author profile

```bash
curl -s "https://api.semanticscholar.org/graph/v1/author/search?query=Yann+LeCun&fields=name,hIndex,citationCount,paperCount" | python3 -m json.tool
```

### Useful Semantic Scholar fields

`title`, `authors`, `year`, `abstract`, `citationCount`, `referenceCount`, `influentialCitationCount`, `isOpenAccess`, `openAccessPdf`, `fieldsOfStudy`, `publicationVenue`, `externalIds` (contains arXiv ID, DOI, etc.)

---

## Complete Research Workflow

1. **Route**: Decide the database using the Router rules at the top of this file.
2. **Discover (CS/Physics)**: `python scripts/search_arxiv.py "your topic" --sort date --max 10`
3. **Discover (Biology/Medicine)**: `python scripts/search_pubmed.py "your topic" --max 10`
4. **Discover (Broad/Social)**: `python scripts/search_s2.py "your topic" --max 10`
5. **Assess impact**: `python scripts/search_s2.py --id arXiv:ID` (shows citation counts)
6. **Read abstract**: `web_extract(urls=["https://arxiv.org/abs/ID"])`
7. **Read full paper**: `web_extract(urls=["https://arxiv.org/pdf/ID"])`
8. **Find related work**: `python scripts/search_s2.py --references arXiv:ID`
9. **Get recommendations**: POST to Semantic Scholar recommendations endpoint
10. **Track authors**: `python scripts/search_s2.py --author "NAME"`

## Rate Limits

| API | Rate | Auth |
|-----|------|------|
| arXiv | ~1 req / 3 seconds | None needed |
| Semantic Scholar | 1 req / second | None (100/sec with API key) |
| PubMed | 3 req / second | None (10/sec with API key) |

## Notes

- arXiv returns Atom XML — use the helper script or parsing snippet for clean output
- Semantic Scholar returns JSON — pipe through `python3 -m json.tool` for readability
- PubMed returns JSON via E-utilities — use the helper script for clean output
- arXiv IDs: old format (`hep-th/0601001`) vs new (`2402.03300`)
- PDF: `https://arxiv.org/pdf/{id}` — Abstract: `https://arxiv.org/abs/{id}`
- HTML (when available): `https://arxiv.org/html/{id}`
- For local PDF processing, see the `ocr-and-documents` skill

## ID Versioning

- `arxiv.org/abs/1706.03762` always resolves to the **latest** version
- `arxiv.org/abs/1706.03762v1` points to a **specific** immutable version
- When generating citations, preserve the version suffix you actually read to prevent citation drift (a later version may substantially change content)
- The API `<id>` field returns the versioned URL (e.g., `http://arxiv.org/abs/1706.03762v7`)

## Withdrawn Papers

Papers can be withdrawn after submission. When this happens:
- The `<summary>` field contains a withdrawal notice (look for "withdrawn" or "retracted")
- Metadata fields may be incomplete
- Always check the summary before treating a result as a valid paper
