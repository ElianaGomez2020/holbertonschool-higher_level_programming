#!/usr/bin/python3
"""Returns the dictionary description with simple data structure"""


class Student:
    """defines a student """
    def __init__(self, first_name, last_name, age):
        """Instantiation Public instance attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Studen"""
        if attrs is not None:
            new_dic = {}
            for i in attrs:
                if i in self.__dict__:
                    new_dic[i] = self.__dict__[i]
            return new_dic
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        self.__dict__ = json
