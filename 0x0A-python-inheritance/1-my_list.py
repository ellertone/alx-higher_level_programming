#!/usr/bin/python3
''' Module: class MyList that inherits from list
'''


class MyList(list):
    ''' Represents a MyList
    '''

    def print_sorted(self):
        '''
        prints the list in ascending order
        '''
        print(sorted(self))
