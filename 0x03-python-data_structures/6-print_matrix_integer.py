#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for obj in item:
            print("{:d}".format(obj), end=" ")
        print()
