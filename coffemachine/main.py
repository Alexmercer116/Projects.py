
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffe_machine_off=False
profit=0

def report():
   print(f"Water: {resources['water']}ml")
   print(f"Milk: {resources['milk']}ml")
   print(f"Coffee: {resources['coffee']}gm")
   print(f"Money: ${profit}")

def is_resources_suffice(cofe_ingredients):

   """Checks with the available resources of machine"""
   
   for cofe in cofe_ingredients:
      if cofe_ingredients[cofe]>=resources[cofe]: 
         print(f"sorry there is not enough {cofe}")
         return False
   return True


def process_coins():
   """Returns total amount inserted"""   
   
   print("Please insert coins.")
   # In Indian currency.But let's stick with quarters and dimes.
   # total=int(input("how many coins with 1 den. :")) *1
   # total+=int(input("how many coins with 2 den. :"))*2
   # total+=int(input("how many coins with 5 den. :"))*5

   total=int(input("how many quarters?"))*0.25
   total+=int(input("how many dimes?"))*0.1
   total+=int(input("how many nickles?"))*0.05
   total+=int(input("how many pennies?"))*0.01

   return total


def is_payment_successful(coffe_cost,pay):
   if(pay>=coffe_cost):
      change=round((pay-coffe_cost),2) 
      print(f"Here's is your ${change} in change.")
      global profit
      profit+=coffe_cost
      return True
   else:
      print("Sorry not enough money.Money refunded.")
      return False


def make_coffee(coffe,ingredients):
   """makes coffee and return the remaining resources."""
   for item in ingredients:
      resources[item]-=ingredients[item]
   print(f"Here's the {coffe} you ordered ☕☕.\nThank you for you patronage.")

while(not coffe_machine_off):
   coffe_type=input("What would you like espresso/latte/cappuccino: ")
   
   # Turning the coffee machine off
   if(coffe_type=="off"):
      coffe_machine_off=True
      report()
      exit(0)
   
   coffee=MENU[coffe_type]
   # Checking for the sufficent resorces
   if(is_resources_suffice(coffee['ingredients'])):
      pay=process_coins()
      # checking for payment successful.
      if(is_payment_successful(coffee['cost'],pay)):
         # making coffee
         make_coffee(coffe_type,coffee["ingredients"])
      



      





   

   
