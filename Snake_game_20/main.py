from snake import Snake
from turtle import Screen
import time
from scoreboard import ScoreBoard
from food import Food


food = Food()
scoreboard = ScoreBoard()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()

screen.title("Snake Game")
snake = Snake()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

snake_is_alive = True

while snake_is_alive:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        scoreboard.clear_board()
        scoreboard.count_score()
        snake.extend_snake()
        food.refresh()
    if (
        snake.segments[0].xcor() > 300
        or snake.segments[0].xcor() < -300
        or snake.segments[0].ycor() > 300
        or snake.segments[0].ycor() < -300
    ):
        scoreboard.reset_score()
        snake.reset_snake()
        

    # Detect collision with Tail
    for segments in snake.segments[1:]:
        if snake.segments[0].distance(segments) < 15:
            scoreboard.reset_score()
            snake.reset_snake()
            
    # if the head collides with any segment of the tail

screen.mainloop()
