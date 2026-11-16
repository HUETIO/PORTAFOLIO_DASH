<script>
  import CardDetailButton from "./components/CardDetailButton.svelte";

  export let projects = [];
  export let onStartDiscovery = () => {};
</script>

<div class="highlights">
  <div class="section-heading">
    <p class="eyebrow">SOLUCIONES DASH.IO</p>
    <h2 id="highlights-title">¿Qué podemos transformar en tu empresa?</h2>
    <p class="section-intro">
      Automatiza procesos, conecta tus sistemas y crea más espacio para que tu equipo avance.
    </p>
  </div>

  <div class="project-grid" aria-labelledby="highlights-title">
    {#each projects as project (project.number)}
      <article class="project-card" style:--project-accent={project.accent}>
        <div class="card-top">
          <span class="card-number">{project.number}</span>
          <span class="card-mark" aria-hidden="true">{project.mark}</span>
        </div>
        <p class="project-category">{project.category}</p>
        <h3>{project.title}</h3>
        <div class="project-details">
          <div class="project-detail">
            <span>EL RETO</span>
            <p>{project.challenge}</p>
          </div>
          <div class="project-detail">
            <span>LO QUE DASH.IO HACE POSIBLE</span>
            <p>{project.contribution}</p>
          </div>
          <div class="project-detail project-outcome">
            <span>LO QUE TU EQUIPO GANA</span>
            <p>{project.outcome}</p>
          </div>
        </div>
        <ul class="project-skills" aria-label={`Tecnologías y plataformas: ${project.title}`}>
          {#each project.skills as skill}
            <li>{skill}</li>
          {/each}
        </ul>
        <CardDetailButton
          title={project.title}
          description={project.challenge}
          details={[
            `Cómo te ayudamos: ${project.contribution}`,
            `Lo que tu equipo gana: ${project.outcome}`,
            `Tecnologías: ${project.skills.join(", ")}`,
          ]}
          accent={project.accent}
        />
      </article>
    {/each}
  </div>

  <button class="contact-cta" type="button" on:click={onStartDiscovery}>
    ¿Quieres que tu equipo trabaje mejor? <span aria-hidden="true">Hablemos con DASH.IO ↗</span>
  </button>
</div>

<style>
  .highlights {
    width: min(1200px, 100%);
    margin: 0 auto;
    padding: clamp(1.5rem, 4vw, 3.5rem);
    color: #f7f5ff;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 24px;
    background:
      radial-gradient(ellipse at 90% 0%, rgba(0, 245, 212, 0.1), transparent 34rem),
      linear-gradient(145deg, #0b0c14, #111322 58%, #0c0d16);
    box-shadow: 0 18px 55px rgba(0, 0, 0, 0.24);
  }

  .section-heading {
    max-width: 670px;
    margin-bottom: 1.75rem;
  }

  .eyebrow,
  .project-category {
    color: #00f5d4;
    font-size: 0.7rem;
    font-weight: 750;
    letter-spacing: 0.14em;
  }

  .eyebrow {
    margin: 0 0 0.65rem;
  }

  h2 {
    margin: 0;
    font-size: clamp(1.65rem, 3.6vw, 2.5rem);
    letter-spacing: -0.045em;
  }

  .section-intro {
    margin: 0.7rem 0 0;
    color: #b8bbca;
    line-height: 1.7;
  }

  .project-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }

  .project-card {
    display: flex;
    min-width: 0;
    flex-direction: column;
    padding: 1.35rem;
    border: 1px solid rgba(255, 255, 255, 0.11);
    border-radius: 18px;
    background: linear-gradient(155deg, rgba(20, 24, 40, 0.94), rgba(12, 15, 25, 0.94));
    transition: transform 180ms ease, border-color 180ms ease, background 180ms ease;
  }

  .project-card:hover {
    transform: translateY(-4px);
    border-color: color-mix(in srgb, var(--project-accent) 60%, transparent);
    background: linear-gradient(155deg, rgba(26, 31, 49, 0.97), rgba(14, 17, 29, 0.97));
  }

  .card-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1.4rem;
  }

  .card-number {
    color: #a4a8ba;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.12em;
  }

  .card-mark {
    display: grid;
    width: 2.6rem;
    aspect-ratio: 1;
    place-items: center;
    color: var(--project-accent);
    border: 1px solid color-mix(in srgb, var(--project-accent) 45%, transparent);
    border-radius: 13px;
    background: color-mix(in srgb, var(--project-accent) 12%, transparent);
    font-size: 1.25rem;
    font-weight: 800;
  }

  .project-category {
    margin: 0 0 0.5rem;
    color: var(--project-accent);
    font-size: 0.62rem;
  }

  .project-card h3 {
    margin: 0 0 0.65rem;
    color: #f7f5ff;
    font-size: 1.15rem;
    letter-spacing: -0.025em;
    line-height: 1.35;
  }

  .project-details {
    display: grid;
    flex: 1;
    align-content: start;
    gap: 0.7rem;
    margin: 0.35rem 0 1rem;
  }

  .project-detail {
    padding-left: 0.75rem;
    border-left: 2px solid rgba(255, 255, 255, 0.16);
  }

  .project-detail span {
    color: #a4a8ba;
    font-size: 0.58rem;
    font-weight: 750;
    letter-spacing: 0.12em;
  }

  .project-detail p {
    margin: 0.2rem 0 0;
    color: #d3d4df;
    font-size: 0.82rem;
    line-height: 1.45;
  }

  .project-outcome {
    border-color: var(--project-accent);
  }

  .project-skills {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .project-skills li {
    padding: 0.28rem 0.55rem;
    color: #d7d4e4;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 999px;
    font-size: 0.68rem;
  }

  .contact-cta {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 0.75rem;
    margin-top: 1.25rem;
    padding: 1rem 1.15rem;
    color: #f7f5ff;
    border: 1px solid rgba(0, 245, 212, 0.25);
    border-radius: 14px;
    background: rgba(0, 245, 212, 0.055);
    font: inherit;
    font-weight: 700;
    text-align: left;
    cursor: pointer;
    transition: border-color 180ms ease, background 180ms ease, transform 180ms ease;
  }

  .contact-cta:hover {
    transform: translateY(-2px);
    border-color: rgba(0, 245, 212, 0.55);
    background: rgba(0, 245, 212, 0.1);
  }

  .contact-cta span {
    color: #00f5d4;
  }

  .contact-cta:focus-visible {
    outline: 2px solid #00f5d4;
    outline-offset: 3px;
  }

  @media (max-width: 900px) {
    .project-grid { grid-template-columns: 1fr; }
  }

  @media (max-width: 620px) {
    .highlights {
      border-radius: 18px;
    }

    .project-grid {
      grid-template-columns: 1fr;
    }

    .project-card {
      padding: 1.15rem;
    }
  }
</style>