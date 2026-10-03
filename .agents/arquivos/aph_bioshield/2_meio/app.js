/**
 * ============================================================================
 * APH-BioShield 3D - Engine Three.js, Simulação Clínica e Controle de Hardware
 * ============================================================================
 */

// Estado Global da Aplicação
const state = {
  explodeRatio: 0,
  targetExplodeRatio: 0,
  isXray: false,
  autoRotate: true,
  currentScenario: 'hemorrhage',
  selectedPart: 'optics',
  formFactor: 'patch', // 'patch' ou 'wrist'
  vitals: {
    hr: 120,
    sbp: 88,
    dbp: 54,
    spo2: 93,
    rr: 26,
    temp: 35.4,
    pi: 0.3,
    pvi: 28,
    si: 1.36
  }
};

// Banco de Dados Técnico dos Componentes da "Receita" + Melhorias
const componentsData = {
  optics: {
    title: "Emissor & Receptor Óptico (Red 660nm + IR 880nm + Verde 525nm)",
    badge: "SENSOR FOTOPLETISMOGRÁFICO (PPG)",
    desc: "Cluster optoeletrônico integrado de alta intensidade. Responsável pela fotopletismografia de reflexão. Permite a extração de SpO2 arterial (relação R/IR), pulso contínuo, frequência respiratória e volume sanguíneo (Índice de Perfusão e PVI).",
    specs: {
      "Comprimentos de Onda": "660nm (Red) + 880nm (IR) + 525nm (Green)",
      "Taxa de Amostragem": "500 Hz a 1000 Hz",
      "Isolamento": "Barreira óptica física de silicone negro (anti-crosstalk)",
      "Parâmetros Extraídos": "SpO2, Pulso, FR, PVI, PI, PAT (Pressão)"
    }
  },
  electrodes: {
    title: "2 Eletrodos de Metal de Contato Seco (ECG)",
    badge: "SENSOR DE BIOPOTENCIAL CARDÍACO",
    desc: "Par de eletrodos em aço cirúrgico 316L com revestimento sinterizado Ag/AgCl de contato seco. Capturam a despolarização ventricular (onda P-QRS-T) através do vetor torácico esternal sem necessidade de gel líquido desidratante.",
    specs: {
      "Material": "Aço cirúrgico 316L sinterizado Ag/AgCl",
      "Distância Inter-eletrodos": "95 mm (otimizado para vetor esternal)",
      "Impedância de Entrada": "> 10 Gigaohms (AFE de ultra-baixo ruído)",
      "Detecção": "Arritmias, Taquicardias, Fibrilação e Pico R para PA"
    }
  },
  temp_sensor: {
    title: "Termômetro Infravermelho MEMS de Superfície",
    badge: "TERMOPILHA MÉDICA CALIBRADA",
    desc: "Sensor termopilha infravermelho sem contato mecânico direto (aperturado na pele). Mede a radiação infravermelha emitida pela pele sobre os vasos subclaviculares, convertendo-a em temperatura central calibrada em tempo real.",
    specs: {
      "Tecnologia": "Termopilha MEMS com lente de silício/germânio",
      "Faixa Operacional": "32.0°C a 43.0°C com precisão de ±0.1°C",
      "Compensação Térmica": "Sensor de temperatura ambiente integrado",
      "Alerta Clínico": "Detecção imediata de Hipotermia de Trauma (<35°C)"
    }
  },
  upper_casing: {
    title: "Carcaça Superior em Policarbonato Grau Médico IP67",
    badge: "CHASSIS ESTRUTURAL ROBUSTO",
    desc: "Estrutura em policarbonato com absorção de impacto nos cantos em elastômero laranja de alta visibilidade. Totalmente vedada (IP67) contra sangue, fluidos corporais, chuva torrencial e lavagem desinfetante.",
    specs: {
      "Material": "Policarbonato Makrolon® biocompatível (ISO 10993)",
      "Grau de Vedação": "IP67 (Submersível a 1m de água)",
      "Resistência Mecânica": "Quedas de até 2 metros em asfalto",
      "Ergonomia": "Passadores laterais para cinta rápida de resgate"
    }
  },
  display_triage: {
    title: "Display OLED de Alto Contraste + Anel de Triagem START",
    badge: "INTERFACE VISUAL DE CENA",
    desc: "Mostrador digital de resposta rápida legível sob luz solar direta e anel perimétrico de LEDs coloridos que pulsam na cor da triagem internacional (Vermelho: Imediato, Amarelo: Urgente, Verde: Leve, Preto: Expectante).",
    specs: {
      "Display": "Micro OLED monocromático de 0.96 polegadas",
      "Halo de Triagem": "Anel de 12 LEDs micro-RGB programáveis",
      "Visibilidade": "Até 30 metros de distância na cena do acidente",
      "Protocolo": "Triagem Automatizada por Algoritmo START / SALT"
    }
  },
  mainboard: {
    title: "Placa-Mãe Rígido-Flexível + Rádios BLE 5.3 & LoRa",
    badge: "PROCESSAMENTO & TELEMETRIA",
    desc: "Cérebro eletrônico do dispositivo. Conta com microcontrolador dual-core ARM Cortex-M4/M33, chip analógico AFE para biosinais de ultra-alta fidelidade, acelerômetro/giroscópio de 6 eixos e comunicação dupla: BLE de curto alcance e LoRa de 2 km.",
    specs: {
      "Processador": "Nordic nRF5340 Dual-Core 128MHz",
      "Telemetria Local": "Bluetooth 5.3 Low Energy (Tablet da ambulância)",
      "Telemetria Longa": "LoRa 915 MHz / Sub-GHz (Direto para o Hospital)",
      "IMU 6 Eixos": "Filtro de artefato de ambulância e guia de RCP"
    }
  },
  battery: {
    title: "Bateria LiPo Médica Ultra-fina com Carregamento Rápido",
    badge: "SISTEMA DE ENERGIA",
    desc: "Célula recarregável de polímero de lítio com invólucro de proteção médica. Fornece energia estável por até 18 horas de transmissão ininterrupta durante todo o trajeto de resgate e permanência na emergência.",
    specs: {
      "Capacidade": "3.7V 280mAh Li-Po ultra-fina",
      "Autonomia": "18 horas contínuas em modo telemetria ativa",
      "Carregamento": "Indução magnética Qi sem fios em 45 minutos",
      "Proteção": "Circuito integrado contra sobrecarga e curto-circuito"
    }
  },
  adhesive_base: {
    title: "Base Adesiva Hidrocoloide / Silicone Biocompatível",
    badge: "FIXAÇÃO ANATÔMICA ESTERNAL",
    desc: "Substrato adesivo médico hipoalergênico com película protetora de puxada rápida (3 segundos). Adere firmemente mesmo sobre pele com suor profuso, resíduos de sangue ou sujidade típica de traumas automobilísticos.",
    specs: {
      "Composição": "Adesivo hidrocoloide com orifícios transpirantes",
      "Tempo de Aplicação": "< 3 segundos (Ready-to-Stick)",
      "Tolerância Cutânea": "Sem maceração ou lesão em peles frágeis",
      "Remoção": "Puxada suave atraumática sem resíduos"
    }
  }
};

