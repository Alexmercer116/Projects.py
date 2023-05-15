import random
from hangman_words import word_list
import hangman_logo as hl

print(hl.logo)
chosen_word=random.choice(word_list)
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
         print(hl.gameover)
   print(hl.stages[lives])
   
   print(*blanks)



