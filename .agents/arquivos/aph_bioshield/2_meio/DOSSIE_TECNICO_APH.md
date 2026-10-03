# APH-BioShield™: Projeto de Engenharia & Telemetria 3D para APH

> **Dispositivo Biométrico Móvel sem Fio para Triagem e Monitoramento Contínuo no Trauma Pré-Hospitalar (APH)**

---

## 1. Visão Geral e Renderização Conceitual 3D

Para atender à necessidade crítica do **Atendimento Pré-Hospitalar (SAMU / Resgate / Trauma)** de realizar a análise imediata e manter o monitoramento ininterrupto da vítima da cena do acidente até o centro cirúrgico hospitalar, foi desenvolvido o conceito industrial e a arquitetura do **APH-BioShield™**.

![APH-BioShield Design Industrial](/C:/Users/Maria/.gemini/antigravity-ide/brain/58104049-dc75-40bd-a7f0-f92c15aaa99b/aph_device_render_1791040266557.jpg)

---

## 2. Decisão Crítica de Form Factor: Adesivo Torácico vs. Pulseira

A dúvida entre **Pulseira** ou **Adesivo** é um dos pontos mais importantes do projeto. Clinicamente e fisiologicamente, **o Adesivo Torácico Esternal é amplamente superior para trauma e choque**:

| Critério Crítico em Trauma | Pulseira de Punho | Adesivo Torácico Esternal (Recomendado) |
| :--- | :--- | :--- |
| **Comportamento no Choque Hemorrágico** | **Falha Grave:** Em sangramentos internos ou externos, o sistema simpático induz **vasoconstrição periférica severa**. Os pulsos radiais no punho somem, a pele esfria e o sensor óptico (PPG) perde o sinal de pulso e SpO2. | **Excelente:** O fluxo sanguíneo no tronco e grandes vasos centrais (arco aórtico e artérias torácicas) é preservado mesmo em choques classe III/IV (hipotensão profunda). |
| **Captação do ECG (2 Eletrodos)** | **Inviável sozinho:** Dois eletrodos no mesmo punho não fecham vetor elétrico cardíaco. Exigiria que a vítima tocasse com a outra mão (impossível em vítimas inconscientes, agitadas ou com fratura). | **Autônomo:** Posicionado longitudinalmente sobre o esterno ou região subclavicular (distância de ~95mm), captura a onda P, o complexo QRS e a onda T continuamente sem cooperação da vítima. |
| **Cálculo da Pressão Arterial (PAT)** | Difícil sincronização com ECG sem cabos adicionais estendidos até o tórax. | O ECG e o PPG estão no mesmo eixo corporal, permitindo o cálculo do tempo de chegada da onda de pulso (**PAT / PTT**) com altíssima correlação. |
| **Detecção de Temperatura** | Mede membro frio por vasoconstrição (falsa leitura de hipotermia grave de extremidade). | Mede a pele sobre a circulação central, aproximando a temperatura da termorregulação central (prevenção da **Tríade Letal do Trauma**). |

> [!TIP]
> **Solução Híbrida Adotada:** O **APH-BioShield** foi projetado primariamente como um **Adesivo Torácico "Peel-and-Stick" de aplicação em 3 segundos**, mas possui passadores laterais reforçados para cintas de liberação rápida, podendo também ser acoplado a uma faixa de braço em pacientes com queimaduras de tórax ou ferimentos penetrantes no esterno.

---

## 3. Diagrama de Engenharia CAD (Vista Explodida dos Elementos)

A "receita" de hardware foi estruturada em camadas independentes, garantindo impermeabilidade (IP67), substituição rápida e proteção contra interferência eletromagnética (EMI):

![Vista Explodida Schematics](/C:/Users/Maria/.gemini/antigravity-ide/brain/58104049-dc75-40bd-a7f0-f92c15aaa99b/aph_exploded_view_1791040295077.jpg)

### Decomposição das Camadas:

1. **Camada 1: Base Adesiva Hidrocoloide / Silicone Biocompatível**
   - Hipoalergênica, respirável, com aberturas de corte a laser para que os sensores ópticos, elétricos e térmicos fiquem em contato íntimo com a pele.
   - Puxador de proteção rápida (Ready-to-Stick) aplicável em menos de 3 segundos mesmo sobre pele suada ou ensanguentada.
