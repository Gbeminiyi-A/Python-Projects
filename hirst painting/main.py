#import colorgram
from turtle import Turtle, Screen
import random

#colors = colorgram.extract('C:\Users\Hp\Documents\100 days of code\hirst painting\hirst.jpg', 10)

Screen().colormode(255)

color_list = [
    (252, 251, 243), (243, 252, 248), (253, 247, 251), (237, 243, 250), (237, 217, 84),
    (212, 147, 99), (180, 78, 33), (125, 161, 210), (50, 30, 22), (44, 42, 130)
              ]

# Brought the turtle image down a bit to have more space for the drawing on line 32
tim = Turtle()
tim.hideturtle()
tim.penup()

# TODO 1. Use the turtle to draw a dot while moving.


def drawing():
    for _ in range(10):
        color = random.choice(color_list)
        tim.dot(20, color)
        tim.penup()
        tim.forward(40)
        tim.pendown()

# TODO 2. Set the position of the turtle to a certain position and draw a 10 x 10 hirst painting


x, y = (-30, -50)
tim.setpos(x, y)
i = 0

# TODO 3. Loop the drawing for as many number of times
while i < 10:
    drawing()
    tim.penup()
    y = y+30
    tim.setpos(x, y)
    i += 1


Screen().mainloop()
