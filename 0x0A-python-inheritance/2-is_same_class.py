#!/usr/bin/python3


def is_same_class(obj, a_class):
    """  returns True if the object is exactly an instance """
    if type(obj) is a_class:
        return True
    else:
        return False
