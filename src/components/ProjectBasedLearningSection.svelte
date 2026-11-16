<script>
  const focusAreas = [
    {
      icon: "✳",
      title: "Aprendizaje activo",
      description: "Experiencias donde aprender significa explorar, participar y llevar ideas a la práctica.",
    },
    {
      icon: "⌘",
      title: "Colaboración",
      description: "Intercambio de ideas, trabajo en equipo y construcción compartida de conocimiento.",
    },
    {
      icon: "◉",
      title: "Enseñanza digital",
      description: "Uso intencional de recursos y herramientas digitales para enriquecer el aprendizaje.",
    },
    {
      icon: "↗",
      title: "Habilidades para el futuro",
      description: "Creatividad, comunicación y pensamiento crítico como parte de la experiencia educativa.",
    },
  ];
</script>

<section class="pbl-section" aria-labelledby="pbl-title">
  <div class="pbl-inner">
    <header class="pbl-heading">
      <p class="eyebrow"><span aria-hidden="true">✦</span> FORMACIÓN COMPLEMENTARIA</p>
      <div class="title-lockup">
        <span class="learning-mark" aria-hidden="true">
          <span class="mark-orbit orbit-one"></span>
          <span class="mark-orbit orbit-two"></span>
          <span class="mark-core">P</span>
          <span class="mark-dot"></span>
        </span>
        <div>
          <p class="diploma-label">DIPLOMATURA EN</p>
          <h2 id="pbl-title">Aprendizaje Basado en Proyectos</h2>
        </div>
      </div>
      <p class="intro">
        Una mirada a la enseñanza moderna que pone la curiosidad, la creatividad y la participación
        en el centro del aprendizaje.
      </p>
      <span class="discipline">APRENDER <i>·</i> COLABORAR <i>·</i> CREAR</span>
    </header>

    <div class="focus-areas">
      <p class="focus-heading">UNA EDUCACIÓN PARA PARTICIPAR Y EVOLUCIONAR</p>
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

    <footer class="learning-note">
      <span class="note-icon" aria-hidden="true">✦</span>
      <p>
        <strong>Aprendizaje con sentido.</strong>
        Metodologías activas y herramientas digitales para acompañar nuevas formas de enseñar y aprender.
      </p>
    </footer>
  </div>
</section>

<style>
  .pbl-section {
    position: relative;
    overflow: hidden;
    padding: clamp(3rem, 7vw, 5.5rem) 1.25rem;
    color: #f3f6ff;
    background:
      radial-gradient(ellipse at 12% 48%, rgba(80, 190, 255, 0.09), transparent 29rem),
      linear-gradient(145deg, rgba(13, 19, 30, 0.8), rgba(11, 12, 20, 0.74));
  }

  .pbl-section::before {
    position: absolute;
    top: -13rem;
    right: -9rem;
    width: 27rem;
    aspect-ratio: 1;
    border: 1px solid rgba(98, 201, 255, 0.07);
    border-radius: 50%;
    box-shadow: 0 0 0 3rem rgba(98, 201, 255, 0.018), 0 0 0 6rem rgba(98, 201, 255, 0.012);
    content: "";
    pointer-events: none;
  }

  .pbl-inner {
    position: relative;
    display: grid;
    grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr);
    align-items: center;
    gap: clamp(2rem, 6vw, 5rem);
    width: min(1120px, 100%);
    margin: 0 auto;
  }

  .pbl-heading {
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
    color: #83d6ff;
  }

  .eyebrow span {
    font-size: 1rem;
  }

  .title-lockup {
    display: flex;
    align-items: center;
    gap: clamp(0.9rem, 2.5vw, 1.5rem);
  }

  .learning-mark {
    position: relative;
    display: grid;
    flex: 0 0 clamp(3.8rem, 8vw, 5.4rem);
    aspect-ratio: 1;
    place-items: center;
  }

  .mark-orbit {
    position: absolute;
    inset: 8%;
    border: 1px solid rgba(131, 214, 255, 0.45);
    border-radius: 50%;
  }

  .orbit-one {
    transform: rotate(-35deg) scaleY(0.52);
  }

  .orbit-two {
    transform: rotate(35deg) scaleY(0.52);
  }

  .mark-core {
    display: grid;
    width: 2rem;
    aspect-ratio: 1;
    place-items: center;
    color: #10202a;
    border-radius: 50%;
    background: linear-gradient(135deg, #c0edff, #65caff);
    box-shadow: 0 0 25px rgba(80, 190, 255, 0.28);
    font-size: 1rem;
    font-weight: 900;
  }

  .mark-dot {
    position: absolute;
    top: 10%;
    right: 12%;
    width: 0.48rem;
    aspect-ratio: 1;
    border-radius: 50%;
    background: #d7f4ff;
    box-shadow: 0 0 14px rgba(131, 214, 255, 0.85);
  }

  .diploma-label {
    margin: 0 0 0.35rem;
    color: #a4b9c9;
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
    color: #b7c1cc;
    font-size: 0.94rem;
    line-height: 1.7;
  }

  .discipline {
    color: #95dfff;
    font-size: 0.57rem;
  }

  .discipline i {
    padding: 0 0.25rem;
    color: #587d91;
    font-style: normal;
  }

  .focus-heading {
    margin: 0 0 0.7rem;
    color: #83d6ff;
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
    background: linear-gradient(90deg, rgba(80, 190, 255, 0.09), transparent);
  }

  .area-icon {
    display: grid;
    width: 2.3rem;
    aspect-ratio: 1;
    place-items: center;
    color: #a4e2ff;
    border: 1px solid rgba(98, 201, 255, 0.24);
    border-radius: 12px;
    background: rgba(80, 190, 255, 0.07);
    font-size: 1rem;
    transition: transform 200ms ease, background 200ms ease;
  }

  li:hover .area-icon {
    transform: rotate(-7deg) scale(1.06);
    background: rgba(80, 190, 255, 0.15);
  }

  .area-number {
    align-self: start;
    padding-top: 0.25rem;
    color: #7f9daf;
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
    color: #b0bbc7;
    font-size: 0.73rem;
    line-height: 1.5;
  }

  .area-arrow {
    color: #83d6ff;
    opacity: 0;
    transform: translate(-3px, 3px);
    transition: opacity 180ms ease, transform 180ms ease;
  }

  li:hover .area-arrow {
    opacity: 1;
    transform: translate(0);
  }

  .learning-note {
    display: flex;
    grid-column: 1 / -1;
    align-items: flex-start;
    gap: 0.75rem;
    margin-top: -1rem;
    padding: 0.9rem 1rem;
    border: 1px solid rgba(98, 201, 255, 0.17);
    border-radius: 14px;
    background: rgba(80, 190, 255, 0.035);
  }

  .note-icon {
    color: #83d6ff;
    font-size: 1.05rem;
  }

  .learning-note p {
    display: grid;
    gap: 0.2rem;
    margin: 0;
    color: #b7c1cc;
    font-size: 0.78rem;
    line-height: 1.55;
  }

  .learning-note strong {
    color: #f3f6ff;
  }

  @media (max-width: 760px) {
    .pbl-inner {
      grid-template-columns: 1fr;
      gap: 2rem;
    }

    .learning-note {
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
    li,
    .area-icon,
    .area-arrow {
      transition: none;
    }
  }
</style>
