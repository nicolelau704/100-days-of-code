#Use the colorgram python package to extract colors from and image an save them into a list
# import colorgram
#
# #Extract colors from image
# colors = colorgram.extract('image.jpg',30)
# rgb_tuples = []
#
# #Save the rgb colors into a list
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_tuples.append((r,g,b))
#
# print(rgb_tuples)

#Use the turtle package to draw the hirst painting
import turtle as turtle_module
import random

tim = turtle_module.Turtle()

turtle_module.colormode(255) #sets the color mode to rgb
color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

#Move the drawing turtle to the bottom left of the screen, make it invisible, and speed it up
tim.penup()
tim.speed(10)
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

#Choose a random color from the list then populate dots in that color in a 10 x 10 grid
#Keeps drawing lines of dots until there are 10 rows
for _ in range(10):
    #Draw 10 dots from left to right
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    #Move the turtle up then back to the left
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.setheading(0)

#Create the drawing screen
screen = turtle_module.Screen()
screen.exitonclick()
