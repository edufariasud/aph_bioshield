# Diário de Bordo — APH-BioShield™

---

## 📌 Contexto Imediato
* **Fase Atual:** Fase 1 (`1_inicio`) — Ideação Bruta, Estruturação da BOM de Bancada e Levantamento de Literatura Científica.
* **Operadora Ativa:** Eduarda (Diretrizes: proteção rigorosa de sono, contenção de over-engineering e respeito à maturidade progressiva das fases).
* **Objetivo Imediato:** Consolidar a documentação de viabilidade técnica da BOM com peças de prateleira (COTS), definir as escolhas arquiteturais fundamentais através das 6 perguntas estratégicas e preparar o ambiente de estudos de DSP no cofre Obsidian.

---

## 📝 Log de Atividades Concluídas

### Sessão 01 — 2026-10-03
1. **Estruturação do Agente Dedicado:** Inicializado o agente e repositório `aph_bioshield` a partir do template mestre `modelo`, com suporte nativo à memória híbrida (Copo 1: `.memoria/`, Copo 2: Cofre Obsidian em `./conhecimento/` com a skill `obsidian-markdown`).
2. **Registro da BOM de Bancada:** Catalogada a lista de materiais real de baixo custo com microcontrolador Seeed XIAO BLE nRF52840, sensores MAX30102, AD8232, MLX90614, módulo LoRa SX1262, display OLED SSD1306 e anel de LEDs WS2812B.
3. **Auditoria Técnica de Viabilidade:** Mapeados os 5 riscos de bancada:
   - Limitação do PAT para aferição contínua de pressão arterial sem manguito no choque hemorrágico;
   - Desafio do ECG com eletrodos secos em vetor curto no esterno;
   - Balanço energético da bateria LiPo 250mAh perante a carga de LEDs e LoRa;
   - Limite físico de pinos GPIO no XIAO BLE;
   - Adaptação mecânica entre módulos de bancada vs patch fino.
4. **Plano de Estudos Científicos:** Estruturado o roadmap de 6 eixos de literatura médica e biomédica para compensar limitações de hardware com algoritmos de DSP.
5. **Coleta de Artigos Científicos:** Criada a pasta dedicada `artigos/` e baixados 5 artigos de alto impacto (2026) via PubMed/PMC e arXiv cobrindo:
   - SpO2 em tempo real por PPG de reflexão esternal (*Sensors*, 2026);
   - Índice de Perfusão no choque traumático/hemorrágico (*Cureus*, 2026);
   - Morfologia de onda PPG para estratificação de risco no choque (*AICOJ*, 2026);
   - Validação de eletrodos secos em ECG vestível (*Sensors*, 2026);
   - Condições mecânicas e pressão de contato em PPG de reflexão (*J Med Syst*, 2026).
6. **Absorção no Cofre Obsidian (Copo 2):** Gerados os 5 fichamentos de literatura completos em `conhecimento/literatura/` com metadados YAML, extração das fórmulas matemáticas e lições práticas diretas para o firmware e chassi do APH-BioShield, interligados ao `moc_aph_bioshield.md`.
7. **Expansão do Estado da Arte (Hardware COTS & Impacto em APH):** Coletados e fichados mais 6 artigos de ponta (2025-2026), totalizando 11 artigos no acervo:
   - *Filgueiras et al. (Micromachines, 2025):* Validação metrológica da nossa exata pilha de hardware (nRF52840 + MAX30102 + temperatura);
   - *Alkhoury et al. (HardwareX, 2026):* Guia de engenharia aberta para nós biomédicos vestíveis ultrafinos (placa de 4 camadas 18x22mm);
   - *Markel et al. (West J Emerg Med, 2026):* Benchmarks mundiais de monitorização sem fio em APH e configurações de recursos limitados;
   - *Gonzalez et al. (Sensors, 2026):* Validação do índice de reserva compensatória (CRI) no choque hemorrágico com PPG vestível;
   - *Rathnayake et al. (Sensors, 2026):* Fusão multimodal ECG+PPG para supressão de ruídos de ambulância;
   - *Rrmoku (Cureus, 2025):* Impacto clínico de vestíveis na redução de atraso e sobrecarga de triagem em emergência.
