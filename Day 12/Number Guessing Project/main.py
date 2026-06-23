import random
import art

#Logo
print(art.logo)

#Greeting
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

#Pick a random number
chosen_number = random.randint(1, 100)

#Set the difficulty of the game
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    #Set the number of lives depending on the difficulty chosen
    lives = 0
    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    else:
        print("Sorry, that is not a valid input.")

    print(f"You have {lives} attempts remaining to guess the number.")
    return lives

def game(lives_left, computer_number):
    win_game = False

    #Allow the user to keep making guesses until they run out of attempts
    while lives_left > 0:
        guess = int(input("Make a guess: "))

        if guess == computer_number:
            print(f"You got it! The answer was {computer_number}.")
            win_game = True
            lives_left = 0
        elif guess < computer_number:
            lives_left -= 1
            if lives_left != 0:
                print("Too low.\nGuess again.")
            print(f"You have {lives_left} attempts remaining to guess the number.")
        elif guess > computer_number:
            lives_left -= 1
            if lives_left != 0:
                print("Too high.\nGuess again.")
            print(f"You have {lives_left} attempts remaining to guess the number.")
        else:
            print("Sorry, that is not a valid number. Guess again.")

    if not win_game:
        print("You have run out of guesses. Refresh the page to play again.")

game(set_difficulty(), chosen_number)