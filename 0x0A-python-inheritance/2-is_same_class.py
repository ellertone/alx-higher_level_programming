#!/usr/bin/python3
'''function: is_same_class
'''


def is_same_class(obj, a_class):
    '''obj: an object
    a_class: a class
    Returns: Bool
    '''
    return type(obj) == a_class
