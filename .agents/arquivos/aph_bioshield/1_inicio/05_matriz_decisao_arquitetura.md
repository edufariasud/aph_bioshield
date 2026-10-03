# Matriz de Decisão Arquitetural & Trade-Offs de Engenharia

> **Documento:** Definições Estruturantes de Projeto  
> **Fase:** 1_inicio / Matriz de Decisão  

---

## 1. As 6 Questões Críticas de Arquitetura

Para balizar o desenvolvimento do hardware e do firmware, as seguintes decisões estruturais foram catalogadas com seus respectivos impactos de projeto:

```text
                                DECISÕES ESTRATÉGICAS
 ┌───────────────────────────┬───────────────────────────┬───────────────────────────┐
 │ 1. Local Anatômico        │ 2. Requisito de PA        │ 3. Ciclo de Vida          │
 │ [ ] Tórax / Esterno       │ [ ] Tendência Hemodinâmica│ [ ] 100% Descartável      │
 │ [ ] Testa / Frontal       │ [ ] Valor Numérico mmHg   │ [ ] Núcleo Reutilizável   │
 ├───────────────────────────┼───────────────────────────┼───────────────────────────┤
 │ 4. Interface & Dados      │ 5. Tolerância a Ruído     │ 6. Entrega do MVP         │
 │ [ ] Local (OLED + LEDs)   │ [ ] Trepidação Ambulância │ [ ] Triagem START Rápida  │
 │ [ ] Tablet BLE Próximo    │ [ ] Tremor Muscular/Frio  │ [ ] Ritmo de ECG Limpo    │
 │ [ ] Central LoRa / 4G     │ [ ] Paciente Estático     │ [ ] Monitor Choque/PI     │
 └───────────────────────────┴───────────────────────────┴───────────────────────────┘
```

---

## 2. Análise Detalhada dos Trade-Offs

### Decisão 1: Local Anatômico de Aplicação
* **Opção A (Tórax / Esterno) [Recomendada]:** Permite integrar ECG de 2 eletrodos, expansão torácica inercial e PPG no mesmo chassi central. *Trade-off:* Exige pressão mecânica firme para o PPG de reflexão.
* **Opção B (Testa):** Excelente perfusão e leitura térmica sem contato; inviabiliza ECG sem puxar fios longos até os braços.
* **Opção C (Híbrido):** Tórax + clipe auricular. Melhora a qualidade óptica mas introduz cabos no paciente, violando a simplicidade do APH.

### Decisão 2: Requisito de Pressão Arterial
* **Opção A (Tendência Hemodinâmica Contínua) [Recomendada para Fase 1]:** O sistema emite alerta de descompensação baseado em desvio de PAT e amplitude de pulso. Tecnicamente honesto e seguro clinicamente.
* **Opção B (Valor Numérico Absoluto):** Exige calibração prévia individual por manguito insuflável ou integração de micro-bomba mecânica, encarecendo e aumentando o peso do hardware.

### Decisão 3: Ciclo de Vida do Hardware
* **Opção A (100% Descartável):** Ideal para contaminação biológica em trauma, mas inviável economicamente com microcontrolador nRF52840 em prototipagem inicial.
* **Opção B (Núcleo Eletrônico Reutilizável com Base Descartável) [Recomendada]:** O módulo inteligente se desencaixa de uma fita adesiva que contém apenas os eletrodos de contato e a janela óptica.

### Decisão 4: Interface e Exibição de Dados
* **Opção A (Apenas Local):** OLED + LEDs no peito do paciente. Econômico em RF, mas obriga o socorrista a olhar para o peito da vítima na ambulância escura.
* **Opção B (Local + BLE para Tablet da Viatura) [Recomendada]:** O socorrista visualiza as curvas completas na tela do tablet/smartphone, enquanto o dispositivo no peito mantém apenas o anel de LEDs START.
* **Opção C (Telemetria LoRa para Central de Regulação):** Essencial para acidentes com múltiplas vítimas ou áreas rurais sem sinal celular. Pode ser adicionado como módulo modular.

### Decisão 5: Nível de Tolerância a Ruído
* O algoritmo deve priorizar **Filtros Adaptativos RLS/LMS acoplados à IMU** para subtrair as frequências de vibração do motor e suspensão da viatura de resgate (faixa típica de 3 a 12 Hz).

### Decisão 6: Escopo do MVP (Fase 1 de Bancada)
* **Entregável Mínimo Recomendado:**
  1. Leitura simultânea e contínua de $SpO_2$ e FC via MAX30102;
  2. Traçado de ECG filtrado e identificação de batimentos via AD8232;
  3. Cálculo do Índice de Perfusão (PI);
  4. Mudança de cor dinâmica do anel de LEDs conforme tabela START;
  5. Envio de pacote de telemetria via Bluetooth Low Energy (BLE) para aplicativo móvel.
