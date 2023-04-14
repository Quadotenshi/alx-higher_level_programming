#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for item in matrix:
        double = map(lambda x: x*x, item)
        new_matirx.append(list(double))
    return new_matrix
