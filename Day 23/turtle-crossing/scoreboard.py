from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280,250)
        self.level = 1
        self.get_level()

    def get_level(self):
        #Display the level to the user
        self.write(f"Level: {self.level}", False, align="Left", font=FONT)

    def level_up(self):
        #Increase the level and display the level to the user
        self.level += 1
        self.clear()
        self.get_level()

    def game_over(self):
        #Display game over message
        self.goto(0,0)
        self.write("GAME OVER", False, align="center", font=FONT)
