<section id="seguridad" class="enterprise-readiness" aria-labelledby="readiness-title">
  <div class="readiness-inner">
    <header class="readiness-heading">
      <p class="eyebrow">SOLUCIONES LISTAS PARA TU OPERACIÓN</p>
      <h2 id="readiness-title">Seguridad y claridad desde el primer paso.</h2>
      <p>
        Diseñamos cada iniciativa con atención a tus datos, accesos, continuidad y objetivos para que la solución encaje con tu forma de trabajar.
      </p>
    </header>

    <ul class="readiness-controls">
      <li>
        <h3>Datos bajo control</h3>
        <p>Claridad sobre la información que se usa, dónde vive y cómo se gestiona.</p>
      </li>
      <li>
        <h3>Accesos responsables</h3>
        <p>Permisos y responsabilidades pensados para proteger tu operación.</p>
      </li>
      <li>
        <h3>Continuidad operativa</h3>
        <p>Decisiones que ayudan a cuidar tus procesos y mantener el trabajo en marcha.</p>
      </li>
      <li>
        <h3>Integraciones confiables</h3>
        <p>Herramientas, servicios y cambios alineados con las necesidades de tu empresa.</p>
      </li>
      <li>
        <h3>Soporte claro</h3>
        <p>Un camino de atención definido para acompañar la solución.</p>
      </li>
      <li>
        <h3>Un piloto para avanzar</h3>
        <p>
          Valida una integración o flujo documental y descubre su potencial en tu operación.
        </p>
      </li>
    </ul>

    <p class="readiness-note">
      ¿Tienes un proceso que podría funcionar mejor? En DASH.IO te ayudamos a convertirlo en una oportunidad concreta.
    </p>
  </div>
</section>

<style>
  .enterprise-readiness {
    padding: clamp(3rem, 7vw, 5.5rem) 1.25rem;
    color: #f7f5ff;
    background: linear-gradient(145deg, #101722, #0b0c14 72%);
    scroll-margin-top: 80px;
  }

  .readiness-inner {
    width: min(1120px, 100%);
    margin: 0 auto;
  }

  .readiness-heading {
    max-width: 760px;
    margin: 0 auto 2rem;
    text-align: center;
  }

  .eyebrow {
    color: #00f5d4;
    font-size: 0.7rem;
    font-weight: 750;
    letter-spacing: 0.14em;
  }

  h2 {
    margin: 0.5rem 0;
    font-size: clamp(1.8rem, 4vw, 2.7rem);
    letter-spacing: -0.04em;
  }

  .readiness-heading > p:last-child,
  .readiness-controls p,
  .readiness-note {
    color: #b7bdc9;
    line-height: 1.65;
  }

  .readiness-controls {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .readiness-controls li {
    padding: 1.25rem;
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 1rem;
    background: rgba(255, 255, 255, 0.035);
  }

  .readiness-controls h3 {
    margin: 0 0 0.5rem;
    font-size: 1.05rem;
  }

  .readiness-controls p {
    margin: 0;
    font-size: 0.92rem;
  }

  .readiness-note {
    margin: 1.25rem auto 0;
    max-width: 850px;
    font-size: 0.86rem;
    text-align: center;
  }

  @media (max-width: 760px) {
    .readiness-controls {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }

  @media (max-width: 520px) {
    .readiness-controls {
      grid-template-columns: 1fr;
    }
  }
</style>
