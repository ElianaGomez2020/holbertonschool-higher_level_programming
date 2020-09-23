#!/usr/bin/python3
"""Square class a private instance attribute init in 0"""


class Square:
    """Attribute size"""
    def __init__(self, size=0):
        """
        Init  a square

        Args:
            size(int): size of square
        """
        self.size = size

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

    def area(self):
        return self.__size ** 2
    
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()

