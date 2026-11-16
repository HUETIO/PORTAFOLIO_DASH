<script>
  import { onDestroy } from "svelte";

  export let color = "#00ffd5";

  const messageTypes = [
    { id: "info", label: "Información", icon: "i", tone: "blue" },
    { id: "success", label: "Éxito", icon: "✓", tone: "green" },
    { id: "warning", label: "Advertencia", icon: "!", tone: "amber" },
    { id: "error", label: "Error", icon: "×", tone: "red" },
  ];

  const tabs = [
    { id: "overview", label: "Resumen" },
    { id: "details", label: "Detalles" },
    { id: "activity", label: "Actividad" },
  ];

  const faqItems = [
    {
      question: "¿Qué es una ventana modal?",
      answer:
        "Es una ventana que aparece sobre el contenido y solicita una acción antes de continuar. En Svelte se puede mostrar o quitar con un bloque {#if}.",
    },
    {
      question: "¿Cómo se actualiza un componente?",
      answer:
        "En este ejemplo, las variables locales controlan la interfaz: al cambiar su valor, Svelte vuelve a renderizar las partes afectadas.",
    },
    {
      question: "¿Qué diferencia hay entre una alerta y un toast?",
      answer:
        "La alerta interrumpe el flujo y requiere atención; el toast confirma una acción de forma breve sin bloquear la página.",
    },
  ];

  const dialogs = {
    info: {
      title: "Información",
      message: "La configuración se guardó correctamente en este dispositivo.",
      icon: "i",
      tone: "blue",
      primary: "Entendido",
    },
    success: {
      title: "¡Todo listo!",
      message: "El componente se ha actualizado y ya está disponible.",
      icon: "✓",
      tone: "green",
      primary: "Continuar",
    },
    warning: {
      title: "Confirmar cambios",
      message: "Hay cambios sin guardar. ¿Quieres salir de todos modos?",
      icon: "!",
      tone: "amber",
      primary: "Salir",
      secondary: "Seguir editando",
    },
    error: {
      title: "No se pudo completar",
      message: "Ocurrió un problema de ejemplo. Revisa los datos e inténtalo otra vez.",
      icon: "×",
      tone: "red",
      primary: "Reintentar",
    },
  };

  let activeDialog = null;
  let activeTab = "overview";
  let expandedFaq = 0;
  let toastMessage = "";
  let toastTimer;
  let userName = "";
  let userEmail = "";
  let formMessage = "";
  let notificationsEnabled = true;
  let progress = 68;

  function showDialog(type) {
    activeDialog = dialogs[type];
  }

  function closeDialog(action) {
    const wasWarning = activeDialog && activeDialog.tone === "amber";
    activeDialog = null;

    if (wasWarning) {
      showToast(action === "confirm" ? "Cambios descartados" : "Edición conservada");
    } else if (action === "confirm") {
      showToast("Acción completada");
    }
  }

  function showToast(message) {
    toastMessage = message;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      toastMessage = "";
    }, 3200);
  }

  function submitForm() {
    formMessage = `¡Gracias, ${userName.trim()}! El formulario de demostración se envió correctamente.`;
    showToast("Formulario enviado");
  }

  function changeProgress(amount) {
    progress = Math.min(100, Math.max(0, progress + amount));
  }

  onDestroy(() => {
    clearTimeout(toastTimer);
  });
</script>

<svelte:head>
  <title>Windows UI Lab · Componentes Svelte</title>
  <meta
    name="description"
    content="Laboratorio interactivo de ventanas, mensajes y componentes de interfaz con Svelte."
  />
</svelte:head>

