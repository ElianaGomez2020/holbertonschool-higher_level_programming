#!/usr/bin/python3
""" empty class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        """ validate if area is implemented """
        self.integer_validator('width', width)
        self.integer_validator('heigth', height)
        self.__width = width
        self.__height = height
