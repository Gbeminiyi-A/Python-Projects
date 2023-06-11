import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=700, height=550)

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', ]
is_race_on = False

# tim = Turtle(shape='turtle')
# tim.color(colors[0])
# tim.penup()
# tim.goto(x=-330, y=-200)
#
# flippy = Turtle(shape='turtle')
# flippy.color(colors[1])
# flippy.penup()
# flippy.goto(x=-330, y=-150)
#
# mack = Turtle(shape='turtle')
# mack.color(colors[2])
# mack.penup()
# mack.goto(x=-330, y=-100)
#
# rafael = Turtle(shape='turtle')
# rafael.color(colors[3])
# rafael.penup()
# rafael.goto(x=-330, y=-50)
#
# donny = Turtle(shape='turtle')
# donny.color(colors[4])
# donny.penup()
# donny.goto(x=-330, y=0)
#
# leo = Turtle(shape='turtle')
# leo.color(colors[5])
# leo.penup()
# leo.goto(x=-330, y=50)
x, y = (-300, -200)

turtles = []
for _ in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[_])
    new_turtle.penup()
    new_turtle.goto(x, y)
    y = y + 75
    turtles.append(new_turtle)

users_bet = screen.textinput(title='Make a bet', prompt='What colour do you bet to win?').lower()

if users_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 330:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == users_bet:
                print('You win!!')
            else:
                print('You lose!')
            print(f'The {winning_color} turtle crossed the finish line first.')
        turtle.forward(random.randint(0, 10))

screen.mainloop()

