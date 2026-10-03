---
trigger: model_decision
description: "Ative quando o operador pedir para criar uma rule, skill ou workflow, ou quando o agente identificar um padrão repetitivo que merece ser capturado como automação. NÃO carregue em conversas comuns."
---

# Guia Oficial Antigravity — Rules, Skills & Workflows

> Fonte: documentação interna do Google Antigravity (extraída do system prompt oficial do agente).

---

## 1. RULES (Regras)

Rules são constraints definidas manualmente para guiar o comportamento do agente. Elas existem em dois níveis:

### Onde ficam
| Escopo | Localização |
|--------|------------|
| **Global** | `~/.gemini/GEMINI.md` — aplicada em todos os workspaces |
| **Workspace** | `.agents/rules/<nome>.md` dentro do projeto (suporta também `.agent/rules/`) |

### Frontmatter disponível
```yaml
---
trigger: always_on | manual | model_decision | glob
glob: "**/*.ts"          # só usado quando trigger = glob
description: "Texto que explica quando a regra deve ser ativada (usado para model_decision)"
---
```

### Modos de ativação (`trigger`)
| Modo | Comportamento |
|------|--------------|
| `manual` | Ativada apenas via `@nome-da-regra` no chat |
| `always_on` | Sempre aplicada em todas as conversas |
| `model_decision` | O modelo decide se aplica baseado na `description` |
| `glob` | Aplicada automaticamente em arquivos que casam com o padrão `glob` |

### Referenciando outros arquivos dentro de uma Rule
Use `@[caminho/do/arquivo.md]` para incluir conteúdo de outros arquivos dentro da rule.
- Caminhos relativos: resolvidos a partir da localização do arquivo de regra.
- Caminhos absolutos: resolvidos como caminho absoluto real.

### Boas práticas
- Escreva uma `description` clara quando usar `model_decision` — ela é o critério de ativação.
- Use `glob` para regras de estilo de código atreladas a tipos específicos de arquivo.
- Mantenha cada regra focada em um único domínio.
- Limite: **12.000 caracteres** por arquivo de regra.

---

## 2. SKILLS (Habilidades)

Skills são pacotes reutilizáveis de conhecimento especializado que estendem as capacidades do agente para tarefas específicas.

### Onde ficam
| Escopo | Localização |
|--------|------------|
| **Workspace** | `.agents/skills/<pasta-da-skill>/` |
| **Global** | `~/.gemini/config/skills/<pasta-da-skill>/` (ou `~/.gemini/antigravity/skills/`) |
| **Local Central** | `.agents/skills/<pasta-da-skill>/` |

O agente também suporta `.agent/skills/` por compatibilidade retroativa.

### Estrutura obrigatória
```
.agents/skills/
└── minha-skill/
    └── SKILL.md          ← OBRIGATÓRIO (com cláusula de Auto-Commit Git)
    ├── scripts/          ← scripts auxiliares (opcional)
    ├── examples/         ← implementações de referência (opcional)
    └── resources/        ← templates e assets (opcional)
```

### Frontmatter do SKILL.md
```yaml
---
name: nome-da-skill          # opcional (padrão: nome da pasta)
description: >               # OBRIGATÓRIO — critério de ativação pelo agente
  Gera testes unitários para Python usando pytest.
  Use quando precisar testar funções isoladas.
---
```

### Corpo do SKILL.md
O corpo é markdown livre com instruções detalhadas:
- Quando usar a skill
- Como usá-la (passo a passo)
- Convenções e padrões a seguir
- Referências a scripts ou exemplos na pasta
- **Cláusula de Versionamento Git Automático (MANDATÓRIA)**

---

## 3. WORKFLOWS (Fluxos de Trabalho)

Workflows definem uma sequência de passos para guiar o agente através de tarefas repetitivas (ex: deploy, revisão de PR, geração de relatório).

### Onde ficam
| Escopo | Localização |
|--------|------------|
| **Workspace** | `.agents/workflows/<nome>.md` |
| **Global** | `~/.gemini/antigravity/workflows/<nome>.md` |

O agente também suporta `_agents/workflows/` e `.agent/workflows/` por retrocompatibilidade.

### Formato do arquivo
```yaml
---
description: Como fazer o deploy da aplicação
---
```

