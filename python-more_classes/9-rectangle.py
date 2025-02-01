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
        number_of_instances : int
            The number of instances.
        print_symbol
            The symbol used for representing the rectangle as a string.
    Methods
    -------
        area(self):
            Method for calculating the rectangle's area.
        perimeter(self):
            Method for calculating the rectangle's perimeter.
        bigger_or_equal(rect_1, rect_2):
            Returns the bigger rectangle based on the area.
        square(cls, size=0):
            Returns a new instance of the Rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        Creates a string representation of the rectangle using '#'.
        Returns
        -------
            rectangle : str
                A string that represents the rectangle with '#'.
            If either the width or height is 0, an empty string is returned.
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle = ""
        for height in range(self.__height):
            for width in range(self.__width):
                rectangle += str(self.print_symbol)
            if height < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """
        Returns a string representation of the rectangle for debugging.
        Returns
        -------
            A representation of the rectangle that can be used to recreate.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletes an instance of the Rectangle class and prints a message.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the bigger rectangle based on the area.
        Raises
        ------
            TypeError
                If rect_1 or rect_2 is not an instance of the Rectangle class.
        Returns
        -------
        Rectangle
           The rectangle with the larger area. If both rectangles have the same
           area, rect_1 is returned.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """
        Returns a new instance of the Rectangle class
        with width and height equal to size.
        Parameters
        ----------
            size : int, optional
                The size of the square's sides (default is 0).
        Returns
        -------
            Rectangle
                A new instance of Rectangle with
                width and height equal to size.
        """
        return Rectangle(size, size)
