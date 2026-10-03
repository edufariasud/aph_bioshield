---
tipo: moc
area: engenharia_biomedica
tags: [aph, bioshield, ppg, ecg, sinais_vitais, trauma, start, hardware, literatura]
status: ativo
data: 2026-10-03
aliases: [MOC APH-BioShield, MOC Biomédica APH]
relacionados: ["[[00_HUB_CENTRAL]]"]
---

# 🩺 MOC — APH-BioShield™ & Engenharia Biomédica de Emergência

Este Mapa de Conteúdo (MOC) centraliza os conceitos biomédicos, modelos de hardware/circuitos, algoritmos de processamento digital de sinais (DSP) e referências de literatura científica que sustentam a arquitetura e a publicação de artigos sobre o **APH-BioShield™**.

---

## 🫀 1. Eletrofisiologia & Ritmo Cardíaco
* [[c_pan_tompkins_ecg|Algoritmo Pan-Tompkins para Detecção em Tempo Real do Complexo QRS]]: Pipeline digital de filtragem passa-faixa, derivada e integração para captura de FC mesmo com eletrodos de vetor curto.

---

## 🩸 2. Hemodinâmica Óptica & Monitoramento de Choque
* [[c_indice_perfusao_choque|Índice de Perfusão (PI) & Detecção Precoce de Choque Hipovolêmico]]: Princípio fisiológico da razão AC/DC do PPG por reflexão e antecipação de colapso circulatório.
* [[c_pulse_arrival_time_pat|Pulse Arrival Time (PAT) & Limites da Pressão Arterial Sem Manguito]]: Correlação matemática entre atraso elétrico-mecânico do pulso e rigidez arterial, seus potenciais e desvios no trauma.

---

## 🫁 3. Ventilação & Respiração Indireta
* [[c_respiracao_derivada_ppg|Extração da Frequência Respiratória via Modulações da Onda PPG (EDR / RIAV / RIIV)]]: Como extrair a frequência respiratória indiretamente a partir do envelope e da linha de base do fotopletismograma sem sensores mecânicos extras.

---

## 📚 4. Literatura Científica & Estado da Arte (Base para Artigo Científico)

### A. Montagem, Hardware de Baixo Custo & Circuitos Integrados
* [[2025-07-01_filgueiras_low_cost_wearable_sensors_nrf52840|Filgueiras et al. (Micromachines, 2025) — Evaluating the Accuracy of Low-Cost Wearable Sensors]]
  * *Validação direta do nosso exato hardware stack (nRF52840 + MAX30102 + temperatura) com acurácia metrológica hospitalar comprovada.*
* [[2026-07-15_alkhoury_tinzr_compact_wireless_multimodal_platform|Alkhoury et al. (HardwareX, 2026) — TinZr: Compact Wireless Multimodal Platform]]
  * *Padrão de engenharia aberta para layout de PCB de 4 camadas (18x22mm), separação de AGND/DGND e gestão LiPo para sensores fisiológicos.*
* [[2026-05-25_rathnayake_ecg_ppg_multimodal_fusion_review|Rathnayake et al. (Sensors, 2026) — Wearable Multimodal Fusion Systems Based on ECG and PPG]]
  * *Topologias de circuito analógico misto (biopotencial + óptico) e cancelamento cruzado de ruído mecânico.*
* [[2026-08-24_contact_pressure_reflectance_ppg_review|Castaneda et al. (J Med Syst, 2026) — Mechanical Contact Conditions in Wearable Reflectance PPG]]
  * *Geometria de encapsulamento com domo de 0.8 mm e faixa de pressão mecânica ótima (20 a 40 mmHg).*

### B. Projetos Semelhantes, APH & Impacto Clínico
* [[2026-03-15_markel_prehospital_monitoring_systems_advances|Markel et al. (West J Emerg Med, 2026) — Advances in Patient Monitoring Systems for Prehospital Settings]]
  * *Revisão crítica dos benchmarks mundiais em APH (Athena GTX, Vitaliti, LifeSignals) e justificativa para dispositivos sem fio de baixo custo.*
* [[2026-04-10_gonzalez_wearable_ppg_hemorrhage_compensatory_reserve|Gonzalez et al. (Sensors, 2026) — Wearable PPG for Compensatory Reserve in Simulated Human Hemorrhage]]
  * *Demonstração empírica militar (LBNP) de que o PPG de reflexão rastreia a perda de sangue antes da queda de pressão arterial.*
* [[2025-08-20_rrmoku_wearables_emergency_department_monitoring|Rrmoku (Cureus, 2025) — Reducing Emergency Department Strain Through Usable Wearables]]
  * *Impacto hospitalar e pré-hospitalar: redução do tempo de resposta médica de 52 min para 4 min e economia de 30% da carga da equipe.*
* [[2026-09-07_sensors_chest_reflectance_ppg_spo2|Kim et al. (Sensors, 2026) — Real-Time SpO2 from Chest Reflectance Photoplethysmography]]
  * *Oximetria em tempo real diretamente no esterno com calibração clínica contra gasometria arterial SaO2.*
* [[2026-07-21_kalathingal_perfusion_index_shock_resuscitation|Kalathingal et al. (Cureus, 2026) — Comparative Evaluation of Perfusion Index in Traumatic Shock]]
  * *Correlação direta entre Índice de Perfusão (PI < 0.6%) e lactato no choque na sala de emergência.*
* [[2026-08-20_deng_ppg_morphology_hemorrhagic_shock|Deng et al. (AICOJ, 2026) — Visual PPG Morphology Scoring for Risk Stratification in Hemorrhage]]
  * *Aceleração do fotopletismograma (APPG) e colapso da onda dícrota como biomarcador de intervenção cirúrgica.*
* [[2026-09-01_wearable_dry_electrode_ecg_platform|Schmidt et al. (Sensors, 2026) — Interval-Level Validation of Wearable Dry-Electrode ECG]]
  * *Uso de botões secos em aço cirúrgico 316L com espaçamento de 60 mm e fidelidade de 99.2% nos intervalos RR.*

### C. Livros e Tratados de Referência Fundamental (Biblioteca Local)
* [[livro_sazonov_wearable_sensors|Sazonov & Neuman (Elsevier) — Wearable Sensors: Fundamentals, Implementation and Applications]]
  * *Fundamentos de biopotenciais com eletrodos secos capacitivos, interface ótica com a pele e gestão ultra-eficiente de bateria LiPo.*
* [[livro_kyriacou_photoplethysmography|Kyriacou & Allen (Elsevier, 2021) — Photoplethysmography: Technology, Signal Analysis and Applications]]
  * *O tratado definitivo sobre física óptica de tecidos, extração de PI/PVI, oximetria de reflexão, estimativa de PAT/PTT e frequência respiratória.*
* [[livro_webster_medical_instrumentation|Webster & Nimunkar (Wiley, 5ª ed 2021) — Medical Instrumentation: Application and Design]]
  * *Normas de isolamento elétrico e segurança do paciente (IEC 60601-1), amplificadores de instrumentação com alto CMRR e termometria IR.*
* [[livro_rangayyan_biomedical_signal_analysis|Rangayyan & Krishnan (IEEE/Wiley, 3ª ed 2024) — Biomedical Signal Analysis]]
  * *Modelagem matemática de ruídos biológicos, algoritmos Pan-Tompkins para Cortex-M4 e filtros digitais de tempo real sem distorção.*

