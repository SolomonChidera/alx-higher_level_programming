#!/usr/bin/python3
"""
Area and perimeter of a rectangle
"""


class Rectangle:
    """
    a class Rectangle that defines
    a rectangle by: (based on 1-rectangle.py)
    Private instance attribute: width
    Private instance attribute: height
    Public instance method: def area(self)
    Public instance method: def perimeter(self)
    """
    def __init__(self, width=0, height=0):
        """Initializes the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returns the rectangle area
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        that returns the rectangle perimeter
        """
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return ((self.__width*2) + (self.__height*2))
