<script>
  export let onStartDiscovery = () => {};

  const experiences = [
    {
      organization: "Axa Colpatria",
      sector: "Seguros",
      platforms: ["Athento", "Viafirma", "Java", "React"],
      challenge:
        "Programas internos que fallaban al comunicarse entre sí y que necesitaban integrar herramientas nuevas.",
      work:
        "Automatización de flujos documentales, formularios dinámicos e integración con firma electrónica.",
      result: "Procesos con trazabilidad de documentos y menos pasos manuales.",
    },
    {
      organization: "OSC Top Solutions Group",
      sector: "Tecnología",
      platforms: ["Zoho CRM", "Alfresco", "Svelte", "Node.js", "Python", "Firebase"],
      challenge:
        "Procesos manuales para comunicar varios programas entre sí, con la meta de apoyarlos con inteligencia artificial.",
      work:
        "Scripts e interfaces que conectan las aplicaciones y mejoras a la base de datos del CRM.",
      result: "Comunicación más fluida entre aplicaciones y datos más íntegros.",
    },
    {
      organization: "GJX",
      sector: "Desarrollo de software",
      platforms: ["React", "PostgreSQL"],
      challenge: "Páginas ya creadas con fallos que necesitaban actualización digital.",
      work:
        "Pruebas y rehabilitación de código antiguo, nuevas interfaces y corrección de procedimientos en la base de datos.",
      result: "Un sistema más estable y eficiente.",
    },
    {
      organization: "Grupo ACI",
      sector: "Industria",
      platforms: ["Siemens Opcenter", "AngularJS", "SQL Server", "Python", "C++", "Java"],
      challenge:
        "Programar máquinas industriales y conectar la planta con su software de comunicación.",
      work:
        "Consultas y APIs que comunican la planta con sus sistemas y scripts de extracción de datos a CSV.",
      result: "Datos de planta disponibles y listos para analizar.",
    },
  ];
</script>

<section class="team-experience" aria-labelledby="team-experience-title">
  <div class="experience-inner">
    <header class="experience-heading">
      <p class="eyebrow">EXPERIENCIA PREVIA DEL EQUIPO</p>
      <h2 id="team-experience-title">Experiencia en entornos como el tuyo</h2>
    </header>

    <div class="experience-grid">
      {#each experiences as experience}
        <article class="experience-card">
          <header class="card-heading">
            <div>
              <h3>{experience.organization}</h3>
              <p class="sector">{experience.sector}</p>
            </div>
            <span class="organization-mark" aria-hidden="true">✳</span>
          </header>

          <ul class="platform-list" aria-label={`Plataformas: ${experience.platforms.join(", ")}`}>
            {#each experience.platforms as platform}
              <li>{platform}</li>
            {/each}
          </ul>

          <dl class="experience-details">
            <div>
              <dt>El reto</dt>
              <dd>{experience.challenge}</dd>
            </div>
            <div>
              <dt>Lo que se hizo</dt>
              <dd>{experience.work}</dd>
            </div>
            <div class="result">
              <dt>Resultado</dt>
              <dd>{experience.result}</dd>
            </div>
          </dl>
        </article>
      {/each}
    </div>

    <div class="experience-cta">
      <button class="hero-action hero-action--primary" type="button" on:click={onStartDiscovery}>
        Hablemos de tu proceso <span aria-hidden="true">↗</span>
      </button>
    </div>
  </div>
</section>

<style>
  .team-experience {
    padding: clamp(3.5rem, 8vw, 6.5rem) 1.25rem;
    color: #f7f5ff;
    background:
      radial-gradient(ellipse at 92% 8%, rgba(125, 168, 255, 0.1), transparent 32rem),
      linear-gradient(180deg, #0b0c14, #101320);
  }

  .experience-inner {
    width: min(1120px, 100%);
    margin: 0 auto;
  }

  .experience-heading {
    max-width: 760px;
    margin: 0 auto clamp(1.75rem, 4vw, 2.75rem);
    text-align: center;
  }

  .eyebrow {
    margin: 0 0 0.75rem;
    color: #00f5d4;
    font-size: 0.7rem;
    font-weight: 750;
    letter-spacing: 0.14em;
  }

  h2 {
    margin: 0;
    font-size: clamp(1.8rem, 4.5vw, 3rem);
    letter-spacing: -0.045em;
    line-height: 1.15;
    text-wrap: balance;
  }

  .experience-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }

  .experience-card {
    min-width: 0;
    padding: clamp(1.1rem, 2.5vw, 1.5rem);
    border: 1px solid rgba(255, 255, 255, 0.14);
    border-radius: 20px;
    background: linear-gradient(145deg, rgba(255, 255, 255, 0.065), rgba(255, 255, 255, 0.025));
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.15);
  }

  .card-heading {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 0.75rem;
  }

  .card-heading h3 {
    margin: 0;
    font-size: clamp(1.15rem, 2.5vw, 1.4rem);
    letter-spacing: -0.025em;
    overflow-wrap: anywhere;
  }

  .sector {
    margin: 0.35rem 0 0;
    color: #cbd0df;
    font-size: 0.9rem;
  }

  .organization-mark {
    display: grid;
    flex: 0 0 2.25rem;
    aspect-ratio: 1;
    place-items: center;
    color: #00f5d4;
    border: 1px solid rgba(0, 245, 212, 0.28);
    border-radius: 12px;
    background: rgba(0, 245, 212, 0.08);
  }

  .platform-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin: 1rem 0 1.1rem;
    padding: 0;
    list-style: none;
  }

  .platform-list li {
    padding: 0.34rem 0.62rem;
    color: #e6e9f2;
    border: 1px solid rgba(125, 168, 255, 0.3);
    border-radius: 999px;
    background: rgba(125, 168, 255, 0.09);
    font-size: 0.75rem;
    font-weight: 650;
    line-height: 1.35;
  }

  .experience-details {
    display: grid;
    gap: 0.85rem;
    margin: 0;
  }

  .experience-details div {
    padding-top: 0.75rem;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
  }

  .experience-details dt {
    margin-bottom: 0.28rem;
    color: #00f5d4;
    font-size: 0.8rem;
    font-weight: 750;
  }

  .experience-details dd {
    margin: 0;
    color: #d7d9e3;
    font-size: 0.9rem;
    line-height: 1.6;
  }

  .experience-details .result dd {
    color: #f7f5ff;
    font-weight: 600;
  }

  .experience-cta {
    display: flex;
    justify-content: center;
    margin-top: clamp(1.75rem, 4vw, 2.5rem);
  }

  .hero-action {
    display: inline-flex;
    min-height: 46px;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.75rem 1.1rem;
    border: 1px solid rgba(0, 245, 212, 0.35);
    border-radius: 12px;
    font: inherit;
    font-weight: 750;
    text-align: center;
    text-decoration: none;
    cursor: pointer;
    transition: transform 180ms ease, border-color 180ms ease, background 180ms ease;
  }

  .hero-action--primary {
    color: #071413;
    background: #00bfa7;
  }

  .hero-action:hover {
    transform: translateY(-2px);
    border-color: #00f5d4;
    background: #00d9bd;
  }

  .hero-action:focus-visible {
    outline: 2px solid #00f5d4;
    outline-offset: 3px;
  }

  @media (max-width: 680px) {
    .experience-grid {
      grid-template-columns: 1fr;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .hero-action {
      transition: none;
    }
  }
</style>
