---
tipo: literatura
area: engenharia_biomedica
tags:
  - literatura
  - paper
  - hardware
  - open_hardware
  - circuito
  - pcb
  - microcontrolador
  - esp32
autores: ["Alkhoury Ludvik", "Moore Tony", "Swissler Petras", "Hill N. Jeremy"]
fonte: "HardwareX, 19:e00833, 2026"
ano: 2026
data: 2026-10-03
status: fichado
doi: "10.1016/j.ohx.2026.e00833"
conceitos_relacionados:
  - "[[c_pan_tompkins_ecg]]"
  - "[[c_indice_perfusao_choque]]"
moc: "[[moc_aph_bioshield]]"
---

# 📑 Fichamento: TinZr: A Compact Wireless Platform for Multi-Modal Physiological Sensor Integration and Data Acquisition

## 📌 Metadados da Fonte
- **Título Original:** TinZr: A compact wireless ESP32-C3 platform for multi-modal physiological sensor integration and data acquisition
- **Autores:** Ludvik Alkhoury, Tony Moore, Petras Swissler, N. Jeremy Hill (Wyss Center for Bio and Neuroengineering & Swiss Federal Laboratories)
- **Publicação:** *HardwareX / Elsevier*, Julho de 2026.
- **Identificadores:** DOI: 10.1016/j.ohx.2026.e00833 | PMCID: PMC13572519 | PMID: 42741027
- **Arquivo Local Bruto:** `artigos/pmc13572519_tinzr_compact_wireless_multimodal_platform.xml`

---

## 🎯 Tese Central
Projetar e fabricar nós sensores biomédicos vestíveis ultrafinos e de baixo custo exige uma separação rigorosa entre circuitos de alimentação comutados e conversores analógicos-digitais, priorizando microcontroladores sem fio monolíticos (SoCs com BLE e Wi-Fi integrados), barramentos I2C compartilhados com pull-ups calibrados e gerenciamento inteligente de energia por hardware (*power gating* com transistores MOSFET de canal P) para garantir que uma bateria LiPo minúscula consiga sustentar aquisição de múltiplos sensores com autonomia superior a 12 horas.

---

## 🔬 Metodologia de Hardware & Arquitetura do Circuito
* **Especificações do Hardware Aberto Documentado:**
  * Dimensões da PCB: Apenas $18\text{ mm} \times 22\text{ mm}$ em placa de 4 camadas (espessura de $0.8\text{ mm}$).
  * Microcontrolador: SoC sem fio RISC-V com Bluetooth Low Energy e rádio de $2.4\text{ GHz}$.
  * Gestão de Alimentação: Regulador LDO de ultrabaixo ruído e consumo quiescente ($I_q < 1\text{ }\mu\text{A}$) acoplado a circuito de recarga LiPo integrado (similar ao que temos no Seeed XIAO).
  * Sensores Integrados na Mesma Placa: IMU de 6 eixos (acelerômetro + giroscópio), barômetro digital e barramento de expansão I2C/SPI para sensores biomédicos ópticos e bioimpedância.
* **Táticas de Minimização de Ruído:**
  * Uso de planos de terra separados (AGND para sensores e DGND para antena RF/rádio), interligados em uma estrela de aterramento de ponto único (*star ground*) logo abaixo do chip regulador de tensão.
  * Capacitores de desacoplamento cerâmicos multicamadas (MLCC de $100\text{ nF}$ e $4.7\text{ }\mu\text{F}$) posicionados a menos de $1.5\text{ mm}$ dos pinos de alimentação de cada sensor.

---

## 🚑 Aplicação Direta no APH-BioShield™ & Impacto para Artigo Científico
1. **Guia de Layout e Montagem de PCB (Fase 2/3):** O artigo fornece o modelo exato de engenharia elétrica para desenhar o esquemático e o layout de circuito impresso do APH-BioShield no KiCad, garantindo que o rádio BLE não induza ruído elétrico de 60 Hz ou ruído de RF na entrada do biopotencial do ECG (AD8232).
2. **Impacto Acadêmico:** O periódico *HardwareX* é a principal referência mundial em hardware científico aberto e reprodutível. Citar o modelo TinZr e seguir suas diretrizes de documentação aberta fortalece a publicação de um artigo completo descrevendo a montagem e os testes do APH-BioShield.

---

## 🔗 Conexões no Grafo
* **Conceitos Alimentados:** [[c_pan_tompkins_ecg]], [[c_indice_perfusao_choque]]
* **MOC Central:** [[moc_aph_bioshield]]