// Cenários Clínicos Pré-Configurados
const scenarios = {
  hemorrhage: {
    name: "Hemorragia Interna Oculta (Choque Inicial)",
    triage: "VERMELHO (IMEDIATO)",
    triageColor: "#ef4444",
    triageClass: "status-danger",
    vitals: { hr: 120, sbp: 88, dbp: 54, spo2: 93, rr: 26, temp: 35.4, pi: 0.3, pvi: 28, si: 1.36 },
    statuses: {
      bp: "Hipotensão por Sangramento",
      vol: "ALERTA: Perda de Volume Ativa",
      hr: "Taquicardia Compensatória",
      spo2: "Hipoxemia Moderada",
      rr: "Taquipneia",
      temp: "Hipotermia Leve de Trauma"
    }
  },
  normal: {
    name: "Vítima Estável (Trauma Leve)",
    triage: "VERDE (LEVE)",
    triageColor: "#10b981",
    triageClass: "status-safe",
    vitals: { hr: 74, sbp: 122, dbp: 78, spo2: 98, rr: 14, temp: 36.8, pi: 2.4, pvi: 11, si: 0.60 },
    statuses: {
      bp: "Normotenso",
      vol: "Volume Circulante Preservado",
      hr: "Ritmo Sinusal Regular",
      spo2: "Normoxemia",
      rr: "Eupneico",
      temp: "Normotérmico"
    }
  },
  critical: {
    name: "Choque Descompensado (Severo)",
    triage: "VERMELHO (CRÍTICO)",
    triageColor: "#ef4444",
    triageClass: "status-danger",
    vitals: { hr: 142, sbp: 62, dbp: 38, spo2: 84, rr: 34, temp: 34.2, pi: 0.1, pvi: 42, si: 2.29 },
    statuses: {
      bp: "Colapso Hemodinâmico",
      vol: "PERIGO: Choque Hipovolêmico Severo",
      hr: "Taquicardia Extrema",
      spo2: "Hipóxia Grave",
      rr: "Respiração Acidótica",
      temp: "Tríade Letal: Hipotermia Grave"
    }
  },
  arrest: {
    name: "Parada Cardiorrespiratória (PCR)",
    triage: "PRETO / AZUL (PCR REANIMAÇÃO)",
    triageColor: "#8b5cf6",
    triageClass: "status-danger",
    vitals: { hr: 0, sbp: 0, dbp: 0, spo2: 0, rr: 0, temp: 33.8, pi: 0.0, pvi: 0, si: 0 },
    statuses: {
      bp: "Sem Pulso Detectável",
      vol: "Parada Circulatória",
      hr: "Assistolia / Fibrilação Ventricular",
      spo2: "Sem Sinal de Oximetria",
      rr: "Apneia",
      temp: "Hipotermia"
    }
  }
};

/* ============================================================================
   3D ENGINE (THREE.JS)
   ============================================================================ */
let scene, camera, renderer, controls;
let mainGroup, layers = {};
let raycaster, mouse;
let highlightedMesh = null;
let container3D;

function init3D() {
  container3D = document.getElementById('three-container');
  const width = container3D.clientWidth;
  const height = container3D.clientHeight;

  // Cena
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x0a0e17);
  scene.fog = new THREE.FogExp2(0x0a0e17, 0.035);

  // Câmera
  camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100);
  camera.position.set(0, 7.5, 11);

  // Renderer
  renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: "high-performance" });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.15;
  container3D.appendChild(renderer.domElement);

  // OrbitControls
  controls = new THREE.OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.06;
  controls.minDistance = 3.5;
  controls.maxDistance = 22;
  controls.maxPolarAngle = Math.PI / 2 + 0.15;
  controls.target.set(0, 0, 0);

  // Iluminação de Estúdio Industrial
  setupLights();

  // Grid e Chão Tecnológico
  setupEnvironment();

  // Construir o Modelo 3D com Todas as Camadas da "Receita"
  buildAPHDeviceModel();

  // Raycaster para Seleção com o Mouse
  raycaster = new THREE.Raycaster();
  mouse = new THREE.Vector2();

  // Event Listeners
  window.addEventListener('resize', onWindowResize);
  renderer.domElement.addEventListener('pointerdown', onPointerDown);

  // Iniciar Loop de Renderização
  animate();
}

function setupLights() {
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
  scene.add(ambientLight);

  // Luz Principal (Key Light)
  const keyLight = new THREE.DirectionalLight(0xfff3e0, 1.4);
  keyLight.position.set(8, 14, 8);
  keyLight.castShadow = true;
  keyLight.shadow.mapSize.width = 2048;
  keyLight.shadow.mapSize.height = 2048;
  keyLight.shadow.bias = -0.0005;
  scene.add(keyLight);

  // Luz de Preenchimento Azulada (Fill Light)
  const fillLight = new THREE.DirectionalLight(0x38bdf8, 0.9);
  fillLight.position.set(-9, 10, -6);
  scene.add(fillLight);

  // Luz de Borda Médica Laranja (Rim Light)
  const rimLight = new THREE.DirectionalLight(0xff5722, 1.2);
  rimLight.position.set(0, -6, 8);
  scene.add(rimLight);

  // Luz Vermelha emissiva no centro dos sensores ópticos
  const redSensorLight = new THREE.PointLight(0xff0044, 1.8, 4);
  redSensorLight.position.set(0, -0.2, 0);
  scene.add(redSensorLight);
}

function setupEnvironment() {
  // Grid Tecnológico de Base
  const gridHelper = new THREE.GridHelper(26, 30, 0x1e293b, 0x0f172a);
  gridHelper.position.y = -2.4;
  scene.add(gridHelper);

  // Chão Circular com Sombra Suave
  const floorGeo = new THREE.CircleGeometry(14, 48);
  const floorMat = new THREE.MeshStandardMaterial({
    color: 0x06090e,
    roughness: 0.85,
    metalness: 0.3
  });
  const floor = new THREE.Mesh(floorGeo, floorMat);
  floor.rotation.x = -Math.PI / 2;
  floor.position.y = -2.41;
  floor.receiveShadow = true;
  scene.add(floor);
}

/* ============================================================================
   CONSTRUÇÃO DO MODELO 3D: APH-BIOSHIELD
   ============================================================================ */
