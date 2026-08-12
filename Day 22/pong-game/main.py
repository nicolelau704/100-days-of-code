from turtle import Screen
from paddle import Paddle
import time

#Create screen
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

#Create paddles
right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))

#Allow the program to accept inputs from the user to control the paddle's movement
screen.listen()
screen.onkey(fun=right_paddle.up,key="Up")
screen.onkey(fun=right_paddle.down,key="Down")
screen.onkey(fun=left_paddle.up,key="w")
screen.onkey(fun=left_paddle.down,key="s")
#Make the paddle move
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()