#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in x:
            if y == (len(x) - 1):
                end = ""
            else:
                end = " "
            print("{:d}".format(y), end = end)
