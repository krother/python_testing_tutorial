
def count_mines(field, location):
    """calculates the number of mines in a x/y position"""
    x, y = location
    s = ''
    if x > 0 and y > 0:
        s += field[x-1][y-1]
    ...
    return s.count('*')


