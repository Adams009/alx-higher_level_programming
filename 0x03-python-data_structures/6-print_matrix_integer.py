#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    else:
        for list_in_row in matrix:
            for idx_in_row in list_in_row:
                print("{}".format(idx_in_row), end=" ")
            print()
