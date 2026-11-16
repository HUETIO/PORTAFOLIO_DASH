# Svelte + Vite

This template should help get you started developing with Svelte in Vite.

## Recommended IDE Setup

[VS Code](https://code.visualstudio.com/) + [Svelte](https://marketplace.visualstudio.com/items?itemName=svelte.svelte-vscode).

## Need an official Svelte framework?

Check out [SvelteKit](https://github.com/sveltejs/kit#readme), which is also powered by Vite. Deploy anywhere with its serverless-first approach and adapt to various platforms, with out of the box support for TypeScript, SCSS, and Less, and easily-added support for mdsvex, GraphQL, PostCSS, Tailwind CSS, and more.

## Technical considerations

**Why use this over SvelteKit?**

- It brings its own routing solution which might not be preferable for some users.
- It is first and foremost a framework that just happens to use Vite under the hood, not a Vite app.

This template contains as little as possible to get started with Vite + Svelte, while taking into account the developer experience with regards to HMR and intellisense. It demonstrates capabilities on par with the other `create-vite` templates and is a good starting point for beginners dipping their toes into a Vite + Svelte project.

Should you later need the extended capabilities and extensibility provided by SvelteKit, the template has been structured similarly to SvelteKit so that it is easy to migrate.

**Why `global.d.ts` instead of `compilerOptions.types` inside `jsconfig.json` or `tsconfig.json`?**

Setting `compilerOptions.types` shuts out all other types not explicitly listed in the configuration. Using triple-slash references keeps the default TypeScript setting of accepting type information from the entire workspace, while also adding `svelte` and `vite/client` type information.

**Why include `.vscode/extensions.json`?**

Other templates indirectly recommend extensions via the README, but this file allows VS Code to prompt the user to install the recommended extension upon opening the project.

**Why enable `checkJs` in the JS template?**

It is likely that most cases of changing variable types in runtime are likely to be accidental, rather than deliberate. This provides advanced typechecking out of the box. Should you like to take advantage of the dynamically-typed nature of JavaScript, it is trivial to change the configuration.

**Why is HMR not preserving my local component state?**

HMR state preservation comes with a number of gotchas! It has been disabled by default in both `svelte-hmr` and `@sveltejs/vite-plugin-svelte` due to its often surprising behavior. You can read the details [here](https://github.com/sveltejs/svelte-hmr/tree/master/packages/svelte-hmr#preservation-of-local-state).

If you have state that's important to retain within a component, consider creating an external store which would not be replaced by HMR.

```js
// store.js
// An extremely simple external store
import { writable } from 'svelte/store'
export default writable(0)
```

## Asistente virtual

El asistente comercial `CapibaraNeitor` muestra el catálogo definido en
`src/services.js` y permite enviar una solicitud de contacto desde
`src/Agent.svelte`. No confirma ventas ni precios. Solo envía el servicio elegido,
nombre, correo, teléfono y los mensajes escritos en el chat después del
consentimiento y de la verificación reCAPTCHA. Los mensajes se procesan con
Google Gemini para responder; si el usuario envía la solicitud, sus mensajes se
incluyen en el correo a DASH.IO. El asistente redirige consultas ajenas a
tecnología y rechaza solicitudes de violencia o intrusión cibernética maliciosa.
Configura `VITE_GEMINI_API_KEY` para usar el chat. Esta clave se incluye en el
cliente web: restríngela en Google Cloud a la API de Generative Language y a los
dominios autorizados; no uses una clave privada de servidor.

### Configurar EmailJS y reCAPTCHA Enterprise

El formulario muestra un widget de reCAPTCHA Enterprise de tipo checkbox con la
acción `SALES_REQUEST` y envía el token junto con los datos a
`/api/sales-request`. Firebase Functions valida el token, la acción y la
puntuación con Google Cloud antes de enviar el correo a través de EmailJS. La
clave privada de EmailJS y la autenticación de Google permanecen en el servidor.

1. En Google Cloud, habilita reCAPTCHA Enterprise para el proyecto
   `portafoliodash`, crea una clave web de tipo checkbox con desafíos habilitados
   y autoriza los dominios publicados. Concede a la cuenta de servicio de Cloud
   Functions el rol `roles/recaptchaenterprise.agent`. Usa claves distintas para
   desarrollo y producción; agrega `localhost` únicamente a la clave de
   desarrollo. Si abres la app con `127.0.0.1`, autoriza también ese hostname en
   esa clave.
2. En EmailJS configura la plantilla `Contact Us` para enviar al destinatario
   `capibaraneitor@gmail.com`. Debe usar `customer_name`, `customer_email`,
   `customer_phone`, `service_name`, `customer_message` y `submitted_at`; el
   destinatario no puede provenir del formulario.
3. La configuración pública local de Functions está en el archivo ignorado
   `functions/.env.portafoliodash`. Ajusta `SALES_ALLOWED_ORIGINS` para incluir
   los orígenes exactos de desarrollo y producción. No registres dominios con
   comodines.
4. Completa los identificadores públicos de EmailJS en el archivo ignorado
   `functions/.env.portafoliodash`. Crea la plantilla para que el destinatario
   sea `capibaraneitor@gmail.com`; configura en ella los seis campos indicados
   arriba.
5. Crea el secreto privado de EmailJS desde la terminal; Firebase CLI solicitará
   el valor sin guardarlo en el código:

   ```powershell
   firebase functions:secrets:set EMAILJS_PRIVATE_KEY --project portafoliodash
   ```

6. Instala y valida Functions, luego despliega el backend y Hosting:

   ```powershell
   npm --prefix functions install
   npm --prefix functions run check
   npm run build
   firebase deploy --only functions:default:submitSalesRequest,hosting --project portafoliodash
   ```

Para desarrollo local, guarda la clave checkbox autorizada para `localhost` en
`.env.local` y usa la misma como `RECAPTCHA_ENTERPRISE_CHECKBOX_SITE_KEY` en
`functions/.env.local`. Para producción, guarda una clave checkbox diferente,
autorizada para `portafoliodash.web.app`, en `.env.production.local` y usa esa
misma clave en `functions/.env.portafoliodash`. Configura también una clave
Gemini restringida a los dominios de producción; Vite puede leerla desde `.env`
o `.env.production.local`. El script `gestionar_portafolio.bat` valida que las
claves reCAPTCHA de frontend y Functions coincidan y que producción no reutilice
la clave local.

Para desarrollo local, inicia Firebase Functions Emulator con
`firebase emulators:start --only functions --project portafoliodash`. Vite
redirige automáticamente `/api/sales-request` al emulador en el puerto `5001`;
no necesitas configurar `VITE_SALES_REQUEST_URL`. Si defines esa variable,
asegúrate de que apunte al emulador o a un backend disponible.
Configura `VITE_RECAPTCHA_ENTERPRISE_CHECKBOX_SITE_KEY` con una site key
Enterprise de tipo checkbox, autorizada para el hostname que usas (`localhost`
o `127.0.0.1`).
Una clave score-based no muestra la casilla y no es compatible con este widget.
Incluye el origen exacto de Vite (por ejemplo, `http://localhost:5174`) en
`SALES_ALLOWED_ORIGINS` dentro de `functions/.env.local` y
`functions/.env.portafoliodash`. Después de cambiar los archivos de entorno,
reinicia Vite para que cargue la nueva clave.
No reutilices la clave de producción para el servidor local y nunca pongas la
clave privada de EmailJS en una variable `VITE_*`.

El umbral inicial de puntuación es `0.5` y se configura en
`RECAPTCHA_MINIMUM_SCORE`. Las primeras 10 000 evaluaciones de reCAPTCHA
Enterprise al mes son gratuitas según Google; uso superior puede requerir
facturación. Las funciones requieren un proyecto Firebase con el plan y APIs
necesarios. No solicites contraseñas, datos de pago ni información confidencial
en el formulario.

## Iniciar y desplegar en Windows

Ejecuta [`gestionar_portafolio.bat`](./gestionar_portafolio.bat) desde el
Explorador o una terminal y elige una opción:

- **Iniciar el sistema local** instala las dependencias si faltan y ejecuta
  `npm run dev`; usa `Ctrl+C` para detener el servidor.
- **Desplegar en Firebase** construye el sitio y despliega la Cloud Function
  `default` junto con Hosting en `portafoliodash`. El script pregunta antes de
  aplicar la política de limpieza de Artifact Registry que Firebase requiere
  para completar el despliegue de Functions. Si se rechaza, publica solamente
  Hosting; la función existente no se modifica.

Se requiere Node.js, npm, Firebase CLI autenticado con acceso al proyecto y
configuración de facturación/secreto de Functions en Firebase.

## Cartelera interactiva

La experiencia de cine vive en `src/components/CinemaExperience.svelte` y usa
`src/lib/movieService.js` para consultar la cartelera actual, próximos estrenos,
películas populares, géneros, búsquedas y fichas con reparto y tráileres de TMDB.
La lista de favoritos se guarda localmente en el dispositivo.

Configura `VITE_THE_MOVIE_DATA_BASE_API_KEY` en `.env.local` para desarrollo
local. Las variables `VITE_*` se incorporan al JavaScript del navegador; la clave
de TMDB no debe tratarse como un secreto. Para otros servicios, no expongas
credenciales privadas en variables `VITE_*`. La sección incluye el aviso de
atribución solicitado por TMDB y no implica que DASH.IO esté afiliado a TMDB.

## Encabezado y navegación

El encabezado vive en `src/Header.svelte`, fuera del `<main>` de `src/App.svelte`,
fijo al viewport y a todo su ancho. Sus estilos son locales al componente: en escritorio muestra todos los enlaces y,
en pantallas de hasta 800 px, usa un menú desplegable con botón accesible,
cierre al elegir una opción y soporte para Escape.
