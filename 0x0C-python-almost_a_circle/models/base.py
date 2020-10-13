#!/usr/bin/python3
"""Class Base"""

import json


class Base:
    """This is class a Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is a method initializer"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns Json string representation of lis_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return'[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs"""
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
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == []:
            return '[]'
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if dictionary is not None:
            new_ins = cls(2, 3)
            new_ins.update(**dictionary)
            return(new_ins)
        return None

    @classmethod
    def load_from_file(cls):
        obj_list = []
        filename = str(cls.__name__) + '.json'
        try:
            with open(filename, 'r', encoding='UTF-8') as f:
                content = f.read()
                obj_l = cls.from_json_string(content)
                for ins_dict in obj_l:
                    obj_list.append(cls.create(**ins_dict))
                return obj_list
        except FileNotFoundError:
            return obj_list
