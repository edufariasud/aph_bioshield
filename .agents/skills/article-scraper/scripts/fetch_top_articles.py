#!/usr/bin/env python3
"""Baixa os artigos mais citados sobre um tema, dividindo entre os mais recentes
e os mais citados de todos os tempos.

Lógica:
  - A quantidade pedida é ARREDONDADA PARA BAIXO ao par mais próximo.
  - Metade dos artigos vem dos ÚLTIMOS 24 MESES (mais citados recentemente).
  - Metade dos artigos vem de TODOS OS TEMPOS (os mais citados da história).
  - Para múltiplas palavras-chave separadas por ";", a quantidade pedida se aplica
    a CADA palavra-chave individualmente.

Exemplos:
    python fetch_top_articles.py "etologia humana" --n 6
    python fetch_top_articles.py "sociobiologia;psicologia evolutiva" --n 10
    python fetch_top_articles.py "apego;trauma;neurociência" --n 4
"""
import sys
import os
import json
import time
import urllib.request
import urllib.parse
from datetime import datetime, timedelta

S2_BASE = "https://api.semanticscholar.org"
API_KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")
DOWNLOAD_DIR = os.environ.get("ARXIV_DOWNLOAD_DIR", "./artigos/")
REGISTRY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloaded.json")
FIELDS = "title,externalIds,openAccessPdf,citationCount,year,authors,abstract"


# ─── Helpers ─────────────────────────────────────────────────────────────────

def make_request(url, retries=3):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}
    if API_KEY:
        headers["x-api-key"] = API_KEY
    req = urllib.request.Request(url, headers=headers)
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                return json.loads(resp.read())
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2)
            else:
                print(f"  ⚠️  API Error: {e}")
                return {}

def load_registry():
    if os.path.exists(REGISTRY_PATH):
        with open(REGISTRY_PATH) as f:
            return json.load(f)
    return {}

def save_registry(registry):
    with open(REGISTRY_PATH, "w") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

def download_pdf(url, filepath):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=45) as response, open(filepath, "wb") as out:
            out.write(response.read())
        with open(filepath, "rb") as f:
            if f.read(4) != b"%PDF":
                os.remove(filepath)
                return False, "Não é um PDF válido (redirecionamento HTML ou paywall)"
        return True, "Sucesso"
    except Exception as e:
        return False, str(e)


# ─── Lógica de Busca ─────────────────────────────────────────────────────────

def get_current_year():
    return datetime.now().year

def search_papers(query, max_results, year_range=None):
    """Retorna lista de papers ordenados por citações (mais citados primeiro)."""
    q = urllib.parse.quote(query)
    url = f"{S2_BASE}/graph/v1/paper/search?query={q}&limit={max_results}&fields={FIELDS}&openAccessPdf=true"
    if year_range:
        url += f"&year={year_range}"
    data = make_request(url)
    papers = data.get("data", [])
    # Ordenar por citações (API não garante ordem por citação)
    papers.sort(key=lambda p: p.get("citationCount", 0), reverse=True)
    return papers


# ─── Download ────────────────────────────────────────────────────────────────

def process_papers(papers, keyword, batch_label, registry):
    """Tenta baixar cada paper, registra sucessos e retorna contagem."""
    success = 0
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    for p in papers:
        s2_id = p.get("paperId", "")
        title = p.get("title", "Unknown")
        year = p.get("year", "?")
        citations = p.get("citationCount", 0)
        pdf_info = p.get("openAccessPdf") or {}
        pdf_url = pdf_info.get("url", "")

        if not pdf_url:
            print(f"  ⏭️  Sem PDF aberto: {title[:60]} ({year})")
            continue

        if s2_id in registry:
            print(f"  ♻️  Já baixado: {title[:60]} ({year})")
            continue

        filename = f"{s2_id}.pdf"
        filepath = os.path.join(DOWNLOAD_DIR, filename)

        print(f"  ⬇️  [{citations} cit.] {title[:60]} ({year})")
        ok, msg = download_pdf(pdf_url, filepath)

        if ok:
            print(f"       ✅ Salvo: {filename}")
            registry[s2_id] = {
                "date": datetime.now().isoformat(),
                "filename": filename,
                "title": title,
                "keyword": keyword,
                "batch": batch_label,
                "citations": citations,
                "year": year
            }
            save_registry(registry)
            success += 1
        else:
            print(f"       ❌ Falhou: {msg}")

        time.sleep(1.5)  # respeitar rate limit da S2

    return success


