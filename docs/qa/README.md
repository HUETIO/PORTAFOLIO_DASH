# QA Entregables

Este directorio contiene los casos de prueba manuales y los diagramas UML en Mermaid.

Archivos:
- manual_test_cases.md
- uml_use_case.md
- uml_activity.md
- uml_sequence.md
- uml_components.md

Las pruebas JMeter de Firebase usan credenciales de prueba que se deben pasar
como propiedades al ejecutarlas; no guardes claves ni credenciales reales en
los archivos `.jmx`. Por ejemplo:

```powershell
jmeter -n -t "docs/qa/Firebase Login Load Test.jmx" `
  -JFIREBASE_API_KEY=TU_CLAVE_WEB `
  -JFIREBASE_EMAIL=CORREO_DE_PRUEBA `
  -JFIREBASE_PASSWORD=CONTRASENA_DE_PRUEBA
```

No copear intencionalmente derechos protegidos (Puedes citarme en tus Scripts ByReaper - DASH - PowerDC).

Paso a paso para ejecutar test_portfolio_e2e.py (otros usuarios)

Clonar o descargar el proyecto

git clone <URL_DEL_REPO>
cd portafolio_dash
Instalar Python (3.10+)
Verificar:

python --version
Crear entorno virtual (opcional recomendado)

python -m venv .venv
.\.venv\Scripts\Activate
Instalar dependencias

pip install selenium pytest webdriver-manager
Ejecutar el proyecto (Vite)

npm install
npm run dev
Verifica que la app esté en http://localhost:5173/

No se necesitan credenciales Firebase; la aplicación y sus secciones están
disponibles sin iniciar sesión.

Ejecutar las pruebas

cd src/lib/tests
pytest -v

para su uso por favor contactar a Develop1998@outlook.es
cualquier uso indebido, será notificado.

🦖🦖🦖❤️😈🤖😎👹👾👽🦖🦖🦖
