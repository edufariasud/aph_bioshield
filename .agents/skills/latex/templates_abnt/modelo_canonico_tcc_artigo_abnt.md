# 📜 Modelo Canônico Absoluto de TCC & Artigo Acadêmico (ABNT / Univassouras Maricá)

> **Fonte Original:** `MODELO DE TCC DIREITO UNIVASSOURAS MARICÁ.docx`  
> **Status:** Modelo Padrão Absoluto da Skill `latex` para Trabalhos de Conclusão de Curso (TCC), Monografias e Artigos Acadêmicos quando nenhum outro modelo for explicitamente exigido pelo usuário.

---

## 📌 1. Parâmetros Tipográficos e Estruturais Obrigatórios

| Elemento | Regra Oficial | Implementação LaTeX |
| :--- | :--- | :--- |
| **Fonte Principal** | **Arial 12 pt** (ou Times New Roman) em todo o corpo | `\usepackage{helvet}` + `\renewcommand{\familydefault}{\sfdefault}` |
| **Margens** | Superior: 3,0 cm \| Esquerda: 3,0 cm<br>Inferior: 2,0 cm \| Direita: 2,0 cm | `\usepackage{geometry}` configurado com `top=3cm, bottom=2cm, left=3cm, right=2cm` |
| **Espaçamento Entrelinhas** | **1,5** no corpo do texto<br>**Simples (1,0)** para: citações diretas longas, notas de rodapé, referências bibliográficas, legendas de figuras e tabelas, epígrafe e resumo/abstract. | `\OnehalfSpacing` (geral) e `\SingleSpacing` (ambientes específicos) |
| **Recuo de Parágrafo** | 1,25 cm a 1,5 cm na primeira linha | `\setlength{\parindent}{1.5cm}` |
| **Numeração de Páginas** | Canto superior direito, algarismos arábicos a partir da primeira folha da parte textual (Introdução), embora todas as folhas a partir da folha de rosto sejam contadas. | Gerenciamento automático nativo pelo `abntex2` |

---

## 📂 2. Estrutura Canônica Sequencial

### 2.1 Elementos Pré-Textuais
1. **Capa Oficial:**
   - Nome da Instituição: `UNIVERSIDADE DE VASSOURAS / CAMPUS MARICÁ / Curso de Bacharelado em DIREITO` (ou área correspondente).
   - Nome do(a) Autor(a) em Arial 12.
   - Título do Trabalho em Arial 12 Negrito.
   - Subtítulo (opcional) em Arial 12 normal.
   - Localidade e Ano: `MARICÁ - RJ / ANO`.
2. **Folha de Rosto:**
   - Autor, Título, Subtítulo.
   - Natureza do trabalho (texto alinhado da metade da página para a direita): *"Trabalho de Conclusão de Curso apresentado ao Curso de Bacharelado em Direito da Universidade de Vassouras, Campus Maricá, como requisito parcial para obtenção do grau de Bacharel em Direito."*
   - Nome do Orientador(a) com titulação acadêmica e Coorientador(a) se houver.
   - Localidade e Ano.
3. **Folha de Aprovação (Banca Examinadora):**
   - Autor, Título, Texto de Aprovação com data e espaço para três assinaturas (Presidente/Orientador, 1º Membro e 2º Membro examinador com titulações e instituições).
4. **Dedicatória (Opcional):**
   - Homenagem e dedicatória pessoal.
5. **Agradecimentos (Opcional):**
   - Reconhecimento formal a familiares, orientador, docentes e instituições de fomento.
6. **Epígrafe (Opcional):**
   - Citação de pensamento inspirador, posicionada na metade inferior da página, com **recuo de 8 cm da margem esquerda**, espaçamento interlinear simples, **sem recurso de itálico**, mencionando abaixo autor, ano e página.
7. **Resumo em Língua Vernácula (Obrigatório — ABNT NBR 6028:2003):**
   - Parágrafo único, de **150 a 500 palavras**, com verbo na voz ativa e na 3ª pessoa do singular.
   - Apresenta: objetivo, metodologia, resultados centrais e conclusão.
   - **Palavras-chave:** De 3 a 5 termos representativos, separados entre si por **ponto final** e iniciados com letra maiúscula.