# ─── Orquestrador ─────────────────────────────────────────────────────────────

def fetch_for_keyword(keyword, n_each):
    """Roda os dois batches (recentes + todos os tempos) para uma palavra-chave."""
    registry = load_registry()
    current_year = get_current_year()
    cutoff_year = current_year - 2  # últimos 24 meses ≈ últimos 2 anos

    print(f"\n{'═'*60}")
    print(f"  🔑 Palavra-chave: \"{keyword}\"")
    print(f"  📦 {n_each} artigos recentes  +  {n_each} de todos os tempos")
    print(f"{'═'*60}")

    # ── Batch 1: Mais citados nos últimos 24 meses ──
    print(f"\n🕐 BATCH 1 — Mais citados nos últimos 24 meses ({cutoff_year}-{current_year}):")
    recent_year_range = f"{cutoff_year}-{current_year}"
    # Buscar mais do que o necessário pois alguns podem não ter PDF
    recent_papers = search_papers(keyword, max_results=n_each * 3, year_range=recent_year_range)
    recent_dl = process_papers(recent_papers[:n_each * 2], keyword, "recentes_24m", registry)

    # ── Batch 2: Mais citados de todos os tempos ──
    print(f"\n🏛️  BATCH 2 — Mais citados de todos os tempos:")
    all_time_papers = search_papers(keyword, max_results=n_each * 3)
    all_time_dl = process_papers(all_time_papers[:n_each * 2], keyword, "todos_os_tempos", registry)

    total = recent_dl + all_time_dl
    print(f"\n  ✅ Concluído: {recent_dl} recentes + {all_time_dl} históricos = {total} artigos baixados.")
    return total


def run(keywords_raw, n_requested):
    # ── Arredondar para o par mais próximo (para baixo) ──
    # Mínimo absoluto: 2 (1 de cada batch). Ex: 1 → 2, 7 → 6, 10 → 10
    if n_requested <= 1:
        n_rounded = 2
    elif n_requested % 2 != 0:
        n_rounded = n_requested - 1
    else:
        n_rounded = n_requested

    n_each = n_rounded // 2

    if n_requested != n_rounded:
        reason = "mínimo é 1 de cada batch" if n_requested <= 1 else "arredondado para baixo ao par"
        print(f"⚙️  Quantidade ajustada de {n_requested} → {n_rounded} ({reason}).")
    else:
        print(f"⚙️  Baixando {n_rounded} artigos por palavra-chave.")
    print(f"   → {n_each} recente(s) + {n_each} histórico(s) por palavra-chave.\n")

    keywords = [k.strip() for k in keywords_raw.split(";") if k.strip()]
    grand_total = 0

    for kw in keywords:
        grand_total += fetch_for_keyword(kw, n_each)

    print(f"\n{'═'*60}")
    print(f"  🏁 TOTAL GERAL: {grand_total} artigos baixados.")
    print(f"  📂 Destino: {DOWNLOAD_DIR}")
    print(f"{'═'*60}\n")


# ─── CLI ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    if not API_KEY:
        print("⚠️  SEMANTIC_SCHOLAR_API_KEY não definida — usando sem autenticação (1 req/seg).\n")

    n_requested = 6  # default
    i = 0
    positional = []

    while i < len(args):
        if args[i] == "--n" and i + 1 < len(args):
            n_requested = int(args[i + 1]); i += 2
        else:
            positional.append(args[i]); i += 1

    if not positional:
        print("Erro: informe ao menos uma palavra-chave.\nExemplo: python fetch_top_articles.py \"etologia humana\" --n 6")
        sys.exit(1)

    keywords_raw = " ".join(positional)
    run(keywords_raw, n_requested)
