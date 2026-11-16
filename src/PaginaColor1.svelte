<script>
  export let color;
  import { onMount, onDestroy } from "svelte";
  import "./lib/snake.css";

  let canvas;
  let ctx;
  let size = 320;
  let grid = 20;
  let cell = 16;
  let gameBoard;
  let score = 0;
  let best = 0;
  let enemyScore = 0;
  let level = 1;
  let running = false;
  let gameOver = false;
  let tickMs = 100;
  let timer;

  let dir = { x: 1, y: 0 };
  let nextDir = { x: 1, y: 0 };
  let snake = [{ x: 5, y: 8 }, { x: 4, y: 8 }, { x: 3, y: 8 }];
  let food = { x: 12, y: 8 };
  let enemy = { x: 15, y: 15 };
  let enemyStep = 0;
  let enemyMode = "head";
  let enemyBody = [];
  let enemyGrow = 0;
  let obstacles = [];
  let particles = [];
  let nextObstacleAt = 120;
  let nextBlockAt = 50;
  let obstacleShapes = [
    [ // O (2x2)
      { x: 0, y: 0 }, { x: 1, y: 0 },
      { x: 0, y: 1 }, { x: 1, y: 1 }
    ],
    [ // L
      { x: 0, y: 0 }, { x: 0, y: 1 }, { x: 0, y: 2 },
      { x: 1, y: 2 }
    ],
    [ // T
      { x: 0, y: 0 }, { x: 1, y: 0 }, { x: 2, y: 0 },
      { x: 1, y: 1 }
    ],
    [ // Z
      { x: 0, y: 0 }, { x: 1, y: 0 },
      { x: 1, y: 1 }, { x: 2, y: 1 }
    ],
    [ // I (línea)
      { x: 0, y: 0 }, { x: 0, y: 1 }, { x: 0, y: 2 }, { x: 0, y: 3 }
    ]
  ];

  let touchStart = null;
  let isActive = false;
  let isFullscreen = false;
  let isLandscape = false;
  let isSwipeMode = false;
  let gameWrap;
  let boardObserver;

  function resize() {
    if (!canvas || !gameBoard) return;
    isLandscape = window.innerWidth > window.innerHeight;
    const availableWidth = gameBoard.clientWidth - 20;
    const availableHeight = gameBoard.clientHeight - 20;
    const maxSize = Math.min(availableWidth, availableHeight, 760);
    size = Math.max(grid * 4, Math.floor(maxSize / grid) * grid);
    canvas.width = size;
    canvas.height = size;
    cell = Math.floor(size / grid);
    canvas.style.width = `${size}px`;
    canvas.style.height = `${size}px`;
    draw();
  }

  function randomFood() {
    let pos;
    do {
      pos = {
        x: Math.floor(Math.random() * grid),
        y: Math.floor(Math.random() * grid),
      };
    } while (
      snake.some((s) => s.x === pos.x && s.y === pos.y) ||
      obstacles.some((o) => o.x === pos.x && o.y === pos.y) ||
      (pos.x === enemy.x && pos.y === enemy.y)
    );
    return pos;
  }

  function randomEnemy() {
    let pos;
    do {
      pos = {
        x: Math.floor(Math.random() * grid),
        y: Math.floor(Math.random() * grid),
      };
    } while (
      snake.some((s) => s.x === pos.x && s.y === pos.y) ||
      (pos.x === food.x && pos.y === food.y) ||
      obstacles.some((o) => o.x === pos.x && o.y === pos.y)
    );
    return pos;
  }

  function rotateShape(shape, times) {
    let rotated = shape;
    for (let i = 0; i < times; i++) {
      rotated = rotated.map((b) => ({ x: b.y, y: -b.x }));
      // normalize to non-negative
      const minX = Math.min(...rotated.map((b) => b.x));
      const minY = Math.min(...rotated.map((b) => b.y));
      rotated = rotated.map((b) => ({ x: b.x - minX, y: b.y - minY }));
    }
    return rotated;
  }

  function canPlace(blocks) {
    const head = snake[0];
    return blocks.every((b) => {
      if (b.x < 0 || b.x >= grid || b.y < 0 || b.y >= grid) return false;
      if (snake.some((s) => s.x === b.x && s.y === b.y)) return false;
      if (obstacles.some((o) => o.x === b.x && o.y === b.y)) return false;
      if (b.x === food.x && b.y === food.y) return false;
      if (b.x === enemy.x && b.y === enemy.y) return false;
      const dist = Math.abs(b.x - head.x) + Math.abs(b.y - head.y);
      if (dist <= 2) return false; // evita spawn cerca de la cabeza
      return true;
    });
  }

  function placeShape() {
    const base = obstacleShapes[Math.floor(Math.random() * obstacleShapes.length)];
    const rotations = Math.floor(Math.random() * 4);
    const shape = rotateShape(base, rotations);
    const maxX = Math.max(...shape.map((b) => b.x));
    const maxY = Math.max(...shape.map((b) => b.y));

    for (let i = 0; i < 40; i++) {
      const origin = {
        x: Math.floor(Math.random() * (grid - maxX)),
        y: Math.floor(Math.random() * (grid - maxY)),
      };
      const blocks = shape.map((b) => ({ x: origin.x + b.x, y: origin.y + b.y }));
      if (canPlace(blocks)) return blocks;
    }
    return null;
  }

  function addObstacle() {
    const blocks = placeShape();
    if (blocks) {
      obstacles = [...obstacles, ...blocks];
    }
  }

  function resetGame() {
    pause();
    score = 0;
    enemyScore = 0;
    isActive = false;
    gameOver = false;
    dir = { x: 1, y: 0 };
    nextDir = { x: 1, y: 0 };
    snake = [{ x: 5, y: 8 }, { x: 4, y: 8 }, { x: 3, y: 8 }];
    food = randomFood();
    enemy = randomEnemy();
    enemyStep = 0;
    enemyMode = "head";
    enemyBody = [];
    enemyGrow = 0;
    obstacles = [];
    particles = [];
    nextObstacleAt = 120;
    nextBlockAt = 50;
    level = 1;
    draw();
  }

  function start() {
    if (running || gameOver) return;
    isActive = true;
    running = true;
    timer = setInterval(step, tickMs);
  }

  function pause() {
    running = false;
    clearInterval(timer);
  }

  // Botón único: iniciar / pausar / continuar
  function toggleGameState() {
    if (!isActive) {
      start();
      return;
    }
    if (running) {
      pause();
    } else {
      start();
    }
  }

  function step() {
    if (gameOver) return;
    dir = nextDir;

    const head = { ...snake[0] };
    head.x += dir.x;
    head.y += dir.y;

    if (head.x < 0 || head.x >= grid || head.y < 0 || head.y >= grid) {
      endGame();
      return;
    }
    if (snake.some((s) => s.x === head.x && s.y === head.y)) {
      endGame();
      return;
    }
    if (obstacles.some((o) => o.x === head.x && o.y === head.y)) {
      endGame();
      return;
    }

    snake.unshift(head);

    if (head.x === food.x && head.y === food.y) {
      score += 10;
      best = Math.max(best, score);
      spawnParticles(food.x, food.y, "player");
      food = randomFood();
      level = Math.floor(score / 20) + 1;
      if (score >= nextObstacleAt) {
        addObstacle();
        nextObstacleAt += 120;
      }
      if (score >= nextBlockAt) {
        addObstacle();
        nextBlockAt += 50;
      }
    } else {
      snake.pop();
    }

    // Enemigo con IA simple: alterna entre comida y cabeza
    enemyStep += 1;
    const enemySpeed = score >= 30 ? 1 : 2; // a mayor score, enemigo más frecuente
    if (enemyStep % enemySpeed === 0) {
      if (enemyStep % 6 === 0) {
        enemyMode = enemyMode === "head" ? "food" : "head";
      }
      const target = enemyMode === "food" ? food : snake[0];
      const nextEnemy = moveEnemy(enemy, target);
      enemyBody.unshift({ x: enemy.x, y: enemy.y });
      enemy = nextEnemy;
      if (enemyGrow > 0) {
        enemyGrow -= 1;
      } else {
        enemyBody.pop();
      }
    }

    if (obstacles.some((o) => o.x === enemy.x && o.y === enemy.y)) {
      endGame();
      return;
    }

    // Si el enemigo come la comida, crece y reaparece la comida
    if (enemy.x === food.x && enemy.y === food.y) {
      enemyGrow += 2;
      enemyScore += 10;
      spawnParticles(food.x, food.y, "enemy");
      food = randomFood();
    }

    if (enemy.x === snake[0].x && enemy.y === snake[0].y) {
      endGame();
      return;
    }

    updateParticles();
    draw();
  }

  function endGame() {
    gameOver = true;
    pause();
    draw();
  }

  function moveEnemy(current, target) {
    const options = [
      { x: current.x + 1, y: current.y },
      { x: current.x - 1, y: current.y },
      { x: current.x, y: current.y + 1 },
      { x: current.x, y: current.y - 1 },
    ];

    const valid = options.filter((p) => {
      if (p.x < 0 || p.x >= grid || p.y < 0 || p.y >= grid) return false;
      if (obstacles.some((o) => o.x === p.x && o.y === p.y)) return false;
      if (enemyBody.some((e) => e.x === p.x && e.y === p.y)) return false;
      if (snake.some((s) => s.x === p.x && s.y === p.y)) return false;
      return true;
    });

    if (!valid.length) {
      return current;
    }

    // Si hay muchas opciones, meter un poco de caos (20%)
    if (Math.random() < 0.2) {
      return valid[Math.floor(Math.random() * valid.length)];
    }

    // Elegir la que minimice la distancia Manhattan a la cabeza
    let best = valid[0];
    let bestDist = Math.abs(best.x - target.x) + Math.abs(best.y - target.y);
    for (const p of valid) {
      const d = Math.abs(p.x - target.x) + Math.abs(p.y - target.y);
      if (d < bestDist) {
        best = p;
        bestDist = d;
      }
    }
    return best;
  }

  function setDir(x, y) {
    if (gameOver) return;
    if (dir.x === -x && dir.y === -y) return;
    isActive = true;
    if (!running && !gameOver) start();
    nextDir = { x, y };
  }

  function handleKey(e) {
    if (!["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight", " "].includes(e.key)) return;
    if (e.target instanceof HTMLElement && e.target.closest("button")) return;
    e.preventDefault();
    if (gameOver) return;
    if (e.key === " ") {
      toggleGameState();
      return;
    }
    if (e.key === "ArrowUp") setDir(0, -1);
    if (e.key === "ArrowDown") setDir(0, 1);
    if (e.key === "ArrowLeft") setDir(-1, 0);
    if (e.key === "ArrowRight") setDir(1, 0);
  }

  function onTouchStart(e) {
    if (!isSwipeMode || gameOver) return;
    const t = e.touches[0];
    touchStart = { x: t.clientX, y: t.clientY };
  }

  function onTouchEnd(e) {
    if (!isSwipeMode || gameOver) return;
    if (!touchStart) return;
    const t = e.changedTouches[0];
    const dx = t.clientX - touchStart.x;
    const dy = t.clientY - touchStart.y;
    touchStart = null;

    if (Math.abs(dx) < 20 && Math.abs(dy) < 20) return;
    if (!running && !gameOver) start();
    if (Math.abs(dx) > Math.abs(dy)) {
      setDir(dx > 0 ? 1 : -1, 0);
    } else {
      setDir(0, dy > 0 ? 1 : -1);
    }
  }

  function spawnParticles(cx, cy, kind) {
    const count = kind === "enemy" ? 14 : 10;
    const baseColor = kind === "enemy" ? "#f97316" : "#22d3ee";
    for (let i = 0; i < count; i++) {
      particles.push({
        x: (cx + 0.5) * cell,
        y: (cy + 0.5) * cell,
        vx: (Math.random() - 0.5) * 2.8,
        vy: (Math.random() - 0.7) * 2.8,
        life: 28 + Math.floor(Math.random() * 12),
        maxLife: 40,
        color: baseColor,
        size: 2 + Math.random() * 2.5,
        coin: kind === "enemy" && Math.random() > 0.4
      });
    }
  }

  function updateParticles() {
    if (!particles.length) return;
    particles = particles
      .map((p) => ({
        ...p,
        x: p.x + p.vx,
        y: p.y + p.vy,
        vy: p.vy + 0.05,
        life: p.life - 1
      }))
      .filter((p) => p.life > 0);
  }

  function draw() {
    if (!ctx) return;
    ctx.clearRect(0, 0, size, size);

    const hue = (level * 40) % 360;
    const bg = ctx.createLinearGradient(0, 0, size, size);
    bg.addColorStop(0, `hsla(${hue}, 60%, 12%, 0.95)`);
    bg.addColorStop(1, `hsla(${(hue + 60) % 360}, 60%, 8%, 0.95)`);
    ctx.fillStyle = bg;
    ctx.fillRect(0, 0, size, size);

    ctx.strokeStyle = "rgba(148, 183, 205, 0.2)";
    ctx.lineWidth = 1;
    for (let i = 0; i <= grid; i++) {
      ctx.beginPath();
      ctx.moveTo(i * cell, 0);
      ctx.lineTo(i * cell, size);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(0, i * cell);
      ctx.lineTo(size, i * cell);
      ctx.stroke();
    }

    ctx.save();
    ctx.strokeStyle = "rgba(125, 211, 252, 0.32)";
    ctx.lineWidth = 1.25;
    for (let i = 0; i <= grid; i += 5) {
      ctx.beginPath();
      ctx.moveTo(i * cell, 0);
      ctx.lineTo(i * cell, size);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(0, i * cell);
      ctx.lineTo(size, i * cell);
      ctx.stroke();
    }
    ctx.restore();

    ctx.fillStyle = `hsl(${hue}, 90%, 60%)`;
    ctx.fillRect(food.x * cell, food.y * cell, cell, cell);

    if (obstacles.length) {
      ctx.fillStyle = "#a855f7";
      for (const o of obstacles) {
        ctx.fillRect(o.x * cell, o.y * cell, cell, cell);
      }
    }


    ctx.fillStyle = "#ef4444";
    ctx.beginPath();
    ctx.arc(
      enemy.x * cell + cell / 2,
      enemy.y * cell + cell / 2,
      Math.max(4, cell / 2 - 2),
      0,
      Math.PI * 2
    );
    ctx.fill();

    if (enemyBody.length) {
      ctx.fillStyle = "rgba(239, 68, 68, 0.6)";
      for (const e of enemyBody) {
        ctx.fillRect(e.x * cell, e.y * cell, cell, cell);
      }
    }

    ctx.fillStyle = "#1f2937";
    for (let i = 0; i < snake.length; i++) {
      const s = snake[i];
      ctx.fillStyle = i === 0 ? "#22d3ee" : "#0ea5e9";
      ctx.fillRect(s.x * cell, s.y * cell, cell, cell);
    }

    if (particles.length) {
      for (const p of particles) {
        const alpha = Math.max(0, p.life / p.maxLife);
        ctx.globalAlpha = alpha;
        if (p.coin) {
          ctx.fillStyle = "#facc15";
          ctx.beginPath();
          ctx.ellipse(p.x, p.y, p.size + 1.5, p.size, 0, 0, Math.PI * 2);
          ctx.fill();
          ctx.strokeStyle = "rgba(255,255,255,0.4)";
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(p.x, p.y - p.size);
          ctx.lineTo(p.x, p.y + p.size);
          ctx.stroke();
        } else {
          ctx.fillStyle = p.color;
          ctx.beginPath();
          ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
          ctx.fill();
        }
      }
      ctx.globalAlpha = 1;
    }

    if (gameOver) {
      ctx.fillStyle = "rgba(2, 8, 18, 0.72)";
      ctx.fillRect(0, 0, size, size);
      ctx.fillStyle = "#fff";
      ctx.font = "700 20px system-ui, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText("FIN DE PARTIDA", size / 2, size / 2 - 4);
      ctx.fillStyle = "#a8c0d0";
      ctx.font = "500 13px system-ui, sans-serif";
      ctx.fillText("Usa Nueva partida para volver a jugar", size / 2, size / 2 + 22, size - 24);
    }
  }

  onMount(() => {
    ctx = canvas.getContext("2d");
    isSwipeMode = window.innerWidth <= 760;
    resize();
    window.addEventListener("resize", resize);
    boardObserver = new ResizeObserver(resize);
    boardObserver.observe(gameBoard);
    resetGame();
  });

  onDestroy(() => {
    window.removeEventListener("resize", resize);
    boardObserver?.disconnect();
    clearInterval(timer);
  });

  function enterFullscreen() {
    if (!gameWrap) return;
    const el = gameWrap;
    if (document.fullscreenElement) return;
    if (el.requestFullscreen) {
      el.requestFullscreen();
    }
  }

  function exitFullscreen() {
    if (document.fullscreenElement) {
      document.exitFullscreen();
    }
  }

  function handleFullscreenChange() {
    isFullscreen = !!document.fullscreenElement;
    resize();
    draw();
  }

  onMount(() => {
    document.addEventListener("fullscreenchange", handleFullscreenChange);
    return () =>
      document.removeEventListener("fullscreenchange", handleFullscreenChange);
  });
