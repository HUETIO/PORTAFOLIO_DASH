<script>
  const focusAreas = [
    {
      icon: "⌘",
      title: "Fundamentos de Android Studio",
      description: "Entorno de desarrollo, estructura del proyecto y herramientas esenciales.",
    },
    {
      icon: "▣",
      title: "Interfaces móviles",
      description: "Diseño de pantallas adaptables y experiencias intuitivas para Android.",
    },
    {
      icon: "⟳",
      title: "Desarrollo y pruebas",
      description: "Construcción, ejecución y depuración de aplicaciones en emuladores y dispositivos.",
    },
    {
      icon: "⇄",
      title: "Integración y publicación",
      description: "Conexión con servicios y preparación de aplicaciones para su distribución.",
    },
  ];
</script>

<section class="mobile-diploma" aria-labelledby="mobile-diploma-title">
  <div class="mobile-inner">
    <header class="mobile-heading">
      <p class="eyebrow"><span aria-hidden="true">✦</span> FORMACIÓN EN DESARROLLO</p>
      <div class="title-lockup">
        <span class="android-mark" aria-hidden="true">
          <svg viewBox="0 0 48 48" fill="none">
            <path d="M13 18h22v15a3 3 0 0 1-3 3H16a3 3 0 0 1-3-3V18Z" />
            <path d="M11 23v9m26-9v9m-19 6v4m12-4v4M17 14l-3-5m17 5 3-5" />
            <path d="M13 18a11 11 0 0 1 22 0H13Z" />
            <circle cx="19" cy="14" r="1" />
            <circle cx="29" cy="14" r="1" />
          </svg>
        </span>
        <div>
          <p class="diploma-label">DIPLOMATURA EN</p>
          <h2 id="mobile-diploma-title">Programador de Aplicaciones Móviles</h2>
        </div>
      </div>
      <p class="intro">
        Formación orientada al desarrollo de aplicaciones Android con Android Studio: de la idea y
        la interfaz a una app funcional.
      </p>
      <span class="discipline">DISEÑAR <i>·</i> DESARROLLAR <i>·</i> PROBAR</span>
    </header>

    <div class="focus-areas">
      <p class="focus-heading">DESARROLLO MÓVIL CON ANDROID STUDIO</p>
      <ol>
        {#each focusAreas as area, index}
          <li>
            <span class="area-icon" aria-hidden="true">{area.icon}</span>
            <span class="area-number">0{index + 1}</span>
            <div class="area-copy">
              <h3>{area.title}</h3>
              <p>{area.description}</p>
            </div>
            <span class="area-arrow" aria-hidden="true">↗</span>
          </li>
        {/each}
      </ol>
    </div>

    <footer class="mobile-note">
      <span class="note-icon" aria-hidden="true">✦</span>
      <p>
        <strong>De aprender la herramienta a crear para móviles.</strong>
        Android Studio como entorno para diseñar, programar y validar experiencias móviles.
      </p>
    </footer>
  </div>
</section>

<style>
  .mobile-diploma {
    position: relative;
    overflow: hidden;
    padding: clamp(3rem, 7vw, 5.5rem) 1.25rem;
    color: #f3f8f2;
    background:
      radial-gradient(ellipse at 12% 48%, rgba(106, 220, 147, 0.09), transparent 29rem),
      linear-gradient(145deg, rgba(13, 23, 22, 0.8), rgba(11, 12, 20, 0.74));
  }

  .mobile-diploma::before {
    position: absolute;
    top: -13rem;
    right: -9rem;
    width: 27rem;
    aspect-ratio: 1;
    border: 1px solid rgba(106, 220, 147, 0.07);
    border-radius: 50%;
    box-shadow: 0 0 0 3rem rgba(106, 220, 147, 0.018), 0 0 0 6rem rgba(106, 220, 147, 0.012);
    content: "";
    pointer-events: none;
  }

  .mobile-inner {
    position: relative;
    display: grid;
    grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr);
    align-items: center;
    gap: clamp(2rem, 6vw, 5rem);
    width: min(1120px, 100%);
    margin: 0 auto;
  }

  .mobile-heading {
    max-width: 520px;
  }

  .eyebrow,
  .diploma-label,
  .discipline,
  .focus-heading {
    font-size: 0.64rem;
    font-weight: 750;
    letter-spacing: 0.14em;
  }

  .eyebrow {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin: 0 0 1.6rem;
    color: #8fe6ae;
  }

  .eyebrow span {
    font-size: 1rem;
  }

  .title-lockup {
    display: flex;
    align-items: center;
    gap: clamp(0.9rem, 2.5vw, 1.5rem);
  }

  .android-mark {
    display: grid;
    flex: 0 0 clamp(3.8rem, 8vw, 5.4rem);
    aspect-ratio: 1;
    place-items: center;
    color: #94e8b0;
    border: 1px solid rgba(106, 220, 147, 0.25);
    border-radius: 1.35rem;
    background: rgba(106, 220, 147, 0.08);
    box-shadow: 0 0 30px rgba(106, 220, 147, 0.1);
    transition: transform 220ms ease, box-shadow 220ms ease;
  }

  .android-mark:hover {
    transform: translateY(-3px) rotate(-5deg);
    box-shadow: 0 0 34px rgba(106, 220, 147, 0.2);
  }

  .android-mark svg {
    width: 2.8rem;
    stroke: currentColor;
    stroke-linecap: round;
    stroke-linejoin: round;
    stroke-width: 1.8;
  }

  .diploma-label {
    margin: 0 0 0.35rem;
    color: #a7bdb0;
  }

  h2 {
    margin: 0;
    font-size: clamp(1.7rem, 3.8vw, 2.8rem);
    letter-spacing: -0.055em;
    line-height: 1.08;
  }

  .intro {
    max-width: 440px;
    margin: 1.2rem 0 1rem;
    color: #b7c5bb;
    font-size: 0.94rem;
    line-height: 1.7;
  }

  .discipline {
    color: #9de8b6;
    font-size: 0.57rem;
  }

  .discipline i {
    padding: 0 0.25rem;
    color: #608670;
    font-style: normal;
  }

  .focus-heading {
    margin: 0 0 0.7rem;
    color: #8fe6ae;
    font-size: 0.6rem;
  }

  ol {
    margin: 0;
    padding: 0;
    border-top: 1px solid rgba(255, 255, 255, 0.13);
    list-style: none;
  }

  li {
    display: grid;
    grid-template-columns: 2.5rem 2rem minmax(0, 1fr) 1rem;
    align-items: center;
    gap: 0.7rem;
    padding: 0.85rem 0.25rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.13);
    transition: padding 200ms ease, background 200ms ease;
  }

  li:hover {
    padding-right: 0.75rem;
    padding-left: 0.75rem;
    background: linear-gradient(90deg, rgba(106, 220, 147, 0.09), transparent);
  }

  .area-icon {
    display: grid;
    width: 2.3rem;
    aspect-ratio: 1;
    place-items: center;
    color: #a7efbf;
    border: 1px solid rgba(106, 220, 147, 0.24);
    border-radius: 12px;
    background: rgba(106, 220, 147, 0.07);
    font-size: 1rem;
    transition: transform 200ms ease, background 200ms ease;
  }

  li:hover .area-icon {
    transform: rotate(-7deg) scale(1.06);
    background: rgba(106, 220, 147, 0.15);
  }

  .area-number {
    align-self: start;
    padding-top: 0.25rem;
    color: #80998a;
    font-size: 0.6rem;
    font-weight: 700;
    letter-spacing: 0.1em;
  }

  .area-copy h3 {
    margin: 0;
    font-size: 0.88rem;
  }

  .area-copy p {
    margin: 0.2rem 0 0;
    color: #b0bdb4;
    font-size: 0.73rem;
    line-height: 1.5;
  }

  .area-arrow {
    color: #8fe6ae;
    opacity: 0;
    transform: translate(-3px, 3px);
    transition: opacity 180ms ease, transform 180ms ease;
  }

  li:hover .area-arrow {
    opacity: 1;
    transform: translate(0);
  }

  .mobile-note {
    display: flex;
    grid-column: 1 / -1;
    align-items: flex-start;
    gap: 0.75rem;
    margin-top: -1rem;
    padding: 0.9rem 1rem;
    border: 1px solid rgba(106, 220, 147, 0.17);
    border-radius: 14px;
    background: rgba(106, 220, 147, 0.035);
  }

  .note-icon {
    color: #8fe6ae;
    font-size: 1.05rem;
  }

  .mobile-note p {
    display: grid;
    gap: 0.2rem;
    margin: 0;
    color: #b7c5bb;
    font-size: 0.78rem;
    line-height: 1.55;
  }

  .mobile-note strong {
    color: #f3f8f2;
  }

  @media (max-width: 760px) {
    .mobile-inner {
      grid-template-columns: 1fr;
      gap: 2rem;
    }

    .mobile-note {
      margin-top: -1rem;
    }
  }

  @media (max-width: 440px) {
    li {
      grid-template-columns: 2.2rem 1.6rem minmax(0, 1fr) 0.8rem;
      gap: 0.5rem;
      padding-right: 0.1rem;
      padding-left: 0.1rem;
    }

    .area-icon {
      width: 2rem;
    }

    .area-number {
      font-size: 0.55rem;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .android-mark,
    li,
    .area-icon,
    .area-arrow {
      transition: none;
    }
  }
</style>
