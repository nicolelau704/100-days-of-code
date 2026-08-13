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
scoreboard = Scoreboard()

#Create turtle player
player = Player()

#Create car
car = CarManager()

#Allow user to control the turtle's movements
screen.listen()
screen.onkey(fun=player.up, key="Up")

#Start the game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Create and move cars
    car.create_car()
    car.move_car()

    #Detect collision with car
    for vehicle in car.all_cars:
        if vehicle.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    #Detect when the turtle reaches the top of the screen
    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        scoreboard.level_up()

screen.exitonclick()