#!/usr/bin/python3
"""
Rotate a 2D matrix 90 degrees clockwise in place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix 90 degrees clockwise.

    Args:
    matrix (list of list of int): 2D matrix to be rotated

    Returns:
    None: Rotates the matrix in place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row to achieve a 90-degree rotation
    for i in range(n):
        matrix[i].reverse()
