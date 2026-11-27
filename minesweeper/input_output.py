'''input_output.py - printing the board and reading commands.

Owner: Lala Abdullayeva
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
    command=text.strip().upper().split()
    if not command:
        return(None,None,"You typed nothing")
    cmd=command[0]
    if cmd in ("D","H","Q"):
        if len(command)==1:
            return(cmd,None,None)
        else:
            return(None,None,"This command has no cell")
    if cmd in ("R","F"):
        if len(command)!=2:
            return(None,None,"Add a cell after the command")
        cell_text=command[1]
        letter=cell_text[0]
        number=cell_text[1:]
        if not letter.isalpha() or not number.isdecimal():
            return(None,None,"Wrong cell format")
        col=ord(letter)-ord("A")
        row=int(number)-1
        if row<0 or row>=rows or col>=cols:
            return(None,None,"This cell is not on the board")
        return(cmd,(row,col),None)
    return(None,None,"Unknown command")


def display_board(state, show_mines):
    '''Print the board with column letters, row numbers and mines left.

    Under the grid print "Mines left: N" where N = nb_mines - number of flags.
    If show_mines is True: show '*' on every mine, 'X' on the mine that was
    hit (state["hit"]), and mark wrongly flagged cells.

    Parameters:
        state (dict): game state
        show_mines (bool): whether to show the mines
    '''

    rows=state["rows"]
    cols=state["cols"]
    board=state["board"]
    revealed=state["revealed"]
    flags=state["flags"]
    mines=state["mines"]
    hit=state["hit"]
    nb_mines=state["nb_mines"]
    print("   ",end="")
    for z in range(cols):
        print(chr(ord("A")+z),end=" ")
    print()
    for i in range(rows):
        if i+1<10:
            print(" "+str(i+1),end=" ")
        else:
            print(i+1,end=" ")
        for z in range(cols):
            cell=(i,z)
            if show_mines and cell in mines:
                if cell==hit:
                    sign="X"
                elif cell in flags:
                    sign="W'
                else:
                    sign="*"
            elif cell in flags:
                sign="F"
            elif cell in revealed:
                sign=board[i][z]
            else:
                sign="#"
            print(sign,end=" ")
        print()
    left=nb_mines-len(flags)
    print("Mines left:",left)

