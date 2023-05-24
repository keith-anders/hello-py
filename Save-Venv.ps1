[CmdletBinding()]
param (
)

$contents = pip freeze
Set-Content -Path .\REQUIREMENTS.txt -Value $contents