8. **Abstract em Língua Estrangeira (Obrigatório):**
   - Versão fiel do resumo em inglês, acompanhado de **Keywords** separadas por ponto final.
9. **Listas Específicas (Opcionais / Condicionadas):**
   - Lista de Ilustrações / Figuras.
   - Lista de Quadros.
   - Lista de Tabelas.
   - Lista de Abreviaturas e Siglas.
10. **Sumário (Obrigatório — ABNT NBR 6027):**
    - Enumeração exata das divisões, seções e subseções na mesma grafia e numeração.

---

### 2.2 Elementos Textuais
* **1. INTRODUÇÃO**
  * *1.1 Justificativa:* Relevância humana, social e teórica do tema.
  * *1.2 Objetivo Geral:* Meta global interligada diretamente ao problema de pesquisa.
  * *1.3 Objetivos Específicos:* Passos instrumentais e operacionais para atingir o objetivo geral.
* **2. FUNDAMENTAÇÃO TEÓRICA**
  * Revisão da literatura doutrinária e jurisprudencial.
  * *Citações Indiretas:* Autor e ano integrados (`\citeonline{...}` ou `\cite{...}`).
  * *Citações Diretas Curtas (até 3 linhas):* Inseridas no próprio corpo do parágrafo, entre aspas duplas.
  * *Citações Diretas Longas (mais de 3 linhas):* Em bloco destacado com recuo de **4,0 cm da margem esquerda**, fonte Arial 10, espaçamento simples, sem aspas (`\begin{citacao} ... \end{citacao}`).
* **3. DESENVOLVIMENTO**
  * *3.1 Caracterização do Objeto de Estudo:* Delimitação do fenômeno ou conjunto normativo.
  * *3.2 Metodologia da Pesquisa:* Classificação quanto aos objetivos (exploratória, descritiva, explicativa) e procedimentos de coleta (bibliográfica, documental, estudo de caso, etc.).
  * *3.3 Procedimentos Metodológicos:* Modo operacional detalhado (amostragem, coleta e tratamento de dados).
  * *3.4 Discussão sobre o Objeto da Pesquisa:* Análise crítica fundamentada confrontando teses, divergências e implicações práticas.
* **4. CONCLUSÃO**
  * Síntese das respostas obtidas para o problema delimitado, cumprimento dos objetivos, confrontação com o referencial teórico e proposição de pesquisas futuras.

---

### 2.3 Elementos Pós-Textuais
* **REFERÊNCIAS (Obrigatório — ABNT NBR 6023):**
  * Alinhadas estritamente à **margem esquerda** (sem recuo de parágrafo).
  * Espaçamento entrelinhas **simples (1,0)**.
  * Separadas entre si por **um espaço simples em branco** (ou espaço duplo).
  * Ordenadas em **rigorosa ordem alfabética**.
* **Apêndices (Opcional):** Textos ou instrumentos elaborados pelo próprio autor.
* **Anexos (Opcional):** Documentos, legislações ou textos de terceiros não elaborados pelo autor.

---

## 🚀 Arquivos de Template no Sistema

* **Arquivo LaTeX Principal:** [`.agents/skills/latex/templates_abnt/modelo_tcc_artigo_direito_univassouras.tex`](file:///run/media/liveuser/1e81fc6b-9460-4560-9706-a416cb37dbfe/@home/eduardo/Arquivos/Agentes/aph_bioshield/.agents/skills/latex/templates_abnt/modelo_tcc_artigo_direito_univassouras.tex)
* **Arquivo BibTeX Base:** [`.agents/skills/latex/templates_abnt/referencias.bib`](file:///run/media/liveuser/1e81fc6b-9460-4560-9706-a416cb37dbfe/@home/eduardo/Arquivos/Agentes/aph_bioshield/.agents/skills/latex/templates_abnt/referencias.bib)
* **Arquivo DOCX Original:** [`.agents/skills/latex/templates_abnt/MODELO DE TCC DIREITO UNIVASSOURAS MARICÁ.docx`](file:///run/media/liveuser/1e81fc6b-9460-4560-9706-a416cb37dbfe/@home/eduardo/Arquivos/Agentes/aph_bioshield/.agents/skills/latex/templates_abnt/MODELO%20DE%20TCC%20DIREITO%20UNIVASSOURAS%20MARIC%C3%81.docx)
