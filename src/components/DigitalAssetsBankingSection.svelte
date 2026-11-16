<section class="digital-assets" aria-labelledby="digital-assets-title">
  <div class="assets-inner">
    <header class="assets-heading">
      <p class="eyebrow"><span aria-hidden="true">✦</span> FINANZAS Y TECNOLOGÍA</p>
      <p class="overline">DASH.IO · FINANZAS DIGITALES</p>
      <h2 id="digital-assets-title">¿Qué nuevas posibilidades puede abrir blockchain para tu entidad?</h2>
      <p class="intro">
        Descubre oportunidades para innovar en activos digitales, validar transacciones y crear nuevos flujos para tu negocio.
      </p>
    </header>

    <div class="opportunity-list">
      <article class="opportunity">
        <div class="opportunity-icon mining-icon" aria-hidden="true">
          <svg viewBox="0 0 48 48" fill="none">
            <path d="m24 5 17 9.5v19L24 43 7 33.5v-19L24 5Z" />
            <path d="m7.5 14.5 16.5 9 16.5-9M24 24v18.5M16 10l17 9.5v9" />
            <circle cx="24" cy="24" r="3" />
          </svg>
        </div>
        <div class="opportunity-copy">
          <span class="opportunity-type">REDES BLOCKCHAIN</span>
          <h3>Minería y validación</h3>
          <p>
            Evaluamos casos de uso vinculados a la operación de redes, validación de transacciones
            y activos digitales, considerando infraestructura, eficiencia y controles.
          </p>
        </div>
        <span class="opportunity-number" aria-hidden="true">01</span>
      </article>

      <article class="opportunity">
        <div class="opportunity-icon token-icon" aria-hidden="true">
          <svg viewBox="0 0 48 48" fill="none">
            <circle cx="24" cy="24" r="17" />
            <path d="M17 19h14M17 24h14M17 29h9" />
            <path d="m32 7 2.5 5.5L40 15l-5.5 2.5L32 23l-2.5-5.5L24 15l5.5-2.5L32 7Z" />
          </svg>
        </div>
        <div class="opportunity-copy">
          <span class="opportunity-type">ACTIVOS DIGITALES</span>
          <h3>Tokenización</h3>
          <p>
            Diseñamos y prototipamos formas de representar activos digitalmente para explorar
            trazabilidad, automatización y nuevos flujos operativos.
          </p>
        </div>
        <span class="opportunity-number" aria-hidden="true">02</span>
      </article>
    </div>

    <footer class="bank-value">
      <span class="value-mark" aria-hidden="true">↗</span>
      <div>
        <p class="value-label">¿DÓNDE APORTA VALOR DASH.IO?</p>
        <p>
          En convertir una idea en una oportunidad concreta: análisis, arquitectura, integraciones y pruebas de concepto.
        </p>
      </div>
      <span class="value-caption">EXPLORAR <i>·</i> DISEÑAR <i>·</i> VALIDAR</span>
    </footer>

  </div>
</section>

