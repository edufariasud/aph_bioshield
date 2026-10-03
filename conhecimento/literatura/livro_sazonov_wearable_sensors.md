---
tipo: literatura
area: engenharia_biomedica
tags:
  - literatura
  - livro
  - sensores_vestiveis
  - biopotenciais
  - ecg
  - ppg
  - gestao_energia
  - artefatos_movimento
autores: ["Edward Sazonov", "Michael R. Neuman"]
fonte: "Wearable Sensors: Fundamentals, Implementation and Applications (Academic Press / Elsevier, 2015/2020)"
ano: 2020
data: 2026-10-03
status: fichado
conceitos_relacionados:
  - "[[c_pulse_arrival_time_pat]]"
  - "[[c_indice_perfusao_choque]]"
  - "[[c_filtros_biomedicos_embarcados]]"
moc: "[[moc_aph_bioshield]]"
---

# 📑 Fichamento: Wearable Sensors — Fundamentals, Implementation and Applications

## 📌 Metadados da Fonte
- **Título Original:** Wearable Sensors: Fundamentals, Implementation and Applications
- **Editores/Autores Principais:** Edward Sazonov, Michael R. Neuman
- **Publicação:** Academic Press / Elsevier (2ª Edição)
- **Formato Local:** `livros/Edward Sazonov_ Michael R Neuman - Wearable sensors _ fundamentals, implementation and applications (2015, Academic Press, , Else.epub` (16.61 MB)

---

## 🎯 Tese Central
A obra consolida a transição dos sistemas diagnósticos hospitalares para plataformas vestíveis discretas e energeticamente autônomas. Estabelece a física e a engenharia necessárias para interfacear transdutores mecânicos, eletroquímicos e ópticos com a pele humana viva, quantificando as não-linearidades de impedância da interface eletrodo-pele, mecanismos de acoplamento óptico em tecidos periféricos e técnicas de mitigação ativa de artefatos de movimento (MAs).

---

## 🔬 Fundamentos Críticos para o APH-BioShield™

### 1. Interface Eletrodo-Pele e Biopotenciais de Contato Seco
* **Modelo Elétrico de Eletrodo Seco:** Diferente dos eletrodos Ag/AgCl com gel eletrolítico (onde a impedância de contato é baixa e dominada por condução iônica), os eletrodos metálicos secos (aço inoxidável, cobre banhado a ouro, têxteis condutivos) estabelecem uma interface capacitiva de alta impedância ($> 1\text{ M}\Omega$ em baixas frequências).
* **Mitigação de Offset e Ruído Mioelétrico:** A impedância elevada exige que o estágio frontal (AFE) possua impedância de entrada ultra-alta ($> 100\text{ M}\Omega$ a $1\text{ G}\Omega$) e rejeição de modo comum (CMRR) acima de $80\text{ dB}$ para suprimir a interferência de $60\text{ Hz}$ da rede elétrica sem necessidade de eletrodo de perna direita acionada (DRL) de três pontos.

### 2. Transdução Fotopletismográfica (PPG) em Dispositivos Vestíveis
* **Mecânica de Acoplamento:** A luz refletida capturada pelo fotodiodo é altamente dependente da pressão de contato aplicada sobre o tecido. Pressão insuficiente causa ruído por descolamento óptico; pressão excessiva oclui o leito microvascular dérmico, colapsando a amplitude do pulso pulsátil (componente AC).
* **Comprimentos de Onda e Profundidade de Penetração:** A luz verde ($~530\text{ nm}$) interage com o leito capilar superficial e apresenta maior imunidade a artefatos de movimento; já o infravermelho ($880\text{--}940\text{ nm}$) e vermelho ($660\text{ nm}$) penetram mais profundamente nos leitos arteriolares, permitindo estimar a saturação de oxigênio ($SpO_2$) e tempos de trânsito de pulso (PAT/PTT).

### 3. Arquitetura de Baixo Consumo e Gestão de Bateria
* **Duty-Cycling de Sensores:** Em monitores vestíveis contínuos, os emissores de luz (LEDs) respondem por até $70\text{--}85\%$ do consumo de energia. O livro demonstra que a redução do ciclo de trabalho (duty-cycle) com rajadas de pulso óptico estreitas ($100\text{--}400\text{ }\mu\text{s}$) e ativação periódica permite estender a autonomia da bateria LiPo de horas para múltiplos dias.
* **Co-processamento no Microcontrolador:** Descarga de processamento simples para núcleos de ultrabaixo consumo e transmissão BLE estruturada em pacotes compactos (evitando envio de dados brutos ponto a ponto continuamente).

---

## 🚑 Aplicações Práticas no Firmware e Hardware do APH-BioShield™
1. **Dimensionamento dos Eletrodos de ECG:** Utilizar contatos metálicos planos ou ligeiramente convexos com acabamento em banho de ouro para evitar passivação oxidativa e manter impedância estável em pele desidratada ou sudoreica de vítimas de trauma.
2. **Duty-Cycling do MAX30102:** Configurar o driver com amostragem a $100\text{ Hz}$, largura de pulso $215\text{--}411\text{ }\mu\text{s}$ e corrente de LED calibrada dinamicamente para manter o componente DC dentro de $50\text{--}70\%$ do fundo de escala do ADC de 18 bits.
3. **Fusão Acelerômetro + PPG:** Utilizar sensor inercial para rotular instantes com aceleração $> 0.2\text{ g}$ como janelas corrompidas, congelando a estimativa de frequência cardíaca até a estabilização do sinal.

---

## 🔗 Conexões no Grafo do Conhecimento
- **Conceitos Alimentados:**
  - [[c_filtros_biomedicos_embarcados]]
  - [[c_pulse_arrival_time_pat]]
  - [[c_indice_perfusao_choque]]
- **MOC Central:** [[moc_aph_bioshield]]
