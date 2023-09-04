from turtle import *
from random import randint,choice

pen=Turtle()

# setup a full screen
screen=Screen()
screen.setup(1.0,1.0)

def change_pos():
   pen.penup()
   pen.setx(randint(100,360))
   pen.sety(randint(-360,180))
   pen.pendown()

def dashed_line():
   for _ in range(10):
      pen.forward(10)
      pen.pu()
      pen.forward(10)
      pen.pd()

def draw_shape(n):
   # n=no of sides
   ang=360/n
   change_pos()
   for _ in range(n):
      pen.forward(100)
      pen.right(ang)

for i in range(3,11):
   pen.color("#" + ''.join([choice('0123456789ABCDEF') for j in range(6)]))
   draw_shape(i)



screen.exitonclick()

