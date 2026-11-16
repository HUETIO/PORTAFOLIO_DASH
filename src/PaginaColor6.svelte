<script>
  export let color = "#b626ff";
  import CardDetailButton from "./components/CardDetailButton.svelte";

  const principles = [
    {
      number: "01",
      title: "Diseño con intención",
      description:
        "Cada pantalla empieza por una pregunta: ¿qué necesita hacer la persona que la usa?",
      icon: "✳",
    },
    {
      number: "02",
      title: "Tecnología útil",
      description:
        "Elijo herramientas por lo que resuelven, no por lo novedosas que parezcan.",
      icon: "⌘",
    },
    {
      number: "03",
      title: "Detalles que importan",
      description:
        "Accesibilidad, velocidad y estados claros también son parte de una buena experiencia.",
      icon: "↗",
    },
  ];

  const steps = [
    { number: "01", title: "Explorar", description: "Entender el reto y a quién va dirigido." },
    { number: "02", title: "Prototipar", description: "Dar forma a una solución y probar el flujo." },
    { number: "03", title: "Construir", description: "Convertir la idea en una experiencia funcional." },
    { number: "04", title: "Mejorar", description: "Pulir, validar y aprender de cada iteración." },
  ];

  const tools = ["Svelte", "JavaScript", "CSS", "APIs", "Firebase"];
</script>

<svelte:head>
  <title>Ideas en movimiento | DASH.IO</title>
  <meta
    name="description"
    content="Una mirada al proceso, las ideas y las herramientas detrás de DASH.IO."
  />
</svelte:head>

