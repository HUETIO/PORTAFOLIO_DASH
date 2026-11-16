<script>
  export let color;

  function normalizeHex(value) {
    const match = /^#?([a-f\d]{3}|[a-f\d]{6})$/i.exec(value.trim());
    if (!match) return null;

    const digits = match[1].length === 3
      ? match[1].split('').map((digit) => digit + digit).join('')
      : match[1];

    return `#${digits.toUpperCase()}`;
  }

  function hexToRgb(hex) {
    const normalized = normalizeHex(hex) || '#000000';
    return {
      r: Number.parseInt(normalized.slice(1, 3), 16),
      g: Number.parseInt(normalized.slice(3, 5), 16),
      b: Number.parseInt(normalized.slice(5, 7), 16)
    };
  }

  function relativeLuminance(rgb) {
    const channels = [rgb.r, rgb.g, rgb.b].map((channel) => {
      const value = channel / 255;
      return value <= 0.04045 ? value / 12.92 : ((value + 0.055) / 1.055) ** 2.4;
    });

    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2];
  }

  function contrastRatio(first, second) {
    const luminance = [relativeLuminance(first), relativeLuminance(second)].sort((a, b) => b - a);
    return (luminance[0] + 0.05) / (luminance[1] + 0.05);
  }

  function rgbToHsl({ r, g, b }) {
    const red = r / 255;
    const green = g / 255;
    const blue = b / 255;
    const maximum = Math.max(red, green, blue);
    const minimum = Math.min(red, green, blue);
    const difference = maximum - minimum;
    let hue = 0;
    let saturation = 0;
    const lightness = (maximum + minimum) / 2;

    if (difference !== 0) {
      saturation = difference / (1 - Math.abs(2 * lightness - 1));
      switch (maximum) {
        case red:
          hue = ((green - blue) / difference) % 6;
          break;
        case green:
          hue = (blue - red) / difference + 2;
          break;
        default:
          hue = (red - green) / difference + 4;
      }
      hue *= 60;
      if (hue < 0) hue += 360;
    }

    return { h: hue, s: saturation, l: lightness };
  }

  function hslToHex(hue, saturation, lightness) {
    const chroma = (1 - Math.abs(2 * lightness - 1)) * saturation;
    const section = hue / 60;
    const secondary = chroma * (1 - Math.abs((section % 2) - 1));
    let rgb;

    if (section < 1) rgb = [chroma, secondary, 0];
    else if (section < 2) rgb = [secondary, chroma, 0];
    else if (section < 3) rgb = [0, chroma, secondary];
    else if (section < 4) rgb = [0, secondary, chroma];
    else if (section < 5) rgb = [secondary, 0, chroma];
    else rgb = [chroma, 0, secondary];

    const offset = lightness - chroma / 2;
    return `#${rgb.map((channel) => Math.round((channel + offset) * 255).toString(16).padStart(2, '0')).join('').toUpperCase()}`;
  }

  function makePalette(hex) {
    const { h, s, l } = rgbToHsl(hexToRgb(hex));
    const variations = [
      { label: 'Análogo −30°', shift: -30 },
      { label: 'Análogo −15°', shift: -15 },
      { label: 'Color base', shift: 0 },
      { label: 'Análogo +15°', shift: 15 },
      { label: 'Complementario', shift: 180 }
    ];

    return variations.map(({ label, shift }) => ({
      label,
      hex: hslToHex((h + shift + 360) % 360, s, l)
    }));
  }

  const darkBackground = { r: 17, g: 24, b: 39 };
  const whiteBackground = { r: 255, g: 255, b: 255 };
  const randomColors = ['#00FFD5', '#2196F3', '#4CAF50', '#FF4081', '#FF9800', '#B626FF', '#F97316', '#14B8A6'];

  let colorValue = normalizeHex(color || '') || '#4CAF50';
  let hexInput = colorValue;
  let inputError = '';
  let copyMessage = '';

  $: rgb = hexToRgb(colorValue);
  $: whiteContrast = contrastRatio(rgb, whiteBackground);
  $: darkContrast = contrastRatio(rgb, darkBackground);
  $: foregroundColor = whiteContrast >= darkContrast ? '#FFFFFF' : '#111827';
  $: palette = makePalette(colorValue);

  function updateHex(event) {
    hexInput = event.currentTarget.value;
    const normalized = normalizeHex(hexInput);

    if (normalized) {
      colorValue = normalized;
      hexInput = normalized;
      inputError = '';
    } else {
      inputError = 'Escribe un HEX válido, por ejemplo #4CAF50.';
    }
  }

  function chooseRandomColor() {
    const nextColor = randomColors[Math.floor(Math.random() * randomColors.length)];
    colorValue = nextColor;
    hexInput = nextColor;
    inputError = '';
    copyMessage = '';
  }

  async function copyValue(value) {
    try {
      if (!navigator.clipboard) {
        throw new Error('El portapapeles no está disponible en este navegador.');
      }

      await navigator.clipboard.writeText(value);
      copyMessage = `Copiado: ${value}`;
    } catch (error) {
      copyMessage = 'No se pudo copiar. Revisa los permisos del navegador.';
    }
  }
