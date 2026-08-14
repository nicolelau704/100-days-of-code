from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,275)
        self.get_high_score()
        self.get_score()

    def get_high_score(self):
        #Read the data.txt file for the high score value and save it as an integer
        with open("data.txt") as file:
            self.high_score = int(file.read())

    def get_score(self):
        #Display the score at the top of the screen
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        #Clear the score, add a point, then display it again
        self.score += 1
        self.get_score()

    # def game_over(self):
    #     #Display message to user to let them know the game is over
    #     self.goto(0,0)
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    #Day 24 - reset game instead of game over
    def reset_game(self):
        #Checks if the current score is higher than the current high score
        if self.score > self.high_score:
            #The current score is now the new high score
            self.high_score = self.score

            #Update the high score in the data.txt file
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")

        #Reset the score to 0 for the next game
        self.score = 0

        #Display the scoreboard again
        self.get_score()