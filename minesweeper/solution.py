
from itertools import product

def count_mines(field, location):
    """calculates the number of mines in a x/y position"""
    x, y = location
    s = ''
    for xd, yd in product([-1, 0, +1], [-1, 0, +1]):
        xnew, ynew = x + xd, y + yd
        if 0 <= xnew <= len(field[0]) and 0 <= y <= len(field):
            s += field[y-1][x-1]
    return s.count('*')
