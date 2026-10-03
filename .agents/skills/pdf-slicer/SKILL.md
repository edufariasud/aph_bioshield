---
name: pdf-slicer
description: >
  Fatia e extrai páginas específicas de um arquivo PDF.
  Use quando o usuário precisar separar uma seção, um capítulo ou extrair páginas isoladas de um PDF maior. Salva as páginas selecionadas em um novo arquivo PDF sem alterar a qualidade ou texto original. Operado via CLI.
version: 1.0.0
author: Antigravity Assistant
platforms: [linux, macos]
metadata:
  tags: [PDF, Fatiador, Slicer, Extração, PyPDF]
---

# PDF Slicer

Esta skill extrai um intervalo de páginas contínuas de um PDF maior, criando um novo arquivo com apenas o conteúdo desejado.

---

## ⚡ Quick Reference

> [!IMPORTANT]
> **AMBIENTE VIRTUAL OBRIGATÓRIO**
> Esta tool possui um `venv` dedicado com as dependências pré-instaladas.
> **SEMPRE** use o interpretador do venv. NUNCA use `python` ou `python3` diretamente.
>
> **Caminho correto do interpretador:**
> ```
> .agents/skills/pdf-slicer/.venv/bin/python
> ```

| Objetivo | Comando |
|---|---|
| **Fatiar um PDF (salva na mesma pasta do original)** | `.venv/bin/python scripts/pdf_slicer.py "caminho/arquivo.pdf" 10 20` |
| **Salvar em local específico** | `.venv/bin/python scripts/pdf_slicer.py "arquivo.pdf" 10 20 -o "novo_caminho.pdf"` |

---

## ⚙️ Parâmetros CLI Completos

| Argumento | Default | Descrição |
|---|---|---|
| `input_file` | **obrigatório** | O caminho absoluto para o PDF original a ser fatiado. |
| `start_page` | **obrigatório** | A página inicial da extração. **Base 1** (ex: digite `10` para extrair começando pela décima página que você vê no leitor de PDF). |
| `end_page` | **obrigatório** | A página final da extração. A página informada será **inclusa** no arquivo final. |
| `--output`, `-o` | *(opcional)* | Caminho exato de onde salvar o arquivo gerado. Se omitido, salva na mesma pasta do arquivo original com o sufixo `_sliced_INICIO_FIM.pdf`. |

---

## 🤖 Como Usar Como Agente de IA (Diretrizes Obrigatórias)

### 🚨 REGRAS DE OURO:

1. **Paginação do Usuário:** Os usuários informam páginas no formato "visual" (base-1). Por exemplo, se pedirem "das páginas 5 a 10", simplesmente passe os argumentos `5` e `10`. O script internamente já faz a conversão de índices (base-0) correta para a biblioteca `pypdf`.
2. **Ambiente Virtual (Venv):** **SEMPRE** execute o script usando o interpretador absoluto do venv do projeto: `.agents/skills/pdf-slicer/.venv/bin/python`.
3. **Caminho Absoluto:** Procure sempre usar o caminho absoluto do PDF caso o usuário referencie o arquivo na sua request.

---

## ⚠️ Troubleshooting

| Sintoma | Causa | Ação |
|---|---|---|
| `[ERROR] O arquivo não foi encontrado` | Caminho do PDF incorreto | Verifique a existência do arquivo, use aspas em caminhos com espaço |
| `[ERROR] Intervalo inválido` | A página solicitada passa do número total de páginas | Corrija a numeração |

---

## 📦 Ambiente Virtual (venv)

O projeto usa um **venv dedicado** localizado em:
```
.agents/skills/pdf-slicer/.venv/
```

> [!CAUTION]
> **NÃO use `pip install` nem `python -m pip`** — isso instalaria no Python global do sistema, não no venv.
> **NÃO use `python` ou `python3`** — o Python global não tem as dependências instaladas.
