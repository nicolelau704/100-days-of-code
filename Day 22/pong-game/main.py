from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Create screen
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
scoreboard = Scoreboard()

#Create paddles
right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))

#Create ball
ball = Ball()

#Allow the program to accept inputs from the user to control the paddle's movement
screen.listen()
screen.onkey(fun=right_paddle.up,key="Up")
screen.onkey(fun=right_paddle.down,key="Down")
screen.onkey(fun=left_paddle.up,key="w")
screen.onkey(fun=left_paddle.down,key="s")

#Start the game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    ball.move()

    #Detect if the ball collides with the top or bottom of the screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect if the ball collides with a paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    #Detect if right paddle misses
    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.l_point()

    #Detect if left paddle misses
    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()