2. **Camada 2: Par de Eletrodos de Contato Seco (ECG)**
   - Liga de aço cirúrgico 316L com revestimento sinterizado de Ag/AgCl (cloreto de prata) com microdomos concêntricos.
   - Dispensa gel condutor líquido (que desidrata ou escorre no transporte) e mantém baixíssima impedância de contato (< 50 kΩ).
3. **Camada 3: Módulo Óptico Red + IR (+ Verde 525nm como melhoria)**
   - Emissores de 660 nm (Red) e 880/940 nm (Infravermelho) de alta luminosidade para oximetria arterial e pulso profundo.
   - **Melhoria adicionada:** LED Verde (525 nm) focado no leito microcapilar cutâneo para medição de perfusão em pacientes hipotérmicos.
   - **Barreira óptica de silicone negro:** Impede que a luz do emissor atinja o fotodiodo diretamente (elimina crosstalk óptico).
4. **Camada 4: Termômetro Infravermelho MEMS de Superfície**
   - Termopilha miniaturizada com lente de germânio/silício calibrada para a faixa de 32°C a 43°C (resolução de ±0.1°C).
   - Sensor de compensação de temperatura ambiente no mesmo invólucro para eliminar desvios térmicos causados pelo clima da cena (frio da noite, sol forte).
5. **Camada 5: Bateria Recarregável LiPo Ultra-fina (3.7V 280mAh)**
   - Autonomia contínua de 18 horas de transmissão de telemetria ininterrupta.
   - Bobina de indução magnética Qi para recarga sem fios na maleta de resgate da ambulância em 45 minutos.
6. **Camada 6: Placa-Mãe Rígido-Flexível (PCB)**
   - SoC Dual-Core ARM Cortex-M4/M33 (Nordic nRF5340) de processamento em tempo real.
   - **Comunicação Dupla:** Bluetooth Low Energy 5.3 (para o tablet do médico dentro da ambulância) + Transceiver Semtech LoRa 915 MHz (para transmissão direta a até 2 km para a central de trauma do hospital receptor).
   - **Acelerômetro/IMU de 6 eixos:** Filtra os choques e solavancos da ambulância e fornece guia de profundidade e frequência em caso de manobras de RCP.
7. **Camada 7: Carcaça Superior em Policarbonato Médico IP67**
   - Resistente a quedas de 2 metros no asfalto, à prova d'água e sangue (lavável com álcool 70% ou clorexidina).
   - Bumpers laterais em borracha de alta absorção de impacto na cor laranja de emergência.
8. **Camada 8: Micro-display OLED + Halo de LEDs Triagem START**
   - Mostrador sob luz solar com os parâmetros vitais principais.
   - Anel de LEDs RGB que pulsa no código internacional de triagem: **Vermelho (Imediato)**, **Amarelo (Urgente)**, **Verde (Leve)** ou **Preto (Expectante)**.

---

## 4. Como o Dispositivo Extrai Todos os Parâmetros Solicitados

### 1. Pressão Arterial (PA) Contínua sem Manguito Pneumático
* **Método Fisiológico:** Tempo de Chegada da Onda de Pulso (**PAT - Pulse Arrival Time**).
* **Como funciona:** O dispositivo detecta a despolarização ventricular pelo **pico R da onda de ECG** ($t_0$) e cronometra em microssegundos quando a onda de pressão arterial atinge o leito vascular abaixo do **sensor óptico PPG** ($t_1$). 
* A velocidade da onda de pulso ($PWV \propto 1/PAT$) é diretamente proporcional à pressão hidrostática arterial e ao tônus vascular. O algoritmo estima a Pressão Sistólica e Diastólica a cada batimento cardíaco sem interromper a circulação do braço com manguito.

