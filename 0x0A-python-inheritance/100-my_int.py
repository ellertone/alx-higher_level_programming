#!/usr/bin/python3
''' module: 100-my_int.py
'''


class MyInt(int):
    ''' Class: MyInt
    '''
    def __init__(self, value):
        '''Initializes MyInt inheritin Int properties
           returns None
        '''
        self.num = value

    def __eq__(self, other):
        '''compares if both are equal
           returns True
        '''
        return self.num != other

    def __ne__(self, other):
        '''compares if both are equal
           returns True
        '''
        return self.num == other
