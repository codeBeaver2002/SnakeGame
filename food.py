from turtle import Turtle
from snake import WIDTH, HEIGHT
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.move()

    def move(self):
        randx = random.randint(-WIDTH / 2 + 20, WIDTH / 2 - 20)
        randy = random.randint(-HEIGHT / 2 + 20, HEIGHT / 2 - 20)
        self.goto(randx, randy)