### 2. Volume Sanguíneo e Hemorragia (Externa e Interna)
* **Método Fisiológico:** Índice de Perfusão (**PI**), Índice de Variabilidade Pletismográfica (**PVI**) e **Índice de Choque (SI)**.
* **Como funciona:**
  - O **PI** mede a proporção de sangue pulsátil vs estático no tecido. Em sangramentos ativos, o PI despenca de valores normais (2.0% - 5.0%) para menos de 0.3%.
  - O **PVI** mede as flutuações respiratórias na amplitude da onda de pulso. Se $PVI > 20\%$, há indicação precoce de hipovolemia por perda volêmica antes mesmo da pressão arterial cair.
  - O algoritmo combina em tempo real o **Shock Index**:
    $$\text{Shock Index (SI)} = \frac{\text{Frequência Cardíaca (BPM)}}{\text{Pressão Arterial Sistólica (mmHg)}}$$
    Se $SI \ge 0.9$, o anel de LED do dispositivo entra em estado de **Alerta Vermelho** e notifica o tablet do socorrista sobre hemorragia interna ativa oculta (baço, fígado, pelve).

### 3. Saturação de Oxigênio (SpO2)
* **Método Fisiológico:** Espectrofotometria de reflexão multi-comprimento de onda.
* **Como funciona:** Alternância de pulso luminoso a 1000 Hz entre o LED Vermelho (660nm - onde a desoxiemoglobina absorve mais) e o LED Infravermelho (880nm - onde a oxiemoglobina absorve mais). A razão das absorbâncias AC/DC calibrada por curva de calibração médica estima a SpO2 arterial com precisão de ±1.5%.

### 4. Batimentos Cardíacos e Ritmo (ECG)
* **Método Fisiológico:** Derivação bipolar de biopotencial torácico modificado.
* **Como funciona:** O par de eletrodos secos capta a diferença de potencial elétrico através do miocárdio, detectando arritmias letais de trauma: taquicardia sinusal compensatória, fibrilação ventricular (FV), taquicardia ventricular sem pulso (TVSP) e assistolia.

### 5. Circulação e Pulso
* **Método Fisiológico:** Morfologia da curva fotopletismográfica e entalhe dicrótico.
* **Como funciona:** Permite analisar a força de contratilidade ventricular esquerda e o fechamento da valva aórtica (entalhe dicrótico). Se o entalhe dicrótico se achatar e o pulso ficar filiforme, indica colapso de tônus vascular.

### 6. Frequências Cardíaca e Respiratória
* **FC:** Calculada instantaneamente pelos intervalos R-R do ECG e intervalos pico-a-pico do pulso PPG.
* **FR:** Extraída por redundância dupla:
  - **EDR (ECG-Derived Respiration):** A expansão da caixa torácica altera a posição anatômica do coração em relação aos eletrodos, modulando a amplitude do QRS.
  - **RIAV (Respiratory Induced Amplitude Variation):** A pressão intratorácica negativa na inspiração diminui o retorno venoso e modula a linha de base da onda óptica.

### 7. Temperatura Corporal Contínua
* **Método Fisiológico:** Radiação de corpo negro na banda de 8 a 14 µm via termopilha MEMS.
* **Como funciona:** Posicionada em câmara selada com abertura para a pele infraclavicular, mede a temperatura cutânea profunda e compensa pela temperatura ambiente interna. Crucial para prevenir a **Tríade Letal do Trauma** (Hipotermia + Coagulopatia + Acidose Metabólica).

---

## 5. Como Abrir o Estúdio 3D Interativo

O estúdio 3D completo foi construído na pasta do projeto:
- **Caminho:** `c:\Users\Maria\Downloads\dispositivo movel aph\index.html`
- **Servidor Local Ativo:** `http://localhost:8085`

### Funcionalidades do Estúdio:
1. **Manipulação 3D Completa:** Rotacione, aproxime e inspecione em qualquer ângulo com o mouse.
2. **Controle de Vista Explodida (0 a 100%):** Mova o slider para separar todas as camadas e ver a eletrônica interna flutuando no espaço.
3. **Modo Raio-X:** Torna a carcaça translúcida para enxergar todos os chips e bateria operando internamente.
4. **Simulação Clínica em Tempo Real:** Alterne entre cenários (Hemorragia Oculta, Vítima Estável, Choque Severo, PCR) e veja os sinais vitais, ondas de ECG e PPG reagirem na hora.
5. **Inspeção de Componentes:** Clique em qualquer componente (Eletrodos, Módulo Red+IR, Termopilha, Placa-Mãe, Bateria) para abrir sua ficha técnica com especificações detalhadas.
