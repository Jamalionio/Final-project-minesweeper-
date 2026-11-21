# Final-project-minesweeper

A text based version of the Minesweeper game for Terminal

Final project for Systems, Algorithms and Programming 1 - course 

Group: Jamal Aghasi, Name2, Name3, Name4, Name5 ( add your full names )

Deadline: 30/11

## REQUIREMENTS

- Python 3,7 or later
- No imported modules except: random and time

## HOW TO RUN

    python main.py 

Run tests: 
  
    python tests.py

## HOW TO PLAY

Player types one command per turn ( not case-sensative ):

| Command | Example | Effect |
| --- | --- | --- |
| R  \<cell\> | R E5 | Reveal a cell |
| F \<cell\> | F C3 | Put or Remove a flag  |
| D | D | Debug mode (show all mines ) |
| H | H | Show the help (list of commands) |
| Q | Q | Quit the current game |

- A cell is written as a column and a row's number: C4 = column C and row 4

## SYMBOLS

| Symbol | Meaning | 
| --- | --- |
| # | Hidden cell |
| F | Flag |
| . | Revealed cell with no neighboring mines |
| 1 - 8 | Number of neighboring mines |
| * | Mine |
| X | The mine that was hit |

### Difficulty levels 

| Level | Grid | Mines |
| --- | --- | --- |
| Easy | 9 x 9 | 10 |
| Medium | 12 x 12 | 25 |
| Hard | 16 x 16 | 40 |

# Rules 

- The first reveal of the cell is always safe
- If a revealed cell has 0 neighboring mines then its neighbors reveals automatically ( flood fill )
- A flagged cell cannot be revealed until a flag is removed ( flood fill does not reveal flagged cells )
- The game is won when all the cells without mine have been revealed
- Flags are not required for win
- When the game end the full board is shown: all the mines, the mine that was hit and wrongly flagged cell
- At start player can give an optional seed: the same seed and the same first move gives the same board

# Project structure 




