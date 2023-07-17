#!/usr/bin/python3
"""Module for class Square that inherits from module rectangle"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """A square is a rectangle with similar sides"""
    
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id)
        self.__size = size
        self.__x = x
        self.__y = y
        