</script>

<main
  class="snake-page"
  class:fullscreen={isFullscreen}
  class:landscape={isLandscape}
  style={`--game-accent: ${color};`}
>
  <!-- The application role makes this composite game surface keyboard-operable. -->
  <!-- svelte-ignore a11y_no_noninteractive_tabindex a11y_no_noninteractive_element_interactions -->
  <div
    bind:this={gameWrap}
    class="snake-card"
    style={`--neon-hue: ${(level * 40) % 360};`}
    role="application"
    tabindex="0"
    aria-label="Juego Snake"
    on:keydown={handleKey}
    on:click={(e) => {
      if (!e.target.closest("button")) e.currentTarget.focus();
    }}
  >
    <header class="game-header">
      <div class="game-title">
        <p class="game-eyebrow">ARCADE <span> / </span> 01</p>
        <h1>Snake <span>Mobile</span></h1>
      </div>
      <div class="header-actions">
        <span class="game-status" class:is-running={running} class:is-over={gameOver}>
          {gameOver ? "Finalizada" : running ? "En curso" : isActive ? "En pausa" : "Listo"}
        </span>
        <button
          type="button"
          class="icon-button fullscreen-button"
          on:click={isFullscreen ? exitFullscreen : enterFullscreen}
          aria-label={isFullscreen ? "Salir de pantalla completa" : "Activar pantalla completa"}
          title={isFullscreen ? "Salir de pantalla completa" : "Pantalla completa"}
        >
          {isFullscreen ? "⤢" : "⛶"}
        </button>
      </div>
    </header>

    <div class="game-layout">
      <section
        bind:this={gameBoard}
        class="board-stage"
        aria-label="Tablero de juego"
        on:touchstart|passive={onTouchStart}
        on:touchend|passive={onTouchEnd}
      >
        <div class="canvas-wrap">
          <canvas bind:this={canvas} aria-label="Cuadrícula de juego de 20 por 20"></canvas>
        </div>
      </section>

      <aside class="game-sidebar" aria-label="Panel de juego">
        <section class="score-panel" aria-label="Marcador">
          <div class="score-main">
            <span class="panel-label">PUNTUACIÓN</span>
            <strong>{score}</strong>
          </div>
          <div class="score-grid">
            <div class="score-tile">
              <span>Récord</span>
              <strong>{best}</strong>
            </div>
            <div class="score-tile enemy-score">
              <span>Rival</span>
              <strong>{enemyScore}</strong>
            </div>
          </div>
          <div class="level-row">
            <span>Nivel</span>
            <strong>{level}</strong>
          </div>
        </section>

        <section class="control-card" aria-label="Controles">
          <div class="control-card-heading">
            <span class="panel-label">CONTROLES</span>
            <div class="control-modes" role="group" aria-label="Modo de control">
              <button
                type="button"
                class:mode-active={!isSwipeMode}
                aria-pressed={!isSwipeMode}
                on:click={() => (isSwipeMode = false)}
              >Botones</button>
              <button
                type="button"
                class:mode-active={isSwipeMode}
                aria-pressed={isSwipeMode}
                on:click={() => (isSwipeMode = true)}
              >Deslizar</button>
            </div>
          </div>

          {#if isSwipeMode}
            <p class="swipe-hint">Desliza sobre la cuadrícula para cambiar de dirección.</p>
          {:else}
            <div class="controls" role="group" aria-label="Direcciones">
              <button type="button" class="direction-button up" aria-label="Mover arriba" on:click={() => setDir(0, -1)}>↑</button>
              <button type="button" class="direction-button left" aria-label="Mover a la izquierda" on:click={() => setDir(-1, 0)}>←</button>
              <button type="button" class="direction-button right" aria-label="Mover a la derecha" on:click={() => setDir(1, 0)}>→</button>
              <button type="button" class="direction-button down" aria-label="Mover abajo" on:click={() => setDir(0, 1)}>↓</button>
            </div>
          {/if}

          <div class="game-actions">
            {#if gameOver}
              <button type="button" class="primary-action" on:click={resetGame}>Nueva partida</button>
            {:else}
              <button type="button" class="primary-action" on:click={toggleGameState}>
                {running ? "Pausar" : isActive ? "Continuar" : "Jugar"}
              </button>
            {/if}
            <button type="button" class="secondary-action" on:click={resetGame}>Reiniciar</button>
          </div>
          <p class="keyboard-hint">Usa las flechas del teclado <span>·</span> Espacio para pausar</p>
        </section>

        <div class="game-legend" aria-label="Elementos del tablero">
          <span><i class="legend-dot food"></i>Comida</span>
          <span><i class="legend-dot player"></i>Tu serpiente</span>
          <span><i class="legend-dot rival"></i>Rival</span>
          <span><i class="legend-dot obstacle"></i>Obstáculos</span>
        </div>
      </aside>
    </div>
  </div>
</main>
