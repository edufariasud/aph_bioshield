---
tipo: literatura
area: engenharia_biomedica
tags:
  - literatura
  - paper
  - perfusao
  - choque_traumatico
  - aph
  - reanimacao
  - lactato
autores: ["Kalathingal et al.", "Dhanapal et al."]
fonte: "Cureus, 18(7):e113061"
ano: 2026
data: 2026-10-03
status: fichado
doi: "10.7759/cureus.113061"
conceitos_relacionados:
  - "[[c_indice_perfusao_choque]]"
  - "[[c_pulse_arrival_time_pat]]"
moc: "[[moc_aph_bioshield]]"
---

# 📑 Fichamento: Comparative Evaluation of Perfusion Index With Lactate and Base Deficit for Assessing Resuscitation Response in Traumatic Shock

## 📌 Metadados da Fonte
- **Título Original:** Comparative Evaluation of Perfusion Index With Lactate and Base Deficit for Assessing Resuscitation Response in Traumatic Shock Patients Not Requiring Blood Transfusion in the Emergency Department
- **Publicação:** *Cureus Journal of Medical Science*, Julho de 2026.
- **Identificadores:** DOI: 10.7759/cureus.113061 | PMCID: PMC13492250 | PMID: 42626319
- **Arquivo Local Bruto:** `artigos/pmc13492250_perfusion_index_shock_resuscitation.xml`

---

## 🎯 Tese Central
O monitoramento contínuo e não-invasivo do **Índice de Perfusão (PI)** derivado da fotopletismografia correlaciona-se de forma direta com marcadores invasivos clássicos de hipóxia celular e metabolismo anaeróbio (lactato sérico e déficit de base) em pacientes com choque traumático na sala de emergência. A evolução do PI fornece uma resposta dinâmica aos esforços de reposição volêmica muito mais rápida do que a pressão arterial sistêmica (PA), confirmando seu papel de biomarcador precoce de perfusão em tempo real.

---

## 🔬 Metodologia & Evidências Empíricas
* **Coorte Clínica:** 120 pacientes adultos vítimas de trauma admitidos com sinais clínicos de choque hemorrágico/traumático.
* **Métricas Aferidas:** Índice de Perfusão (PI) contínuo no momento da admissão ($T_0$), após 1 hora ($T_1$) e após 4 horas de ressuscitação fluídica ($T_4$), correlacionados com dosagens de lactato arterial e gasometria.
* **Resultados Principais:**
  * Pacientes que responderam à reanimação apresentaram elevação estatisticamente significativa do PI (média basal de $0.54 \pm 0.21\%$ subindo para $> 1.45 \pm 0.38\%$).
  * A correlação negativa entre PI e níveis de lactato foi de $r = -0.68$ ($p < 0.001$), provando que quanto menor o PI, maior o sofrimento isquêmico celular.
  * O ponto de corte de $\text{PI} < 0.6\%$ apresentou sensibilidade de $88.5\%$ e especificidade de $82.1\%$ para identificação de choque clinicamente relevante.

---

## 🚑 Aplicação Prática no APH-BioShield™
1. **Regra de Decisão do Firmware para Alerta de Choque:**
   * $\text{PI} < 0.6\%$: Estado crítico de hipoperfusão sistêmica. Aciona LED Vermelho no anel START e telemetria de alerta de urgência imediata.
   * $0.6\% \le \text{PI} < 1.2\%$: Zona de alerta (choque moderado / vasoconstrição).
   * $\text{PI} \ge 1.4\%$: Perfusão satisfatória.
2. **Monitoramento da Reposição Volêmica em Trânsito:** Permite que a equipe do SAMU/Resgate monitore se o soro fisiológico ou plasma infundido durante o trajeto da ambulância está de fato restaurando a microcirculação periférica antes de chegar ao hospital.

---

## 🔗 Conexões no Grafo
* **Conceitos Alimentados:** [[c_indice_perfusao_choque]], [[c_pulse_arrival_time_pat]]
* **MOC Central:** [[moc_aph_bioshield]]
