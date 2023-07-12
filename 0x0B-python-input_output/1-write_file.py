#!/usr/bin/python3
'''Module: 1-write_file
'''


def write_file(filename="", text=""):
    ''' Function: write text to file
        Return: number of characters
    '''
    if filename == "" or type(filename) != str:
        return 0
    with open(filename, 'w') as a_file:
        return a_file.write(text)
    counter = 0
    with open(filename, 'r') as a_file:
        for line in a_file:
            counter += 1
    return counter