function buildAPHDeviceModel() {
  mainGroup = new THREE.Group();
  scene.add(mainGroup);

  // Materiais PBR
  const matUpperCasingWhite = new THREE.MeshStandardMaterial({
    color: 0xf1f5f9,
    roughness: 0.28,
    metalness: 0.12,
    clearcoat: 0.4
  });

  const matUpperCasingOrange = new THREE.MeshStandardMaterial({
    color: 0xff5722,
    roughness: 0.5,
    metalness: 0.1
  });

  const matPcb = new THREE.MeshStandardMaterial({
    color: 0x0f3b25, // Verde PCB industrial escuro
    roughness: 0.35,
    metalness: 0.45
  });

  const matChip = new THREE.MeshStandardMaterial({
    color: 0x111827,
    roughness: 0.4,
    metalness: 0.6
  });

  const matGoldPins = new THREE.MeshStandardMaterial({
    color: 0xfbbf24,
    roughness: 0.25,
    metalness: 0.95
  });

  const matBattery = new THREE.MeshStandardMaterial({
    color: 0xd1d5db,
    roughness: 0.35,
    metalness: 0.85
  });

  const matElectrodes = new THREE.MeshStandardMaterial({
    color: 0xf3f4f6,
    roughness: 0.15,
    metalness: 0.95 // Aço cirúrgico espelhado
  });

  const matOpticsHousing = new THREE.MeshStandardMaterial({
    color: 0x020617,
    roughness: 0.2,
    metalness: 0.3
  });

  const matGlass = new THREE.MeshPhysicalMaterial({
    color: 0xffffff,
    transparent: true,
    opacity: 0.75,
    roughness: 0.05,
    transmission: 0.9,
    thickness: 0.4
  });

  const matAdhesive = new THREE.MeshStandardMaterial({
    color: 0x93c5fd,
    transparent: true,
    opacity: 0.55,
    roughness: 0.7,
    metalness: 0.05
  });

  // --------------------------------------------------------------------------
  // CAMADA 1: Base Adesiva Hidrocoloide Médica (Layer Y base: -0.6)
  // --------------------------------------------------------------------------
  const adhesiveGroup = new THREE.Group();
  adhesiveGroup.name = "adhesive_base";

  // Adesivo anatômico oval com abas
  const adhesiveShape = new THREE.Shape();
  const w = 4.2, h = 1.9, r = 0.9;
  adhesiveShape.moveTo(-w/2 + r, -h/2);
  adhesiveShape.lineTo(w/2 - r, -h/2);
  adhesiveShape.quadraticCurveTo(w/2, -h/2, w/2, -h/2 + r);
  adhesiveShape.lineTo(w/2, h/2 - r);
  adhesiveShape.quadraticCurveTo(w/2, h/2, w/2 - r, h/2);
  adhesiveShape.lineTo(-w/2 + r, h/2);
  adhesiveShape.quadraticCurveTo(-w/2, h/2, -w/2, h/2 - r);
  adhesiveShape.lineTo(-w/2, -h/2 + r);
  adhesiveShape.quadraticCurveTo(-w/2, -h/2, -w/2 + r, -h/2);

  // Furos no adesivo para os sensores tocarem a pele diretamente
  const holeOptics = new THREE.Path();
  holeOptics.absellipse(0, 0, 0.65, 0.55, 0, Math.PI * 2, true);
  adhesiveShape.holes.push(holeOptics);

  const holeLeftECG = new THREE.Path();
  holeLeftECG.absellipse(-1.45, 0, 0.42, 0.42, 0, Math.PI * 2, true);
  adhesiveShape.holes.push(holeLeftECG);

  const holeRightECG = new THREE.Path();
  holeRightECG.absellipse(1.45, 0, 0.42, 0.42, 0, Math.PI * 2, true);
  adhesiveShape.holes.push(holeRightECG);

  const holeTemp = new THREE.Path();
  holeTemp.absellipse(0.72, 0.35, 0.22, 0.22, 0, Math.PI * 2, true);
  adhesiveShape.holes.push(holeTemp);

  const extrudeSettingsAdhesive = { depth: 0.04, bevelEnabled: true, bevelSegments: 3, steps: 1, bevelSize: 0.02, bevelThickness: 0.02 };
  const adhesiveGeo = new THREE.ExtrudeGeometry(adhesiveShape, extrudeSettingsAdhesive);
  adhesiveGeo.rotateX(Math.PI / 2);
  const adhesiveMesh = new THREE.Mesh(adhesiveGeo, matAdhesive);
  adhesiveMesh.castShadow = true;
  adhesiveMesh.receiveShadow = true;
  adhesiveMesh.userData = { partKey: "adhesive_base" };
  adhesiveGroup.add(adhesiveMesh);

  layers.adhesive_base = { group: adhesiveGroup, baseY: -0.6, explodeFactor: -1.8 };
  mainGroup.add(adhesiveGroup);

  // --------------------------------------------------------------------------
  // CAMADA 2: 2 Eletrodos Metálicos de Contato Seco para ECG (Layer Y: -0.45)
  // --------------------------------------------------------------------------
  const electrodesGroup = new THREE.Group();
  electrodesGroup.name = "electrodes";

  // Eletrodo Esquerdo
  const electrodeGeo = new THREE.CylinderGeometry(0.38, 0.40, 0.08, 32);
  const electrodeLeft = new THREE.Mesh(electrodeGeo, matElectrodes);
  electrodeLeft.position.set(-1.45, 0, 0);
  electrodeLeft.castShadow = true;
  electrodeLeft.userData = { partKey: "electrodes" };

  // Textura concêntrica / anéis do eletrodo para adesão seca
  const ringGeo = new THREE.TorusGeometry(0.24, 0.03, 16, 32);
  ringGeo.rotateX(Math.PI / 2);
  const ringLeft = new THREE.Mesh(ringGeo, matGoldPins);
  ringLeft.position.set(-1.45, -0.03, 0);
  electrodeLeft.add(ringLeft);

  // Eletrodo Direito
  const electrodeRight = electrodeLeft.clone();
  electrodeRight.position.set(1.45, 0, 0);
  electrodeRight.userData = { partKey: "electrodes" };

  electrodesGroup.add(electrodeLeft);
  electrodesGroup.add(electrodeRight);

  layers.electrodes = { group: electrodesGroup, baseY: -0.45, explodeFactor: -1.2 };
  mainGroup.add(electrodesGroup);

  // --------------------------------------------------------------------------
  // CAMADA 3: Emissor/Receptor Óptico Dual Red+IR (Layer Y: -0.35)
  // --------------------------------------------------------------------------
  const opticsGroup = new THREE.Group();
  opticsGroup.name = "optics";

  // Carcaça de isolamento óptico negro (para evitar interferência óptica direta)
  const opticsBaseGeo = new THREE.BoxGeometry(1.2, 0.12, 0.95);
  const opticsBase = new THREE.Mesh(opticsBaseGeo, matOpticsHousing);
  opticsBase.userData = { partKey: "optics" };
  opticsGroup.add(opticsBase);

  // Lente de Vidro de Safira frontal
  const glassGeo = new THREE.BoxGeometry(1.16, 0.02, 0.91);
  const glassMesh = new THREE.Mesh(glassGeo, matGlass);
  glassMesh.position.y = -0.06;
  opticsGroup.add(glassMesh);

  // Matriz de LEDs Emissores: Red (660nm) e IR (880nm)
  const ledGeo = new THREE.CylinderGeometry(0.06, 0.06, 0.04, 16);
  
  // LED Vermelho 660nm
  const matLedRed = new THREE.MeshStandardMaterial({
    color: 0xff1744,
    emissive: 0xff0044,
    emissiveIntensity: 1.6,
    roughness: 0.2
  });
  const ledRed = new THREE.Mesh(ledGeo, matLedRed);
  ledRed.position.set(-0.3, -0.03, -0.2);
  ledRed.userData = { partKey: "optics" };
  opticsGroup.add(ledRed);

  // LED Infravermelho 880nm
  const matLedIR = new THREE.MeshStandardMaterial({
    color: 0x9333ea,
    emissive: 0x7c3aed,
    emissiveIntensity: 1.2,
    roughness: 0.2
  });
  const ledIR = new THREE.Mesh(ledGeo, matLedIR);
  ledIR.position.set(-0.3, -0.03, 0.2);
  ledIR.userData = { partKey: "optics" };
  opticsGroup.add(ledIR);

  // LED Verde 525nm (Melhoria de microcirculação periférica em choque)
  const matLedGreen = new THREE.MeshStandardMaterial({
    color: 0x10b981,
    emissive: 0x059669,
    emissiveIntensity: 1.4,
    roughness: 0.2
  });
  const ledGreen = new THREE.Mesh(ledGeo, matLedGreen);
  ledGreen.position.set(-0.1, -0.03, 0);
  ledGreen.userData = { partKey: "optics" };
  opticsGroup.add(ledGreen);

  // Fotodiodo Receptor Central de Silício de Alta Área
  const photodiodeGeo = new THREE.BoxGeometry(0.35, 0.04, 0.45);
  const matPhotodiode = new THREE.MeshStandardMaterial({
    color: 0x0f172a,
    metalness: 0.9,
    roughness: 0.1
  });
  const photodiode = new THREE.Mesh(photodiodeGeo, matPhotodiode);
  photodiode.position.set(0.32, -0.03, 0);
  photodiode.userData = { partKey: "optics" };
  opticsGroup.add(photodiode);

  // Barreira Física de Silicone Negro contra Crosstalk (crucial em APH)
  const barrierGeo = new THREE.BoxGeometry(0.06, 0.08, 0.65);
  const matBarrier = new THREE.MeshStandardMaterial({ color: 0x000000, roughness: 0.9 });
  const barrier = new THREE.Mesh(barrierGeo, matBarrier);
  barrier.position.set(0.08, -0.03, 0);
  opticsGroup.add(barrier);

  layers.optics = { group: opticsGroup, baseY: -0.35, explodeFactor: -0.6 };
  mainGroup.add(opticsGroup);

  // --------------------------------------------------------------------------
  // CAMADA 4: Termômetro Infravermelho MEMS de Superfície (Layer Y: -0.35)
  // --------------------------------------------------------------------------
  const tempGroup = new THREE.Group();
  tempGroup.name = "temp_sensor";

  // Cilindro do sensor termopilha de ouro/latão
  const tempCanGeo = new THREE.CylinderGeometry(0.18, 0.20, 0.12, 24);
  const tempCan = new THREE.Mesh(tempCanGeo, matGoldPins);
  tempCan.position.set(0.72, 0, 0.35);
  tempCan.userData = { partKey: "temp_sensor" };

  // Lente de Germânio do termômetro IR
  const tempLensGeo = new THREE.CylinderGeometry(0.11, 0.11, 0.02, 24);
  const matGermanium = new THREE.MeshStandardMaterial({
    color: 0xd97706,
    metalness: 0.95,
    roughness: 0.1
  });
  const tempLens = new THREE.Mesh(tempLensGeo, matGermanium);
  tempLens.position.set(0.72, -0.05, 0.35);
  tempGroup.add(tempCan);
  tempGroup.add(tempLens);

  layers.temp_sensor = { group: tempGroup, baseY: -0.35, explodeFactor: -0.6 };
  mainGroup.add(tempGroup);

  // --------------------------------------------------------------------------
  // CAMADA 5: Bateria LiPo Médica Ultra-fina (Layer Y: -0.15)
  // --------------------------------------------------------------------------
  const batteryGroup = new THREE.Group();
  batteryGroup.name = "battery";

  const batteryGeo = new THREE.BoxGeometry(2.2, 0.16, 1.25);
  const batteryMesh = new THREE.Mesh(batteryGeo, matBattery);
  batteryMesh.castShadow = true;
  batteryMesh.userData = { partKey: "battery" };
  batteryGroup.add(batteryMesh);

  // Cabos de energia de silicone (Vermelho e Preto)
  const wireGeo = new THREE.CylinderGeometry(0.025, 0.025, 0.45, 12);
  wireGeo.rotateZ(Math.PI / 2);
  const matWireRed = new THREE.MeshBasicMaterial({ color: 0xef4444 });
  const matWireBlack = new THREE.MeshBasicMaterial({ color: 0x111827 });

  const wireRed = new THREE.Mesh(wireGeo, matWireRed);
  wireRed.position.set(1.25, 0.04, 0.15);
  const wireBlack = new THREE.Mesh(wireGeo, matWireBlack);
  wireBlack.position.set(1.25, 0.04, -0.15);
  batteryGroup.add(wireRed);
  batteryGroup.add(wireBlack);

  layers.battery = { group: batteryGroup, baseY: -0.15, explodeFactor: 0.2 };
  mainGroup.add(batteryGroup);

  // --------------------------------------------------------------------------
  // CAMADA 6: Placa-Mãe Rígido-Flexível + Rádios BLE / LoRa (Layer Y: 0.15)
  // --------------------------------------------------------------------------
  const mainboardGroup = new THREE.Group();
  mainboardGroup.name = "mainboard";

  const pcbShape = new THREE.Shape();
  const pw = 3.6, ph = 1.6, pr = 0.65;
  pcbShape.moveTo(-pw/2 + pr, -ph/2);
  pcbShape.lineTo(pw/2 - pr, -ph/2);
  pcbShape.quadraticCurveTo(pw/2, -ph/2, pw/2, -ph/2 + pr);
  pcbShape.lineTo(pw/2, ph/2 - pr);
  pcbShape.quadraticCurveTo(pw/2, ph/2, pw/2 - pr, ph/2);
  pcbShape.lineTo(-pw/2 + pr, ph/2);
  pcbShape.quadraticCurveTo(-pw/2, ph/2, -pw/2, ph/2 - pr);
  pcbShape.lineTo(-pw/2, -ph/2 + pr);
  pcbShape.quadraticCurveTo(-pw/2, -ph/2, -pw/2 + pr, -ph/2);

  const extrudeSettingsPcb = { depth: 0.06, bevelEnabled: false };
  const pcbGeo = new THREE.ExtrudeGeometry(pcbShape, extrudeSettingsPcb);
  pcbGeo.rotateX(Math.PI / 2);
  const pcbMesh = new THREE.Mesh(pcbGeo, matPcb);
  pcbMesh.castShadow = true;
  pcbMesh.userData = { partKey: "mainboard" };
  mainboardGroup.add(pcbMesh);

  // Microcontrolador SoC ARM Cortex-M4 (Nordic nRF5340)
  const mcuGeo = new THREE.BoxGeometry(0.55, 0.08, 0.55);
  const mcu = new THREE.Mesh(mcuGeo, matChip);
  mcu.position.set(-0.6, 0.05, 0.1);
  mcu.userData = { partKey: "mainboard" };
  mainboardGroup.add(mcu);

  // Chip LoRa Semtech SX1262 (Comunicação longa distância para APH)
  const loraGeo = new THREE.BoxGeometry(0.48, 0.07, 0.48);
  const lora = new THREE.Mesh(loraGeo, matChip);
  lora.position.set(0.65, 0.05, 0.1);
  lora.userData = { partKey: "mainboard" };
  mainboardGroup.add(lora);

  // Chip AFE de ECG e Biosinais de Ultra-Precisão
  const afeGeo = new THREE.BoxGeometry(0.38, 0.06, 0.38);
  const afe = new THREE.Mesh(afeGeo, matChip);
  afe.position.set(0, 0.05, -0.4);
  mainboardGroup.add(afe);

  // Antena Cerâmica SMD LoRa 915MHz
  const antGeo = new THREE.BoxGeometry(0.6, 0.09, 0.18);
  const matAnt = new THREE.MeshStandardMaterial({ color: 0x3b82f6, roughness: 0.3, metalness: 0.4 });
  const ant = new THREE.Mesh(antGeo, matAnt);
  ant.position.set(-1.25, 0.05, -0.45);
  mainboardGroup.add(ant);

  // Sensor IMU Acelerômetro 6 Eixos (para filtrar solavancos da ambulância)
  const imuGeo = new THREE.BoxGeometry(0.2, 0.05, 0.2);
  const imu = new THREE.Mesh(imuGeo, matChip);
  imu.position.set(1.2, 0.05, -0.35);
  mainboardGroup.add(imu);

  layers.mainboard = { group: mainboardGroup, baseY: 0.15, explodeFactor: 1.0 };
  mainGroup.add(mainboardGroup);

  // --------------------------------------------------------------------------
  // CAMADA 7: Carcaça Superior em Policarbonato IP67 (Layer Y: 0.45)
  // --------------------------------------------------------------------------
  const casingGroup = new THREE.Group();
  casingGroup.name = "upper_casing";

  // Carcaça principal aerodinâmica e anatômica
  const caseShape = new THREE.Shape();
  const cw = 4.0, ch = 1.8, cr = 0.8;
  caseShape.moveTo(-cw/2 + cr, -ch/2);
  caseShape.lineTo(cw/2 - cr, -ch/2);
  caseShape.quadraticCurveTo(cw/2, -ch/2, cw/2, -ch/2 + cr);
  caseShape.lineTo(cw/2, ch/2 - cr);
  caseShape.quadraticCurveTo(cw/2, ch/2, cw/2 - cr, ch/2);
  caseShape.lineTo(-cw/2 + cr, ch/2);
  caseShape.quadraticCurveTo(-cw/2, ch/2, -cw/2, ch/2 - cr);
  caseShape.lineTo(-cw/2, -ch/2 + cr);
  caseShape.quadraticCurveTo(-cw/2, -ch/2, -cw/2 + cr, -ch/2);

  // Abertura circular no centro para o display OLED e halo de LEDs
  const holeDisplay = new THREE.Path();
  holeDisplay.absellipse(0, 0, 0.72, 0.72, 0, Math.PI * 2, true);
  caseShape.holes.push(holeDisplay);

  const extrudeSettingsCase = { depth: 0.35, bevelEnabled: true, bevelSegments: 6, steps: 1, bevelSize: 0.14, bevelThickness: 0.14 };
  const caseGeo = new THREE.ExtrudeGeometry(caseShape, extrudeSettingsCase);
  caseGeo.rotateX(Math.PI / 2);
  const caseMesh = new THREE.Mesh(caseGeo, matUpperCasingWhite);
  caseMesh.castShadow = true;
  caseMesh.receiveShadow = true;
  caseMesh.userData = { partKey: "upper_casing" };
  casingGroup.add(caseMesh);

  // Bumpers Laterais de Borracha Laranja Resgate (Absorção de Impacto)
  const bumperGeo = new THREE.BoxGeometry(0.3, 0.28, 1.4);
  const bumperLeft = new THREE.Mesh(bumperGeo, matUpperCasingOrange);
  bumperLeft.position.set(-2.0, 0.05, 0);
  bumperLeft.userData = { partKey: "upper_casing" };
  const bumperRight = bumperLeft.clone();
  bumperRight.position.set(2.0, 0.05, 0);
  bumperRight.userData = { partKey: "upper_casing" };
  casingGroup.add(bumperLeft);
  casingGroup.add(bumperRight);

  // Presilhas para Cinta Rápida de Resgate nas Extremidades
  const loopGeo = new THREE.TorusGeometry(0.25, 0.06, 12, 24);
  loopGeo.rotateY(Math.PI / 2);
  const loopLeft = new THREE.Mesh(loopGeo, matUpperCasingOrange);
  loopLeft.position.set(-2.15, 0.05, 0);
  const loopRight = loopLeft.clone();
  loopRight.position.set(2.15, 0.05, 0);
  casingGroup.add(loopLeft);
  casingGroup.add(loopRight);

  layers.upper_casing = { group: casingGroup, baseY: 0.45, explodeFactor: 1.8 };
  mainGroup.add(casingGroup);

  // --------------------------------------------------------------------------
  // CAMADA 8: Display OLED + Halo de LEDs Triagem START (Layer Y: 0.70)
  // --------------------------------------------------------------------------
  const displayGroup = new THREE.Group();
  displayGroup.name = "display_triage";

  // Canvas dinâmico para a interface gráfica do display do dispositivo
  const displayCanvas = document.createElement('canvas');
  displayCanvas.width = 256;
  displayCanvas.height = 256;
  const ctx = displayCanvas.getContext('2d');
  
  // Renderizar interface gráfica no display do dispositivo
  renderDisplayTexture(ctx, displayCanvas);
  const displayTexture = new THREE.CanvasTexture(displayCanvas);

  const displayGeo = new THREE.CircleGeometry(0.68, 36);
  const matDisplay = new THREE.MeshBasicMaterial({
    map: displayTexture,
    toneMapped: false
  });
  const displayMesh = new THREE.Mesh(displayGeo, matDisplay);
  displayMesh.rotation.x = -Math.PI / 2;
  displayMesh.position.y = 0.02;
  displayMesh.userData = { partKey: "display_triage" };
  displayGroup.add(displayMesh);

  // Anel Perimétrico de Triagem START (Halo LED pulsante)
  const ringHaloGeo = new THREE.TorusGeometry(0.72, 0.065, 16, 48);
  ringHaloGeo.rotateX(Math.PI / 2);
  const matTriageHalo = new THREE.MeshStandardMaterial({
    color: 0xef4444,
    emissive: 0xef4444,
    emissiveIntensity: 1.5,
    roughness: 0.2
  });
  const ringHalo = new THREE.Mesh(ringHaloGeo, matTriageHalo);
  ringHalo.userData = { partKey: "display_triage", isTriageHalo: true };
  displayGroup.add(ringHalo);

  layers.display_triage = { group: displayGroup, baseY: 0.70, explodeFactor: 2.6 };
  mainGroup.add(displayGroup);
}

