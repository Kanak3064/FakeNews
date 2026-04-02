@echo off
REM Start Flask Backend Server
REM This script starts the Python ML backend

echo.
echo ========================================
echo   Starting Flask Backend (Port 5000)
echo ========================================
echo.

cd C:\Users\Asus\OneDrive\Desktop\NewsVerifier

REM Check if venv exists
if exist venv\ (
    call venv\Scripts\activate
) else (
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate
)

REM Check if requirements are installed
pip list | findstr flask >nul
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements-api.txt
)

REM Start Flask server
echo.
echo Starting Flask API Server...
python api_server.py

pause
