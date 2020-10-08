#!/usr/bin/python3
""" writes an Object to a text file, using a JSON"""

import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON """
    with open(filename, 'w') as my_file:
        json.dump(my_obj, my_file)
