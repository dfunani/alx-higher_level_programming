#!/usr/bin/python3
"""
0-matrix_dividend is a module containg 1 function
member functions matrix_dividend(matrix, div)
"""

def matrix_divided(matrix, div):
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for col in row:
            if type(col) != int and type(col) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
