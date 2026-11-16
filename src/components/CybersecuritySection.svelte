<script>
  let selectedBadge = null;
  let closeButton;
  let dialog;
  let previouslyFocusedElement;
  let imageLoadError = false;

  const skillBadges = [
    {
      id: "23539362",
      imageUrl: "https://cdn.qwiklabs.com/%2BoWdm%2FHzI%2FCAdbH%2BVisNVqZNrjaLwl24mARfInT99b0%3D",
    },
    {
      id: "23506116",
      imageUrl: "https://cdn.qwiklabs.com/8WAx69Kk1nJNoipzoi0vmesqTSEsQlKcbiSUJW0VeOA%3D",
    },
    {
      id: "24604339",
      imageUrl: "https://cdn.qwiklabs.com/cjGVnoF%2FOdfhTVoDqKjUZhwt7oXFDcBmdki6VS4jkUk%3D",
    },
    {
      id: "24553259",
      imageUrl: "https://cdn.qwiklabs.com/0i6utW3BHaH3%2Bpf5bJCyVH995qWC1%2FkBnKm64cZfoi0%3D",
    },
    {
      id: "24451110",
      imageUrl: "https://cdn.qwiklabs.com/k9QPlamtqAYqyBDn0hIOWr%2BBoJxznnibFblS%2Fsn%2Fgns%3D",
    },
    {
      id: "24451029",
      imageUrl: "https://cdn.qwiklabs.com/WcxbS5GLopt%2F0kDlgb7FWMWOdxrYl6Ozw8q4c4JCfLU%3D",
    },
    {
      id: "24416858",
      imageUrl: "https://cdn.qwiklabs.com/7AR8jskbY0fbmBzYu1XE6vWn1mkrCoakx%2FDRhQrKLFs%3D",
    },
    {
      id: "23541833",
      imageUrl: "https://cdn.qwiklabs.com/BVV%2Fj%2F0h1ZRwMel0M0Ip3uZcNXd%2FzeWEqkZLZ2umN3E%3D",
    },
    {
      id: "23540147",
      imageUrl: "https://cdn.qwiklabs.com/5gTJ1A69jkF3DqOrP4CNZcgB2219G46Tz2zx741LFFc%3D",
    },
    {
      id: "23524487",
      imageUrl: "https://cdn.qwiklabs.com/ydX8SIVF3NS1pN246f9PtJjGf5EmnyrlnQMNYJ9X0zQ%3D",
    },
  ].map((badge) => ({
    ...badge,
    label: "Insignia de aprendizaje Google Skills",
    url: `https://www.skills.google/public_profiles/efb60a19-0e77-4cea-ace6-363bc02e924c/badges/${badge.id}`,
  }));

  function openBadge(badge, event) {
    selectedBadge = badge;
    imageLoadError = false;
    previouslyFocusedElement = event.currentTarget;
    requestAnimationFrame(() => closeButton?.focus());
  }

  function closeBadge() {
    selectedBadge = null;
    imageLoadError = false;
    requestAnimationFrame(() => previouslyFocusedElement?.focus());
  }

  function handleDialogKeydown(event) {
    if (event.key === "Escape") {
      event.preventDefault();
      closeBadge();
      return;
    }

    if (event.key === "Tab" && dialog) {
      const focusable = [...dialog.querySelectorAll("button:not([disabled]), a[href]")];
      if (!focusable.length) return;

      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }
  }
</script>

