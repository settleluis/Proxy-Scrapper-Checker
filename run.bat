@echo off
color 07
title Proxy Tool - Running Setup...

cls
echo.
echo ===============================
echo         Awaiting...
echo ===============================
echo.

pip install -r requirements.txt >nul 2>&1

cls
echo.
echo ===============================
echo         Running!
echo ===============================
echo.
timeout /t 2 >nul

cls
title Proxy Tool - Main Menu
py main.py
pause
