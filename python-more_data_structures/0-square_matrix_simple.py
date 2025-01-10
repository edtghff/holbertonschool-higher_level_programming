#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for i in range(len(matrix)):
        row = []
        for j in matrix[i]:
            row.append(j*j)
        square.append(row)
    return square
