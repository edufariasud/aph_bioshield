---
name: obsidian-markdown
description: >
  Cria e edita notas no padrão Obsidian Flavored Markdown com cabeçalhos de metadados
  (YAML frontmatter / Properties), tags, categorias, links bidirecionais (wikilinks [[...]]),
  transclusões/embeds (![[...]]) e callouts visuais. Use sempre que criar notas para o cofre
  do Obsidian ou manipular arquivos de conhecimento multidisciplinar.
---

# Obsidian Markdown & Knowledge Vault Skill

Esta skill guia o agente na criação, edição e manutenção de notas de conhecimento no ecossistema do **Obsidian**, garantindo consistência estrutural, metadados ricos em YAML (Properties) e interconexão via grafo.

Baseada nas diretrizes oficiais de `kepano/obsidian-skills` (Steph Ango, CEO do Obsidian) e adaptada para a arquitetura de Memória Híbrida.

---

### 🔒 Versionamento Git Automático (MANDATÓRIO)
Sempre que esta skill for executada, auto-fichada, gerar dados ou tiver seus arquivos/scripts alterados, execute obrigatoriamente o commit semântico no repositório correspondente no mesmo turno:
```bash
git add . && git commit -m "feat(skill/obsidian-markdown): atualização nas diretrizes de notas e propriedades Obsidian"
```

---

## 1. O Cabeçalho Padrão de Metadados (YAML Frontmatter / Properties)

Toda nota criada no cofre Obsidian DEVE iniciar obrigatoriamente com o bloco YAML no topo. Isso habilita o painel de **Properties** do Obsidian, permitindo filtros pelo Dataview, buscas por tags e visualização por categorias.

```yaml
---
tipo: conceito # conceito | literatura | moc | diario
area: geral # ia_agentes | engenharia | engenharia_biomedica | saude
tags:
  - conceito
  - modelo_mental
status: consolidado # consolidado | rascunho | em_validacao
data: YYYY-MM-DD
aliases:
  - "Nome Alternativo"
fontes:
  - "[[AAAA-MM-DD_fonte]]"
relacionados:
  - "[[c_outro_conceito]]"
---
```

### Tipos de Propriedades Recomendadas:
| Propriedade | Tipo | Finalidade |
| :--- | :--- | :--- |
| `tipo` | Texto | `moc`, `conceito`, `literatura`, `resumo` |
| `area` | Texto | Grande domínio temático |
| `tags` | Lista | Palavras-chave para o grafo de tags |
| `status` | Texto | Grau de maturação da nota |
| `data` | Data | Data de criação ou estudo (`AAAA-MM-DD`) |
| `aliases` | Lista | Nomes alternativos pelos quais a nota pode ser linkada |
| `fontes` | Lista de Wikilinks | Links `[[...]]` para as notas de literatura de apoio |
| `relacionados` | Lista de Wikilinks | Links `[[...]]` para outros conceitos irmãos |

---

## 2. Links Bidirecionais (Wikilinks) & Ancoragem

Sempre utilize a sintaxe de wikilink para conectar notas internas do cofre:

```markdown
[[Nome da Nota]]                    # Link direto
[[Nome da Nota|Texto de Exibição]]  # Link com texto customizado
[[Nome da Nota#Título da Seção]]    # Link direto para um cabeçalho
[[Nome da Nota#^bloco-id]]          # Link para um parágrafo/bloco específico
```

### Criando âncoras de bloco:
Adicione `^id-do-bloco` no final de qualquer parágrafo para que outras notas possam citá-lo cirurgicamente:
```markdown
O princípio central define a arquitetura base. ^principio-central-def
```

---

## 3. Transclusões & Embeds (`![[...]]`)

Para incorporar o conteúdo de outra nota, imagem ou trecho sem duplicar o texto, utilize a exclamação `!`:

```markdown
![[c_conceito]]                     # Transclui a nota inteira dentro desta
![[c_conceito#Mecanismos]]          # Transclui apenas a seção Mecanismos
![[diagrama.png|400]]               # Renderiza a imagem com largura de 400px
![[artigo.pdf#page=3]]              # Incorpora a página 3 do PDF
```

---

## 4. Callouts Visuais (Destaques no Obsidian)

O Obsidian renderiza caixas visuais estilizadas usando a sintaxe `> [!tipo]`:

```markdown
> [!note]
> Nota padrão ou contexto adicional.

> [!tip] Dica Prática
> Estratégia acionável para aplicação imediata.

> [!important]
> Informação crítica que não pode ser ignorada.

> [!warning]
> Ponto de atenção ou risco técnico.

> [!faq]- Detalhes Expansíveis (Recolhido por padrão)
> Use o sinal de menos (-) para começar fechado ou mais (+) para aberto.
```

---

## 5. Estrutura do Cofre de Segundo Cérebro

Para manter qualquer cofre limpo e navegável por humanos e agentes:

```text
conhecimento/
├── 00_HUB_CENTRAL.md        # MOC Mestre (Índice de entrada)
├── mocs/                    # Mapas de Conteúdo por disciplina
├── conceitos/               # Nível 2: Notas permanentes / Sínteses
├── literatura/              # Nível 3: Fichamentos atômicos de livros/artigos
└── templates/               # Modelos pré-configurados
```
