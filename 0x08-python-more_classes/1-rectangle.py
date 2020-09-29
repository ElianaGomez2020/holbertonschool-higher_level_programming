#!/usr/bin/python3
"""This module define a Rectangle Class
"""


class Rectangle:
    """
    This is rectangle class
    """
    def __init__(self, width=0, height=0):
        """__init__ initialize metod an with a private inistance
        attribute width and height

        Args:
            width . Defaults to 0.
            height . Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter method width attribute
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """getter method height attribute
        """
        return self.__heigth

    @height.setter
    def height(self, value):
        """setter method height attribute
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
