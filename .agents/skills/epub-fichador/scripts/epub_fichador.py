#!/usr/bin/env python3
import os
import sys
import re
import html
import zipfile
import argparse
import unicodedata
import xml.etree.ElementTree as ET

def sanitize_filename(name):
    nfkd = unicodedata.normalize('NFKD', name)
    cleaned = "".join([c for c in nfkd if not unicodedata.combining(c)])
    cleaned = re.sub(r'[^a-zA-Z0-9_ -]', '', cleaned)
    cleaned = re.sub(r'\s+', '_', cleaned).strip('_')
    return cleaned[:100]

def clean_html_to_markdown(raw_html):
    # Strip scripts, styles
    text = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', raw_html, flags=re.DOTALL | re.IGNORECASE)
    
    # Headers conversion
    text = re.sub(r'<h1[^>]*>(.*?)</h1>', r'\n\n# \1\n\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n\n## \1\n\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n\n### \1\n\n', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<h4[^>]*>(.*?)</h4>', r'\n\n#### \1\n\n', text, flags=re.DOTALL | re.IGNORECASE)
    
    # Formatting
    text = re.sub(r'<(strong|b)[^>]*>(.*?)</\1>', r'**\2**', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<(em|i)[^>]*>(.*?)</\1>', r'*\2*', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', r'\n\n> \1\n\n', text, flags=re.DOTALL | re.IGNORECASE)
    
    # Paragraphs and line breaks
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'</p>', '\n\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', text, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove all remaining HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)
    
    # Unescape HTML entities
    text = html.unescape(text)
    
    # Clean whitespace
    lines = [line.strip() for line in text.splitlines()]
    cleaned_text = re.sub(r'\n{3,}', '\n\n', '\n'.join(lines)).strip()
    return cleaned_text

class EpubBookReader:
    def __init__(self, epub_path):
        if not epub_path.lower().endswith('.epub'):
            raise ValueError(f"Formato invalido! Esta ferramenta suporta EXCLUSIVAMENTE arquivos .epub (recebido: {epub_path})")
        if not os.path.exists(epub_path):
            raise FileNotFoundError(f"Arquivo EPUB nao encontrado: {epub_path}")
            
        self.epub_path = epub_path
        self.zip = zipfile.ZipFile(epub_path, 'r')
        self.opf_dir = ""
        self.opf_path = self._locate_opf()
        self.metadata = self._extract_metadata()
        self.spine_items = self._get_spine_items()
        self.toc_titles = self._extract_toc_titles()

    def _locate_opf(self):
        container_xml = self.zip.read('META-INF/container.xml')
        root = ET.fromstring(container_xml)
        rootfile = root.find('.//{*}rootfile')
        full_path = rootfile.attrib.get('full-path', '')
        self.opf_dir = os.path.dirname(full_path)
        return full_path

    def _extract_metadata(self):
        opf_xml = self.zip.read(self.opf_path)
        root = ET.fromstring(opf_xml)
        
        def get_meta(tag_name):
            el = root.find(f'.//{{*}}{tag_name}')
            return el.text.strip() if el is not None and el.text else ""
            
        title = get_meta('title') or os.path.splitext(os.path.basename(self.epub_path))[0]
        creator = get_meta('creator') or "Autor Desconhecido"
        date = get_meta('date') or ""
        year = date[:4] if len(date) >= 4 and date[:4].isdigit() else "Ano N/A"
        language = get_meta('language') or "pt/en"
        
        return {
            'title': title,
            'author': creator,
            'year': year,
            'language': language
        }

    def _get_spine_items(self):
        opf_xml = self.zip.read(self.opf_path)
        root = ET.fromstring(opf_xml)
        
        manifest = {}
        for item in root.findall('.//{*}manifest/{*}item'):
            manifest[item.attrib.get('id')] = item.attrib.get('href')
            
        spine_hrefs = []
        for itemref in root.findall('.//{*}spine/{*}itemref'):
            idref = itemref.attrib.get('idref')
            if idref in manifest:
                href = manifest[idref]
                full_href = os.path.normpath(os.path.join(self.opf_dir, href)) if self.opf_dir else href
                spine_hrefs.append(full_href)
        return spine_hrefs

    def _extract_toc_titles(self):
        toc_map = {}
        for name in self.zip.namelist():
            if name.endswith('.ncx'):
                try:
                    ncx_xml = self.zip.read(name)
                    root = ET.fromstring(ncx_xml)
                    for navpoint in root.findall('.//{*}navPoint'):
                        label_el = navpoint.find('.//{*}text')
                        content_el = navpoint.find('.//{*}content')
                        if label_el is not None and content_el is not None:
                            src = content_el.attrib.get('src', '').split('#')[0]
                            clean_src = os.path.normpath(os.path.join(os.path.dirname(name), src))
                            if clean_src not in toc_map and label_el.text:
                                toc_map[clean_src] = label_el.text.strip()
                except Exception:
                    pass
        return toc_map

    def get_chapters(self):
        chapters = []
        chap_index = 1
        
        for href in self.spine_items:
            try:
                raw_bytes = self.zip.read(href)
                raw_html = raw_bytes.decode('utf-8', errors='ignore')
            except Exception:
                continue
                
            clean_text = clean_html_to_markdown(raw_html)
            word_count = len(clean_text.split())
            
            if word_count < 80:
                continue
                
            title = self.toc_titles.get(href, "")
            if not title:
                h_match = re.search(r'^#+\s+(.+)$', clean_text, re.MULTILINE)
                if h_match:
                    title = h_match.group(1).strip()
                else:
                    title = f"Capitulo {chap_index}"
                    
            title = re.sub(r'[\r\n\t]+', ' ', title).strip()
            
            chapters.append({
                'index': chap_index,
                'href': href,
                'title': title,
                'text': clean_text,
                'words': word_count
            })
            chap_index += 1
            
        return chapters

