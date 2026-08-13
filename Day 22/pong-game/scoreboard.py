from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100,200)
        self.display_score()

    def l_point(self):
        #Increase the score for the left paddle
        self.l_score += 1
        self.display_score()

    def r_point(self):
        #Increase the score for the right paddle
        self.r_score += 1
        self.display_score()

    def display_score(self):
        #Display the scores
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 70, "normal"))

    def game_over(self):
        # Display message to user to let them know the game is over
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Courier", 70, "normal"))