function renderDisplayTexture(ctx, canvas) {
  ctx.fillStyle = '#060a12';
  ctx.fillRect(0, 0, 256, 256);

  // Borda sutil interna
  ctx.strokeStyle = '#38bdf8';
  ctx.lineWidth = 4;
  ctx.beginPath();
  ctx.arc(128, 128, 122, 0, Math.PI * 2);
  ctx.stroke();

  // Cabeçalho: Título e Bateria
  ctx.fillStyle = '#ff5722';
  ctx.font = 'bold 20px "Chakra Petch", sans-serif';
  ctx.textAlign = 'center';
  ctx.fillText('APH-BioShield', 128, 48);

  ctx.fillStyle = '#10b981';
  ctx.font = '14px "JetBrains Mono", monospace';
  ctx.fillText('⚡ BATT: 94%', 128, 72);

  // Dados Vitais em Tempo Real
  ctx.fillStyle = '#f8fafc';
  ctx.font = 'bold 28px "Chakra Petch", sans-serif';
  ctx.fillText(`HR: ${state.vitals.hr} BPM`, 128, 114);

  ctx.font = 'bold 22px "Chakra Petch", sans-serif';
  ctx.fillText(`PA: ${state.vitals.sbp}/${state.vitals.dbp}`, 128, 146);

  ctx.font = 'bold 20px "Chakra Petch", sans-serif';
  ctx.fillStyle = '#38bdf8';
  ctx.fillText(`SpO2: ${state.vitals.spo2}%`, 128, 178);

  ctx.font = 'bold 16px "Chakra Petch", sans-serif';
  ctx.fillStyle = '#f59e0b';
  ctx.fillText(`T: ${state.vitals.temp}°C | RR: ${state.vitals.rr}`, 128, 206);

  // Status de Alerta de Hemorragia / Choque
  ctx.fillStyle = '#ef4444';
  ctx.font = 'bold 14px "Chakra Petch", sans-serif';
  ctx.fillText('SI: 1.36 | CHOQUE ATIVO', 128, 230);
}