def split_chapter_into_fatias(chapter, max_words=3500):
    text = chapter['text']
    words = text.split()
    total_words = len(words)
    
    if total_words <= max_words:
        return [chapter]
        
    sections = re.split(r'(?=\n##+\s+)', text)
    fatias = []
    current_chunk = []
    current_count = 0
    fatia_idx = 1
    
    for sec in sections:
        sec_words = len(sec.split())
        if current_count + sec_words > max_words and current_chunk:
            chunk_text = "".join(current_chunk).strip()
            fatias.append({
                'index': chapter['index'],
                'fatia': fatia_idx,
                'title': f"{chapter['title']} (Parte {fatia_idx})",
                'text': chunk_text,
                'words': len(chunk_text.split())
            })
            fatia_idx += 1
            current_chunk = [sec]
            current_count = sec_words
        else:
            current_chunk.append(sec)
            current_count += sec_words
            
    if current_chunk:
        chunk_text = "".join(current_chunk).strip()
        fatias.append({
            'index': chapter['index'],
            'fatia': fatia_idx,
            'title': f"{chapter['title']} (Parte {fatia_idx})" if fatia_idx > 1 else chapter['title'],
            'text': chunk_text,
            'words': len(chunk_text.split())
        })
        
    return fatias

def format_ficha_content(meta, chap_info, total_fatias_in_chap=1):
    fatia_num = chap_info.get('fatia', 1)
    title_display = f"{meta['title']} - Cap {chap_info['index']:02d}: {chap_info['title']}"
    
    frontmatter = f"""---
titulo: "{title_display}"
livro: "{meta['title']}"
autor: "{meta['author']}"
ano: "{meta['year']}"
formato: "epub_nativo"
capitulo_numero: {chap_info['index']}
capitulo_titulo: "{chap_info['title']}"
fatia_numero: {fatia_num}
total_fatias_capitulo: {total_fatias_in_chap}
palavras_conteudo: {chap_info['words']}
tags:
  - livro_fichado
  - epub_fichamento
  - comunicacao
  - {sanitize_filename(meta['title']).lower()}
eixo_cognitivo:
  modalidade: "livro_fichado_epub"
  nivel: "tatico_aplicado"
  confianca: "material_integral_verificado"
resumo_executivo: "Fichamento estruturado do capitulo {chap_info['index']} da obra {meta['title']} ({meta['author']})."
---

# 📌 1. Ideia Central & Tese do Capitulo
<!-- Sintese dos argumentos nucleares e da premissa fundamental defendida pelo autor neste trecho -->

---

# 🛠️ 2. Tecnicas, Modelos Mentais & Heuristicas
<!-- Passo a passo, regras praticas, frameworks conceituais e estrategias operacionais ensinadas -->

---

# 📖 3. Casos Reais, Estudos & Exemplos Citados
<!-- Narrativas, experimentos cientificos, dialogos historicos ou anedotas usadas como evidencia -->

---

# 💬 4. Aplicacao Pratica & Traducao para o Dia a Dia
<!-- Como aplicar diretamente em conversas, interacoes interpessoais ou mensagens de texto -->

---

# ⚠️ 5. Anti-Padroes & Armadilhas (O que NAO fazer)
<!-- Vicios comuns, erros criticos e comportamentos contraproducentes alertados pelo autor -->

---

# 💎 6. Citacoes & Destaques Textuais
<!-- Frases de alto impacto e aforismos diretos da obra -->

---

# 📑 7. Conteudo Integral Extraido do EPUB
{chap_info['text']}
"""
    return frontmatter

