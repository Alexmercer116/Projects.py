import random
from words import word_list
from art import logo,stages,gameover

# dislay the art
print(logo)

# choosing a random word from the list using choice()
chosen_word=random.choice(word_list)

# a blanks list
blanks=["_"]*len(chosen_word)
lives=6
gameover=False
while(not(gameover)):
   guess=input("Guess a letter in the word: ").lower()
   if guess in blanks:print(f"You have already guessed {guess}")
   for j in range(len(chosen_word)):
      if guess in chosen_word[j]:
         blanks[j]=guess
   if guess not in chosen_word:
      print(f"You guessed {guess},which is not in the word.You Lost a life")
      lives-=1
      if(lives==0):
         gameover=True
         print(gameover)
   print(stages[lives])
   
   print(*blanks)



