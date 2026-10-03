---
tipo: literatura
area: engenharia_biomedica
tags:
  - literatura
  - paper
  - ecg
  - eletrodos_secos
  - biopotencial
  - dsp
  - pan_tompkins
autores: ["Schmidt et al.", "Weber et al."]
fonte: "Sensors / Biomedical Engineering Journal, Setembro de 2026"
ano: 2026
data: 2026-10-03
status: fichado
doi: "10.3390/s26175510"
conceitos_relacionados:
  - "[[c_pan_tompkins_ecg]]"
  - "[[c_pulse_arrival_time_pat]]"
moc: "[[moc_aph_bioshield]]"
---

# 📑 Fichamento: Interval-Level Validation of a Wearable Dry-Electrode ECG Biosensor Platform: A Proof-of-Concept Study

## 📌 Metadados da Fonte
- **Título Original:** Interval-Level Validation of a Wearable Dry-Electrode ECG Biosensor Platform: A Proof-of-Concept Study
- **Publicação:** *Sensors (Basel)*, Setembro de 2026.
- **Identificadores:** DOI: 10.3390/s26175510 | PMCID: PMC13604097 | PMID: 42740150
- **Arquivo Local Bruto:** `artigos/pmc13604097_wearable_dry_electrode_ecg_platform.xml`

---

## 🎯 Tese Central
Sistemas vestíveis de eletrocardiografia baseados em **eletrodos secos (dry electrodes)** são indispensáveis para dispositivos compactos sem gel condutivo, mas enfrentam o desafio da alta impedância de interface pele-eletrodo ($> 500\text{ k}\Omega$). Este estudo demonstra que com uma geometria de contato adequada (botões condutivos em aço inoxidável cirúrgico ou polímeros condutores) e pré-filtragem analógica acoplada a um detector digital QRS robusto (estilo Pan-Tompkins), o erro nos intervalos RR atinge concordância superior a $99.2\%$ quando comparado ao sistema clínico de referência de 12 derivações com eletrodos de gel úmido.

---

## 🔬 Metodologia & Evidências Empíricas
* **Amostra:** Monitoramento contínuo em participantes em repouso e sob testes de esforço físico e movimentação torácica.
* **Hardware Avaliado:** Patch torácico com 2 eletrodos secos espaçados por $60\text{ mm}$ no esterno, conectado a um front-end analógico de alta impedância de entrada ($> 1\text{ G}\Omega$) e conversor ADC de 12 bits amostrado a $250\text{ Hz}$.
* **Tratamento de Sinal:**
  * Uso de filtro notch digital para 50/60 Hz e filtro passa-altas de corte abrupto em $0.67\text{ Hz}$ para remover oscilações da respiração.
  * O algoritmo de detecção QRS adaptativo manteve sensibilidade de $99.4\%$ e valor preditivo positivo de $99.1\%$ na identificação dos picos R.

---

## 🚑 Aplicação Prática no APH-BioShield™
1. **Validação do Uso de Botões Snap de Aço Cirúrgico 316L:** Confirma que o item 03 da nossa BOM (botões metálicos secos sem gel) é tecnicamente viável para captar ritmo e FC com acurácia médica, desde que a distância entre os polos no chassi do APH-BioShield seja de **pelo menos 50 a 60 mm**.
2. **Requisito de Fixação Mecânica:** O artigo destaca que o maior gerador de ruído em eletrodos secos não é a pele, mas o micro-escorregamento (*slippage* mecânico). A fita médica adesiva externa (Tegaderm) deve manter pressão uniforme de contato para que o sinal permaneça limpo durante a movimentação da maca.

---

## 🔗 Conexões no Grafo
* **Conceitos Alimentados:** [[c_pan_tompkins_ecg]], [[c_pulse_arrival_time_pat]]
* **MOC Central:** [[moc_aph_bioshield]]