def process_single_epub(epub_path, base_output_dir):
    print(f"\n\033[94m📖 Processando EPUB:\033[0m {epub_path}")
    reader = EpubBookReader(epub_path)
    meta = reader.metadata
    print(f"\033[92m✔ Livro identificado:\033[0m {meta['title']} | \033[96mAutor:\033[0m {meta['author']} ({meta['year']})")
    
    book_folder_name = sanitize_filename(f"{meta['author']} - {meta['title']}")
    book_dest_dir = os.path.join(base_output_dir, book_folder_name)
    os.makedirs(book_dest_dir, exist_ok=True)
    
    raw_chapters = reader.get_chapters()
    print(f"Capitulos semanticos detectados no EPUB: {len(raw_chapters)}")
    
    total_fichas = 0
    for chap in raw_chapters:
        fatias = split_chapter_into_fatias(chap)
        total_fatias = len(fatias)
        
        for f in fatias:
            fatia_idx = f.get('fatia', 1)
            filename = f"cap_{chap['index']:02d}_fatia_{fatia_idx:02d}_{sanitize_filename(chap['title'])[:40]}.md"
            filepath = os.path.join(book_dest_dir, filename)
            
            content = format_ficha_content(meta, f, total_fatias_in_chap=total_fatias)
            with open(filepath, 'w', encoding='utf-8') as out:
                out.write(content)
            total_fichas += 1
            
    print(f"\033[92m✔ Fichamento concluido com sucesso!\033[0m")
    print(f"📁 Pasta de saida: {book_dest_dir}")
    print(f"📝 Total de fichas geradas: {total_fichas}\n")
    return book_dest_dir, total_fichas

def main():
    parser = argparse.ArgumentParser(
        description="EPUB Fichador — Fatiador e Fichador Estruturado Exclusivo para Livros EPUB"
    )
    parser.add_argument("-i", "--input", required=True, help="Caminho do arquivo .epub ou diretorio contendo arquivos .epub")
    parser.add_argument("-o", "--output-dir", default="./conhecimento/literatura", help="Diretorio base de saida")
    
    args = parser.parse_args()
    
    input_path = os.path.abspath(args.input)
    output_dir = os.path.abspath(args.output_dir)
    os.makedirs(output_dir, exist_ok=True)
    
    if os.path.isfile(input_path):
        if not input_path.lower().endswith(".epub"):
            print(f"\033[91mErro Critico: O arquivo '{input_path}' nao e um EPUB!\033[0m")
            print("Esta ferramenta aceita EXCLUSIVAMENTE livros no formato .epub.")
            sys.exit(1)
        process_single_epub(input_path, output_dir)
    elif os.path.isdir(input_path):
        epubs = [os.path.join(input_path, f) for f in sorted(os.listdir(input_path)) if f.lower().endswith('.epub')]
        if not epubs:
            print(f"\033[93mAviso: Nenhum arquivo .epub encontrado no diretorio: {input_path}\033[0m")
            sys.exit(0)
        print(f"\033[95mEncontrados {len(epubs)} livros EPUB para fichamento.\033[0m")
        for ep in epubs:
            process_single_epub(ep, output_dir)
    else:
        print(f"\033[91mErro: Caminho invalido: {input_path}\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()
