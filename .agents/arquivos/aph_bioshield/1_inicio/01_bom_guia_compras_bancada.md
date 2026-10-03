# Lista de Materiais (BOM) & Guia de Compra para Prototipagem em Bancada

> **Dispositivo:** APH-BioShield™  
> **Finalidade:** Prova de Conceito (PoC) Funcional em Bancada com Módulos COTS de Baixo Custo  

---

## 1. Visão Geral da Receita de Hardware

O protótipo de bancada integra os seguintes blocos funcionais:
1. **Emissor/Receptor Óptico Red + IR:** $SpO_2$, Pulso, Frequência Respiratória e Índice de Perfusão (PI).
2. **Front-End de ECG:** Monitoramento de 1 derivação para ritmo cardíaco e detecção do complexo QRS.
3. **Termômetro Infravermelho:** Leitura contínua de temperatura dérmica sem contato direto.
4. **Microcontrolador Central:** Plataforma ARM Cortex-M4F com Bluetooth Low Energy 5.0 integrado.
5. **Comunicação de Longo Alcance:** Módulo transceptor LoRa 915 MHz para telemetria de campo.
6. **Interface com Usuário:** Microdisplay OLED de alta definição e Anel de LEDs RGB para triagem visual START.
7. **Sistema de Alimentação:** Bateria de polímero de lítio (LiPo) 3.7V recarregável via USB-C.

---

## 2. Catálogo Técnico de Peças (BOM Detalhada)

| Item | Componente / Função | Part Number Comercial | Interface | Onde Encontrar | Preço Estimado (BRL) |
| :---: | :--- | :--- | :---: | :--- | :---: |
| **01** | Sensor Óptico Red + IR ($SpO_2$, Pulso, PI, FR) | MAX30102 (CJMCU-30102) | I2C (3.3V) | Mercado Livre, AliExpress, Shopee | R$ 20 – 35 |
| **02** | Front-End Analógico ECG (Ritmo e Frequência) | AD8232 Heart Monitor | Analógico | Mercado Livre, Eletrogate, Robocore | R$ 32 – 55 |
| **03** | Eletrodos de Contato | Eletrodos padrão ECG (gel) + Botões Snap Inox 316L | Mecânico | Lojas Médicas, AliExpress | R$ 20 – 40 |
| **04** | Termômetro Infravermelho | MLX90614ESF-BAA (Módulo GY-906) | I2C (3.3V) | Mercado Livre, Mouser, AliExpress | R$ 48 – 80 |
| **05** | Microcontrolador Principal + Rádio BLE | Seeed Studio XIAO BLE nRF52840 | I2C, SPI, ADC, BLE | Mouser, AliExpress, Mercado Livre | R$ 68 – 95 |
| **06** | Transceptor LoRa Longo Alcance | Ra-01S ou SX1262 (915 MHz) | SPI | AliExpress, Mercado Livre | R$ 35 – 60 |
| **07** | Micro Display OLED de Leitura Local | OLED 0.96" 128x64 (SSD1306) | I2C (0x3C) | Mercado Livre, Robocore, Baú Eletrônica | R$ 16 – 28 |
| **08** | Anel LED Triagem START | Anel 8 ou 12 LEDs WS2812B / SK6812 | 1-Wire Digital | Mercado Livre, Shopee, AliExpress | R$ 14 – 25 |
| **09** | Bateria LiPo Recarregável | Bateria LiPo 3.7V 250mAh (Mod. 402030) | 3.7V / JST | Mercado Livre, AliExpress | R$ 22 – 38 |
| **10** | Fita de Fixação Médica | Fita Médica Tegaderm ou 3M Hipoalergênica | Tópico | Farmácias e Distribuidores Médicos | R$ 15 – 30 |

* **Custo Total Estimado para 1 Unidade:** R$ 290,00 a R$ 486,00.

---

## 3. Mapa de Pinout e Interligação (XIAO BLE nRF52840)

O barramento I2C é compartilhado entre múltiplos periféricos, aproveitando seus endereços de hardware exclusivos:

| Módulo / Periférico | Pinos do Módulo | Pino no XIAO BLE | Função / Observação |
| :--- | :--- | :--- | :--- |
| **MAX30102 (Óptico)** | VCC / GND | 3V3 / GND | Alimentação regulada 3.3V |
| **MAX30102 (Óptico)** | SDA / SCL | D4 (SDA) / D5 (SCL) | Endereço I2C: `0x57` |
| **MLX90614 (Térmico)** | VIN / GND | 3V3 / GND | Alimentação 3.3V |
| **MLX90614 (Térmico)** | SDA / SCL | D4 (SDA) / D5 (SCL) | Endereço I2C: `0x5A` |
| **OLED 0.96 (SSD1306)** | VCC / GND | 3V3 / GND | Alimentação 3.3V |
| **OLED 0.96 (SSD1306)** | SDA / SCL | D4 (SDA) / D5 (SCL) | Endereço I2C: `0x3C` |
| **AD8232 (ECG)** | 3.3V / GND | 3V3 / GND | Alimentação analógica |
| **AD8232 (ECG)** | OUTPUT | A0 (P0.02) | Leitura via ADC de 12 bits |
| **Anel WS2812B (LEDs)** | DIN | D1 (P0.03) | Linha de comando PWM/Digital |
| **LoRa SX1262 (SPI)** | SCK / MOSI / MISO / NSS | D8 / D10 / D9 / D7 | Barramento de dados de alta velocidade |
| **LoRa SX1262 (Controle)** | RESET / BUSY / DIO1 | D2 / D3 / D6 | Linhas de controle do rádio |
| **Bateria LiPo 3.7V** | Polo (+) e (-) | Pads BAT+ e BAT- | Pads de solda na face inferior da placa |
