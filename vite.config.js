import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vite.dev/config/
export default defineConfig({
  plugins: [svelte()],
  server: {
    proxy: {
      '/api/sales-request': {
        target: 'http://127.0.0.1:5001',
        changeOrigin: true,
        rewrite: () => '/portafoliodash/us-central1/submitSalesRequest',
      },
    },
  },
})
