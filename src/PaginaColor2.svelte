<script>
  import { onDestroy, onMount } from "svelte";

  export let color = "#00ffd5";

  const symbols = ["🚀", "🪐", "👾", "🌙", "⭐", "🛸"];
  let cards = [];
  let revealed = [];
  let matched = [];
  let moves = 0;
  let seconds = 0;
  let best = null;
  let locked = false;
  let finished = false;
  let timer;
  let mismatchTimeout;

  $: pairsFound = matched.length;
  $: timeLabel = `${Math.floor(seconds / 60)
    .toString()
    .padStart(2, "0")}:${(seconds % 60).toString().padStart(2, "0")}`;

  onMount(() => {
    const savedBest = Number(localStorage.getItem("pagina-color-2-best"));
    if (savedBest > 0) best = savedBest;
    startNewGame();
  });

  onDestroy(() => {
    clearInterval(timer);
    clearTimeout(mismatchTimeout);
  });

  function startNewGame() {
    clearInterval(timer);
    clearTimeout(mismatchTimeout);
    timer = undefined;
    mismatchTimeout = undefined;
    revealed = [];
    matched = [];
    moves = 0;
    seconds = 0;
    locked = false;
    finished = false;
    cards = [...symbols, ...symbols]
      .map((symbol, index) => ({ id: index, pair: symbol, symbol }))
      .sort(() => Math.random() - 0.5);
  }

  function revealCard(card) {
    if (locked || finished || revealed.includes(card.id) || matched.includes(card.pair)) return;

    if (!timer) {
      timer = setInterval(() => {
        seconds += 1;
      }, 1000);
    }

    revealed = [...revealed, card.id];
    if (revealed.length !== 2) return;

    moves += 1;
    const [firstId, secondId] = revealed;
    const firstCard = cards.find((item) => item.id === firstId);
    const secondCard = cards.find((item) => item.id === secondId);

    if (firstCard.pair === secondCard.pair) {
      matched = [...matched, firstCard.pair];
      revealed = [];
      if (matched.length === symbols.length) finishGame();
      return;
    }

    locked = true;
    mismatchTimeout = setTimeout(() => {
      revealed = [];
      locked = false;
      mismatchTimeout = undefined;
    }, 850);
  }

  function finishGame() {
    finished = true;
    clearInterval(timer);
    timer = undefined;
    if (best === null || moves < best) {
      best = moves;
      localStorage.setItem("pagina-color-2-best", String(best));
    }
  }
</script>

<svelte:head>
  <title>Memoria cósmica | DASH.IO</title>
  <meta
    name="description"
    content="Encuentra las parejas de planetas y estrellas en este juego de memoria."
  />
</svelte:head>

