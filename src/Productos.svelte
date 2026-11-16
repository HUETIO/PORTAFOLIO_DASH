<script>
  import { services } from "./services.js";
</script>

<svelte:head>
  <title>Productos para bancos y empresas | DASH.IO</title>
  <meta
    name="description"
    content="Soluciones digitales para bancos y empresas: software, gestión documental, IA, integridad de datos y más."
  />
</svelte:head>

<div class="products-page" role="main">
  <div class="page-shell">
    <header class="topbar">
      <a class="brand" href="#inicio" aria-label="DASH.IO, volver al portafolio">DASH<span>.</span>IO</a>
      <span class="topbar-label"><span class="status-dot"></span> SOLUCIONES PARA EMPRESAS</span>
      <a class="back-link" href="#inicio">Volver al portafolio <span aria-hidden="true">↗</span></a>
    </header>

    <section class="hero" aria-labelledby="products-title">
      <div class="hero-copy">
        <p class="eyebrow">PRODUCTOS / BANCA Y EMPRESA</p>
        <h1 id="products-title">Tecnología para operaciones <span>que inspiran confianza.</span></h1>
        <p class="intro">
          Un espacio independiente del portafolio creativo para explorar herramientas
          digitales enfocadas en las necesidades de bancos y organizaciones.
        </p>
        <a class="primary-link" href="#catalogo">Explorar soluciones <span aria-hidden="true">↓</span></a>
      </div>
      <div class="hero-visual" aria-hidden="true">
        <div class="visual-orbit orbit-outer"></div>
        <div class="visual-orbit orbit-inner"></div>
        <div class="visual-core"><span>D</span></div>
        <span class="visual-tag tag-one">DATOS</span>
        <span class="visual-tag tag-two">CONFIANZA</span>
        <span class="visual-tag tag-three">OPERACIÓN</span>
      </div>
    </section>

    <section class="catalog" id="catalogo" aria-labelledby="catalog-title">
      <div class="section-heading">
        <div>
          <p class="eyebrow">CAPACIDADES DIGITALES</p>
          <h2 id="catalog-title">Un catálogo para retos reales.</h2>
        </div>
        <p class="section-note">
          Soluciones que pueden diseñarse, integrarse y evolucionar según cada operación.
        </p>
      </div>

      <div class="product-grid">
        {#each services as product}
          <article class="product-card" style:--card-accent={product.accent}>
            <div class="card-top">
              <span class="card-number">{product.number}</span>
              <span class="card-icon" aria-hidden="true">{product.icon}</span>
            </div>
            <p class="card-category">{product.category}</p>
            <h3>{product.title}</h3>
            <p class="card-description">{product.description}</p>
            <ul class="capabilities">
              {#each product.capabilities as capability}
                <li>{capability}</li>
              {/each}
            </ul>
          </article>
        {/each}
      </div>
    </section>

    <section class="principles" aria-labelledby="principles-title">
      <div>
        <p class="eyebrow">PENSADO PARA ENTORNOS EXIGENTES</p>
        <h2 id="principles-title">Integración, trazabilidad y claridad desde el inicio.</h2>
      </div>
      <div class="principle-list">
        <p><span>01</span> Integración con los sistemas y flujos existentes.</p>
        <p><span>02</span> Acceso controlado y evidencia de las operaciones.</p>
        <p><span>03</span> Diseño adaptable a los objetivos de cada organización.</p>
      </div>
    </section>

    <footer class="page-footer">
      <a class="brand" href="#inicio">DASH<span>.</span>IO</a>
      <span>Herramientas digitales para una operación más confiable.</span>
      <a class="footer-link" href="#contact">Hablemos <span aria-hidden="true">↗</span></a>
    </footer>
  </div>
</div>

<style>
  .products-page {
    --page-bg: #080d15;
    --panel: rgba(17, 26, 39, 0.82);
    --line: rgba(180, 203, 222, 0.14);
    --text: #f0f5f8;
    --muted: #a4b2c0;
    --accent: #55e5c5;
    position: fixed;
    inset: 0;
    z-index: 1200;
    overflow-y: auto;
    color: var(--text);
    background:
      radial-gradient(ellipse at 82% 9%, rgba(35, 155, 143, 0.14), transparent 34rem),
      radial-gradient(ellipse at 8% 40%, rgba(57, 91, 156, 0.13), transparent 32rem),
      var(--page-bg);
    font-family: "Segoe UI", system-ui, sans-serif;
  }

  .products-page,
  .products-page * {
    box-sizing: border-box;
  }

  .products-page a::after {
    display: none;
  }

  .page-shell {
    width: min(1180px, calc(100% - 3rem));
    margin: 0 auto;
  }

  .topbar {
    display: flex;
    min-height: 76px;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    border-bottom: 1px solid var(--line);
  }

  .brand {
    color: var(--text);
    font-size: 1.15rem;
    font-weight: 800;
    letter-spacing: 0.08em;
  }

  .brand span {
    color: var(--accent);
  }

  .topbar-label,
  .eyebrow,
  .card-category {
    color: var(--accent);
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.16em;
  }

  .topbar-label {
    display: inline-flex;
    align-items: center;
    gap: 0.55rem;
    color: #b7c5d0;
  }

  .status-dot {
    width: 0.5rem;
    height: 0.5rem;
    border-radius: 50%;
    background: var(--accent);
    box-shadow: 0 0 14px rgba(85, 229, 197, 0.8);
  }

  .back-link,
  .footer-link {
    color: var(--text);
    font-size: 0.86rem;
    font-weight: 600;
  }

  .back-link span,
  .footer-link span {
    margin-left: 0.3rem;
    color: var(--accent);
  }

  .hero {
    display: grid;
    min-height: 430px;
    grid-template-columns: minmax(0, 1.2fr) minmax(260px, 0.8fr);
    align-items: center;
    gap: 3rem;
    padding: 3.5rem 0 4.5rem;
  }

  .hero-copy {
    max-width: 720px;
  }

  .eyebrow {
    margin: 0 0 1rem;
  }

  .hero h1 {
    max-width: 700px;
    margin: 0;
    color: var(--text);
    font-size: clamp(2.5rem, 5.2vw, 4.65rem);
    line-height: 1.06;
    letter-spacing: -0.055em;
    text-shadow: none;
  }

  .hero h1 span {
    color: var(--accent);
  }

  .intro {
    max-width: 620px;
    margin: 1.35rem 0 1.8rem;
    color: var(--muted);
    font-size: 1.04rem;
    line-height: 1.75;
  }

  .primary-link {
    display: inline-flex;
    min-height: 2.9rem;
    align-items: center;
    gap: 1rem;
    padding: 0.7rem 1.1rem;
    border: 1px solid rgba(85, 229, 197, 0.45);
    border-radius: 10px;
    background: rgba(85, 229, 197, 0.1);
    color: var(--accent);
    font-size: 0.9rem;
    font-weight: 700;
    transition: background 180ms ease, transform 180ms ease;
  }

  .primary-link:hover {
    transform: translateY(-2px);
    background: rgba(85, 229, 197, 0.17);
  }

  .hero-visual {
    position: relative;
    display: grid;
    width: min(100%, 340px);
    aspect-ratio: 1;
    place-items: center;
    justify-self: center;
  }

  .visual-orbit {
    position: absolute;
    border: 1px solid rgba(85, 229, 197, 0.24);
    border-radius: 50%;
    transform: rotate(-28deg);
  }

  .orbit-outer {
    width: 94%;
    height: 62%;
  }

  .orbit-inner {
    width: 68%;
    height: 90%;
    border-color: rgba(125, 168, 255, 0.28);
    transform: rotate(38deg);
  }

  .visual-core {
    display: grid;
    width: 7rem;
    height: 7rem;
    place-items: center;
    border: 1px solid rgba(85, 229, 197, 0.6);
    border-radius: 2rem;
    background: linear-gradient(145deg, rgba(85, 229, 197, 0.22), rgba(22, 43, 61, 0.85));
    box-shadow: 0 0 70px rgba(85, 229, 197, 0.18), inset 0 0 30px rgba(85, 229, 197, 0.1);
    color: var(--accent);
    font-size: 3rem;
    font-weight: 700;
  }

  .visual-tag {
    position: absolute;
    padding: 0.4rem 0.65rem;
    border: 1px solid var(--line);
    border-radius: 999px;
    background: rgba(8, 13, 21, 0.78);
    color: #c5d2dc;
    font-size: 0.6rem;
    font-weight: 700;
    letter-spacing: 0.12em;
  }

  .tag-one {
    top: 16%;
    left: 5%;
  }

  .tag-two {
    top: 29%;
    right: 0;
  }

  .tag-three {
    bottom: 17%;
    left: 14%;
  }

  .catalog {
    padding: 2.5rem 0 5rem;
    border-top: 1px solid var(--line);
  }

  .section-heading {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    gap: 2rem;
    margin-bottom: 1.5rem;
  }

  .section-heading h2,
  .principles h2 {
    margin: 0;
    color: var(--text);
    font-size: clamp(1.7rem, 3.4vw, 2.6rem);
    line-height: 1.2;
    letter-spacing: -0.035em;
  }

  .section-note {
    max-width: 360px;
    margin: 0 0 0.25rem;
    color: var(--muted);
    font-size: 0.9rem;
    line-height: 1.65;
  }

  .product-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 0.9rem;
  }

  .product-card {
    display: flex;
    min-height: 315px;
    flex-direction: column;
    padding: 1.25rem;
    border: 1px solid var(--line);
    border-radius: 16px;
    background:
      linear-gradient(145deg, color-mix(in srgb, var(--card-accent), transparent 94%), transparent 58%),
      var(--panel);
    transition: border-color 180ms ease, transform 180ms ease, background 180ms ease;
  }

  .product-card:hover {
    transform: translateY(-4px);
    border-color: color-mix(in srgb, var(--card-accent), transparent 45%);
  }

  .card-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1.1rem;
  }

  .card-number {
    color: var(--card-accent);
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.12em;
  }

  .card-icon {
    display: grid;
    min-width: 2.4rem;
    height: 2.4rem;
    place-items: center;
    padding: 0 0.35rem;
    border: 1px solid color-mix(in srgb, var(--card-accent), transparent 68%);
    border-radius: 11px;
    background: color-mix(in srgb, var(--card-accent), transparent 91%);
    color: var(--card-accent);
    font-family: ui-monospace, monospace;
    font-size: 1rem;
    font-weight: 700;
  }

  .card-category {
    margin: 0 0 0.55rem;
    color: var(--card-accent);
    font-size: 0.59rem;
    letter-spacing: 0.13em;
  }

  .product-card h3 {
    margin: 0;
    color: var(--text);
    font-size: 1.14rem;
    line-height: 1.35;
  }

  .card-description {
    margin: 0.65rem 0 1rem;
    color: var(--muted);
    font-size: 0.82rem;
    line-height: 1.65;
  }

  .capabilities {
    display: grid;
    gap: 0.42rem;
    margin: auto 0 0;
    padding: 0.8rem 0 0;
    border-top: 1px solid var(--line);
    list-style: none;
  }

  .capabilities li {
    color: #d3dde5;
    font-size: 0.75rem;
  }

  .capabilities li::before {
    margin-right: 0.5rem;
    color: var(--card-accent);
    content: "•";
  }

  .principles {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    padding: 2.5rem;
    border: 1px solid var(--line);
    border-radius: 20px;
    background: linear-gradient(120deg, rgba(85, 229, 197, 0.08), rgba(17, 26, 39, 0.68));
  }

  .principles h2 {
    max-width: 510px;
  }

  .principle-list {
    display: grid;
    align-content: center;
    gap: 0.75rem;
  }

  .principle-list p {
    margin: 0;
    color: #d1dce5;
    font-size: 0.9rem;
  }

  .principle-list span {
    margin-right: 0.6rem;
    color: var(--accent);
    font-size: 0.75rem;
    font-weight: 700;
  }

  .page-footer {
    display: flex;
    min-height: 100px;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    color: var(--muted);
    font-size: 0.78rem;
  }

  @media (max-width: 980px) {
    .product-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }

  @media (max-width: 700px) {
    .page-shell {
      width: min(100% - 2rem, 560px);
    }

    .topbar {
      min-height: 68px;
    }

    .topbar-label {
      display: none;
    }

    .hero {
      min-height: auto;
      grid-template-columns: 1fr;
      gap: 0.5rem;
      padding: 3.5rem 0 2.5rem;
    }

    .hero-visual {
      width: min(76vw, 280px);
      margin: 0 auto;
    }

    .section-heading {
      align-items: flex-start;
      flex-direction: column;
      gap: 0.6rem;
    }

    .principles {
      grid-template-columns: 1fr;
      gap: 1.5rem;
      padding: 1.5rem;
    }
  }

  @media (max-width: 520px) {
    .back-link {
      font-size: 0.75rem;
    }

    .hero h1 {
      font-size: clamp(2.35rem, 12vw, 3.4rem);
    }

    .product-grid {
      grid-template-columns: 1fr;
    }

    .product-card {
      min-height: 285px;
    }

    .page-footer {
      min-height: 120px;
      flex-wrap: wrap;
      justify-content: space-between;
      padding: 1.5rem 0;
    }

    .page-footer > span {
      order: 1;
      width: 100%;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .product-card,
    .primary-link {
      transition: none;
    }
  }
</style>
