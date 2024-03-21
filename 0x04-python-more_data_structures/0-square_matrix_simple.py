#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
        This function computes the square of all
        integers of a matrix
    Args:
        matrix: The matrix of integer
    Return:
        A matrix
    """

    newmatrix = list(map(lambda x: [i * i for i in x], matrix))
    return newmatrix
