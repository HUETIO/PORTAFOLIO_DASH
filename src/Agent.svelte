<script>
  import { onMount, tick } from "svelte";
  import { services } from "./services.js";
  import { chatWithGemini } from "./geminis.js";

  const providerName = "CapibaraNeitor";
  const maxChatMessages = 6;
  const maxChatCharacters = 2900;
  const recaptchaSiteKey =
    import.meta.env.VITE_RECAPTCHA_ENTERPRISE_CHECKBOX_SITE_KEY;
  const salesRequestUrl =
    import.meta.env.VITE_SALES_REQUEST_URL || "/api/sales-request";

  let showAgent = false;
  let isFooter = false;
  let isRoutedPage = false;
  let isSending = false;
  let captchaReady = false;
  let captchaToken = "";
  let captchaContainer;
  let captchaWidgetId;
  let captchaStatus = recaptchaSiteKey ? "loading" : "unconfigured";
  let formError = "";
  let successMessage = "";
  let intakeStep = 0;
  let intakeService = "";
  let intakeNeed = "";
  let showSalesForm = false;
  let chatMessages = [];
  let chatDraft = "";
  let chatError = "";
  let isChatting = false;
  let form = {
    name: "",
    email: "",
    phone: "",
    service: "",
    message: "",
    website: "",
    consent: false,
  };

  $: customerMessages = chatMessages.filter((message) => message.role === "user");
  $: chatCharactersUsed = customerMessages.reduce(
    (total, message) => total + message.text.length,
    0,
  );
  $: chatCharactersRemaining = Math.max(0, maxChatCharacters - chatCharactersUsed);
  $: chatMessagesRemaining = Math.max(0, maxChatMessages - customerMessages.length);

  function syncChatTranscript(messages = chatMessages) {
    form.message = messages
      .filter((message) => message.role === "user")
      .map((message) => message.text)
      .join("\n\n");
  }

  function updatePlacement() {
    isRoutedPage = window.location.hash.startsWith("#/");
    isFooter = window.scrollY > 220 || isRoutedPage;
  }

  function initializeCaptcha() {
    if (!recaptchaSiteKey || captchaReady) return;

    const markCaptchaReady = () => {
      const enterprise = window.grecaptcha?.enterprise;
      if (!enterprise?.ready) {
        captchaStatus = "error";
        return;
      }

      enterprise.ready(() => {
        if (!window.grecaptcha?.enterprise?.render) {
          captchaStatus = "error";
          return;
        }

        captchaReady = true;
        captchaStatus = "ready";
        renderCaptcha();
      });
    };

    if (window.grecaptcha?.enterprise?.ready) {
      markCaptchaReady();
      return;
    }

    const existingScript = document.querySelector(
      'script[src^="https://www.google.com/recaptcha/enterprise.js"]',
    );
    if (existingScript) {
      existingScript.addEventListener("load", markCaptchaReady, { once: true });
      existingScript.addEventListener(
        "error",
        () => (captchaStatus = "error"),
        { once: true },
      );
      return;
    }

    const script = document.createElement("script");
    script.src = "https://www.google.com/recaptcha/enterprise.js?render=explicit&hl=es";
    script.async = true;
    script.defer = true;
    script.onload = markCaptchaReady;
    script.onerror = () => (captchaStatus = "error");
    document.head.appendChild(script);
  }

  function renderCaptcha() {
    if (
      !captchaReady ||
      !captchaContainer ||
      captchaWidgetId !== undefined ||
      !window.grecaptcha?.enterprise
    ) {
      return;
    }

    window.grecaptcha.enterprise.ready(() => {
      if (!captchaContainer || captchaWidgetId !== undefined) return;

      try {
        captchaWidgetId = window.grecaptcha.enterprise.render(captchaContainer, {
          sitekey: recaptchaSiteKey,
          action: "SALES_REQUEST",
          callback: (token) => {
            captchaToken = token;
            formError = "";
          },
          "expired-callback": () => {
            captchaToken = "";
          },
          "error-callback": () => {
            captchaToken = "";
            captchaStatus = "error";
            formError = "No se pudo completar reCAPTCHA. Revisa tu conexión e inténtalo nuevamente.";
          },
        });
      } catch (error) {
        console.error("No se pudo mostrar el widget reCAPTCHA Enterprise.", error);
        captchaStatus = "error";
      }
    });
  }

  function resetCaptcha() {
    captchaToken = "";
    if (captchaWidgetId !== undefined && window.grecaptcha?.enterprise) {
      window.grecaptcha.enterprise.reset(captchaWidgetId);
    }
  }

  async function toggleAgent() {
    showAgent = !showAgent;
    if (showAgent) {
      await tick();
      initializeCaptcha();
    }
  }

  async function openAgent() {
    showAgent = true;
    await tick();
    initializeCaptcha();
  }

  async function continueIntake() {
    if (intakeStep === 0) {
      if (!intakeService) return;
      intakeStep = 1;
      return;
    }

    const need = intakeNeed.trim();
    if (!need || !form.consent) return;

    form.service = intakeService;
    chatMessages = [{ role: "user", text: need }];
    syncChatTranscript(chatMessages);
    showSalesForm = true;
    await tick();
    renderCaptcha();
    await requestChatReply();
  }

  async function requestChatReply() {
    if (isChatting) return;
    isChatting = true;
    chatError = "";

    try {
      const contents = chatMessages.map((message) => ({
        role: message.role,
        parts: [{ text: message.text }],
      }));
      const reply = await chatWithGemini(contents);
      chatMessages = [...chatMessages, { role: "model", text: reply }];
    } catch (error) {
      console.error("Error en el chat de orientación tecnológica", error);
      chatError =
        error instanceof Error && error.message
          ? error.message
          : "No se pudo obtener una respuesta. Intenta de nuevo.";
    } finally {
      isChatting = false;
    }
  }

  async function sendChatMessage() {
    const text = chatDraft.trim();
    if (
      !text ||
      isChatting ||
      chatError ||
      chatMessagesRemaining === 0 ||
      text.length > chatCharactersRemaining
    ) {
      return;
    }

    chatMessages = [...chatMessages, { role: "user", text }];
    chatDraft = "";
    syncChatTranscript(chatMessages);
    await requestChatReply();
  }

  async function retryChatReply() {
    if (!chatError || isChatting) return;
    await requestChatReply();
  }

  function goBack() {
    if (showSalesForm) {
      intakeService = form.service;
      intakeNeed = customerMessages[0]?.text ?? intakeNeed;
      intakeStep = 1;
      showSalesForm = false;
      chatMessages = [];
      chatDraft = "";
      chatError = "";
      captchaContainer = undefined;
      captchaWidgetId = undefined;
      captchaToken = "";
      return;
    }

    if (intakeStep === 1) intakeStep = 0;
  }

  onMount(() => {
    updatePlacement();
    window.addEventListener("scroll", updatePlacement, { passive: true });
    window.addEventListener("hashchange", updatePlacement);
    window.addEventListener("open-contact-agent", openAgent);

    return () => {
      window.removeEventListener("scroll", updatePlacement);
      window.removeEventListener("hashchange", updatePlacement);
      window.removeEventListener("open-contact-agent", openAgent);
    };
  });

  async function submitRequest() {
    if (isSending) return;
    formError = "";
    successMessage = "";

    if (form.website.trim()) {
      formError = "No se pudo validar la solicitud. Intenta nuevamente.";
      return;
    }
    if (!recaptchaSiteKey || !captchaReady) {
      formError = "La verificación anti-bots no está disponible. Intenta más tarde.";
      return;
    }
    if (!captchaToken) {
      formError = "Marca la casilla reCAPTCHA antes de enviar la solicitud.";
      return;
    }

    const selectedService = services.find(
      (service) => service.title === form.service,
    );
    if (!selectedService) {
      formError = "Selecciona un servicio del catálogo.";
      return;
    }

    isSending = true;
    try {
      const recaptchaToken = captchaToken;
      captchaToken = "";
      const response = await fetch(salesRequestUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name: form.name.trim(),
          email: form.email.trim(),
          phone: form.phone.trim(),
          service: selectedService.title,
          message: form.message.trim(),
          website: form.website.trim(),
          consent: form.consent,
          recaptchaToken,
        }),
      });
      const result = await response.json().catch(() => ({}));
      if (!response.ok) {
        throw new Error(result.error || `El servidor respondió ${response.status}.`);
      }

      form = {
        name: "",
        email: "",
        phone: "",
        service: "",
        message: "",
        website: "",
        consent: false,
      };
      chatMessages = [];
      chatDraft = "";
      successMessage =
        "Solicitud enviada. CapibaraNeitor te contactará para conversar sobre el servicio; esto no confirma una venta ni un precio.";
    } catch (error) {
      console.error("Error al enviar la solicitud comercial", error);
      resetCaptcha();
      formError =
        error instanceof Error && error.message
          ? error.message
          : "No se pudo enviar la solicitud. Intenta nuevamente.";
    } finally {
      isSending = false;
    }
  }
