from turtle import Turtle


class Name(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def location(self, x, y, state):
        self.goto(x, y)
        self.write(state)
