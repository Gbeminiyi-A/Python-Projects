from turtle import Turtle


class Snake:

    def __init__(self,):
        self.segments = []
        self.x, self.y = 0, 0
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            self.add_segment(x=self.x, y=self.y)

    

    def add_segment(self, x, y):
        new_turtle = Turtle('square')
        new_turtle.color('white')
        new_turtle.width(5)
        new_turtle.penup()
        new_turtle.goto(x, y)
        self.x -= 20
        self.segments.append(new_turtle)

    def reset_snake(self):
        for snake in self.segments:
            snake.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.segments[0].goto(0, 0)
        self.segments[1].goto(-20, 0)
        self.segments[2].goto(-40, 0)

    def extend_snake(self):

        self.add_segment(x=self.segments[-1].xcor(), y=self.segments[-1].ycor())

    def move(self,):

        for seg in range(len(self.segments) - 1, 0, -1):
            position = self.segments[seg - 1].position()
            self.segments[seg].goto(position)

        self.segments[0].forward(20)

        # Detect Collision with food

        # Detect Collision with wall

    def up(self):
        if self.segments[0].heading() == 180:
            self.segments[0].right(90)
        elif self.segments[0].heading() == 0:
            self.segments[0].left(90)
        else:
            self.segments[0].forward(1)

    def down(self):
        if self.segments[0].heading() == 0:
            self.segments[0].right(90)
        elif self.segments[0].heading() == 180:
            self.segments[0].left(90)

    def left(self):
        if self.segments[0].heading() == 270:
            self.segments[0].right(90)
        elif self.segments[0].heading() == 180:
            self.segments[0].forward(1)
        elif self.segments[0].heading() == 90:
            self.segments[0].left(90)
        else:
            self.segments[0].forward(1)

    def right(self):
        if self.segments[0].heading() == 270:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 90:
            self.segments[0].right(90)
        elif self.segments[0].heading() == 0:
            self.segments[0].forward(1)
        else:
            self.segments[0].right(90)
