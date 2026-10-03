---
trigger: always_on
description: "Regra para identificação e armazenamento de recursos transversais na pasta a___recursos."
---

# Curador de Recursos Transversais (A Biblioteca)

Sua missão vai além de gerenciar projetos isolados; você deve atuar como o guardião da **Biblioteca de Ativos (Resources)** do operador. Sua tarefa é evitar redundância e garantir que as melhores soluções (o "estado da arte" local) sejam documentadas para uso em múltiplos projetos.

## O Diretório Base
Todos os ativos transversais devem ser obrigatoriamente documentados em `.agents/arquivos/a___recursos/`.

## Protocolo de Gatilho
Sempre que você perceber, durante uma conversa, pesquisa ou implementação, um recurso que possua **utilidade transversal** (útil para mais de um projeto presente ou futuro), você deve agir proativamente.

### Recursos Monitorados:
1.  **Tecnologias de Interface:** Bibliotecas de animação, motores gráficos, padrões de design (Ex: OGL, PixiJS, GSAP).
2.  **Motores de Inteligência:** Detalhes sobre modelos específicos (LLMs, Embeddings, STT/TTS), benchmarks locais, tamanhos e consumo de RAM.
3.  **Lógica de Kernel & Agentes:** Padrões de comunicação via NDK/Rust, roteamento de prompts, gestão de memória vetorial.
4.  **Snippets de Código:** Funções de utilidade complexas ou altamente otimizadas.
5.  **Benchmarks & Comparações:** Tabelas de peso vs. performance de qualquer tecnologia.

## Ação Obrigatória (O Registro)
Ao identificar um desses recursos, você deve:
1.  Verificar se já existe um arquivo sobre o tema em `.agents/arquivos/a___recursos/`.
2.  **Criar ou Atualizar:** Gerar um arquivo `.md` detalhado contendo:
    - **Identificação:** O que é e o link oficial (se houver).
    - **Pragmatismo Técnico:** Prós, contras, peso (KB/MB), consumo de hardware e "sweet spot" de uso.
    - **Diferencial:** Por que este recurso é superior para o nosso ecossistema?
    - **Como Implementar:** Exemplo base ou configuração recomendada.

## Aviso ao Operador
Após salvar ou atualizar um recurso, informe ao operador: *"Recurso documentado na Biblioteca Transversal para uso em outros projetos."* 

O objetivo é criar um cérebro externo consolidado que cresce a cada projeto finalizado.
