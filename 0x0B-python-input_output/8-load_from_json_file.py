#!/usr/bin/python3
"""  creates an Object from a JSON file"""

import json


def load_from_json_file(filename):
    """ creates an Object from a JSON file """
    with open(filename, 'r') as my_file:
        return json.load(my_file)