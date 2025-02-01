#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """Represents a square with a given size."""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Sets the size of the value with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
    
    def __str__(self):
        """Returns a string representation of the Square instance."""
        return f"Square(size={self.__size})"
