<script>
  export let color;
  import CardDetailButton from "./components/CardDetailButton.svelte";

  let currentSignal = 'suelo';

  const signals = {
    suelo: {
      label: 'Humedad del suelo',
      value: '38%',
      status: 'Necesita agua',
      detail: 'La raíz todavía puede esperar; el riego inteligente evita desperdiciar agua.',
      progress: 38
    },
    luz: {
      label: 'Luz recibida',
      value: '7.2 h',
      status: 'Buen equilibrio',
      detail: 'La luz de hoy favorece la fotosíntesis sin someter las hojas a demasiado calor.',
      progress: 72
    },
    aire: {
      label: 'Calidad del aire',
      value: '94%',
      status: 'Aire saludable',
      detail: 'Las hojas intercambian gases con el entorno: medir también ayuda a protegerlo.',
      progress: 94
    }
  };

  $: activeSignal = signals[currentSignal];
</script>

<svelte:head>
  <title>Raíz y Razón | Ciencia viva</title>
  <meta
    name="description"
    content="Una revista digital sobre plantas, biología, tecnología y las conexiones entre ciencia y naturaleza."
  />
</svelte:head>

<main class="magazine" id="inicio" style={`--tab-color: ${color || '#526a54'}`}>
  <a class="skip-link" href="#contenido">Saltar al contenido</a>

  <div class="page-shell">
    <header class="masthead">
      <a class="brand" href="#inicio" aria-label="Raíz y Razón, inicio">
        <span class="brand-mark" aria-hidden="true">
          <svg viewBox="0 0 42 42" fill="none">
            <path d="M21 34V18m0 8c-8 0-13-5-13-13 8 0 13 5 13 13Zm0-5c0-8 5-13 13-13 0 8-5 13-13 13Z" />
            <path d="M14 34h14" />
          </svg>
        </span>
        <span class="brand-name">raíz <i>y</i> razón</span>
      </a>
      <p class="masthead-note">Una revista para mentes curiosas y manos en la tierra</p>
      <div class="issue-stamp"><span>EDICIÓN 05</span><span>CIENCIA VIVA · 2025</span></div>
    </header>

    <nav class="issue-nav" aria-label="Secciones de la revista">
      <a href="#portada">Portada</a>
      <a href="#historias">Historias</a>
      <a href="#observatorio">Observatorio</a>
      <a href="#cuaderno">Cuaderno de campo</a>
      <span class="nav-note">N.º 05 <span aria-hidden="true">✳</span> Naturaleza + tecnología</span>
    </nav>

    <section class="cover-story" id="portada" aria-labelledby="cover-title">
      <div class="cover-copy">
        <p class="kicker"><span class="kicker-line"></span> BIOLOGÍA · INNOVACIÓN · PLANETA</p>
        <h1 id="cover-title">La naturaleza también sabe <em>ingeniería.</em></h1>
        <p class="cover-intro">
          De una hoja que recoge luz a una máquina que aprende de ella: las ideas más
          sorprendentes del futuro ya están creciendo a nuestro alrededor.
        </p>
        <a class="text-link" href="#historias">Explora esta edición <span aria-hidden="true">↗</span></a>
        <div class="cover-byline">
          <span class="byline-rule"></span>
          <span>UN RECORRIDO ENTRE LO VIVO Y LO CREADO</span>
        </div>
      </div>

      <div class="cover-art" role="img" aria-label="Ilustración de una planta conectada con líneas de un circuito">
        <div class="art-caption"><span>FIG. 01</span> Una hoja, mil soluciones</div>
        <svg class="plant-illustration" viewBox="0 0 620 540" fill="none" aria-hidden="true">
          <defs>
            <linearGradient id="leaf" x1="140" y1="110" x2="470" y2="420" gradientUnits="userSpaceOnUse">
              <stop stop-color="#D9E7A8" />
              <stop offset="1" stop-color="#8DB18A" />
            </linearGradient>
            <linearGradient id="stem" x1="260" y1="145" x2="345" y2="430" gradientUnits="userSpaceOnUse">
              <stop stop-color="#E9E9B8" />
              <stop offset="1" stop-color="#91B18D" />
            </linearGradient>
          </defs>
          <circle cx="318" cy="266" r="205" stroke="#D8E2BF" stroke-opacity=".22" />
          <circle cx="318" cy="266" r="160" stroke="#D8E2BF" stroke-opacity=".16" stroke-dasharray="3 9" />
          <path d="M314 448C311 374 310 300 319 182" stroke="url(#stem)" stroke-width="8" stroke-linecap="round" />
          <path d="M312 354C253 347 184 310 173 229C244 218 304 257 312 354Z" fill="url(#leaf)" />
          <path d="M312 353C266 321 220 279 181 237" stroke="#52725E" stroke-width="3" stroke-linecap="round" />
          <path d="M319 278C327 202 379 151 459 159C460 239 409 286 319 278Z" fill="url(#leaf)" />
          <path d="M325 273C369 232 407 194 451 166" stroke="#52725E" stroke-width="3" stroke-linecap="round" />
          <path d="M313 403C265 394 227 357 224 311C278 310 312 343 313 403Z" fill="#AEC79C" />
          <path d="M313 401C279 374 254 347 231 319" stroke="#52725E" stroke-width="2.5" stroke-linecap="round" />
          <path d="M317 216C281 180 282 135 315 102C351 132 354 180 317 216Z" fill="#D6E4A5" />
          <path d="M317 211V110" stroke="#52725E" stroke-width="2.5" stroke-linecap="round" />
          <path d="M450 166h67v-38h41m-246 226h-91v52h-49m224-191h93v-47h43" stroke="#D8E2BF" stroke-opacity=".62" stroke-width="1.5" stroke-dasharray="4 7" />
          <circle cx="558" cy="128" r="5" fill="#E1E9B8" />
          <circle cx="172" cy="406" r="5" fill="#E1E9B8" />
          <circle cx="581" cy="168" r="3" fill="#E1E9B8" />
          <path d="M95 185h58m-29-29v58m368 190h55m-27-27v55" stroke="#D8E2BF" stroke-opacity=".5" stroke-width="1.5" />
          <path d="M103 95h42m-21-21v42m363 336h42m-21-21v42" stroke="#D8E2BF" stroke-opacity=".4" stroke-width="1" />
        </svg>
        <div class="art-label art-label-top"><span>01</span> FOTOSÍNTESIS</div>
        <div class="art-label art-label-bottom"><span>02</span> DISEÑO BIOMIMÉTICO</div>
        <div class="art-orbit" aria-hidden="true">OBSERVAR <span>·</span> APRENDER <span>·</span> CUIDAR</div>
      </div>
    </section>

    <section class="briefing-strip" aria-label="Temas de esta edición">
      <div><span class="briefing-icon" aria-hidden="true">✳</span><strong>La vida inspira</strong><span>Ideas que nacen en la naturaleza</span></div>
      <div><span class="briefing-icon" aria-hidden="true">⌁</span><strong>La ciencia conecta</strong><span>De los datos a los ecosistemas</span></div>
      <div><span class="briefing-icon" aria-hidden="true">↗</span><strong>El futuro se cultiva</strong><span>Tecnología con propósito</span></div>
    </section>

    <section class="stories-section" id="historias" aria-labelledby="stories-title">
      <div class="section-heading">
        <div>
          <p class="kicker"><span class="kicker-line"></span> REPORTAJES DE ESTA EDICIÓN</p>
          <h2 id="stories-title">Pequeñas pistas, <em>grandes ideas.</em></h2>
        </div>
        <a class="text-link section-link" href="#cuaderno">Ir al cuaderno <span aria-hidden="true">↘</span></a>
      </div>

      <div class="story-grid">
        <article class="story-card">
          <div class="story-art story-art-leaf" aria-hidden="true">
            <span class="story-number">01 / BOTÁNICA</span>
            <svg viewBox="0 0 280 150" fill="none">
              <path d="M63 126C66 73 105 27 202 18C200 105 143 139 63 126Z" fill="#B5C79A" />
              <path d="M70 123C111 91 151 55 194 25" stroke="#536B52" stroke-width="2" />
              <path d="m113 89-2-29m27 8-4-25m-13 57-26-10m54-15-23-8" stroke="#536B52" stroke-width="1.5" />
              <circle cx="216" cy="107" r="31" stroke="#536B52" stroke-opacity=".38" />
              <circle cx="216" cy="107" r="21" stroke="#536B52" stroke-opacity=".38" stroke-dasharray="2 5" />
            </svg>
          </div>
          <div class="story-copy">
            <p class="story-meta">PLANTAS EXTRAORDINARIAS <span>· 6 MIN</span></p>
            <h3>La hoja que convierte el sol en energía</h3>
            <p>Cómo la fotosíntesis está inspirando nuevas formas de producir energía limpia.</p>
            <CardDetailButton
              title="La hoja que convierte el sol en energía"
              description="Reportaje editorial sobre la fotosíntesis y su inspiración para pensar en energía limpia."
              details={["Presenta la fotosíntesis como referencia para estudiar cómo se capta y transforma la energía solar.", "La tarjeta es parte de una edición temática sobre biología, innovación y planeta."]}
              accent={color}
            />
            <a href="#observatorio" aria-label="Leer sobre fotosíntesis en el observatorio">Leer historia <span aria-hidden="true">→</span></a>
          </div>
        </article>

        <article class="story-card">
          <div class="story-art story-art-tech" aria-hidden="true">
            <span class="story-number">02 / BIOMIMÉTICA</span>
            <svg viewBox="0 0 280 150" fill="none">
              <path d="M40 118h200M63 118V85m0 0h44V57h43V36h52" stroke="#C9D7B3" stroke-width="2" stroke-dasharray="4 6" />
              <circle cx="63" cy="83" r="7" stroke="#E4E9D1" stroke-width="2" />
              <circle cx="107" cy="57" r="7" stroke="#E4E9D1" stroke-width="2" />
              <circle cx="150" cy="36" r="7" stroke="#E4E9D1" stroke-width="2" />
              <path d="M179 100c-1-30 14-50 37-54-1 27-12 44-37 54Z" fill="#B5C79A" />
              <path d="M182 98c13-19 23-32 32-48" stroke="#536B52" stroke-width="2" />
              <path d="M185 88h13m-9-13h12" stroke="#536B52" stroke-width="1.5" />
            </svg>
          </div>
          <div class="story-copy">
            <p class="story-meta">DISEÑO QUE APRENDE <span>· 8 MIN</span></p>
            <h3>Robots con raíces: máquinas inspiradas en plantas</h3>
            <p>Sensores, algoritmos y estructuras que imitan estrategias de la vida vegetal.</p>
            <CardDetailButton
              title="Robots con raíces: máquinas inspiradas en plantas"
              description="Reportaje editorial sobre biomimética: sensores, algoritmos y estructuras inspirados en la vida vegetal."
              details={["Explora cómo observar estrategias de las plantas puede inspirar diseños tecnológicos.", "El tema conecta naturaleza, robótica y diseño biomimético."]}
              accent={color}
            />
            <a href="#observatorio" aria-label="Leer sobre máquinas inspiradas en plantas">Leer historia <span aria-hidden="true">→</span></a>
          </div>
        </article>

        <article class="story-card">
          <div class="story-art story-art-field" aria-hidden="true">
            <span class="story-number">03 / ECOLOGÍA</span>
            <svg viewBox="0 0 280 150" fill="none">
              <path d="M35 119h210M54 119V74m32 45V54m34 65V79m36 40V48m35 71V67m35 52V43" stroke="#63745E" stroke-width="3" stroke-linecap="round" />
              <path d="M36 75c11-18 25-18 36 0-11 17-25 17-36 0Zm34-22c10-18 25-18 35 0-10 18-25 18-35 0Zm33 27c10-18 25-18 35 0-10 17-25 17-35 0Zm36-32c10-18 25-18 35 0-10 18-25 18-35 0Zm35 19c10-18 25-18 35 0-10 18-25 18-35 0Zm33-24c10-18 25-18 35 0-10 18-25 18-35 0Z" fill="#AEBF91" />
              <path d="M45 134h180" stroke="#B6A783" stroke-width="2" stroke-dasharray="3 5" />
            </svg>
          </div>
          <div class="story-copy">
            <p class="story-meta">CUIDAR EL TERRITORIO <span>· 5 MIN</span></p>
            <h3>Un bosque cabe en los datos</h3>
            <p>Satélites y ciencia ciudadana ayudan a descubrir cómo cambia un ecosistema.</p>
            <CardDetailButton
              title="Un bosque cabe en los datos"
              description="Reportaje editorial sobre el uso de observaciones, satélites y ciencia ciudadana para comprender cambios en ecosistemas."
              details={["Presenta datos y observación territorial como herramientas para estudiar transformaciones ambientales.", "La tarjeta forma parte de una revista conceptual sobre naturaleza y tecnología."]}
              accent={color}
            />
            <a href="#cuaderno" aria-label="Leer sobre monitoreo de ecosistemas">Leer historia <span aria-hidden="true">→</span></a>
          </div>
        </article>
      </div>
    </section>

    <section class="observatory" id="observatorio" aria-labelledby="observatory-title">
      <div class="observatory-copy">
        <p class="kicker"><span class="kicker-line"></span> UNA VENTANA AL MUNDO VIVO</p>
        <h2 id="observatory-title">Medir para <em>comprender.</em></h2>
        <p>
          La tecnología no reemplaza a la naturaleza: nos ayuda a escucharla.
          Así podría verse el registro diario de una planta.
        </p>
        <div class="signal-tabs" role="group" aria-label="Elegir una señal de la planta">
          <button type="button" class:active={currentSignal === 'suelo'} aria-pressed={currentSignal === 'suelo'} on:click={() => (currentSignal = 'suelo')}>Suelo</button>
          <button type="button" class:active={currentSignal === 'luz'} aria-pressed={currentSignal === 'luz'} on:click={() => (currentSignal = 'luz')}>Luz</button>
          <button type="button" class:active={currentSignal === 'aire'} aria-pressed={currentSignal === 'aire'} on:click={() => (currentSignal = 'aire')}>Aire</button>
        </div>
        <p class="signal-note"><span aria-hidden="true">✳</span> {activeSignal.detail}</p>
      </div>

      <div class="sensor-card">
        <div class="sensor-topline"><span>INVERNADERO 01</span><span class="live-dot">REGISTRO DE EJEMPLO</span></div>
        <div class="sensor-reading">
          <div>
            <p>{activeSignal.label}</p>
            <strong>{activeSignal.value}</strong>
          </div>
          <div class="sensor-leaf" aria-hidden="true">
            <svg viewBox="0 0 64 64" fill="none">
              <path d="M13 48C14 26 29 13 52 12c0 23-13 38-39 36Z" fill="#9FB38B" />
              <path d="M15 47c12-12 23-23 35-33" stroke="#425D4A" stroke-width="2" />
              <path d="m28 34-1-11m10 3-1-7m-2 23-11-3" stroke="#425D4A" stroke-width="1.5" />
            </svg>
          </div>
        </div>
        <div class="meter" aria-label={`${activeSignal.label}: ${activeSignal.value}`}>
          <div class="meter-fill" style={`--meter-value: ${activeSignal.progress}%`}></div>
        </div>
        <div class="sensor-footer"><span>{activeSignal.status}</span><span>DATOS PARA CUIDAR</span></div>
      </div>
    </section>

    <section class="field-notes" id="cuaderno" aria-labelledby="field-title">
      <div class="field-heading">
        <p class="kicker"><span class="kicker-line"></span> NOTAS PARA LLEVAR</p>
        <h2 id="field-title">Tres ideas para mirar distinto.</h2>
      </div>
      <div class="note-list">
        <article class="note-item">
          <span class="note-index">01</span>
          <p><strong>Observa antes de intervenir.</strong> Cada organismo ya tiene estrategias que vale la pena entender.</p>
        </article>
        <article class="note-item">
          <span class="note-index">02</span>
          <p><strong>La tecnología también puede ser humilde.</strong> Un buen sensor sirve para hacer mejores preguntas.</p>
        </article>
        <article class="note-item">
          <span class="note-index">03</span>
          <p><strong>Todo está conectado.</strong> Cuidar una planta es aprender sobre agua, suelo, clima y comunidad.</p>
        </article>
      </div>
    </section>

    <footer class="magazine-footer">
      <a class="brand footer-brand" href="#inicio">
        <span class="brand-mark" aria-hidden="true">
          <svg viewBox="0 0 42 42" fill="none">
            <path d="M21 34V18m0 8c-8 0-13-5-13-13 8 0 13 5 13 13Zm0-5c0-8 5-13 13-13 0 8-5 13-13 13Z" />
            <path d="M14 34h14" />
          </svg>
        </span>
        <span class="brand-name">raíz <i>y</i> razón</span>
      </a>
      <p>Una edición imaginada para celebrar las ideas que crecen entre ciencia y naturaleza.</p>
      <a class="back-to-top" href="#inicio">Volver arriba ↑</a>
    </footer>
  </div>
