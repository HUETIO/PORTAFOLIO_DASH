<script>
  export let onStartDiscovery = () => {};

  import { onMount } from "svelte";
  import { fade } from "svelte/transition";
  import {
    getMovieDetails,
    getMovieGenres,
    getMovies,
    getMovieImage,
  } from "../lib/movieService.js";

  const categories = [
    { id: "now_playing", label: "En cartelera", icon: "◉" },
    { id: "upcoming", label: "Próximamente", icon: "✦" },
    { id: "popular", label: "Más populares", icon: "↗" },
  ];

  let movies = [];
  let genres = [];
  let category = "now_playing";
  let selectedGenre = "";
  let searchInput = "";
  let activeQuery = "";
  let currentPage = 1;
  let totalPages = 1;
  let loading = true;
  let loadingMore = false;
  let error = "";
  let selectedMovie = null;
  let movieDetails = null;
  let loadingDetails = false;
  let detailError = "";
  let favorites = [];
  let showFavorites = false;
  let requestVersion = 0;

  $: featuredMovie = movies.find((movie) => movie.backdrop_path) || movies[0];
  $: visibleMovies = showFavorites ? favorites : movies;
  $: selectedTrailer = movieDetails?.videos?.results?.find(
    (video) => video.site === "YouTube" && video.type === "Trailer" && video.iso_639_1 === "es",
  ) || movieDetails?.videos?.results?.find(
    (video) => video.site === "YouTube" && video.type === "Trailer",
  );
  $: movieCast = movieDetails?.credits?.cast?.slice(0, 5) || [];
  $: movieCertification = movieDetails?.release_dates?.results
    ?.find((release) => release.iso_3166_1 === "CO")
    ?.release_dates?.find((release) => release.certification)?.certification;

  function portal(node) {
    document.body.appendChild(node);

    return {
      destroy() {
        node.remove();
      },
    };
  }

  onMount(() => {
    try {
      const savedFavorites = localStorage.getItem("dash-cinema-favorites");
      if (savedFavorites) {
        const parsedFavorites = JSON.parse(savedFavorites);
        if (Array.isArray(parsedFavorites)) {
          favorites = parsedFavorites.filter((movie) => movie && Number.isInteger(movie.id));
        }
      }
    } catch (storageError) {
      console.warn("No se pudo recuperar Mi lista de cine.", storageError);
    }

    loadGenres();
    loadMovies();
  });

  async function loadGenres() {
    try {
      genres = await getMovieGenres();
    } catch (loadError) {
      console.error("No se pudieron cargar los géneros de TMDB.", loadError);
    }
  }

  async function loadMovies({ append = false } = {}) {
    const version = ++requestVersion;
    const page = append ? currentPage + 1 : 1;
    loading = !append;
    loadingMore = append;
    error = "";

    try {
      const result = await getMovies({
        category,
        page,
        query: activeQuery,
        genreId: selectedGenre,
      });

      if (version !== requestVersion) return;

      movies = append ? [...movies, ...result.results] : result.results;
      currentPage = result.page;
      totalPages = result.total_pages;
    } catch (loadError) {
      if (version !== requestVersion) return;
      error = loadError.message || "No fue posible cargar la cartelera.";
      console.error("No se pudo cargar la cartelera de TMDB.", loadError);
    } finally {
      if (version === requestVersion) {
        loading = false;
        loadingMore = false;
      }
    }
  }

  function chooseCategory(nextCategory) {
    category = nextCategory;
    activeQuery = "";
    searchInput = "";
    selectedGenre = "";
    showFavorites = false;
    loadMovies();
  }

  function submitSearch() {
    activeQuery = searchInput.trim();
    selectedGenre = "";
    showFavorites = false;
    loadMovies();
  }

  function clearSearch() {
    searchInput = "";
    activeQuery = "";
    loadMovies();
  }

  function chooseGenre(genreId) {
    selectedGenre = selectedGenre === String(genreId) ? "" : String(genreId);
    activeQuery = "";
    searchInput = "";
    showFavorites = false;
    loadMovies();
  }

  function toggleFavoritesView() {
    showFavorites = !showFavorites;
    if (showFavorites) {
      activeQuery = "";
      searchInput = "";
      selectedGenre = "";
    }
  }

  async function openMovie(movie) {
    const movieId = movie.id;
    selectedMovie = movie;
    movieDetails = null;
    detailError = "";
    loadingDetails = true;

    try {
      const details = await getMovieDetails(movieId);
      if (selectedMovie?.id === movieId) movieDetails = details;
    } catch (detailsError) {
      console.error(`No se pudieron cargar los detalles de ${movie.title}.`, detailsError);
      if (selectedMovie?.id === movieId) {
        detailError = "No fue posible obtener todos los detalles en este momento.";
      }
    } finally {
      if (selectedMovie?.id === movieId) loadingDetails = false;
    }
  }

  function closeMovie() {
    selectedMovie = null;
    movieDetails = null;
  }

  function handleWindowKeydown(event) {
    if (event.key === "Escape") closeMovie();
  }

  function isFavorite(movieId) {
    return favorites.some((movie) => movie.id === movieId);
  }

  function toggleFavorite(movie) {
    favorites = isFavorite(movie.id)
      ? favorites.filter((savedMovie) => savedMovie.id !== movie.id)
      : [...favorites, movie];

    try {
      localStorage.setItem("dash-cinema-favorites", JSON.stringify(favorites));
    } catch (storageError) {
      console.error("No se pudo guardar Mi lista de cine.", storageError);
    }
  }

  function formatReleaseDate(date) {
    if (!date) return "Fecha por confirmar";
    return new Intl.DateTimeFormat("es-CO", {
      day: "numeric",
      month: "long",
      year: "numeric",
      timeZone: "UTC",
    }).format(new Date(`${date}T00:00:00Z`));
  }
