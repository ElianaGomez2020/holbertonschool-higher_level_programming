#!/usr/bin/python3
"""[summary]"""

from models.base import Base


class Rectangle(Base):
    """[summary]

    Args:
        Base ([type]): [description]
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """[summary]"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Getter"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Getter"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        print( '\n' * self.__y + (' ' * self.__x + "#" * self.width 
              + "\n") * self.height, end="")

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, 
                self.x, self.y, self.width, self.height)

    def update(self, *args):
        if len(args) != 0:
            atrib = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, atrib[i], arg)

