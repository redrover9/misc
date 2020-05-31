$pathOfFile = Read-Host -Prompt 'Where would you like to save your output? '
$servername = Read-Host -Prompt 'Input a server name to check CPU and memory usage: '

$cpuUsage = Invoke-Command -ScriptBlock {Get-WmiObject Win32_Processor -ComputerName $servername | Measure-Object -Property LoadPercentage -Average | Select Average}
Write-Host 'CPU Load Average: ' | Tee-Object -Append -FilePath $pathOfFile
$cpuUsage | Tee-Object -Append -FilePath $pathOfFile

$detailedCPUUsage = Invoke-Command {Get-Counter -Counter '\Processor(_Total)\*' -ComputerName $servername}
Write-Host 'Detailed CPU Info: ' | Tee-Object -Append -FilePath $pathOfFile
$detailedCPUUsage | Tee-Object -Append -FilePath $pathOfFile

$memoryUsage = Invoke-Command {Get-Counter '\Memory\AvailableMBytes' -ComputerName $servername}
Write-Host 'Memory available in MB: ' | Tee-Object -Append -FilePath $pathOfFile
$memoryUsage | Tee-Object -Append -FilePath $pathOfFile

$detailedMemoryUsage = Invoke-Command {Get-Counter '\Memory\*' -ComputerName $servername}
Write-Host 'Detailed Memory Info:' | Tee-Object -Append -FilePath $pathOfFile
$detailedMemoryUsage | Tee-Object -Append -FilePath $pathOfFile

$serverProcesses = Invoke-Command -ScriptBlock {Get-Process | Sort CPU -Descending} -ComputerName $servername
Write-Host 'Server Processes:' | Tee-Object -Append -FilePath $pathOfFile
$serverProcesses | Tee-Object -Append -FilePath $pathOfFile

while ($true) {
Invoke-Command -ScriptBlock {$selectedProcess = Read-Host -Prompt 'Select a PID to view info about it in more detail: ' 
Get-Process -Id $selectedProcess | Format-List *} -ComputerName $serverName | Tee-Object -Append $pathOfFile
}