<section class="cybersecurity" aria-labelledby="cybersecurity-title">
  <div class="cybersecurity-inner">
    <div class="intro">
      <p class="eyebrow">APRENDIZAJE CONTINUO</p>
      <h2 id="cybersecurity-title">La seguridad digital evoluciona. Nosotros también.</h2>
      <p class="lead">
        En DASH.IO, aprender sobre seguridad es parte de crear soluciones tecnológicas con criterio y atención a cada detalle.
      </p>
    </div>

    <div class="credentials">
      <span class="credential-mark" aria-hidden="true">✓</span>
      <p>
        <strong>Aprendizaje constante en Google Skills</strong>
        Explora las insignias que inspiran una visión responsable de la tecnología.
      </p>
    </div>

    <div class="certificates">
      <div class="certificates-heading">
        <div>
          <p class="eyebrow">APRENDIZAJE INDIVIDUAL</p>
          <h3>Insignias de Google Skills</h3>
        </div>
        <span class="certificate-count">10 insignias</span>
      </div>

      <div class="certificate-grid" aria-label="Insignias de aprendizaje Google Skills">
        {#each skillBadges as badge}
          <button
            class="certificate-card featured-card"
            type="button"
            aria-haspopup="dialog"
            aria-label={`Ver imagen de ${badge.label}`}
            on:click={(event) => openBadge(badge, event)}
          >
            <span class="certificate-icon" aria-hidden="true">✦</span>
            <span class="certificate-label">{badge.label}</span>
            <span class="certificate-link">Ver insignia <span aria-hidden="true">↗</span></span>
          </button>
        {/each}
      </div>
    </div>
  </div>
</section>

{#if selectedBadge}
  <div
    class="badge-modal-backdrop"
    role="presentation"
    on:click={(event) => event.target === event.currentTarget && closeBadge()}
  >
    <dialog
      class="badge-dialog"
      open
      bind:this={dialog}
      aria-modal="true"
      aria-labelledby="badge-dialog-title"
      on:keydown={handleDialogKeydown}
      on:click|stopPropagation
    >
      <button
        bind:this={closeButton}
        class="badge-dialog-close"
        type="button"
        aria-label="Cerrar insignia"
        on:click={closeBadge}
      >×</button>
      <p class="eyebrow badge-dialog-eyebrow">GOOGLE SKILLS</p>
      <h2 id="badge-dialog-title">{selectedBadge.label}</h2>
      {#if imageLoadError}
        <p class="badge-image-error" role="alert">
          No se pudo cargar la imagen de la insignia. Puedes consultar la ficha oficial en Google Skills.
        </p>
      {:else}
        <img
          class="badge-image"
          src={selectedBadge.imageUrl}
          alt={selectedBadge.label}
          on:error={() => imageLoadError = true}
        />
      {/if}
      <a class="badge-source-link" href={selectedBadge.url} target="_blank" rel="noopener noreferrer">
        Abrir ficha oficial en Google Skills <span aria-hidden="true">↗</span>
      </a>
    </dialog>
  </div>
{/if}

<style>
  .cybersecurity {
    padding: clamp(3.5rem, 8vw, 7rem) 1.25rem;
    color: #f7f5ff;
    background:
      radial-gradient(ellipse at 12% 10%, rgba(0, 245, 212, 0.12), transparent 34rem),
      linear-gradient(180deg, #0b0c14, #101320);
  }

  .cybersecurity-inner {
    width: min(1120px, 100%);
    margin: 0 auto;
  }

  .intro {
    max-width: 720px;
  }

  .eyebrow {
    color: #00f5d4;
    font-size: 0.7rem;
    font-weight: 750;
    letter-spacing: 0.14em;
  }

  .eyebrow {
    margin: 0 0 0.75rem;
  }

  h2 {
    margin: 0;
    font-size: clamp(2rem, 5vw, 3.5rem);
    letter-spacing: -0.05em;
    line-height: 1.08;
  }

  .lead {
    max-width: 620px;
    margin: 1rem 0 0;
    color: #b8bbca;
    font-size: 1.05rem;
    line-height: 1.7;
  }

  .credentials {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    margin: 2rem 0;
    padding: 1.1rem 1.25rem;
    border: 1px solid rgba(0, 245, 212, 0.25);
    border-radius: 16px;
    background: rgba(0, 245, 212, 0.055);
  }

  .credential-mark {
    display: grid;
    flex: 0 0 2rem;
    aspect-ratio: 1;
    place-items: center;
    color: #071311;
    border-radius: 50%;
    background: #00f5d4;
    font-weight: 900;
  }

  .credentials p {
    display: grid;
    gap: 0.3rem;
    margin: 0;
    color: #b8bbca;
    line-height: 1.6;
  }

  .credentials strong {
    color: #f7f5ff;
  }

  .certificates {
    margin: 2rem 0;
  }

  .certificates-heading {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 1rem;
  }

  .certificates-heading .eyebrow {
    margin-bottom: 0.4rem;
  }

  .certificates-heading h3 {
    margin: 0;
    font-size: clamp(1.35rem, 3vw, 1.8rem);
    letter-spacing: -0.035em;
  }

  .certificate-count {
    color: #b8bbca;
    font-size: 0.8rem;
    white-space: nowrap;
  }

  .certificate-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 0.75rem;
  }

  .certificate-card {
    display: grid;
    grid-template-columns: auto 1fr;
    align-items: center;
    gap: 0.2rem 0.7rem;
    min-width: 0;
    padding: 0.9rem;
    text-align: left;
    font: inherit;
    color: #f7f5ff;
    border: 1px solid rgba(255, 255, 255, 0.11);
    border-radius: 14px;
    background: rgba(255, 255, 255, 0.035);
    cursor: pointer;
    transition: transform 180ms ease, border-color 180ms ease, background 180ms ease;
  }

  .certificate-card:hover,
  .certificate-card:focus-visible {
    transform: translateY(-2px);
    border-color: rgba(0, 245, 212, 0.5);
    background: rgba(0, 245, 212, 0.07);
  }

  .certificate-card:focus-visible {
    outline: 2px solid #00f5d4;
    outline-offset: 3px;
  }

  .featured-card {
    border-color: rgba(0, 245, 212, 0.25);
    background: rgba(0, 245, 212, 0.055);
  }

  .certificate-icon {
    grid-row: span 2;
    color: #00f5d4;
    font-size: 1.15rem;
  }

  .certificate-label {
    overflow: hidden;
    font-size: 0.8rem;
    font-weight: 700;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .certificate-link {
    color: #a4a8ba;
    font-size: 0.7rem;
  }

  .certificate-link span {
    color: #00f5d4;
  }

  .badge-modal-backdrop {
    position: fixed;
    z-index: 5000;
    inset: 0;
    display: grid;
    place-items: center;
    padding: 1rem;
    background: rgba(3, 5, 11, 0.8);
    backdrop-filter: blur(8px);
  }

  .badge-dialog {
    position: relative;
    width: min(680px, 100%);
    max-height: min(88vh, 760px);
    margin: 0;
    overflow-y: auto;
    padding: clamp(1.25rem, 4vw, 2rem);
    color: #f7f5ff;
    border: 1px solid rgba(0, 245, 212, 0.3);
    border-radius: 22px;
    background:
      radial-gradient(ellipse at 100% 0%, rgba(0, 245, 212, 0.1), transparent 19rem),
      #10131f;
    box-shadow: 0 28px 90px rgba(0, 0, 0, 0.62);
  }

  .badge-dialog-close {
    position: absolute;
    top: 0.8rem;
    right: 0.8rem;
    display: grid;
    width: 2.4rem;
    aspect-ratio: 1;
    place-items: center;
    color: #e8e7f0;
    border: 1px solid rgba(255, 255, 255, 0.16);
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.06);
    font-size: 1.5rem;
    cursor: pointer;
  }

  .badge-dialog-close:hover,
  .badge-dialog-close:focus-visible {
    border-color: #00f5d4;
    outline: 2px solid #00f5d4;
    outline-offset: 2px;
  }

  .badge-dialog-eyebrow {
    margin-right: 3rem;
  }

  .badge-dialog h2 {
    margin: 0 3rem 1.25rem 0;
    font-size: clamp(1.2rem, 3vw, 1.65rem);
    line-height: 1.3;
    overflow-wrap: anywhere;
  }

  .badge-image {
    display: block;
    width: 100%;
    max-height: min(50vh, 420px);
    object-fit: contain;
    border-radius: 12px;
    background: rgba(255, 255, 255, 0.04);
  }

  .badge-image-error {
    margin: 0;
    padding: 1rem;
    color: #ffd7a8;
    border: 1px solid rgba(255, 215, 168, 0.25);
    border-radius: 12px;
    background: rgba(255, 215, 168, 0.06);
  }

  .badge-source-link {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    margin-top: 1rem;
    padding: 0.7rem 0.95rem;
    color: #071311;
    border-radius: 10px;
    background: #00f5d4;
    font-size: 0.9rem;
    font-weight: 750;
  }

  .badge-source-link:hover,
  .badge-source-link:focus-visible {
    color: #071311;
    background: #78ffe9;
    outline: 2px solid #f7f5ff;
    outline-offset: 3px;
  }

  @media (max-width: 640px) {
    .certificate-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .credentials {
      padding: 1rem;
    }
  }

  @media (max-width: 380px) {
    .certificate-grid {
      grid-template-columns: 1fr;
    }
  }
</style>