<main class="ui-lab" style={`--page-accent: ${color || "#00ffd5"}`}>
  <header class="topbar">
    <a class="brand" href="#inicio" aria-label="Windows UI Lab, inicio">
      <span class="window-mark" aria-hidden="true">
        <i></i><i></i><i></i><i></i>
      </span>
      <span>Windows UI <b>Lab</b></span>
    </a>
    <nav class="top-nav" aria-label="Navegación principal">
      <a href="#ventanas">Ventanas</a>
      <a href="#componentes">Componentes</a>
      <a href="#formulario">Formulario</a>
    </nav>
    <span class="version-pill"><span class="live-dot"></span> Svelte showcase</span>
  </header>

  <section class="hero" id="inicio">
    <div class="hero-copy">
      <p class="eyebrow"><span></span> INTERFAZ INTERACTIVA · SVELTE</p>
      <h1>Ventanas, mensajes<br />y <span>componentes.</span></h1>
      <p class="hero-description">
        Un pequeño laboratorio inspirado en Windows para explorar patrones de interfaz
        construidos con componentes reactivos de Svelte.
      </p>
      <div class="hero-actions">
        <a class="button button-primary" href="#ventanas">Explorar ventanas <span>↘</span></a>
        <a class="text-link" href="#componentes">Ver componentes <span>→</span></a>
      </div>
      <div class="hero-meta">
        <span><i class="meta-check">✓</i> Interactivo</span>
        <span><i class="meta-check">✓</i> Adaptable</span>
        <span><i class="meta-check">✓</i> Sin dependencias UI</span>
      </div>
    </div>

    <div class="hero-visual" aria-label="Vista previa de una ventana de Windows">
      <div class="glow-orb"></div>
      <div class="preview-window">
        <div class="window-titlebar">
          <div class="window-title"><span class="mini-window-mark">▦</span> Centro de notificaciones</div>
          <div class="window-controls" aria-hidden="true"><span>−</span><span>□</span><span>×</span></div>
        </div>
        <div class="preview-content">
          <div class="preview-icon green">✓</div>
          <div>
            <p class="preview-kicker">OPERACIÓN COMPLETADA</p>
            <h2>¡Todo en orden!</h2>
            <p>Tu espacio de trabajo está actualizado y listo para continuar.</p>
          </div>
        </div>
        <div class="preview-footer">
          <span><i class="live-dot"></i> Sistema activo</span>
          <button type="button" on:click={() => showDialog("success")}>Ver mensaje</button>
        </div>
        <div class="floating-notice">
          <span class="notice-symbol">✦</span>
          <span><b>Notificación</b><small>Los cambios se guardaron</small></span>
          <span class="notice-time">ahora</span>
        </div>
      </div>
      <div class="hero-chip chip-top"><span>✦</span> Feedback claro</div>
      <div class="hero-chip chip-bottom"><span class="live-dot"></span> Estado reactivo</div>
    </div>
  </section>

  <section class="section-block" id="ventanas">
    <div class="section-heading">
      <div>
        <p class="eyebrow"><span></span> MENSAJES DEL SISTEMA</p>
        <h2>¿Qué necesitas comunicar?</h2>
        <p class="section-description">Prueba cuatro tipos de cuadros de mensaje y sus estados.</p>
      </div>
      <span class="section-count">01 <i>/</i> 04</span>
    </div>

    <div class="message-grid">
      {#each messageTypes as item}
        <article class="message-card">
          <div class={`message-icon ${item.tone}`}>{item.icon}</div>
          <div class="message-copy">
            <span class="card-overline">MESSAGE BOX · {item.id.toUpperCase()}</span>
            <h3>{item.label}</h3>
            <p>
              {#if item.id === "info"}Presenta contexto útil sin interrumpir la tarea.
              {:else if item.id === "success"}Confirma que una acción terminó bien.
              {:else if item.id === "warning"}Solicita atención antes de una decisión.
              {:else}Explica un problema y ofrece el siguiente paso.{/if}
            </p>
          </div>
          <button
            type="button"
            class="icon-button"
            aria-label={`Abrir mensaje de ${item.label.toLowerCase()}`}
            on:click={() => showDialog(item.id)}
          >↗</button>
        </article>
      {/each}
    </div>
  </section>

  <section class="section-block component-section" id="componentes">
    <div class="section-heading">
      <div>
        <p class="eyebrow"><span></span> KIT DE INTERFAZ</p>
        <h2>Pequeños bloques, grandes experiencias.</h2>
        <p class="section-description">Componentes cotidianos con estado, acciones y feedback.</p>
      </div>
      <span class="section-count">02 <i>/</i> 04</span>
    </div>

    <div class="component-grid">
      <article class="demo-card tabs-card">
        <div class="demo-card-heading">
          <div><span class="component-label">NAVEGACIÓN</span><h3>Pestañas</h3></div>
          <span class="code-chip">tabs</span>
        </div>
        <div class="tab-list" role="tablist" aria-label="Pestañas de demostración">
          {#each tabs as tab}
            <button
              type="button"
              id={`tab-${tab.id}`}
              role="tab"
              aria-selected={activeTab === tab.id}
              aria-controls="tab-panel"
              class:active={activeTab === tab.id}
              on:click={() => (activeTab = tab.id)}
            >{tab.label}</button>
          {/each}
        </div>
        <div class="tab-panel" id="tab-panel" role="tabpanel" aria-labelledby={`tab-${activeTab}`}>
          {#if activeTab === "overview"}
            <span class="panel-icon">◈</span>
            <div><b>Vista general</b><p>Organiza contenido relacionado sin salir de la sección.</p></div>
          {:else if activeTab === "details"}
            <span class="panel-icon">⌘</span>
            <div><b>Detalles del componente</b><p>El estado activo se refleja visualmente y con aria-selected.</p></div>
          {:else}
            <span class="panel-icon">◷</span>
            <div><b>Actividad reciente</b><p>Las pestañas cambian al instante, sin recargar la página.</p></div>
          {/if}
        </div>
      </article>

      <article class="demo-card toggle-card">
        <div class="demo-card-heading">
          <div><span class="component-label">PREFERENCIAS</span><h3>Interruptor</h3></div>
          <span class="code-chip">toggle</span>
        </div>
        <div class="setting-row">
          <div class="setting-icon">♧</div>
          <div class="setting-description"><b>Notificaciones</b><span>Recibe novedades del sistema</span></div>
          <button
            type="button"
            class="switch"
            class:enabled={notificationsEnabled}
            role="switch"
            aria-checked={notificationsEnabled}
            aria-label="Activar notificaciones"
            on:click={() => (notificationsEnabled = !notificationsEnabled)}
          ><span></span></button>
        </div>
        <div class="setting-status">
          <span class:status-on={notificationsEnabled}></span>
          Notificaciones {notificationsEnabled ? "activadas" : "en pausa"}
        </div>
      </article>

      <article class="demo-card progress-card">
        <div class="demo-card-heading">
          <div><span class="component-label">ESTADO</span><h3>Progreso</h3></div>
          <span class="code-chip">{progress}%</span>
        </div>
        <div class="progress-label"><span>Instalando componentes</span><b>{progress}%</b></div>
        <div
          class="progress-track"
          role="progressbar"
          aria-label="Progreso de instalación"
          aria-valuemin="0"
          aria-valuemax="100"
          aria-valuenow={progress}
        ><span style={`width: ${progress}%`}></span></div>
        <div class="progress-footer">
          <span>{progress === 100 ? "Instalación finalizada" : "Aproximadamente 2 minutos"}</span>
          <div class="progress-actions">
            <button type="button" aria-label="Reducir progreso" on:click={() => changeProgress(-10)}>−</button>
            <button type="button" aria-label="Aumentar progreso" on:click={() => changeProgress(10)}>+</button>
          </div>
        </div>
      </article>

      <article class="demo-card accordion-card">
        <div class="demo-card-heading">
          <div><span class="component-label">CONTENIDO</span><h3>Preguntas frecuentes</h3></div>
          <span class="code-chip">accordion</span>
        </div>
        <div class="faq-list">
          {#each faqItems as faq, index}
            <div class="faq-item">
              <button
                type="button"
                aria-expanded={expandedFaq === index}
                aria-controls={`faq-answer-${index}`}
                on:click={() => (expandedFaq = expandedFaq === index ? -1 : index)}
              >
                {faq.question}<span class:rotated={expandedFaq === index}>⌄</span>
              </button>
              {#if expandedFaq === index}
                <p id={`faq-answer-${index}`}>{faq.answer}</p>
              {/if}
            </div>
          {/each}
        </div>
      </article>
    </div>
  </section>

  <section class="section-block form-section" id="formulario">
    <div class="section-heading">
      <div>
        <p class="eyebrow"><span></span> ENTRADA DE DATOS</p>
        <h2>Un formulario listo para usar.</h2>
        <p class="section-description">Campos con etiquetas, validación del navegador y confirmación visual.</p>
      </div>
      <span class="section-count">03 <i>/</i> 04</span>
    </div>

    <div class="form-layout">
      <div class="form-intro">
        <div class="form-illustration"><span>✉</span><i>✦</i><b>↗</b></div>
        <h3>Hablemos de tu próximo proyecto.</h3>
        <p>Completa estos campos para probar el patrón de formulario. No se envían datos a ningún servidor.</p>
        <div class="privacy-note"><span>◈</span> Demostración local · tus datos no se guardan</div>
      </div>
      <form class="contact-form" on:submit|preventDefault={submitForm}>
        <label for="name">Nombre <span>*</span></label>
        <input id="name" name="name" type="text" placeholder="¿Cómo te llamas?" bind:value={userName} required />
        <label for="email">Correo electrónico <span>*</span></label>
        <input id="email" name="email" type="email" placeholder="nombre@ejemplo.com" bind:value={userEmail} required />
        <button class="button button-primary submit-button" type="submit">Enviar mensaje <span>→</span></button>
        {#if formMessage}
          <p class="form-feedback" role="status">{formMessage}</p>
        {/if}
      </form>
    </div>
  </section>

  <section class="closing-banner">
    <div class="closing-spark">✦</div>
    <div><p class="eyebrow">SIGUIENTE PASO</p><h2>¿Listo para construir algo increíble?</h2></div>
    <button type="button" class="button button-light" on:click={() => showDialog("info")}>Explorar el laboratorio <span>↗</span></button>
  </section>

  <footer class="page-footer">
    <a class="brand footer-brand" href="#inicio">
      <span class="window-mark" aria-hidden="true"><i></i><i></i><i></i><i></i></span>
      <span>Windows UI <b>Lab</b></span>
    </a>
    <span>Diseñado para aprender. Construido con componentes Svelte.</span>
    <a href="#inicio" class="back-top">Volver arriba ↑</a>
  </footer>

  {#if activeDialog}
    <div class="modal-layer">
      <dialog
        open
        class="message-dialog"
        aria-modal="true"
        aria-labelledby="dialog-title"
        aria-describedby="dialog-message"
      >
        <div class="dialog-titlebar">
          <span id="dialog-title">{activeDialog.title}</span>
          <button type="button" class="dialog-close" aria-label="Cerrar ventana" on:click={() => closeDialog("cancel")}>×</button>
        </div>
        <div class="dialog-body">
          <div class={`dialog-icon ${activeDialog.tone}`}>{activeDialog.icon}</div>
          <p id="dialog-message">{activeDialog.message}</p>
        </div>
        <div class="dialog-actions">
          {#if activeDialog.secondary}
            <button type="button" class="button button-quiet" on:click={() => closeDialog("cancel")}>{activeDialog.secondary}</button>
          {/if}
          <button type="button" class="button button-primary" on:click={() => closeDialog("confirm")}>{activeDialog.primary}</button>
        </div>
      </dialog>
    </div>
  {/if}

  {#if toastMessage}
    <div class="toast-message" role="status" aria-live="polite">
      <span class="toast-check">✓</span>{toastMessage}
      <button type="button" aria-label="Cerrar notificación" on:click={() => (toastMessage = "")}>×</button>
    </div>
  {/if}
</main>

<style>
  :global(*) { box-sizing: border-box; }

  .ui-lab {
    --page-accent: #00ffd5;
    --ink: #e8ecf5;
    --muted: #9299ab;
    --surface: #12151d;
    --surface-raised: #181c26;
    --line: rgba(195, 205, 226, .11);
    min-height: 100vh;
    overflow: hidden;
    color: var(--ink);
    background:
      radial-gradient(ellipse at 50% -18%, color-mix(in srgb, var(--page-accent) 9%, transparent), transparent 38%),
      #0d0f15;
    font-family: Inter, "Segoe UI", Arial, sans-serif;
  }

  .topbar, .page-footer {
    width: min(1160px, calc(100% - 64px));
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .topbar { height: 78px; border-bottom: 1px solid var(--line); }
  .brand { display: inline-flex; gap: 11px; align-items: center; color: var(--ink); text-decoration: none; font-size: 15px; font-weight: 650; letter-spacing: -.3px; }
  .brand b { color: var(--page-accent); font-weight: 700; }
  .window-mark { display: grid; width: 21px; height: 21px; grid-template-columns: 1fr 1fr; gap: 3px; transform: skewY(-8deg); }
  .window-mark i { background: var(--page-accent); border-radius: 1px; }
  .window-mark i:nth-child(2), .window-mark i:nth-child(3) { opacity: .76; }
  .top-nav { display: flex; gap: 34px; }
  .top-nav a, .back-top { color: #a7adbc; text-decoration: none; font-size: 12px; transition: color .2s ease; }
  .top-nav a:hover, .back-top:hover { color: var(--page-accent); }
  .version-pill { border: 1px solid var(--line); color: #b7bdca; border-radius: 30px; padding: 8px 12px; font-size: 10px; }
  .live-dot { display: inline-block; width: 7px; height: 7px; margin-right: 7px; border-radius: 50%; background: #48d7a1; box-shadow: 0 0 9px rgba(72,215,161,.65); }

  .hero { width: min(1160px, calc(100% - 64px)); min-height: 530px; margin: auto; display: grid; grid-template-columns: 1fr 1fr; align-items: center; gap: 48px; }
  .hero-copy { padding: 44px 0 50px; }
  .eyebrow { margin: 0 0 17px; color: #a2a9b9; font-size: 9px; font-weight: 700; letter-spacing: 1.65px; }
  .eyebrow > span { display: inline-block; width: 17px; height: 2px; margin: 0 8px 3px 0; background: var(--page-accent); }
  h1, h2, h3, p { margin-top: 0; }
  .hero h1 { margin-bottom: 19px; font-size: clamp(42px, 5vw, 63px); line-height: 1.06; letter-spacing: -3.2px; font-weight: 720; }
  .hero h1 span { color: var(--page-accent); }
  .hero-description { max-width: 470px; color: #9da4b3; font-size: 14px; line-height: 1.85; }
  .hero-actions { display: flex; align-items: center; gap: 25px; margin-top: 28px; }
  .button { min-height: 40px; padding: 0 16px; border: 0; border-radius: 7px; cursor: pointer; font: inherit; font-size: 11px; font-weight: 700; transition: transform .2s ease, filter .2s ease, background .2s ease; }
  .button:hover { transform: translateY(-2px); filter: brightness(1.09); }
  .button-primary { color: #081412; background: var(--page-accent); box-shadow: 0 7px 22px color-mix(in srgb, var(--page-accent) 17%, transparent); text-decoration: none; display: inline-flex; align-items: center; justify-content: center; gap: 14px; }
  .button-primary span, .button-light span { font-size: 15px; }
  .text-link { color: #c2c7d2; font-size: 11px; text-decoration: none; }
  .text-link span { margin-left: 6px; color: var(--page-accent); }
  .hero-meta { display: flex; flex-wrap: wrap; gap: 19px; margin-top: 40px; color: #858d9f; font-size: 10px; }
  .meta-check { margin-right: 5px; color: var(--page-accent); font-style: normal; }

  .hero-visual { position: relative; min-height: 350px; display: grid; place-items: center; }
  .glow-orb { position: absolute; width: 330px; height: 280px; border-radius: 50%; background: color-mix(in srgb, var(--page-accent) 11%, transparent); filter: blur(80px); }
  .preview-window { position: relative; z-index: 1; width: min(440px, 100%); border: 1px solid rgba(204,214,233,.17); border-radius: 11px; background: rgba(23,27,37,.96); box-shadow: 0 28px 80px rgba(0,0,0,.4); }
  .window-titlebar { height: 41px; padding: 0 14px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid var(--line); color: #b8bfcc; font-size: 10px; }
  .window-title { display: flex; align-items: center; gap: 8px; }
  .mini-window-mark { color: var(--page-accent); font-size: 15px; }
  .window-controls { display: flex; gap: 15px; color: #9299a8; font-size: 13px; }
  .preview-content { display: flex; gap: 15px; padding: 27px 23px 24px; }
  .preview-icon, .dialog-icon { flex: 0 0 auto; display: grid; width: 37px; height: 37px; place-items: center; border-radius: 50%; font-size: 19px; font-weight: 650; }
  .preview-icon.green, .dialog-icon.green { color: #45d7a1; background: rgba(69,215,161,.12); }
  .preview-kicker { margin: 2px 0 8px; color: #54d9a8; font-size: 8px; letter-spacing: 1.1px; font-weight: 700; }
  .preview-content h2 { margin: 0 0 7px; font-size: 19px; letter-spacing: -.5px; }
  .preview-content p:last-child { max-width: 290px; margin-bottom: 0; color: #969eae; font-size: 10px; line-height: 1.7; }
  .preview-footer { display: flex; align-items: center; justify-content: space-between; padding: 12px 16px; border-top: 1px solid var(--line); color: #929aaa; font-size: 9px; }
  .preview-footer button { padding: 7px 10px; border: 1px solid rgba(0,255,213,.25); border-radius: 5px; color: var(--page-accent); background: rgba(0,255,213,.06); cursor: pointer; font: inherit; font-size: 9px; }
  .floating-notice { position: absolute; right: -25px; bottom: -34px; display: flex; align-items: center; gap: 11px; min-width: 235px; padding: 13px; border: 1px solid rgba(204,214,233,.14); border-radius: 9px; background: #1b202b; box-shadow: 0 13px 35px rgba(0,0,0,.32); }
  .notice-symbol { display: grid; width: 30px; height: 30px; place-items: center; border-radius: 7px; color: var(--page-accent); background: rgba(0,255,213,.09); }
  .floating-notice b, .floating-notice small { display: block; }
  .floating-notice b { font-size: 10px; }
  .floating-notice small { margin-top: 4px; color: #969eae; font-size: 9px; }
  .notice-time { align-self: flex-start; margin-left: auto; color: #788093; font-size: 8px; }
  .hero-chip { position: absolute; z-index: 2; padding: 9px 12px; border: 1px solid rgba(204,214,233,.12); border-radius: 7px; background: #191d27; color: #c1c7d3; font-size: 9px; box-shadow: 0 9px 22px rgba(0,0,0,.22); }
  .hero-chip span:first-child { margin-right: 6px; color: var(--page-accent); }
  .chip-top { top: 28px; right: 3px; }
  .chip-bottom { bottom: 38px; left: 3px; }

  .section-block { width: min(1160px, calc(100% - 64px)); margin: 25px auto 0; padding: 53px 0 25px; border-top: 1px solid var(--line); scroll-margin-top: 25px; }
  .section-heading { display: flex; justify-content: space-between; align-items: flex-end; gap: 20px; margin-bottom: 25px; }
  .section-heading .eyebrow { margin-bottom: 12px; }
  .section-heading h2 { margin: 0 0 8px; font-size: clamp(23px, 3vw, 31px); letter-spacing: -1.15px; }
  .section-description { margin: 0; color: #9299a9; font-size: 11px; line-height: 1.7; }
  .section-count { padding-bottom: 4px; color: var(--page-accent); font-size: 10px; letter-spacing: 1px; }
  .section-count i { padding: 0 4px; color: #666e7f; font-style: normal; }
  .message-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; }
  .message-card { min-height: 136px; display: flex; align-items: flex-start; gap: 15px; padding: 19px; border: 1px solid var(--line); border-radius: 9px; background: linear-gradient(135deg, rgba(255,255,255,.025), transparent 70%), var(--surface); transition: border-color .2s ease, transform .2s ease; }
  .message-card:hover { transform: translateY(-2px); border-color: color-mix(in srgb, var(--page-accent) 35%, transparent); }
  .message-icon { display: grid; flex: 0 0 auto; width: 35px; height: 35px; place-items: center; border-radius: 9px; font-size: 17px; font-weight: 700; }
  .message-icon.blue, .dialog-icon.blue { color: #69a8ff; background: rgba(69,142,255,.13); }
  .message-icon.green { color: #45d7a1; background: rgba(69,215,161,.12); }
  .message-icon.amber, .dialog-icon.amber { color: #f1bd56; background: rgba(241,189,86,.12); }
  .message-icon.red, .dialog-icon.red { color: #ff777d; background: rgba(255,97,108,.12); }
  .message-copy { min-width: 0; }
  .card-overline, .component-label { color: #7e8798; font-size: 8px; letter-spacing: 1.05px; font-weight: 700; }
  .message-copy h3 { margin: 7px 0 5px; font-size: 14px; }
  .message-copy p { margin: 0; color: #9299a9; font-size: 10px; line-height: 1.6; }
  .icon-button { margin-left: auto; border: 0; color: #788194; background: transparent; cursor: pointer; font-size: 15px; }
  .icon-button:hover { color: var(--page-accent); }

  .component-section { padding-top: 52px; }
  .component-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 13px; }
  .demo-card { min-width: 0; padding: 19px; border: 1px solid var(--line); border-radius: 9px; background: var(--surface); }
  .demo-card-heading { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 20px; }
  .demo-card-heading h3 { margin: 6px 0 0; font-size: 14px; }
  .code-chip { padding: 5px 8px; border: 1px solid var(--line); border-radius: 5px; color: #8d96a7; font: 9px ui-monospace, Consolas, monospace; }
  .tab-list { display: flex; gap: 19px; border-bottom: 1px solid var(--line); }
  .tab-list button { position: relative; padding: 0 0 10px; border: 0; color: #8e96a7; background: none; cursor: pointer; font: inherit; font-size: 10px; }
  .tab-list button.active { color: var(--page-accent); }
  .tab-list button.active::after { position: absolute; right: 0; bottom: -1px; left: 0; height: 2px; background: var(--page-accent); content: ""; }
  .tab-panel { display: flex; gap: 12px; min-height: 77px; align-items: center; padding-top: 9px; }
  .panel-icon { display: grid; width: 31px; height: 31px; flex: 0 0 auto; place-items: center; border-radius: 8px; color: var(--page-accent); background: color-mix(in srgb, var(--page-accent) 9%, transparent); }
  .tab-panel b, .setting-description b { font-size: 10px; }
  .tab-panel p { margin: 5px 0 0; color: #9299a9; font-size: 9px; line-height: 1.6; }
  .setting-row { display: flex; align-items: center; gap: 11px; padding: 5px 0 13px; }
  .setting-icon { display: grid; width: 31px; height: 31px; place-items: center; border-radius: 8px; color: #a18bff; background: rgba(161,139,255,.12); }
  .setting-description { display: flex; flex: 1; flex-direction: column; gap: 4px; }
  .setting-description span { color: #9299a9; font-size: 9px; }
  .switch { width: 38px; height: 22px; padding: 3px; border: 1px solid #444a58; border-radius: 20px; background: #303541; cursor: pointer; transition: background .2s ease; }
  .switch span { display: block; width: 14px; height: 14px; border-radius: 50%; background: #bec4d0; transition: transform .2s ease, background .2s ease; }
  .switch.enabled { border-color: var(--page-accent); background: color-mix(in srgb, var(--page-accent) 35%, #20252e); }
  .switch.enabled span { transform: translateX(15px); background: var(--page-accent); }
  .setting-status { padding-top: 11px; border-top: 1px solid var(--line); color: #8e96a6; font-size: 9px; }
  .setting-status > span { display: inline-block; width: 6px; height: 6px; margin-right: 5px; border-radius: 50%; background: #72798a; }
  .setting-status > span.status-on { background: #48d7a1; }
  .progress-label, .progress-footer { display: flex; align-items: center; justify-content: space-between; color: #b5bbc7; font-size: 9px; }
  .progress-label b { color: var(--page-accent); font-size: 10px; }
  .progress-track { height: 7px; margin: 12px 0 11px; overflow: hidden; border-radius: 8px; background: #292e3a; }
  .progress-track span { display: block; height: 100%; border-radius: inherit; background: linear-gradient(90deg, color-mix(in srgb, var(--page-accent) 55%, #5d8aff), var(--page-accent)); transition: width .3s ease; }
  .progress-footer { color: #818a9a; }
  .progress-actions { display: flex; gap: 5px; }
  .progress-actions button { width: 23px; height: 22px; border: 1px solid var(--line); border-radius: 5px; color: #c5cbd6; background: #20242e; cursor: pointer; }
  .progress-actions button:hover { color: var(--page-accent); border-color: color-mix(in srgb, var(--page-accent) 35%, transparent); }
  .faq-list { margin-top: -6px; }
  .faq-item { border-top: 1px solid var(--line); }
  .faq-item button { width: 100%; display: flex; align-items: center; justify-content: space-between; padding: 11px 1px; border: 0; color: #c6cbd5; background: transparent; text-align: left; cursor: pointer; font: inherit; font-size: 10px; }
  .faq-item button span { color: #9299a9; font-size: 15px; transition: transform .2s ease; }
  .faq-item button span.rotated { transform: rotate(180deg); color: var(--page-accent); }
  .faq-item p { margin: -2px 22px 12px 1px; color: #9098a8; font-size: 9px; line-height: 1.7; }

  .form-section { padding-bottom: 47px; }
  .form-layout { display: grid; grid-template-columns: .9fr 1.1fr; gap: 55px; padding: 25px; border: 1px solid var(--line); border-radius: 10px; background: linear-gradient(115deg, rgba(0,255,213,.035), transparent 45%), var(--surface); }
  .form-illustration { position: relative; display: grid; width: 56px; height: 56px; margin-bottom: 17px; place-items: center; border: 1px solid color-mix(in srgb, var(--page-accent) 27%, transparent); border-radius: 14px; color: var(--page-accent); background: color-mix(in srgb, var(--page-accent) 8%, transparent); font-size: 22px; }
  .form-illustration i { position: absolute; top: -5px; right: -7px; color: #f1bd56; font-size: 14px; font-style: normal; }
  .form-illustration b { position: absolute; right: -11px; bottom: -7px; display: grid; width: 21px; height: 21px; place-items: center; border-radius: 50%; color: #10131a; background: #f1bd56; font-size: 10px; }
  .form-intro h3 { max-width: 300px; margin-bottom: 9px; font-size: 20px; line-height: 1.3; letter-spacing: -.5px; }
  .form-intro > p { max-width: 325px; margin-bottom: 20px; color: #9299a9; font-size: 10px; line-height: 1.8; }
  .privacy-note { color: #848d9d; font-size: 9px; }
  .privacy-note span { margin-right: 6px; color: var(--page-accent); }
  .contact-form { display: flex; flex-direction: column; }
  .contact-form label { margin: 0 0 7px; color: #c3c9d4; font-size: 10px; font-weight: 600; }
  .contact-form label span { color: #ff777d; }
  .contact-form input { width: 100%; height: 39px; margin-bottom: 15px; padding: 0 11px; border: 1px solid rgba(195,205,226,.14); border-radius: 6px; outline: none; color: var(--ink); background: #0e1118; font: inherit; font-size: 10px; }
  .contact-form input::placeholder { color: #677082; }
  .contact-form input:focus { border-color: color-mix(in srgb, var(--page-accent) 60%, transparent); box-shadow: 0 0 0 3px color-mix(in srgb, var(--page-accent) 10%, transparent); }
  .submit-button { align-self: flex-start; margin-top: 2px; }
  .form-feedback { margin: 12px 0 0; color: #54d9a8; font-size: 10px; line-height: 1.6; }

  .closing-banner { width: min(1160px, calc(100% - 64px)); min-height: 128px; margin: 25px auto 0; padding: 23px 29px; display: flex; align-items: center; gap: 18px; border: 1px solid color-mix(in srgb, var(--page-accent) 20%, transparent); border-radius: 10px; background: radial-gradient(ellipse at 0% 50%, color-mix(in srgb, var(--page-accent) 12%, transparent), transparent 55%), #141923; }
  .closing-spark { display: grid; width: 38px; height: 38px; flex: 0 0 auto; place-items: center; border-radius: 10px; color: var(--page-accent); background: color-mix(in srgb, var(--page-accent) 10%, transparent); font-size: 19px; }
  .closing-banner .eyebrow { margin-bottom: 7px; }
  .closing-banner h2 { margin: 0; font-size: clamp(16px, 2.4vw, 22px); letter-spacing: -.6px; }
  .button-light { display: inline-flex; align-items: center; gap: 12px; margin-left: auto; color: #10131a; background: #f1f3f6; white-space: nowrap; }
  .page-footer { min-height: 93px; margin-top: 15px; border-top: 1px solid var(--line); }
  .footer-brand { font-size: 12px; }
  .footer-brand .window-mark { width: 17px; height: 17px; gap: 2px; }
  .page-footer > span { color: #778092; font-size: 9px; }

  .modal-layer { position: fixed; z-index: 20; inset: 0; display: grid; place-items: center; padding: 20px; background: rgba(4,6,10,.72); backdrop-filter: blur(7px); }
  .message-dialog { position: relative; margin: 0; width: min(410px, 100%); max-width: 100%; padding: 0; overflow: hidden; border: 1px solid rgba(205,215,233,.2); border-radius: 10px; color: var(--ink); background: #191d26; box-shadow: 0 25px 90px rgba(0,0,0,.55); animation: dialog-in .18s ease-out; }
  @keyframes dialog-in { from { opacity: 0; transform: translateY(8px) scale(.98); } to { opacity: 1; transform: translateY(0) scale(1); } }
  .dialog-titlebar { height: 43px; display: flex; align-items: center; justify-content: space-between; padding: 0 14px; border-bottom: 1px solid var(--line); color: #c7cdd8; font-size: 10px; }
  .dialog-close { width: 26px; height: 26px; border: 0; border-radius: 5px; color: #9299a9; background: transparent; cursor: pointer; font-size: 18px; }
  .dialog-close:hover { color: #fff; background: rgba(255,255,255,.08); }
  .dialog-body { display: flex; align-items: center; gap: 15px; min-height: 116px; padding: 22px; }
  .dialog-body p { margin: 0; color: #c2c8d3; font-size: 12px; line-height: 1.75; }
  .dialog-actions { display: flex; justify-content: flex-end; gap: 9px; padding: 12px 17px; border-top: 1px solid var(--line); background: rgba(0,0,0,.09); }
  .dialog-actions .button { min-height: 34px; }
  .button-quiet { border: 1px solid rgba(195,205,226,.15); color: #bdc4d1; background: #242934; }
  .toast-message { position: fixed; z-index: 30; right: 25px; bottom: 24px; display: flex; align-items: center; gap: 10px; min-width: 240px; max-width: calc(100% - 32px); padding: 12px 13px; border: 1px solid rgba(204,214,233,.15); border-radius: 8px; color: #e3e7ed; background: #202630; box-shadow: 0 12px 35px rgba(0,0,0,.35); font-size: 10px; animation: dialog-in .2s ease-out; }
  .toast-check { display: grid; width: 21px; height: 21px; place-items: center; border-radius: 50%; color: #45d7a1; background: rgba(69,215,161,.12); }
  .toast-message button { margin-left: auto; border: 0; color: #9da5b3; background: transparent; cursor: pointer; font-size: 16px; }

  @media (max-width: 760px) {
    .topbar, .page-footer, .hero, .section-block, .closing-banner { width: min(100% - 36px, 560px); }
    .topbar { height: 66px; }
    .top-nav { gap: 14px; }
    .top-nav a { font-size: 10px; }
    .version-pill { display: none; }
    .hero { grid-template-columns: 1fr; gap: 0; padding-top: 24px; }
    .hero-copy { padding: 30px 0 6px; }
    .hero-visual { min-height: 330px; margin: 4px 0 28px; }
    .preview-window { width: min(440px, calc(100% - 24px)); }
    .chip-top { right: -2px; }
    .chip-bottom { left: 0; }
    .floating-notice { right: -4px; }
    .section-block { padding-top: 38px; }
    .form-layout { gap: 28px; padding: 20px; }
    .closing-banner { padding: 20px; }
    .page-footer { gap: 14px; }
    .page-footer > span { display: none; }
  }
  @media (max-width: 520px) {
    .topbar, .page-footer, .hero, .section-block, .closing-banner { width: calc(100% - 32px); }
    .top-nav { gap: 11px; }
    .top-nav a { font-size: 9px; }
    .brand { gap: 8px; font-size: 12px; }
    .window-mark { width: 18px; height: 18px; gap: 2px; }
    .hero h1 { font-size: 43px; letter-spacing: -2.4px; }
    .hero-meta { gap: 11px; font-size: 9px; }
    .hero-visual { min-height: 310px; }
    .preview-content { padding: 21px 15px; }
    .floating-notice { min-width: 220px; }
    .section-heading { align-items: flex-start; }
    .section-count { padding-top: 4px; white-space: nowrap; }
    .message-grid, .component-grid, .form-layout { grid-template-columns: 1fr; }
    .message-card { min-height: auto; }
    .form-layout { gap: 22px; padding: 18px; }
    .closing-banner { flex-wrap: wrap; gap: 12px; }
    .closing-banner > div:nth-child(2) { flex: 1; }
    .button-light { width: 100%; justify-content: center; margin: 4px 0 0; }
    .page-footer { min-height: 75px; }
    .back-top { font-size: 9px; }
  }
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { scroll-behavior: auto !important; animation-duration: .01ms !important; animation-iteration-count: 1 !important; transition-duration: .01ms !important; }
  }
</style>
