# Análise Crítica de Viabilidade Técnica e Gargalos de Hardware

> **Documento:** Análise de Risco e Engenharia Pré-Fabricação  
> **Fase:** 1_inicio / Viabilidade de Bancada  

---

## 1. Veredito Executivo de Viabilidade

| Domínio | Nota (0 a 10) | Diagnóstico |
| :--- | :---: | :--- |
| **Prova de Conceito (PoC de Bancada)** | **8.5 / 10** | Altamente viável. Peças prontas, baratas, protocoladas e fáceis de integrar. |
| **Dispositivo de Campo APH Real** | **4.0 / 10** | Exige evolução profunda para PCB integrada de 4 camadas e filtros digitais severos. |

---

## 2. Detalhamento dos 5 Gargalos Técnicos Críticos

### Gargalo 1: Pressão Arterial Contínua por PAT (*Pulse Arrival Time*)
* **Mecanismo:** Intervalo de tempo entre o pico elétrico R do ECG (AD8232) e o início da onda de pulso no PPG (MAX30102).
* **Risco Clínico:** Em pacientes de trauma em choque hemorrágico, a liberação maciça de catecolaminas (adrenalina) e a vasoconstrição periférica alteram a rigidez da parede arterial independentemente do volume sanguíneo. A correlação milissegundo $\rightarrow$ mmHg descalibra.
* **Mitigação Técnica:** Reportar o PAT como **Indicador de Tendência Hemodinâmica** (ex: *"PA em queda livre"* ou *"Vasoconstrição aguda"*), sem prometer aferição numérica de 120×80 mmHg sem calibração prévia por manguito.

### Gargalo 2: ECG de Vetor Curto com Eletrodos Secos
* **Mecanismo:** O AD8232 foi projetado para 3 derivações (eletrodos nos membros com perna de referência *Right Leg Drive* para aterramento de ruído de 60 Hz).
* **Risco de Bancada:** Posicionar dois botões secos a 5 cm de distância no esterno gera um sinal de amplitude muito baixa (microvolts), que se perde com tremores musculares ou respiração.
* **Mitigação Técnica:** Para a Fase 1 na bancada, utilizar eletrodos descartáveis padrão com gel aderente para validar o firmware; implementar o algoritmo Pan-Tompkins para detecção robusta do QRS mesmo sob ruído.

### Gargalo 3: Autonomia da Bateria LiPo (250 mAh) vs. Consumo Real
* **Consumo Estimado do Sistema:**
  * XIAO nRF52840 (ativo com BLE): ~7 mA
  * Display OLED 0.96 (aceso contínuo): ~15–20 mA
  * Anel de LEDs WS2812B (8 LEDs a 50% de brilho contínuo): ~80–120 mA
  * Transceptor LoRa SX1262 (picos de transmissão TX): ~100 mA
* **Duração Teórica:** Apenas **35 a 50 minutos** se display e anel ficarem ligados continuamente.
* **Mitigação Técnica:**
  * Modo pulsado/sob demanda para os LEDs (acender por 3 segundos apenas ao atualizar status da triagem START ou ao toque).
  * *Sleep mode* do OLED após 30 segundos de inatividade, reativado por acelerômetro ou comando BLE.
  * Transmissão de pacotes LoRa em intervalos de 5 a 10 segundos, não contínua.

### Gargalo 4: Limite Físico de Pinos (GPIO) no Seeed XIAO
* O Seeed XIAO expõe 11 pinos GPIO utilizáveis.
* Alocação necessária: 2 pinos (I2C) + 1 pino (ADC ECG) + 1 pino (LEDs) + 7 pinos (LoRa SPI + controles) = **11 pinos**.
* **Impacto:** Ocupação de 100% dos pinos. Não sobra linha para botão liga/desliga físico, interrupção do acelerômetro ou pino de alarme de eletrodo solto (*Leads-Off* do AD8232).
* **Mitigação Técnica:** No protótipo inicial de bancada, priorizar o rádio BLE nativo do nRF52840 (que não gasta nenhum pino físico externo) e desacoplar o módulo LoRa físico para uma placa de expansão posterior.

### Gargalo 5: Volume Mecânico dos Módulos vs. Formato "Adesivo Torácico"
* Placas de bancada empilhadas com barras de pinos (headers) e jumpers atingem mais de 25 mm de altura.
* Uma fita Tegaderm não sustenta esse bloco mecânico no suor do paciente.
* **Mitigação Técnica:** Manter a Prova de Conceito de Fase 1 em uma pequena caixa plástica rígida (case impressa em 3D) com fixação por cinta elástica peitoral ou cabo curto para eletrodos adesivos, migrando para encapsulamento flexível apenas na Fase 3 após desenho de PCB proprietária.
