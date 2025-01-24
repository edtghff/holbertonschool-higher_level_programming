#!/usr/bin/python3
"""This module defines the function `print_square`."""


def print_square(size):
    """
    Prints a square of '#' characters with the given size.

    Args:
        size (int): The size of the square. Must be a non-negative integer.

    Raises:
        TypeError: If size is not an integer or if it is a negative float.
        ValueError: If size is a negative integer.

    Examples:
        >>> print_square(2)
        ##
        ##
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
