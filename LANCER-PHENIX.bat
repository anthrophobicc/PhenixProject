@echo off
setlocal
chcp 65001 >nul
cd /d "%~dp0"

REM Si l'executable a deja ete construit, on le lance en priorite.
set "EXE=%~dp0src-tauri\target\release\phenix.exe"
if exist "%EXE%" (
  start "" "%EXE%"
  exit /b 0
)

REM Sinon on ouvre l'application dans le navigateur. Tout fonctionne
REM de la meme facon, seule la sauvegarde sur disque est indisponible.
start "" "%~dp0app\phenix.html"
exit /b 0
