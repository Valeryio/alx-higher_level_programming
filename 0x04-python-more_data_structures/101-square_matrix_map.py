#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map((lambda x: [i * i for i in x]), matrix))
