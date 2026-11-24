'''core.py - mine placement and reveal with flood fill.

Owner: Jamal Aghasi 
'''

import random

from neighbour import neighbours, compute_numbers


def place_mines(rows, colms, nb_mines, safe_cell):
    '''Randomly place the mines, never on safe_cell.

    Parameters:
        rows, cols (int): board size
        nb_mines (int): number of mines to place
        safe_cell (tuple): (row, col) of the first revealed cell

    Returns:
        set: set of tuples (row, col) containing the mines
    '''
    
    mines = set()
    while len(mines) < nb_mines:
        mine = (random.randint(0, rows - 1), random.randint(1, colms - 1))
        if mine == safe_cell or mine in mines:
                continue
        mines.add(mine)

    return mines

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

    if cell in state["revealed"]:
        return (False, "You cannot open revealed cell, choose another one!")
        
    if cell in state["flagged"]:
        return (False, "You cannot open the flagged cell, remove flag fom there or choose another cell!")
        
    if cell in state["mines"]:
        state["hit"] = cell 
        state["game_over"] = True
        
    if state["first_move"]:
        state["mines"] = place_mines(cell)
        state["numbers"] = compute_numbers(state["rows"], state["colms"], state["mines"]) ###
        state["first_move"] = False
        
    state["board"][cell[0]][cell[1]] == state["numbers"][cell[0]][cell[1]]
    if state["board"][cell[0]][cell[1]] == 0:
    pass
        
        
        
