from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#Create screen
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
my_scoreboard = Scoreboard()

#Create snake and food
my_snake = Snake()
my_food = Food()

#Allow the program to accept inputs from the user to control the snake's movement
screen.listen()
screen.onkey(fun=my_snake.up,key="Up")
screen.onkey(fun=my_snake.down,key="Down")
screen.onkey(fun=my_snake.left, key="Left")
screen.onkey(fun=my_snake.right,key="Right")

# Make the snake move
game_is_on = True
while game_is_on:
    # Move the snake in the background then update the screen every 0.1 seconds so the snake has a smooth movement
    screen.update()
    time.sleep(0.1)

    my_snake.move()

    #Detect collision with food
    if my_snake.head.distance(my_food) < 15: #checks if the snake head is within 15 pixels of the food
        my_food.refresh()
        my_snake.extend()
        my_scoreboard.update_score()

    #Detect collision with wall
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 270 or my_snake.head.ycor() < -280:
        game_is_on = False
        my_scoreboard.game_over()

    #Detect collision with tail
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            game_is_on = False
            my_scoreboard.game_over()

screen.exitonclick()