<main class="game-page" style="--game-accent: {color};">
  <section class="game-shell" aria-label="Juego de memoria cósmica">
    <header class="game-header">
      <div>
        <p class="eyebrow"><span class="status-dot"></span> MINI JUEGO</p>
        <h1>Memoria <span>cósmica</span></h1>
        <p class="subtitle">Encuentra las parejas y explora la galaxia.</p>
      </div>
      <button class="restart-button" type="button" on:click={startNewGame}>
        <span aria-hidden="true">↻</span> Reiniciar
      </button>
    </header>

    <div class="game-info" aria-label="Estadísticas de la partida">
      <div class="stat">
        <span class="stat-icon" aria-hidden="true">🎯</span>
        <span class="stat-copy"><small>MOVIMIENTOS</small><strong>{moves}</strong></span>
      </div>
      <div class="stat">
        <span class="stat-icon" aria-hidden="true">⏱️</span>
        <span class="stat-copy"><small>TIEMPO</small><strong>{timeLabel}</strong></span>
      </div>
      <div class="stat">
        <span class="stat-icon" aria-hidden="true">✨</span>
        <span class="stat-copy"><small>PAREJAS</small><strong>{pairsFound} / {symbols.length}</strong></span>
      </div>
      <div class="stat best-stat">
        <span class="stat-icon" aria-hidden="true">🏆</span>
        <span class="stat-copy"><small>MEJOR</small><strong>{best === null ? "—" : `${best} mov.`}</strong></span>
      </div>
    </div>

    <div class="board" aria-label="Tablero de cartas">
      {#each cards as card (card.id)}
        <button
          class:revealed={revealed.includes(card.id) || matched.includes(card.pair)}
          class:matched={matched.includes(card.pair)}
          class="card"
          type="button"
          aria-label={revealed.includes(card.id) || matched.includes(card.pair)
            ? `Carta ${card.symbol}`
            : "Carta oculta"}
          aria-pressed={revealed.includes(card.id) || matched.includes(card.pair)}
          disabled={locked || matched.includes(card.pair)}
          on:click={() => revealCard(card)}
        >
          <span class="card-face card-back" aria-hidden="true">✦</span>
          <span class="card-face card-front" aria-hidden="true">{card.symbol}</span>
        </button>
      {/each}
    </div>

    <footer class="game-footer">
      {#if finished}
        <p class="win-message" role="status">¡Misión cumplida! Encontraste todas las parejas. 🚀</p>
        <button class="play-again" type="button" on:click={startNewGame}>Jugar otra vez</button>
      {:else}
        <p>Voltea dos cartas por turno. ¿Puedes encontrar las 6 parejas?</p>
      {/if}
    </footer>
  </section>
</main>

<style>
  :global(body) {
    margin: 0;
  }

  .game-page {
    --game-accent: #00ffd5;
    min-height: 100vh;
    box-sizing: border-box;
    display: grid;
    place-items: center;
    padding: 40px 20px;
    color: #f5f7ff;
    background:
      radial-gradient(ellipse at 15% 10%, color-mix(in srgb, var(--game-accent) 15%, transparent), transparent 35%),
      radial-gradient(ellipse at 90% 85%, rgba(116, 74, 255, 0.15), transparent 35%),
      #090d19;
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }

  .game-shell {
    width: min(100%, 720px);
  }

  .game-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    margin-bottom: 28px;
  }

  .eyebrow {
    display: flex;
    align-items: center;
    gap: 9px;
    margin: 0 0 10px;
    color: #99a5bc;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 0.18em;
  }

  .status-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: var(--game-accent);
    box-shadow: 0 0 12px var(--game-accent);
  }

  h1 {
    margin: 0;
    font-size: clamp(30px, 6vw, 46px);
    line-height: 1.05;
    letter-spacing: -0.045em;
  }

  h1 span {
    color: var(--game-accent);
  }

  .subtitle {
    margin: 10px 0 0;
    color: #9aa5ba;
    font-size: 14px;
  }

  button {
    font: inherit;
  }

  .restart-button,
  .play-again {
    border: 1px solid rgba(255, 255, 255, 0.13);
    border-radius: 12px;
    background: rgba(255, 255, 255, 0.06);
    color: #f5f7ff;
    cursor: pointer;
    font-size: 13px;
    font-weight: 700;
    transition: border-color 160ms ease, background 160ms ease, transform 160ms ease;
  }

  .restart-button {
    flex: 0 0 auto;
    padding: 11px 15px;
  }

  .restart-button span {
    margin-right: 5px;
    color: var(--game-accent);
    font-size: 18px;
    vertical-align: -1px;
  }

  .restart-button:hover,
  .play-again:hover {
    transform: translateY(-2px);
    border-color: color-mix(in srgb, var(--game-accent) 55%, transparent);
    background: rgba(255, 255, 255, 0.1);
  }

  .game-info {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    margin-bottom: 18px;
  }

  .stat {
    display: flex;
    align-items: center;
    gap: 10px;
    min-width: 0;
    padding: 12px 14px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    background: rgba(18, 24, 41, 0.82);
  }

  .stat-icon {
    font-size: 19px;
  }

  .stat-copy {
    display: grid;
    gap: 3px;
    min-width: 0;
  }

  .stat-copy small {
    color: #8994ab;
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 0.1em;
  }

  .stat-copy strong {
    overflow: hidden;
    color: #f3f5fc;
    font-size: 16px;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .board {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 12px;
    padding: 16px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    background: rgba(15, 20, 35, 0.78);
    box-shadow: 0 22px 70px rgba(0, 0, 0, 0.28);
  }

  .card {
    position: relative;
    aspect-ratio: 1.18;
    padding: 0;
    border: 1px solid rgba(255, 255, 255, 0.09);
    border-radius: 14px;
    background: transparent;
    cursor: pointer;
    perspective: 700px;
    -webkit-tap-highlight-color: transparent;
  }

  .card:disabled {
    cursor: default;
  }

  .card:focus-visible,
  .restart-button:focus-visible,
  .play-again:focus-visible {
    outline: 3px solid var(--game-accent);
    outline-offset: 3px;
  }

  .card-face {
    position: absolute;
    inset: 0;
    display: grid;
    place-items: center;
    border-radius: 13px;
    backface-visibility: hidden;
    transition: transform 260ms ease, opacity 200ms ease, background 200ms ease;
  }

  .card-back {
    color: var(--game-accent);
    background: linear-gradient(145deg, #1d2941, #141b2d);
    font-size: clamp(22px, 5vw, 34px);
    text-shadow: 0 0 18px color-mix(in srgb, var(--game-accent) 55%, transparent);
  }

  .card-front {
    transform: rotateY(180deg);
    opacity: 0;
    background: linear-gradient(145deg, color-mix(in srgb, var(--game-accent) 18%, #202641), #181d31);
    font-size: clamp(26px, 6vw, 42px);
  }

  .card:hover:not(:disabled) .card-back {
    background: linear-gradient(145deg, #293956, #1b2540);
  }

  .card.revealed .card-back {
    transform: rotateY(180deg);
    opacity: 0;
  }

  .card.revealed .card-front {
    transform: rotateY(0);
    opacity: 1;
  }

  .card.matched .card-front {
    border: 1px solid color-mix(in srgb, var(--game-accent) 40%, transparent);
    background: color-mix(in srgb, var(--game-accent) 13%, #171f33);
    box-shadow: inset 0 0 22px color-mix(in srgb, var(--game-accent) 10%, transparent);
  }

  .game-footer {
    min-height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 14px;
    margin-top: 16px;
    color: #929db2;
    font-size: 13px;
    text-align: center;
  }

  .game-footer p {
    margin: 0;
  }

  .win-message {
    color: var(--game-accent);
    font-weight: 700;
  }

  .play-again {
    padding: 9px 13px;
    border-color: color-mix(in srgb, var(--game-accent) 35%, transparent);
  }

  @media (max-width: 560px) {
    .game-page {
      padding: 28px 14px;
    }

    .game-header {
      align-items: flex-start;
      margin-bottom: 22px;
    }

    .restart-button {
      padding: 9px 10px;
      font-size: 12px;
    }

    .game-info {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .board {
      gap: 8px;
      padding: 10px;
      border-radius: 16px;
    }

    .card {
      border-radius: 11px;
    }

    .card-face {
      border-radius: 10px;
    }

    .game-footer {
      flex-wrap: wrap;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .card-face,
    .restart-button,
    .play-again {
      transition-duration: 0.01ms;
    }
  }
</style>