/* ============================================================================
   INTERAÇÃO 3D: RAYCASTING & CLIQUE EM ELEMENTOS
   ============================================================================ */
function onPointerDown(event) {
  const rect = renderer.domElement.getBoundingClientRect();
  mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
  mouse.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

  raycaster.setFromCamera(mouse, camera);
  const intersects = raycaster.intersectObjects(mainGroup.children, true);

  if (intersects.length > 0) {
    let target = intersects[0].object;
    while (target && (!target.userData || !target.userData.partKey) && target.parent && target.parent !== mainGroup) {
      target = target.parent;
    }

    if (target && target.userData && target.userData.partKey) {
      selectComponent(target.userData.partKey);
    }
  }
}

function selectComponent(partKey) {
  if (!componentsData[partKey]) return;

  state.selectedPart = partKey;

  // Atualizar Lista no Painel Direito
  document.querySelectorAll('.layer-item').forEach(el => {
    if (el.getAttribute('data-part') === partKey) {
      el.classList.add('active');
      el.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    } else {
      el.classList.remove('active');
    }
  });

  // Atualizar Card Flutuante de Inspeção
  const data = componentsData[partKey];
  document.getElementById('comp-type').textContent = data.badge;
  document.getElementById('comp-title').textContent = data.title;
  document.getElementById('comp-desc').textContent = data.desc;

  const specsContainer = document.getElementById('comp-specs');
  specsContainer.innerHTML = '';
  for (const [key, val] of Object.entries(data.specs)) {
    const cell = document.createElement('div');
    cell.className = 'spec-cell';
    cell.innerHTML = `<span>${key}</span><strong>${val}</strong>`;
    specsContainer.appendChild(cell);
  }

  const card = document.getElementById('component-card');
  card.style.display = 'block';

  // Destaque visual: iluminar suavemente a camada
  pulseLayer(partKey);
}

