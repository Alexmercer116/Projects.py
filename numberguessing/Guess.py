import random
from math import sqrt
# choosing a number between 1 to 100
num=random.randint(1,100)
def get_hint1():
  global num
  if(num%2==0):
    return "The Number you're guessing is even"
  else:
    return "The Number you're guessing is odd"

def is_prime(num):
  for i in range(2,int(sqrt(num))):
    if(num%i==0):return False
  return True

def get_hint2():
  global num
  if(is_prime(num) and num > 9):
    return "The Number is two digit prime number"
  elif(is_prime(num) and num > 9):
    return "The Number is single digit prime number"
  elif(num>9):
    return "The Number is two digit number which is not a prime"
  else:
    return "The Number is single digit number which is not a prime"


def get_hint3():
  global num
  if(num>=90):
    return "The Number is greater than 90"
  elif(num>=80 and num<90):
    return "The Number lies between 80 and 90"
  elif(num>=70 and num<80):
    return "The Number lies between 70 and 80"
  elif(num>=60 and num<70):
    return "The Number lies between 60 and 70"
  elif(num>=50 and num<60):
    return "The Number lies between 50 and 60"
  elif(num>=40 and num<50):
    return "The Number lies between 40 and 50"
  elif(num>=30 and num<40):
    return "The Number lies between 30 and 40"
  elif(num>=20 and num<30):
    return "The Number lies between 20 and 30"
  else:
    return "The Number lies between 10 and 20"


# Easy level game 
def easy_level_guessing():
  lives=7
  hints=3
  while(lives>0):
    guess=int(input("Guess the number between 1 to 100: "))
    if(guess==num):
      print(f"Hoorayy!!You guessed the number correctly!The Number was {num}")
      break
    else:
      print("Wrong Guess.")
      lives-=1
      if(lives==0):
        print(f"Sorry,Unfortunately you cannot guess the number.The number was {num}")
        break
      hint=input(f"You've {lives} remaining guesses.Want help?Type 'yes' or 'no'").lower()
      if(hint=='yes'):
        if(hints==3):print(get_hint1())
        elif(hints==2):print(get_hint2())
        elif(hints==1):print(get_hint3())
        else:print("Sorry,You're out of hints.")
        hints-=1

# hard level game
def hard_level_guessing():
  lives=5
  hints=3
  while(lives>0):
    guess=int(input("Guess the number between 1 to 100: "))
    if(guess==num):
      print(f"Hoorayy!!You guessed the number correctly!The Number was {num}")
      break
    else:
      lives-=1
      if(lives==0):
        print(f"Sorry,Unfortunately you cannot guess the number.The number was {num}")
        break
      hint=input(f"You've {lives} remaining guesses.Want help?Type 'yes' or 'no'").lower()
      if(hint=='yes'):
        if(hints==3):print(get_hint1())
        elif(hints==2):print(get_hint2())
        else:print("Sorry,You're out of hints.")
        hints-=1