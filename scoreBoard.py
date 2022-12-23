from turtle import *
from snake import WIDTH, HEIGHT

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
file = open("data.txt")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.highscore = int(file.read())
        self.penup()
        self.goto(0, HEIGHT/2 - 30)
        self.scoreBoard()


    def scoreBoard(self):
        self.clear()
        self.write(f"Score = {self.score}    Max Score = {self.highscore}" ,move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        self.clear()
        if self.score > 0:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.write(f"Score = {self.score}    Max Score = {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def updateScore(self):
        self.score = self.score + 1
