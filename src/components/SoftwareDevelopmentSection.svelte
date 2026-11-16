<script>
  const lifecycle = [
    {
      number: "01",
      symbol: "⌘",
      title: "Arquitectura",
      description: "Definimos estructura, componentes e integraciones para que el software pueda crecer.",
    },
    {
      number: "02",
      symbol: "⌁",
      title: "Desarrollo",
      description: "Convertimos requerimientos en aplicaciones y experiencias listas para usarse.",
    },
    {
      number: "03",
      symbol: "⟳",
      title: "Actualización",
      description: "Modernizamos funcionalidades y evolucionamos sistemas existentes paso a paso.",
    },
    {
      number: "04",
      symbol: "⇄",
      title: "Integración",
      description: "Conectamos aplicaciones, servicios y datos para que trabajen como un solo producto.",
    },
  ];
</script>

<section class="software-section" aria-labelledby="software-title">
  <div class="software-inner">
    <header class="software-heading">
      <p class="eyebrow">INGENIERÍA DE SOFTWARE</p>
      <h2 id="software-title">Software que nace para crecer.</h2>
      <p class="intro">
        Desde la arquitectura hasta la evolución del producto: diseñamos, desarrollamos e integramos
        soluciones para Android y Windows.
      </p>
    </header>

    <div class="lifecycle" aria-label="Ciclo de desarrollo de software">
      {#each lifecycle as phase}
        <article class="phase">
          <div class="phase-marker">
            <span class="phase-symbol" aria-hidden="true">{phase.symbol}</span>
            <span class="phase-number">{phase.number}</span>
          </div>
          <h3>{phase.title}</h3>
          <p>{phase.description}</p>
        </article>
      {/each}
    </div>

    <div class="platforms">
      <p class="platforms-label">PLATAFORMAS EN LAS QUE CONSTRUIMOS</p>
      <div class="platform">
        <div class="platform-icon android-icon" aria-hidden="true">
          <svg viewBox="0 0 40 40" fill="none">
            <path d="M11 14.5h18v12a2 2 0 0 1-2 2H13a2 2 0 0 1-2-2v-12Z" />
            <path d="M10 19v7M30 19v7M16 31v3M24 31v3M14 11l-2-3M26 11l2-3" />
            <path d="M11 15a9 9 0 0 1 18 0H11Z" />
            <circle cx="16" cy="12" r="1" />
            <circle cx="24" cy="12" r="1" />
          </svg>
        </div>
        <div class="platform-copy">
          <span class="platform-overline">MÓVIL</span>
          <h3>Android</h3>
          <p>Aplicaciones móviles funcionales, conectadas y preparadas para evolucionar.</p>
        </div>
        <span class="platform-arrow" aria-hidden="true">↗</span>
      </div>

      <div class="platform">
        <div class="platform-icon windows-icon" aria-hidden="true">
          <svg viewBox="0 0 40 40" fill="none">
            <path d="m6 11 12-2v11H6V11Zm16-2 12-2v13H22V9ZM6 22h12v11L6 31V22Zm16 0h12v13l-12-2V22Z" />
          </svg>
        </div>
        <div class="platform-copy">
          <span class="platform-overline">ESCRITORIO</span>
          <h3>Windows</h3>
          <p>Software de escritorio, herramientas internas e integración con tus sistemas.</p>
        </div>
        <span class="platform-arrow" aria-hidden="true">↗</span>
      </div>
    </div>

    <p class="closing-line">
      <span aria-hidden="true">✳</span>
      Crear desde cero, mejorar lo que ya existe o conectar las piezas.
    </p>
  </div>
</section>

<style>
  .software-section {
    position: relative;
    overflow: hidden;
    padding: clamp(3.5rem, 8vw, 7rem) 1.25rem;
    color: #f4f6ed;
    background:
      radial-gradient(ellipse at 2% 20%, rgba(196, 255, 87, 0.055), transparent 31rem),
      linear-gradient(180deg, rgba(11, 12, 20, 0.72), rgba(17, 21, 14, 0.76));
  }

  .software-section::before {
    position: absolute;
    top: 0;
    right: -7rem;
    width: 24rem;
    aspect-ratio: 1;
    border: 1px solid rgba(196, 255, 87, 0.055);
    border-radius: 50%;
    box-shadow: 0 0 0 3rem rgba(196, 255, 87, 0.012), 0 0 0 6rem rgba(196, 255, 87, 0.008);
    content: "";
    pointer-events: none;
  }

  .software-inner {
    position: relative;
    width: min(1120px, 100%);
    margin: 0 auto;
  }

  .software-heading {
    max-width: 760px;
    margin-bottom: clamp(2.2rem, 5vw, 4rem);
  }

  .eyebrow,
  .platforms-label,
  .platform-overline {
    color: #c4ff57;
    font-size: 0.68rem;
    font-weight: 750;
    letter-spacing: 0.15em;
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

  .intro {
    max-width: 660px;
    margin: 1rem 0 0;
    color: #b7baa9;
    font-size: 1.05rem;
    line-height: 1.7;
  }

  .lifecycle {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    margin-bottom: clamp(2.5rem, 6vw, 4.5rem);
    border-top: 1px solid rgba(196, 255, 87, 0.28);
  }

  .phase {
    position: relative;
    padding: 1.5rem 1.2rem 0 0;
  }

  .phase:not(:last-child)::after {
    position: absolute;
    top: -1px;
    right: 1.2rem;
    left: 0;
    height: 1px;
    background: linear-gradient(90deg, #c4ff57, rgba(196, 255, 87, 0.08));
    content: "";
    transform: scaleX(0.35);
    transform-origin: left;
    transition: transform 280ms ease;
  }

  .phase:hover::after {
    transform: scaleX(1);
  }

  .phase-marker {
    display: flex;
    align-items: center;
    gap: 0.65rem;
    margin-bottom: 1rem;
  }

  .phase-symbol {
    display: grid;
    width: 2.5rem;
    aspect-ratio: 1;
    place-items: center;
    color: #d7ff8c;
    border: 1px solid rgba(196, 255, 87, 0.26);
    border-radius: 12px;
    background: rgba(196, 255, 87, 0.075);
    font-size: 1.2rem;
    transition: transform 220ms ease, background 220ms ease;
  }

  .phase:hover .phase-symbol {
    transform: rotate(-8deg) scale(1.08);
    background: rgba(196, 255, 87, 0.16);
  }

  .phase-number {
    color: #8d927e;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.12em;
  }

  .phase h3 {
    margin: 0 0 0.5rem;
    font-size: 1.08rem;
  }

  .phase p {
    max-width: 240px;
    margin: 0;
    color: #aeb19f;
    font-size: 0.84rem;
    line-height: 1.65;
  }

  .platforms {
    display: grid;
    grid-template-columns: 1fr 1fr;
    align-items: center;
    column-gap: clamp(1.5rem, 5vw, 4rem);
    padding: 1.5rem 0;
    border-top: 1px solid rgba(255, 255, 255, 0.12);
    border-bottom: 1px solid rgba(255, 255, 255, 0.12);
  }

  .platforms-label {
    grid-column: 1 / -1;
    margin: 0 0 0.75rem;
    color: #929783;
    font-size: 0.6rem;
  }

  .platform {
    display: grid;
    grid-template-columns: auto minmax(0, 1fr) auto;
    align-items: center;
    gap: 1rem;
    min-width: 0;
    padding: 1rem 0;
  }

  .platform + .platform {
    border-left: 1px solid rgba(255, 255, 255, 0.12);
    padding-left: clamp(1rem, 3vw, 2rem);
  }

  .platform-icon {
    display: grid;
    width: 3.2rem;
    aspect-ratio: 1;
    place-items: center;
    border-radius: 16px;
  }

  .platform-icon svg {
    width: 2rem;
    stroke: currentColor;
    stroke-linecap: round;
    stroke-linejoin: round;
    stroke-width: 1.8;
  }

  .android-icon {
    color: #c4ff57;
    background: rgba(196, 255, 87, 0.09);
  }

  .windows-icon {
    color: #7bc8ff;
    background: rgba(123, 200, 255, 0.09);
  }

  .platform-overline {
    color: #909583;
    font-size: 0.55rem;
  }

  .platform-copy h3 {
    margin: 0.15rem 0;
    font-size: 1.3rem;
    letter-spacing: -0.03em;
  }

  .platform-copy p {
    margin: 0;
    color: #aeb19f;
    font-size: 0.78rem;
    line-height: 1.5;
  }

  .platform-arrow {
    align-self: start;
    color: #c4ff57;
    font-size: 1.2rem;
    transition: transform 200ms ease;
  }

  .platform:hover .platform-arrow {
    transform: translate(3px, -3px);
  }

  .closing-line {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin: 1.25rem 0 0;
    color: #c9cdbb;
    font-size: 0.88rem;
  }

  .closing-line span {
    color: #c4ff57;
    font-size: 1.2rem;
  }

  @media (max-width: 760px) {
    .lifecycle {
      grid-template-columns: repeat(2, minmax(0, 1fr));
      row-gap: 1.25rem;
    }

    .phase:nth-child(2)::after {
      display: none;
    }

    .phase {
      padding-right: 1rem;
    }
  }

  @media (max-width: 560px) {
    .lifecycle {
      grid-template-columns: 1fr;
      gap: 0;
      border-top: 0;
    }

    .phase {
      display: grid;
      grid-template-columns: 2.8rem minmax(0, 1fr);
      column-gap: 0.75rem;
      padding: 1rem 0;
      border-top: 1px solid rgba(255, 255, 255, 0.12);
    }

    .phase::after {
      display: none;
    }

    .phase-marker {
      grid-row: span 2;
      flex-direction: column;
      align-items: center;
      margin: 0;
    }

    .phase h3 {
      align-self: end;
      margin-bottom: 0.25rem;
    }

    .phase p {
      grid-column: 2;
      max-width: none;
    }

    .platforms {
      grid-template-columns: 1fr;
    }

    .platform + .platform {
      border-top: 1px solid rgba(255, 255, 255, 0.12);
      border-left: 0;
      padding-left: 0;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .phase::after,
    .phase-symbol,
    .platform-arrow {
      transition: none;
    }
  }
</style>
