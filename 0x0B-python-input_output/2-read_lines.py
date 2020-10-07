#!/usr/bin/python3
""" reads n lines of a text file (UTF8) and prints"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file """
    with open(filename, 'r', encoding='utf-8') as my_file:
        num = my_file.readlines()
        if nb_lines <= 0 or nb_lines > len(num):
            nb_lines = len(num)
        for i in range(nb_lines):
            print(num[i], end='')
    return i + 1
