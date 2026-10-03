---
tipo: conceito
area: engenharia_biomedica
tags: [ecg, pan_tompkins, dsp, qrs, frequencia_cardiaca, algoritmo]
status: consolidado
data: 2026-10-03
aliases: [Algoritmo Pan-Tompkins, Detecção QRS, Filtro QRS]
fontes: ["Pan & Tompkins (1985)"]
relacionados: ["[[moc_aph_bioshield]]"]
---

# 🫀 Algoritmo Pan-Tompkins para Detecção de QRS em Tempo Real

O algoritmo proposto por Jiapu Pan e Willis J. Tompkins em 1985 é o padrão da indústria para detecção confiável do complexo QRS em eletrocardiogramas sob condições de ruído e baixa amplitude.

---

## ⚙️ 1. O Pipeline Matemático

O processamento digital opera em 5 estágios consecutivos de baixa complexidade computacional (ideal para Cortex-M4):

1. **Filtro Passa-Faixa (5 Hz a 15 Hz):** Combinação de filtro passa-baixas e passa-altas para eliminar ruído de linha (50/60 Hz), contrações musculares de alta frequência e oscilação da linha de base causada pela respiração.
2. **Derivada:** Destaca a inclinação acentuada do complexo QRS em relação às ondas P e T.
3. **Elevação ao Quadrado ($y[n] = x[n]^2$):** Torna todos os valores positivos e amplifica de forma não-linear os picos de maior amplitude.
4. **Integração em Janela Móvel:** Suaviza o pulso derivado, gerando uma onda retangular cuja largura reflete a duração do QRS.
5. **Limiar Adaptativo Duplo:** Dois limiares móveis que se ajustam automaticamente à amplitude média do sinal e ao ruído de fundo, evitando falsos positivos.

---

## 🚑 2. Aplicação no APH-BioShield

* Com eletrodos secos no esterno espaçados por curta distância, a amplitude do QRS é atenuada.
* A derivada e quadratura do Pan-Tompkins permitem isolar o instante exato do pico R com precisão de milissegundos, fundamental tanto para a Frequência Cardíaca (FC) quanto para o cálculo do *Pulse Arrival Time* (PAT).
