# from _typeshed import Self
from turtle import Turtle
HEIGHT = 600

# TODO 1. Draw a line a the center of the screen

# TODO 2. Put the score for each person at the person's half

# TODO 3. Create a ball that moves from one half to another

# TODO 4. Create a set squares that moves when a key is pressed


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape('square')
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.color('white')
        self.goto(x, y)
        self.x_move = 10
        self.y_move = 10

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)


