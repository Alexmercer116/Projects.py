from turtle import Turtle,Screen
from random import randint

is_race_on=False
screen=Screen()
screen.title("Let's Race!!")
screen.screensize(2000,2500)
screen.bgpic('race.png')
usr_bet=screen.textinput(title="Place your bet",prompt="Who do you bet on?")
colors=['red','orange','green','yellow','blue','purple']
turtles=[]
y_c=-130

# creating multiple turtle objects
for t_id in range(6):
   turtle=Turtle('turtle')
   turtle.pu()
   turtle.color(colors[t_id])
   turtle.goto(x=-240,y=y_c)
   y_c+=50
   turtles.append(turtle)

if usr_bet:
   is_race_on=True

while is_race_on:
   
   for turtle in turtles:
      turtle.fd(randint(1,50))
      # getting the xcor to end the race condition
      if turtle.xcor >230:
         # making the race flag var false
         is_race_on=False 
         # getting only the turtle color
         win_color=turtle.pencolor()
         if(win_color==usr_bet):
            print(f"You won! The {win_color} turtle won the race.")
            break
         else:
            print(f"You Lost! The {win_color} turtle won the race.")
            break



      
screen.exitonclick()