from art import logo
from Guess import easy_level_guessing,hard_level_guessing

# printing the logo
print(logo)

# setting a flag for play again
play_again=True
# Continuing the game
while(play_again):
  start_game=input('''Do You want to play the game?
  Type 'yes' or 'no' ''').lower()
  if(start_game=='yes'):
    # Asking for level type
    level=input("Choose Level: 'easy' or 'hard'").lower()
    if(level=='easy'):
      # easy game
      easy_level_guessing()
    else:
      # hard game
      hard_level_guessing()
    # want to play again?
    play=input("Want to play again? Type 'yes' or 'no' ").lower()
    if(play!='yes'):play_again=False
print("Thank you for playing.")
    