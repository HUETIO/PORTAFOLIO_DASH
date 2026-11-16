<section class="creative-ai" aria-labelledby="creative-ai-title">
  <div class="creative-inner">
    <header class="creative-heading">
      <p class="eyebrow"><span aria-hidden="true">✦</span> CREATIVIDAD · TECNOLOGÍA · IA</p>
      <h2 id="creative-ai-title">¿Y si una idea pudiera convertirse en una herramienta hecha a tu medida?</h2>
      <p>
        En DASH.IO combinamos creatividad e inteligencia artificial para transformar ideas en experiencias digitales.
      </p>
    </header>

    <div class="creative-cards">
      <article class="creative-card creative-card--alfresco">
        <div class="alfresco-banner" aria-hidden="true">
          <span class="alfresco-document">A</span>
          <span class="alfresco-spark">✦</span>
          <span class="alfresco-banner-label">DOCUMENTOS · IDEAS · IA</span>
        </div>
        <div class="creative-card-content">
          <p class="model-label">IA · IDEAS · EXPERIENCIAS DIGITALES</p>
          <h3>Herramientas de IA para manualidades</h3>
          <p>
            Creamos herramientas inteligentes que convierten ideas creativas en procesos sencillos y experiencias interactivas.
          </p>
        </div>
      </article>

      <article class="creative-card creative-card--qwen">
        <div class="art-panel" role="img" aria-label="Ilustración conceptual de una idea artesanal convertida en imagen">
          <div class="art-orbit art-orbit--one"></div>
          <div class="art-orbit art-orbit--two"></div>
          <div class="art-sun"></div>
          <div class="art-paper art-paper--back"></div>
          <div class="art-paper art-paper--front">
            <span class="paper-label">IDEA → IMAGEN</span>
            <span class="paper-flower" aria-hidden="true">✿</span>
            <span class="paper-lines" aria-hidden="true"></span>
            <span class="paper-caption">hecho para crear</span>
          </div>
          <span class="art-chip art-chip--one">patrones</span>
          <span class="art-chip art-chip--two">texturas</span>
        </div>

        <div class="creative-card-content">
          <p class="model-label">CREACIÓN VISUAL · INTELIGENCIA ARTIFICIAL</p>
          <h3>De una idea a una nueva imagen</h3>
          <p>
            Explora patrones, texturas y conceptos visuales para dar vida a productos, contenidos y nuevas ideas.
          </p>
        </div>
      </article>
    </div>
  </div>
</section>

