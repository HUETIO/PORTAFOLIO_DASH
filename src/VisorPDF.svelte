<script>
  import { onMount } from 'svelte';
  import * as pdfjsLib from 'pdfjs-dist';

  export let url;

  let canvas;

  onMount(async () => {
    pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.4.120/pdf.worker.min.js';
    const loadingTask = pdfjsLib.getDocument(url);
    const pdf = await loadingTask.promise;
    const page = await pdf.getPage(1);
    const viewport = page.getViewport({ scale: 1.0 });
    canvas.width = viewport.width;
    canvas.height = viewport.height;
    await page.render({
      canvasContext: canvas.getContext('2d'),
      viewport: viewport
    }).promise;
  });
</script>

<canvas bind:this={canvas} style="width: 100%; height: 500px; border: 1px solid #333;"></canvas>
