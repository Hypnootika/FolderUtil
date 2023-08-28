# Run as administrator
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]"Administrator"))
{
    Start-Process powershell -Verb RunAs "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`""
    Exit
}

# Prompt for the path to FolderUtil.exe
$exe_path = Read-Host "Enter the full path to FolderUtil.exe"

Write-Host "You entered: $exe_path"

# Check if the file exists
$exists = [System.IO.File]::Exists($exe_path)
Write-Host "File exists: $exists"

if ($exists)
{
    # Define the registry key and value
    $registryPath = "Registry::HKEY_CLASSES_ROOT\Directory\Background\shell\FolderUtil-Dump-folder"
    $registryKey = "Registry::HKEY_CLASSES_ROOT\Directory\Background\shell\FolderUtil-Dump-folder\command"
    $registryValue = "$exe_path -ud"

    # Create the registry key and value
    New-Item -Path $registryPath -Force
    New-Item -Path $registryKey -Force
    Set-ItemProperty -Path $registryKey -Name "(Default)" -Value $registryValue

    Write-Host "Context menu item added. You may need to restart Explorer or your computer for the changes to take effect."
}
else
{
    Write-Host "Invalid path. Context menu item not added."
}

# Pause before closing
Write-Host "Press any key to continue ..."
$null = $host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
