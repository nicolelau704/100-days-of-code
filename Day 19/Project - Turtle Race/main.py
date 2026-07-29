from turtle import Turtle, Screen
import random

#Set up the screen
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

#Ask the user to bet on which turtle will win
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

#Create the list of colors being used and the position the turtles will be in
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_values = [-100, -70, -40, -10, 20, 50]
all_turtles = []

#Create each turtle then place them at the starting line
for count in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[count])
    new_turtle.goto(x=-230, y=y_values[count])
    all_turtles.append(new_turtle)

#Checks that the user made a bet
if user_bet:
    is_race_on = True

#Keep moving the turtles forward until there is a winner
while is_race_on:
    #When half the turtle is across the finish line, then stop the race
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            #Print whether or not the user bet on the winning turtle
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")
        else:
            #move the turtles at a random number of steps each iteration
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

screen.exitonclick()