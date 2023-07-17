#!/usr/bin/python3
"""Rectangle Module defining private instance attributes
"""


class Rectangle:
    """Defines the area and perimeter functions"""

    def __init__(self, height=0, width=0):
        """Initialize a new rectangle
        Args:
            width: integer value of rectangle width
            height: integer value of rectangle height
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width value"""
        self.__width = value

    @property
    def height(self):
        """Height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value for the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def perimeter(self):
        """Returns the perimeter value for the Rectangle Created"""
        if self.__width == 0 or self.__height == 0:
            self.__perimeter = 0
        else:
            self.__perimeter = 2 * (self.width + self.height)
        return self.__perimeter

    
    def area(self):
        """Calculates and returns the value for the Rectangle passed"""
        self.__area = self.__width * self.__height
        return self.__area
    