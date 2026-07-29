from turtle import Screen, Turtle
import time

#Create screen
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#Create the initial snake with 3 body sections
starting_positions = [(0, 0), (-20, 0), (-40,0)]
segments = []

for position in starting_positions:
    segment = Turtle(shape="square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments.append(segment)

#Make the snake move
game_is_on = True
while game_is_on:
    #Move the snake in the background then update the screen every 0.1 seconds so the snake has a smooth movement
    screen.update()
    time.sleep(0.1)
    #Move each body segment to the body segment before its position. Move the 1st to a new position
    for seg_num in range(len(segments) - 1, 0, -1):     #starts with position of last segment
        new_x = segments[seg_num - 1].xcor()    #gets x coordinate for segment before it
        new_y = segments[seg_num - 1].ycor()    #gets y coordinate for segment before it
        segments[seg_num].goto(new_x, new_y)    #moves the segment to the position of the segment before it

    segments[0].forward(20)     #moves segment 1


screen.exitonclick()