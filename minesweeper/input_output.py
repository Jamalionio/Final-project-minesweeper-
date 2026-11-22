'''input_output.py - printing the board and reading commands.

Owner: Your name
'''


def parse_command(text, rows, cols):
    '''Check the text typed by the player and split it into a command.

    Commands (not case-sensitive): "R E5", "F C3", "D", "H", "Q".
    Must NEVER crash: empty text, "R", "R Z99", "R 5E", "R E-5", "X 1"...
    Converts "C4" to (3, 2): letter -> column, number minus 1 -> row.

    Parameters:
        text (str): what the player typed
        rows, cols (int): board size

    Returns:
        tuple: (command, cell, error)
            command: "R", "F", "D", "H" or "Q" (None if there is an error)
            cell: (row, col) from zero, or None for D, H, Q
            error: None if everything is fine, otherwise a clear message
    '''
    pass


def display_board(state, show_mines):
    '''Print the board with column letters, row numbers and mines left.

    Under the grid print "Mines left: N" where N = nb_mines - number of flags.
    If show_mines is True: show '*' on every mine, 'X' on the mine that was
    hit (state["hit"]), and mark wrongly flagged cells.

    Parameters:
        state (dict): game state
        show_mines (bool): whether to show the mines
    '''
    pass
