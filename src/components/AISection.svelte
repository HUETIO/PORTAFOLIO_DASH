<script>
  const capabilities = [
    {
      number: "01",
      icon: "✦",
      category: "ASISTENTES Y AGENTES",
      title: "IA que conversa y actúa",
      description:
        "Asistentes que responden preguntas, usan herramientas y ayudan a completar tareas con contexto.",
      examples: ["Agentes de IA", "Copilotos", "Atención inteligente"],
    },
    {
      number: "02",
      icon: "⌕",
      category: "CONOCIMIENTO",
      title: "Tus documentos, convertidos en respuestas",
      description:
        "Experiencias que buscan en contenido propio y ofrecen respuestas útiles basadas en tus fuentes.",
      examples: ["Búsqueda semántica", "RAG", "Bases de conocimiento"],
    },
    {
      number: "03",
      icon: "↗",
      category: "AUTOMATIZACIÓN",
      title: "Menos tareas repetitivas",
      description:
        "Flujos inteligentes para clasificar solicitudes, extraer información y conectar procesos.",
      examples: ["Procesamiento de documentos", "Flujos de trabajo", "Integraciones"],
    },
    {
      number: "04",
      icon: "◉",
      category: "CREACIÓN GENERATIVA",
      title: "Nuevas formas de crear",
      description:
        "Aplicaciones que generan y transforman texto, imágenes y otros contenidos para experiencias digitales.",
      examples: ["Generación de contenido", "Experiencias multimodales", "Prototipos"],
    },
    {
      number: "05",
      icon: "⌁",
      category: "DATOS E INSIGHTS",
      title: "Información que ayuda a decidir",
      description:
        "Soluciones que resumen datos, identifican patrones y hacen más accesible el análisis.",
      examples: ["Análisis asistido", "Resúmenes", "Exploración conversacional"],
    },
    {
      number: "06",
      icon: "＋",
      category: "PRODUCTOS CON IA",
      title: "IA integrada en tus aplicaciones",
      description:
        "Funciones inteligentes diseñadas para encajar en una plataforma, servicio o producto existente.",
      examples: ["APIs de IA", "Aplicaciones web", "Integración con sistemas"],
    },
  ];
</script>

