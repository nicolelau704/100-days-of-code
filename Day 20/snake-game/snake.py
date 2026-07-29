from turtle import Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_body()
        self.head = self.segments[0]

    def create_body(self):
        for position in STARTING_POSITIONS:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        #Move each body segment to the body segment before its position. Move the 1st to a new position
        for seg_num in range(len(self.segments) - 1, 0, -1):     #starts with position of last segment
            new_x = self.segments[seg_num - 1].xcor()    #gets x coordinate for segment before it
            new_y = self.segments[seg_num - 1].ycor()    #gets y coordinate for segment before it
            self.segments[seg_num].goto(new_x, new_y)    #moves the segment to the position of the segment before it

        self.head.forward(MOVE_DISTANCE)     #moves segment 1