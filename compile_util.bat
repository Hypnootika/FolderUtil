@echo off
NET SESSION >nul 2>&1 || (powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList '/c %~0'";exit)
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt
echo Dependencies installed.
pyinstaller --onefile FolderUtil.py
echo Compilation completed. Executable is located in the "dist" folder.
pause
