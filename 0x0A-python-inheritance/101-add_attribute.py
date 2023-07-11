#!/usr/bin/python3
''' module: 101-add_attribute.py
'''


def add_attribute(*args):
    '''raises a TypeError with the message if condition fails
       returns None
    '''
    if "main" in str(type(args[0])):
        setattr(args[0], args[1], args[2])
    else:
        raise TypeError("can't add new attribute")
