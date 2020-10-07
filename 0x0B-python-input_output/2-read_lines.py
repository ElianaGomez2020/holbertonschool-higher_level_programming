#!/usr/bin/python3
""" reads n lines of a text file (UTF8) and prints"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file """
    with open(filename, 'r', encoding='utf-8') as my_file:
        if nb_lines <= 0:
            print(my_file.read())
            return
        for i in range(nb_lines):
            print(my_file.readline())
