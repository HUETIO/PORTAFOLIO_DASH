<script>
  import CardDetailButton from "./components/CardDetailButton.svelte";

  export let onStartDiscovery = () => {};

  const documentPlatforms = [
    { name: "Athento", mark: "A", accent: "#48e5c2", style: "athento" },
    { name: "Alfresco", mark: "a", accent: "#7da8ff", style: "alfresco" },
    { name: "SharePoint", mark: "S", accent: "#c29aff", style: "sharepoint" },
    { name: "OpenText", mark: "O", accent: "#ffb86b", style: "opentext" },
    { name: "M-Files", mark: "M", accent: "#ff8ba7", style: "mfiles" },
  ];
</script>

<section
  class="business-services"
  aria-labelledby="business-services-title"
>
  <div class="section-copy">
    <p class="eyebrow">SOLUCIONES DASH.IO PARA EMPRESAS</p>
    <h2 id="business-services-title">
      ¿Cuánto podría avanzar tu empresa con sus procesos conectados?
    </h2>
    <p class="intro">
      En DASH.IO transformamos tareas repetitivas en flujos más ágiles e integramos tus documentos con las herramientas que tu equipo ya utiliza.
    </p>
  </div>

  <div class="service-grid" aria-label="Servicios para empresas">
    <article class="service-card" style:--service-accent="#48e5c2">
      <span class="service-icon" aria-hidden="true">↗</span>
      <h3>Libera a tu equipo de tareas repetitivas</h3>
      <p>
        Automatiza tareas y validaciones en flujos documentales y procesos conectados.
      </p>
      <CardDetailButton
        title="Automatización de procesos"
        description="DASH.IO diseña flujos para reducir tareas manuales y dar más claridad a la operación."
        details={["Identificamos los pasos repetitivos, los intercambios de información y los puntos de control.", "Definimos reglas, validaciones y responsables para automatizar con claridad.", "Alineamos la solución con los objetivos de tu equipo."]}
        accent="#48e5c2"
      />
    </article>

    <article class="service-card" style:--service-accent="#7da8ff">
      <span class="service-icon" aria-hidden="true">⌘</span>
      <h3>Haz que tus sistemas trabajen juntos</h3>
      <p>
        Conectamos gestores documentales con aplicaciones empresariales y sistemas existentes.
      </p>
      <CardDetailButton
        title="Software e integraciones"
        description="DASH.IO conecta tus aplicaciones o desarrolla software para una necesidad concreta."
        details={["Analizamos los sistemas, datos y necesidades de tu operación.", "Diseñamos integraciones mediante APIs y mecanismos compatibles.", "Creamos un camino claro para implementar y mantener la solución."]}
        accent="#7da8ff"
      />
    </article>

    <article class="service-card" style:--service-accent="#c29aff">
      <span class="service-icon" aria-hidden="true">✳</span>
      <h3>Prueba una idea y descubre su potencial</h3>
      <p>
        Valida un flujo y sus integraciones antes de considerar un despliegue más amplio.
      </p>
      <CardDetailButton
        title="Diagnóstico y piloto empresarial"
        description="Acota un flujo documental y valida una integración mediante un piloto."
        details={["El alcance inicial se limita a un flujo documental acordado.", "Los entregables pueden incluir mapa del proceso, requisitos de integración y una prueba de concepto, según lo acordado.", "Plazo, precio y criterios de éxito se validan en reuniones de alcance y quedan por escrito antes de iniciar."]}
        accent="#c29aff"
      />
    </article>
  </div>

  <div class="approach">
    <p class="approach-label">DE TU RETO A UNA SOLUCIÓN QUE AVANZA</p>
    <ol>
      <li><span>01</span>      <strong>Descubrimos la oportunidad</strong></li>
      <li><span>02</span>      <strong>Diseñamos el camino</strong></li>
      <li><span>03</span>      <strong>La hacemos realidad</strong></li>
    </ol>
    <p class="approach-note">
      Cada proyecto empieza con un objetivo claro y un primer paso pensado para tu empresa.
    </p>
  </div>

  <section class="document-platforms" aria-labelledby="document-platforms-title">
    <div class="platforms-copy">
      <p class="eyebrow">INTEGRACIÓN DOCUMENTAL</p>
      <h3 id="document-platforms-title">
        ¿Y si tus documentos pudieran impulsar toda tu operación?
      </h3>
      <p>
        DASH.IO conecta tus flujos documentales con las aplicaciones de negocio para que la información llegue donde hace falta, con menos pasos manuales.
      </p>
    </div>

    <ul class="platform-list" aria-label="Ejemplos de plataformas documentales">
      {#each documentPlatforms as platform}
        <li class="platform-card" style:--platform-accent={platform.accent}>
          <span class="platform-symbol {platform.style}" aria-hidden="true">
            {platform.mark}
          </span>
          <strong class="platform-wordmark {platform.style}">{platform.name}</strong>
        </li>
      {/each}
    </ul>

    <div class="integration-cta">
      <p>
        ¿Ya trabajas con alguna de estas plataformas? Conectémosla con los procesos y sistemas que impulsan tu negocio.
      </p>
      <button class="discovery-cta" type="button" on:click={onStartDiscovery}>
        Descubre nuevas posibilidades <span aria-hidden="true">↗</span>
      </button>
    </div>
  </section>
</section>

<style>
  .business-services {
    position: relative;
    isolation: isolate;
    width: min(1200px, 100%);
    margin: clamp(1.5rem, 4vw, 3rem) auto;
    scroll-margin-top: 5rem;
    padding: clamp(1.5rem, 4vw, 3.5rem);
    overflow: hidden;
    color: #f7f5ff;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 24px;
    background:
      radial-gradient(ellipse at 100% 0%, rgba(125, 168, 255, 0.13), transparent 34rem),
      linear-gradient(145deg, #0b0c14, #111322 58%, #0c0d16);
    box-shadow: 0 18px 55px rgba(0, 0, 0, 0.24);
  }

  .section-copy {
    max-width: 760px;
    margin-bottom: 2rem;
  }

  .eyebrow,
  .approach-label {
    margin: 0 0 0.7rem;
    color: #48e5c2;
    font-size: 0.7rem;
    font-weight: 750;
    letter-spacing: 0.14em;
  }

  h2 {
    margin: 0;
    font-size: clamp(1.8rem, 4vw, 3rem);
    letter-spacing: -0.045em;
    line-height: 1.15;
    text-wrap: balance;
  }

  .intro {
    max-width: 680px;
    margin: 0.9rem 0 0;
    color: #b8bbca;
    line-height: 1.75;
  }

  .service-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
  }

  .service-card {
    min-width: 0;
    padding: 1.35rem;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 18px;
    background: linear-gradient(155deg, rgba(255, 255, 255, 0.075), rgba(255, 255, 255, 0.025));
    transition: transform 180ms ease, border-color 180ms ease;
  }

  .service-card:hover {
    transform: translateY(-4px);
    border-color: color-mix(in srgb, var(--service-accent) 60%, transparent);
  }

  .service-icon {
    display: grid;
    width: 2.7rem;
    aspect-ratio: 1;
    margin-bottom: 1.2rem;
    place-items: center;
    color: var(--service-accent);
    border: 1px solid color-mix(in srgb, var(--service-accent) 45%, transparent);
    border-radius: 13px;
    background: color-mix(in srgb, var(--service-accent) 12%, transparent);
    font-size: 1.25rem;
    font-weight: 800;
  }

  .service-card h3 {
    margin: 0 0 0.55rem;
    font-size: 1.08rem;
    letter-spacing: -0.02em;
  }

  .service-card p {
    margin: 0;
    color: #b8bbca;
    font-size: 0.9rem;
    line-height: 1.7;
  }

  .approach {
    display: grid;
    grid-template-columns: minmax(180px, 0.7fr) 1.5fr;
    gap: 0.5rem 2rem;
    align-items: center;
    margin-top: 1.25rem;
    padding: 1.2rem 1.35rem;
    border: 1px solid rgba(72, 229, 194, 0.18);
    border-radius: 16px;
    background: rgba(72, 229, 194, 0.045);
  }

  .approach-label {
    margin: 0;
  }

  .approach ol {
    display: flex;
    flex-wrap: wrap;
    gap: 0.8rem 1.25rem;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .approach li {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: #e7e5ef;
    font-size: 0.82rem;
  }

  .approach li span {
    color: #48e5c2;
    font-size: 0.7rem;
    font-weight: 800;
  }

  .approach-note {
    grid-column: 2;
    margin: 0;
    color: #a4a8ba;
    font-size: 0.78rem;
  }

  .document-platforms {
    display: grid;
    grid-template-columns: minmax(0, 0.85fr) minmax(0, 1.15fr);
    gap: 1.5rem 2.5rem;
    align-items: center;
    margin-top: clamp(2rem, 5vw, 3.5rem);
    padding-top: clamp(1.5rem, 4vw, 2.5rem);
    border-top: 1px solid rgba(255, 255, 255, 0.1);
  }

  .platforms-copy {
    max-width: 520px;
  }

  .platforms-copy h3 {
    margin: 0;
    font-size: clamp(1.45rem, 2.7vw, 2.15rem);
    letter-spacing: -0.04em;
    line-height: 1.2;
    text-wrap: balance;
  }

  .platforms-copy > p:last-child,
  .integration-cta > p {
    margin: 0.75rem 0 0;
    color: #b8bbca;
    font-size: 0.9rem;
    line-height: 1.7;
  }

  .platform-list {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0.75rem;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .platform-card {
    display: flex;
    min-height: 88px;
    align-items: center;
    justify-content: center;
    gap: 0.55rem;
    padding: 0.85rem;
    border: 1px solid rgba(255, 255, 255, 0.11);
    border-radius: 14px;
    background: linear-gradient(145deg, rgba(255, 255, 255, 0.07), rgba(255, 255, 255, 0.025));
    transition: transform 180ms ease, border-color 180ms ease, background 180ms ease;
  }

  .platform-card:hover {
    transform: translateY(-3px);
    border-color: color-mix(in srgb, var(--platform-accent) 55%, transparent);
    background: color-mix(in srgb, var(--platform-accent) 8%, #10121d);
  }

  .platform-symbol {
    display: grid;
    flex: 0 0 1.8rem;
    width: 1.8rem;
    aspect-ratio: 1;
    place-items: center;
    color: var(--platform-accent);
    border: 1px solid color-mix(in srgb, var(--platform-accent) 50%, transparent);
    border-radius: 8px;
    background: color-mix(in srgb, var(--platform-accent) 12%, transparent);
    font-size: 1rem;
    font-weight: 800;
  }

  .platform-symbol.alfresco,
  .platform-wordmark.alfresco {
    font-family: Georgia, serif;
  }

  .platform-wordmark {
    color: #f2f1f8;
    font-size: clamp(0.82rem, 1.4vw, 1rem);
    letter-spacing: -0.03em;
    white-space: nowrap;
  }

  .platform-wordmark.sharepoint {
    font-weight: 600;
  }

  .integration-cta {
    display: flex;
    grid-column: 1 / -1;
    align-items: center;
    justify-content: space-between;
    gap: 1.25rem;
    padding: 1.1rem 1.25rem;
    border: 1px solid rgba(72, 229, 194, 0.2);
    border-radius: 15px;
    background: rgba(72, 229, 194, 0.045);
  }

  .integration-cta > p {
    max-width: 620px;
    margin: 0;
  }

  .discovery-cta {
    display: inline-flex;
    flex: 0 0 auto;
    align-items: center;
    gap: 0.7rem;
    min-height: 46px;
    padding: 0.65rem 1rem;
    border: 1px solid rgba(72, 229, 194, 0.5);
    border-radius: 999px;
    background: rgba(72, 229, 194, 0.12);
    color: #75f0d2;
    font-size: 0.85rem;
    font-weight: 700;
    transition: background 180ms ease, border-color 180ms ease, transform 180ms ease;
  }

  .discovery-cta:hover {
    transform: translateY(-2px);
    border-color: #48e5c2;
    background: rgba(72, 229, 194, 0.2);
    color: #fff;
  }

  .discovery-cta:focus-visible {
    outline: 2px solid #48e5c2;
    outline-offset: 3px;
  }

  @media (max-width: 760px) {
    .business-services {
      border-radius: 18px;
    }

    .service-grid {
      grid-template-columns: 1fr;
    }

    .service-card {
      padding: 1.15rem;
    }

    .approach {
      grid-template-columns: 1fr;
      gap: 0.8rem;
    }

    .approach-note {
      grid-column: 1;
    }

    .document-platforms {
      grid-template-columns: 1fr;
      gap: 1.25rem;
    }

    .platform-list {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .integration-cta {
      align-items: flex-start;
      flex-direction: column;
    }

  }

  @media (prefers-reduced-motion: reduce) {
    .service-card,
    .platform-card,
    .discovery-cta {
      transition: none;
    }

    .service-card:hover,
    .platform-card:hover,
    .discovery-cta:hover {
      transform: none;
    }
  }
</style>
