#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, celda in enumerate(row):
            if index != len(row) - 1:
                print("{:d}".format(celda), end=" ")
            else:
                print("{:d}".format(celda), end="")
        print()
