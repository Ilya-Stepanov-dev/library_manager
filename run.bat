@echo off

where python3 >nul 2>nul
if %errorlevel%==0 (
    set PYTHON=python3
) else (
    set PYTHON=python
)

%PYTHON% app/main.py