</script>

<svelte:head>
  <title>Laboratorio de color | DASH.IO</title>
  <meta name="description" content="Explora colores, crea paletas y comprueba el contraste para tus diseños." />
</svelte:head>

<main class="color-lab">
  <div class="lab-shell">
    <header class="lab-header">
      <div>
        <p class="eyebrow">HERRAMIENTA DE DISEÑO</p>
        <h1>Laboratorio de color</h1>
        <p class="intro">Explora tonos, crea una paleta y comprueba si tus textos se leen bien.</p>
      </div>
      <button class="random-button" type="button" on:click={chooseRandomColor}>✨ Sorpréndeme</button>
    </header>

    <section class="workspace" aria-label="Editor de color">
      <div class="color-card">
        <div class="color-preview" style={`background-color: ${colorValue}; color: ${foregroundColor};`}>
          <span>Tu color</span>
          <strong>{colorValue}</strong>
          <span class="preview-sample">El diseño también comunica.</span>
        </div>

        <div class="color-controls">
          <label class="picker-label" for="color-picker">Selector de color</label>
          <div class="input-row">
            <input
              id="color-picker"
              class="color-picker"
              type="color"
              value={colorValue}
              aria-label="Seleccionar color"
              on:input={(event) => {
                colorValue = event.currentTarget.value.toUpperCase();
                hexInput = colorValue;
                inputError = '';
                copyMessage = '';
              }}
            />
            <label class="hex-field">
              <span>Valor HEX</span>
              <input
                type="text"
                value={hexInput}
                on:input={updateHex}
                aria-label="Valor hexadecimal"
                aria-invalid={Boolean(inputError)}
                aria-describedby={inputError ? 'hex-error' : undefined}
                maxlength="7"
                spellcheck="false"
              />
            </label>
            <button class="copy-button" type="button" on:click={() => copyValue(colorValue)}>Copiar HEX</button>
          </div>
          {#if inputError}
            <p class="error-message" id="hex-error" role="alert">{inputError}</p>
          {/if}
          {#if copyMessage}
            <p class="copy-message" role="status">{copyMessage}</p>
          {/if}
        </div>
      </div>

      <section class="contrast-card" aria-labelledby="contrast-title">
        <div class="section-heading">
          <div>
            <p class="eyebrow">ACCESIBILIDAD</p>
            <h2 id="contrast-title">Prueba de contraste</h2>
          </div>
          <span class:pass={Math.max(whiteContrast, darkContrast) >= 4.5} class="contrast-badge">
            {Math.max(whiteContrast, darkContrast) >= 4.5 ? 'AA aprobado' : 'Revisar contraste'}
          </span>
        </div>

        <div class="contrast-samples">
          <div class="sample light-sample" style={`background-color: ${colorValue}; color: #FFFFFF;`}>
            <strong>Texto blanco</strong>
            <span>Contraste {whiteContrast.toFixed(2)}:1</span>
          </div>
          <div class="sample dark-sample" style={`background-color: ${colorValue}; color: #111827;`}>
            <strong>Texto oscuro</strong>
            <span>Contraste {darkContrast.toFixed(2)}:1</span>
          </div>
        </div>
        <p class="contrast-note">AA requiere 4.5:1 para texto normal y 3:1 para texto grande. Usa el texto con mayor contraste.</p>
      </section>
    </section>

    <section class="palette-section" aria-labelledby="palette-title">
      <div class="section-heading">
        <div>
          <p class="eyebrow">ARMONÍA CROMÁTICA</p>
          <h2 id="palette-title">Paleta sugerida</h2>
        </div>
        <button class="copy-button secondary" type="button" on:click={() => copyValue(`--color-brand: ${colorValue};`)}>
          Copiar variable CSS
        </button>
      </div>

      <div class="palette-grid">
        {#each palette as swatch}
          <article class="swatch-card">
            <div class="swatch" style={`background-color: ${swatch.hex};`}></div>
            <div class="swatch-info">
              <span>{swatch.label}</span>
              <button type="button" class="swatch-hex" on:click={() => copyValue(swatch.hex)} aria-label={`Copiar ${swatch.hex}`}>
                {swatch.hex} <span aria-hidden="true">⧉</span>
              </button>
            </div>
          </article>
        {/each}
      </div>
      <p class="palette-hint">Pulsa un código HEX para copiarlo al portapapeles.</p>
    </section>
  </div>
</main>

<style>
  .color-lab {
    min-height: 100vh;
    padding: clamp(24px, 5vw, 64px) 20px;
    color: #e5e7eb;
    background: radial-gradient(ellipse at top left, #172554 0, #0b1020 42%, #080b14 100%);
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  }

  .lab-shell {
    width: min(100%, 1080px);
    margin: 0 auto;
  }

  .lab-header,
  .section-heading {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
  }

  .lab-header {
    margin-bottom: 30px;
  }

  .eyebrow {
    margin: 0 0 8px;
    color: #67e8f9;
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.16em;
  }

  h1,
  h2,
  p {
    margin-top: 0;
  }

  h1 {
    margin-bottom: 9px;
    color: #f9fafb;
    font-size: clamp(2rem, 5vw, 3.2rem);
    letter-spacing: -0.045em;
  }

  h2 {
    margin-bottom: 0;
    color: #f9fafb;
    font-size: 1.25rem;
  }

  .intro {
    max-width: 580px;
    margin-bottom: 0;
    color: #aab4c8;
    line-height: 1.6;
  }

  button {
    border: 0;
    font: inherit;
    cursor: pointer;
  }

  .random-button,
  .copy-button {
    border-radius: 12px;
    color: #07111c;
    background: #67e8f9;
    font-weight: 750;
    transition: transform 160ms ease, filter 160ms ease;
  }

  .random-button {
    flex-shrink: 0;
    padding: 13px 17px;
  }

  .random-button:hover,
  .copy-button:hover {
    filter: brightness(1.08);
    transform: translateY(-1px);
  }

  .workspace {
    display: grid;
    grid-template-columns: minmax(0, 1.1fr) minmax(300px, 0.9fr);
    gap: 18px;
  }

  .color-card,
  .contrast-card,
  .palette-section {
    border: 1px solid rgba(148, 163, 184, 0.17);
    border-radius: 20px;
    background: rgba(15, 23, 42, 0.78);
    box-shadow: 0 18px 50px rgba(0, 0, 0, 0.17);
  }

  .color-card,
  .contrast-card {
    padding: 18px;
  }

  .color-preview {
    min-height: 220px;
    padding: 25px;
    border-radius: 15px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    gap: 7px;
    transition: background-color 180ms ease;
  }

  .color-preview > span:first-child {
    font-size: 0.82rem;
    font-weight: 700;
    opacity: 0.8;
  }

  .color-preview strong {
    font-size: clamp(2rem, 4vw, 2.8rem);
    letter-spacing: 0.02em;
  }

  .preview-sample {
    margin-top: 7px;
    font-size: 1.05rem;
    font-weight: 650;
  }

  .color-controls {
    padding-top: 19px;
  }

  .picker-label,
  .hex-field span {
    display: block;
    margin-bottom: 8px;
    color: #cbd5e1;
    font-size: 0.82rem;
    font-weight: 700;
  }

  .input-row {
    display: flex;
    align-items: end;
    gap: 10px;
  }

  .color-picker {
    width: 52px;
    height: 45px;
    padding: 4px;
    border: 1px solid #334155;
    border-radius: 10px;
    background: #111827;
    cursor: pointer;
  }

  .hex-field {
    flex: 1;
    min-width: 100px;
  }

  .hex-field input {
    width: 100%;
    height: 45px;
    padding: 0 12px;
    border: 1px solid #334155;
    border-radius: 10px;
    outline: none;
    color: #f8fafc;
    background: #0b1220;
    font: 600 0.95rem ui-monospace, SFMono-Regular, Menlo, monospace;
  }

  .hex-field input:focus {
    border-color: #67e8f9;
    box-shadow: 0 0 0 3px rgba(103, 232, 249, 0.14);
  }

  .copy-button {
    min-height: 45px;
    padding: 0 14px;
    white-space: nowrap;
    font-size: 0.85rem;
  }

  .error-message,
  .copy-message {
    margin: 9px 0 0;
    font-size: 0.83rem;
  }

  .error-message {
    color: #fca5a5;
  }

  .copy-message {
    color: #67e8f9;
  }

  .section-heading {
    margin-bottom: 18px;
  }

  .contrast-badge {
    padding: 7px 10px;
    border: 1px solid rgba(251, 191, 36, 0.35);
    border-radius: 999px;
    color: #fcd34d;
    background: rgba(251, 191, 36, 0.08);
    font-size: 0.72rem;
    font-weight: 750;
    white-space: nowrap;
  }

  .contrast-badge.pass {
    border-color: rgba(52, 211, 153, 0.35);
    color: #6ee7b7;
    background: rgba(52, 211, 153, 0.08);
  }

  .contrast-samples {
    display: grid;
    gap: 10px;
  }

  .sample {
    min-height: 72px;
    padding: 12px 15px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
  }

  .sample span {
    font-size: 0.8rem;
    font-weight: 650;
  }

  .contrast-note,
  .palette-hint {
    margin: 14px 0 0;
    color: #94a3b8;
    font-size: 0.8rem;
    line-height: 1.55;
  }

  .palette-section {
    margin-top: 18px;
    padding: 22px;
  }

  .copy-button.secondary {
    border: 1px solid rgba(103, 232, 249, 0.35);
    color: #a5f3fc;
    background: rgba(103, 232, 249, 0.08);
  }

  .palette-grid {
    display: grid;
    grid-template-columns: repeat(5, minmax(0, 1fr));
    gap: 12px;
  }

  .swatch-card {
    overflow: hidden;
    border: 1px solid rgba(148, 163, 184, 0.15);
    border-radius: 13px;
    background: #0b1220;
  }

  .swatch {
    height: 100px;
  }

  .swatch-info {
    padding: 11px;
    display: grid;
    gap: 7px;
  }

  .swatch-info > span {
    min-height: 2.2em;
    color: #aab4c8;
    font-size: 0.75rem;
  }

  .swatch-hex {
    padding: 0;
    color: #f8fafc;
    background: transparent;
    text-align: left;
    font: 700 0.79rem ui-monospace, SFMono-Regular, Menlo, monospace;
  }

  .swatch-hex:hover {
    color: #67e8f9;
  }

  .swatch-hex span {
    margin-left: 4px;
    color: #67e8f9;
  }

  @media (max-width: 760px) {
    .workspace {
      grid-template-columns: 1fr;
    }

    .palette-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .swatch {
      height: 80px;
    }
  }

  @media (max-width: 480px) {
    .lab-header,
    .section-heading {
      align-items: flex-start;
      flex-direction: column;
    }

    .random-button {
      width: 100%;
    }

    .input-row {
      flex-wrap: wrap;
    }

    .hex-field {
      min-width: calc(100% - 65px);
    }

    .copy-button:not(.secondary) {
      width: 100%;
    }

    .copy-button.secondary {
      width: 100%;
    }

    .sample {
      align-items: flex-start;
      flex-direction: column;
      justify-content: center;
    }
  }
</style>
