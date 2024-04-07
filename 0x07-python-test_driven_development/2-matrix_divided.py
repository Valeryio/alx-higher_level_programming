#!/usr/bin/python3
"""
    This modules handle a function that makes a division
    :param matrix: a matrix
    :return matrix: a new matrix
"""

def matrix_divided(matrix, div):
    """This function divides all the elements of a matrix
    """

# Matrix shoudl be a list of list of integer or floats
    
    if isinstance(matrix, list):
        for submatrix in matrix:
            if len(submatrix) != len(matrix[0]):
                raise TypeError("Each row of the matrix must have the same size")
            if isinstance(submatrix, list):
                for j in range(len(submatrix)):
                    if not isinstance(submatrix[j], (int, float)):
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if int(div) == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for submatrix in matrix:
        new_submatrix = []
        for i in range(len(submatrix)):
            op = submatrix[i] / div
            new_submatrix.append(round(op, 2))

        new_matrix.append(new_submatrix)

    return new_matrix
