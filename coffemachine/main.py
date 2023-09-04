from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# creating a money machine object
money_machine=MoneyMachine()
# creating a coffemaker object
coffee_maker=CoffeeMaker()
# creating a menu object
menu=Menu()

make_coffee=True

while make_coffee:
   options=menu.get_items()
   drink_type=input(f"What Would you like? ({options}): ")
   if drink_type=='off':
      # switching off the coffee machine
      make_coffee=False
      # printing the report of coffee machine
      coffee_maker.report()
      # printing the report of profit
      money_machine.report()
   else:
      # getting the coffee from menu
      drink=menu.find_drink(drink_type)
      #checking resource availability and processing payment
      if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # making coffee
            coffee_maker.make_coffee(drink)

   
   
