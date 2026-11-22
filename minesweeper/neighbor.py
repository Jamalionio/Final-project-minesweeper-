'''neighbors.py - neighbor search and numbers around cells.

Owner: Jamal Aghasi
'''


def neighbors(row, col, rows, cols):
    '''Find all existing neighboring cells (up to 8).

    Parameters:
        row, col (int): the cell
        rows, cols (int): board size

    Returns:
        list: list of tuples (row, col) of the neighbors inside the board
              (3 for a corner, 5 for an edge, 8 in the middle)
    '''
    pass


def count_adjacent(row, col, rows, cols, mines):
    '''Count the mines around one cell (uses neighbours).

    Parameters:
        row, col (int): the cell
        rows, cols (int): board size
        mines (set): positions of the mines

    Returns:
        int: number of neighbouring mines
    '''
    pass


def compute_numbers(rows, cols, mines):
    '''Compute the numbers for the whole board (uses count_adjacent).

    Parameters:
        rows, cols (int): board size
        mines (set): positions of the mines

    Returns:
        list: list of lists of int; a cell with a mine gets -1
   '''
    pass
