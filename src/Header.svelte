<script>
  let menuOpen = false;

  function closeMenu() {
    menuOpen = false;
  }

  function handleKeydown(event) {
    if (event.key === "Escape") closeMenu();
  }
</script>

<svelte:window on:keydown={handleKeydown} />

<header class="site-header">
  <nav class="nav-container" aria-label="Navegación principal">
    <a href="#inicio" class="nav-logo" on:click={closeMenu}>DASH.IO</a>

    <button
      class="nav-toggle"
      type="button"
      aria-label={menuOpen ? "Cerrar menú de navegación" : "Abrir menú de navegación"}
      aria-expanded={menuOpen}
      aria-controls="primary-navigation"
      on:click={() => (menuOpen = !menuOpen)}
    >
      <span class:open={menuOpen}></span>
      <span class:open={menuOpen}></span>
      <span class:open={menuOpen}></span>
    </button>

    <ul id="primary-navigation" class="nav-menu" class:active={menuOpen}>
      <li><a href="#servicios" class="nav-link" on:click={closeMenu}>Servicios</a></li>
      <li><a href="#casos" class="nav-link" on:click={closeMenu}>Soluciones</a></li>
      <li><a href="#seguridad" class="nav-link" on:click={closeMenu}>Seguridad y operación</a></li>
      <li><a href="#trayectoria" class="nav-link" on:click={closeMenu}>Laboratorio digital</a></li>
      <li><a href="#contact" class="nav-link" on:click={closeMenu}>Contacto</a></li>
    </ul>
  </nav>
</header>

<style>
  .site-header {
    position: fixed;
    inset: 0 0 auto;
    width: auto;
    z-index: 1100;
    border-bottom: 1px solid rgba(255, 255, 255, 0.12);
    background: rgba(10, 10, 10, 0.92);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
  }

  .nav-container {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: min(100%, 1200px);
    min-height: 60px;
    margin: 0 auto;
    padding: 0 clamp(1rem, 3vw, 2rem);
  }

  .nav-logo {
    flex-shrink: 0;
    color: #00f5d4;
    font-size: 1.5rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-decoration: none;
  }

  .nav-logo::after {
    display: none;
  }

  .nav-menu {
    display: flex;
    align-items: center;
    gap: clamp(1rem, 2.5vw, 2rem);
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .nav-link {
    display: inline-flex;
    align-items: center;
    min-height: 44px;
    color: #f0f0f0;
    font-size: 0.95rem;
    font-weight: 600;
    text-decoration: none;
    transition: color 180ms ease, transform 180ms ease;
  }

  .nav-link:hover {
    color: #00f5d4;
    transform: translateY(-1px);
  }

  .nav-toggle {
    display: none;
    align-items: center;
    justify-content: center;
    width: 44px;
    height: 44px;
    padding: 0.5rem;
    border: 1px solid rgba(0, 245, 212, 0.32);
    border-radius: 10px;
    background: rgba(15, 23, 42, 0.92);
    box-shadow: none;
    cursor: pointer;
  }

  .nav-toggle:hover {
    border-color: #00f5d4;
    background: rgba(15, 23, 42, 0.98);
    box-shadow: 0 0 14px rgba(0, 245, 212, 0.2);
  }

  .nav-toggle:focus-visible,
  .nav-link:focus-visible,
  .nav-logo:focus-visible {
    outline: 2px solid #00f5d4;
    outline-offset: 3px;
  }

  .nav-toggle span {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 22px;
    height: 2px;
    margin: 0;
    border-radius: 2px;
    background: #00f5d4;
    transform: translate(-50%, -50%);
    transition: transform 180ms ease, opacity 180ms ease;
  }

  .nav-toggle span:nth-child(1) {
    transform: translate(-50%, calc(-50% - 7px));
  }

  .nav-toggle span:nth-child(3) {
    transform: translate(-50%, calc(-50% + 7px));
  }

  .nav-toggle span.open:nth-child(1) {
    transform: translate(-50%, -50%) rotate(45deg);
  }

  .nav-toggle span.open:nth-child(2) {
    opacity: 0;
  }

  .nav-toggle span.open:nth-child(3) {
    transform: translate(-50%, -50%) rotate(-45deg);
  }

  @media (max-width: 800px) {
    .nav-container {
      min-height: 64px;
    }

    .nav-toggle {
      position: relative;
      display: inline-flex;
      flex-shrink: 0;
    }

    .nav-menu {
      position: absolute;
      top: calc(100% + 0.5rem);
      left: auto;
      right: 0;
      display: flex;
      flex-direction: column;
      align-items: stretch;
      gap: 0.25rem;
      width: min(340px, calc(100vw - 2rem), 100%);
      max-width: none;
      max-height: calc(100dvh - 100px);
      margin: 0;
      padding: 0.75rem;
      overflow-y: auto;
      border: 1px solid rgba(0, 245, 212, 0.2);
      border-radius: 14px;
      background: rgba(10, 15, 28, 0.98);
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.42);
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
      transform: translateY(-8px);
      transition:
        opacity 180ms ease,
        transform 180ms ease,
        visibility 180ms ease;
    }

    .nav-menu.active {
      opacity: 1;
      visibility: visible;
      pointer-events: auto;
      transform: translateY(0);
    }

    .nav-link {
      width: 100%;
      min-height: 48px;
      padding: 0.65rem 0.8rem;
      border-radius: 8px;
    }

    .nav-link:hover {
      background: rgba(0, 245, 212, 0.08);
      transform: none;
    }

  }

  @media (prefers-reduced-motion: reduce) {
    .nav-link,
    .nav-toggle span,
    .nav-menu {
      transition: none;
    }
  }
</style>
