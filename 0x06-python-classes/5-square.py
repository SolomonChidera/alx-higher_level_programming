#!/usr/bin/python3

"""Defines a square module."""


class Square:
    """Represents a Square class"""

    def __init__(self, size=0):
        """Initialize a square

        Args:
            size (int): size of the square
        """
        self.__size = size

    @property
    def size(self):
        """Get/set size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Finds area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for x in range(self.__size):
            for y in range(self.__size):
                print("{}".format("#"), end="")
            print()
