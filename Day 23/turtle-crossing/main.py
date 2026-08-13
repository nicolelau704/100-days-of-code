import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Create screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

#create player
player = Player()

#create car
car = CarManager()

#Allow user to control the turtle's movements
screen.listen()
screen.onkey(fun=player.up, key="Up")

game_is_on = True
count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if count > 5:
        car.create_car()
        count = 0

    count += 1