function pulseLayer(partKey) {
  const layerInfo = layers[partKey];
  if (!layerInfo) return;

  const group = layerInfo.group;
  const originalScale = group.scale.clone();
  group.scale.set(1.08, 1.08, 1.08);

  setTimeout(() => {
    group.scale.set(1, 1, 1);
  }, 250);
}

/* ============================================================================
   VISTA EXPLODIDA 3D & ANIMAÇÃO
   ============================================================================ */
function updateExplodedView() {
  // Interpolar suavemente o valor atual para o alvo
  state.explodeRatio += (state.targetExplodeRatio - state.explodeRatio) * 0.12;

  // Atualizar posição Y de cada camada proporcionalmente ao seu explodeFactor
  for (const [key, layer] of Object.entries(layers)) {
    const targetY = layer.baseY + (layer.explodeFactor * state.explodeRatio * 2.2);
    layer.group.position.y = targetY;
  }
}

function toggleXrayMode() {
  state.isXray = !state.isXray;
  const btn = document.getElementById('btn-toggle-xray');
  btn.classList.toggle('active', state.isXray);

  // Alterar opacidade da carcaça superior
  if (layers.upper_casing) {
    layers.upper_casing.group.traverse(child => {
      if (child.isMesh && child.material) {
        child.material.transparent = true;
        child.material.opacity = state.isXray ? 0.22 : 1.0;
        child.material.needsUpdate = true;
      }
    });
  }
}

function setViewPreset(preset) {
  document.querySelectorAll('.toolbar-group .tool-btn').forEach(b => b.classList.remove('active'));

  if (preset === 'iso') {
    camera.position.set(0, 7.5, 11);
    controls.target.set(0, 0, 0);
    document.getElementById('view-preset-iso').classList.add('active');
  } else if (preset === 'top') {
    camera.position.set(0, 14, 0.01);
    controls.target.set(0, 0, 0);
    document.getElementById('view-preset-top').classList.add('active');
  } else if (preset === 'bottom') {
    camera.position.set(0, -14, 0.01);
    controls.target.set(0, 0, 0);
    document.getElementById('view-preset-bottom').classList.add('active');
  } else if (preset === 'side') {
    camera.position.set(12, 1, 0);
    controls.target.set(0, 0, 0);
    document.getElementById('view-preset-side').classList.add('active');
  }
}

