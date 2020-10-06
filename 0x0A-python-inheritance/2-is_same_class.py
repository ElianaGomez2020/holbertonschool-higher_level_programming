#!/usr/bin/python3
""" returns True if the object is an instance of, or if the object """


def is_same_class(obj, a_class):
    """ returns True if the object is exactly an instance """
    if type(obj) is a_class:
        return True
    else:
        return False
