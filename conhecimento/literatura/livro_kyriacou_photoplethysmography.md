---
tipo: literatura
area: engenharia_biomedica
tags:
  - literatura
  - livro
  - fotopletismografia
  - ppg
  - spo2
  - pat
  - ptt
  - perfusao
  - hemodinamica
autores: ["John Allen", "Panicos A. Kyriacou"]
fonte: "Photoplethysmography: Technology, Signal Analysis and Applications (Elsevier Ltd., Academic Press, 2021)"
ano: 2021
data: 2026-10-03
status: fichado
conceitos_relacionados:
  - "[[c_pulse_arrival_time_pat]]"
  - "[[c_indice_perfusao_choque]]"
  - "[[c_filtros_biomedicos_embarcados]]"
moc: "[[moc_aph_bioshield]]"
---

# 📑 Fichamento: Photoplethysmography — Technology, Signal Analysis and Applications

## 📌 Metadados da Fonte
- **Título Original:** Photoplethysmography: Technology, Signal Analysis and Applications
- **Autores / Editores:** Panicos A. Kyriacou, John Allen
- **Publicação:** Elsevier / Academic Press, 2021. ISBN: 978-0-12-823374-0
- **Formato Local:** `livros/John Allen - Photoplethysmography Technology Signal Analysis and Applications (2021, Elsevier Ltd.) - libgen.li.pdf` (59.14 MB)

---

## 🎯 Tese Central
A obra é o tratado definitivo internacional sobre a tecnologia da fotopletismografia (PPG). Sistematiza desde os fundamentos ópticos de interação luz-tecido (espalhamento anisotrópico e absorção pela oxi/desoxi-hemoglobina) até os métodos matemáticos avançados de decomposição de onda de pulso para extração simultânea de: saturação de oxigênio ($SpO_2$), frequência cardíaca ($HR$), variabilidade da frequência cardíaca ($HRV$), frequência respiratória ($RR$), índice de perfusão ($PI$), índice de variabilidade pletismográfica ($PVI$) e estimativa de rigidez arterial e pressão arterial contínua sem manguito ($PAT/PTT$).

---

## 🔬 Fundamentos Técnicos Críticos para o APH-BioShield™

### 1. Separação de Componentes AC e DC do Sinal Óptico
* **Componente DC ($I_{DC}$):** Representa a atenuação basal constante da luz causada por ossos, músculos, tecido adiposo, pele e sangue venoso/arterial não pulsátil. É a linha de base de baixa frequência.
* **Componente AC ($I_{AC}$):** Representa a modulação pulsátil sincrônica com a ejeção sistólica ventricular (variação de volume nas arteríolas dérmicas). Tipicamente corresponde a apenas $0.1\%\text{ a }2.0\%$ da intensidade total de luz detectada.
* **Índice de Perfusão ($PI$):** Formalmente definido pela razão percentual entre os componentes pulsátil e não pulsátil:
  $$PI = \left(\frac{I_{AC}}{I_{DC}}\right) \times 100\%$$
* Em pacientes normovolêmicos e perfundidos, o $PI$ situa-se tipicamente entre $1.5\%\text{ e }10\%$. Em quadros de choque hipovolêmico, hipotermia ou vasoconstrição periférica intensa, o $PI$ desce abaixo de $0.5\%$, servindo como biomarcador primário de falência circulatória pré-hospitalar.

### 2. Oximetria de Pulso ($SpO_2$) e Relação $R$
* Utiliza a absorção diferencial da hemoglobina oxigenada ($HbO_2$) e desoxigenada ($RHb$) nos comprimentos de onda de $660\text{ nm}$ (Vermelho) e $880\text{--}940\text{ nm}$ (Infravermelho):
  $$R = \frac{(I_{AC} / I_{DC})_{\text{red}}}{(I_{AC} / I_{DC})_{\text{ir}}}$$
* A curva de calibração empírica padrão adotada na indústria segue a aproximação:
  $$SpO_2 \approx A - B \cdot R \quad \text{ou} \quad SpO_2 = \frac{k_1 - k_2 \cdot R}{k_3 - k_4 \cdot R}$$

### 3. Estimativa de Pressão Arterial via Pulse Arrival Time (PAT)
* **Definição de PAT:** O intervalo temporal transcorrido entre o pico da onda R no eletrocardiograma (despolarização ventricular) e o pé (início do aclive sistólico) da onda de pulso periférica no PPG:
  $$PAT = PEP + PTT$$
  onde $PEP$ é o período pré-ejeção isométrica cardíaca e $PTT$ é o tempo real de propagação do pulso através da árvore arterial.
* **Física da Propagação (Equação de Moens-Korteweg):**
  $$PWV = \frac{D}{PTT} = \sqrt{\frac{E \cdot h}{\rho \cdot 2r_0}}$$
  A velocidade da onda de pulso ($PWV$) varia com a rigidez elástica vascular ($E$), que por sua vez é modulada pela pressão arterial transluminal instantânea. Logo, aumentos de pressão arterial enrijecem a parede do vaso, aumentam $PWV$ e **reduzem o $PAT$**.

### 4. Extração de Frequência Respiratória ($RR$) a partir do PPG
O livro detalha as 3 modulações fisiológicas induzidas pela respiração no sinal PPG periférico:
1. **Modulação de Linha de Base (BW - Baseline Wander):** Variação de baixa frequência decorrente das oscilações da pressão intratorácica que alteram o retorno venoso sistêmico.
2. **Modulação de Amplitude (AM - Amplitude Modulation):** Flutuações periódicas na amplitude sistólica de pico a pico do pulso arterial decorrentes da variação do volume de ejeção sistólico (análogo ao pulso paradoxal).
3. **Modulação de Frequência (FM - Frequency Modulation):** Arritmia Sinusal Respiratória (RSA), onde a frequência cardíaca acelera durante a inspiração e desacelera na expiração.

---

## 🚑 Diretrizes de Engenharia para o APH-BioShield™
1. **Algoritmo de Detecção do Pé Sistólico:** Para o cálculo de PAT, detectar o "pé" da onda de pulso via primeira derivada máxima ($d(PPG)/dt_{\max}$) ou segunda derivada ($d^2(PPG)/dt^2$) é significativamente mais robusto contra variações morfológicas do que tentar usar o topo sistólico.
2. **Filtragem Digital de Banda:**
   * Para extração de $HR$ e forma de pulso: Filtro passa-faixa Butterworth de 4ª ordem ($0.5\text{--}5.0\text{ Hz}$).
   * Para análise de respiração por linha de base: Filtro passa-baixo de corte em $0.1\text{--}0.5\text{ Hz}$.
3. **Controle Automático de Ganho (AGC) dos LEDs:** Em pacientes com vasoconstrição ou pele de baixa refletância, o algoritmo de calibração em tempo real deve ajustar a corrente do LED (passos de $0.2\text{ mA}$) para manter o valor do ADC na faixa ideal ($150.000\text{ a }220.000$ counts no conversor de 18 bits do MAX30102).

---

## 🔗 Conexões no Grafo do Conhecimento
- **Conceitos Alimentados:**
  - [[c_pulse_arrival_time_pat]]
  - [[c_indice_perfusao_choque]]
  - [[c_filtros_biomedicos_embarcados]]
- **MOC Central:** [[moc_aph_bioshield]]
