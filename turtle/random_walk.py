import turtle as t
from turtle import *
from random import choice,randint

# create a turtle with a width of 5
tim = Turtle()
tim.shape('circle')
tim.width(5)
tim.speed(10)

# changing colormode to 255
t.colormode(255)

# setup a full screen
screen=Screen()
screen.setup(1.0,1.0)

def random_color():
  r=randint(0,255)
  g=randint(0,255)
  b=randint(0,255)
  return (r,g,b)

# east=0,north=90,west=180,south=270
directions=[0,90,180,270]

# set the coordiates of turtle
tim.penup()
tim.setx(100)
tim.sety(75)
tim.pendown()

for _ in range(100):
  tim.color(random_color())
  tim.bk(50)
  tim.setheading(choice(directions))

screen.exitonclick()