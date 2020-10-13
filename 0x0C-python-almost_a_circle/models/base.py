#!/usr/bin/python3
"""[summary]"""

import json


class Base:
    """[summary]"""
    __nb_objects = 0

    def __init__(self, id=None):
        """[summary]

        Args:
            id ([type], optional): [description]. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return'[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        s_list = []
        for obj in list_objs:
            obj = obj.to_dictionary()
            s_list.append(obj)
        json_string = cls.to_json_string(s_list)
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="UTF-8") as f:
            f.write(json_string)
    
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == []:
            return '[]'
        return json.loads(json_string)
