from turtle import Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_body()

    def create_body(self):
        for position in STARTING_POSITIONS:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)

    def move(self):
        #Move each body segment to the body segment before its position. Move the 1st to a new position
        for seg_num in range(len(self.segments) - 1, 0, -1):     #starts with position of last segment
            new_x = self.segments[seg_num - 1].xcor()    #gets x coordinate for segment before it
            new_y = self.segments[seg_num - 1].ycor()    #gets y coordinate for segment before it
            self.segments[seg_num].goto(new_x, new_y)    #moves the segment to the position of the segment before it

        self.segments[0].forward(MOVE_DISTANCE)     #moves segment 1