#!/usr/bin/python3
"""The function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """---"""

    matrixError = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(matrixError)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError(
                    "Each row of the matrix must have the same size"
            )
    new_mat = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = []
        for elm in row:
            if not isinstance(elm, (int, float)):
                raise TypeError(matrixError)
            new_row.append(round(elm / div, 2))
        new_mat.append(new_row)

    return new_mat
