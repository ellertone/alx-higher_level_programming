#!/usr/bin/python3
'''Module: 2-append_write
'''


def append_write(filename="", text=""):
    '''Function: Appends string to text file with UTF8 encoding
       Return: number of characters added
    '''
    with open(filename, 'a') as a_file:
        return a_file.write(text)
    count = 0
    for char in text:
        count += 1
    return count
