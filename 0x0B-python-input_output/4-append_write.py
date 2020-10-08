#!/usr/bin/python3
""" appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, 'w', encoding='utf-8') as my_file:
        my_file.write(text)
    return len(text)
