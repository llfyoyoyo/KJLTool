@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo Starting KJLTool viewer...
echo.

where python >nul 2>&1
if errorlevel 1 (
    echo [Error] Python not found. Please install Python and add it to PATH.
    pause
    exit /b 1
)

start "" "http://127.0.0.1:8080/viewer/"
python serve.py --host 127.0.0.1 --port 8080

pause
