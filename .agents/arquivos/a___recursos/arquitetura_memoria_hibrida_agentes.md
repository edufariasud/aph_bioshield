# 🏛️ Recurso Transversal: Arquitetura de Memória Híbrida para Agentes

**Versão:** 1.0  
**Data:** 2026-09-24  
**Status:** Aprovado e Homologado na Arquitetura Base  
**Escopo:** Template Base (`modelo`) e todos os agentes derivados.

---

## 1. O Problema Resolvido
Agentes com memória puramente plana em texto perdem o fio da meada em interações longas. Agentes com memória puramente em JSON sofrem para armazenar literatura técnica densa, artigos, livros e códigos.

A **Memória Híbrida** resolve isso dividindo a cognição do agente em **dois copos independentes**:
1. **Copo 1: Memória Operacional & Relacional (`.memoria/`)**
2. **Copo 2: Memória de Conhecimento Prático (`./conhecimento/` no formato Obsidian)**

---

## 2. A Tabela Comparativa de Decisão Operacional

| Dimensão | Copo 1: Memória Operacional & Relacional | Copo 2: Memória de Conhecimento Prático (Obsidian) |
| :--- | :--- | :--- |
| **O que armazena** | Acordos práticos, decisões de projeto, status de projetos e alinhamentos entre agentes. | Conhecimentos práticos, artigos científicos, livros dissecados, transcrições/legendas do YouTube, threads técnicas e modelos mentais. |
| **Tecnologia & Formato** | JSON estruturado em 3 Camadas (`identidade.json` -> `consciencia/` -> `memorias/M_XXX.json`). | Markdown com YAML Frontmatter (Properties), links bidirecionais (`[[...]]`), tags e MOCs. |
| **Skill Associada** | Protocolo Cognitivo Nativo (`cognicao.md`). | **`obsidian-markdown`** (`.agents/skills/obsidian-markdown/SKILL.md`). |
| **Diretório Padrão** | `./.agents/arquivos/.memoria/` | `./conhecimento/` |
| **Lógica de Conexão** | Temporal e contextual (prioridades 1-10, notas objetivas). | Causal e em rede (grafo conceitual, multi-hop reasoning). |
| **Integração Humana** | Blindada por isolamento estrito de contexto. | Abrível como Vault diretamente no Obsidian. |

---

## 3. Estrutura Padrão do Copo de Conhecimento (Obsidian)

```text
conhecimento/
├── 00_HUB_CENTRAL.md             <-- MOC Mestre de entrada
├── mocs/                         <-- Mapas de Conteúdo por grande área temática
│   └── moc_geral.md
├── conceitos/                    <-- Nível 2: Notas Permanentes / Síntese consolidada
│   └── README.md
├── literatura/                   <-- Nível 3: Fichamentos atômicos de fontes brutas
│   └── README.md
└── templates/                    <-- Modelos de criação de notas
    ├── template_conceito.md
    └── template_literatura.md
```
