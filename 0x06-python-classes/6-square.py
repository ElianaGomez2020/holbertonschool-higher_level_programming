#!/usr/bin/python3
"""Square class a private instance attribute init in 0"""


class Square:
    """Attribute size"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Init  a square

        Args:
            size(int): size of square
        """
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """ Setter to size"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or \
           type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for b in range(self.__size):
            for c in range(self.__position[0]):
                print(' ', end='')
            for d in range(self.__size):
                print('#', end='')
            print()
