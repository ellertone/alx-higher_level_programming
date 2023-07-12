#!/usr/bin/python3
import json
"""module load_from_json_file
"""


def load_from_json_file(filename):
    '''function that creates an Object from a "JSON file".
       returns corresponding Python object
    '''
    with open(filename, 'r') as f:
        return json.loads(f.read())
