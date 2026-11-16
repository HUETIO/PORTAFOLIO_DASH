<script>
  import "./lib/stylesGeneral.css";
  import PortfolioHighlights from "./PortfolioHighlights.svelte";
  import CardDetailButton from "./components/CardDetailButton.svelte";
  import CardDetailModal from "./components/CardDetailModal.svelte";
  import BusinessServices from "./BusinessServices.svelte";
  import BusinessDiscovery from "./BusinessDiscovery.svelte";
  import TeamExperienceSection from "./components/TeamExperienceSection.svelte";
  import EnterpriseReadinessSection from "./components/EnterpriseReadinessSection.svelte";
  import { tick } from 'svelte';
  import Header from "./Header.svelte";
  import Agent from "./Agent.svelte";
  import { clickOutside } from "./lib/clickOutside.js";
  import CinemaExperience from "./components/CinemaExperience.svelte";
  import CybersecuritySection from "./components/CybersecuritySection.svelte";
  import AISection from "./components/AISection.svelte";
  import SoftwareDevelopmentSection from "./components/SoftwareDevelopmentSection.svelte";
  import SocialMediaDiplomaSection from "./components/SocialMediaDiplomaSection.svelte";
  import ProjectBasedLearningSection from "./components/ProjectBasedLearningSection.svelte";
  import MobileAppDiplomaSection from "./components/MobileAppDiplomaSection.svelte";
  import TechnicalTrainingSection from "./components/TechnicalTrainingSection.svelte";
  import LocalCreativeAISection from "./components/LocalCreativeAISection.svelte";
  import DigitalAssetsBankingSection from "./components/DigitalAssetsBankingSection.svelte";
  import founderPortrait from "./assets/img/DSC_0106.JPG";
  import {
    Carousel as FlowbiteCarousel,
    CarouselIndicators,
    Controls,
  } from "flowbite-svelte";
  import Router from 'svelte-spa-router';
  import routes from './routes.js';
  import PaginaColor1 from './PaginaColor1.svelte';
  import PaginaColor2 from './PaginaColor2.svelte';
  import PaginaColor3 from './PaginaColor3.svelte';
  import PaginaColor4 from './PaginaColor4.svelte';
  import PaginaColor5 from './PaginaColor5.svelte';
  import PaginaColor6 from './PaginaColor6.svelte';

  let showBusinessDiscovery = false;
  let secondaryPortfolio;
  let portfolioWasOpen = false;
  let documentTitleBeforePrint = null;
  let isPreparingPrint = false;

  const toolkitImages = [
    {
      src: "https://media4.giphy.com/media/QpVUMRUJGokfqXyfa1/giphy.gif",
      title: "JavaScript",
      alt: "Animación representativa de JavaScript",
    },
    {
      src: "https://media3.giphy.com/media/pOEbLRT4SwD35IELiQ/giphy.gif",
      title: "Python",
      alt: "Animación representativa de Python",
    },
    {
      src: "https://media3.giphy.com/media/SSf1BUICbHfcBCybPd/giphy.gif",
      title: "DevOps",
      alt: "Animación representativa de DevOps",
    },
  ];

  function dragToScroll(node) {
    let activePointerId;
    let startX = 0;
    let startScrollLeft = 0;

    function handlePointerDown(event) {
      if (event.pointerType !== "mouse" || event.button !== 0) return;

      activePointerId = event.pointerId;
      startX = event.clientX;
      startScrollLeft = node.scrollLeft;
      node.setPointerCapture(event.pointerId);
    }

    function handlePointerMove(event) {
      if (event.pointerId !== activePointerId) return;
      node.scrollLeft = startScrollLeft - (event.clientX - startX);
    }

    function handlePointerEnd(event) {
      if (event.pointerId !== activePointerId) return;
      activePointerId = undefined;
    }

    function preventNativeDrag(event) {
      event.preventDefault();
    }

    node.addEventListener("pointerdown", handlePointerDown);
    node.addEventListener("pointermove", handlePointerMove);
    node.addEventListener("pointerup", handlePointerEnd);
    node.addEventListener("pointercancel", handlePointerEnd);
    node.addEventListener("lostpointercapture", handlePointerEnd);
    node.addEventListener("dragstart", preventNativeDrag);

    return {
      destroy() {
        node.removeEventListener("pointerdown", handlePointerDown);
        node.removeEventListener("pointermove", handlePointerMove);
        node.removeEventListener("pointerup", handlePointerEnd);
        node.removeEventListener("pointercancel", handlePointerEnd);
        node.removeEventListener("lostpointercapture", handlePointerEnd);
        node.removeEventListener("dragstart", preventNativeDrag);
      },
    };
  }

  function handleStackKeydown(event) {
    const distance = event.currentTarget.clientWidth * 0.8;

    if (event.key === "ArrowRight" || event.key === "ArrowLeft") {
      event.preventDefault();
      event.currentTarget.scrollBy({
        left: event.key === "ArrowRight" ? distance : -distance,
        behavior: "smooth",
      });
    } else if (event.key === "Home" || event.key === "End") {
      event.preventDefault();
      event.currentTarget.scrollTo({
        left: event.key === "Home" ? 0 : event.currentTarget.scrollWidth,
        behavior: "smooth",
      });
    }
  }

  function handleMouseOver(e, color) {
    const target = e.target;
    target.style.transform = "translateY(-3px)";
    target.style.boxShadow = `0 6px 25px rgba(0,0,0,0.4), 0 0 30px ${color}66`;
  }

  function handleMouseOut(e, color) {
    const target = e.target;
    target.style.transform = "translateY(0)";
    target.style.boxShadow = `0 4px 20px rgba(0,0,0,0.3), 0 0 20px ${color}44`;
  }

  const projects = [
    {
      number: "01",
      mark: "↗",
      category: "DASH.IO · AUTOMATIZACIÓN DOCUMENTAL",
      title: "¿Cuántas tareas manuales puedes eliminar?",
      challenge:
        "Documentos, validaciones y aprobaciones que consumen tiempo todos los días.",
      contribution:
        "DASH.IO conecta formularios, validaciones inteligentes y firma electrónica en flujos más ágiles.",
      outcome:
        "Menos pasos repetitivos, información mejor conectada y más tiempo para que tu equipo se enfoque en lo que importa.",
      skills: ["Automatización", "Gestión documental", "IA", "Integraciones"],
      accent: "#48e5c2",
    },
    {
      number: "02",
      mark: "✳",
      category: "DASH.IO · INTEGRACIONES INTELIGENTES",
      title: "¿Tus sistemas trabajan juntos?",
      challenge:
        "La información de clientes dispersa entre aplicaciones ralentiza al equipo y duplica tareas.",
      contribution:
        "DASH.IO conecta CRM, herramientas inteligentes y flujos de trabajo para que la información llegue donde hace falta.",
      outcome:
        "Procesos conectados, menos trabajo duplicado y un equipo con más contexto para atender a sus clientes.",
      skills: ["CRM", "Integraciones", "Automatización", "IA"],
      accent: "#7da8ff",
    },
  ];

  const colors = [
    "#00ffd5", // cian
    "#2196f3", // azul
    "#4caf50", // verde
    "#ff4081", // rosa
    "#ff9800", // naranja
    "#b626ff", // violeta
  ];

  const colorNames = [
    "Cian",
    "Azul",
    "Verde",
    "Rosa",
    "Naranja",
    "Violeta"
  ];

  const portfolioSections = [
    { name: 'Snake Mobile', description: 'Un clásico arcade con controles táctiles.', details: ['Juega desde una pantalla adaptada a dispositivos táctiles.', 'La experiencia reúne controles, estado de juego y reinicio en una misma interfaz.'], icon: '🐍' },
    { name: 'Memoria cósmica', description: 'Encuentra parejas y explora la galaxia.', details: ['Voltea cartas para encontrar símbolos coincidentes.', 'La experiencia muestra el avance y permite volver a empezar.'], icon: '✦' },
    { name: 'Laboratorio de color', description: 'Crea paletas y prueba el contraste.', details: ['Explora combinaciones de color y consulta sus valores.', 'Incluye herramientas para copiar códigos y revisar contraste.'], icon: '🎨' },
    { name: 'Windows UI Lab', description: 'Ventanas, mensajes y componentes interactivos.', details: ['Experimenta con controles y ventanas en una interfaz inspirada en escritorio.', 'Explora mensajes y acciones visuales sin salir del portafolio.'], icon: '▦' },
    { name: 'Raíz y Razón', description: 'Una revista digital sobre naturaleza y tecnología.', details: ['Formato editorial para presentar temas de naturaleza y tecnología.', 'Combina lectura y exploración visual dentro del portafolio.'], icon: '🌿' },
    { name: 'Ideas en movimiento', description: 'El proceso creativo detrás de DASH.IO.', details: ['Una experiencia visual que presenta ideas y el proceso creativo de la marca.', 'Explora el contenido interactivo sin salir de la página.'], icon: '✳' }
  ];

  const tabComponents = [
    PaginaColor1,
    PaginaColor2,
    PaginaColor3,
    PaginaColor4,
    PaginaColor5,
    PaginaColor6
  ];

  let activeTab = null;

  function openTab(idx) {
    activeTab = idx;
  }

  function closeExperienceWindow() {
    activeTab = null;
  }

  function handleExperienceWindowKeydown(event) {
    if (event.key === "Escape" && activeTab !== null) {
      closeExperienceWindow();
    }
  }

  function portal(node) {
    document.body.appendChild(node);

    return {
      destroy() {
        node.remove();
      },
    };
  }

  // Generar estilos dinámicos
  const styles = colors.map((color) => {
    // Función para invertir el color HEX
    const invertColor = (hex) => {
      const r = 255 - parseInt(hex.slice(1, 3), 16);
      const g = 255 - parseInt(hex.slice(3, 5), 16);
      const b = 255 - parseInt(hex.slice(5, 7), 16);
      return `rgb(${r}, ${g}, ${b})`;
    };

    const opposite = invertColor(color);

    return {
      background: `
      linear-gradient(135deg, 
        ${color} 0%, 
        rgba(${parseInt(color.slice(1, 3), 16)}, ${parseInt(color.slice(3, 5), 16)}, ${parseInt(color.slice(5, 7), 16)}, 0.8) 40%, 
        rgba(${opposite.match(/\d+/g).join(", ")}, 0.3) 70%, 
        ${opposite} 100%)
    `,
      color: "#fff",
      border: "none",
      padding: "12px 24px",
      borderRadius: "12px",
      fontSize: "1rem",
      fontWeight: "600",
      backdropFilter: "blur(4px)",
      boxShadow: `
      0 4px 20px rgba(0, 0, 0, 0.3),
      0 0 20px ${color}44,
      inset 0 0 2px ${opposite}22
    `,
      textShadow: "0 0 8px rgba(0,0,0,0.5)",
      transition: "all 0.3s ease",
      "&:hover": {
        transform: "translateY(-2px)",
        boxShadow: `
        0 6px 25px rgba(0, 0, 0, 0.4),
        0 0 30px ${color}66,
        inset 0 0 4px ${opposite}44
      `,
      },
    };
  });

  function goToColorPage(idx) {
    window.location.hash = `/color/${idx + 1}`;
  }

  async function startBusinessDiscovery() {
    showBusinessDiscovery = true;
    await tick();
    document.getElementById("business-discovery-section")?.scrollIntoView({
      behavior: "smooth",
      block: "start",
    });
  }

  function closeBusinessDiscovery() {
    showBusinessDiscovery = false;
  }

  function handleBeforePrint() {
    if (isPreparingPrint || !secondaryPortfolio) return;

    isPreparingPrint = true;
    portfolioWasOpen = secondaryPortfolio.open;
    documentTitleBeforePrint = document.title;
    secondaryPortfolio.open = true;
    document.title = "Portafolio-DASH";
  }

  function handleAfterPrint() {
    if (!isPreparingPrint || !secondaryPortfolio) return;

    secondaryPortfolio.open = portfolioWasOpen;
    document.title = documentTitleBeforePrint;
    documentTitleBeforePrint = null;
    isPreparingPrint = false;
  }

  function downloadPortfolio() {
    window.print();
  }
  
