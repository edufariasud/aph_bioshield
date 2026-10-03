---
tipo: literatura
area: engenharia_biomedica
tags:
  - literatura
  - paper
  - ppg_reflexao
  - pressao_de_contato
  - optica
  - encapsulamento
  - aph
autores: ["Castaneda et al.", "Espina et al."]
fonte: "Journal of Medical Systems / Springer-Nature, Agosto de 2026"
ano: 2026
data: 2026-10-03
status: fichado
doi: "10.1007/s10916-026-02110-4"
conceitos_relacionados:
  - "[[c_indice_perfusao_choque]]"
  - "[[c_respiracao_derivada_ppg]]"
moc: "[[moc_aph_bioshield]]"
---

# 📑 Fichamento: Mechanical Contact Conditions in Wearable Reflectance Photoplethysmography: Scoping Review

## 📌 Metadados da Fonte
- **Título Original:** Mechanical Contact Conditions in Wearable Reflectance Photoplethysmography: Scoping Review
- **Publicação:** *Journal of Medical Systems / Springer-Nature*, Agosto de 2026.
- **Identificadores:** DOI: 10.1007/s10916-026-02110-4 | PMCID: PMC13550977 | PMID: 42702110
- **Arquivo Local Bruto:** `artigos/pmc13550977_contact_pressure_reflectance_ppg.xml`

---

## 🎯 Tese Central
A pressão mecânica de acoplamento entre o sensor óptico (PPG de reflexão) e a derme humana é a variável externa mais crítica na determinação da amplitude do pulso e da relação sinal-ruído (SNR). Pressão mecânica insuficiente ($< 10\text{ mmHg}$) gera reflexão parasita direta de ar e satura o fotodiodo; por outro lado, pressão excessiva ($> 60\text{ mmHg}$) oclui fisicamente o leito capilar e oblitera a onda pulsátil. A faixa ótima de pressão de contato para tórax e membros situa-se entre **$20\text{ mmHg}$ e $40\text{ mmHg}$**.

---

## 🔬 Metodologia & Evidências Empíricas
* **Revisão Sistemática & Metanálise:** Análise de 84 estudos empíricos medindo a variação da amplitude AC e estabilidade do DC do PPG sob diferentes forças mecânicas e geometrias de lentes ópticas.
* **Morfologia Óptica Ideal:**
  * Domos ópticos convexos ligeiramente protuberantes ($0.5\text{ mm}$ a $1.0\text{ mm}$ além da carcaça) melhoram o contato com os tecidos e aumentam a penetração de fótons sem exigir aperto excessivo da fita de fixação.
  * O uso de uma barreira opaca física entre os LEDs emissores e o fotodetector (barreira de isolamento óptico interno) reduz o *crosstalk* óptico em até $85\%$.

---

## 🚑 Aplicação Prática no APH-BioShield™
1. **Design Mecânico do Chassi (Case 3D na Fase 2/3):**
   * A janela óptica do MAX30102 não deve ficar afundada na carcaça plástica, mas sim ter uma leve saliência de $0.8\text{ mm}$ para garantir que a fita adesiva exerça a pressão ótima ($20\text{--}40\text{ mmHg}$) contra a pele do tórax.
   * Deve ser incluída uma pequena barreira preta de silicone ou resina opaca entre o LED e o fotodiodo do módulo CJMCU-30102 para evitar saturação direta da luz vermelha/IR no sensor.
2. **Garantia de Leitura no Choque:** Se o socorrista colar o patch frouxo no tórax, o sinal parecerá ausente (falsa assistolia óptica). O manual de operação e a rigidez do adesivo devem assegurar o assentamento mecânico imediato.

---

## 🔗 Conexões no Grafo
* **Conceitos Alimentados:** [[c_indice_perfusao_choque]], [[c_respiracao_derivada_ppg]]
* **MOC Central:** [[moc_aph_bioshield]]
