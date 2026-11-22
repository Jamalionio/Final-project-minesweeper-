'''core.py - mine placement and reveal with flood fill.

Owner: Jamal Aghasi 
'''

import random

from neighbours import neighbours, compute_numbers


def place_mines(rows, cols, nb_mines, safe_cell):
    '''Randomly place the mines, never on safe_cell.

    Parameters:
        rows, cols (int): board size
        nb_mines (int): number of mines to place
        safe_cell (tuple): (row, col) of the first revealed cell

    Returns:
        set: set of tuples (row, col) containing the mines
    '''
    pass


def reveal(cell, state):
    '''Reveal a cell. If it has 0 neighbouring mines, flood fill.

    Uses a while loop and a list as a stack. Flagged cells are not opened.
    On the first move: place_mines + compute_numbers, then first_move = False.
    If the cell is a mine: state["game_over"] = True, state["hit"] = cell.
    Updates state["revealed"] and state["board"].

    Parameters:
        cell (tuple): (row, col)
        state (dict): game state

    Returns:
        tuple:(False, "text") if the cell is already revealed or flagged, otherwise (True, "")
    '''
    pass
