#!/usr/bin/python3
"""This module defines a class named Rectangle."""


class Rectangle:
    """
    This class defines a rectangle.
    Attributes
    ----------
    __height : int
        The height of the rectangle.
    __width : int
        The width of the rectangle.
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.
        Returns
        -------
        __height : int
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.
        Parameters
        ----------
        value : int
            The value for the height of the rectangle.
        Raises
        ------
        TypeError
            If the value is not an integer.
        ValueError
            If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.
        Returns
        -------
        __width : int
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.
        Parameters
        ----------
        value : int
            The value for the width of the rectangle.
        Raises
        ------
        TypeError
            If the value is not an integer.
        ValueError
            If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        Method for calculating the rectangle's area.
        Returns
        -------
            int
                The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Method for calculating the perimeter of the rectangle.
        Returns
        -------
            int
                The perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
