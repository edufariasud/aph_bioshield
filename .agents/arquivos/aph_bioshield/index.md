# APH-BioShield™ — Monitor Biomédico Multiparamétrico Portátil para APH

> **Status:** Fase 1 (Ideação Bruta e Prototipagem em Bancada)  
> **Área:** Engenharia Biomédica & Sistemas Embarcados de Resgate  
> **Público-Alvo:** Atendimento Pré-Hospitalar (APH), Equipes de Resgate, SAMU, Medicina Tática  

---

## 🎯 1. O Pitch (O Topo da Pirâmide)
O **APH-BioShield™** é um dispositivo biométrico vestível sem fio, ultracompacto e de baixo custo, projetado especificamente para o ambiente caótico do **Atendimento Pré-Hospitalar (APH)**. 

Diferente de monitores de leito tradicionais (pesados, cheios de cabos e dependentes de tomadas) e de oxímetros comuns de dedo (que falham por vasoconstrição periférica no choque hemorrágico), o APH-BioShield é concebido para ser aplicado em **menos de 10 segundos** em região central (tórax/esterno), fornecendo triagem contínua instantânea (método START), suporte hemodinâmico e telemetria sem fio durante o transporte do paciente politraumatizado.

---

## ⚡ 2. A Dor Clínica que Resolve
1. **O colapso da oximetria de extremidade no choque:** No trauma com hemorragia e hipotermia, o corpo fecha os vasos periféricos para irrigar coração e cérebro. Sensores de dedo perdem o sinal. O monitoramento no tórax central preserva o sinal pulsátil.
2. **Tempo de resposta no protocolo de trauma (XABCDE):** O socorrista precisa de agilidade. Cabos soltos enrolam na maca e atrasam a imobilização. Um patch/dispositivo central sem fios consolida todos os parâmetros essenciais em um único ponto de contato.
3. **Detecção precoce de choque oculto:** A pressão arterial sistêmica demora a cair no choque compensado. O **Índice de Perfusão (PI)** e a variabilidade do pulso captados pelo PPG óptico revelam a hipovolemia muito antes da hipotensão severa.

---

## 🔬 3. Mapeamento de Sinais e Parâmetros
* **Oximetria ($SpO_2$) & Pulso:** PPG óptico multiespectral (Red + IR) por reflexão.
* **Índice de Perfusão (PI) / Perda Volêmica:** Razão AC/DC da onda pletismográfica.
* **Eletrocardiograma (ECG):** Derivação única torácica para ritmo cardíaco e arritmias.
* **Frequência Respiratória (FR):** Dupla extração (modulação respiratória na onda PPG + expansão torácica por IMU/acelerômetro).
* **Temperatura Corporal:** Termometria infravermelha dérmica com algoritmo de compensação.
* **Triagem START Visual:** Anel de LEDs RGB inteligente indicando cor de prioridade (Vermelho / Amarelo / Verde / Preto).
* **Conectividade:** Bluetooth Low Energy (BLE 5.0) para tablet de campo e LoRa de longo alcance.

---

## 📂 4. Estrutura do Repositório do Projeto

```text
aph_bioshield/
├── index.md                 <-- Este documento (Pitch e visão macro)
├── diario_de_bordo.md       <-- Rastreador de sessões e pendências
├── 1_inicio/                <-- Fase 1: Ideação Bruta, BOM de Bancada e Pesquisa
│   ├── 01_bom_guia_compras_bancada.md
│   ├── 02_analise_critica_viabilidade.md
│   ├── 03_desafios_fisiologicos_aph.md
│   ├── 04_plano_estudo_artigos_cientificos.md
│   └── 05_matriz_decisao_arquitetura.md
├── 2_meio/                  <-- Fase 2: Laboratório (Algoritmos DSP, Schematics e Firmware)
└── 3_fim/                   <-- Fase 3: Especificação Final de Fabricação (Gerbers e Firmware v1)
```
