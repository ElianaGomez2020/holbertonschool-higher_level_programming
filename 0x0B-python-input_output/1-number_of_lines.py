#!/usr/bin/python3
""" Returns the number of lines of a text file"""


def number_of_lines(filename=""):
    """Returns the number of lines of a text file """
    with open(filename, 'r', 'utf8') as my_file:
        return sum(1 for line in my_file)
