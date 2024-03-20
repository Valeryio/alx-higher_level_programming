#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
        This function prints a matrix

    Args:
        matrix: matrix

    Returns:
        Returns nothing
    """

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            if (j < (len(matrix[i]) - 1)):
                print("{:d}".format(matrix[i][j]), end=" ")
            else:
                print("{:d}".format(matrix[i][j]))

