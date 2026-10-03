---
tipo: literatura
area: engenharia_biomedica
tags:
  - literatura
  - paper
  - ppg
  - choque_hemorragico
  - reserva_compensatoria
  - trauma
  - lbnp
autores: ["Gonzalez Jose M.", "Ortiz Ryan", "Amezcua Krysta-Lynn", "Bedolla Carlos"]
fonte: "Sensors (Basel), 26(8):2513"
ano: 2026
data: 2026-10-03
status: fichado
doi: "10.3390/s26082513"
conceitos_relacionados:
  - "[[c_indice_perfusao_choque]]"
  - "[[c_pulse_arrival_time_pat]]"
moc: "[[moc_aph_bioshield]]"
---

# 📑 Fichamento: Validation of a Wearable Photoplethysmography-Based Sensor for Compensatory Reserve Measurement Monitoring in Simulated Human Hemorrhage

## 📌 Metadados da Fonte
- **Título Original:** Validation of a Wearable Photoplethysmography-Based Sensor for Compensatory Reserve Measurement Monitoring in Simulated Human Hemorrhage
- **Autores:** Jose M. Gonzalez, Ryan Ortiz, Krysta-Lynn Amezcua, Carlos Bedolla et al. (US Army Institute of Surgical Research / Medical Research)
- **Publicação:** *Sensors (Basel)*, Abril de 2026.
- **Identificadores:** DOI: 10.3390/s26082513 | PMCID: PMC13120294 | PMID: 42076622
- **Arquivo Local Bruto:** `artigos/pmc13120294_wearable_ppg_hemorrhage_compensatory_reserve.xml`

---

## 🎯 Tese Central
Durante hemorragias agudas, o corpo humano aciona mecanismos fisiológicos compensatórios reflexos que mantêm a pressão arterial e a oxigenação estáveis até que cerca de 30% a 40% do volume intravascular seja perdido, momento em que ocorre o colapso hemodinâmico repentino. Este estudo valida experimentalmente que sensores vestíveis baseados em **fotopletismografia (PPG)** conseguem rastrear a exaustão da **Reserva Compensatória (CRI - Compensatory Reserve Index)** em tempo real através da análise morfológica do pulso arterial, detectando o choque hemorrágico iminente muito antes dos sinais vitais clássicos sofrerem alterações.

---

## 🔬 Metodologia & Evidências Empíricas
* **Modelo Experimental:** Protocolo de Pressão Negativa nos Membros Inferiores (LBNP - *Lower Body Negative Pressure*), o padrão-ouro de simulação fisiológica de perda sanguínea aguda e choque hemorrágico progressivo em humanos sem lesão física.
* **Dispositivo Testado:** Patch epidérmico vestível sem fio (*Epicore Patch*) com fotopletismografia multiespectral por reflexão.
* **Achados Chave:**
  * O sensor vestível atingiu concordância superior a $98.5\%$ com monitores hospitalares padrão-ouro invasivos na curva de esgotamento volêmico.
  * O sinal de PPG permitiu calcular o declínio linear da reserva compensatória de $1.0$ (reserva intacta) até $< 0.2$ (choque descompensado/síncope iminente).
  * A colocação anatômica central demonstrou resistência muito superior a variações de temperatura em comparação à colocação em dedos.

---

## 🚑 Aplicação Direta no APH-BioShield™ & Impacto para Artigo Científico
1. **Fundamentação da "Detecção de Hemorragia Oculta":** Responde diretamente à pergunta que você e a Duda discutiram sobre *"detectar volume sanguíneo em caso de hemorragia interna/externa"*. O paper prova que a curva PPG por reflexão é o padrão militar e científico para detectar hemorragia antes da pressão cair.
2. **Algoritmo de Compensatory Reserve para o Firmware:** Em vez de monitorar apenas se o paciente está vivo ou morto, o algoritmo do APH-BioShield pode gerar um medidor numérico ou gráfico de "Reserva Volêmica Restante", essencial para triagem de múltiplas vítimas em acidentes graves.

---

## 🔗 Conexões no Grafo
* **Conceitos Alimentados:** [[c_indice_perfusao_choque]], [[c_pulse_arrival_time_pat]]
* **MOC Central:** [[moc_aph_bioshield]]
