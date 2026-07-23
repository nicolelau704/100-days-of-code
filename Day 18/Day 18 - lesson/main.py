#from turtle import Turtle, Screen
#from turtle import *       #imports everything but is not recommended
#import turtle      #must use the dot method to call on things turtle.Turtle()
import turtle as t     #using alias names turtle.t

#import heroes
#print(heroes.gen())

import random

tim = t.Turtle()
t.colormode(255)

tim.shape("turtle")
tim.color("green")

#Create a function to get a random color using RGBs and tuples
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

#Draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

#Draw a dashed line
# for _ in range(20):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

#Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon in different colors
corners = 3
color_count = 0
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown"]

while corners < 11:
    angle = 360/corners
    tim.pencolor(colors[color_count])
    for _ in range(corners):
        tim.forward(40)
        tim.right(angle)
        tim.forward(40)
    corners += 1
    color_count += 1

#Random walk at a quicker speed
# direction = ["right", "left", "forward", "back"]
# colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown"]
#
# tim.pensize(10)
# tim.speed(10)
#
# for _ in range(600):
#     tim.color(random.choice(colors))
#     where = random.choice(direction)
#     if where == "right":
#         tim.right(90)
#         tim.forward(20)
#     elif where == "left":
#         tim.left(90)
#         tim.forward(20)
#     elif where == "back":
#         tim.back(20)
#     else:
#         tim.forward(20)

#teacher solution
# positions = [0, 90, 180, 270]
# colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown"]
# tim.pensize(10)
# tim.speed(10)
#
# for _ in range(200):
#     tim.color(random.choice(colors))
#     tim.setheading(random.choice(positions))
#     tim.forward(20)

#Use the random_color() function to get a random color for each movement
# positions = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed(10)
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.setheading(random.choice(positions))
#     tim.forward(20)

#Draw a spirograph with repeating circles that stops before the circles start overlapping
# tim.speed(6)
# original_position = tim.position()
# gap = 10
#
# for _ in range(int(360/gap)):
#     tim.pencolor(random_color())
#     tim.circle(100)
#     tim.left(gap)
#







screen = t.Screen()
screen.exitonclick()