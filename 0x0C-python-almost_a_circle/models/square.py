#!/usr/bin/python3
"""[summary]"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ ee"""
    def __init__(self, size, x=0, y=0, id=None):
        '''initialize the instance attributes'''
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """[]"""
        return self.width

    @size.setter
    def size(self, size):
        """[summary]"""
        self.width = size
        self.height = size

        
    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}'.format(self.id, 
                self.x, self.y, self.width)

def update(self, *args, **kwargs):
        if len(args) != 0:
            atrib = ["id", "size," "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, atrib[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

def to_dictionary(self):
    return {'id': self.id,'size': self.size,'x': self.x,
            'y': self.y}