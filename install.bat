@echo off
chcp 65001 >nul
echo ============================================
echo   WeChat Monitor - Install
echo ============================================
echo.

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found! Please install Python 3.10+ from python.org
    echo         and check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

echo [1/2] Installing dependencies...
python -m pip install wechatauto-replica pywin32 cryptography pycryptodome psutil colorama Pillow pyperclip --quiet

echo [2/2] Done!
echo.
echo Next: right-click start_monitor.bat and Run as administrator
pause
