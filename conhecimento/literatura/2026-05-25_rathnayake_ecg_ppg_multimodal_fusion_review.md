---
tipo: literatura
area: engenharia_biomedica
tags:
  - literatura
  - paper
  - fusao_multimodal
  - ecg_ppg
  - hardware
  - cancelamento_ruido
  - dsp
autores: ["Rathnayake Chamod", "Chen Wenjing", "Jayawickrama Sahan", "Lai Dakun"]
fonte: "Sensors (Basel), 26(11):3477"
ano: 2026
data: 2026-10-03
status: fichado
doi: "10.3390/s26113477"
conceitos_relacionados:
  - "[[c_pan_tompkins_ecg]]"
  - "[[c_pulse_arrival_time_pat]]"
  - "[[c_respiracao_derivada_ppg]]"
moc: "[[moc_aph_bioshield]]"
---

# 📑 Fichamento: Physiological Monitoring Applications of Wearable Multimodal Fusion Systems Based on ECG and PPG: A Comprehensive Review

## 📌 Metadados da Fonte
- **Título Original:** Physiological Monitoring Applications of Wearable Multimodal Fusion Systems Based on ECG and PPG: A Comprehensive Review
- **Autores:** Chamod Rathnayake, Wenjing Chen, Sahan Jayawickrama, Dakun Lai (School of Information and Communication Engineering)
- **Publicação:** *Sensors (Basel)*, Maio de 2026.
- **Identificadores:** DOI: 10.3390/s26113477 | PMCID: PMC13259056 | PMID: 42280994
- **Arquivo Local Bruto:** `artigos/pmc13259056_ecg_ppg_multimodal_fusion_review.xml`

---

## 🎯 Tese Central
A integração síncrona de **Eletrocardiografia (ECG)** e **Fotopletismografia (PPG)** no mesmo dispositivo vestível desbloqueia capacidades diagnósticas que nenhum sensor consegue fornecer isoladamente: estimativa contínua de rigidez vascular e pressão arterial por atraso de pulso (PAT/PTT), cancelamento cruzado de artefatos de movimento (usando o pico R elétrico para calibrar a janela de aceitação óptica) e extração de arritmias com redundância de sinal. A fusão em nível de sinal e em nível de características é a chave para a estabilidade em ambientes dinâmicos.

---

## 🔬 Metodologia & Topologias de Hardware em Destaque
* **Topologias de Circuito Integrado:**
  * Uso de front-ends analógicos (AFEs) com canais mistos biopotenciais e ópticos (como AD8232/MAX30001 e MAX30102/MAX86150).
  * Gestão de terra compartilhado (GND) analógico e digital para evitar acoplamento de ruído do chaveamento de LEDs de alta corrente nos amplificadores de instrumentação de ECG de alto ganho.
* **Técnicas de Fusão Algorítmica:**
  1. *Signal-Level Fusion:* Correlação cruzada temporal para cálculo do PAT amostra a amostra.
  2. *Feature-Level Fusion:* Cruzamento da Variabilidade da Frequência Cardíaca (HRV derivada do ECG) com a Variabilidade da Amplitude de Pulso (PPA derivada do PPG) para avaliação do tônus autonômico simpático/parassimpático.
  3. *Decision-Level Fusion:* Se o ECG apresentar ruído muscular intenso, a taxa cardíaca é sustentada temporariamente pelo sinal óptico (e vice-versa).

---

## 🚑 Aplicação Direta no APH-BioShield™ & Impacto para Artigo Científico
1. **Solução do Problema de Ruído da Ambulância:** O paper detalha exatamente como evitar que a trepidação da viatura destrua a leitura: quando o acelerômetro detecta vibração mecânica, o firmware ativa a janela de concordância ECG-PPG — apenas os picos ópticos que chegam dentro do intervalo fisiológico esperado após o pico R (tipicamente entre $150\text{ ms}$ e $350\text{ ms}$) são considerados batimentos válidos.
2. **Citação Estratégica:** Serve como referência principal para embasar a seção de *Signal Processing & Multi-Sensor Fusion Architecture* do futuro artigo acadêmico.

---

## 🔗 Conexões no Grafo
* **Conceitos Alimentados:** [[c_pan_tompkins_ecg]], [[c_pulse_arrival_time_pat]], [[c_respiracao_derivada_ppg]]
* **MOC Central:** [[moc_aph_bioshield]]
