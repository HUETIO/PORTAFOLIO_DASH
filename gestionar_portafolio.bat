@echo off
setlocal
cd /d "%~dp0"
if errorlevel 1 (
  echo No se pudo acceder a la carpeta del proyecto.
  pause
  exit /b 1
)

:menu
cls
echo ==========================================
echo          DASH.IO - GESTION
echo ==========================================
echo 1. Iniciar el sistema local
echo 2. Desplegar en Firebase
echo 3. Salir
echo.
choice /C 123 /N /M "Elige una opcion: "
if errorlevel 3 goto end
if errorlevel 2 goto deploy
if errorlevel 1 goto start

:start
if not exist "node_modules\vite\bin\vite.js" (
  echo No se encontraron las dependencias del sitio. Instalando...
  call npm ci
  if errorlevel 1 goto failure
)
echo Iniciando DASH.IO. Usa Ctrl+C para detener el servidor.
call npm run dev
if errorlevel 1 goto failure
goto end

:deploy
where firebase >nul 2>nul
if errorlevel 1 (
  echo Firebase CLI no esta instalado o no esta disponible en PATH.
  echo Instala Firebase CLI y vuelve a ejecutar este archivo.
  goto failure
)

where powershell >nul 2>nul
if errorlevel 1 (
  echo PowerShell no esta disponible para validar la configuracion de produccion.
  goto failure
)

if not exist "node_modules\vite\bin\vite.js" (
  echo No se encontraron las dependencias del sitio. Instalando...
  call npm ci
  if errorlevel 1 goto failure
)

if not exist "functions\node_modules\firebase-functions\package.json" (
  echo No se encontraron las dependencias de Cloud Functions. Instalando...
  call npm --prefix functions ci
  if errorlevel 1 goto failure
)

echo Validando las claves de produccion...
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ErrorActionPreference='Stop'; function ReadEnv($path,$name) { if (-not (Test-Path $path)) { return $null }; $line = Get-Content $path | Where-Object { $_ -match ('^\s*' + [regex]::Escape($name) + '\s*=') } | Select-Object -Last 1; if ($line) { return (($line -replace ('^\s*' + [regex]::Escape($name) + '\s*=\s*'), '').Trim().Trim([char]34).Trim([char]39)) }; return $null }; $gemini=$null; foreach ($file in @('.env.production.local','.env.production','.env.local','.env')) { $gemini=ReadEnv $file 'VITE_GEMINI_API_KEY'; if ($gemini) { break } }; $productionKey=ReadEnv '.env.production.local' 'VITE_RECAPTCHA_ENTERPRISE_CHECKBOX_SITE_KEY'; $developmentKey=ReadEnv '.env.local' 'VITE_RECAPTCHA_ENTERPRISE_CHECKBOX_SITE_KEY'; $functionsKey=ReadEnv 'functions/.env.portafoliodash' 'RECAPTCHA_ENTERPRISE_CHECKBOX_SITE_KEY'; if ([string]::IsNullOrWhiteSpace($gemini) -or $gemini -match '^(your_|placeholder|change_me)') { Write-Output 'Falta VITE_GEMINI_API_KEY en la configuracion local.'; exit 1 }; if ([string]::IsNullOrWhiteSpace($productionKey) -or $productionKey -match '^(your_|placeholder|change_me)') { Write-Output 'Falta la clave checkbox de produccion en .env.production.local.'; exit 1 }; if ($productionKey -eq $developmentKey) { Write-Output 'La clave reCAPTCHA de produccion no puede ser la clave local.'; exit 1 }; if ($productionKey -ne $functionsKey) { Write-Output 'La clave de .env.production.local debe coincidir con RECAPTCHA_ENTERPRISE_CHECKBOX_SITE_KEY en functions/.env.portafoliodash.'; exit 1 }"
if errorlevel 1 goto failure

echo Validando Cloud Functions...
call npm --prefix functions run check
if errorlevel 1 goto failure

echo Construyendo el sitio para produccion...
call npm run build
if errorlevel 1 goto failure

echo.
echo Firebase recomienda una politica de limpieza de imagenes para Functions.
echo Conservar imagenes por 7 dias limita almacenamiento; imagenes antiguas
echo dejaran de estar disponibles para rollback, pero la funcion activa no se borra.
choice /C SN /N /M "Configurar ahora la politica de 7 dias? [S/N]: "
if errorlevel 2 goto hosting_only

call firebase functions:artifacts:setpolicy --location us-central1 --days 7 --force --project portafoliodash
if errorlevel 1 goto failure

echo.
echo Desplegando Cloud Functions y Hosting en portafoliodash...
call firebase deploy --only functions:default:submitSalesRequest,hosting --project portafoliodash
if errorlevel 1 goto failure
goto success

:hosting_only
echo.
echo Se omitira Cloud Functions y se publicara unicamente Hosting.
call firebase deploy --only hosting --project portafoliodash
if errorlevel 1 goto failure
goto success

:success
echo.
echo Despliegue completado.
echo https://portafoliodash.web.app
pause
goto end

:failure
echo.
echo La tarea fallo. Revisa el mensaje anterior antes de volver a intentarlo.
pause
exit /b 1

:end
endlocal
