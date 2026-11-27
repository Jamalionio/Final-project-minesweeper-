'''play.py - level choice and one full game.

Owner: Jamal Aghasi
Team rules: see README.md (coordinates are (row, col), counted from zero).
'''

import random

from board import create_board, new_state, show_help
from logic_simple import toggle_flag, check_win, check_loss
from io_utils import parse_command, display_board
from core import reveal

LEVELS = {"1": ("Easy", 9, 9, 10), "2": ("Medium", 12, 12, 25), "3": ("Hard", 16, 16, 40)}


def choose_level():
    '''Ask the level and an optional seed.

    If a seed is given, call random.seed(seed).
    Ask again if the input is wrong.

    Returns:
        tuple: (rows, cols, nb_mines)
    '''
    if input("Would you like to choose an optional seed?\nEnter YES or Y if so, or 'N' or 'NO' if changed your mind ").lower() in ("yes", "y"):
        seed = input("Your seed: ")
        if seed.isdecimal():
     
def play_game():
    '''Play one full game: choose level, loop on commands until the end.

    Loop: display_board -> input -> parse_command -> action
    (reveal / toggle_flag / debug / help / quit) -> check_loss / check_win.
    At the end display the full board (show_mines=True).

    
    '''
    pass
