# AppForge rebrand (Windows PowerShell)
# source: doxigo/muchToman
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
if (Get-Command python -ErrorAction SilentlyContinue) {
  python -c "exec(open('rebrand.py', encoding='utf-8').read())" 
} elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
  python3 -c "exec(open('rebrand.py', encoding='utf-8').read())" 
} else {
  Write-Host 'Python is required. Install Python 3, then rerun.'
}