import random

#List all potential letters, numbers, and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Greeting
print("Welcome to the PyPassword Generator!")

#Find out what kind of password the user needs
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Create a list to hold each character in the password
password =[]

#Add a random letter to the password list until you reach the necessary number of letters
for count in range(0, nr_letters):
    password.append(random.choice(letters))

#Add a random symbol to the password list until you reach the necessary number of symbols
for count in range(0, nr_symbols):
    password.append(random.choice(symbols))

#Add a random number to the password list until you reach the necessary number of numbers
for count in range(0, nr_numbers):
    password.append(random.choice(numbers))

#Mix up the characters in the password
mixed_password = []
for count in range(0, len(password)):
    chosen_character = random.choice(password)
    mixed_password.append(chosen_character)
    password.remove(chosen_character) #remove the chosen character so it is not selected again

#Convert the mixed_password list into a string
final_password = ""
for count in range(0, len(mixed_password)):
    final_password += str(mixed_password[count])

#Present the password to the user
print(f"Your password is: {final_password}")