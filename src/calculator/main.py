#!../../venv/bin/python
"""Runs the program
"""
import sys

if __name__ == '__main__':
    print('Hello world')
    for i, arg in enumerate(sys.argv):
        print(f'Argument #{i}: {arg}')
