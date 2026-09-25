@echo off
setlocal
chcp 65001 >nul
title Phenix - Construction de l'executable
cd /d "%~dp0"

echo.
echo   ================================================
echo     PHENIX - Construction de l'executable
echo   ================================================
echo.

REM ---------- Verification de Rust ----------
where cargo >nul 2>&1
if errorlevel 1 (
  echo   [X] Rust n'est pas installe.
  echo.
  echo   Installez-le ici : https://rustup.rs
  echo   Relancez ce fichier apres l'installation.
  echo.
  pause
  exit /b 1
)
echo   [OK] Rust detecte

REM ---------- Verification de tauri-cli ----------
cargo tauri --version >nul 2>&1
if errorlevel 1 (
  echo   [..] Installation de tauri-cli, patientez 2-5 minutes...
  cargo install tauri-cli --version "^2.0.0" --locked
  if errorlevel 1 (
    echo   [X] L'installation de tauri-cli a echoue.
    pause
    exit /b 1
  )
)
echo   [OK] tauri-cli pret

REM ---------- Construction ----------
echo.
echo   [..] Construction en cours. Le premier build prend 5-15 minutes.
echo.
cargo tauri build
if errorlevel 1 (
  echo.
  echo   [X] La construction a echoue. Lisez les erreurs ci-dessus.
  pause
  exit /b 1
)

REM ---------- Resultat ----------
echo.
echo   ================================================
echo     TERMINE
echo   ================================================
echo.

set "NSIS=%~dp0src-tauri\target\release\bundle\nsis"
set "EXE=%~dp0src-tauri\target\release\phenix.exe"

if exist "%NSIS%" (
  echo   Installateur : %NSIS%
  explorer "%NSIS%"
) else if exist "%EXE%" (
  echo   Executable : %EXE%
  explorer /select,"%EXE%"
)
echo.
pause
