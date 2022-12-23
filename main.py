import scoreBoard
import time
from turtle import Screen
from snake import *
from random import *
from food import Food
from scoreBoard import *

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkeypress(key="a", fun=snake.left)
screen.onkeypress(key="d", fun=snake.right)
screen.onkeypress(key="w", fun=snake.up)
screen.onkeypress(key="s", fun=snake.down)

time_a_sleep = 0.05
game = True
while game:
    if snake.hit_wall() or snake.hit_tail():
        score.reset()
        score.score = 0
        score.reset()
        game_over = Turtle()
        game_over.color("white")
        game_over.hideturtle()
        snake.reset()

    time.sleep(time_a_sleep)
    snake.move()
    screen.update()
    if snake.snakes[0].distance(food) < 15:
        time_a_sleep -= 0.001
        snake.after_eat_create()
        food.move()
        score.updateScore()
        score.scoreBoard()




screen.exitonclick()