<script>
  import { showCardDetails } from "../lib/cardDetails.js";

  export let title;
  export let description;
  export let details = [];
  export let accent = "#00f5d4";
  export let stretch = false;
</script>

<button
  class="card-detail-trigger"
  class:stretch
  type="button"
  style:--detail-accent={accent}
  title={`Ver detalles de ${title}`}
  aria-label={`Ver detalles de ${title}`}
  on:click={() => showCardDetails({ title, description, details, accent })}
>
  <span aria-hidden="true">ⓘ</span>
</button>

<style>
  .card-detail-trigger {
    display: grid;
    flex: 0 0 auto;
    width: 2.2rem;
    aspect-ratio: 1;
    margin-top: 0.75rem;
    padding: 0;
    place-items: center;
    color: var(--detail-accent);
    border: 1px solid color-mix(in srgb, var(--detail-accent) 32%, transparent);
    border-radius: 50%;
    background: color-mix(in srgb, var(--detail-accent) 8%, transparent);
    font: inherit;
    font-size: 1.15rem;
    font-weight: 700;
    line-height: 1;
    cursor: pointer;
    transition: background 160ms ease, border-color 160ms ease, transform 160ms ease;
  }

  .card-detail-trigger:hover {
    transform: translateY(-1px);
    border-color: color-mix(in srgb, var(--detail-accent) 68%, transparent);
    background: color-mix(in srgb, var(--detail-accent) 14%, transparent);
  }

  .card-detail-trigger:focus-visible {
    outline: 2px solid var(--detail-accent);
    outline-offset: 3px;
  }

  .card-detail-trigger.stretch {
    grid-column: 1 / -1;
    justify-self: start;
    margin-top: 0.35rem;
  }

  @media (prefers-reduced-motion: reduce) {
    .card-detail-trigger {
      transition: none;
    }
  }
</style>
