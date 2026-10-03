---
tipo: conceito
area: engenharia_biomedica
tags: [pat, ptt, pressao_arterial, cuffless_bp, hemodinamica, aph]
status: consolidado
data: 2026-10-03
aliases: [PAT, Pulse Arrival Time, PTT, Pressão Sem Manguito]
fontes: ["Mukkamala et al. (2015)", "Finnegan et al. (2021)"]
relacionados: ["[[moc_aph_bioshield]]", "[[c_pan_tompkins_ecg]]", "[[c_indice_perfusao_choque]]"]
---

# ⏱️ Pulse Arrival Time (PAT) & Limites da Pressão Arterial Sem Manguito

O **Pulse Arrival Time (PAT)** é o atraso temporal entre a despolarização elétrica ventricular (pico R no ECG) e o momento em que a onda de pulso de sangue atinge um leito capilar periférico (sensor óptico PPG).

---

## 🔬 1. Relação com o PTT e Fisiologia

$$\text{PAT} = \text{PEP} + \text{PTT}$$

* **PEP (*Pre-Ejection Period*):** Tempo eletromecânico que o miocárdio leva para se contrair e abrir as valvas aórticas após o estímulo elétrico.
* **PTT (*Pulse Transit Time*):** Tempo real de viagem da onda de pressão pelo leito arterial.

De acordo com a equação de Moens-Korteweg, a velocidade da onda de pulso ($PWV = \frac{\text{Distância}}{\text{PTT}}$) é proporcional à raiz quadrada da rigidez da parede arterial e da pressão transmural:
* $\uparrow$ Pressão Arterial $\rightarrow \uparrow$ Rigidez Arterial $\rightarrow \uparrow PWV \rightarrow \downarrow \text{PAT}$ (o pulso chega mais rápido).
* $\downarrow$ Pressão Arterial $\rightarrow \downarrow PWV \rightarrow \uparrow \text{PAT}$ (o pulso demora mais para chegar).

---

## ⚠️ 2. A Limitação Clínica no APH

No paciente de trauma em choque hipovolêmico ou sob dor extrema:
1. O PEP varia de forma imprevisível devido à ativação adrenérgica inotrópica.
2. A vasoconstrição simpática enrijece a parede muscular das artérias periféricas mesmo com volume intravascular reduzido.
3. Isso pode fazer com que o PAT diminua (simulando pressão normal ou alta) enquanto a pressão sistêmica real em mmHg está desabando.

> **Diretriz de Engenharia para o APH-BioShield:** O PAT não deve ser apresentado como medida absoluta de mmHg. Ele deve operar como **marcador de tendência de instabilidade vascular** e ser cruzado com a queda do Índice de Perfusão (PI).
