# 📚 Acervo de Referências Acadêmicas Brasileiras & LaTeX

Esta pasta reúne os templates canônicos, estilos e guias de formatação acadêmica para o agente **Aluno Nota 90**, servindo como base para a criação da skill personalizada de LaTeX para a faculdade.

---

## 📂 Arquivos Disponíveis

| Arquivo | Descrição | Utilidade Principal |
| :--- | :--- | :--- |
| **`modelo_tcc_artigo_direito_univassouras.tex`** | **MODELO PADRÃO ABSOLUTO:** Template canônico ABNT baseado no modelo da Univassouras Maricá (Arial 12, margens 3/2cm, folha de aprovação com banca, epígrafe 8cm, resumo ABNT 6028, estrutura completa). | **Modelo padrão obrigatório para TCCs, monografias e artigos acadêmicos quando o usuário não especificar outro modelo.** |
| **`modelo_canonico_tcc_artigo_abnt.md`** | Manual e guia completo com especificação de cada elemento pré-textual, textual e pós-textual. | Consulta rápida de normas, citações diretas/indiretas e formatação ABNT. |
| **`referencias.bib`** | Base BibTeX padrão para o modelo Univassouras Maricá. | Referências bibliográficas no padrão ABNT NBR 6023. |
| **`MODELO DE TCC DIREITO UNIVASSOURAS MARICÁ.docx`** | Arquivo Word (.docx) original fornecido pela instituição. | Preservação da fonte primária institucional. |
| **`sbc.sty`** | Arquivo de estilo oficial da Sociedade Brasileira de Computação (SBC). | Formatação padrão de artigos científicos e simpósios de computação. |
| **`sbc-template.tex`** | Modelo/esqueleto completo de artigo da SBC com preâmbulo, resumo, seções e bibliografia. | Base pronta para escrever artigos acadêmicos da faculdade. |
| **`sbc-template.bib`** | Arquivo BibTeX de exemplo com citações de livros, conferências e periódicos. | Gestão de referências bibliográficas da SBC. |
| **`modelo_abntex2_trabalho_academico.tex`** | Template canônico genérico em ABNTeX2. | Relatórios de disciplinas e trabalhos acadêmicos genéricos. |
| **`guia_codigo_fonte_listings_minted.md`** | Guia definitivo de inclusão de código-fonte (Python, Java, SQL, TypeScript/JS, C++) com suporte a UTF-8/acentos e `minted`. | Trabalhos práticos de programação, banco de dados e arquitetura de software. |

---

## 🛠️ Como Integrar com as Skills Instaladas
Ao lado desta pasta, em `.agents/skills/`, estão as 4 skills de referência instaladas:
- `latex-paper-en` (Diagnóstico de erros e escrita acadêmica)
- `latex-formatting` (Equações e tabelas)
- `latex-document-skill` (Scripts de compilação direta)
- `latex-writing` (Estruturação de relatórios técnicos)
