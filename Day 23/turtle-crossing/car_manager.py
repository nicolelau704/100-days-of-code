from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.create_car()
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        #Create a random colored car somewhere along the right side of the screen
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(x=300, y=random.randint(-250,250))
            self.all_cars.append(new_car)

    def move_car(self):
        #Move the cars from the right side of the screen to the left
        for car in self.all_cars:
            car.backward(self.speed)

    def level_up(self):
        #Increase the speed of the car
        self.speed += MOVE_INCREMENT