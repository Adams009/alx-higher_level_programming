#!/usr/bin/python3
""" Square module"""


class Square:
    """This is the Square class. """

    def __init__(self, size=0):
        """Initializes a new instance of the Square class.

        Args:
            size: The size of the square
        """
        self.size = size

    @property
    def size(self):
        """proprty for the length

        Raises:
            TypeError: when not an int
            ValueError: when less than zero
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ Area of a square

        Returns:
            size of square
        """
        return self.__size ** 2
