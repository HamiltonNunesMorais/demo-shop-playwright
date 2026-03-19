@echo off
echo [1/3] Criando ambiente virtual (.venv)...
python -m venv .venv

echo [2/3] Instalando bibliotecas do requirements.txt...
call .venv\Scripts\activate && pip install -r requirements.txt

echo [3/3] Instalando navegadores do Playwright (Chromium)...
call .venv\Scripts\activate && playwright install chromium

echo.
echo ======================================================
echo PROJETO CONFIGURADO! 
echo RELEMBRE: Crie o arquivo .env manualmente na raiz.
echo ======================================================
pause