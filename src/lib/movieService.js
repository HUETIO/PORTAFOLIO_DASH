const API_KEY = import.meta.env.VITE_THE_MOVIE_DATA_BASE_API_KEY;
const API_BASE_URL = "https://api.themoviedb.org/3";
const IMAGE_BASE_URL = "https://image.tmdb.org/t/p";
const categories = new Set(["now_playing", "upcoming", "popular"]);

async function request(endpoint, params = {}) {
  if (!API_KEY) {
    throw new Error(
      "Falta configurar VITE_THE_MOVIE_DATA_BASE_API_KEY para conectar con TMDB.",
    );
  }

  const url = new URL(`${API_BASE_URL}/${endpoint}`);
  url.search = new URLSearchParams({
    api_key: API_KEY,
    language: "es-ES",
    region: "CO",
    ...params,
  }).toString();

  const response = await fetch(url);
  const data = await response.json();

  if (!response.ok) {
    throw new Error(
      data.status_message || `TMDB respondió con el estado ${response.status}.`,
    );
  }

  return data;
}

export function getMovieImage(path, size = "w500") {
  return path ? `${IMAGE_BASE_URL}/${size}${path}` : "";
}

export async function getMovieGenres() {
  const data = await request("genre/movie/list");
  return data.genres || [];
}

export async function getMovies({ category, page = 1, query = "", genreId = "" }) {
  const search = query.trim();
  const params = { page: String(page) };
  let endpoint;

  if (search) {
    endpoint = "search/movie";
    params.query = search;
    params.region = "CO";
    params.include_adult = "false";
  } else if (genreId) {
    endpoint = "discover/movie";
    params.with_genres = genreId;

    if (category === "upcoming") {
      params["primary_release_date.gte"] = new Date().toISOString().slice(0, 10);
      params.sort_by = "primary_release_date.asc";
    } else if (category === "now_playing") {
      const recentDate = new Date();
      recentDate.setDate(recentDate.getDate() - 90);
      params["primary_release_date.gte"] = recentDate.toISOString().slice(0, 10);
      params["primary_release_date.lte"] = new Date().toISOString().slice(0, 10);
      params.sort_by = "popularity.desc";
    } else {
      params.sort_by = "popularity.desc";
    }
  } else {
    if (!categories.has(category)) {
      throw new Error("La categoría de cartelera seleccionada no es válida.");
    }
    endpoint = `movie/${category}`;
  }

  return request(endpoint, params);
}

export async function getMovieDetails(movieId) {
  return request(`movie/${encodeURIComponent(movieId)}`, {
    append_to_response: "videos,credits,release_dates",
    include_video_language: "es,en,null",
  });
}

export async function getPopularMovies() {
  const data = await getMovies({ category: "popular" });
  return data.results.map((movie) => ({
    ...movie,
    poster_path: getMovieImage(movie.poster_path),
  }));
}