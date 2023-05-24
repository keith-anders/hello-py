# Hello Python

This is a starter repository for setting up a new python project on a Windows computer. It uses the python venv module to contain a virtual environment for isolating dependencies.

## Getting started

### Make sure Python is installed

Make sure you have python installed. Version 3.3 or later is required for this project.

```batch
python --version
```

If Python is not installed, you can install it via winget. To get the list of available versions:

```batch
winget search Python.Python --source=winget
```

To install one, use its Id column (say, `Python.Python.3.11`) like so:

```batch
winget install --id Python.Python.3.11
```

### Make sure Git is installed

Make sure you have git installed so as to be able to clone this repository. If not, you can install it from winget:

```batch
winget install --id Git.Git
```

### Actually Getting Started

Clone this repository:

```batch
git clone git@github.com:keith-anders/hello-py.git
```

Then enter the repository and create the virtual environment. This should be done *before* opening VS Code here, so that the proper interpreter will exist

```batch
python -m venv venv
```

## Commands

All of these commands are encapsulated in powershell scripts in this directory.

To set the venv's packages from the REQUIREMENTS.txt file (this must be done immediately after creating the venv):

```batch
pip install -r REQUIREMENTS.txt
```

To activate the venv for the current terminal:

```batch
venv\Scripts\activate.bat
```

To delete the venv:

```batch
rmdir /S /Q venv
```

To deactivate the venv for the current terminal:

```batch
deactivate
```

To save the venv's current packages to the REQUIREMENTS.txt file:

```batch
pip freeze > REQUIREMENTS.txt
```

To execute the main script (assuming the venv is activated for the current terminal):

```batch
python src\calculator\main.py other args-to pass
```

To run the unit tests (assuming the venv is activated for the current terminal):

```batch
python -m unittest discover -v -s ./tests -p test*.py
```
