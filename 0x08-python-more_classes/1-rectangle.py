#!/usr/bin/python3
""" The Rectangle Class """

class Rectangle:
    """ announcing the properties in it """
    def __init__(self, width=0, height=0):
        """ the assignment """
        self.width = width
        self.heigth = height

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
        def heigth(self, value):
            """ retriever private instance attribute height """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
