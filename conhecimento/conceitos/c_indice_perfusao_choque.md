---
tipo: conceito
area: engenharia_biomedica
tags: [perfusao, choque_hipovolemico, ppg, trauma, aph]
status: consolidado
data: 2026-10-03
aliases: [Índice de Perfusão, Perfusion Index, PI no Choque]
fontes: ["Lima & Bakker (2005)", "Convertino et al. (2020)"]
relacionados: ["[[moc_aph_bioshield]]", "[[c_pulse_arrival_time_pat]]"]
---

# 🩸 Índice de Perfusão (PI) & Detecção Precoce de Choque no APH

O **Índice de Perfusão (PI - Perfusion Index)** é a relação numérica entre o componente pulsátil (arterial) e o componente não pulsátil (tecido, músculo, osso e sangue venoso) de um sinal de fotopletismografia (PPG).

---

## 📐 1. Formulação Matemática

$$\text{PI} = \frac{\text{Componente AC}}{\text{Componente DC}} \times 100\%$$

* **Componente AC (Pulsátil):** Modulação óptica gerada pela expansão sistólica dos vasos arteriais a cada batimento cardíaco.
* **Componente DC (Estático):** Nível de absorção constante de luz pelos tecidos circundantes, pele e sangue estático.

---

## 🚨 2. Fisiopatologia no Choque Hemorrágico

1. **Janela Silenciosa de Choque Compensado:** Em perdas de até 20–30% da volemia, a frequência cardíaca aumenta e a vasoconstrição simpática fecha o leito periférico, mantendo a Pressão Arterial Sistêmica (PA) dentro de faixas normais.
2. **Queda do PI:** Como a vasoconstrição reduz o volume arterial pulsátil periférico, o componente AC encolhe dramaticamente.
3. **Alerta Precoce:** O $\text{PI}$ cai para valores abaixo de **$0.5\% - 0.6\%$** muito antes de o paciente apresentar hipotensão evidente (choque descompensado).

---

## 🛠️ 3. Aplicação no APH-BioShield

* O sensor MAX30102 colado no tórax calcula o PI a cada janela de 2 segundos.
* Se $\text{PI} < 0.5\%$, o sistema emite alerta imediato de hipoperfusão tecidual e aciona a classificação Vermelha na triagem START.
