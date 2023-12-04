#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for r in matrix:
        print(" ".join("{}".format(num) for num in r))