</script>

<svelte:window on:keydown={handleWindowKeydown} />

<section class="cinema" aria-labelledby="cinema-title">
  <div class="cinema-shell">
    <header class="cinema-heading">
      <div>
        <p class="eyebrow"><span class="live-dot"></span> TU PRÓXIMA HISTORIA EMPIEZA AQUÍ</p>
        <h2 id="cinema-title">Una cartelera para <span>compartir.</span></h2>
        <p class="heading-copy">
          Descubre qué ver, conoce los próximos estrenos y arma el plan perfecto para disfrutar
          con tu familia.
        </p>
      </div>
      <a class="tmdb-credit" href="https://www.themoviedb.org/" target="_blank" rel="noopener noreferrer">
        <span aria-hidden="true">✦</span>
        Cine para explorar
        <small>Información actualizada con TMDB</small>
      </a>
    </header>

    {#if featuredMovie}
      <section
        class="featured"
        style={`--featured-image: url("${getMovieImage(featuredMovie.backdrop_path, "w1280") || getMovieImage(featuredMovie.poster_path, "w780")}")`}
        aria-label={`Película destacada: ${featuredMovie.title}`}
      >
        <div class="featured-copy">
          <span class="featured-label">RECOMENDADA PARA TU PRÓXIMA SALIDA</span>
          <h3>{featuredMovie.title}</h3>
          <p>
            {featuredMovie.overview || "Una nueva historia te espera en la pantalla grande."}
          </p>
          <div class="featured-meta">
            <span class="rating">★ {featuredMovie.vote_average?.toFixed(1) || "—"}</span>
            <span>{formatReleaseDate(featuredMovie.release_date)}</span>
          </div>
          <button class="featured-button" type="button" on:click={() => openMovie(featuredMovie)}>
            Descubrir película <span aria-hidden="true">↗</span>
          </button>
        </div>
        <span class="featured-index" aria-hidden="true">DASH.IO / CINE</span>
      </section>
    {/if}

    <div class="catalog">
      <div class="catalog-topline">
        <div>
          <p class="eyebrow">ELIGE TU PLAN Y VÉ AL CINE CON TU FAMILIA</p>
          <h3>La cartelera se mueve contigo.</h3>
        </div>
        <button
          class="favorites-toggle"
          class:active={showFavorites}
          type="button"
          aria-pressed={showFavorites}
          on:click={toggleFavoritesView}
        >
          <span aria-hidden="true">{showFavorites ? "♥" : "♡"}</span>
          Mi lista <b>{favorites.length}</b>
        </button>
      </div>

      <div class="catalog-controls">
        <div class="category-tabs" role="tablist" aria-label="Tipo de cartelera">
          {#each categories as item}
            <button
              class:active={category === item.id && !activeQuery}
              type="button"
              role="tab"
              aria-selected={category === item.id && !activeQuery}
              on:click={() => chooseCategory(item.id)}
            >
              <span aria-hidden="true">{item.icon}</span>
              {item.label}
            </button>
          {/each}
        </div>

        <form class="search-form" on:submit|preventDefault={submitSearch} role="search">
          <label class="sr-only" for="movie-search">Buscar películas</label>
          <span aria-hidden="true">⌕</span>
          <input
            id="movie-search"
            bind:value={searchInput}
            placeholder="Busca una película..."
            autocomplete="off"
          />
          {#if searchInput}
            <button class="clear-search" type="button" aria-label="Limpiar búsqueda" on:click={clearSearch}>×</button>
          {/if}
          <button class="search-submit" type="submit" aria-label="Buscar">Buscar</button>
        </form>
      </div>

      {#if genres.length}
        <div class="genre-list" aria-label="Filtrar por género">
          <button
            class:active={!selectedGenre}
            type="button"
            on:click={() => selectedGenre && chooseGenre(selectedGenre)}
          >Todo</button>
          {#each genres as genre (genre.id)}
            <button
              class:active={selectedGenre === String(genre.id)}
              type="button"
              aria-pressed={selectedGenre === String(genre.id)}
              on:click={() => chooseGenre(genre.id)}
            >{genre.name}</button>
          {/each}
        </div>
      {/if}

      {#if activeQuery}
        <p class="result-context">
          Resultados para <strong>“{activeQuery}”</strong>
          <button type="button" on:click={clearSearch}>Limpiar</button>
        </p>
      {:else if showFavorites}
        <p class="result-context">Tus películas favoritas guardadas en este dispositivo.</p>
      {/if}

      {#if loading}
        <div class="status-panel" role="status">
          <span class="spinner"></span>
          <p>Buscando historias para tu próxima salida…</p>
        </div>
      {:else if error}
        <div class="status-panel error-panel" role="alert">
          <span aria-hidden="true">!</span>
          <p>{error}</p>
          <button type="button" on:click={() => loadMovies()}>Intentar de nuevo</button>
        </div>
      {:else if visibleMovies.length === 0}
        <div class="status-panel">
          <span aria-hidden="true">✦</span>
          <p>{showFavorites ? "Todavía no tienes películas guardadas." : "No encontramos películas con esos filtros."}</p>
          {#if showFavorites}
            <button type="button" on:click={() => (showFavorites = false)}>Explorar cartelera</button>
          {/if}
        </div>
      {:else}
        <div class="movie-grid" aria-live="polite">
          {#each visibleMovies as movie (movie.id)}
            <article class="movie-card" in:fade={{ duration: 220 }}>
              <div class="poster-wrap">
                <button
                  class="poster-button"
                  type="button"
                  aria-label={`Ver detalles de ${movie.title}`}
                  on:click={() => openMovie(movie)}
                >
                  {#if movie.poster_path}
                    <img
                      src={getMovieImage(movie.poster_path)}
                      alt={`Póster de ${movie.title}`}
                      loading="lazy"
                    />
                  {:else}
                    <span class="poster-placeholder" aria-hidden="true">D</span>
                  {/if}
                  <span class="poster-overlay">Ver detalles <span aria-hidden="true">↗</span></span>
                </button>
                {#if movie.vote_average}
                  <span class="poster-rating">★ {movie.vote_average.toFixed(1)}</span>
                {/if}
              </div>
              <div class="movie-copy">
                <div class="movie-title-row">
                  <h4>{movie.title}</h4>
                  <button
                    class="favorite-button"
                    class:saved={isFavorite(movie.id)}
                    type="button"
                    aria-label={isFavorite(movie.id) ? `Quitar ${movie.title} de Mi lista` : `Guardar ${movie.title} en Mi lista`}
                    aria-pressed={isFavorite(movie.id)}
                    on:click={() => toggleFavorite(movie)}
                  >{isFavorite(movie.id) ? "♥" : "♡"}</button>
                </div>
                <p>{formatReleaseDate(movie.release_date)}</p>
              </div>
            </article>
          {/each}
        </div>

        {#if !showFavorites && currentPage < totalPages}
          <div class="load-more">
            <button type="button" disabled={loadingMore} on:click={() => loadMovies({ append: true })}>
              {loadingMore ? "Cargando…" : "Ver más películas"}
              {#if !loadingMore}<span aria-hidden="true">↓</span>{/if}
            </button>
          </div>
        {/if}
      {/if}
    </div>

    <section class="dash-bridge" aria-labelledby="dash-bridge-title">
      <div class="bridge-intro">
        <p class="eyebrow">ESTA EXPERIENCIA TAMBIÉN CUENTA UNA HISTORIA</p>
        <h3 id="dash-bridge-title">¿Te gusta esta tecnología?</h3>
        <p>
          En DASH.IO conectamos la información de tu empresa, la ponemos en contexto y la
          convertimos en experiencias digitales que ayudan a tomar mejores decisiones.
        </p>
        <button class="bridge-cta" type="button" on:click={onStartDiscovery}>
          Hablemos de tu empresa <span aria-hidden="true">↗</span>
        </button>
      </div>
      <div class="bridge-steps">
        <article>
          <span>01</span>
          <h4>Conectamos</h4>
          <p>APIs, aplicaciones, bases de datos y procesos que ya usas.</p>
        </article>
        <article>
          <span>02</span>
          <h4>Damos contexto</h4>
          <p>Organizamos la información para entender qué está pasando.</p>
        </article>
        <article>
          <span>03</span>
          <h4>Lo hacemos útil</h4>
          <p>Experiencias y automatizaciones pensadas para tu negocio.</p>
        </article>
      </div>
    </section>

    <p class="attribution">
      Este producto usa un API Externo para - DASH.IO.
      <a href="https://www.themoviedb.org/" target="_blank" rel="noopener noreferrer">Conoce TMDB ↗</a>
    </p>
  </div>
</section>

{#if selectedMovie}
  <div class="modal-backdrop" use:portal role="presentation" on:click={closeMovie}>
    <dialog
      class="movie-modal"
      open
      aria-modal="true"
      aria-labelledby="movie-modal-title"
      on:click|stopPropagation
    >
      <div class="modal-topbar">
        <p class="eyebrow">FICHA DE PELÍCULA</p>
        <button class="modal-close" type="button" aria-label="Cerrar detalles" on:click={closeMovie}>×</button>
      </div>
      {#if selectedMovie.backdrop_path}
        <div
          class="modal-backdrop-image"
          style={`background-image: linear-gradient(0deg, #11131b 0%, rgba(17,19,27,.1) 100%), url("${getMovieImage(selectedMovie.backdrop_path, "w1280")}")`}
        ></div>
      {/if}
      <div class="modal-content">
        <h2 id="movie-modal-title">{movieDetails?.title || selectedMovie.title}</h2>
        <div class="detail-chips">
          <span>★ {movieDetails?.vote_average?.toFixed(1) || selectedMovie.vote_average?.toFixed(1) || "—"}</span>
          <span>{formatReleaseDate(movieDetails?.release_date || selectedMovie.release_date)}</span>
          {#if movieDetails?.runtime}<span>{movieDetails.runtime} min</span>{/if}
          {#if movieCertification}<span>Clasificación {movieCertification}</span>{/if}
        </div>
        {#if loadingDetails}
          <p class="detail-loading" role="status">Cargando reparto y detalles…</p>
        {:else}
          {#if detailError}<p class="detail-loading" role="alert">{detailError}</p>{/if}
          <p class="movie-overview">
            {movieDetails?.overview || selectedMovie.overview || "La sinopsis de esta película no está disponible."}
          </p>
          {#if movieDetails?.genres?.length}
            <div class="detail-genres">
              {#each movieDetails.genres as genre (genre.id)}<span>{genre.name}</span>{/each}
            </div>
          {/if}
          {#if movieCast.length}
            <div class="cast-list">
              <h3>Con</h3>
              <p>{movieCast.map((person) => person.name).join(" · ")}</p>
            </div>
          {/if}
          {#if selectedTrailer}
            <a
              class="trailer-link"
              href={`https://www.youtube.com/watch?v=${selectedTrailer.key}`}
              target="_blank"
              rel="noopener noreferrer"
            >Ver tráiler <span aria-hidden="true">↗</span></a>
          {/if}
        {/if}
      </div>
    </dialog>
  </div>
{/if}

<style>
  .cinema {
    --cinema-accent: #65f0d0;
    --cinema-ink: #f4f3f8;
    --cinema-muted: #a7a9b5;
    position: relative;
    z-index: 1;
    padding: clamp(4rem, 9vw, 8rem) clamp(1rem, 5vw, 4rem);
    color: var(--cinema-ink);
    background:
      radial-gradient(ellipse at 87% 14%, rgba(101, 240, 208, .09), transparent 31rem),
      linear-gradient(180deg, #10121a 0%, #0c0d13 100%);
    font-family: Inter, "Segoe UI", sans-serif;
  }
  .cinema-shell { width: min(1160px, 100%); margin: 0 auto; }
  .cinema-heading { display: flex; align-items: end; justify-content: space-between; gap: 2rem; margin-bottom: 2.2rem; }
  .eyebrow { margin: 0 0 .75rem; color: var(--cinema-accent); font-size: .68rem; font-weight: 800; letter-spacing: .16em; }
  .live-dot { display: inline-block; width: 7px; height: 7px; margin-right: .4rem; border-radius: 50%; background: var(--cinema-accent); box-shadow: 0 0 12px var(--cinema-accent); }
  .cinema-heading h2 { margin: 0; color: var(--cinema-ink); font-size: clamp(2.2rem, 5vw, 4.2rem); letter-spacing: -.06em; line-height: 1.02; }
  .cinema-heading h2 span { color: var(--cinema-accent); }
  .heading-copy { max-width: 610px; margin: .9rem 0 0; color: var(--cinema-muted); font-size: 1rem; line-height: 1.75; }
  .tmdb-credit { display: grid; flex-shrink: 0; gap: .15rem; color: var(--cinema-ink); font-size: .85rem; font-weight: 700; text-decoration: none; }
  .tmdb-credit > span { color: var(--cinema-accent); font-size: 1.2rem; }
  .tmdb-credit small { color: var(--cinema-muted); font-size: .7rem; font-weight: 500; }
  .featured { position: relative; display: flex; min-height: clamp(330px, 39vw, 480px); align-items: end; overflow: hidden; padding: clamp(1.5rem, 5vw, 3.5rem); border: 1px solid rgba(255,255,255,.12); border-radius: 24px; background-color: #222431; background-image: linear-gradient(90deg, rgba(10,11,17,.96) 0%, rgba(10,11,17,.76) 44%, rgba(10,11,17,.08) 100%), linear-gradient(0deg, rgba(10,11,17,.82), transparent 70%), var(--featured-image); background-position: center; background-size: cover; box-shadow: 0 28px 80px rgba(0,0,0,.24); }
  .featured-copy { position: relative; z-index: 1; max-width: 570px; }
  .featured-label { color: var(--cinema-accent); font-size: .67rem; font-weight: 800; letter-spacing: .13em; }
  .featured h3 { margin: .7rem 0 .55rem; color: #fff; font-size: clamp(2rem, 5vw, 3.6rem); letter-spacing: -.05em; line-height: 1.02; }
  .featured-copy > p { display: -webkit-box; max-width: 510px; margin: 0; overflow: hidden; color: rgba(255,255,255,.82); font-size: .94rem; line-height: 1.65; -webkit-box-orient: vertical; -webkit-line-clamp: 3; }
  .featured-meta { display: flex; flex-wrap: wrap; gap: 1rem; margin: 1rem 0 1.3rem; color: rgba(255,255,255,.78); font-size: .78rem; }
  .rating { color: #ffce75; font-weight: 800; }
  .featured-button, .bridge-cta { display: inline-flex; min-height: 46px; align-items: center; justify-content: center; gap: .8rem; padding: .7rem 1.15rem; border: 1px solid var(--cinema-accent); border-radius: 999px; background: var(--cinema-accent); color: #07120f; font: inherit; font-size: .85rem; font-weight: 800; text-decoration: none; cursor: pointer; transition: transform 180ms ease, box-shadow 180ms ease; }
  .featured-button:hover, .bridge-cta:hover { transform: translateY(-2px); box-shadow: 0 8px 26px rgba(101,240,208,.25); }
  .bridge-cta:focus-visible { outline: 2px solid #fff; outline-offset: 3px; }
  .featured-index { position: absolute; top: 1.5rem; right: 1.5rem; color: rgba(255,255,255,.75); font-size: .64rem; font-weight: 800; letter-spacing: .12em; }
  .catalog { padding: clamp(3rem, 7vw, 5.5rem) 0; }
  .catalog-topline, .catalog-controls { display: flex; align-items: end; justify-content: space-between; gap: 1.3rem; }
  .catalog-topline h3 { margin: 0; color: var(--cinema-ink); font-size: clamp(1.4rem, 2.5vw, 2rem); letter-spacing: -.04em; }
  .favorites-toggle { display: inline-flex; min-height: 42px; align-items: center; gap: .5rem; padding: .5rem .85rem; border: 1px solid rgba(255,255,255,.15); border-radius: 999px; background: transparent; color: var(--cinema-ink); font-size: .8rem; cursor: pointer; }
  .favorites-toggle > span { color: #ff7191; font-size: 1.1rem; }
  .favorites-toggle b { color: var(--cinema-muted); font-size: .7rem; }
  .favorites-toggle.active { border-color: rgba(255,113,145,.7); background: rgba(255,113,145,.1); }
  .catalog-controls { align-items: center; margin-top: 1.5rem; }
  .category-tabs { display: flex; flex-wrap: wrap; gap: .45rem; }
  .category-tabs button, .genre-list button { border: 1px solid transparent; background: transparent; color: var(--cinema-muted); cursor: pointer; transition: color 160ms ease, border 160ms ease, background 160ms ease; }
  .category-tabs button { display: inline-flex; min-height: 42px; align-items: center; gap: .45rem; padding: .55rem .85rem; border-radius: 999px; font-size: .8rem; font-weight: 700; }
  .category-tabs button:hover, .category-tabs button.active { border-color: rgba(101,240,208,.3); background: rgba(101,240,208,.09); color: var(--cinema-accent); }
  .search-form { display: flex; width: min(340px, 100%); min-height: 44px; align-items: center; gap: .45rem; padding: .25rem .3rem .25rem .8rem; border: 1px solid rgba(255,255,255,.15); border-radius: 999px; background: rgba(255,255,255,.04); color: var(--cinema-muted); }
  .search-form > span { font-size: 1.25rem; }
  .search-form input { width: 100%; min-width: 40px; border: 0; outline: 0; background: transparent; color: var(--cinema-ink); font: inherit; font-size: .78rem; }
  .search-form input::placeholder { color: #868895; }
  .search-submit { flex-shrink: 0; min-height: 34px; padding: .35rem .8rem; border: 0; border-radius: 999px; background: var(--cinema-accent); color: #07120f; font-size: .73rem; font-weight: 800; cursor: pointer; }
  .clear-search { padding: 0 .25rem; border: 0; background: transparent; color: var(--cinema-muted); font-size: 1.2rem; cursor: pointer; }
  .genre-list { display: flex; gap: .45rem; margin: 1rem 0 1.4rem; padding-bottom: .35rem; overflow-x: auto; scrollbar-color: #3a3c48 transparent; }
  .genre-list button { flex-shrink: 0; padding: .42rem .75rem; border-color: rgba(255,255,255,.12); border-radius: 999px; font-size: .7rem; }
  .genre-list button:hover, .genre-list button.active { border-color: var(--cinema-accent); color: var(--cinema-accent); }
  .result-context { margin: 1.25rem 0; color: var(--cinema-muted); font-size: .82rem; }
  .result-context strong { color: var(--cinema-ink); }
  .result-context button { margin-left: .55rem; border: 0; background: none; color: var(--cinema-accent); font: inherit; cursor: pointer; }
  .movie-grid { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 1.25rem 1rem; }
  .movie-card { min-width: 0; }
  .poster-wrap { position: relative; overflow: hidden; border: 1px solid rgba(255,255,255,.1); border-radius: 13px; background: #20222d; box-shadow: 0 8px 22px rgba(0,0,0,.16); }
  .poster-button { position: relative; display: block; width: 100%; aspect-ratio: 2 / 3; padding: 0; overflow: hidden; border: 0; border-radius: inherit; background: #20222d; cursor: pointer; }
  .poster-button img { display: block; width: 100%; height: 100%; object-fit: cover; transition: transform 350ms ease; }
  .movie-card:hover .poster-button img { transform: scale(1.045); }
  .poster-overlay { position: absolute; inset: auto 0 0; display: flex; align-items: center; justify-content: space-between; padding: 1.5rem .8rem .7rem; background: linear-gradient(transparent, rgba(0,0,0,.84)); color: #fff; font-size: .72rem; font-weight: 700; opacity: 0; transition: opacity 180ms ease; }
  .movie-card:hover .poster-overlay, .poster-button:focus-visible .poster-overlay { opacity: 1; }
  .poster-placeholder { display: grid; width: 100%; height: 100%; place-items: center; color: var(--cinema-accent); font-size: 3rem; font-weight: 800; }
  .movie-title-row { display: flex; align-items: flex-start; justify-content: space-between; gap: .45rem; }
  .movie-title-row h4 { flex: 1; min-width: 0; }
  .favorite-button { display: grid; flex: 0 0 auto; width: 30px; height: 30px; padding: 0; place-items: center; border: 1px solid rgba(255,255,255,.22); border-radius: 50%; background: rgba(10,11,17,.72); color: #fff; font-size: 1rem; line-height: 1; cursor: pointer; }
  .favorite-button.saved { color: #ff7191; }
  .poster-rating { position: absolute; bottom: .55rem; left: .55rem; padding: .28rem .45rem; border-radius: 6px; background: rgba(10,11,17,.82); color: #ffce75; font-size: .67rem; font-weight: 800; pointer-events: none; }
  .movie-copy { padding: .72rem .1rem 0; }
  .movie-copy h4 { display: -webkit-box; margin: 0; overflow: hidden; color: var(--cinema-ink); font-size: .85rem; font-weight: 700; line-height: 1.4; -webkit-box-orient: vertical; -webkit-line-clamp: 2; }
  .movie-copy p { margin: .3rem 0 0; color: var(--cinema-muted); font-size: .7rem; }
  .load-more { display: flex; justify-content: center; padding-top: 2rem; }
  .load-more button { display: inline-flex; min-height: 44px; align-items: center; gap: .7rem; padding: .65rem 1.1rem; border: 1px solid rgba(101,240,208,.45); border-radius: 999px; background: rgba(101,240,208,.08); color: var(--cinema-accent); font-size: .8rem; font-weight: 700; cursor: pointer; }
  .load-more button:disabled { opacity: .6; cursor: wait; }
  .status-panel { display: flex; min-height: 220px; flex-direction: column; align-items: center; justify-content: center; gap: .7rem; padding: 2rem; border: 1px solid rgba(255,255,255,.1); border-radius: 16px; background: rgba(255,255,255,.025); color: var(--cinema-muted); text-align: center; }
  .status-panel > span:not(.spinner) { color: var(--cinema-accent); font-size: 1.8rem; }
  .status-panel p { margin: 0; font-size: .88rem; }
  .status-panel button { padding: .5rem .8rem; border: 1px solid rgba(101,240,208,.4); border-radius: 999px; background: transparent; color: var(--cinema-accent); cursor: pointer; }
  .error-panel > span:not(.spinner) { display: grid; width: 30px; height: 30px; place-items: center; border: 1px solid #ff8f91; border-radius: 50%; color: #ff8f91; font-weight: 800; }
  .spinner { width: 27px; height: 27px; border: 2px solid rgba(101,240,208,.2); border-top-color: var(--cinema-accent); border-radius: 50%; animation: spin 750ms linear infinite; }
  @keyframes spin { to { transform: rotate(360deg); } }
  .dash-bridge { display: grid; grid-template-columns: .9fr 1.1fr; gap: clamp(2rem, 6vw, 5rem); align-items: center; padding: clamp(1.6rem, 5vw, 3.5rem); border: 1px solid rgba(101,240,208,.2); border-radius: 22px; background: linear-gradient(135deg, rgba(101,240,208,.09), rgba(101,240,208,.015) 54%, rgba(124,114,255,.08)); }
  .bridge-intro h3 { margin: 0 0 .8rem; color: var(--cinema-ink); font-size: clamp(1.7rem, 3vw, 2.6rem); letter-spacing: -.05em; }
  .bridge-intro > p:not(.eyebrow) { max-width: 490px; margin: 0 0 1.4rem; color: var(--cinema-muted); font-size: .92rem; line-height: 1.75; }
  .bridge-cta { min-height: 43px; padding: .6rem 1rem; font-size: .77rem; }
  .bridge-steps { display: grid; grid-template-columns: repeat(3, 1fr); gap: .85rem; }
  .bridge-steps article { min-height: 155px; padding: 1rem; border: 1px solid rgba(255,255,255,.1); border-radius: 13px; background: rgba(10,11,17,.35); }
  .bridge-steps article > span { color: var(--cinema-accent); font-size: .68rem; font-weight: 800; letter-spacing: .1em; }
  .bridge-steps h4 { margin: 1rem 0 .45rem; color: var(--cinema-ink); font-size: .88rem; }
  .bridge-steps p { margin: 0; color: var(--cinema-muted); font-size: .7rem; line-height: 1.6; }
  .attribution { margin: 1.6rem 0 0; color: #858895; font-size: .66rem; text-align: center; }
  .attribution a { margin-left: .3rem; color: #b9bdc9; }
  .modal-backdrop { --modal-gutter: clamp(.75rem, 3vw, 1.5rem); position: fixed; z-index: 3000; inset: 0; display: grid; place-items: center; padding: max(var(--modal-gutter), env(safe-area-inset-top)) max(var(--modal-gutter), env(safe-area-inset-right)) max(var(--modal-gutter), env(safe-area-inset-bottom)) max(var(--modal-gutter), env(safe-area-inset-left)); overflow-y: auto; overscroll-behavior: contain; background: rgba(5,6,10,.83); backdrop-filter: blur(12px); }
  .movie-modal { position: relative; width: min(760px, 100%); max-height: min(calc(100vh - 2rem), 900px); max-height: min(calc(100dvh - 2rem), 900px); min-height: 0; margin: auto; padding: 0; overflow-y: auto; border: 1px solid rgba(255,255,255,.15); border-radius: 20px; background: #11131b; color: var(--cinema-ink); box-shadow: 0 30px 90px rgba(0,0,0,.6); }
  .modal-topbar { display: flex; align-items: center; justify-content: space-between; gap: 1rem; padding: .75rem clamp(1.25rem, 4vw, 2rem); }
  .modal-topbar .eyebrow { margin: 0; }
  .modal-close { position: static; flex: 0 0 auto; display: grid; width: 36px; height: 36px; margin: 0; padding: 0; place-items: center; border: 1px solid rgba(255,255,255,.25); border-radius: 50%; background: rgba(10,11,17,.75); color: white; font-size: 1.35rem; line-height: 1; cursor: pointer; }
  .modal-backdrop-image { height: clamp(150px, 28vh, 270px); background-position: center 35%; background-size: cover; }
  .modal-content { padding: clamp(1.25rem, 4vw, 2rem); }
  .modal-content h2 { margin: 0 0 .8rem; color: #fff; font-size: clamp(1.7rem, 4vw, 2.6rem); letter-spacing: -.05em; }
  .detail-chips, .detail-genres { display: flex; flex-wrap: wrap; gap: .5rem; }
  .detail-chips span, .detail-genres span { padding: .38rem .6rem; border: 1px solid rgba(255,255,255,.12); border-radius: 999px; color: #c3c5d0; font-size: .68rem; }
  .detail-chips span:first-child { color: #ffce75; }
  .movie-overview { margin: 1.2rem 0; color: #c4c6d0; font-size: .88rem; line-height: 1.8; }
  .cast-list { margin-top: 1.3rem; }
  .cast-list h3 { margin: 0 0 .4rem; color: var(--cinema-accent); font-size: .75rem; text-transform: uppercase; letter-spacing: .1em; }
  .cast-list p { margin: 0; color: #c4c6d0; font-size: .8rem; line-height: 1.7; }
  .detail-loading { color: var(--cinema-muted); font-size: .8rem; }
  .trailer-link { display: inline-flex; gap: .6rem; margin-top: 1.2rem; color: var(--cinema-accent); font-size: .8rem; font-weight: 800; text-decoration: none; }
  .sr-only { position: absolute; width: 1px; height: 1px; padding: 0; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0; }

  @media (max-width: 900px) {
    .movie-grid { grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 1.1rem .8rem; }
    .dash-bridge { grid-template-columns: 1fr; }
  }
  @media (max-width: 640px) {
    .cinema { padding-right: 1rem; padding-left: 1rem; }
    .cinema-heading { align-items: start; flex-direction: column; gap: 1rem; }
    .tmdb-credit { grid-template-columns: auto 1fr; column-gap: .5rem; align-items: center; }
    .tmdb-credit > span { grid-row: span 2; }
    .featured { min-height: 390px; align-items: end; background-image: linear-gradient(0deg, rgba(10,11,17,.98) 0%, rgba(10,11,17,.72) 58%, rgba(10,11,17,.1) 100%), var(--featured-image); }
    .featured-index { top: 1rem; right: 1rem; }
    .catalog-topline { align-items: start; }
    .catalog-controls { align-items: stretch; flex-direction: column; }
    .category-tabs { display: grid; grid-template-columns: repeat(3, 1fr); gap: .2rem; }
    .category-tabs button { justify-content: center; padding: .5rem .25rem; font-size: .68rem; }
    .search-form { width: 100%; box-sizing: border-box; }
    .movie-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1.2rem .75rem; }
    .poster-overlay { opacity: 1; }
    .bridge-steps { grid-template-columns: 1fr; }
    .bridge-steps article { min-height: 0; }
    .bridge-steps h4 { margin-top: .55rem; }
    .modal-backdrop-image { height: clamp(140px, 25vh, 190px); }
    .movie-modal { border-radius: 16px; }
    .favorite-button { width: 36px; height: 36px; font-size: 1.1rem; }
  }
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { scroll-behavior: auto !important; animation-duration: .01ms !important; animation-iteration-count: 1 !important; transition-duration: .01ms !important; }
  }
</style>
