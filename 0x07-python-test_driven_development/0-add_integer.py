#!/usr/bin/python3

"""
Addition of two integers
"""


def add_integer(a, b=98):
    """Adds two numbers and returns the result"""

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
