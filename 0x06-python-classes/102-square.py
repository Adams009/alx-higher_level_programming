#!/usr/bin/python3

class Square:
    """
    This is the Square class.

    The Square class defines a square with private instance attributes: size.
    It has properties to retrieve and set the size, a method for calculating
    the area, and supports comparison operators based on the square area.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (float or int): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size of the square.

        Returns:
        - float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size of the square.

        Parameters:
        - value (float or int): The new size of the square.

        Raises:
        - TypeError: If the value is not a number.
        - ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparison based on square area."""
        return self.area() == other.area() if isinstance(other, Square) else False

    def __ne__(self, other):
        """Inequality comparison based on square area."""
        return self.area() != other.area() if isinstance(other, Square) else True

    def __gt__(self, other):
        """Greater than comparison based on square area."""
        return self.area() > other.area() if isinstance(other, Square) else False

    def __ge__(self, other):
        """Greater than or equal comparison based on square area."""
        return self.area() >= other.area() if isinstance(other, Square) else False

    def __lt__(self, other):
        """Less than comparison based on square area."""
        return self.area() < other.area() if isinstance(other, Square) else False

    def __le__(self, other):
        """Less than or equal comparison based on square area."""
        return self.area() <= other.area() if isinstance(other, Square) else False
