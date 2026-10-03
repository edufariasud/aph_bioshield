---
tipo: literatura
area: engenharia_biomedica
tags:
  - literatura
  - paper
  - ppg_morfologia
  - choque_hemorragico
  - estratificacao_risco
  - dsp
autores: ["Deng et al.", "Xiang et al.", "Cao et al."]
fonte: "Artificial Intelligence and Clinical Outcomes Journal (AICOJ), 2026"
ano: 2026
data: 2026-10-03
status: fichado
doi: "10.1016/j.aicoj.2026.100138"
conceitos_relacionados:
  - "[[c_indice_perfusao_choque]]"
  - "[[c_pulse_arrival_time_pat]]"
moc: "[[moc_aph_bioshield]]"
---

# 📑 Fichamento: Visual and Algorithmic Scoring of Photoplethysmography Morphology for Risk Stratification in Hemorrhagic Shock

## 📌 Metadados da Fonte
- **Título Original:** Visual scoring of photoplethysmography morphology for risk stratification in hemorrhagic shock: a prospective observational study
- **Publicação:** *AICOJ / Elsevier*, Agosto de 2026.
- **Identificadores:** DOI: 10.1016/j.aicoj.2026.100138 | PMCID: PMC13551925 | PMID: 42713335
- **Arquivo Local Bruto:** `artigos/pmc13551925_ppg_morphology_hemorrhagic_shock.xml`

---

## 🎯 Tese Central
A morfologia da curva pletismográfica (formato da onda de pulso) sofre alterações geométricas previsíveis e patológicas à medida que a volemia se esgota em pacientes com hemorragia aguda. O achatamento da onda dícrota, a diminuição da inclinação sistólica e o estreitamento da área pulsátil formam um padrão de colapso circulatório que supera a acurácia dos sinais vitais convencionais (FC isolada e PA com manguito) na predição de necessidade de UTI e mortalidade precoce.

---

## 🔬 Metodologia & Evidências Empíricas
* **Delineamento:** Estudo observacional prospectivo em centro de trauma nível 1 avaliando pacientes com sangramento ativo e choque hemorrágico.
* **Classificação Morfológica de Onda:**
  * *Grau 1 (Normal):* Pico sistólico nítido, entalhe dícroto bem definido e pico diastólico proeminente.
  * *Grau 2 (Perda Volêmica Moderada):* Entalhe dícroto desaparece; onda com declive suave e perda da reflexão diastólica.
  * *Grau 3 (Choque Grave / Colapso Vascular):* Onda de pulso senoidal com amplitude extremamente reduzida, sem pico acentuado e perda completa do tônus pulsátil.
* **Resultados:** A transição para Grau 3 teve uma área sob a curva ROC ($AUC = 0.91$) para predição de intervenção cirúrgica de controle de danos, superando o Índice de Choque convencional ($HR / SBP$).

---

## 🚑 Aplicação Prática no APH-BioShield™
1. **Algoritmo de Análise de Formato de Onda:** Em vez de apenas calcular o valor escalar numérico de $SpO_2$ ou FC, o algoritmo no nRF52840 deve extrair os pontos de inflexão da onda pletismográfica (derivada primeira e segunda do PPG - *Photoplethysmogram Acceleration / APPG*).
2. **Detecção de Desaparecimento da Onda Dícrota:** Quando a segunda derivada não detecta mais a onda reflexa dícrota, o APH-BioShield pode indicar "Alerta de Hipovolemia em Evolução" mesmo com pressão arterial ainda em valores toleráveis.

---

## 🔗 Conexões no Grafo
* **Conceitos Alimentados:** [[c_indice_perfusao_choque]], [[c_pulse_arrival_time_pat]]
* **MOC Central:** [[moc_aph_bioshield]]
