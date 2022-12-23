from turtle import *
WIDTH, HEIGHT = 800,800
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            newTurtle = Turtle("square")
            newTurtle.color("green")
            newTurtle.penup()
            newTurtle.goto(pos)
            self.snakes.append(newTurtle)

    def after_eat_create(self):
        newTurtle = Turtle("square")
        newTurtle.color("green")
        newTurtle.penup()
        self.snakes.append(newTurtle)

    def move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            newx = self.snakes[i - 1].xcor()
            newy = self.snakes[i - 1].ycor()
            self.snakes[i].goto(newx, newy)
        self.snakes[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)

    def right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)

    def up(self):
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(90)

    def down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)

    def hit_wall(self):
            if self.snakes[0].xcor() == WIDTH / 2  or self.snakes[0].ycor() == HEIGHT / 2  or self.snakes[0].xcor() == -WIDTH / 2 or self.snakes[0].ycor() == -HEIGHT / 2 :
                return True

    def hit_tail(self):
        for snake in self.snakes[1:]:
            if self.snakes[0].distance(snake) < 10:
                return True

    def reset(self):
        for snake in self.snakes:
            snake.goto(1000,1000)
        self.snakes.clear()
        self.create_snake()