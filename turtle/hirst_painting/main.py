import turtle as t
from turtle import *
from random import choice

# import colorgram as col

# # Extracting colors
# colors=col.extract('hirst_image.jpg',50)

# # creating a list of rgb colors
# rgb_colors=[(color.rgb.r,color.rgb.g,color.rgb.b) for color in colors]

# # display the rgb colors
# print(rgb_colors)

colors=[
     (25, 108, 164), (194, 38, 81), (238, 161, 49), (234, 215, 85), (223, 137, 176), (144, 108, 56), (102, 197, 219), (206, 166, 29), (20, 57, 132), (214, 73, 90), (239, 89, 50), (141, 208, 227), (118, 192, 140), (3, 186, 176), (106, 107, 199), (138, 29, 73), (4, 161, 86), (98, 51, 36), (22, 156, 210), (232, 165, 184), (175, 185, 221), (29, 90, 95), (233, 172, 161), (152, 213, 190), (242, 205, 8), (89, 48, 31), (39, 46, 81), (26, 97, 94)
    ]

# setting up a screen
screen=Screen()
screen.setup(1.0,1.0)

# creating a turtle 
trt=Turtle()
t.colormode(255)
trt.hideturtle()
trt.speed("fastest")
trt.pu()
trt.seth(225)
trt.fd(300)
trt.seth(0)

for dot_count in range(1,101):
   trt.dot(20,choice(colors))
   trt.fd(50)
   if dot_count%10==0:
      trt.seth(90)
      trt.fd(50)
      trt.seth(180)
      trt.fd(500)
      trt.seth(0)




screen.exitonclick()
