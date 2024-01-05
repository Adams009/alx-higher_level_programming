#!/usr/bin/python3
""" The Rectangle Class """


class Rectangle:
    """ announcing the properties in it """
    def __init__(self, width=0, height=0):
        """ the assignment """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ retriever private instance attribute width """
        return self.__width

    @width.setter
    def width(self, value):
        """ retriever private instance attribute width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ retriever private instance attribute height """
        return self.__height

    @height.setter
    def height(self, value):
        """ retriever private instance attribute height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ calculating area of rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ claculating perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width for j in range(self.__height))

        return string
