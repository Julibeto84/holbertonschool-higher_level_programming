#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(range(len(matrix)))
    for y, row in enumerate(matrix):
        new_matrix[y] = list(range(len(matrix[y])))
        for x, celda in enumerate(row):
            new_matrix[y][x] = celda * celda
    return new_matrix

        
        
        