<style>
  .digital-assets {
    position: relative;
    overflow: hidden;
    padding: clamp(3rem, 7vw, 5.5rem) 1.25rem;
    color: #f2f7f7;
    background:
      radial-gradient(ellipse at 12% 18%, rgba(52, 220, 196, 0.085), transparent 30rem),
      linear-gradient(145deg, rgba(10, 25, 30, 0.82), rgba(11, 12, 20, 0.76));
  }

  .digital-assets::before {
    position: absolute;
    top: -12rem;
    right: -8rem;
    width: 26rem;
    aspect-ratio: 1;
    border: 1px solid rgba(89, 231, 210, 0.07);
    border-radius: 50%;
    box-shadow: 0 0 0 3rem rgba(89, 231, 210, 0.016), 0 0 0 6rem rgba(89, 231, 210, 0.01);
    content: "";
    pointer-events: none;
  }

  .assets-inner {
    position: relative;
    width: min(1120px, 100%);
    margin: 0 auto;
  }

  .assets-heading {
    max-width: 720px;
    margin-bottom: clamp(1.75rem, 4vw, 3rem);
  }

  .eyebrow,
  .overline,
  .opportunity-type,
  .value-label,
  .value-caption {
    font-size: 0.62rem;
    font-weight: 750;
    letter-spacing: 0.14em;
  }

  .eyebrow {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin: 0 0 1.25rem;
    color: #75e8d4;
  }

  .eyebrow span {
    font-size: 1rem;
  }

  .overline {
    margin: 0 0 0.4rem;
    color: #92aaa9;
  }

  h2 {
    margin: 0;
    font-size: clamp(2rem, 4.5vw, 3.2rem);
    letter-spacing: -0.05em;
    line-height: 1.08;
  }

  .intro {
    max-width: 650px;
    margin: 0.85rem 0 0;
    color: #b5c3c4;
    font-size: 0.98rem;
    line-height: 1.7;
  }

  .opportunity-list {
    border-top: 1px solid rgba(255, 255, 255, 0.13);
  }

  .opportunity {
    display: grid;
    grid-template-columns: 3.5rem minmax(0, 1fr) 2rem;
    align-items: center;
    gap: 1rem;
    padding: 1.35rem 0.5rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.13);
    transition: padding 200ms ease, background 200ms ease;
  }

  .opportunity:hover {
    padding-right: 1rem;
    padding-left: 1rem;
    background: linear-gradient(90deg, rgba(52, 220, 196, 0.085), transparent 75%);
  }

  .opportunity-icon {
    display: grid;
    width: 3.1rem;
    aspect-ratio: 1;
    place-items: center;
    color: #75e8d4;
    border: 1px solid rgba(89, 231, 210, 0.25);
    border-radius: 15px;
    background: rgba(52, 220, 196, 0.07);
    transition: transform 200ms ease, background 200ms ease;
  }

  .opportunity-icon svg {
    width: 1.8rem;
    stroke: currentColor;
    stroke-linecap: round;
    stroke-linejoin: round;
    stroke-width: 1.5;
  }

  .opportunity:hover .opportunity-icon {
    transform: translateY(-2px) rotate(-5deg);
    background: rgba(52, 220, 196, 0.14);
  }

  .opportunity-type {
    color: #75e8d4;
    font-size: 0.57rem;
  }

  .opportunity-copy h3 {
    margin: 0.2rem 0 0.3rem;
    font-size: 1.12rem;
    letter-spacing: -0.02em;
  }

  .opportunity-copy p {
    max-width: 760px;
    margin: 0;
    color: #b5c3c4;
    font-size: 0.84rem;
    line-height: 1.65;
  }

  .opportunity-number {
    align-self: start;
    padding-top: 0.2rem;
    color: #668581;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.12em;
  }

  .bank-value {
    display: grid;
    grid-template-columns: 2rem minmax(0, 1fr) auto;
    align-items: center;
    gap: 1rem;
    margin-top: 1.25rem;
    padding: 1rem 1.15rem;
    border: 1px solid rgba(89, 231, 210, 0.18);
    border-radius: 15px;
    background: rgba(52, 220, 196, 0.045);
  }

  .value-mark {
    display: grid;
    width: 2rem;
    aspect-ratio: 1;
    place-items: center;
    color: #09201e;
    border-radius: 50%;
    background: #75e8d4;
    font-weight: 800;
  }

  .value-label {
    margin: 0 0 0.25rem;
    color: #75e8d4;
    font-size: 0.57rem;
  }

  .bank-value div > p:last-child {
    margin: 0;
    color: #bac8c8;
    font-size: 0.82rem;
    line-height: 1.6;
  }

  .value-caption {
    color: #8ca9a6;
    font-size: 0.55rem;
    white-space: nowrap;
  }

  .value-caption i {
    padding: 0 0.2rem;
    color: #557a75;
    font-style: normal;
  }

  @media (max-width: 700px) {
    .bank-value {
      grid-template-columns: 2rem minmax(0, 1fr);
    }

    .value-caption {
      grid-column: 2;
    }
  }

  @media (max-width: 460px) {
    .opportunity {
      grid-template-columns: 2.8rem minmax(0, 1fr) 1.5rem;
      gap: 0.7rem;
      padding-right: 0.15rem;
      padding-left: 0.15rem;
    }

    .opportunity-icon {
      width: 2.6rem;
      border-radius: 13px;
    }

    .opportunity:hover {
      padding-right: 0.45rem;
      padding-left: 0.45rem;
    }

  }

  @media (prefers-reduced-motion: reduce) {
    .opportunity,
    .opportunity-icon {
      transition: none;
    }
  }
</style>