/* ============================================================================
   SIMULAÇÃO DE TRAÇADOS EM TEMPO REAL: ECG & PPG
   ============================================================================ */
let ecgCanvas, ecgCtx;
let ppgCanvas, ppgCtx;
let ecgX = 0, ppgX = 0;
let ecgPhase = 0, ppgPhase = 0;

function initWaveforms() {
  ecgCanvas = document.getElementById('canvas-ecg');
  ecgCtx = ecgCanvas.getContext('2d');

  ppgCanvas = document.getElementById('canvas-ppg');
  ppgCtx = ppgCanvas.getContext('2d');

  // Limpar com fundo escuro
  clearCanvas(ecgCtx, ecgCanvas);
  clearCanvas(ppgCtx, ppgCanvas);
}

function clearCanvas(ctx, canvas) {
  ctx.fillStyle = '#080c14';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}

function updateWaveforms() {
  const hr = state.vitals.hr;
  if (hr === 0) {
    // Assistolia na PCR: Linha reta com ruído mínimo
    drawFlatLine(ecgCtx, ecgCanvas, '#22c55e');
    drawFlatLine(ppgCtx, ppgCanvas, '#f43f5e');
    return;
  }

  const speed = (hr / 60) * 0.065;
  ecgPhase += speed;
  ppgPhase += speed;

  // --------------------------------------------------------------------------
  // Traçado ECG: P, QRS, T Sintético
  // --------------------------------------------------------------------------
  const t = ecgPhase % 1.0;
  let ecgY = 0;

  if (t > 0.12 && t < 0.20) {
    // Onda P
    ecgY = Math.sin((t - 0.12) / 0.08 * Math.PI) * 0.2;
  } else if (t > 0.24 && t < 0.27) {
    // Onda Q (pequena deflexão negativa)
    ecgY = -0.15;
  } else if (t >= 0.27 && t < 0.33) {
    // Pico R Alto (Despolarização ventricular)
    ecgY = 1.0;
  } else if (t >= 0.33 && t < 0.36) {
    // Onda S (deflexão negativa)
    ecgY = -0.3;
  } else if (t > 0.45 && t < 0.65) {
    // Onda T (repolarização)
    ecgY = Math.sin((t - 0.45) / 0.20 * Math.PI) * 0.35;
  }

  // Adicionar micro-ruído biológico
  ecgY += (Math.random() - 0.5) * 0.04;

  const baselineEcg = ecgCanvas.height * 0.6;
  const drawEcgY = baselineEcg - (ecgY * (ecgCanvas.height * 0.45));

  drawTrace(ecgCtx, ecgCanvas, ecgX, drawEcgY, '#22c55e');
  ecgX += 2;
  if (ecgX >= ecgCanvas.width) {
    ecgX = 0;
  }

  // --------------------------------------------------------------------------
  // Traçado PPG: Pulso Arterial Óptico com Entalhe Dicrótico & Modulação PVI
  // --------------------------------------------------------------------------
  const pt = (ppgPhase + 0.32) % 1.0; // Atraso fisiológico PAT relativo ao ECG
  let ppgY = 0;

  if (pt < 0.35) {
    // Ascensão Sistólica Rápida
    ppgY = Math.sin((pt / 0.35) * (Math.PI / 2));
  } else if (pt >= 0.35 && pt < 0.48) {
    // Queda inicial pós-sistólica
    ppgY = 1.0 - ((pt - 0.35) / 0.13) * 0.4;
  } else if (pt >= 0.48 && pt < 0.58) {
    // Entalhe Dicrótico (Fechamento da valva aórtica)
    ppgY = 0.6 + Math.sin(((pt - 0.48) / 0.10) * Math.PI) * 0.12;
  } else {
    // Decaimento Diastólico
    ppgY = 0.6 * (1.0 - ((pt - 0.58) / 0.42));
  }

  // Modulação respiratória da amplitude (PVI - reflete hipovolemia)
  const respiratoryMod = 1.0 + Math.sin(Date.now() * 0.003) * (state.vitals.pvi / 100);
  ppgY *= respiratoryMod;

  const baselinePpg = ppgCanvas.height * 0.85;
  const drawPpgY = baselinePpg - (ppgY * (ppgCanvas.height * 0.65));

  drawTrace(ppgCtx, ppgCanvas, ppgX, drawPpgY, '#f43f5e');
  ppgX += 2;
  if (ppgX >= ppgCanvas.width) {
    ppgX = 0;
  }
}

function drawTrace(ctx, canvas, x, y, color) {
  // Apagar faixa à frente do feixe de varredura
  ctx.fillStyle = '#080c14';
  ctx.fillRect(x, 0, 10, canvas.height);

  // Linhas guia sutis
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(x, canvas.height / 2);
  ctx.lineTo(x + 10, canvas.height / 2);
  ctx.stroke();

  // Desenhar ponto luminoso
  ctx.fillStyle = color;
  ctx.shadowColor = color;
  ctx.shadowBlur = 6;
  ctx.beginPath();
  ctx.arc(x, y, 1.8, 0, Math.PI * 2);
  ctx.fill();
  ctx.shadowBlur = 0;
}

function drawFlatLine(ctx, canvas, color) {
  ctx.fillStyle = '#080c14';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.strokeStyle = color;
  ctx.lineWidth = 1.5;
  ctx.beginPath();
  ctx.moveTo(0, canvas.height / 2);
  ctx.lineTo(canvas.width, canvas.height / 2);
  ctx.stroke();
}

/* ============================================================================
   CONTROLE DE CENÁRIOS E TELEMETRIA CLÍNICA
   ============================================================================ */
function applyScenario(scenarioKey) {
  const sc = scenarios[scenarioKey];
  if (!sc) return;

  state.currentScenario = scenarioKey;
  state.vitals = { ...sc.vitals };

  // Atualizar Triagem START no Cabeçalho
  const pill = document.getElementById('triage-status-pill');
  const text = document.getElementById('triage-text');
  text.textContent = `TRIAGEM: ${sc.triage}`;
  pill.style.borderColor = sc.triageColor;
  pill.style.color = sc.triageColor;
  pill.style.background = `${sc.triageColor}22`;

  // Atualizar Halo de Triagem no Modelo 3D
  if (layers.display_triage) {
    layers.display_triage.group.traverse(child => {
      if (child.userData && child.userData.isTriageHalo) {
        child.material.color.set(sc.triageColor);
        child.material.emissive.set(sc.triageColor);
      }
    });
  }

  // Atualizar Valores do Painel
  document.getElementById('val-bp').innerHTML = `${sc.vitals.sbp}/${sc.vitals.dbp} <small>mmHg</small>`;
  document.getElementById('status-bp').textContent = sc.statuses.bp;

  document.getElementById('val-pi').textContent = `${sc.vitals.pi}%`;
  document.getElementById('val-pvi').textContent = `${sc.vitals.pvi}%`;
  document.getElementById('val-si-badge').textContent = `SI: ${sc.vitals.si}`;
  document.getElementById('status-vol').textContent = sc.statuses.vol;

  document.getElementById('val-hr').innerHTML = `${sc.vitals.hr} <small>BPM</small>`;
  document.getElementById('status-hr').textContent = sc.statuses.hr;

  document.getElementById('val-spo2').innerHTML = `${sc.vitals.spo2} <small>%</small>`;
  document.getElementById('status-spo2').textContent = sc.statuses.spo2;

  document.getElementById('val-rr').innerHTML = `${sc.vitals.rr} <small>RPM</small>`;
  document.getElementById('status-rr').textContent = sc.statuses.rr;

  document.getElementById('val-temp').innerHTML = `${sc.vitals.temp} <small>°C</small>`;
  document.getElementById('status-temp').textContent = sc.statuses.temp;
}

