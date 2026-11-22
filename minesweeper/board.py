'''board.py - board creation, game state, help text.

Owner: Your name
'''


def create_board(rows, cols):
    '''Create a board where every cell is hidden.

    Parameters:
        rows (int): number of rows
        cols (int): number of columns

    Returns:
        list: list of lists filled with the symbol '#'
    '''
    pass


def new_state(rows, cols, nb_mines):
    '''Create the state dictionary for a new game.

    Keys of the dictionary (everyone relies on these exact names):
        "rows"       int   - number of rows
        "cols"       int   - number of columns
        "nb_mines"   int   - number of mines
        "mines"      set   - {(row, col), ...}, empty until the first reveal
        "board"      list  - list of lists of symbols shown to the player:
                             '#' hidden, 'F' flag, '.' revealed 0, '1'..'8'
        "numbers"    list  - list of lists of int (mines around each cell),
                             empty until the first reveal
        "revealed"   set   - {(row, col), ...}
        "flags"      set   - {(row, col), ...}
        "first_move" bool  - True until the first reveal
        "game_over"  bool  - True if the player hit a mine
        "hit"        tuple - (row, col) of the mine that was hit, or None

    Parameters:
        rows (int), cols (int): board size
        nb_mines (int): number of mines

    Returns:
        dict: the state of a new game
    '''
    pass


def show_help():
    '''Print the list of commands (R, F, D, H, Q) with an example each.
    '''
    pass
