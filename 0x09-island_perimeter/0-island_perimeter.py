#!/usr/bin/python3
""" Island Perimeter
"""


def island_perimeter(grid):
    """ Function that returns perimeter of the island
    """
    co = 0
    row = len(grid)
    col = len(grid[0]) if row else 0

    for x in range(len(grid)):
        for y in range(len(grid[x])):

            idex = [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]
            check = [1 if k[0] in range(row) and k[1] in range(col) else 0
                     for k in idex]

            if grid[x][y]:
                co += sum([1 if not r or not grid[k[0]][k[1]] else 0
                              for r, k in zip(check, idex)])

    return (co)
