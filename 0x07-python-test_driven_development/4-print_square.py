#!/usr/bin/python3
"""
Module for printing a square using hashes(#)
"""


def print_square(size):
    """
    Function to decide the size of the square
    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif isinstance(size, bool) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)

