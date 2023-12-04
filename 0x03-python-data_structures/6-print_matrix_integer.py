#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    else:
        for row in matrix:
            line = " ".join("{}".format(num) for num in row)
            print(line)
