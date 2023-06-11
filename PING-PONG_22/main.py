from turtle import Screen
from pong import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.tracer(0)
screen.listen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('pong')


r_paddle = Paddle(x=350, y=0)
l_paddle = Paddle(x=-350, y=0)
ball = Ball()

scoreboard = Scoreboard()

screen.onkey(fun=r_paddle.move_down, key='Down')
screen.onkey(fun=r_paddle.move_up, key='Up')

screen.onkey(fun=l_paddle.move_down, key='s')
screen.onkey(fun=l_paddle.move_up, key='w')


while True:
    time.sleep(0.1)
    screen.update()
    ball.move() 

    #detect collision with top and bottom wall
    if ball.ycor() > 279 or ball.ycor() < -279:
        ball.bounce_y()
        time.sleep(1)

    #detect collision with center of both paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        time.sleep(1)
    if (ball.distance(r_paddle) > 50 and ball.xcor() > 410):
        ball.restart()
        scoreboard.left_score()
    if (ball.distance(l_paddle) > 50 and ball.xcor() < -410):
        ball.restart()
        scoreboard.right_score()
        


# screen.mainloop()
