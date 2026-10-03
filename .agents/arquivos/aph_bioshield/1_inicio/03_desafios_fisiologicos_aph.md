# Desafios Fisiológicos e Operacionais no Atendimento Pré-Hospitalar (APH)

> **Documento:** Requisitos Clínicos e Fisiologia de Emergência  
> **Fase:** 1_inicio / Engenharia de Requisitos Clínicos  

---

## 1. O Ambiente do APH vs. Ambiente Hospitalar de Leito

No leito hospitalar tradicional, o paciente repousa em ambiente termicamente controlado, imóvel, com acesso a tomadas e cabos de 2 metros. No **APH (Atendimento Pré-Hospitalar)**, o paciente se encontra sob:
* **Cinemática de Trauma:** Vítimas encarceradas em ferragens, atropelamentos, quedas ou ferimentos por projétil de arma de fogo.
* **Ambiente Caótico:** Poeira, sangue, chuva, asfalto molhado e manobras rápidas de extricação.
* **Transporte em Alta Velocidade:** Trepidação constante de maca, solavancos de ambulância e aceleração/desaceleração brusca gerando artefatos mecânicos severos.
* **Regime de Poucos Minutos ("Hora de Ouro"):** O protocolo XABCDE exige que nenhuma intervenção de monitoramento atrase a hemostasia ou a via aérea.

---

## 2. A Fisiologia do Choque Hemorrágico: Por que o "Dedo" Falha?

O choque hipovolêmico por perda sanguínea ativa uma resposta reflexa maciça do sistema nervoso simpático:
1. **Vasoconstrição Periférica Seletiva:** Vasos cutâneos e das extremidades (dedos das mãos e pés) se fecham para desviar todo o débito cardíaco aos órgãos vitais nobres (miocárdio e encéfalo).
2. **Queda Drástica do Sinal Pulsátil no Dedo:** A onda pulsátil que chega aos leitos capilares dos dedos torna-se quase indetectável para fotodetectores comuns de oxímetros de pulso por transmissão. O aparelho reporta erro ou leituras aberrantes.
3. **Preservação do Fluxo Central:** O fluxo sanguíneo no leito vascular do **esterno, tórax anterior e região cefálica (testa/orelha)** permanece robusto e perfundido por muito mais tempo durante o choque.

> **Conclusão de Projeto:** O ponto ótimo de sensoriamento óptico para trauma não é o dedo, mas a **região central (esterno / tórax)**.

---

## 3. O Índice de Perfusão (PI) como Ferramenta Diagnóstica Antecipada

O Índice de Perfusão é calculado a partir da relação entre o componente de pulso pulsátil (AC) e a absorção estática dos tecidos não pulsáteis (DC):

$$\text{PI} = \frac{\text{Componente AC}}{\text{Componente DC}} \times 100\%$$

* **Comportamento Clínico:**
  * Em repouso normal: $\text{PI} > 1.5\%$.
  * Início de perda volêmica / vasoconstrição: O $\text{PI}$ cai vertiginosamente para valores abaixo de $0.6\%$, **minutos ou horas antes de a Pressão Arterial Sistêmica desabar**.
  * No APH, monitorar o declínio da tendência do PI permite ao socorrista iniciar reposição volêmica ou infusão antes da parada cardiorrespiratória por choque descompensado.

---

## 4. O Protocolo de Triagem START Integrado ao Dispositivo

O algoritmo embarcado deve alimentar automaticamente o anel de LEDs de triagem START (*Simple Triage and Rapid Treatment*):

| Cor do LED | Classificação START | Critérios Fisiológicos Automáticos |
| :---: | :---: | :--- |
| **VERMELHO** | Imediato (Prioridade 1) | FR $> 30$ irpm ou $< 10$ irpm; ausência de pulso radial / PI $< 0.4\%$; $SpO_2 < 85\%$. |
| **AMARELO** | Urgente (Prioridade 2) | FR entre 10 e 29 irpm; pulso presente e estável; sem sinais de hipóxia imediata. |
| **VERDE** | Menor Gravidade (Prioridade 3) | Sinais vitais dentro dos limites normais de repouso ($SpO_2 > 95\%$, FC entre 60 e 100 bpm). |
| **PRETO** | Expectante / Óbito | Ausência sustentada de sinal cardíaco elétrico (ECG em assistolia) e ausência de frequência respiratória após desobstrução. |
