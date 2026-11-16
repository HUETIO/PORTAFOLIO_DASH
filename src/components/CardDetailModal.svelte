<script>
  import { activeCardDetails, hideCardDetails } from "../lib/cardDetails.js";

  let closeButton;
  let dialog;

  $: if ($activeCardDetails) {
    requestAnimationFrame(() => closeButton?.focus());
  }

  function handleKeydown(event) {
    if (event.key === "Escape" && $activeCardDetails) {
      hideCardDetails();
      return;
    }

    if (event.key === "Tab" && $activeCardDetails && dialog) {
      const focusable = [...dialog.querySelectorAll("button:not([disabled]), a[href], [tabindex]:not([tabindex='-1'])")];
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

{#if $activeCardDetails}
  <div
    class="details-backdrop"
    role="presentation"
    on:click={(event) => event.target === event.currentTarget && hideCardDetails()}
  >
    <dialog
      class="details-dialog"
      open
      bind:this={dialog}
      style:--dialog-accent={$activeCardDetails.accent || "#00f5d4"}
      aria-modal="true"
      aria-labelledby="card-details-title"
      on:keydown={handleKeydown}
      on:cancel|preventDefault={hideCardDetails}
    >
      <button
        bind:this={closeButton}
        class="details-close"
        type="button"
        aria-label="Cerrar detalles"
        on:click={hideCardDetails}
      >×</button>
      <p class="details-eyebrow">DETALLES</p>
      <h2 id="card-details-title">{$activeCardDetails.title}</h2>
      <p class="details-description">{$activeCardDetails.description}</p>
      {#if $activeCardDetails.details?.length}
        <ul class="details-list">
          {#each $activeCardDetails.details as detail}
            <li>{detail}</li>
          {/each}
        </ul>
      {/if}
    </dialog>
  </div>
{/if}

<style>
  .details-backdrop {
    position: fixed;
    z-index: 5000;
    inset: 0;
    display: grid;
    place-items: center;
    padding: 1rem;
    background: rgba(3, 5, 11, 0.78);
    backdrop-filter: blur(10px);
    animation: backdrop-in 160ms ease-out;
  }

  .details-dialog {
    position: relative;
    width: min(560px, 100%);
    max-height: min(82vh, 680px);
    margin: 0;
    overflow-y: auto;
    padding: clamp(1.4rem, 5vw, 2.2rem);
    color: #f7f5ff;
    border: 1px solid color-mix(in srgb, var(--dialog-accent) 34%, rgba(255, 255, 255, 0.14));
    border-radius: 22px;
    background:
      radial-gradient(ellipse at 100% 0%, color-mix(in srgb, var(--dialog-accent) 13%, transparent), transparent 19rem),
      #10131f;
    box-shadow: 0 28px 90px rgba(0, 0, 0, 0.62);
    animation: dialog-in 190ms ease-out;
  }

  .details-close {
    position: absolute;
    top: 0.9rem;
    right: 0.9rem;
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

  .details-close:hover,
  .details-close:focus-visible {
    border-color: var(--dialog-accent);
    outline: none;
  }

  .details-eyebrow {
    margin: 0 3rem 0.7rem 0;
    color: var(--dialog-accent);
    font-size: 0.68rem;
    font-weight: 800;
    letter-spacing: 0.16em;
  }

  h2 {
    margin: 0;
    font-size: clamp(1.5rem, 4vw, 2.1rem);
    letter-spacing: -0.04em;
    line-height: 1.18;
  }

  .details-description {
    margin: 1rem 0 0;
    color: #d3d5e0;
    line-height: 1.7;
  }

  .details-list {
    display: grid;
    gap: 0.65rem;
    margin: 1.2rem 0 0;
    padding: 0;
    list-style: none;
  }

  .details-list li {
    position: relative;
    padding: 0.75rem 0.85rem 0.75rem 2rem;
    color: #c4c7d4;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    background: rgba(255, 255, 255, 0.035);
    line-height: 1.55;
  }

  .details-list li::before {
    position: absolute;
    top: 0.85rem;
    left: 0.85rem;
    width: 0.5rem;
    aspect-ratio: 1;
    border-radius: 50%;
    background: var(--dialog-accent);
    content: "";
  }

  @keyframes backdrop-in {
    from { opacity: 0; }
    to { opacity: 1; }
  }

  @keyframes dialog-in {
    from { opacity: 0; transform: translateY(10px) scale(0.98); }
    to { opacity: 1; transform: translateY(0) scale(1); }
  }

  @media (prefers-reduced-motion: reduce) {
    .details-backdrop,
    .details-dialog {
      animation: none;
    }
  }
</style>
