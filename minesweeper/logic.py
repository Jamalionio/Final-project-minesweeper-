'''logic.py - flags and end-of-game checks.

Owner: Your name 
'''


def toggle_flag(cell, state):
    '''Put a flag on a hidden cell, or remove it if there is one.

    Must update state["flags"] and state["board"] ('F' or '#').
    A revealed cell cannot be flagged.

    Parameters:
        cell (tuple): (row, col)
        state (dict): game state

    Returns:
        tuple: (ok, message). (True, "") if done,
               (False, "text of the error") if the cell is revealed.
    '''
    pass


def check_win(state):
    '''Check if the player won: all cells without a mine are revealed.

    Parameters:
        state (dict): game state

    Returns:
        bool: True if the game is won
    '''
    pass


def check_loss(state):
    '''Check if the player lost (a mine was revealed).

    Parameters:
        state (dict): game state

    Returns:
        bool: True if the game is lost
    '''
    pass