<main class="ideas-page" style:--accent={color}>
  <div class="page-shell">
    <header class="topline">
      <a class="brand" href="#inicio" aria-label="DASH.IO, volver al inicio">DASH<span>.</span>IO</a>
      <span class="section-label"><span class="status-dot"></span> ESPACIO CREATIVO / 06</span>
    </header>

    <section class="hero" aria-labelledby="ideas-title">
      <div class="hero-copy">
        <p class="eyebrow">IDEAS EN MOVIMIENTO</p>
        <h1 id="ideas-title">La tecnología también puede <span>sentirse.</span></h1>
        <p class="intro">
          Me gusta crear experiencias digitales que sean útiles, claras y un poco
          inesperadas. Este espacio reúne las ideas que guían cada proyecto.
        </p>
        <a class="text-link" href="https://github.com/HUETIO" target="_blank" rel="noreferrer">
          Explorar proyectos <span aria-hidden="true">↗</span>
        </a>
      </div>

      <div class="hero-art" aria-hidden="true">
        <div class="orbit orbit-one"></div>
        <div class="orbit orbit-two"></div>
        <div class="orbit orbit-three"></div>
        <div class="core"><span>D</span></div>
        <span class="orbit-label label-top">IMAGINAR</span>
        <span class="orbit-label label-bottom">HACER</span>
        <span class="spark spark-one">✳</span>
        <span class="spark spark-two">✦</span>
      </div>
    </section>

    <section class="principles" aria-labelledby="principles-title">
      <div class="section-heading">
        <p class="eyebrow">UNA FORMA DE HACER</p>
        <h2 id="principles-title">Ideas simples. Experiencias memorables.</h2>
      </div>

      <div class="principle-grid">
        {#each principles as principle}
          <article class="principle-card">
            <div class="card-top">
              <span class="card-number">{principle.number}</span>
              <span class="card-icon" aria-hidden="true">{principle.icon}</span>
            </div>
            <h3>{principle.title}</h3>
            <p>{principle.description}</p>
            <CardDetailButton
              title={principle.title}
              description={principle.description}
              details={[
                principle.title === "Diseño con intención"
                  ? "Las decisiones de interfaz parten de las tareas y necesidades de quien la utiliza."
                  : principle.title === "Tecnología útil"
                    ? "La selección de herramientas debe responder al problema y al contexto del proyecto."
                    : "Accesibilidad, rendimiento y estados comprensibles se consideran durante el diseño y la implementación."
              ]}
              accent={color}
            />
          </article>
        {/each}
      </div>
    </section>

    <section class="process" aria-labelledby="process-title">
      <div class="process-heading">
        <div>
          <p class="eyebrow">DEL CONCEPTO AL DETALLE</p>
          <h2 id="process-title">Así toma forma una idea.</h2>
        </div>
        <p class="process-note">Un proceso flexible, con curiosidad en cada paso.</p>
      </div>

      <ol class="steps">
        {#each steps as step}
          <li class="step">
            <span class="step-number">{step.number}</span>
            <h3>{step.title}</h3>
            <p>{step.description}</p>
            <CardDetailButton
              title={step.title}
              description={step.description}
              details={[
                step.title === "Explorar"
                  ? "Se aclara el problema, las personas usuarias y el contexto antes de decidir una solución."
                  : step.title === "Prototipar"
                    ? "Se representa el flujo principal para revisar la idea y detectar dudas temprano."
                    : step.title === "Construir"
                      ? "La propuesta se implementa como una experiencia funcional y se valida con sus requisitos."
                      : "Se revisa el resultado, se corrigen detalles y se incorporan aprendizajes en nuevas iteraciones."
              ]}
              accent={color}
            />
          </li>
        {/each}
      </ol>
    </section>

    <footer class="page-footer">
      <div class="toolbelt">
        <span class="toolbelt-label">EN MI CAJA DE HERRAMIENTAS</span>
        <ul aria-label="Tecnologías">
          {#each tools as tool}
            <li>{tool}</li>
          {/each}
        </ul>
      </div>
      <a class="contact-link" href="mailto:Develop1998@outlook.es">
        ¿Construimos algo? <span aria-hidden="true">↗</span>
      </a>
    </footer>
  </div>
</main>

<style>
  .ideas-page {
    --accent: #b626ff;
    --surface: rgba(15, 17, 29, 0.88);
    --muted: #a4a8ba;
    position: relative;
    z-index: 1;
    min-height: 100vh;
    padding: clamp(1.25rem, 4vw, 3.5rem);
    color: #f7f5ff;
    background:
      radial-gradient(ellipse at 82% 10%, color-mix(in srgb, var(--accent) 15%, transparent), transparent 34rem),
      linear-gradient(145deg, #0b0c14 0%, #111322 55%, #0c0d16 100%);
    font-family: Inter, "Segoe UI", sans-serif;
  }

  .page-shell {
    width: min(1120px, 100%);
    margin: 0 auto;
  }

  .topline,
  .page-footer,
  .process-heading,
  .card-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .topline {
    padding-bottom: 1.2rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.12);
  }

  .brand {
    color: #fff;
    font-size: 1.1rem;
    font-weight: 800;
    letter-spacing: 0.12em;
    text-decoration: none;
  }

  .brand span {
    color: var(--accent);
  }

  .section-label,
  .eyebrow,
  .toolbelt-label {
    color: #c1c3d0;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.16em;
  }

  .status-dot {
    display: inline-block;
    width: 7px;
    height: 7px;
    margin-right: 0.5rem;
    border-radius: 50%;
    background: var(--accent);
    box-shadow: 0 0 12px var(--accent);
  }

  .hero {
    display: grid;
    min-height: 430px;
    grid-template-columns: 1.1fr 0.9fr;
    align-items: center;
    gap: 2rem;
    padding: 3.6rem 0 3rem;
  }

  .hero-copy {
    position: relative;
    z-index: 1;
    max-width: 610px;
  }

  .eyebrow {
    margin: 0 0 1rem;
    color: var(--accent);
  }

  h1,
  h2,
  h3,
  p {
    margin-top: 0;
  }

  h1 {
    max-width: 650px;
    margin-bottom: 1.1rem;
    color: #f7f5ff;
    font-size: clamp(2.6rem, 6vw, 5rem);
    font-weight: 750;
    letter-spacing: -0.065em;
    line-height: 1.02;
  }

  h1 span {
    color: var(--accent);
  }

  .intro {
    max-width: 510px;
    margin-bottom: 1.7rem;
    color: #b8bbca;
    font-size: clamp(0.98rem, 1.7vw, 1.1rem);
    line-height: 1.8;
  }

  .text-link,
  .contact-link {
    display: inline-flex;
    align-items: center;
    gap: 0.7rem;
    color: #fff;
    font-weight: 700;
    text-decoration: none;
  }

  .text-link span,
  .contact-link span {
    color: var(--accent);
    transition: transform 180ms ease;
  }

  .text-link:hover span,
  .contact-link:hover span {
    transform: translate(3px, -3px);
  }

  .hero-art {
    position: relative;
    display: grid;
    min-height: 340px;
    place-items: center;
    overflow: hidden;
  }

  .orbit {
    position: absolute;
    width: min(72vw, 310px);
    aspect-ratio: 1;
    border: 1px solid rgba(255, 255, 255, 0.13);
    border-radius: 50%;
    transform: rotate(-24deg) scaleY(0.55);
  }

  .orbit-two {
    transform: rotate(38deg) scaleY(0.55);
  }

  .orbit-three {
    transform: rotate(90deg) scaleY(0.55);
    border-color: color-mix(in srgb, var(--accent) 40%, transparent);
  }

  .core {
    display: grid;
    width: 118px;
    aspect-ratio: 1;
    place-items: center;
    border: 1px solid color-mix(in srgb, var(--accent) 75%, white);
    border-radius: 34% 66% 57% 43% / 42% 42% 58% 58%;
    background: radial-gradient(circle at 35% 30%, color-mix(in srgb, var(--accent) 50%, #fff), #4d1f78 75%);
    box-shadow: 0 0 75px color-mix(in srgb, var(--accent) 45%, transparent), inset 0 0 24px rgba(255, 255, 255, 0.28);
    animation: float 6s ease-in-out infinite;
  }

  .core span {
    color: white;
    font-size: 3.3rem;
    font-weight: 800;
    letter-spacing: -0.1em;
    text-shadow: 0 3px 20px rgba(0, 0, 0, 0.3);
  }

  .orbit-label {
    position: absolute;
    color: #d7d4e4;
    font-size: 0.6rem;
    font-weight: 700;
    letter-spacing: 0.2em;
  }

  .label-top {
    top: 16%;
    right: 12%;
  }

  .label-bottom {
    bottom: 17%;
    left: 12%;
  }

  .spark {
    position: absolute;
    color: var(--accent);
    font-size: 1.2rem;
    text-shadow: 0 0 20px var(--accent);
  }

  .spark-one {
    top: 25%;
    left: 19%;
  }

  .spark-two {
    right: 22%;
    bottom: 25%;
    color: #62f3dc;
  }

  .principles,
  .process {
    padding: 2.5rem 0;
  }

  .section-heading {
    max-width: 650px;
    margin-bottom: 1.5rem;
  }

  .section-heading h2,
  .process h2 {
    margin-bottom: 0;
    font-size: clamp(1.65rem, 3.5vw, 2.5rem);
    letter-spacing: -0.045em;
  }

  .principle-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
  }

  .principle-card {
    min-height: 205px;
    padding: 1.4rem;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 18px;
    background: linear-gradient(145deg, rgba(255, 255, 255, 0.065), rgba(255, 255, 255, 0.018));
    transition: border-color 180ms ease, transform 180ms ease, background 180ms ease;
  }

  .principle-card:hover {
    transform: translateY(-4px);
    border-color: color-mix(in srgb, var(--accent) 60%, transparent);
    background: linear-gradient(145deg, color-mix(in srgb, var(--accent) 12%, #171725), rgba(255, 255, 255, 0.025));
  }

  .card-number {
    color: #8d90a3;
    font-size: 0.72rem;
    font-weight: 700;
  }

  .card-icon {
    color: var(--accent);
    font-size: 1.4rem;
  }

  .principle-card h3 {
    margin: 1.6rem 0 0.55rem;
    font-size: 1.05rem;
  }

  .principle-card p,
  .step p,
  .process-note {
    margin-bottom: 0;
    color: var(--muted);
    font-size: 0.88rem;
    line-height: 1.7;
  }

  .process {
    margin-top: 1rem;
    padding: 2rem;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 22px;
    background: var(--surface);
  }

  .process-heading {
    align-items: flex-end;
    gap: 1rem;
  }

  .process-note {
    max-width: 260px;
    text-align: right;
  }

  .steps {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 1.2rem;
    margin: 2rem 0 0;
    padding: 0;
    list-style: none;
  }

  .step {
    position: relative;
    padding-top: 1.25rem;
    border-top: 1px solid color-mix(in srgb, var(--accent) 45%, transparent);
  }

  .step-number {
    color: var(--accent);
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.1em;
  }

  .step h3 {
    margin: 0.75rem 0 0.4rem;
    font-size: 1rem;
  }

  .step p {
    font-size: 0.8rem;
  }

  .page-footer {
    flex-wrap: wrap;
    gap: 1.5rem;
    margin-top: 1.5rem;
    padding: 1.7rem 0 0.5rem;
    border-top: 1px solid rgba(255, 255, 255, 0.12);
  }

  .toolbelt-label {
    display: block;
    margin-bottom: 0.8rem;
    color: #8f92a4;
    font-size: 0.58rem;
  }

  .toolbelt ul {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .toolbelt li {
    padding: 0.35rem 0.7rem;
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 999px;
    color: #d6d5e0;
    font-size: 0.73rem;
  }

  .contact-link {
    padding: 0.8rem 1rem;
    border: 1px solid color-mix(in srgb, var(--accent) 50%, transparent);
    border-radius: 999px;
    transition: background 180ms ease;
  }

  .contact-link:hover {
    background: color-mix(in srgb, var(--accent) 14%, transparent);
  }

  @keyframes float {
    0%, 100% { transform: translateY(0) rotate(-8deg); }
    50% { transform: translateY(-10px) rotate(5deg); }
  }

  @media (max-width: 760px) {
    .hero {
      min-height: auto;
      grid-template-columns: 1fr;
      gap: 0;
      padding-top: 3rem;
    }

    .hero-art {
      min-height: 260px;
    }

    .principle-grid {
      grid-template-columns: 1fr;
    }

    .principle-card {
      min-height: 0;
    }

    .principle-card h3 {
      margin-top: 1rem;
    }

    .process {
      padding: 1.35rem;
    }

    .steps {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }

  @media (max-width: 480px) {
    .section-label {
      font-size: 0.55rem;
    }

    .process-heading {
      align-items: flex-start;
      flex-direction: column;
    }

    .process-note {
      max-width: 100%;
      text-align: left;
    }

    .steps {
      gap: 1.5rem 1rem;
    }

    .page-footer {
      align-items: flex-start;
      flex-direction: column;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      scroll-behavior: auto !important;
      transition-duration: 0.01ms !important;
    }
  }
</style>
