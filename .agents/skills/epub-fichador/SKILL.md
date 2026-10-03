---
name: epub-fichador
description: "Fatiador e Fichador Cognitivo Estruturado EXCLUSIVO para livros digitais no formato EPUB (.epub). Abre qualquer e-book EPUB, extrai a árvore semântica nativa por capítulos (Spine/TOC) e gera fichamentos atômicos Zettelkasten em pastas dedicadas com YAML Frontmatter rico."
version: 1.0.0
author: Antigravity Assistant
license: MIT
platforms: [linux, macos, windows]
metadata:
  tags: [EPUB, Fichamento, Slicing, Zettelkasten, Livros, Conhecimento, Agentic-OS]
  supported_formats: [epub]
---

# 📚 EPUB Fichador (Fatiador & Fichador Estruturado de Livros EPUB)

O **EPUB Fichador** é uma habilidade e ferramenta projetada para ingestão limpa, estruturada e de alta fidelidade de livros digitais. Diferente de fatiadores cegos de texto ou PDFs que sofrem com quebras de página e tabelas rompidas, o `epub-fichador` aproveita a estrutura nativa **XHTML/Spine/NCX** dos arquivos `.epub` para preservar a linha de raciocínio de cada capítulo.

> ⚠️ **RESTRIÇÃO ESTATUTÁRIA DE FORMATO:**
> Esta Skill opera **EXCLUSIVAMENTE** sobre arquivos `.epub`.
> Arquivos `.pdf`, `.docx`, `.mobi` ou `.txt` **NÃO** são suportados por esta ferramenta, pois dependem de pipelines de OCR e layout fixo distintos.

---

## 🎯 O que a Skill faz:

1. **Abertura e Mapeamento do Livro**:
   - Lê metadados canônicos do arquivo EPUB (Título da Obra, Autores, Ano, Idioma, Identificador).
   - Inspeciona o `Spine` e `manifest` do `.opf` para manter rigorosamente a ordem sequencial pretendida pelo autor.
   - Lê a tabela de conteúdo (`toc.ncx` / `nav.xhtml`) para resgatar os títulos originais dos capítulos.

2. **Criação de Diretório Dedicado**:
   - Cria automaticamente uma subpasta nomeada conforme a obra: `<output_dir>/<Autor>_-_<Titulo_Do_Livro>/`.

3. **Geração de Fichas Estruturadas (Padrão Zettelkasten)**:
   - Capítulos padrão geram uma ficha atômica completa `.md`.
   - Capítulos densos/extensos (> 3.500 palavras) são fracionados em subtópicos lógicos (Parte 1, Parte 2...) sem nunca quebrar uma sentença ao meio.
   - Cada ficha é envelopada com **YAML Frontmatter** e 7 seções cognitivas padronizadas:
     - `📌 1. Ideia Central & Tese do Capítulo`
     - `🛠️ 2. Técnicas, Modelos Mentais & Heurísticas`
     - `📖 3. Casos Reais, Estudos & Exemplos Citados`
     - `💬 4. Aplicação Prática & Tradução para o Dia a Dia`
     - `⚠️ 5. Anti-Padrões & Armadilhas (O que NÃO fazer)`
     - `💎 6. Citações & Destaques Textuais`
     - `📑 7. Conteúdo Integral Extraído do EPUB`

---

## ⚡ Guia de Referência Rápida (CLI)

```bash
# 1. Fichar um único livro EPUB:
python3 .agents/skills/epub-fichador/scripts/epub_fichador.py -i "/caminho/do/livro.epub"

# 2. Fichar com destino personalizado:
python3 .agents/skills/epub-fichador/scripts/epub_fichador.py -i "/caminho/do/livro.epub" -o "/caminho/fichas/"

# 3. Processar em lote todos os EPUBs de uma pasta:
python3 .agents/skills/epub-fichador/scripts/epub_fichador.py -i "/pasta/com/varios_epubs/" -o "/pasta/fichas/"
```

---

## ⚙️ Parâmetros CLI

- **`-i`, `--input` (Obrigatório)**:
  Caminho absoluto ou relativo para um arquivo `.epub` individual ou para uma pasta contendo um ou mais arquivos `.epub`.
- **`-o`, `--output-dir` (Opcional)**:
  Pasta de saída onde será gerado o subdiretório do livro. (Default: `./conhecimento/literatura/`).

---

### 🔒 Versionamento Git Automático (MANDATÓRIO)
Sempre que esta skill for executada, auto-fichada, gerar dados ou tiver seus arquivos/scripts alterados, execute obrigatoriamente o commit semântico no repositório correspondente no mesmo turno:
```bash
git add . && git commit -m "tipo(epub-fichador): descrição concisa da alteração"
```