### Annotations de auto-execução
| Annotation | Comportamento |
|------------|--------------|
| `// turbo` | Coloca acima de um step: auto-executa **apenas esse** step (`SafeToAutoRun = true`) |
| `// turbo-all` | Coloca em qualquer lugar do workflow: auto-executa **todos** os steps |

---

## 4. PROTOCOLO DE CAPTURA — Transformar em Skill, Rule ou Workflow

> **REGRA OBRIGATÓRIA:** O agente DEVE monitorar ativamente todos os padrões que surgem nas conversas e propor ao usuário a captura deles antes de qualquer ação.

### Gatilhos de Captura
| Sinal | Tipo sugerido |
|-------|--------------|
| Instrução que o usuário repete em várias conversas | **Rule** (`always_on`) |
| Preferência de estilo, tom ou formato recorrente | **Rule** (`always_on` ou `model_decision`) |
| Sequência de passos executada mais de uma vez | **Workflow** |
| Conhecimento especializado que pode ser reutilizado em outros projetos | **Skill** |
| Padrão de erro que o agente comete e o usuário corrige | **Rule** (para evitar reincidência) |
| Conjunto de comandos repetitivos no terminal | **Workflow** (com `// turbo`) |
| Contexto técnico de uma lib/ferramenta explicado pelo usuário | **Skill** |

---

## 5. PROTOCOLO OBRIGATÓRIO DE VERSIONAMENTO (GIT AUTOMATION)

> 🚨 **REGRA DE BLINDAGEM DE CÓDIGO, SKILLS & RULES:**
>
> ### 5.1 Injeção Obrigatória de Auto-Commit ao Editar Skills (PRÉ-REQUISITO MANDATÓRIO)
> Sempre que qualquer agente for **criar, modificar, enriquecer ou refatorar uma Skill**:
> 1. O agente **DEVE verificar se o `SKILL.md` dessa skill já possui a cláusula/passo de Versionamento Git Automático**.
> 2. **Se NÃO possuir, o agente é TERMINANTEMENTE OBRIGADO a inserir o bloco de auto-commit no `SKILL.md` ANTES de realizar a modificação desejada.**
>
> 📝 **Bloco Padrão a ser inserido no `SKILL.md`:**
> ```markdown
> ### 🔒 Versionamento Git Automático (MANDATÓRIO)
> Sempre que esta skill for executada, auto-fichada, gerar dados ou tiver seus arquivos/scripts alterados, execute obrigatoriamente o commit semântico no repositório correspondente no mesmo turno:
> ```bash
> git add . && git commit -m "tipo(nome-da-skill): descrição concisa da alteração"
> ```
> ```
>
> ### 5.2 Execução do Commit Atômico Pós-Modificação
> Sempre que qualquer alteração for realizada em:
> - **Skills:** Arquivos `SKILL.md`, `scripts/`, `resources/` em `.agents/skills/` ou `~/.gemini/config/skills/`;
> - **Rules & Workflows:** Arquivos `.agents/rules/*.md` ou `.agents/workflows/*.md`;
> - **Consolidação de Módulos:** Promoção de especificações finais para `3_fim/*.md`;
>
> **O AGENTE DEVE EXECUTAR O COMMIT ATÔMICO NO MESMO TURNO:**
> ```bash
> git add <arquivos-modificados>
> git commit -m "tipo(escopo): descrição concisa do que foi alterado"
> ```
>
> 📌 **Convenção Semântica de Commits:**
> - `feat(skill/<nome>):` Nova habilidade, script ou instrução adicionada.
> - `fix(skill/<nome>):` Correção de bugs em scripts ou calibração de prompt da skill.
> - `feat(rule/<nome>):` Nova regra de governança ou cognição implementada.
> - `fix(rule/<nome>):` Ajuste de trigger, rota ou ordem de operações na regra.
> - `docs(modulo/<nome>):` Consolidação de módulo no 3_fim ou diário de bordo.
> - `checkpoint(memoria):` Registro consolidado de memórias e consciência.

---

## Resumo de Localização

```
.agents/
├── rules/
│   ├── minha-regra.md       ← Rule de workspace
│   └── outra-regra.md
├── skills/
│   └── minha-skill/
│       └── SKILL.md         ← Skill de workspace (com auto-commit)
└── workflows/
    └── meu-workflow.md      ← Workflow de workspace

~/.gemini/
├── GEMINI.md                ← Rule global
└── config/skills/           ← Skills globais ativas

.agents/skills/  ← Acervo central de skills
```
