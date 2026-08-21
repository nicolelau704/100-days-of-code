import turtle
import pandas

#Set up the screen for the game
screen = turtle.Screen()
screen.title("U.S. States Game")

#Put the map image in the background
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Create a turtle to write the state names with
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

#Open the data file containing all the state information
data = pandas.read_csv("50_states.csv")
guesses = []
x_value = 0
y_value = 0

#Keep prompting the user for guesses as long as there are still states left to guess
while len(guesses) < 50:

    #Get guess from user and display how many they've already gotten correct
    guess = (screen.textinput(title=f"{len(guesses)}/50 States Correct", prompt="What's another state's name?")).title()

    if guess == "Exit":
        break

    #Check if the guess matches any of the states in the list
    for state in data["state"]:
        #If the guess is correct
        if state == guess:
            #If the guess has not previously been made, then add it to the list of correct guesses
            if guess not in guesses:
                guesses.append(guess)

            #Get the x and y values that correspond to the guessed state
            row = data[data["state"] == state]
            x_value = (row["x"]).item()
            y_value = (row["y"]).item()

            #Write the name of the state in the correct position on the map
            writer.goto(x_value, y_value)
            writer.write(f"{state}")

#Display "you win" message
if len(guesses) == 50:
    writer.write("YOU WIN!")

#Create a CSV file of what states the user still needs to learn
all_states = data["state"].to_list()

for state in guesses:
    if state in all_states:
        all_states.remove(state)

states_needed = pandas.DataFrame(all_states)
states_needed.to_csv("states_to_learn.csv")