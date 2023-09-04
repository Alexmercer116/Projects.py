import turtle as t
from turtle import *
from random import randint


# setting up a screen
screen=Screen()
screen.setup(1.0,1.0)

# creating a turtle 
tim=Turtle()

# animation speed
tim.speed('fastest')

# set colormode
t.colormode(255)

# creating random rgb
def random_color():
  r=randint(0,255)
  g=randint(0,255)
  b=randint(0,255)
  return (r,g,b)


def draw_spirograph(gap):
  for _ in range(int(360/gap)):
      tim.circle(100)
      tim.color(random_color())
      tim.setheading(tim.heading()+gap)

draw_spirograph(5)

screen.exitonclick()
