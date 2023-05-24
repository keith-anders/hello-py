# Hello Python

This is a starter repository for setting up a new python project on a Windows computer. It uses the python venv module to contain a virtual environment for isolating dependencies.

## Clone

Start by cloning this repository:

```bash
git clone foo
```

## Commands

All of these commands are encapsulated in powershell scripts in this directory.

To create the venv:

```batch
python -m venv venv
```

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