</main>

<style>
  :global(html) {
    scroll-behavior: smooth;
    background: #f3f1e9;
  }

  :global(body) {
    margin: 0;
  }

  .magazine {
    --ink: #26342c;
    --muted: #70796e;
    --green: #526a54;
    --paper: #f3f1e9;
    min-height: 100vh;
    padding: 0 28px;
    background:
      radial-gradient(ellipse at 87% 5%, rgba(216, 221, 193, .28), transparent 28rem),
      var(--paper);
    color: var(--ink);
    font-family: "Avenir Next", Avenir, "Segoe UI", sans-serif;
  }

  .page-shell {
    width: min(1120px, 100%);
    margin: 0 auto;
  }

  .skip-link {
    position: absolute;
    top: -60px;
    left: 16px;
    z-index: 5;
    padding: 10px 14px;
    background: var(--ink);
    color: white;
  }

  .skip-link:focus {
    top: 12px;
  }

  .masthead {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    align-items: center;
    min-height: 92px;
    border-bottom: 1px solid #d8d8ca;
  }

  .brand {
    display: inline-flex;
    align-items: center;
    gap: 9px;
    width: fit-content;
    color: var(--ink);
    text-decoration: none;
  }

  .brand-mark {
    display: grid;
    width: 38px;
    height: 38px;
    place-items: center;
    border: 1px solid #9fa991;
    border-radius: 50%;
  }

  .brand-mark svg {
    width: 28px;
    stroke: var(--green);
    stroke-width: 1.8;
    stroke-linecap: round;
    stroke-linejoin: round;
  }

  .brand-name {
    font-family: Georgia, "Times New Roman", serif;
    font-size: 23px;
    font-weight: 700;
    letter-spacing: -.9px;
  }

  .brand-name i {
    color: #788868;
    font-weight: 400;
  }

  .masthead-note {
    margin: 0;
    color: var(--muted);
    font-family: Georgia, "Times New Roman", serif;
    font-size: 13px;
    font-style: italic;
    text-align: center;
  }

  .issue-stamp {
    display: flex;
    flex-direction: column;
    gap: 5px;
    align-items: flex-end;
    color: var(--muted);
    font-size: 9px;
    letter-spacing: 1.5px;
  }

  .issue-stamp span:first-child {
    color: var(--tab-color, var(--ink));
    font-weight: 700;
  }

  .issue-nav {
    display: flex;
    min-height: 50px;
    align-items: center;
    gap: 30px;
    border-bottom: 1px solid #d8d8ca;
  }

  .issue-nav a,
  .nav-note {
    color: #505b50;
    font-size: 11px;
    text-decoration: none;
  }

  .issue-nav a:hover,
  .issue-nav a:focus-visible,
  .text-link:hover,
  .text-link:focus-visible {
    color: #8b6943;
  }

  .nav-note {
    margin-left: auto;
    color: #858b7e;
    font-size: 9px;
    letter-spacing: 1px;
    text-transform: uppercase;
  }

  .nav-note span {
    padding: 0 5px;
    color: #9c8056;
  }

  .cover-story {
    display: grid;
    min-height: 510px;
    grid-template-columns: .9fr 1.1fr;
    align-items: stretch;
    gap: 44px;
    padding: 54px 0 45px;
    border-bottom: 1px solid #d8d8ca;
  }

  .cover-copy {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 20px 0 0 6px;
  }

  .kicker {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 0 0 22px;
    color: #6f7a68;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 1.65px;
  }

  .kicker-line {
    width: 23px;
    height: 1px;
    background: #9d8a64;
  }

  .cover-copy h1,
  .section-heading h2,
  .observatory h2 {
    margin: 0;
    font-family: Georgia, "Times New Roman", serif;
    font-weight: 400;
    letter-spacing: -2.5px;
  }

  .cover-copy h1 {
    max-width: 465px;
    font-size: clamp(47px, 5.3vw, 68px);
    line-height: .99;
  }

  .cover-copy h1 em,
  .section-heading h2 em,
  .observatory h2 em {
    color: #72836b;
    font-weight: 400;
  }

  .cover-intro {
    max-width: 390px;
    margin: 23px 0 25px;
    color: #687064;
    font-size: 13px;
    line-height: 1.85;
  }

  .text-link {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    padding-bottom: 5px;
    border-bottom: 1px solid #aeb39f;
    color: var(--ink);
    font-size: 11px;
    font-weight: 700;
    text-decoration: none;
    transition: color .2s ease;
  }

  .text-link span {
    font-size: 15px;
  }

  .cover-byline {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-top: auto;
    padding-top: 40px;
    color: #8a8e80;
    font-size: 8px;
    letter-spacing: 1.2px;
  }

  .byline-rule {
    width: 28px;
    height: 1px;
    background: #a6aa98;
  }

  .cover-art {
    position: relative;
    display: flex;
    min-height: 410px;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    background:
      radial-gradient(ellipse at 50% 49%, rgba(195, 207, 165, .16), transparent 38%),
      #354b3c;
  }

  .cover-art::after {
    position: absolute;
    inset: 12px;
    border: 1px solid rgba(226, 232, 209, .2);
    content: "";
    pointer-events: none;
  }

  .plant-illustration {
    width: 95%;
    height: 90%;
    max-height: 440px;
  }

  .art-caption,
  .art-label {
    position: absolute;
    z-index: 1;
    color: #e0e6d2;
    font-size: 8px;
    letter-spacing: 1.3px;
  }

  .art-caption {
    top: 30px;
    left: 32px;
    color: #c2cbb7;
  }

  .art-caption span,
  .art-label span {
    margin-right: 7px;
    color: #d7dcae;
  }

  .art-label-top {
    top: 32%;
    right: 7%;
  }

  .art-label-bottom {
    bottom: 23%;
    left: 7%;
  }

  .art-orbit {
    position: absolute;
    right: 25px;
    bottom: 28px;
    color: #b7c3ad;
    font-size: 7px;
    letter-spacing: 1.2px;
  }

  .art-orbit span {
    padding: 0 5px;
    color: #d5d9a8;
  }

  .briefing-strip {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    padding: 23px 0;
    border-bottom: 1px solid #d8d8ca;
  }

  .briefing-strip > div {
    display: grid;
    grid-template-columns: 25px 1fr;
    column-gap: 10px;
    align-items: center;
    padding-left: 12%;
  }

  .briefing-strip > div + div {
    border-left: 1px solid #d8d8ca;
  }

  .briefing-icon {
    grid-row: span 2;
    color: #8b8c68;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 20px;
  }

  .briefing-strip strong {
    font-family: Georgia, "Times New Roman", serif;
    font-size: 13px;
    font-weight: 400;
  }

  .briefing-strip div > span:last-child {
    margin-top: 4px;
    color: #818577;
    font-size: 9px;
  }

  .stories-section {
    padding: 66px 0 67px;
    border-bottom: 1px solid #d8d8ca;
  }

  .section-heading {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    margin-bottom: 27px;
  }

  .section-heading .kicker {
    margin-bottom: 13px;
  }

  .section-heading h2,
  .observatory h2 {
    font-size: clamp(32px, 4vw, 43px);
    line-height: 1.08;
    letter-spacing: -1.6px;
  }

  .section-link {
    margin-bottom: 5px;
  }

  .story-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
  }

  .story-card {
    overflow: hidden;
    border: 1px solid #deded1;
    background: rgba(255, 255, 255, .24);
  }

  .story-art {
    position: relative;
    display: flex;
    height: 165px;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }

  .story-art svg {
    width: 100%;
    height: 100%;
  }

  .story-art-leaf {
    background: #dfe4d2;
  }

  .story-art-tech {
    background: #465a4a;
  }

  .story-art-field {
    background: #e7e1d1;
  }

  .story-number {
    position: absolute;
    top: 14px;
    left: 15px;
    z-index: 1;
    color: rgba(44, 58, 46, .72);
    font-size: 8px;
    font-weight: 700;
    letter-spacing: 1.2px;
  }

  .story-art-tech .story-number {
    color: #d4dfcb;
  }

  .story-copy {
    padding: 18px 18px 20px;
  }

  .story-meta {
    margin: 0 0 11px;
    color: #818575;
    font-size: 8px;
    font-weight: 700;
    letter-spacing: 1px;
  }

  .story-meta span {
    color: #a5a18e;
    font-weight: 400;
  }

  .story-copy h3 {
    min-height: 52px;
    margin: 0;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 20px;
    font-weight: 400;
    line-height: 1.25;
  }

  .story-copy > p:not(.story-meta) {
    min-height: 55px;
    margin: 10px 0 15px;
    color: #73796e;
    font-size: 10px;
    line-height: 1.7;
  }

  .story-copy a {
    color: #536a54;
    font-size: 10px;
    font-weight: 700;
    text-decoration: none;
  }

  .story-copy a:hover,
  .story-copy a:focus-visible {
    color: #8b6943;
  }

  .story-copy a span {
    margin-left: 5px;
  }

  .observatory {
    display: grid;
    grid-template-columns: 1fr .85fr;
    align-items: center;
    gap: 70px;
    padding: 66px 6%;
    border-bottom: 1px solid #d8d8ca;
    background: #e9e9dc;
  }

  .observatory-copy .kicker {
    margin-bottom: 15px;
  }

  .observatory-copy > p:not(.kicker):not(.signal-note) {
    max-width: 390px;
    margin: 16px 0 20px;
    color: #70786d;
    font-size: 11px;
    line-height: 1.8;
  }

  .signal-tabs {
    display: flex;
    gap: 7px;
  }

  .signal-tabs button {
    padding: 7px 13px;
    border: 1px solid #c8caba;
    border-radius: 18px;
    background: transparent;
    color: #626d60;
    cursor: pointer;
    font: inherit;
    font-size: 9px;
    transition: background .2s ease, color .2s ease, border-color .2s ease;
  }

  .signal-tabs button:hover,
  .signal-tabs button:focus-visible {
    border-color: #667b63;
  }

  .signal-tabs button.active {
    border-color: #536b55;
    background: #536b55;
    color: #fff;
  }

  .signal-note {
    max-width: 400px;
    min-height: 32px;
    margin: 17px 0 0;
    color: #747b70;
    font-size: 9px;
    line-height: 1.7;
  }

  .signal-note span {
    margin-right: 4px;
    color: #9c8056;
  }

  .sensor-card {
    padding: 23px 23px 19px;
    border: 1px solid #cdd0c0;
    background: rgba(248, 248, 240, .62);
  }

  .sensor-topline,
  .sensor-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: #868c7c;
    font-size: 7px;
    font-weight: 700;
    letter-spacing: 1px;
  }

  .live-dot {
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }

  .live-dot::before {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #8c9d72;
    content: "";
  }

  .sensor-reading {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 27px 0 21px;
  }

  .sensor-reading p {
    margin: 0 0 5px;
    color: #737b6d;
    font-size: 10px;
  }

  .sensor-reading strong {
    font-family: Georgia, "Times New Roman", serif;
    font-size: 39px;
    font-weight: 400;
    letter-spacing: -1px;
  }

  .sensor-leaf {
    display: grid;
    width: 55px;
    height: 55px;
    place-items: center;
    border-radius: 50%;
    background: #e2e7d8;
  }

  .sensor-leaf svg {
    width: 42px;
  }

  .meter {
    height: 5px;
    overflow: hidden;
    background: #d9ddcf;
  }

  .meter-fill {
    width: var(--meter-value);
    height: 100%;
    background: #74876c;
    transition: width .3s ease;
  }

  .sensor-footer {
    margin-top: 10px;
    font-size: 7px;
    font-weight: 400;
    letter-spacing: .7px;
  }

  .sensor-footer span:first-child {
    color: #596e56;
    font-weight: 700;
  }

  .field-notes {
    display: grid;
    grid-template-columns: .8fr 1.2fr;
    gap: 45px;
    padding: 60px 6%;
    border-bottom: 1px solid #d8d8ca;
  }

  .field-heading .kicker {
    margin-bottom: 13px;
  }

  .field-heading h2 {
    max-width: 300px;
    margin: 0;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 29px;
    font-weight: 400;
    letter-spacing: -1px;
    line-height: 1.15;
  }

  .note-item {
    display: grid;
    grid-template-columns: 34px 1fr;
    gap: 10px;
    align-items: baseline;
    padding: 12px 0;
    border-bottom: 1px solid #deded1;
  }

  .note-item:first-child {
    padding-top: 0;
  }

  .note-item:last-child {
    border-bottom: 0;
  }

  .note-index {
    color: #9a8c6e;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 14px;
    font-style: italic;
  }

  .note-item p {
    margin: 0;
    color: #72796e;
    font-size: 10px;
    line-height: 1.7;
  }

  .note-item strong {
    color: #344337;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 13px;
    font-weight: 400;
  }

  .magazine-footer {
    display: flex;
    min-height: 90px;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
  }

  .footer-brand .brand-mark {
    width: 32px;
    height: 32px;
  }

  .footer-brand .brand-mark svg {
    width: 24px;
  }

  .footer-brand .brand-name {
    font-size: 19px;
  }

  .magazine-footer > p {
    max-width: 350px;
    margin: 0;
    color: #85897c;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 10px;
    font-style: italic;
    text-align: center;
  }

  .back-to-top {
    color: #65735f;
    font-size: 9px;
    text-decoration: none;
  }

  @media (max-width: 760px) {
    .magazine {
      padding: 0 20px;
    }

    .masthead {
      grid-template-columns: 1fr auto;
      min-height: 76px;
    }

    .masthead-note {
      display: none;
    }

    .cover-story {
      grid-template-columns: 1fr 1fr;
      gap: 22px;
      min-height: 430px;
      padding-top: 38px;
    }

    .cover-copy h1 {
      font-size: clamp(42px, 7vw, 56px);
    }

    .cover-art {
      min-height: 360px;
    }

    .briefing-strip > div {
      padding-left: 7%;
    }

    .story-grid {
      gap: 12px;
    }

    .story-copy {
      padding: 15px 13px 17px;
    }

    .story-copy h3 {
      font-size: 17px;
    }

    .observatory {
      gap: 35px;
      padding-right: 2%;
      padding-left: 2%;
    }

    .field-notes {
      gap: 25px;
      padding-right: 2%;
      padding-left: 2%;
    }
  }

  @media (max-width: 560px) {
    .magazine {
      padding: 0 16px;
    }

    .brand-name {
      font-size: 20px;
    }

    .issue-stamp {
      font-size: 8px;
    }

    .issue-nav {
      min-height: 45px;
      justify-content: space-between;
      gap: 12px;
    }

    .issue-nav a {
      font-size: 10px;
    }

    .nav-note {
      display: none;
    }

    .cover-story {
      grid-template-columns: 1fr;
      gap: 25px;
      padding: 38px 0 30px;
    }

    .cover-copy {
      padding: 0;
    }

    .cover-copy h1 {
      max-width: 440px;
      font-size: clamp(48px, 13vw, 64px);
    }

    .cover-intro {
      margin: 17px 0 19px;
    }

    .cover-byline {
      display: none;
    }

    .cover-art {
      min-height: 330px;
    }

    .briefing-strip {
      grid-template-columns: 1fr;
      gap: 14px;
      padding: 18px 2px;
    }

    .briefing-strip > div {
      padding-left: 0;
    }

    .briefing-strip > div + div {
      padding-top: 12px;
      border-top: 1px solid #d8d8ca;
      border-left: 0;
    }

    .stories-section {
      padding: 48px 0;
    }

    .section-heading {
      align-items: flex-start;
      gap: 14px;
    }

    .section-heading h2 {
      font-size: 34px;
    }

    .section-link {
      flex: 0 0 auto;
      margin-top: 36px;
      font-size: 9px;
    }

    .story-grid {
      grid-template-columns: 1fr;
      gap: 14px;
    }

    .story-card {
      display: grid;
      grid-template-columns: .8fr 1.2fr;
    }

    .story-art {
      height: 100%;
      min-height: 180px;
    }

    .story-copy h3,
    .story-copy > p:not(.story-meta) {
      min-height: 0;
    }

    .story-copy h3 {
      font-size: 18px;
    }

    .observatory {
      grid-template-columns: 1fr;
      gap: 28px;
      padding: 45px 0;
    }

    .field-notes {
      grid-template-columns: 1fr;
      gap: 25px;
      padding: 45px 0;
    }

    .field-heading h2 {
      max-width: 400px;
    }

    .magazine-footer {
      min-height: 100px;
      flex-wrap: wrap;
      padding: 15px 0;
    }

    .magazine-footer > p {
      order: 3;
      max-width: none;
      flex-basis: 100%;
      text-align: left;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    :global(html) {
      scroll-behavior: auto;
    }

    *,
    *::before,
    *::after {
      transition-duration: .01ms !important;
    }
  }
</style>
