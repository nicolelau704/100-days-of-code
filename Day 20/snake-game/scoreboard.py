from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,275)
        self.score = 0
        self.get_score()

    def get_score(self):
        #Display the score at the top of the screen
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        #Clear the score, add a point, then display it again
        self.score += 1
        self.clear()
        self.get_score()

    def game_over(self):
        #Display message to user to let them know the game is over
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