<style>
  .creative-ai {
    position: relative;
    overflow: hidden;
    padding: clamp(3rem, 7vw, 6rem) 1.25rem;
    color: #f7f5ff;
    background:
      radial-gradient(ellipse at 12% 18%, rgba(244, 154, 207, 0.12), transparent 28rem),
      radial-gradient(ellipse at 90% 85%, rgba(121, 105, 255, 0.13), transparent 30rem),
      linear-gradient(145deg, #17111e, #0d101c 65%, #121020);
  }

  .creative-inner {
    width: min(1120px, 100%);
    margin: 0 auto;
  }

  .creative-heading {
    max-width: 760px;
    margin-bottom: 2rem;
  }

  .eyebrow,
  .model-label {
    color: #f2a9d5;
    font-size: 0.68rem;
    font-weight: 750;
    letter-spacing: 0.14em;
  }

  .eyebrow {
    margin: 0 0 0.8rem;
  }

  .eyebrow span {
    margin-right: 0.35rem;
  }

  h2 {
    margin: 0;
    font-size: clamp(2rem, 5vw, 3.35rem);
    letter-spacing: -0.05em;
    line-height: 1.08;
  }

  .creative-heading > p:last-child {
    max-width: 680px;
    margin: 0.9rem 0 0;
    color: #c3bfce;
    font-size: 1rem;
    line-height: 1.7;
  }

  .creative-cards {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1.25rem;
  }

  .creative-card {
    display: flex;
    min-width: 0;
    flex-direction: column;
    overflow: hidden;
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 24px;
    background: linear-gradient(155deg, rgba(31, 29, 46, 0.92), rgba(17, 19, 30, 0.95));
    box-shadow: 0 18px 48px rgba(0, 0, 0, 0.2);
  }

  .creative-card-content {
    display: flex;
    flex: 1;
    flex-direction: column;
    align-items: flex-start;
    padding: clamp(1.25rem, 3vw, 1.8rem);
  }

  .creative-card-content > p:not(.model-label) {
    margin: 0.8rem 0 1rem;
    color: #c3bfce;
    font-size: 0.88rem;
    line-height: 1.65;
  }

  .creative-card h3 {
    margin: 0;
    font-size: clamp(1.3rem, 2.4vw, 1.8rem);
    letter-spacing: -0.03em;
    line-height: 1.2;
  }

  .alfresco-banner {
    position: relative;
    display: grid;
    min-height: 220px;
    place-items: center;
    overflow: hidden;
    background:
      radial-gradient(circle at 50% 50%, rgba(116, 194, 167, 0.2), transparent 9rem),
      linear-gradient(145deg, #173b3b, #14242d 65%, #211b32);
  }

  .alfresco-banner::before,
  .alfresco-banner::after {
    position: absolute;
    width: 75%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(144, 211, 210, 0.35), transparent);
    content: "";
  }

  .alfresco-banner::before {
    transform: rotate(28deg);
  }

  .alfresco-banner::after {
    transform: rotate(-28deg);
  }

  .alfresco-document {
    z-index: 1;
    display: grid;
    width: 5rem;
    aspect-ratio: 0.78;
    place-items: center;
    border: 1px solid rgba(199, 240, 222, 0.5);
    border-radius: 13px;
    background: linear-gradient(155deg, rgba(101, 185, 153, 0.9), rgba(43, 107, 111, 0.9));
    box-shadow: 0 14px 40px rgba(0, 0, 0, 0.28);
    color: #f0fff7;
    font-size: 2rem;
    font-weight: 800;
  }

  .alfresco-spark {
    position: absolute;
    top: 24%;
    right: 28%;
    color: #f2a9d5;
    font-size: 2rem;
    text-shadow: 0 0 24px rgba(242, 169, 213, 0.7);
  }

  .alfresco-banner-label {
    position: absolute;
    bottom: 1rem;
    color: #c7d8d5;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.16em;
  }

  .art-panel {
    position: relative;
    display: grid;
    min-height: 260px;
    overflow: hidden;
    place-items: center;
    border: 1px solid rgba(244, 169, 213, 0.2);
    border-radius: 24px;
    background:
      radial-gradient(circle at 50% 45%, rgba(242, 169, 213, 0.19), transparent 14rem),
      linear-gradient(155deg, #252036, #171522 62%, #111520);
    isolation: isolate;
  }

  .art-orbit {
    position: absolute;
    width: min(72%, 370px);
    aspect-ratio: 1;
    border: 1px solid rgba(242, 169, 213, 0.18);
    border-radius: 50%;
  }

  .art-orbit--one {
    transform: rotate(-24deg) scaleY(0.52);
  }

  .art-orbit--two {
    transform: rotate(38deg) scaleY(0.72);
    border-color: rgba(144, 211, 210, 0.23);
  }

  .art-sun {
    position: absolute;
    top: 17%;
    left: 21%;
    width: 4.5rem;
    aspect-ratio: 1;
    border-radius: 50%;
    background: linear-gradient(145deg, #f8d59a, #f09ec9 65%, #b1a3ff);
    box-shadow: 0 0 70px rgba(242, 169, 213, 0.36);
  }

  .art-paper {
    position: absolute;
    width: min(57%, 260px);
    aspect-ratio: 0.78;
    border-radius: 8px;
    box-shadow: 0 28px 60px rgba(0, 0, 0, 0.35);
  }

  .art-paper--back {
    transform: rotate(11deg) translate(24px, 5px);
    background: linear-gradient(145deg, #92c6bd, #476d73);
  }

  .art-paper--front {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0.8rem;
    transform: rotate(-7deg);
    border: 1px solid rgba(255, 255, 255, 0.38);
    background:
      radial-gradient(circle at 25% 80%, rgba(221, 130, 170, 0.25), transparent 30%),
      repeating-linear-gradient(45deg, rgba(102, 90, 130, 0.045) 0 1px, transparent 1px 9px),
      #f2e7d8;
    color: #332c43;
  }

  .paper-label {
    font-size: 0.57rem;
    font-weight: 800;
    letter-spacing: 0.16em;
  }

  .paper-flower {
    color: #bd6589;
    font-size: clamp(4rem, 8vw, 6.5rem);
    line-height: 1;
    text-shadow: 0 5px 16px rgba(189, 101, 137, 0.24);
  }

  .paper-lines {
    width: 52%;
    height: 1.5rem;
    border-top: 1px solid rgba(51, 44, 67, 0.32);
    border-bottom: 1px solid rgba(51, 44, 67, 0.18);
  }

  .paper-caption {
    color: #61556c;
    font-family: Georgia, serif;
    font-size: 0.85rem;
    font-style: italic;
  }

  .art-chip {
    position: absolute;
    padding: 0.45rem 0.7rem;
    border: 1px solid rgba(255, 255, 255, 0.14);
    border-radius: 999px;
    background: rgba(13, 16, 28, 0.68);
    color: #e8d8e6;
    font-size: 0.72rem;
    backdrop-filter: blur(8px);
  }

  .art-chip--one {
    top: 25%;
    right: 12%;
  }

  .art-chip--two {
    bottom: 23%;
    left: 10%;
  }

  .model-label {
    margin: 0 0 0.65rem;
  }

  @media (max-width: 780px) {
    .creative-cards {
      grid-template-columns: 1fr;
    }

    .art-panel {
      min-height: 300px;
    }
  }

  @media (max-width: 440px) {
    .art-panel {
      min-height: 260px;
    }

  }

  @media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
      scroll-behavior: auto !important;
    }
  }
</style>
