from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(UP)
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.goto(starting_position)

    def up(self):
        self.setheading(UP)
        self.move()

    def down(self):
        self.setheading(DOWN)
        self.move()

    def move(self):
          self.forward(MOVE_DISTANCE)