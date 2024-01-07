#!/usr/bin/python3
"""Defines a divide fn for a matrix"""
def matrix_divided(matrix, div):
    """Divides all matrix elements.

    Args:
        matrix (list): (list of lists) of integers/floats
        div (int/float): division sign

    Raises:
        TypeError: If not an int
        TypeError: if matrices are of different sizes
        TypeError: if div != int/float
        ZeroDivisionError: if div = 0

    Return:
        division result in a matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or not all((isinstance(ele, int)
        or isinstance(ele, float)) for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of " "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
