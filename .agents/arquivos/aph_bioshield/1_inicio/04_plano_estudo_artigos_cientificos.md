# Plano de Estudo de Literatura Científica & Processamento de Sinais (DSP)

> **Documento:** Base Científica e Algorítmica  
> **Fase:** 1_inicio / Revisão de Estado da Arte  

---

## 1. Visão Geral da Abordagem
Para viabilizar medições clínicas robustas utilizando sensores de baixo custo (MAX30102, AD8232, MLX90614 e acelerômetro), a inteligência do sistema é transferida do hardware físico para o **processamento digital de sinais em tempo real** executado no microcontrolador ARM Cortex-M4F (nRF52840).

---

## 2. Os 6 Eixos de Pesquisa Científica

### Eixo 1: Oximetria e PPG em Região Torácica/Esternal (*Chest PPG*)
* **Desafio:** Menor amplitude de sinal em relação ao dedo; suscetibilidade a variações de pressão de contato.
* **Artigos Chave:**
  * *Tamura, T., et al. (2014).* "Wearable Photoplethysmographic Sensors—Past and Present". *Electronics*, 3(2), 282-302.
  * *Poh, M. Z., et al. (2010).* "Motion-Tolerant Wearable Biosensor for Simultaneous Monitoring of Heart Rate and Respiratory Rate". *IEEE Trans Biomed Eng*.
* **Extração Algorítmica:** Filtros adaptativos LMS (*Least Mean Squares*) usando eixos do acelerômetro como sinal de referência para cancelamento de ruído mecânico.

### Eixo 2: Índice de Perfusão (PI) e Marcadores de Choque
* **Desafio:** Identificar precocemente hipovolemia por hemorragia interna antes da hipotensão sistêmica.
* **Artigos Chave:**
  * *Lima, A., & Bakker, J. (2005).* "Noninvasive monitoring of peripheral perfusion in serious illness". *Intensive Care Medicine*, 31(10), 1316-1326.
  * *Convertino, V. A., et al. (2020).* "The Compensatory Reserve Index (CRI) for early identification of hemorrhage". *Shock*, 53(2), 143-151.
* **Extração Algorítmica:** Cálculo contínuo da razão $AC/DC$ da onda pletismográfica e monitoramento da inclinação de decaimento do sinal.

### Eixo 3: ECG de Vetor Curto com Eletrodos Secos
* **Desafio:** Baixa amplitude do QRS no esterno e ruído de 60 Hz sem eletrodo de perna direita (RLD).
* **Artigos Chave:**
  * *Pan, J., & Tompkins, W. J. (1985).* "A Real-Time QRS Detection Algorithm". *IEEE Trans Biomed Eng*, 32(3), 230-236.
  * *Meziane, N., et al. (2013).* "Dry electrodes for electrocardiography: A review of the state of the art". *Med Eng Phys*.
* **Extração Algorítmica:** Pipeline Pan-Tompkins (Passa-faixa 5–15 Hz $\rightarrow$ Derivada $\rightarrow$ Quadratura $\rightarrow$ Integração móvel $\rightarrow$ Limiar adaptativo duplo).

### Eixo 4: Extração da Frequência Respiratória Indireta (EDR e PPG)
* **Desafio:** Eliminar faixas mecânicas no peito, extraindo a FR puramente por software a partir dos dados do MAX30102 e AD8232.
* **Artigos Chave:**
  * *Charlton, P. H., et al. (2018).* "Breeding practical algorithms for respiratory rate estimation from the electrocardiogram and photoplethysmogram". *Physiol Meas*, 39(2).
  * *Reisner, A., et al. (2008).* "Utility of the photoplethysmogram in circulatory monitoring". *Anesthesiology*.
* **Extração Algorítmica:** Fusão de três modulações: RIAV (amplitude do pulso), RIIV (linha de base) e RIFV (variabilidade da frequência cardíaca).

### Eixo 5: Limites e Realidade da Pressão Arterial Cuffless (PTT/PAT)
* **Desafio:** Entender as limitações hemodinâmicas do *Pulse Arrival Time* para não induzir a equipe de trauma a erro.
* **Artigos Chave:**
  * *Mukkamala, R., et al. (2015).* "Toward ubiquitous blood pressure monitoring via pulse transit time: theory and practice". *IEEE Trans Biomed Eng*.
  * *Finnegan, E., et al. (2021).* "Pulse arrival time is not an adequate surrogate for pulse transit time during hemodynamic instability". *Physiol Meas*.
* **Extração Algorítmica:** Restringir o PAT ao papel de **alerta de tendência de descompensação**, desvinculando-o de valores numéricos de mmHg não calibrados.

### Eixo 6: Estimativa de Temperatura Central (*Core Temperature*)
* **Desafio:** Medir temperatura da pele torácica e estimar temperatura interna mesmo sob ambiente frio e choque.
* **Artigos Chave:**
  * *Gunga, H. C., et al. (2009).* "A non-invasive device to continuously determine heat strain in humans". *J Therm Biol*, 34(6).
* **Extração Algorítmica:** Modelo de compensação de fluxo de calor (*Dual Heat Flux*) cruzando a temperatura ambiente medida pelo sensor com a temperatura de superfície.
