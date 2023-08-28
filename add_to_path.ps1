# Run as administrator
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]"Administrator"))
{
    Start-Process powershell -Verb RunAs "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`""
    Exit
}

# Get the executable path from the user
$exe_path = Read-Host "Enter the path to the FolderUtil.exe"

# Get the current PATH
$current_path = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::User)

# Calculate the new length
$new_length = $current_path.Length + $exe_path.Length + 1

# Update the PATH if within limits
if ($new_length -lt 2048)
{
    [Environment]::SetEnvironmentVariable('Path', "$current_path;$exe_path", [EnvironmentVariableTarget]::User)
    Write-Host "Path updated. You may need to restart your command prompt or computer."
}
else
{
    Write-Host "Cannot update PATH. The new PATH would exceed the maximum character limit."
}

# Pause before closing
Write-Host "Press any key to continue ..."
$null = $host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