8. **Integração do Pacote de Laboratório (Fase 2 - `2_meio`):** Importado e descompactado o pacote `dispositivo_movel_aph.zip` da estação de downloads local diretamente em `2_meio/`:
   - *Dossiê Técnico Completo:* `DOSSIE_TECNICO_APH.md` com arquitetura em 8 camadas (base hidrocoloide, eletrodos secos 316L, barreira óptica, termopilha, bateria LiPo 280mAh, PCB rígido-flexível nRF5340/nRF52840, policarbonato IP67, halo START);
   - *Modelagem e Renders Industriais:* `assets/aph_device_render.jpg` e `assets/aph_exploded_view.jpg`;
   - *Simulador de Telemetria 3D Interativo:* Aplicação Web Three.js completa (`index.html`, `app.js`, `style.css`, `libs/`).
9. **Aquisição e Absorção de Livros Fundamentais (Tratados de Referência):**
   - Baixados 4 livros de referência mundial no tema para a pasta `livros/` utilizando o buscador acadêmico local (`libgen_scraper.py`), com prioridade a EPUB para fragmentação e RAG:
     * *Wearable Sensors: Fundamentals, Implementation and Applications* — Edward Sazonov & Michael R. Neuman (Elsevier, EPUB - 16.6 MB);
     * *Photoplethysmography: Technology, Signal Analysis and Applications* — Panicos A. Kyriacou & John Allen (Elsevier, 2021, PDF - 59.1 MB);
     * *Medical Instrumentation: Application and Design* — John G. Webster & Amit J. Nimunkar (Wiley, 5ª Ed. 2021, EPUB - 14.5 MB);
     * *Biomedical Signal Analysis* — Rangaraj M. Rangayyan & Sridhar Krishnan (IEEE/Wiley, 3ª Ed. 2024, PDF - 40.4 MB).
   - Gerados os 4 fichamentos completos em `conhecimento/literatura/`, integrados ao `moc_aph_bioshield.md` no cofre Obsidian.
10. **Alinhamento Cognitivo da Nova Operadora (Eduarda):**
    - Formalizada a transição cognitiva para Eduarda através da memória episódica `M002.json` e criação da ficha `consciencia/p_eduarda.json`.
    - Calibrados os três compromissos inegociáveis: proteção rigorosa das horas de sono, freio anti-afobação (respeito às etapas 1_inicio -> 2_meio -> 3_fim) e bloqueio ativo de over-engineering.
11. **Consolidação do Modelo Canônico Absoluto de TCC/Artigos na Skill LaTeX:**
    - Incorporado o modelo oficial `MODELO DE TCC DIREITO UNIVASSOURAS MARICÁ.docx` na skill `latex` (`templates_abnt/` e `assets/templates/`).
    - Desenvolvido o template completo em LaTeX `modelo_tcc_artigo_direito_univassouras.tex` (Arial 12, margens 3/2cm, banca de 3 membros, epígrafe 8cm, resumo ABNT 6028, citações 4cm e referências ABNT NBR 6023).
    - Criados a base BibTeX `referencias.bib` e o manual `modelo_canonico_tcc_artigo_abnt.md`.
    - Injetadas cláusulas de versionamento git no `SKILL.md` e estabelecido como o modelo padrão absoluto na ausência de especificação do usuário. Realizado commit semântico.

---

## 🎯 Próximos Passos (To-Do)
- [ ] Definir as respostas das 6 decisões estratégicas de arquitetura (form factor, requisitos de PA, descartável vs reutilizável, etc.).
- [ ] Elaborar o esquemático elétrico detalhado de interligação no KiCad/Fritzing com gerenciamento de pinos do XIAO BLE.
- [ ] Desenvolver o algoritmo base em Python para processamento de sinal em dados simulados (filtro Pan-Tompkins para ECG e extração de PI/FR no PPG com cancelamento de ruído).
