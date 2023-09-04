# A simple black jack game
from art import logo
from random import choice
import os


def deal_card():
    """Returns a random card from deck"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    return choice(cards)

def calculate_score(cards):
   """Return score from the given list of cards"""
   if(sum(cards)==21 and len(cards)==2):
      return 0
   if(11 in cards and sum(cards)>21):
      cards.remove(11);cards.append(1)
      return sum(cards)
   return sum(cards)

def compare(player_score,dealer_score):
   if player_score==dealer_score:
      return "PUSH 🙃"
   elif dealer_score==0:
      return "You Lost, Dealer has Blackjack 😱"
   elif player_score==0:
      return "You Won!! Blackjack Win 😎"
   elif player_score>21:
      return "You Lost,you went over 😭"
   elif dealer_score>21:
      return "You won,dealer went over 😁"
   elif player_score>dealer_score:
      return "You Won 😃"
   else:
      return "You Lose 😤"

def black_jack():
   print(logo)
   # In this black jack Ace=11 always
   # Jack,queen,king are 10
   # we are assuming an infinite deck of cards to make the game easier
   player_cards=[]
   dealer_cards=[]
   game_over=False
   for _ in range(2):
      player_cards.append(deal_card())
      dealer_cards.append(deal_card())
   
   while not game_over:
   # calculating scores
      player_score=calculate_score(player_cards)
      dealer_score=calculate_score(dealer_cards)
      print(f"Your Cards : {player_cards} , your score : {player_score}")
      print(f"Dealer's First Card {dealer_cards[0]}")
      
      if(player_score==0 or dealer_score==0 or player_score>21):
         game_over=True
      else:
         # player picking up cards
         player_choice=input("Hit or  Stand ")
         if(player_choice.lower()=='hit'):
            player_cards.append(deal_card())
         else:
            game_over=True
   # Dealer picking cards
   while dealer_score!=0 and dealer_score<17:
      dealer_cards.append(deal_card())
      dealer_score=calculate_score(dealer_cards)
   print(f"Your final hand {player_cards}, Your Final Score {player_score}")
   print(f"Dealers final hand {dealer_cards}, Dealer's Final Score {dealer_score}")
   print(compare(player_score,dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system('clear')
  black_jack()