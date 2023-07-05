#!/usr/bin/python3

"""
Module for printing the Name entered by user
"""


def say_my_name(first_name, last_name=""):
    """
    Function for storing the names entered
    Keyword arguments:
        first_name -> string
        last_name -> string
    """

    # Error messages
    err_msg_first = "first_name must be a string"
    err_msg_last = "last_name must be a string"

    # Tests
    if not isinstance(first_name, str):
        raise TypeError(err_msg_first)
    if not isinstance(last_name, str):
        raise TypeError(err_msg_last)

    # print name
    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
