from turtle import *

tim=Turtle()


screen=Screen()
screen.setup(1.0,1.0)

def move_front():
    tim.fd(100)

def move_back():
    tim.bk(100)

def turn_right():
    n_h=tim.heading()+30
    tim.seth(n_h)

def turn_left():
    n_h=tim.heading()-30
    tim.seth(n_h)

def clear():
    tim.reset()

screen.listen()
# screen.onkey(key='w',fun=move_front)
# screen.onkey(key='s',fun=move_back)
# screen.onkey(key='a',fun=move_right)
# screen.onkey(key='d',fun=move_left)
screen.onkey(move_front,"w")
screen.onkey(move_back,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")
screen.exitonclick()