</script>

<div
  class="agent-launcher-slot"
  class:agent-launcher-slot--route={isRoutedPage}
>
  <svelte:element
    this={isFooter ? "footer" : "div"}
    class={`agent-launcher-region ${isFooter ? "agent-launcher-region--footer" : ""}`}
    aria-label={isFooter ? "Asistente comercial" : undefined}
  >
    {#if isFooter}
      <span class="agent-footer-label">¿Necesitas ayuda?</span>
    {/if}
    <button
      type="button"
      class="agent-launcher"
      aria-expanded={showAgent}
      aria-controls="agent-chat"
      on:click={toggleAgent}
    >
      <svg viewBox="0 0 100 50" preserveAspectRatio="none" aria-hidden="true">
        <path
          d="M25,2 C11,2 2,12 2,25 C2,38 12,48 27,48 H73 C88,48 98,38 98,25 C98,12 88,2 73,2 Z"
        />
      </svg>
      <span class="agent-launcher-text">
        {isFooter ? "Habla con DASH.IO" : "¿Cómo puede ayudarte DASH.IO? 🦖"}
      </span>
    </button>
  </svelte:element>
</div>

<section
  id="agent-chat"
  class="agent-modal"
  class:agent-modal--hidden={!showAgent}
  aria-label={`Asistente comercial ${providerName}`}
  aria-hidden={!showAgent}
>
  <div class="agent_ui">
    <h2>Hola, soy {providerName}</h2>
    <p class="agent-intro">
      Cuéntanos qué quieres mejorar. DASH.IO te ayudará a encontrar una solución tecnológica para que tu empresa avance.
    </p>

    {#if successMessage}
      <div class="form-notice success" role="status">{successMessage}</div>
    {:else if !showSalesForm}
      <form class="intake-form" on:submit|preventDefault={continueIntake}>
        {#if intakeStep === 0}
          <label for="intake-service">1 de 2: ¿Qué servicio de DASH.IO te interesa?</label>
          <select id="intake-service" bind:value={intakeService} required>
            <option value="" disabled>Selecciona un servicio</option>
            {#each services as service}
              <option value={service.title}>{service.title}</option>
            {/each}
          </select>
          <div class="intake-actions">
            <button class="submit-request" type="submit" disabled={!intakeService}>
              Adelante
            </button>
          </div>
        {:else}
          <label for="intake-need">2 de 2: ¿Qué necesitas resolver o mejorar con ese servicio?</label>
          <textarea
            id="intake-need"
            bind:value={intakeNeed}
            maxlength="500"
            rows="3"
            placeholder="Escribe tu consulta tecnológica inicial."
            required
          ></textarea>
          <div class="privacy-summary">
            <p>
              Al continuar, tu mensaje se enviará a Google Gemini para generar respuestas. Si luego
              envías la solicitud, tus mensajes y datos de contacto se enviarán a DASH.IO por correo.
              No incluyas contraseñas, datos de pago ni información confidencial.
            </p>
          </div>
          <label class="consent-row">
            <input bind:checked={form.consent} type="checkbox" required />
            <span>
              Acepto que mi mensaje se procese con IA y, si envío la solicitud, que mis datos se usen
              para responder a esta consulta comercial.
            </span>
          </label>
          <div class="intake-actions">
            <button class="back-button" type="button" on:click={goBack}>Atrás</button>
            <button
              class="submit-request"
              type="submit"
              disabled={!intakeNeed.trim() || !form.consent}
            >
              Adelante
            </button>
          </div>
        {/if}
      </form>
    {:else}
      <form class="sales-form" on:submit|preventDefault={submitRequest}>
        <button class="back-button" type="button" on:click={goBack}>Atrás</button>

        <label for="sales-service">Servicio de interés <span aria-hidden="true">*</span></label>
        <select id="sales-service" bind:value={form.service} required>
          <option value="" disabled>Selecciona un servicio</option>
          {#each services as service}
            <option value={service.title}>{service.title}</option>
          {/each}
        </select>

        <label for="sales-name">Nombre <span aria-hidden="true">*</span></label>
        <input
          id="sales-name"
          bind:value={form.name}
          name="customer_name"
          type="text"
          autocomplete="name"
          minlength="2"
          maxlength="120"
          required
        />

        <label for="sales-email">Correo electrónico <span aria-hidden="true">*</span></label>
        <input
          id="sales-email"
          bind:value={form.email}
          name="customer_email"
          type="email"
          autocomplete="email"
          maxlength="254"
          required
        />

        <label for="sales-phone">Teléfono <span aria-hidden="true">*</span></label>
        <input
          id="sales-phone"
          bind:value={form.phone}
          name="customer_phone"
          type="tel"
          autocomplete="tel"
          minlength="7"
          maxlength="24"
          pattern="(?:[+0-9.]|\(|\)| |-){7,24}"
          title="Usa de 7 a 24 caracteres: números, espacios, +, paréntesis, puntos o guiones."
          required
        />

        <fieldset class="chat-field">
          <legend>Conversemos sobre tu necesidad</legend>
          <div
            class="chat-transcript"
            role="log"
            aria-live="polite"
            aria-label="Conversación con CapibaraNeitor"
          >
            <div class="chat-bubble assistant">
              Hola, soy {providerName}. Puedo orientarte sobre tecnología. ¿Qué te gustaría resolver?
            </div>
            {#each chatMessages as message}
              <div class={`chat-bubble ${message.role === "user" ? "customer" : "assistant"}`}>
                {message.text}
              </div>
            {/each}
            {#if isChatting}
              <div class="chat-bubble assistant" role="status">CapibaraNeitor está escribiendo…</div>
            {/if}
          </div>
          {#if chatError}
            <p class="form-notice error" role="alert">{chatError}</p>
            <button
              class="chat-retry"
              type="button"
              on:click={retryChatReply}
              disabled={isChatting}
            >
              Reintentar respuesta
            </button>
          {/if}
          <label for="sales-chat-message">Tu mensaje</label>
          <div class="chat-compose">
            <textarea
              id="sales-chat-message"
              bind:value={chatDraft}
              maxlength={Math.min(500, chatCharactersRemaining)}
              rows="2"
              placeholder="Escribe una pregunta sobre tecnología…"
              disabled={isChatting || chatMessagesRemaining === 0 || chatCharactersRemaining === 0}
              on:keydown={(event) => {
                if (event.key === "Enter" && !event.shiftKey) {
                  event.preventDefault();
                  sendChatMessage();
                }
              }}
            ></textarea>
            <button
              class="submit-request chat-send"
              type="button"
              on:click={sendChatMessage}
              disabled={
                !chatDraft.trim() ||
                isChatting ||
                Boolean(chatError) ||
                chatMessagesRemaining === 0 ||
                chatDraft.trim().length > chatCharactersRemaining
              }
            >
              Enviar
            </button>
          </div>
          <p class="chat-limit">
            {chatMessagesRemaining} mensajes disponibles · {chatCharactersRemaining} caracteres restantes.
            No compartas información confidencial.
          </p>
        </fieldset>

        <div class="privacy-summary">
          <strong>Antes de enviar</strong>
          <p>
            Al enviar este formulario, se enviarán a capibaraneitor@gmail.com tu nombre, correo,
            teléfono, servicio elegido y los mensajes que escribiste en el chat.
          </p>
        </div>

        <div class="captcha-area">
          {#if captchaStatus === "unconfigured"}
            <p class="setup-note">
              Falta configurar VITE_RECAPTCHA_ENTERPRISE_CHECKBOX_SITE_KEY.
            </p>
          {:else if captchaStatus === "loading"}
            <p class="setup-note">Preparando verificación anti-bots…</p>
          {:else if captchaStatus === "error"}
            <p class="setup-note" role="alert">
              No se pudo mostrar reCAPTCHA Enterprise. Revisa que la clave sea de tipo checkbox,
              que el dominio esté autorizado y que Google no esté bloqueado por la red.
            </p>
          {:else}
            <div class="captcha-widget" bind:this={captchaContainer}></div>
          {/if}
        </div>

        <label class="honeypot" aria-hidden="true">
          No rellenar
          <input
            bind:value={form.website}
            name="website"
            type="text"
            tabindex="-1"
            autocomplete="off"
          />
        </label>

        {#if formError}
          <p class="form-notice error" role="alert">{formError}</p>
        {/if}

        <button
          class="submit-request"
          type="submit"
          disabled={isSending || isChatting || !recaptchaSiteKey || !captchaReady || !captchaToken}
        >
          {isSending ? "Enviando…" : "Enviar solicitud"}
        </button>
      </form>
    {/if}

    <p class="provider-label">Gestión comercial por: {providerName}</p>
    <button class="close-agent" type="button" on:click={toggleAgent}>Cerrar</button>
  </div>
</section>

<style>
  .agent-launcher-slot {
    height: 0;
  }

  .agent-launcher-region:not(.agent-launcher-region--footer) {
    display: none;
  }

  .agent-launcher-slot--route {
    height: 0;
  }

  .agent-launcher-region {
    position: relative;
    z-index: 2000;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 150px;
  }

  .agent-launcher-region--footer {
    position: fixed;
    inset: auto 0 0;
    width: 100%;
    justify-content: flex-end;
    gap: 1rem;
    height: auto;
    min-height: 76px;
    padding: 0.65rem clamp(1rem, 4vw, 2rem);
    border-top: 1px solid rgba(0, 245, 212, 0.28);
    background: rgba(8, 13, 24, 0.94);
    box-shadow: 0 -8px 28px rgba(0, 0, 0, 0.28);
    backdrop-filter: blur(14px);
    margin: 0;
    text-align: left;
    pointer-events: none;
  }

  .agent-launcher-region--footer .agent-launcher {
    pointer-events: auto;
  }

  .agent-footer-label {
    color: #e2e8f0;
    font-size: 0.95rem;
  }

  .agent-launcher {
    position: relative;
    isolation: isolate;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 240px;
    min-height: 68px;
    padding: 0.75rem 1rem;
    overflow: hidden;
    border: 0;
    border-radius: 20px;
    background: transparent;
    box-shadow: none;
    color: #fff;
    cursor: pointer;
    transition: transform 0.25s ease, filter 0.25s ease;
  }

  .agent-launcher:hover {
    transform: translateY(-3px) scale(1.02);
    filter: drop-shadow(0 0 14px rgba(0, 255, 213, 0.45));
  }

  .agent-launcher:active {
    transform: scale(0.98);
  }

  .agent-launcher:focus-visible {
    outline: 2px solid #00f5d4;
    outline-offset: 4px;
  }

  .agent-launcher svg {
    position: absolute;
    inset: 0;
    z-index: -1;
    width: 100%;
    height: 100%;
    overflow: visible;
    filter: drop-shadow(0 4px 12px rgba(0, 0, 0, 0.35));
  }

  .agent-launcher path {
    fill: #00cdb4;
    transform-box: fill-box;
    transform-origin: center;
    animation: agent-liquid 3s ease-in-out infinite alternate;
  }

  .agent-launcher-text {
    position: relative;
    z-index: 1;
    font-size: 0.9rem;
    font-weight: 700;
    letter-spacing: 0.02em;
    text-align: center;
    text-shadow: 0 1px 5px rgba(0, 0, 0, 0.75);
    white-space: nowrap;
    pointer-events: none;
  }

  .agent-modal {
    position: fixed;
    right: 24px;
    bottom: 96px;
    z-index: 2100;
    width: min(440px, calc(100vw - 32px));
    max-height: min(80vh, 760px);
    padding: 20px;
    overflow-y: auto;
    border: 1px solid rgba(0, 245, 212, 0.22);
    border-radius: 16px;
    background: #111827;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.45);
    color: #fff;
  }

  .agent-modal--hidden {
    display: none;
  }

  .agent-modal h2 {
    margin: 0 0 0.5rem;
    font-size: 1.1rem;
  }

  .agent-intro,
  .privacy-summary p,
  .setup-note {
    color: #cbd5e1;
    font-size: 0.86rem;
    line-height: 1.45;
  }

  .agent-intro {
    margin: 0 0 1rem;
  }

  .sales-form {
    display: grid;
    gap: 0.45rem;
  }

  .intake-form {
    display: grid;
    gap: 0.7rem;
  }

  .intake-actions {
    display: flex;
    gap: 0.6rem;
  }

  .intake-actions .submit-request {
    flex: 1;
  }

  .back-button {
    justify-self: start;
    border: 1px solid #64748b;
    border-radius: 8px;
    padding: 0.7rem 1rem;
    background: #1f2937;
    color: #e2e8f0;
    font: inherit;
    font-weight: 650;
    cursor: pointer;
  }

  .back-button:hover {
    border-color: #00f5d4;
    color: #fff;
  }

  .intake-form label {
    font-size: 0.9rem;
    font-weight: 650;
  }

  .intake-form select,
  .intake-form textarea {
    width: 100%;
    min-width: 0;
    padding: 0.65rem 0.75rem;
    border: 1px solid #475569;
    border-radius: 8px;
    background: #1f2937;
    color: #fff;
    font: inherit;
  }

  .intake-form select:focus-visible,
  .intake-form textarea:focus-visible {
    outline: 2px solid #00f5d4;
    outline-offset: 2px;
  }

  .sales-form > label:not(.consent-row, .honeypot) {
    margin-top: 0.35rem;
    font-size: 0.88rem;
    font-weight: 650;
  }

  .sales-form select,
  .sales-form input:not([type="checkbox"]),
  .sales-form textarea {
    width: 100%;
    min-width: 0;
    padding: 0.65rem 0.75rem;
    border: 1px solid #475569;
    border-radius: 8px;
    background: #1f2937;
    color: #fff;
    font: inherit;
  }

  .sales-form select:focus-visible,
  .sales-form input:focus-visible,
  .sales-form textarea:focus-visible {
    outline: 2px solid #00f5d4;
    outline-offset: 2px;
  }

  .sales-form textarea {
    resize: vertical;
  }

  .chat-field {
    display: grid;
    gap: 0.55rem;
    min-width: 0;
    margin: 0.6rem 0 0;
    padding: 0;
    border: 0;
  }

  .chat-field legend,
  .chat-field > label {
    font-size: 0.88rem;
    font-weight: 650;
  }

  .chat-transcript {
    display: grid;
    gap: 0.6rem;
    max-height: 220px;
    min-height: 120px;
    overflow-y: auto;
    padding: 0.75rem;
    border: 1px solid #334155;
    border-radius: 10px;
    background: #0b1220;
  }

  .chat-bubble {
    max-width: 90%;
    padding: 0.6rem 0.75rem;
    border-radius: 12px;
    font-size: 0.84rem;
    line-height: 1.45;
    overflow-wrap: anywhere;
    white-space: pre-wrap;
  }

  .chat-bubble.assistant {
    justify-self: start;
    border: 1px solid #334155;
    background: #1f2937;
    color: #e2e8f0;
  }

  .chat-bubble.customer {
    justify-self: end;
    background: #075e57;
    color: #fff;
  }

  .chat-compose {
    display: flex;
    align-items: stretch;
    gap: 0.5rem;
  }

  .chat-compose textarea {
    flex: 1;
    min-height: 58px;
    resize: vertical;
  }

  .chat-compose .chat-send {
    align-self: end;
    flex: 0 0 auto;
    padding-inline: 0.8rem;
  }

  .chat-limit {
    color: #94a3b8;
    font-size: 0.73rem;
    line-height: 1.4;
  }

  .chat-retry {
    justify-self: start;
    border: 1px solid #64748b;
    border-radius: 8px;
    padding: 0.55rem 0.75rem;
    background: #1f2937;
    color: #e2e8f0;
    font: inherit;
    font-size: 0.82rem;
    cursor: pointer;
  }

  .optional {
    color: #94a3b8;
    font-weight: 400;
  }

  .privacy-summary {
    margin-top: 0.6rem;
    padding: 0.75rem;
    border: 1px solid rgba(0, 245, 212, 0.24);
    border-radius: 8px;
    background: rgba(0, 245, 212, 0.06);
  }

  .privacy-summary p {
    margin: 0.3rem 0 0;
  }

  .consent-row {
    display: flex;
    align-items: flex-start;
    gap: 0.55rem;
    margin: 0.45rem 0;
    font-size: 0.82rem;
    line-height: 1.4;
  }

  .consent-row input {
    flex: 0 0 auto;
    margin-top: 0.18rem;
    accent-color: #00cdb4;
  }

  .captcha-area {
    min-height: 78px;
    overflow-x: auto;
  }

  .captcha-widget {
    min-height: 78px;
  }

  .setup-note {
    margin: 0.2rem 0 0.5rem;
  }

  .form-notice {
    margin: 0.35rem 0;
    padding: 0.7rem;
    border-radius: 8px;
    font-size: 0.88rem;
    line-height: 1.45;
  }

  .form-notice.error {
    background: #7f1d1d;
    color: #fff;
  }

  .form-notice.success {
    background: #064e3b;
    color: #d1fae5;
  }

  .submit-request,
  .close-agent {
    border: 0;
    border-radius: 8px;
    padding: 0.7rem 1rem;
    background: #00ffd5;
    color: #111;
    font-weight: 700;
    cursor: pointer;
  }

  .submit-request:disabled {
    background: #64748b;
    color: #e2e8f0;
    cursor: not-allowed;
  }

  .honeypot {
    position: absolute;
    left: -10000px;
    width: 1px;
    height: 1px;
    overflow: hidden;
  }

  .provider-label {
    margin: 0.8rem 0 0;
    color: #94a3b8;
    font-size: 0.76rem;
    text-align: right;
  }

  .close-agent {
    margin-top: 0.7rem;
    background: #333;
    color: #fff;
  }

  .close-agent:hover {
    background: #00ffd5;
    color: #111;
  }

  @keyframes agent-liquid {
    from { transform: scaleX(1) scaleY(1); }
    to { transform: scaleX(1.04) scaleY(0.95); }
  }

  @media (max-width: 600px) {
    .agent-launcher-region--footer {
      min-height: 68px;
      gap: 0.5rem;
      padding: 0.5rem 0.75rem;
    }

    .agent-footer-label {
      font-size: 0.82rem;
    }

    .agent-launcher {
      width: 205px;
      min-height: 58px;
    }

    .agent-launcher-text {
      font-size: 0.82rem;
    }

    .agent-modal {
      right: 8px;
      bottom: 82px;
      width: calc(100vw - 16px);
      max-height: calc(100vh - 100px);
      padding: 16px;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .agent-launcher path {
      animation: none;
    }
  }
</style>
