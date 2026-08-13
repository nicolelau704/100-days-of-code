from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        #Keeps moving the ball on the screen
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        #When the ball hits the top or bottom of the screen, it bounces it in a different direction
        self.y_move *= -1

    def bounce_x(self):
        #When the ball hits a paddle, it bounces it in a different direction
        self.x_move *= -1

        #Increases the speed of the ball
        self.move_speed *= 0.9

    def reset_ball(self):
        #Places ball back in the center of the screen then moves it in the opposite direction at the initial speed
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
