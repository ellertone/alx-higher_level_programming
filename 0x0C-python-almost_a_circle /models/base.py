#!/usr/bin/python3

"""Initiating a python package"""


class Base:
    """The base class for the package"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Inititialization of the base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
