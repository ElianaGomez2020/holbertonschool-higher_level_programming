#!/usr/bin/python3


class MyList(list):
    """ class = MyList """
    def print_sorted(self):
        """ prints the list, but sorted """
        print(sorted(self))
