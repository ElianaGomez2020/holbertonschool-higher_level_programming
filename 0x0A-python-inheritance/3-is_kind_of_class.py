#!/usr/bin/python3
""" function that returns True if the object is an instance """


def is_kind_of_class(obj, a_class):
    """  returns True if the object is an instance """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
