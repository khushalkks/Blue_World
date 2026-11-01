@echo off
title The Last Signal - Prototype Launcher
echo ============================================================
echo   THE LAST SIGNAL - Prototype Milestone 1
echo   Launching game window with Godot Engine 4.x...
echo ============================================================

set GODOT_EXE=%LOCALAPPDATA%\Microsoft\WinGet\Packages\GodotEngine.GodotEngine_Microsoft.Winget.Source_8wekyb3d8bbwe\Godot_v4.7.2-stable_win64.exe

if not exist "%GODOT_EXE%" (
    echo [ERROR] Godot executable was not found at:
    echo "%GODOT_EXE%"
    echo Please make sure Godot is installed or update the path in this script.
    pause
    exit /b 1
)

start "" "%GODOT_EXE%" --path "%~dp0."
exit /b 0
