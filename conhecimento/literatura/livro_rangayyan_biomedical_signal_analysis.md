---
tipo: literatura
area: engenharia_biomedica
tags:
  - literatura
  - livro
  - processamento_sinais
  - filtros_digitais
  - pan_tompkins
  - remocao_ruido
  - qrs_detection
autores: ["Rangaraj M. Rangayyan", "Sridhar Krishnan"]
fonte: "Biomedical Signal Analysis (3rd Edition, IEEE Press Series on Biomedical Engineering / John Wiley & Sons, 2024)"
ano: 2024
data: 2026-10-03
status: fichado
conceitos_relacionados:
  - "[[c_filtros_biomedicos_embarcados]]"
  - "[[c_pulse_arrival_time_pat]]"
moc: "[[moc_aph_bioshield]]"
---

# 📑 Fichamento: Biomedical Signal Analysis (3ª Edição, 2024)

## 📌 Metadados da Fonte
- **Título Original:** Biomedical Signal Analysis
- **Autores:** Rangaraj M. Rangayyan, Sridhar Krishnan
- **Publicação:** IEEE Press / John Wiley & Sons (3ª Edição, 2024). ISBN: 978-1-119-82585-2
- **Formato Local:** `livros/Rangaraj M. Rangayyan, Sridhar Krishnan - Biomedical Signal Analysis (IEEE Press Series on Biomedical Engineering) (2024, Wiley-I.pdf` (40.42 MB)

---

## 🎯 Tese Central
A mais recente edição (2024) do tratado fundamental sobre processamento digital de sinais fisiológicos. Sistematiza os modelos estocásticos e determinísticos para tratamento de ruído biológico, filtragem ótima (FIR/IIR, filtros adaptativos LMS/RLS para cancelamento de interferência), algoritmos de detecção morfológica (QRS de Pan-Tompkins, picos sistólicos e incisuras dicróticas) e fusão multissensorial para diagnóstico em tempo real com baixa complexidade computacional.

---

## 🔬 Fundamentos Técnicos Críticos para o APH-BioShield™

### 1. Fontes de Contaminação e Ruído em Sinais Biológicos
* **Wander de Linha de Base (Baseline Drift):** Oscilações lentas de $0.05\text{--}0.5\text{ Hz}$ decorrentes da respiração do paciente e variações na interface eletrodo-pele.
* **Interferência de Rede Elétrica (Power-Line Interference):** Ruído em $50\text{ Hz}$ ou $60\text{ Hz}$ com harmônicos. Rangayyan demonstra que filtros notch convencionais de alta ordem distorcem a amplitude do complexo QRS e recomenda o emprego de filtros notch IIR de banda estreita com pólos próximos ao círculo unitário ($r \approx 0.95\text{--}0.98$) ou filtros comb baseados em médias móveis.
* **Artefatos Mioelétricos (EMG):** Ruído de alta frequência ($20\text{--}500\text{ Hz}$) de contrações musculares do paciente em estresse ou choque, que masqueram ondas P e T.
* **Artefatos de Movimento (Motion Artifacts):** Deslocamentos mecânicos súbitos que afetam simultaneamente o acoplamento óptico do PPG e a impedância de contato do ECG.

### 2. Algoritmo Pan-Tompkins Otimizado para Microcontroladores (ARM Cortex-M4)
Para a detecção em tempo real do complexo QRS e marcação precisa do pico R (essencial para sincronização do PAT), Rangayyan detalha a esteira canônica de Pan-Tompkins:
1. **Filtro Passa-Faixa ($5\text{--}15\text{ Hz}$):** Atenua o drift de linha de base e ruídos mioelétricos/60 Hz, concentrando a energia típica do complexo QRS.
2. **Diferenciação ($y(n) = \frac{1}{8}[2x(n) + x(n-1) - x(n-3) - 2x(n-4)]$):** Realça a alta declividade da rampa da onda R e suprime ondas P e T lentas.
3. **Elevamento ao Quadrado ($y(n) = [x(n)]^2$):** Garante valores positivos e amplifica não-linearmente componentes de maior magnitude.
4. **Integração por Janela Móvel (Moving-Window Integrator):** Janela temporal de aproximadamente $150\text{ ms}$ ($N = 15$ a $100\text{ Hz}$) que engloba a largura fisiológica total do QRS.
5. **Limiar Adaptativo Duplo (Dual Adaptive Thresholding):** Dois limiares concorrentes (um para sinal e outro para ruído) ajustados dinamicamente com base no histórico dos últimos 8 batimentos para evitar falsos positivos e ignorar batimentos ectópicos isolados.

### 3. Filtragem Digital Adaptativa com Baixo Custo Computacional
* **Cancelamento Adaptativo de Ruído (ANC):** Utilização de um canal secundário de aceleração (IMU de 3 eixos) como sinal de referência de ruído de movimento. O algoritmo LMS (*Least Mean Squares*) calcula os pesos do filtro com apenas multiplicações simples por amostra, perfeitamente viável em microcontroladores com unidade de ponto flutuante (FPU) como o Cortex-M4F do nRF52840.

---

## 🚑 Aplicações Práticas no Firmware do APH-BioShield™
1. **Implementação Pan-Tompkins com Operações Inteiras/Ponto Fixo:** O pipeline do Pan-Tompkins pode rodar em C/C++ consumindo menos de $2\%$ da CPU do nRF52840 a $100\text{ Hz}$.
2. **Cálculo de PAT com Marcadores Sincronizados:** O instante do pico R fornecido pelo Pan-Tompkins no canal de ECG aciona um temporizador de microsegundos no hardware para capturar o atraso do pé sistólico no PPG óptico, fornecendo a métrica de PAT estável amostra a amostra.
3. **Média Móvel Exponencial (EMA):** Aplicação de filtros EMA nos valores finais de frequência cardíaca e saturação para suavizar a apresentação visual e evitar saltos bruscos na telemetria durante solavancos da ambulância.

---

## 🔗 Conexões no Grafo do Conhecimento
- **Conceitos Alimentados:**
  - [[c_filtros_biomedicos_embarcados]]
  - [[c_pulse_arrival_time_pat]]
- **MOC Central:** [[moc_aph_bioshield]]
