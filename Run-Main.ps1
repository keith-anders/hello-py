[CmdletBinding()]
param (
    [Parameter(Mandatory=$True,ValueFromRemainingArguments=$true,Position=0)][string[]]$Args
)

$pythonArgs = @('src\calculator\main.py')
$pythonArgs += $Args
& 'python' $pythonArgs
