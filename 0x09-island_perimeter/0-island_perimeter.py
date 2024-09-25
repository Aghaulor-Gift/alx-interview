#!/usr/bin/python3
"""
This module defines the function `island_perimeter` to compute the perimeter
of an island in a grid.
"""

def island_perimeter(grid):
    """
    This function calculates the perimeter of an island in a grid.

    Args:
        grid (list of list of int): A 2D grid where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island in the grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2
                
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2

    return perimeter
