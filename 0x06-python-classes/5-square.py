#!/usr/bin/python3
""" the square module"""


class Square:
    """ This is the Square class. """

    def __init__(self, size=0):
        """Initializes a new instance of the Square class.

        Args:
            size: The size of the square
        """
        self.size = size

    @property
    def size(self):
        """ Getter method for retrieving the size

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for setting the size of the square.

        Args:
            value: The new size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Calculates and returns the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """ Prints the square with the character # to stdout."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
