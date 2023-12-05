#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        if row:
            print("{}".format(row[0]), end="")
            for num in row[1:]:
                print(" {}".format(num), end="")
            print()
        else:
            print()
