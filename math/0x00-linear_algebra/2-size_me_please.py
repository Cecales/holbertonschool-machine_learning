#!/usr/bin/env python3
""" calculate the shape of a matrix"""


def matrix_shape(matrix):
    """ calculate the shape of a matrix """
    shape = [len(matrix)]
    while type(matrix[0]) != int:
        shape.append(len(matrix[0]))
        matrix = matrix[0]
    return shape
