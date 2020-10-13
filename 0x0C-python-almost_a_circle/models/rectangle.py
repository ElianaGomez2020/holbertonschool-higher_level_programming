#!/usr/bin/python3
"""This is a module for a Class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from Class Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """This is a method initalizer"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter method to width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Getter method to height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Getter method to height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Getter method to x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method to x"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Getter method to y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method to y"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ In this method it compute the area value"""
        return self.__width * self.__height

    def display(self):
        """This method prints in stdout the Rectangle"""
        print('\n' * self.__y + (' ' * self.__x + "#" * self.width +
              '\n') * self.height, end="")

    def __str__(self):
        """This method returns the string
        representation of the object"""
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Update the argument of Rectangle"""
        if len(args) != 0:
            atrib = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, atrib[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x,
                'y': self.y}
