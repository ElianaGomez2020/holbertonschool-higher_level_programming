#!/usr/bin/python3
"""In this module it create a Class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the instance attributes"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getter method to size"""
        return self.width

    @size.setter
    def size(self, size):
        """Setter method to size"""
        self.width = size
        self.height = size

    def __str__(self):
        return('[Rectangle] ({}) {}/{} - {}'.format(self.id,
               self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """Update the argument of Square"""
        if len(args) != 0:
            atrib = ["id", "size," "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, atrib[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x,
                'y': self.y}
