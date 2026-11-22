'''
main.py - program entry point

Owner: Jamal Aghasi
'''

from play import play_game 

def main():
  '''
  Menu : start a game , then ask "play again ?" or quit 

  return True if player prefers to end game 
  '''
  while True:
    play_game()
    answer = input("Would you like to play again?\nYES/NO - Y/N\n").strip().lower()
    while answer not in ("y", "yes", "n", "no"):
      answer = input("Invalid value\nPlay again?\nYES/NO - Y/N\n").strip().lower()
    if answer in ("y", "yes"):
      print("Then, let's play again!")
    elif answer in ("n", "no"):
      return True
      
    
      

if __name__ == "__main__":
  if main():
    print("Goodbye!")
