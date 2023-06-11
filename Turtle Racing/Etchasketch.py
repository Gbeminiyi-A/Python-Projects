from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()




def move_forward():
    tim.forward(10)


def move_backwards():
    tim.back(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.setposition(0, 0)
    tim.setheading(0)
    tim.pendown()


screen.onkey(key='c', fun=clear_screen)
screen.onkey(key='w', fun=turn_left)
screen.onkey(key='s', fun=turn_right)
screen.onkey(key='a', fun=move_backwards)
screen.onkey(key='d', fun=move_forward)

Screen().mainloop()
