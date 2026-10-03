---
tipo: literatura
area: engenharia_biomedica
tags:
  - literatura
  - paper
  - hardware
  - nrf52840
  - max30102
  - baixo_custo
  - acuracia_metrologica
  - bpt
autores: ["Filgueiras Tatiana Pereira", "Bertemes-Filho Pedro", "Noveletto Fabrício"]
fonte: "Micromachines, 16(7):791"
ano: 2025
data: 2026-10-03
status: fichado
doi: "10.3390/mi16070791"
conceitos_relacionados:
  - "[[c_indice_perfusao_choque]]"
  - "[[c_pulse_arrival_time_pat]]"
moc: "[[moc_aph_bioshield]]"
---

# 📑 Fichamento: Evaluating the Accuracy of Low-Cost Wearable Sensors for Healthcare Monitoring

## 📌 Metadados da Fonte
- **Título Original:** Evaluating the Accuracy of Low-Cost Wearable Sensors for Healthcare Monitoring
- **Autores:** Tatiana Pereira Filgueiras, Pedro Bertemes-Filho, Fabrício Noveletto (Universidade do Estado de Santa Catarina / UDESC, Brasil)
- **Publicação:** *Micromachines (MDPI)*, Julho de 2025.
- **Identificadores:** DOI: 10.3390/mi16070791 | PMCID: PMC12299930 | PMID: 40731700
- **Arquivo Local Bruto:** `artigos/pmc12299930_low_cost_wearable_sensors_accuracy.xml`

---

## 🎯 Tese Central
Sistemas vestíveis biomédicos construídos exclusivamente com **componentes comerciais de prateleira (COTS) de baixo custo** — especificamente o microcontrolador **nRF52840** e o sensor óptico **MAX30102** acoplado a termometria dérmica — conseguem atingir acurácia metrológica compatível com monitores clínicos hospitalares padrão-ouro para Frequência Cardíaca ($r = 0.98$), Saturação de Oxigênio ($SpO_2$, erro $< 2\%$) e Tendência de Pressão Arterial (BPT - *Blood Pressure Trend* via atraso de pulso), desde que submetidos a filtragem digital em tempo real e calibração por regressão linear robusta.

---

## 🔬 Metodologia & Evidências de Bancada
* **Arquitetura de Hardware Avaliada:**
  * MCU: Nordic Semiconductor **nRF52840** (ARM Cortex-M4F @ 64 MHz com BLE 5.0).
  * Óptica: Módulo **MAX30102** operando a $100\text{ Hz}$ com amostragem de LEDs Red ($660\text{ nm}$) e IR ($880\text{ nm}$).
  * Temperatura: Sensor térmico digital de contato NTC/I2C.
* **Validação Metrológica:**
  * Comparação direta contra o monitor multiparamétrico hospitalar de referência Philips IntelliVue e oxímetro de bancada calibrado.
  * *Resultados de FC:* Erro médio absoluto (MAE) de apenas $1.12\text{ bpm}$ em repouso e $2.45\text{ bpm}$ sob movimentação moderada.
  * *Resultados de $SpO_2$:* Raiz do erro quadrático médio ($A_{rms}$) de $1.87\%$ no intervalo clínico de $90\%$ a $100\%$.
  * *Pressão Arterial por Tendência (BPT):* O sistema demonstrou alta sensibilidade ($r = 0.84$) para detectar oscilações dinâmicas de pressão sistólica induzidas por manobra de esforço isométrico, validando o uso de sensores ópticos para alertar alterações hemodinâmicas sem insuflação de manguito.

---

## 🚑 Aplicação Direta no APH-BioShield™ & Impacto para Artigo Científico
1. **Validação da Lista de Peças (BOM):** É a prova científica definitiva de que a escolha da nossa BOM (XIAO nRF52840 + MAX30102) tem lastro acadêmico internacional e acurácia metrológica comprovada em bancada.
2. **Citação Estratégica em Artigo:** Este paper deve ser citado como benchmark direto na seção de *Metodologia / Hardware Architecture*: demonstra que nossa proposta de baixo custo não é um brinquedo maker, mas uma plataforma biomédica válida com custo de fabricação $< \text{R\$} 150$.
3. **Firmware de Amostragem:** O artigo recomenda operar o MAX30102 com largura de pulso de $411\text{ }\mu\text{s}$ e corrente de LED de $7.6\text{ mA}$ para maximizar a relação sinal-ruído (SNR) sem esgotar prematuramente a bateria LiPo.

---

## 🔗 Conexões no Grafo
* **Conceitos Alimentados:** [[c_indice_perfusao_choque]], [[c_pulse_arrival_time_pat]]
* **MOC Central:** [[moc_aph_bioshield]]
