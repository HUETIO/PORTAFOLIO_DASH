<script>
    import { animateShape } from '../lib/btnAnimation.js';
    import { getPopularMovies } from '../lib/movieService.js';
    import { fade, scale } from 'svelte/transition';

    let movies = [];
    let loading = false;
    let showGrid = false;
    let currentPage = 0;
    const itemsPerPage = 4; // Definimos el tamaño de la matriz (2x2)

    // Lógica de Matriz reactiva
    $: movieMatrix = chunkArray(movies, itemsPerPage);
    $: currentItems = movieMatrix[currentPage] || [];

    function chunkArray(arr, size) {
        let matrix = [];
        for (let i = 0; i < arr.length; i += size) {
            matrix.push(arr.slice(i, i + size));
        }
        return matrix;
    }

    async function toggleExplore() {
        if (!showGrid) {
            loading = true;
            movies = await getPopularMovies();
            loading = false;
            showGrid = true;
        } else {
            showGrid = false;
        }
    }
</script>

<div class="cinema-section">
    <!-- Botón con ID y Action únicos -->
    <button class="cinema-morph-btn" use:animateShape on:click={toggleExplore}>
        <svg viewBox="0 0 100 50" preserveAspectRatio="none">
            <path d="M0,0 Q50,20 100,0 Q50,50 0,0 Z" />
        </svg>
        <span class="btn-text">
            {loading ? 'Cargando...' : showGrid ? 'Cerrar Galería' : 'Explorar Películas'}
        </span>
    </button>

    {#if showGrid}
        <div class="cinema-overlay" transition:fade>
            <div class="cinema-modal" transition:scale>
                <header>
                    <h2>🎬 Cartelera (Matriz de Datos)</h2>
                    <p>Página {currentPage + 1} de {movieMatrix.length}</p>
                </header>

                <!-- Matriz Grid 2x2 -->
                <div class="movie-grid">
                    {#each currentItems as movie}
                        <div class="movie-card" in:scale>
                            <img src={movie.poster_path} alt={movie.title} />
                            <div class="movie-info">
                                <h3>{movie.title}</h3>
                            </div>
                        </div>
                    {/each}
                </div>

                <!-- Paginación -->
                <nav class="pagination">
                    <button disabled={currentPage === 0} on:click={() => currentPage--}>Anterior</button>
                    
                    <div class="dots">
                        {#each movieMatrix as _, i}
                            <span class="dot" class:active={i === currentPage}></span>
                        {/each}
                    </div>

                    <button disabled={currentPage >= movieMatrix.length - 1} on:click={() => currentPage++}>Siguiente</button>
                </nav>
            </div>
        </div>
    {/if}
</div>

<style>
    .cinema-section {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 2rem;
    }

    .cinema-morph-btn {
        position: relative;
        width: 240px;
        height: 70px;
        border: none;
        background: transparent;
        cursor: pointer;
        border-radius: 20px;
        overflow: hidden;
        z-index: 100;
    }

    .btn-text {
        position: relative;
        z-index: 2;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    svg {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        z-index: 1;
    }

    /* Modal Estilo Cinema */
    .cinema-overlay {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0,0,0,0.85);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 2000;
        backdrop-filter: blur(8px);
    }

    .cinema-modal {
        background: #111;
        border: 2px solid #00ffd5;
        border-radius: 30px;
        padding: 30px;
        width: 90%;
        max-width: 600px;
        box-shadow: 0 0 40px rgba(0,255,213,0.2);
    }

    .movie-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr); /* Matriz de 2 columnas */
        gap: 20px;
        margin: 20px 0;
    }

    .movie-card {
        background: #222;
        border-radius: 15px;
        overflow: hidden;
        border: 1px solid #333;
    }

    .movie-card img {
        width: 100%;
        height: 180px;
        object-fit: cover;
    }

    .movie-info { padding: 10px; text-align: center; }
    .movie-info h3 { font-size: 0.9rem; margin: 0; color: #fff; }

    /* Paginación */
    .pagination {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 20px;
    }

    .pagination button {
        background: #00ffd5;
        color: #000;
        border: none;
        padding: 8px 16px;
        border-radius: 10px;
        font-weight: bold;
        cursor: pointer;
    }

    .pagination button:disabled { opacity: 0.3; cursor: not-allowed; }

    .dots { display: flex; gap: 8px; }
    .dot { width: 10px; height: 10px; background: #444; border-radius: 50%; }
    .dot.active { background: #00ffd5; box-shadow: 0 0 10px #00ffd5; }
</style>