#!/usr/bin/python3i
''' module: 7-base_geometry.py
'''


class BaseGeometry:
    ''' Class: BaseGeometry
    '''
    def area(self):
        '''raises an Exception with the message
           returns None
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''raises a TypeError exception if not int
           raises a ValueError exception if le than 0
           returns None
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0". format(name))
