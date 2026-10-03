---
tipo: conceito
area: engenharia_biomedica
tags: [respiracao, ppg, edr, frequencia_respiratoria, dsp, aph]
status: consolidado
data: 2026-10-03
aliases: [Frequência Respiratória por PPG, EDR, RIAV, RIIV]
fontes: ["Charlton et al. (2018)", "Reisner et al. (2008)"]
relacionados: ["[[moc_aph_bioshield]]"]
---

# 🫁 Frequência Respiratória Derivada de PPG (Extração Indireta)

A respiração espontânea induz alterações cíclicas na pressão intratorácica que modulam diretamente o enchimento cardíaco e a circulação periférica, imprimindo padrões identificáveis na onda de fotopletismografia (PPG).

---

## 🌊 1. As Três Modulações Respiratórias na Onda PPG

1. **RIAV (*Respiratory-Induced Amplitude Variation*):** A cada inspiração profunda, a pressão intratorácica negativa aumenta o retorno venoso para o ventrículo direito e reduz temporariamente o enchimento do ventrículo esquerdo, reduzindo a altura do pico sistólico do pulso periférico.
2. **RIIV (*Respiratory-Induced Intensity Variation*):** A variação de pressão mecânica intratorácica altera a drenagem do leito venoso, fazendo com que a linha de base (componente DC de baixa frequência) oscile no ritmo da respiração.
3. **RIFV (*Respiratory-Induced Frequency Variation*):** Arritmia sinusal respiratória (RSA) mediada pelo nervo vago — a frequência cardíaca acelera durante a inspiração e desacelera na expiração.

---

## 🛠️ 2. Algoritmo de Extração no Microcontrolador

1. Aplicação de filtro passa-faixa digital (0.1 Hz a 0.5 Hz, correspondendo a 6 a 30 respirações por minuto) na componente da linha de base do PPG.
2. Contagem de cruzamento por zero ou identificação do pico espectral dominante via FFT curta de 16 segundos.
3. Fusão com os dados inerciais do acelerômetro torácico para validação cruzada do movimento mecânico da caixa torácica.
