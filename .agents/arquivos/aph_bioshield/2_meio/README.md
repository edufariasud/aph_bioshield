# APH-BioShield™ | Dispositivo Móvel de Telemetria e Triagem para APH

Este pacote contém o projeto completo do dispositivo médico biométrico sem fio **APH-BioShield™**, desenvolvido para monitoramento ininterrupto de trauma desde o local do acidente até o hospital.

---

## 🚀 Como Abrir e Usar

### Opção 1: Direto no Navegador (Mais Rápido)
1. Dê um **duplo clique no arquivo `INICIAR_PROJETO.bat`** (ele abrirá automaticamente no seu navegador padrão); **ou**
2. Dê um **duplo clique direto no arquivo `index.html`**.

### Opção 2: Servidor Local (Opcional)
Se você tiver Python instalado neste computador:
```bash
python -m http.server 8080
```
E acesse `http://localhost:8080` no navegador.

---

## 📁 Estrutura de Arquivos Inclusa no Pacote

* **`index.html`** - Interface principal com o estúdio 3D, painel de sinais vitais e controles de visualização.
* **`style.css`** - Folha de estilos completa com tema escuro médico, glassmorphism e traçados em tempo real.
* **`app.js`** - Motor 3D em Three.js com as 8 camadas interativas, controle de explosão, detecção de choque e gerador de traçados de ECG e PPG.
* **`DOSSIE_TECNICO_APH.md`** - Documentação clínica e de engenharia detalhando a física e matemática de cada parâmetro (PA por PAT, Volume Sanguíneo/PVI, ECG, Temperatura, etc.).
* **`INICIAR_PROJETO.bat`** - Script executável de 1 clique para iniciar o projeto no Windows.
* **`assets/`**
  * `aph_device_render.jpg` - Render industrial em alta definição do produto (visão superior e inferior).
  * `aph_exploded_view.jpg` - Diagrama de engenharia CAD em vista explodida de todas as camadas.
* **`libs/`** - Bibliotecas Three.js e OrbitControls para funcionamento autônomo.

---

## 🎛️ Recursos do Estúdio 3D
1. **Manipulação 3D:** Clique e arraste para girar; use o scroll para aproximar/afastar; clique com o botão direito para arrastar.
2. **Vista Explodida (0 a 100%):** Mova o slider superior para ver todas as peças mecânicas e eletrônicas flutuando no espaço.
3. **Modo Raio-X:** Alterne para tornar a carcaça translúcida e ver a bateria e chips internos.
4. **Inspeção de Peças:** Clique em qualquer componente (na tela 3D ou na lista à direita) para ler sua especificação técnica.
5. **Simulador de Cenários Clínicos:** Alterne entre *Hemorragia Oculta*, *Vítima Estável*, *Choque Descompensado* e *PCR* para ver os traçados de ECG/PPG e os parâmetros mudarem em tempo real.