<section class="ai-section" aria-labelledby="ai-title">
  <div class="ai-inner">
    <header class="ai-heading">
      <p class="eyebrow">INTELIGENCIA ARTIFICIAL APLICADA</p>
      <h2 id="ai-title">De una idea a algo que la IA puede hacer.</h2>
      <p class="ai-intro">
        Diseño y construyo soluciones con inteligencia artificial para resolver problemas reales:
        desde un asistente especializado hasta una aplicación completa. La tecnología se elige
        según el objetivo, los datos y las necesidades de cada proyecto.
      </p>
    </header>

    <div class="capability-list">
      {#each capabilities as capability}
        <article class="capability-row">
          <div class="row-identity">
            <span class="row-icon" aria-hidden="true">{capability.icon}</span>
            <span class="row-number">{capability.number}</span>
          </div>
          <div class="row-main">
            <p class="category">{capability.category}</p>
            <h3>{capability.title}</h3>
            <p class="description">{capability.description}</p>
          </div>
          <ul aria-label={`Ejemplos: ${capability.title}`}>
            {#each capability.examples as example}
              <li>{example}</li>
            {/each}
          </ul>
        </article>
      {/each}
    </div>

    <div class="platform-note">
      <span class="note-mark" aria-hidden="true">✦</span>
      <p>
        <strong>La IA correcta para cada reto.</strong>
        Modelos generativos, agentes y servicios cloud pueden combinarse con tus datos y sistemas,
        con atención a la seguridad y al uso responsable.
      </p>
    </div>
  </div>
</section>

<style>
  .ai-section {
    padding: clamp(3.5rem, 8vw, 7rem) 1.25rem;
    color: #f7f5ff;
    background:
      radial-gradient(ellipse at 92% 3%, rgba(128, 92, 255, 0.16), transparent 34rem),
      linear-gradient(180deg, #101320, #0b0c14);
  }

  .ai-inner {
    width: min(1120px, 100%);
    margin: 0 auto;
  }

  .ai-heading {
    max-width: 760px;
    margin-bottom: 2rem;
    animation: rise-in 650ms both;
  }

  .eyebrow,
  .category {
    color: #b7a3ff;
    font-size: 0.7rem;
    font-weight: 750;
    letter-spacing: 0.14em;
  }

  .eyebrow {
    margin: 0 0 0.75rem;
  }

  h2 {
    margin: 0;
    font-size: clamp(2rem, 5vw, 3.5rem);
    letter-spacing: -0.05em;
    line-height: 1.08;
  }

  .ai-intro {
    max-width: 680px;
    margin: 1rem 0 0;
    color: #b8bbca;
    font-size: 1.05rem;
    line-height: 1.7;
  }

  .capability-list {
    border-top: 1px solid rgba(255, 255, 255, 0.12);
    perspective: 900px;
  }

  .capability-row {
    display: grid;
    grid-template-columns: 4.5rem minmax(0, 1fr) minmax(14rem, 0.72fr);
    align-items: center;
    gap: 1.5rem;
    padding: 1.4rem 0.5rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.12);
    animation: rise-in 550ms both;
    transition: padding 220ms ease, background 220ms ease, border-color 220ms ease;
  }

  .capability-row:nth-child(1) { animation-delay: 80ms; }
  .capability-row:nth-child(2) { animation-delay: 140ms; }
  .capability-row:nth-child(3) { animation-delay: 200ms; }
  .capability-row:nth-child(4) { animation-delay: 260ms; }
  .capability-row:nth-child(5) { animation-delay: 320ms; }
  .capability-row:nth-child(6) { animation-delay: 380ms; }

  .row-identity {
    display: grid;
    justify-items: center;
    gap: 0.35rem;
  }

  .capability-row:hover {
    padding-right: 1rem;
    padding-left: 1rem;
    border-bottom-color: rgba(183, 163, 255, 0.38);
    background: linear-gradient(90deg, rgba(128, 92, 255, 0.13), rgba(128, 92, 255, 0.025) 65%, transparent);
  }

  .row-icon {
    display: grid;
    width: 3rem;
    aspect-ratio: 1;
    place-items: center;
    color: #d3c8ff;
    border: 1px solid rgba(183, 163, 255, 0.28);
    border-radius: 14px;
    background:
      radial-gradient(circle at 30% 20%, rgba(183, 163, 255, 0.23), transparent 70%),
      rgba(128, 92, 255, 0.12);
    box-shadow: 0 0 0 rgba(128, 92, 255, 0);
    font-size: 1.3rem;
    transition: transform 260ms ease, border-color 260ms ease, box-shadow 260ms ease;
  }

  .capability-row:hover .row-icon {
    transform: translateY(-2px) rotate(-8deg) scale(1.08);
    border-color: rgba(183, 163, 255, 0.75);
    box-shadow: 0 0 24px rgba(128, 92, 255, 0.28);
  }

  .row-number {
    color: #9084b8;
    font-size: 0.62rem;
    font-weight: 700;
    letter-spacing: 0.12em;
  }

  .category {
    margin: 0 0 0.3rem;
    font-size: 0.6rem;
  }

  .row-main h3 {
    position: relative;
    display: inline-block;
    margin: 0;
    font-size: clamp(1.05rem, 2vw, 1.3rem);
    letter-spacing: -0.02em;
    line-height: 1.35;
  }

  .row-main h3::after {
    position: absolute;
    right: 0;
    bottom: -0.15rem;
    left: 0;
    height: 1px;
    background: linear-gradient(90deg, #b7a3ff, transparent);
    content: "";
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 260ms ease;
  }

  .capability-row:hover .row-main h3::after {
    transform: scaleX(1);
  }

  .description {
    max-width: 600px;
    margin: 0.4rem 0 0;
    color: #b8bbca;
    font-size: 0.86rem;
    line-height: 1.65;
  }

  ul {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin: 1rem 0 0;
    padding: 0;
    list-style: none;
  }

  li {
    padding: 0.2rem 0;
    color: #d7d4e4;
    font-size: 0.65rem;
  }

  li + li::before {
    margin: 0 0.5rem 0 0.15rem;
    color: #8d7acb;
    content: "/";
  }

  .platform-note {
    display: flex;
    align-items: flex-start;
    gap: 0.85rem;
    margin-top: 1rem;
    padding: 1.1rem 1.25rem;
    border: 1px solid rgba(183, 163, 255, 0.22);
    border-radius: 16px;
    background: rgba(128, 92, 255, 0.06);
    animation: glow-in 700ms 450ms both;
  }

  .note-mark {
    color: #b7a3ff;
    font-size: 1.2rem;
    animation: sparkle 2.8s ease-in-out infinite;
  }

  .platform-note p {
    display: grid;
    gap: 0.3rem;
    margin: 0;
    color: #b8bbca;
    font-size: 0.88rem;
    line-height: 1.6;
  }

  .platform-note strong {
    color: #f7f5ff;
  }

  @keyframes rise-in {
    from {
      opacity: 0;
      transform: translateY(14px);
    }

    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  @keyframes glow-in {
    from {
      opacity: 0;
      box-shadow: 0 0 0 rgba(128, 92, 255, 0);
    }

    to {
      opacity: 1;
      box-shadow: 0 0 28px rgba(128, 92, 255, 0.12);
    }
  }

  @keyframes sparkle {
    0%, 100% { transform: scale(1) rotate(0); }
    50% { transform: scale(1.15) rotate(12deg); }
  }

  @media (max-width: 760px) {
    .capability-row {
      grid-template-columns: 3.5rem minmax(0, 1fr);
      gap: 0.7rem 1rem;
    }

    .capability-row ul {
      grid-column: 2;
      margin-top: 0.35rem;
    }
  }

  @media (max-width: 560px) {
    .capability-row {
      grid-template-columns: 2.8rem minmax(0, 1fr);
      gap: 0.65rem;
      padding: 1.2rem 0.15rem;
    }

    .row-icon {
      width: 2.5rem;
      border-radius: 12px;
    }

    .capability-row:hover {
      padding-right: 0.4rem;
      padding-left: 0.4rem;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .ai-heading,
    .capability-row,
    .platform-note,
    .note-mark {
      animation: none;
    }

    .capability-row,
    .row-icon,
    .row-main h3::after {
      transition: none;
    }
  }
</style>
