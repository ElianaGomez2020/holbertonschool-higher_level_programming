#!/usr/bin/python3
"""This mnodule define a Rectangule class"""


class Rectangle:
    """This is a rectangule class"""

    def __init__(self, width=0, height=0):
        """This __init__ method initialize an instance with a private
        instance attributte width and height.
        Keyword Arguments:
            width {int} -- Input value of width (default: {0})
            height {int} -- Input value of height (default: {0})
        """

        self.width = width
        self.height = height

    @property
    def height(self):
        """Height attribute getter method"""
        return self.__height

    @height.setter
    def height(self, height):
        """height attribute setter method
        Arguments:
            height {int} -- Input value of height
        """
        if isinstance(height, int) is True:
            if height < 0:
                raise ValueError("height must be >= 0")
            else:
                    self.__height = height
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """Width attribute getter method"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width attribute setter method
        Arguments:
            width {int} -- Input value of height
        """
        if isinstance(width, int) is True:
            if width < 0:
                raise ValueError("width must be >= 0")
            else:
                    self.__width = width
        else:
            raise TypeError("width must be an integer")
