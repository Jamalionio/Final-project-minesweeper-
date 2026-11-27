'''play.py - level choice and one full game.

Owner: Jamal Aghasi
Team rules: see README.md (coordinates are (row, col), counted from zero).
'''

import random

from board import new_state, show_help
from logic import toggle_flag, check_win, check_loss
from input_output import parse_command, display_board
from core import reveal

LEVELS = {"1": ("Easy", 9, 9, 10), "2": ("Medium", 12, 12, 25), "3": ("Hard", 16, 16, 40)}


def choose_level():
    '''Ask the level and an optional seed.

    If a seed is given, call random.seed(seed).
    Ask again if the input is wrong.

    Returns:
        tuple: (rows, cols, nb_mines)
    '''
    print("Choose level: ")
    for key in LEVELS:
        dif, rows, cols, nb_mines = LEVELS[key]
        print(f"{key} - {dif} ({rows} X {cols}, {nb_mines} mines)")

    level = input("Choose level (1/2/3): ").strip()
    while level not in LEVELS:
        print("Invalid value")
        level = input("Try again, (1/2/3): ").strip()
        
    dif, rows, cols, nb_mines = LEVELS[level]

    seed = input("Choose optional seed or leave it empty: ").strip()
    while seed and not seed.isdecimal():
        print("Invalid value")
        seed = input("Try again: ").strip()

    if seed:
        random.seed(int(seed))

    return rows, cols, nb_mines

def play_game():
    '''Play one full game: choose level, loop on commands until the end.

    Loop: display_board -> input -> parse_command -> action
    (reveal / toggle_flag / debug / help / quit) -> check_loss / check_win.
    At the end display the full board (show_mines=True). 

    Returns: None
    
    '''
    
    rows, cols, nb_mines = choose_level()
    state = new_state(rows, cols, nb_mines)
    show_mines = False
    while True:
        display_board(state, show_mines)
        action = input("Command (R cell / F cell / D / H / Q): ")
        command, cell, error = parse_command(action, rows, cols)

        if error != None:
            print(error)
            continue

        if command == "Q":
            display_board(state, True)
            print("You have quit the game")
            break

        if command == "H":
            show_help()
            continue 

        if command == "D":
            show_mines = not show_mines
            continue

        if command == "R":
            ok, message = reveal(cell, state)
        else:
            ok, message = toggle_flag(cell, state)

        if not ok:
            print(message)
            continue

        if check_loss(state):
            display_board(state, True)
            print("BOOOM!!!\nYou hit a mine. You lost :(")
            break
        if check_win(state):
            display_board(state, True)
            print("Congratulations, You won!!!")

