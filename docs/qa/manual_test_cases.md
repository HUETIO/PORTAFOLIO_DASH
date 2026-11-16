# Casos de Prueba Manuales

Formato solicitado: ID del caso, Objetivo, Precondiciones, Pasos, Resultado Esperado, Resultado Obtenido, Evidencia.

## TC-ACC-001 — Acceso público al contenido
- **Objetivo:** Verificar que las secciones y proyectos estén disponibles sin iniciar sesión.
- **Precondiciones:** App abierta en `http://localhost:5173/`; no se requieren credenciales.
- **Pasos Detallados:**
  1. Abrir la aplicación.
  2. Desplazarse hasta “Mi Stack Tecnológico” y “Mis Mejores Proyectos”.
- **Resultado Esperado:** Ambas secciones aparecen disponibles y no se solicita autenticación.
- **Resultado Obtenido:** ________
- **Evidencia:** Captura de la sección visible.

## TC-AGT-002 — Agente sin iniciar sesión
- **Objetivo:** Verificar que se pueda abrir el chat Gemini sin autenticación.
- **Precondiciones:** App cargada.
- **Pasos Detallados:**
  1. Clic en el botón del agente Gemini.
- **Resultado Esperado:** Se muestra el chat del agente sin pedir credenciales.
- **Resultado Obtenido:** ________
- **Evidencia:** Captura del chat abierto.

## TC-CIN-003 — Modal de película (Cinema Explorer)
- **Objetivo:** Validar que se abra y cierre el modal “Info”.
- **Precondiciones:** App cargada y películas visibles.
- **Pasos Detallados:**
  1. Scroll a “Cinema Explorer”.
  2. Pasar el mouse sobre una tarjeta.
  3. Clic en botón `▶ Info`.
  4. Clic en `Cerrar`.
- **Resultado Esperado:** Modal se abre con información y se cierra correctamente.
- **Resultado Obtenido:** ________
- **Evidencia:** Capturas de modal abierto y cerrado.

## TC-TAB-004 — Sistema de Tabs
- **Objetivo:** Validar apertura y cierre de pestañas de color.
- **Precondiciones:** App cargada.
- **Pasos Detallados:**
  1. En “Color Tab Section”, clic en una pestaña.
  2. Verificar que la pestaña aparece arriba.
  3. Clic en “×” para cerrarla.
- **Resultado Esperado:** La pestaña se abre y se cierra sin errores.
- **Resultado Obtenido:** ________
- **Evidencia:** Captura de pestaña abierta y luego cerrada.
