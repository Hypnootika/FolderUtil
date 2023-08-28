@echo off
NET SESSION >nul 2>&1 || (powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList '/c %~0'";exit)
set /p exe_path="Enter the full path to the FolderUtil.exe: "
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\FolderUtil.exe" /v Path /d "%exe_path%"
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\FolderUtil.exe" /ve /d "%exe_path"
echo Registry updated. You can now run "FolderUtil" from the command prompt.
pause
