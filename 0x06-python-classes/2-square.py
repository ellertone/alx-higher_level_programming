#!/usr/bin/python3
'''Defining a  square with optional classes'''


class Square:
    '''dOptional Class attribute size'''
    pass

    def __init__(self, size=0):
        '''Initialization for class Square'''
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