</script>

<svelte:window
  on:beforeprint={handleBeforePrint}
  on:afterprint={handleAfterPrint}
  on:keydown|capture={handleExperienceWindowKeydown}
/>

<Header />
<main>
  <!-- El asistente permanece disponible y cambia a footer al navegar o desplazarse. -->
  <Agent />
  <header id="inicio" class="hero animate company-hero">
    <div class="container-parr">
      <p class="eyebrow">DASH.IO · TECNOLOGÍA QUE IMPULSA TU EMPRESA</p>
      <h1>¿Cómo puede la tecnología hacer más fácil el día a día de tu equipo?</h1>
      <h2 class="dash-title">
        Con DASH.IO, conecta documentos, procesos y sistemas para que tu empresa avance con menos fricción.
      </h2>
      <p>
        Automatiza tareas, integra tus herramientas y libera a tu equipo para enfocarse en lo que hace crecer tu negocio.
      </p>

      <div class="hero-actions">
        <a class="hero-action hero-action--primary" href="#servicios">Descubre lo que DASH.IO puede transformar</a>
        <button
          class="hero-action hero-action--secondary"
          type="button"
          on:click={() => window.dispatchEvent(new CustomEvent("open-contact-agent"))}
        >Agendar conversación empresarial</button>
      </div>
    </div>
  </header>

  <section id="servicios" aria-label="Servicios profesionales">
    <BusinessServices onStartDiscovery={startBusinessDiscovery} />
  </section>

  {#if showBusinessDiscovery}
    <section
      id="business-discovery-section"
      class="banner full experience-section"
      aria-label="Descubrimiento de necesidades empresariales"
    >
      <BusinessDiscovery onBack={closeBusinessDiscovery} />
    </section>
  {/if}

  <section
    id="casos"
    class="banner full experience-section"
    aria-label="Soluciones para transformar procesos empresariales"
  >
    <PortfolioHighlights {projects} onStartDiscovery={startBusinessDiscovery} />
  </section>

  <TeamExperienceSection onStartDiscovery={startBusinessDiscovery} />

  <EnterpriseReadinessSection />

  <details class="secondary-portfolio" bind:this={secondaryPortfolio}>
    <summary id="trayectoria">
      <span class="lab-cta-icon" aria-hidden="true">✦</span>
      <span class="lab-cta-copy">
        <span class="lab-cta-eyebrow">INNOVACIÓN · APRENDIZAJE · CREATIVIDAD</span>
        <strong>Descubre las ideas detrás de DASH.IO</strong>
        <span>Experiencias digitales, tecnología y nuevas formas de resolver retos.</span>
      </span>
      <span class="lab-cta-action">
        <span class="lab-cta-open">Explorar ideas</span>
        <span class="lab-cta-close">Cerrar experiencias</span>
        <span class="lab-cta-arrow" aria-hidden="true">↗</span>
      </span>
    </summary>
    <div class="founder-story">
      <div class="founder-story-copy">
        <p class="founder-story-eyebrow">LA VISIÓN DE DASH.IO</p>
        <h2>Tecnología que trabaja mejor para las personas.</h2>
        <p>
          En DASH.IO unimos software, automatización e integración para convertir retos cotidianos en experiencias de trabajo más simples.
        </p>
      </div>
      <figure class="founder-portrait">
        <img
          src={founderPortrait}
          alt="Profesional creando soluciones tecnológicas"
          loading="lazy"
          decoding="async"
        />
        <figcaption>Ideas que impulsan DASH.IO</figcaption>
      </figure>
    </div>
    <section class="career-journey" aria-label="Trayectoria académica y técnica">
      <TechnicalTrainingSection />
    </section>

  <section id="herramientas" class="portfolio-toolkit" aria-label="Tecnologías para crear soluciones empresariales">
    <!-- Inicio del stack de container-->
      <div class="title-stack">
        <h2>Tecnología para impulsar nuevas soluciones</h2>
      </div>

      <ul class="toolkit-gallery" aria-label="Tecnologías destacadas">
        {#each toolkitImages as img}
          <li>
            <figure class="toolkit-image-card">
              <img src={img.src} alt={img.alt} loading="lazy" decoding="async" />
              <figcaption>{img.title}</figcaption>
            </figure>
          </li>
        {/each}
      </ul>
      <p>
        Combinamos herramientas modernas para diseñar productos digitales, conectar sistemas y simplificar procesos.
      </p>

      <!-- fin del stack de container-->

      <!-- svelte-ignore a11y_no_noninteractive_tabindex a11y_no_noninteractive_element_interactions -->
      <!-- Scrollable region stays keyboard-focusable for arrow-key navigation. -->
      <div
        class="stack-grid"
        role="region"
        aria-label="Categorías de tecnologías; desliza para explorar"
        tabindex="0"
        use:dragToScroll
        on:keydown={handleStackKeydown}
      >
        <!-- Backend -->
        <div class="stack-group">
          <strong>Backend</strong>
          <div class="icons">
            <img
              src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original-wordmark.svg"
              width="100"
              alt="Java"
            />
            <img
              src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"
              width="100"
              alt="Python"
            />
            <img
              src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg"
              width="100"
              alt="C++"
            />
            <img
              src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original-wordmark.svg"
              width="100"
              alt="Go"
            />
          </div>
        </div>
        <!-- Frontend -->
        <div class="stack-group">
          <strong>Frontend</strong>
          <div class="icons">
            <img
              src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg"
              width="100"
              alt="React"
            />
            <img
              src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/svelte/svelte-original.svg"
              width="100"
              alt="Svelte"
            />
            <img
              src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"
              width="100"
              alt="HTML5"
            />
            <img
              src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg"
              width="100"
              alt="CSS3"
            />
          </div>
        </div>
        <!-- Bases de datos -->
        <div class="stack-group">
          <strong>Bases de datos</strong>
          <div class="icons">
            <img
              src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original-wordmark.svg"
              width="100"
              alt="MySQL"
            />
            <img
              src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg"
              width="100"
              alt="PostgreSQL"
            />
            <img
              src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg"
              width="100"
              alt="SQLite"
            />
          </div>
        </div>
        <!-- Seguridad -->
        <div class="stack-group">
          <strong>Seguridad</strong>
          <div class="icons">
            <img
              src="https://raw.githubusercontent.com/devicons/devicon/master/icons/kalilinux/kalilinux-original.svg"
              width="100"
              alt="Kali Linux"
            />
            <img
              src="https://www.vectorlogo.zone/logos/wireshark/wireshark-icon.svg"
              width="100"
              alt="Wireshark"
            />
            <img
              src="https://www.vectorlogo.zone/logos/metasploit/metasploit-icon.svg"
              width="100"
              alt="Metasploit"
            />
          </div>
        </div>
        <!-- Herramientas -->
        <div class="stack-group">
          <strong>Herramientas</strong>
          <div class="icons">
            <img
              src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg"
              width="100"
              alt="Git"
            />
            <img
              src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/windows8/windows8-original.svg"
              width="100"
              alt="Windows"
            />
            <img
              src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg"
              width="100"
              alt="Docker"
            />
            <img
              src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/androidstudio/androidstudio-original.svg"
              width="100"
              alt="Android Studio"
            />
          </div>
        </div>
      </div>
      <!-- Inicio de mis mejores proyectos -->
      <div class="projects-section">
        <h2>🚀 Ideas digitales para llevar más lejos</h2>
        <ul class="project-list">
          <li>
            <a
              class="project-card"
              href="https://github.com/HUETIO/youtuber-downloader/releases/latest/download/Clipstream-Setup.exe"
              target="_blank"
              rel="noopener noreferrer"
              >📺 YouTuber Downloader <span class="project-status-badge project-status-badge--new">¡NUEVO!</span></a
            >
          </li>
          <li>
            <a
              class="project-card"
              href="https://github.com/HUETIO/logo-studio-ai/releases/latest/download/LogoStudioAI-Windows.zip"
              target="_blank"
              rel="noopener noreferrer"
              >🎨 Logo Studio AI <span class="project-status-badge project-status-badge--new">¡NUEVO!</span></a
            >
          </li>
          <li>
            <a
              class="project-card"
              href="https://github.com/HUETIO/pasar-datos-pc-android/releases/latest/download/Enviar-a-Android-Setup-1.0.0.exe"
              target="_blank"
              rel="noopener noreferrer"
              >📲 Pasar Datos PC a Android <span class="project-status-badge project-status-badge--new">¡NUEVO!</span></a
            >
          </li>
          <li>
            <button type="button" class="project-card project-coming-soon" disabled>
              <span class="project-status-badge project-status-badge--upcoming">PRÓXIMAMENTE</span>
              <span>🎵 OmniPlayer</span>
            </button>
          </li>
          <li>
            <button type="button" class="project-card project-coming-soon" disabled>
              <span class="project-status-badge project-status-badge--upcoming">PRÓXIMAMENTE</span>
              <span>🛠️ PRETUL</span>
            </button>
          </li>
          <li>
            <button type="button" class="project-card project-coming-soon" disabled>
              <span class="project-status-badge project-status-badge--upcoming">PRÓXIMAMENTE</span>
              <span>🤖 DASH.AI</span>
            </button>
          </li>
        </ul>
      </div>

      <!-- Final del table principal -->
  </section>

  <!-- TAB SYSTEM -->
  <div id="experiencias" class="color-tab-section">
    <header class="portfolio-heading">
      <div>
        <p class="portfolio-eyebrow">PORTAFOLIO INTERACTIVO</p>
        <h2>¿Qué podemos crear para tu empresa?</h2>
        <p class="portfolio-intro">Explora experiencias digitales, ideas y herramientas que muestran nuevas posibilidades.</p>
      </div>
      <span class="portfolio-count"><strong>06</strong> experiencias</span>
    </header>

    <div class="color-buttons" aria-label="Experiencias del portafolio">
      {#each portfolioSections as section, idx}
        <article
          class="experience-card"
          class:is-open={activeTab === idx}
          class:is-active={activeTab === idx}
          style={`--card-accent: ${colors[idx]}`}
        >
          <span class="experience-card-top">
            <span class="experience-number">0{idx + 1}</span>
            <span class="experience-icon" aria-hidden="true">{section.icon}</span>
          </span>
          <span class="experience-title">{section.name}</span>
          <span class="experience-description">{section.description}</span>
          <div class="experience-card-actions">
            <button type="button" class="experience-action" on:click={() => openTab(idx)}>
              {activeTab === idx ? 'Volver a explorar' : 'Explorar experiencia'}
              <span aria-hidden="true">↗</span>
            </button>
            <CardDetailButton
              title={section.name}
              description={section.description}
              details={section.details}
              accent={colors[idx]}
            />
          </div>
        </article>
      {/each}
    </div>

    {#if activeTab !== null}
      <div class="experience-window-backdrop" use:portal role="presentation">
        <dialog
          class="experience-window"
          open
          aria-modal="true"
          aria-labelledby="experience-window-title"
        >
          <header class="experience-window-header">
            <div>
              <p class="experience-window-eyebrow">PORTAFOLIO INTERACTIVO</p>
              <h2 id="experience-window-title">{portfolioSections[activeTab].name}</h2>
            </div>
            <button
              class="experience-window-close"
              type="button"
              aria-label="Cerrar experiencia"
              on:click={closeExperienceWindow}
            >×</button>
          </header>
          <nav class="experience-window-nav" aria-label="Selecciona una experiencia">
            {#each portfolioSections as section, idx}
              <button
                type="button"
                aria-pressed={activeTab === idx}
                class:active={activeTab === idx}
                on:click={() => openTab(idx)}
              >
                <span>0{idx + 1}</span>{section.name}
              </button>
            {/each}
          </nav>
          <div class="experience-window-content" class:is-snake={activeTab === 0}>
            {#key activeTab}
              <svelte:component this={tabComponents[activeTab]} color={colors[activeTab]} />
            {/key}
          </div>
        </dialog>
      </div>
    {/if}
  </div>

  <LocalCreativeAISection />

  <CybersecuritySection />

  <AISection />

  <SoftwareDevelopmentSection />

  <SocialMediaDiplomaSection />

  <ProjectBasedLearningSection />

  <MobileAppDiplomaSection />

  <DigitalAssetsBankingSection />

  <!-- Grid principal -->

  <div class="card-grid">
    <!-- Sobre mí -->
    <details id="about" class="about card animate">
      <summary>
        <img
          src="https://media.giphy.com/media/iY8CRBdQXODJSCERIr/giphy.gif"
          width="25"
          alt="Icono de información"
        />
        <strong>La visión detrás de DASH.IO</strong>
      </summary>
      <div class="content">
        <p>
          En DASH.IO creemos en una tecnología práctica, cercana y creada para hacer más sencillo el trabajo de las personas.
        </p>
        <p>
          Combinamos desarrollo de software, integración y automatización para convertir retos reales en soluciones digitales.
        </p>
        <p>
          Cada proyecto es una oportunidad para simplificar procesos y ayudar a las empresas a avanzar.
        </p>
        <CardDetailButton
          title="Lo que nos mueve"
          description="DASH.IO crea soluciones tecnológicas pensadas para hacer más sencillo el trabajo de las personas."
          details={["Software e integraciones para necesidades reales.", "Automatización que libera tiempo para lo que importa.", "Experiencias digitales creadas para ayudar a las empresas a avanzar."]}
        />
      </div>
    </details>

    <!-- Código en acción -->
    <section class="code-move card animate">
      <h2>💻 Ideas que se convierten en software</h2>
      <p>
        Creamos experiencias digitales que simplifican procesos y ayudan a las empresas a avanzar.
      </p>
      <img
        src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif"
        alt="Animación de código en cascada"
        width="100%"
      />
    </section>

    <!-- Construyendo proyectos -->
    <section class="building card animate">
      <h2>🔧 Innovación en movimiento</h2>
      <p>
        En DASH.IO exploramos nuevas formas de convertir tecnología emergente en herramientas útiles para las empresas.
      </p>
      <img
        src="https://media.giphy.com/media/juua9i2c2fA0AIp2iq/giphy.gif"
        alt="Animación de desarrollo de software"
        width="100%"
      />
      <CardDetailButton
        title="Innovación en movimiento"
        description="DASH.IO convierte nuevas ideas tecnológicas en herramientas prácticas para las empresas."
        details={["Seguimos creando experiencias para ayudar a proteger, automatizar y simplificar la operación digital."]}
      />
    </section>

    <!-- Soluciones reales -->
    <section class="solutions card animate">
      <h2>⚡ Tecnología que resuelve retos reales</h2>
      <p>
        Identificamos oportunidades, conectamos las piezas y desarrollamos soluciones claras para que tu empresa avance.
      </p>
      <img
        src="https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif"
        alt="Programador escribiendo código"
        width="100%"
      />
      <CardDetailButton
        title="Programando soluciones eficientes"
        description="El enfoque de trabajo comienza por entender el problema y diseñar una solución clara."
        details={["Identificar el problema y sus restricciones.", "Diseñar una arquitectura comprensible.", "Desarrollar con atención a la calidad y la mantenibilidad."]}
      />
    </section>
  </div>

  <CinemaExperience onStartDiscovery={startBusinessDiscovery} />
  </details>

  <!-- Contacto -->
  <div id="contact">
    <h2>¿Listo para hacer más con tu tecnología?</h2>
    <p>
      Cuéntanos qué quieres mejorar. En DASH.IO encontraremos contigo una forma clara de empezar.
    </p>
    <div
      class="contact-links"
      style="display: flex; gap: 16px; align-items: center;"
    >
      <!-- Email -->
      <a
        href="mailto:Develop1998@outlook.es"
        title="Enviar correo"
        style="text-decoration: none; color: inherit;"
      >
        <svg
          width="24"
          height="24"
          fill="currentColor"
          viewBox="0 0 24 24"
          style="vertical-align: middle;"
        >
          <path
            d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4-8 5-8-5V6l8 5 8-5v2z"
          />
        </svg>
        <span style="margin-left: 8px;">Inicia una conversación por correo</span>
      </a>
      <!-- LinkedIn -->
      <a
        href="https://www.linkedin.com/in/diegosepulveda"
        target="_blank"
        rel="noopener noreferrer"
        title="LinkedIn"
      >
        <svg
          width="24"
          height="24"
          fill="currentColor"
          viewBox="0 0 24 24"
          style="vertical-align: middle;"
        >
          <path
            d="M4.98 3.5C4.98 4.88 3.87 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1 4.98 2.12 4.98 3.5zM.5 8h4V24h-4V8zm7.5 0h3.6v2.2h.05c.5-.95 1.75-2.2 3.6-2.2 3.85 0 4.55 2.53 4.55 5.82V24h-4v-8.2c0-1.95-.03-4.45-2.7-4.45-2.7 0-3.1 2.1-3.1 4.3V24h-4V8z"
          />
        </svg>
        <span style="margin-left: 8px;">LinkedIn</span>
      </a>
      <!-- GitHub -->
      <a
        href="https://github.com/HUETIO"
        target="_blank"
        rel="noopener noreferrer"
        title="GitHub"
      >
        <svg
          width="24"
          height="24"
          fill="currentColor"
          viewBox="0 0 24 24"
          style="vertical-align: middle;"
        >
          <path
            d="M12 .5C5.73.5.5 5.73.5 12c0 5.08 3.29 9.39 7.86 10.92.58.11.79-.25.79-.56v-2.02c-3.2.7-3.87-1.54-3.87-1.54-.53-1.35-1.3-1.71-1.3-1.71-1.06-.72.08-.71.08-.71 1.17.08 1.78 1.2 1.78 1.2 1.04 1.78 2.73 1.27 3.4.97.11-.75.41-1.27.75-1.56-2.56-.29-5.26-1.28-5.26-5.7 0-1.26.45-2.29 1.2-3.1-.12-.29-.52-1.45.11-3.02 0 0 .98-.31 3.2 1.18a11.1 11.1 0 0 1 5.82 0c2.22-1.49 3.2-1.18 3.2-1.18.63 1.57.23 2.73.11 3.02.75.81 1.2 1.84 1.2 3.1 0 4.43-2.7 5.41-5.27 5.7.42.36.8 1.08.8 2.18v3.23c0 .31.21.68.8.56A10.5 10.5 0 0 0 23.5 12C23.5 5.73 18.27.5 12 .5z"
          />
        </svg>
        <span style="margin-left: 8px;">GitHub</span>
      </a>
    </div>
  </div>

  <!-- Footer -->
  <footer class="site-footer">
    <p>
      <small
        >DASH.IO · Tecnología que impulsa tu empresa</small
      >
    </p>
    <button
      class="portfolio-download"
      type="button"
      aria-label="Descargar portafolio en PDF"
      title="Descargar portafolio en PDF"
      on:click={downloadPortfolio}
    >
      <svg
        width="24"
        height="24"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
        aria-hidden="true"
      >
        <path d="M12 3v12m0 0 5-5m-5 5-5-5M4 17v4h16v-4" />
      </svg>
    </button>
  </footer>
  <Router {routes} />
  <CardDetailModal />
</main>

<style>
  .company-hero {
    margin-top: 80px;
    scroll-margin-top: 100px;
  }

  .company-hero .container-parr {
    max-width: 850px;
    text-align: center;
  }

  .company-hero .container-parr h1 {
    font-size: clamp(2rem, 4vw, 3rem);
    line-height: 1.15;
  }

  .company-hero .container-parr > p {
    max-width: 740px;
    margin-inline: auto;
  }

  .hero-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 0.8rem;
    margin-top: 1.5rem;
  }

  .hero-action {
    display: inline-flex;
    min-height: 46px;
    align-items: center;
    justify-content: center;
    padding: 0.7rem 1rem;
    border: 1px solid rgba(0, 245, 212, 0.45);
    border-radius: 12px;
    color: #f7f5ff;
    font: inherit;
    font-weight: 700;
    text-decoration: none;
    cursor: pointer;
    transition: transform 180ms ease, background 180ms ease, border-color 180ms ease;
  }

  .hero-action:hover {
    transform: translateY(-2px);
    border-color: #00f5d4;
  }

  .hero-action--primary {
    background: #00bfa7;
    color: #071413;
  }

  .hero-action--secondary {
    background: rgba(0, 245, 212, 0.06);
  }

  .hero-action:focus-visible {
    outline: 2px solid #00f5d4;
    outline-offset: 3px;
  }

  @media (max-width: 600px) {
    .company-hero .container-parr > .eyebrow {
      font-size: clamp(0.7rem, 2.8vw, 0.78rem);
      letter-spacing: 0.12em;
      line-height: 1.4;
    }

    .company-hero .container-parr h1 {
      font-size: clamp(1.75rem, 7.5vw, 2.25rem);
      line-height: 1.12;
    }

    .company-hero .container-parr .dash-title {
      font-size: clamp(1rem, 4vw, 1.15rem);
      letter-spacing: 0.04em;
      line-height: 1.5;
    }

    .company-hero .container-parr > p:not(.eyebrow) {
      font-size: clamp(0.9rem, 3.6vw, 1rem);
      line-height: 1.6;
    }
  }

  .experience-section {
    margin-top: 0;
    scroll-margin-top: 80px;
  }

  .secondary-portfolio {
    position: relative;
    isolation: isolate;
    padding: 1.5rem 1rem;
    border: 1px solid rgba(126, 111, 255, 0.28);
    border-radius: 1.25rem;
    background:
      radial-gradient(ellipse at 12% 0%, rgba(120, 92, 255, 0.15), transparent 34rem),
      radial-gradient(ellipse at 88% 100%, rgba(0, 245, 212, 0.1), transparent 32rem),
      linear-gradient(145deg, rgba(24, 21, 44, 0.88), rgba(11, 13, 23, 0.94));
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.2);
    transition: border-color 220ms ease, box-shadow 220ms ease, background-color 220ms ease;
  }

  .founder-story {
    display: grid;
    grid-template-columns: minmax(0, 1fr) auto;
    align-items: center;
    gap: clamp(1.5rem, 5vw, 4rem);
    width: min(1120px, 100%);
    margin: 1.75rem auto 0;
    padding: clamp(1.25rem, 4vw, 2.5rem);
    border: 1px solid rgba(195, 173, 255, 0.18);
    border-radius: 1.25rem;
    background: linear-gradient(120deg, rgba(166, 135, 255, 0.08), rgba(0, 245, 212, 0.04));
  }

  .founder-story-copy {
    max-width: 680px;
  }

  .founder-story-eyebrow {
    margin: 0 0 0.75rem;
    color: #7cebd9;
    font-size: 0.68rem;
    font-weight: 750;
    letter-spacing: 0.14em;
  }

  .founder-story-copy h2 {
    margin: 0;
    color: #f0edff;
    font-size: clamp(1.35rem, 3vw, 2rem);
    line-height: 1.2;
  }

  .founder-story-copy > p:last-child {
    max-width: 62ch;
    margin: 0.85rem 0 0;
    color: #c5c2d2;
    font-size: 0.92rem;
    line-height: 1.7;
  }

  .founder-portrait {
    width: min(220px, 28vw);
    margin: 0;
    padding: 5px;
    border: 1px solid rgba(124, 235, 217, 0.62);
    border-radius: 1.2rem;
    background: linear-gradient(145deg, rgba(0, 245, 212, 0.3), rgba(166, 135, 255, 0.38));
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.26), 0 0 24px rgba(0, 245, 212, 0.08);
  }

  .founder-portrait img {
    display: block;
    width: 100%;
    aspect-ratio: 4 / 5;
    border-radius: 0.9rem;
    object-fit: cover;
    object-position: 42% 38%;
  }

  .founder-portrait figcaption {
    padding: 0.65rem 0.25rem 0.25rem;
    color: #c8fff5;
    font-size: 0.72rem;
    font-weight: 650;
    text-align: center;
  }

  .secondary-portfolio > summary {
    display: grid;
    grid-template-columns: 3.5rem minmax(0, 1fr) auto;
    grid-template-areas: "icon copy action";
    width: min(1120px, 100%);
    min-height: 112px;
    align-items: center;
    gap: 1.1rem;
    margin: 0 auto;
    padding: 1.1rem 1.25rem;
    border: 1px solid rgba(0, 245, 212, 0.38);
    border-radius: 1rem;
    background:
      radial-gradient(ellipse at 0% 50%, rgba(0, 245, 212, 0.16), transparent 55%),
      linear-gradient(110deg, rgba(0, 245, 212, 0.1), rgba(174, 123, 255, 0.12) 65%, rgba(16, 25, 38, 0.7));
    color: #f0edff;
    cursor: pointer;
    list-style: none;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.2), 0 0 26px rgba(0, 245, 212, 0.08);
    transition: border-color 200ms ease, background 200ms ease, transform 200ms ease, box-shadow 200ms ease;
  }

  .secondary-portfolio > summary::-webkit-details-marker {
    display: none;
  }

  .lab-cta-icon {
    display: grid;
    grid-area: icon;
    width: 3.5rem;
    aspect-ratio: 1;
    place-items: center;
    border: 1px solid rgba(0, 245, 212, 0.42);
    border-radius: 1rem;
    background: linear-gradient(145deg, rgba(0, 245, 212, 0.2), rgba(174, 123, 255, 0.22));
    color: #9ffff0;
    font-size: 1.7rem;
    box-shadow: inset 0 0 18px rgba(0, 245, 212, 0.1);
  }

  .lab-cta-copy {
    display: grid;
    grid-area: copy;
    gap: 0.2rem;
    min-width: 0;
  }

  .lab-cta-eyebrow {
    color: #9ffff0;
    font-size: 0.68rem;
    font-weight: 800;
    letter-spacing: 0.12em;
  }

  .lab-cta-copy strong {
    color: #fff;
    font-size: clamp(1rem, 2.4vw, 1.25rem);
    line-height: 1.35;
  }

  .lab-cta-copy > span:last-child {
    color: #cbd5e1;
    font-size: 0.9rem;
    line-height: 1.45;
  }

  .lab-cta-action {
    display: inline-flex;
    grid-area: action;
    min-height: 46px;
    align-items: center;
    justify-content: center;
    gap: 0.65rem;
    padding: 0.65rem 0.9rem;
    border: 1px solid rgba(0, 245, 212, 0.5);
    border-radius: 999px;
    background: linear-gradient(110deg, rgba(0, 245, 212, 0.2), rgba(174, 123, 255, 0.22));
    color: #c8fff5;
    font-size: 0.82rem;
    font-weight: 800;
    white-space: nowrap;
    transition: background 200ms ease, color 200ms ease, transform 200ms ease;
  }

  .lab-cta-close {
    display: none;
  }

  .lab-cta-arrow {
    font-size: 1.05rem;
    transition: transform 200ms ease;
  }

  .secondary-portfolio > summary:hover {
    border-color: rgba(0, 245, 212, 0.75);
    background:
      radial-gradient(ellipse at 0% 50%, rgba(0, 245, 212, 0.22), transparent 55%),
      linear-gradient(110deg, rgba(0, 245, 212, 0.16), rgba(174, 123, 255, 0.2) 65%, rgba(16, 25, 38, 0.75));
    box-shadow: 0 16px 38px rgba(0, 0, 0, 0.3), 0 0 32px rgba(0, 245, 212, 0.14);
    transform: translateY(-2px);
  }

  .secondary-portfolio > summary:hover .lab-cta-action {
    background: linear-gradient(110deg, rgba(0, 245, 212, 0.28), rgba(174, 123, 255, 0.32));
    color: #fff;
  }

  .secondary-portfolio > summary:hover .lab-cta-arrow {
    transform: translate(2px, -2px);
  }

  .secondary-portfolio > summary:focus-visible {
    outline: 2px solid #00f5d4;
    outline-offset: 5px;
  }

  .secondary-portfolio[open] {
    border-color: rgba(0, 245, 212, 0.42);
    box-shadow: 0 16px 42px rgba(65, 51, 130, 0.2), 0 0 24px rgba(0, 245, 212, 0.07);
  }

  .secondary-portfolio[open] > summary .lab-cta-open {
    display: none;
  }

  .secondary-portfolio[open] > summary .lab-cta-close {
    display: inline;
  }

  .secondary-portfolio[open] > summary .lab-cta-arrow {
    transform: rotate(45deg);
  }

  .secondary-portfolio[open] > :not(summary) {
    animation: lab-content-enter 420ms ease both;
  }

  .secondary-portfolio[open] > :nth-child(3) {
    animation-delay: 50ms;
  }

  .secondary-portfolio[open] > :nth-child(4) {
    animation-delay: 100ms;
  }

  .secondary-portfolio[open] > :nth-child(5) {
    animation-delay: 150ms;
  }

  .secondary-portfolio[open] > :nth-child(n + 6) {
    animation-delay: 200ms;
  }

  @keyframes lab-content-enter {
    from {
      opacity: 0.75;
      transform: translateY(8px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  @media (max-width: 560px) {
    .secondary-portfolio > summary {
      grid-template-columns: 2.9rem minmax(0, 1fr);
      grid-template-areas:
        "icon copy"
        "action action";
      gap: 0.85rem;
      min-height: 0;
      padding: 1rem;
    }

    .lab-cta-icon {
      width: 2.9rem;
      border-radius: 0.85rem;
      font-size: 1.4rem;
    }

    .lab-cta-eyebrow {
      font-size: 0.62rem;
    }

    .lab-cta-copy strong {
      font-size: 1rem;
    }

    .lab-cta-copy > span:last-child {
      font-size: 0.82rem;
    }

    .lab-cta-action {
      width: 100%;
      min-height: 48px;
    }

    .founder-story {
      grid-template-columns: 1fr;
    }

    .founder-portrait {
      width: min(220px, 72vw);
      justify-self: center;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .secondary-portfolio > summary,
    .lab-cta-arrow,
    .lab-cta-action,
    .secondary-portfolio[open] > :not(summary) {
      animation: none;
      transition: none;
    }
  }

  .career-journey,
  #servicios,
  #experiencias,
  #contact {
    scroll-margin-top: 80px;
  }

  .portfolio-toolkit {
    padding: clamp(2rem, 5vw, 4rem) 1rem;
  }

  .toolkit-gallery {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: clamp(1rem, 3vw, 2rem);
    width: min(1120px, 100%);
    margin: 2rem auto;
    padding: 0;
    list-style: none;
  }

  .toolkit-gallery li {
    min-width: 0;
  }

  .toolkit-image-card {
    position: relative;
    aspect-ratio: 16 / 10;
    overflow: hidden;
    margin: 0;
    border: 1px solid rgba(148, 163, 184, 0.28);
    border-radius: 22px;
    background: #101827;
    box-shadow: 0 18px 38px rgba(0, 0, 0, 0.3);
    isolation: isolate;
    transition: transform 220ms ease, border-color 220ms ease, box-shadow 220ms ease;
  }

  .toolkit-image-card::after {
    position: absolute;
    z-index: 1;
    inset: 35% 0 0;
    background: linear-gradient(transparent, rgba(5, 10, 20, 0.88));
    content: "";
    pointer-events: none;
  }

  .toolkit-image-card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: saturate(0.82);
    transition: transform 500ms ease, filter 500ms ease;
  }

  .toolkit-image-card figcaption {
    position: absolute;
    z-index: 2;
    right: 1rem;
    bottom: 1rem;
    left: 1rem;
    color: #f4f7fb;
    font-size: 1rem;
    font-weight: 700;
    letter-spacing: 0.04em;
  }

  .toolkit-image-card:hover {
    transform: translateY(-6px);
    border-color: rgba(0, 245, 212, 0.72);
    box-shadow: 0 22px 44px rgba(0, 0, 0, 0.42), 0 0 24px rgba(0, 245, 212, 0.12);
  }

  .toolkit-image-card:hover img {
    transform: scale(1.06);
    filter: saturate(1.08);
  }

  @media (max-width: 720px) {
    .toolkit-gallery {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }

  @media (max-width: 480px) {
    .toolkit-gallery {
      grid-template-columns: 1fr;
      max-width: 420px;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .toolkit-image-card,
    .toolkit-image-card img {
      transition: none;
    }
  }

  .color-tab-section {
    width: min(1120px, calc(100% - 2rem));
    margin: 3rem auto;
    padding: clamp(1.25rem, 3vw, 2.25rem);
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-radius: 28px;
    background:
      radial-gradient(ellipse at 5% 0%, rgba(0, 245, 212, 0.09), transparent 42%),
      rgba(8, 13, 24, 0.78);
    box-shadow: 0 24px 70px rgba(0, 0, 0, 0.28);
    backdrop-filter: blur(18px);
  }

  .experience-window-backdrop {
    position: fixed;
    z-index: 3200;
    inset: 0;
    display: grid;
    place-items: center;
    padding: 1rem;
    background: rgba(3, 7, 16, 0.78);
    backdrop-filter: blur(10px);
    overscroll-behavior: contain;
  }

  .experience-window {
    position: relative;
    display: flex;
    width: min(1120px, 100%);
    height: min(88vh, 900px);
    height: min(88dvh, 900px);
    margin: 0;
    padding: 0;
    min-width: 0;
    min-height: 0;
    flex-direction: column;
    overflow: hidden;
    border: 1px solid rgba(148, 163, 184, 0.24);
    border-radius: 22px;
    background: #0b1220;
    color: #f4f7fb;
    box-shadow: 0 24px 80px rgba(0, 0, 0, 0.55);
  }

  .experience-window-header {
    display: flex;
    flex: 0 0 auto;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    padding: 1rem 1.25rem;
    border-bottom: 1px solid rgba(148, 163, 184, 0.16);
  }

  .experience-window-eyebrow {
    margin: 0 0 0.2rem;
    color: #00f5d4;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.14em;
  }

  .experience-window-header h2 {
    margin: 0;
    font-size: clamp(1.05rem, 2.5vw, 1.45rem);
    line-height: 1.25;
  }

  .experience-window-close {
    display: grid;
    width: 40px;
    height: 40px;
    flex: 0 0 auto;
    padding: 0;
    place-items: center;
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.06);
    color: #fff;
    font-size: 1.5rem;
    line-height: 1;
    cursor: pointer;
  }

  .experience-window-nav {
    display: flex;
    flex: 0 0 auto;
    gap: 0.5rem;
    padding: 0.75rem 1rem;
    overflow-x: auto;
    border-bottom: 1px solid rgba(148, 163, 184, 0.16);
    scrollbar-width: thin;
  }

  .experience-window-nav button {
    display: inline-flex;
    min-height: 40px;
    flex: 0 0 auto;
    align-items: center;
    gap: 0.45rem;
    padding: 0.45rem 0.75rem;
    border: 1px solid rgba(148, 163, 184, 0.16);
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.04);
    color: #cbd5e1;
    font-size: 0.76rem;
    cursor: pointer;
  }

  .experience-window-nav button span {
    color: #7cebd9;
    font-size: 0.66rem;
    font-weight: 700;
  }

  .experience-window-nav button.active {
    border-color: rgba(0, 245, 212, 0.55);
    background: rgba(0, 245, 212, 0.1);
    color: #fff;
  }

  .experience-window-content {
    min-width: 0;
    min-height: 0;
    flex: 1 1 auto;
    padding: clamp(0.5rem, 2vw, 1.25rem);
    overflow: auto;
    overscroll-behavior: contain;
  }

  .experience-window-content.is-snake {
    display: flex;
    overflow: hidden;
  }

  .experience-window-content :global(.snake-page) {
    width: 100%;
    height: 100%;
    flex: 1 1 auto;
    min-height: 0;
    margin: 0;
    padding: 0;
  }

  .experience-window-content.is-snake :global(.snake-card) {
    width: 100%;
    height: 100%;
    max-width: none;
    align-items: stretch;
  }

  .experience-window-content :global(.snake-card),
  .experience-window-content :global(.snake-card.desktop) {
    display: flex;
    width: min(100%, 520px);
    max-width: 520px;
    flex-direction: column;
    align-items: center;
  }

  .experience-window-content :global(.snake-card.desktop .info-panel),
  .experience-window-content :global(.snake-card.desktop .control-panel) {
    width: 100%;
    justify-self: stretch;
    text-align: center;
  }

  .portfolio-heading {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 1.5rem;
  }

  .portfolio-eyebrow {
    margin: 0 0 0.35rem;
    color: #00f5d4;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.16em;
  }

  .portfolio-heading h2 {
    margin: 0;
    color: #f4f7fb;
    font-size: clamp(1.6rem, 3vw, 2.25rem);
    line-height: 1.2;
  }

  .portfolio-intro {
    margin: 0.55rem 0 0;
    color: #aab5c5;
    font-size: 0.95rem;
  }

  .portfolio-count {
    flex: 0 0 auto;
    padding: 0.45rem 0.8rem;
    border: 1px solid rgba(148, 163, 184, 0.2);
    border-radius: 999px;
    color: #aab5c5;
    font-size: 0.78rem;
  }

  .portfolio-count strong {
    margin-right: 0.3rem;
    color: #f4f7fb;
  }

  .color-buttons {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
  }

  .experience-card {
    display: flex;
    min-width: 0;
    min-height: 190px;
    flex-direction: column;
    align-items: flex-start;
    padding: 1.15rem 1.25rem;
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-radius: 20px;
    background: linear-gradient(145deg, rgba(255, 255, 255, 0.075), rgba(255, 255, 255, 0.025));
    color: #f4f7fb;
    text-align: left;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.04);
    transition: transform 180ms ease, border-color 180ms ease, background 180ms ease, box-shadow 180ms ease;
  }

  .experience-card:hover,
  .experience-card.is-open {
    transform: translateY(-3px);
    border-color: color-mix(in srgb, var(--card-accent), transparent 35%);
    color: #f4f7fb;
    box-shadow: 0 14px 34px rgba(0, 0, 0, 0.25), 0 0 22px color-mix(in srgb, var(--card-accent), transparent 85%);
  }

  .experience-card.is-active {
    border-color: var(--card-accent);
    background: linear-gradient(145deg, color-mix(in srgb, var(--card-accent), transparent 88%), rgba(255, 255, 255, 0.04));
    box-shadow: 0 0 0 1px color-mix(in srgb, var(--card-accent), transparent 55%), 0 14px 34px rgba(0, 0, 0, 0.25);
  }

  .experience-card:focus-visible {
    outline: 2px solid var(--card-accent);
    outline-offset: 3px;
  }

  .experience-card-actions {
    display: flex;
    width: 100%;
    align-items: center;
    justify-content: space-between;
    gap: 0.5rem;
    margin-top: auto;
  }

  .experience-card-top {
    display: flex;
    width: 100%;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1rem;
  }

  .experience-number {
    color: color-mix(in srgb, var(--card-accent), white 12%);
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.12em;
  }

  .experience-icon {
    display: grid;
    width: 2.5rem;
    height: 2.5rem;
    place-items: center;
    border: 1px solid color-mix(in srgb, var(--card-accent), transparent 65%);
    border-radius: 13px;
    background: color-mix(in srgb, var(--card-accent), transparent 90%);
    font-size: 1.25rem;
  }

  .experience-title {
    font-size: 1.08rem;
    font-weight: 700;
    line-height: 1.35;
  }

  .experience-description {
    margin-top: 0.35rem;
    color: #aab5c5;
    font-size: 0.84rem;
    font-weight: 400;
    line-height: 1.5;
  }

  .experience-action {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0;
    color: color-mix(in srgb, var(--card-accent), white 15%);
    border: 0;
    background: transparent;
    font: inherit;
    font-size: 0.78rem;
    font-weight: 600;
    text-align: left;
    cursor: pointer;
  }

  .experience-card-actions :global(.card-detail-trigger) {
    flex: 0 0 auto;
    width: 2.2rem;
    margin-top: 0;
    padding: 0;
    font-size: 1.15rem;
  }

  .experience-action span {
    font-size: 1rem;
    transition: transform 180ms ease;
  }

  .experience-card:hover .experience-action span {
    transform: translate(2px, -2px);
  }

  .site-footer {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.75rem;
  }

  .portfolio-download {
    display: inline-grid;
    width: 44px;
    height: 44px;
    padding: 0;
    place-items: center;
    color: var(--accent, #00f5d4);
    border: 0;
    border-radius: 0.5rem;
    background: transparent;
    cursor: pointer;
    transition: color 180ms ease, transform 180ms ease;
  }

  .portfolio-download:hover {
    color: #60a5fa;
    transform: translateY(-2px);
  }

  .portfolio-download:focus-visible {
    outline: 2px solid currentColor;
    outline-offset: 3px;
  }

  @page {
    size: A4 portrait;
    margin: 12mm;
  }

  @media print {
    :global(html),
    :global(body) {
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
      background: #0a0a0a !important;
      color: #f7f5ff !important;
    }

    :global(body::before),
    :global(.site-header),
    :global(.agent-launcher-slot),
    :global(.agent-modal),
    :global(.details-backdrop),
    :global(.details-dialog),
    .portfolio-download {
      display: none !important;
    }

    :global(body),
    :global(body *) {
      animation: none !important;
      transition: none !important;
      scroll-behavior: auto !important;
    }

    main {
      margin: 0 !important;
      padding: 0 !important;
    }

    .company-hero {
      margin-top: 0 !important;
    }

    .secondary-portfolio {
      break-before: page;
    }

    img {
      max-width: 100% !important;
      print-color-adjust: exact;
      -webkit-print-color-adjust: exact;
    }
  }

  @media (max-width: 760px) {
    .color-buttons {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .experience-card {
      min-height: 180px;
    }
  }

  @media (max-width: 520px) {
    .color-tab-section {
      width: min(100% - 1rem, 1120px);
      margin: 2rem auto;
      border-radius: 22px;
    }

    .portfolio-heading {
      align-items: flex-start;
      flex-direction: column;
    }

    .color-buttons {
      grid-template-columns: 1fr;
      gap: 0.75rem;
    }

    .experience-card {
      min-height: 168px;
    }

    .experience-window-backdrop {
      padding: 0.5rem;
    }

    .experience-window {
      width: 100%;
      height: calc(100vh - 1rem);
      height: calc(100dvh - 1rem);
      border-radius: 16px;
    }

    .experience-window-header {
      padding: 0.75rem;
    }

    .experience-window-nav {
      gap: 0.4rem;
      padding: 0.6rem 0.65rem;
    }

    .experience-window-nav button {
      min-height: 38px;
      padding: 0.4rem 0.65rem;
      font-size: 0.72rem;
    }

    .experience-window-content {
      padding: 0.5rem;
    }

    .experience-window-content.is-snake {
      padding: 0.5rem;
    }

    .experience-window-content :global(.color-lab) {
      min-height: 0;
      padding: 0.5rem;
    }

    .experience-window-content :global(.color-lab .lab-shell),
    .experience-window-content :global(.color-lab .workspace),
    .experience-window-content :global(.color-lab .color-card),
    .experience-window-content :global(.color-lab .contrast-card),
    .experience-window-content :global(.color-lab .palette-section) {
      width: 100%;
      min-width: 0;
    }

    .experience-window-content :global(.color-lab .workspace) {
      grid-template-columns: minmax(0, 1fr);
      gap: 0.75rem;
    }

    .experience-window-content :global(.color-lab .color-card),
    .experience-window-content :global(.color-lab .contrast-card),
    .experience-window-content :global(.color-lab .palette-section) {
      padding: 0.75rem;
    }

    .experience-window-content :global(.color-lab .color-preview) {
      min-height: clamp(140px, 22vh, 180px);
      padding: 1rem;
    }

    .experience-window-content :global(.color-lab .input-row),
    .experience-window-content :global(.color-lab .hex-field) {
      min-width: 0;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .experience-card,
    .experience-action span {
      transition: none;
    }
  }

</style>
