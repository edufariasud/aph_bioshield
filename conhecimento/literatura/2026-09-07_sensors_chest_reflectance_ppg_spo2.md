---
tipo: literatura
area: engenharia_biomedica
tags:
  - literatura
  - paper
  - ppg
  - chest_ppg
  - spo2
  - aph
  - bioshield
autores: ["Kim et al.", "Park et al."]
fonte: "Sensors (Basel), 26(17):5676"
ano: 2026
data: 2026-10-03
status: fichado
doi: "10.3390/s26175676"
conceitos_relacionados:
  - "[[c_indice_perfusao_choque]]"
  - "[[c_pan_tompkins_ecg]]"
  - "[[c_respiracao_derivada_ppg]]"
moc: "[[moc_aph_bioshield]]"
---

# 📑 Fichamento: Real-Time SpO2 Estimation from Chest Reflectance Photoplethysmography: Algorithm Development and Clinical Validation Against Arterial SaO2

## 📌 Metadados da Fonte
- **Título Original:** Real-Time SpO2 Estimation from Chest Reflectance Photoplethysmography: Algorithm Development and Clinical Validation Against Arterial SaO2
- **Publicação:** *Sensors (Basel)*, Setembro de 2026.
- **Identificadores:** DOI: 10.3390/s26175676 | PMCID: PMC13567920 | PMID: 42740296
- **Arquivo Local Bruto:** `artigos/pmc13567920_chest_ppg_spo2.xml`

---

## 🎯 Tese Central
A oximetria de pulso convencional no dedo ou orelha apresenta excelentes amplitudes, porém é inviável para integração anatômica direta com eletrocardiograma (ECG) em um único dispositivo vestível torácico. Este estudo comprova clinicamente que é possível extrair saturação periférica de oxigênio ($SpO_2$) em tempo real com alta acurácia médica ($A_{rms} < 3.0\%$) diretamente do **tórax anterior (esterno)** via **fotopletismografia de reflexão**, desde que implementado um pipeline digital de cancelamento de artefatos e calibração óptica específica para tecidos de baixa perfusão central.

---

## 🔬 Metodologia & Evidências Empíricas
* **Validação Clínica:** Protocolo de desoxigenação arterial induzida em ambiente controlado com amostragem direta de sangue arterial ($SaO_2$) via gasometria como padrão-ouro (faixa de $70\%$ a $100\%$).
* **Dispositivo Testado:** Patch torácico com LEDs Vermelho ($660\text{ nm}$) e Infravermelho ($940\text{ nm}$) com fotodiodo PIN em modo de reflexão.
* **Pipeline Matemático Desenvolvido:**
  1. *Signal Preprocessing:* Filtro passa-faixa elíptico de 4ª ordem ($0.5\text{ Hz}$ a $5.0\text{ Hz}$) com correção de offset DC móvel.
  2. *Detecção Adaptativa de Picos:* Janela móvel baseada no intervalo RR do ECG simultâneo para guiar o limiar do pico sistólico óptico, anulando falsos picos causados por ruído.
  3. *Cálculo da Razão de Razões ($R$):*
     $$R = \frac{(AC_{\text{red}} / DC_{\text{red}})}{(AC_{\text{ir}} / DC_{\text{ir}})}$$
  4. *Equação de Calibração Torácica Ajustada:*
     $$SpO_2 = A - B \times R$$
     (Onde os coeficientes $A$ e $B$ diferem significativamente dos valores do dedo devido ao espalhamento óptico esternal).

---

## 🚑 Aplicação Prática no APH-BioShield™
1. **Confirmação da Arquitetura de Tórax Central:** Valida formalmente a escolha do esterno para o MAX30102 colado no peito em vez do dedo.
2. **Guia de Picos Guiado por ECG:** Como o APH-BioShield possui o AD8232 (ECG) e o MAX30102 operando juntos no mesmo microcontrolador (nRF52840), o firmware pode usar os complexos QRS do ECG para saber exatamente quando o pico sistólico do PPG deve ocorrer, descartando trepidações da ambulância que aconteçam fora dessa janela temporal esperada.
3. **Calibração de Firmware:** A curva de calibração padrão de fábrica do MAX30102 para dedo subestima a oxigenação no tórax; os parâmetros empíricos deste paper devem ser programados na tabela de lookup do firmware.

---

## 🔗 Conexões no Grafo
* **Conceitos Alimentados:** [[c_indice_perfusao_choque]], [[c_pan_tompkins_ecg]], [[c_respiracao_derivada_ppg]]
* **MOC Central:** [[moc_aph_bioshield]]
