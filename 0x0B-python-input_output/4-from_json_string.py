#!/usr/bin/python3
''' Module: from_json_string
'''

import json


def from_json_string(my_str):
    '''Function: Returns an object represented by a JSON string
       Returns: Python objects
    '''
    return json.loads(my_str)