/* ============================================================================
   LOOP DE ANIMAÇÃO & EVENT LISTENERS
   ============================================================================ */
let lastWaveUpdate = 0;

function animate(time) {
  requestAnimationFrame(animate);

  // Rotação Automática da Câmera
  if (state.autoRotate) {
    mainGroup.rotation.y += 0.0035;
  }

  // Atualizar Posição Suave da Vista Explodida
  updateExplodedView();

  // Pulsar Anel de Triagem
  if (layers.display_triage) {
    const pulseFactor = 1.0 + Math.sin(time * 0.005) * 0.4;
    layers.display_triage.group.traverse(child => {
      if (child.userData && child.userData.isTriageHalo) {
        child.material.emissiveIntensity = pulseFactor;
      }
    });
  }

  // Atualizar Ondas Fisiológicas (ECG / PPG) a cada 20ms
  if (time - lastWaveUpdate > 20) {
    updateWaveforms();
    lastWaveUpdate = time;
  }

  controls.update();
  renderer.render(scene, camera);
}

function onWindowResize() {
  const width = container3D.clientWidth;
  const height = container3D.clientHeight;
  camera.aspect = width / height;
  camera.updateProjectionMatrix();
  renderer.setSize(width, height);
}

/* ============================================================================
   INICIALIZAÇÃO DO DOM & EVENT BINDINGS
   ============================================================================ */
document.addEventListener('DOMContentLoaded', () => {
  // Inicializar o 3D e as Ondas
  init3D();
  initWaveforms();

  // Selecionar o primeiro componente por padrão
  selectComponent('optics');

  // Slider de Vista Explodida
  const sliderExplode = document.getElementById('slider-explode');
  const explodeVal = document.getElementById('explode-val');
  sliderExplode.addEventListener('input', (e) => {
    const val = parseFloat(e.target.value);
    state.targetExplodeRatio = val / 100;
    explodeVal.textContent = `${Math.round(val)}%`;
  });

  // Presets de Câmera
  document.getElementById('view-preset-iso').addEventListener('click', () => setViewPreset('iso'));
  document.getElementById('view-preset-top').addEventListener('click', () => setViewPreset('top'));
  document.getElementById('view-preset-bottom').addEventListener('click', () => setViewPreset('bottom'));
  document.getElementById('view-preset-side').addEventListener('click', () => setViewPreset('side'));

  // Botões da Toolbar
  document.getElementById('btn-toggle-xray').addEventListener('click', toggleXrayMode);
  
  const btnRotate = document.getElementById('btn-toggle-autorotate');
  btnRotate.addEventListener('click', () => {
    state.autoRotate = !state.autoRotate;
    btnRotate.classList.toggle('active', state.autoRotate);
  });

  document.getElementById('btn-toggle-labels').addEventListener('click', () => {
    // Alterna slider para 50% para ver os layers
    if (state.targetExplodeRatio === 0) {
      sliderExplode.value = 60;
      sliderExplode.dispatchEvent(new Event('input'));
    } else {
      sliderExplode.value = 0;
      sliderExplode.dispatchEvent(new Event('input'));
    }
  });

  // Clique nos Itens da Lista de Hardware (Painel Direito)
  document.querySelectorAll('.layer-item').forEach(item => {
    item.addEventListener('click', () => {
      const partKey = item.getAttribute('data-part');
      selectComponent(partKey);
    });
  });

  // Fechar Card de Inspeção
  document.getElementById('btn-close-card').addEventListener('click', () => {
    document.getElementById('component-card').style.display = 'none';
  });

  // Seletor de Cenários Clínicos
  document.getElementById('select-scenario').addEventListener('change', (e) => {
    applyScenario(e.target.value);
  });

  // Toggle de Form Factor (Adesivo vs Pulseira)
  const btnPatch = document.getElementById('btn-ff-patch');
  const btnWrist = document.getElementById('btn-ff-wrist');
  const ffText = document.getElementById('ff-veredicto-text');

  btnPatch.addEventListener('click', () => {
    btnPatch.classList.add('active');
    btnWrist.classList.remove('active');
    state.formFactor = 'patch';
    ffText.innerHTML = `<strong>Adesivo Torácico Esternal:</strong> Posição superior para trauma. Garante o sinal de pulso central mesmo com hipotensão profunda e captura o vetor QRS do ECG em um único local, sem depender da outra mão do paciente.`;
  });

  btnWrist.addEventListener('click', () => {
    btnWrist.classList.add('active');
    btnPatch.classList.remove('active');
    state.formFactor = 'wrist';
    ffText.innerHTML = `<strong>Pulseira de Punho:</strong> Prática em emergências leves, porém <em>arriscada em trauma grave</em>: no choque hemorrágico, a vasoconstrição periférica elimina o pulso no punho e o ECG exige que o paciente encoste o outro braço para fechar o circuito.`;
  });

  // Accordion da Extração de Parâmetros
  document.querySelectorAll('.accordion-header').forEach(header => {
    header.addEventListener('click', () => {
      const content = header.nextElementSibling;
      const isOpen = content.style.display === 'block';
      document.querySelectorAll('.accordion-content').forEach(c => c.style.display = 'none');
      if (!isOpen) {
        content.style.display = 'block';
      }
    });
  });

  // Modais de Galeria e Dossiê
  const modalGallery = document.getElementById('modal-gallery');
  const btnOpenGallery = document.getElementById('btn-gallery');
  const btnCloseGallery = document.getElementById('btn-close-gallery');

  btnOpenGallery.addEventListener('click', () => modalGallery.classList.add('open'));
  btnCloseGallery.addEventListener('click', () => modalGallery.classList.remove('open'));

  const modalDocs = document.getElementById('modal-docs');
  const btnOpenDocs = document.getElementById('btn-docs');
  const btnCloseDocs = document.getElementById('btn-close-docs');

  btnOpenDocs.addEventListener('click', () => modalDocs.classList.add('open'));
  btnCloseDocs.addEventListener('click', () => modalDocs.classList.remove('open'));

  // Fechar modais ao clicar no fundo
  [modalGallery, modalDocs].forEach(m => {
    m.addEventListener('click', (e) => {
      if (e.target === m) m.classList.remove('open');
    });
  });
});
