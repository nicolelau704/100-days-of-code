import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hand_signs = [rock, paper, scissors]

#Greeting
print("The computer has challenged you to a game of Rock, Paper, Scissors!")

#Get user input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))

#Display user's hand symbol
print(hand_signs[user_choice])

#Get computer choice
print("Computer chose:")

computer_choice = random.randint(0, 2)
print(hand_signs[computer_choice])

#Decide who wins
result = "You win!"
if user_choice == computer_choice:
    result = "It's a draw!"
elif user_choice == 0: #rock
    if computer_choice == 1:
        result = "You lose."
elif user_choice == 1:
    if computer_choice == 2:
        result = "You lose."
elif user_choice == 2:
    if computer_choice == 0:
        result = "You lose."
else:
    print("It was inconclusive.")

print(result)
