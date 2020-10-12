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
