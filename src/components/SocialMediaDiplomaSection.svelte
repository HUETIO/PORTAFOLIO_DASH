<script>
  const focusAreas = [
    {
      number: "01",
      title: "Estrategia digital",
      description: "Planificación de objetivos, audiencias y presencia de marca en redes sociales.",
      icon: "◎",
    },
    {
      number: "02",
      title: "Contenido y comunicación",
      description: "Ideas y mensajes adaptados a cada plataforma y comunidad.",
      icon: "✳",
    },
    {
      number: "03",
      title: "Gestión de comunidades",
      description: "Interacción, escucha y construcción de relaciones con las audiencias.",
      icon: "◌",
    },
    {
      number: "04",
      title: "Métricas y optimización",
      description: "Lectura de resultados para aprender y mejorar las acciones digitales.",
      icon: "↗",
    },
  ];
</script>

<section class="social-diploma" aria-labelledby="social-diploma-title">
  <div class="social-inner">
    <div class="diploma-intro">
      <p class="eyebrow"><span aria-hidden="true">✦</span> FORMACIÓN COMPLEMENTARIA</p>
      <div class="title-lockup">
        <span class="orbit-mark" aria-hidden="true">
          <span class="orbit orbit-one"></span>
          <span class="orbit orbit-two"></span>
          <span class="orbit-core">S</span>
          <span class="orbit-dot"></span>
        </span>
        <div>
          <p class="diploma-label">DIPLOMATURA EN</p>
          <h2 id="social-diploma-title">Social Media<br />Management</h2>
        </div>
      </div>
      <p class="intro">
        Una mirada estratégica a la comunicación digital: conectar marcas con personas, crear
        contenido con intención y aprender de cada interacción.
      </p>
      <span class="discipline">ESTRATEGIA <i>·</i> CONTENIDO <i>·</i> COMUNIDAD</span>
    </div>

    <div class="focus-areas">
      <p class="focus-heading">ÁREAS DE ENFOQUE</p>
      <ol>
        {#each focusAreas as area}
          <li>
            <span class="area-icon" aria-hidden="true">{area.icon}</span>
            <span class="area-number">{area.number}</span>
            <div class="area-copy">
              <h3>{area.title}</h3>
              <p>{area.description}</p>
            </div>
            <span class="area-arrow" aria-hidden="true">↗</span>
          </li>
        {/each}
      </ol>
    </div>
  </div>
</section>

<style>
  .social-diploma {
    position: relative;
    overflow: hidden;
    padding: clamp(3.5rem, 8vw, 7rem) 1.25rem;
    color: #f7f3fa;
    background:
      radial-gradient(ellipse at 18% 55%, rgba(245, 105, 179, 0.1), transparent 28rem),
      linear-gradient(135deg, rgba(20, 13, 27, 0.88), rgba(13, 15, 25, 0.78));
  }

  .social-diploma::after {
    position: absolute;
    right: -9rem;
    bottom: -16rem;
    width: 30rem;
    aspect-ratio: 1;
    border: 1px solid rgba(255, 139, 202, 0.08);
    border-radius: 50%;
    box-shadow: 0 0 0 3rem rgba(255, 139, 202, 0.025), 0 0 0 6rem rgba(255, 139, 202, 0.016);
    content: "";
    pointer-events: none;
  }

  .social-inner {
    position: relative;
    z-index: 1;
    display: grid;
    grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr);
    gap: clamp(2.5rem, 8vw, 7rem);
    align-items: center;
    width: min(1120px, 100%);
    margin: 0 auto;
  }

  .eyebrow,
  .diploma-label,
  .focus-heading,
  .discipline {
    font-size: 0.66rem;
    font-weight: 750;
    letter-spacing: 0.14em;
  }

  .eyebrow {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin: 0 0 2rem;
    color: #ff9ccc;
  }

  .eyebrow span {
    font-size: 1rem;
  }

  .title-lockup {
    display: flex;
    align-items: center;
    gap: clamp(1rem, 3vw, 1.8rem);
  }

  .orbit-mark {
    position: relative;
    display: grid;
    flex: 0 0 clamp(4.5rem, 10vw, 7rem);
    aspect-ratio: 1;
    place-items: center;
  }

  .orbit {
    position: absolute;
    inset: 9%;
    border: 1px solid rgba(255, 156, 204, 0.48);
    border-radius: 50%;
  }

  .orbit-one {
    transform: rotate(-35deg) scaleY(0.52);
  }

  .orbit-two {
    transform: rotate(35deg) scaleY(0.52);
  }

  .orbit-core {
    display: grid;
    width: 2.45rem;
    aspect-ratio: 1;
    place-items: center;
    color: #211321;
    border-radius: 50%;
    background: linear-gradient(135deg, #ffc2df, #ff74b6);
    box-shadow: 0 0 30px rgba(255, 116, 182, 0.3);
    font-size: 1.15rem;
    font-weight: 900;
  }

  .orbit-dot {
    position: absolute;
    top: 10%;
    right: 12%;
    width: 0.55rem;
    aspect-ratio: 1;
    border-radius: 50%;
    background: #ffe2f0;
    box-shadow: 0 0 15px rgba(255, 156, 204, 0.9);
  }

  .diploma-label {
    margin: 0 0 0.4rem;
    color: #b7a9b8;
  }

  h2 {
    margin: 0;
    font-size: clamp(2rem, 4.5vw, 3.5rem);
    letter-spacing: -0.055em;
    line-height: 1.02;
  }

  .intro {
    max-width: 470px;
    margin: 1.5rem 0;
    color: #bdb4c2;
    font-size: 0.97rem;
    line-height: 1.75;
  }

  .discipline {
    color: #ffabd1;
    font-size: 0.58rem;
  }

  .discipline i {
    padding: 0 0.25rem;
    color: #8d6a80;
    font-style: normal;
  }

  .focus-heading {
    margin: 0 0 0.7rem;
    color: #ff9ccc;
  }

  ol {
    margin: 0;
    padding: 0;
    border-top: 1px solid rgba(255, 255, 255, 0.13);
    list-style: none;
  }

  li {
    display: grid;
    grid-template-columns: 2.5rem 2rem minmax(0, 1fr) 1.2rem;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem 0.25rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.13);
    transition: padding 200ms ease, background 200ms ease;
  }

  li:hover {
    padding-right: 0.8rem;
    padding-left: 0.8rem;
    background: linear-gradient(90deg, rgba(245, 105, 179, 0.1), transparent);
  }

  .area-icon {
    display: grid;
    width: 2.3rem;
    aspect-ratio: 1;
    place-items: center;
    color: #ffabd1;
    border: 1px solid rgba(255, 156, 204, 0.25);
    border-radius: 12px;
    background: rgba(245, 105, 179, 0.08);
    font-size: 1rem;
    transition: transform 200ms ease, background 200ms ease;
  }

  li:hover .area-icon {
    transform: rotate(-8deg) scale(1.06);
    background: rgba(245, 105, 179, 0.18);
  }

  .area-number {
    align-self: start;
    padding-top: 0.25rem;
    color: #9c8b9b;
    font-size: 0.62rem;
    font-weight: 700;
    letter-spacing: 0.1em;
  }

  .area-copy h3 {
    margin: 0;
    font-size: 0.95rem;
    font-weight: 700;
  }

  .area-copy p {
    margin: 0.25rem 0 0;
    color: #b7aebb;
    font-size: 0.77rem;
    line-height: 1.55;
  }

  .area-arrow {
    color: #ff9ccc;
    opacity: 0;
    transform: translate(-4px, 4px);
    transition: opacity 180ms ease, transform 180ms ease;
  }

  li:hover .area-arrow {
    opacity: 1;
    transform: translate(0, 0);
  }

  @media (max-width: 760px) {
    .social-inner {
      grid-template-columns: 1fr;
      gap: 2.5rem;
    }

    .intro {
      max-width: 620px;
    }
  }

  @media (max-width: 420px) {
    li {
      grid-template-columns: 2.3rem minmax(0, 1fr) 1rem;
      gap: 0.6rem;
    }

    .area-number {
      display: none;
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
