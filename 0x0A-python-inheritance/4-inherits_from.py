#!/usr/bin/python3
""" function that returns True if the object is an instance """


def inherits_from(obj, a_class):
    """  returns True if the object is an instance """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
