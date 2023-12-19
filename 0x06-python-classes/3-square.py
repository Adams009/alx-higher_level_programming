#!/usr/bin/python3
""" Square module"""


class Square:
    """This is the Square class. """

    def __init__(self, size=0):
        """Initializes a new instance of the Square class.

        Args:
            size: The size of the square

        Raises:
            TypeError: when not an int
            ValueError: when less than zero
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """ Area of a square

        Returns:
            size of square
        """
        return self.__size ** 2
