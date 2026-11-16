<script>
    import { animateShape } from '../lib/btnAnimation.js';
    import { getPopularMovies } from '../lib/movieService.js';
    
    let movies = [];
    let loading = false;

    async function handleExplore() {
        loading = true;
        movies = await getPopularMovies();
        loading = false;
    }
</script>

<div class="movie-container">
    <!-- El botón ahora usa la animación mediante 'use:animateShape' -->
    <button id="morph-btn" use:animateShape on:click={handleExplore}>
        <svg viewBox="0 0 100 50" preserveAspectRatio="none">
            <path id="btn-shape" d="M0,0 Q50,20 100,0 Q50,50 0,0 Z" />
        </svg>
        <span class="btn-text">
            {loading ? 'Cargando...' : 'Explorar Películas'}
        </span>
    </button>

    {#if movies.length > 0}
        <div class="movie-grid">
            {#each movies as movie}
                <div class="movie-card">
                    <img src={movie.poster_path} alt={movie.title} />
                    <h3>{movie.title}</h3>
                </div>
            {/each}
        </div>
    {/if}
</div>

<style>
    /* Estilos del botón (los mismos que ya tenías) */
    #morph-btn {
        position: relative;
        width: 240px;
        height: 70px;
        border: none;
        background: transparent;
        cursor: pointer;
        border-radius: 16px;
        overflow: hidden;
    }
    .btn-text {
        position: relative;
        z-index: 2;
        font-weight: bold;
    }
    svg {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        z-index: 1;
    }
    /* Estilos de la rejilla de películas */
    .movie-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
        gap: 20px;
        margin-top: 30px;
    }
    .movie-card img {
        width: 100%;
        border-radius: 8px;
    }
</style>