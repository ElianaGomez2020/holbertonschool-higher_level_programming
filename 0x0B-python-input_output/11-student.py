#!/usr/bin/python3
"""Returns the dictionary description with simple data structure"""


class Student:
    """defines a student """
    def __init__(self, first_name, last_name, age):
        """Instantiation Public instance attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Studen"""
        return self.__dict__
