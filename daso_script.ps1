# Check if the script is running as administrator
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    # Relaunch the script with administrator privileges
    $arguments = "& '" + $myinvocation.mycommand.definition + "'"
    Start-Process powershell -Verb runAs -ArgumentList $arguments
    Exit
}

# General output text
Write-Output "Welcome to the DASO installer!"

# Get the directory of the script
$scriptPath = Split-Path -Parent -Path $MyInvocation.MyCommand.Definition
$srcPath = Join-Path -Path $scriptPath -ChildPath "src"

# Add src directory to system PATH
$envPath = [System.Environment]::GetEnvironmentVariable("Path", [System.EnvironmentVariableTarget]::Machine)
if (-not ($envPath.Split(';') -contains $srcPath)) {
    $newPath = $envPath + ";" + $srcPath
    [System.Environment]::SetEnvironmentVariable("Path", $newPath, [System.EnvironmentVariableTarget]::Machine)
    Write-Output "The directory has been added to your system PATH."
} else {
    Write-Output "The directory is already in your system PATH."
}

Read-Host -Prompt "Press Enter to exit setup..." # Wait for user input before closing the window
