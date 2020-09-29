#!/usr/bin/python3
"""This module define a Rectangle Class
"""


class Rectangle:
    """
    This is rectangle class
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """__init__ initialize metod an with a private inistance
        attribute width and height

        Args:
            width . Defaults to 0.
            height . Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter method width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter method width attribute
        """
        self.__width = value
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

    @property
    def height(self):
        """getter method height attribute
        """
        return self.__heigth

    @height.setter
    def height(self, value):
        """setter method height attribute
        """
        self.__height = value
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

    def area(self):
        """Return the rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """Return the rectangle parimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return((self.__width + self.__height) * 2)

    def __str__(self):
        if self.width is 0 or self.__height is 0:
            return ''
        str_object = ''
        for i in range(self.__height):
            for j in range(self.__width):
                str_object += str(self.print_symbol)
            if i < self.__height - 1:
                str_object += '\n'
        return str_object

    def __repr__(self):
        return("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """
        """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This method validate which is the biggest rectangle
            and return the biggest
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        """
        return cls(size, size)
