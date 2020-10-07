#!/usr/bin/python3
""" reads n lines of a text file (UTF8) and prints"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file """
    with open('my_file_0.txt', 'r') as my_file:
        if nb_lines <= 0 or nb_lines >= len(my_file.readlines()):
            print(my_file.read())
        else:
            print(my_file.readline())
