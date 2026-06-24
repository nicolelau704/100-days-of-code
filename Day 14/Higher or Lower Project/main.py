import random
import art
from game_data import data

#Displays data for first person
def get_person_a(p_a):
    name = p_a["name"]
    description = p_a["description"]
    country = p_a["country"]

    print(f"Compare A: {name}, a {description}, from {country}.")

#Displays data for second person
def get_person_b(p_b):
    name = p_b["name"]
    description = p_b["description"]
    country = p_b["country"]

    print(f"Against B: {name}, a {description}, from {country}.")
    return

#Compares the follower count for each person and sees which one is higher
def compare_data(p_a, p_b):
    followers_a = p_a["follower_count"]
    followers_b = p_b["follower_count"]

    if followers_a > followers_b:
        return "A"
    else:
        return "B"

#Runs game
def game():
    # Display the logo
    print(art.logo)

    current_score = 0
    game_over = False

    #Get first person
    person_a = random.choice(data)

    while not game_over:
        # Get a different person from game_data module
        data.remove(person_a)
        person_b = random.choice(data)

        #Display Person A
        get_person_a(person_a)

        #Display VS picture
        print(art.vs)

        #Display Person B
        get_person_b(person_b)

        #Get input from user
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        # Clear the console and display the logo
        print("\n" * 100)
        print(art.logo)

        #Determine if the guess was correct
        if guess == compare_data(person_a, person_b):
            #Add a point to the current score
            current_score += 1

            #Display the current score
            print(f"You're right! Current score: {current_score}")

            #Person A now becomes Person B
            person_a = person_b
        elif not guess == compare_data(person_a, person_b):
            print(f"Sorry, that's wrong. Final score: {current_score}.")
            game_over = True
        else:
            print("Sorry, that is not a valid input.")
            game_over = True

game()