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

#create player
player = Player()

#create car
car = CarManager()

#Allow user to control the turtle's movements
screen.listen()
screen.onkey(fun=player.up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    #detect collision with car
    for vehicle in car.all_cars:
        if vehicle.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    #detect when the turtle reaches the top of the screen
    if player.ycor() >= player.finish_line_y:
        player.level_up()
        car.level_up()
        scoreboard.level_up()

screen.exitonclick()