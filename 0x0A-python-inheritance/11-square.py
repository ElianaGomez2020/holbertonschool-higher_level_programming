#!/usr/bin/python3
""" empty class """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size):
        self.__size = size
        super().integer_validator('size', size)
        super().__init__(size, size)

    def __str__(self):
        """return string representation of ibject"""
        return '[Square] {}/{}'.format(self.__size, self.__size)
