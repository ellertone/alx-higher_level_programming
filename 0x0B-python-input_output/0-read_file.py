#!/usr/bin/python3
'''Module: 0-read_file.py
'''


def read_file(filename=""):
    '''Reads a text file (UTF8) and prints it to stdout
       Returns none
    '''
    with open(filename, "r", encoding="utf-8") as a_file:
        print(a_file.read(), end="")
