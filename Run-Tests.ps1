[CmdletBinding()]
param (
)

python -m unittest discover -v -s ./tests -p test*.py
