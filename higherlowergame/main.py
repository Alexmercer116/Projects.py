# An easier version of higher and lower game 
# Instead of using google searches we are using the
# number of instagram followers of each person

from art import logo,vs
from game_data import data
import random
import os

 # display logo
print(logo)

#format the account data
def format_account(account):
    """Formats the account data"""
    account_name=account['name']
    account_desc=account['description']
    account_counntry=account['country']
    return f"{account_name},a {account_desc},from { account_counntry}."

# compare the follower count of account
def check_followers(guess,followers_a,followers_b):
    """compares the followers count of each account"""
    if followers_a>followers_b:
        return guess=='a'
    else:
        return guess=='b'


def higherlower():
   # keep track of score
   score=0
   # A flag to continue the game
   game_continue=True
   # Defining an account before hand
   account_b=random.choice(data)
   while(game_continue):
      # Generate a random account from game_data
      # Make account_a as account_b in the next iteration
      account_a=account_b
      account_b=random.choice(data)
      # if two accounts are same
      if(account_a==account_b):random.choice(data)

      # print the formatted data
      print(f"Compare A: {format_account(account_a)}")

      print(vs)

      print(f"Against B: {format_account(account_b)}")

      # Ask the user a guess
      guess=input("Who has more followers?Type 'A' or 'B' : ").lower()

      # Get the followers of each account
      followers_a=account_a['follower_count']
      followers_b=account_b['follower_count']

      # clear the screen
      os.system('clear')

      # display logo after screen clear
      print(logo)

      #check the answer of user
      if(check_followers(guess,followers_a,followers_b)):
         score+=1
         print(f"You're absolutely correct! Current Score: {score}")
      else:
         game_continue=False
         print(f"Sorry,unfortunately that's a wrong one. Final Score: {score}")

higherlower()
