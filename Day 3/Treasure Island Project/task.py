print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input("You've reached a fork in the road. Would you like to go left or right? (left/right) ")
if choice == "right" or "Right" or "RIGHT":
    print("You fell into a hole! Game over.")
elif choice == "left" or "Left" or "LEFT":
    print("A huge lake appears just beyond the line of trees.\n"
          "You can see a small island floating in the middle.\n")
    choice = input("Do you choose to swim across or wait for a boat? (swim/wait) ")
    if choice == "swim" or "Swim" or "SWIM":
        print("A trout surges upward and attacks you! Game over.")
    elif choice == "wait" or "Wait" or "WAIT":
        print("A woman pulls up in a fishing boat an hour later.\n"
              "She tells you that the island is rumored to have treasure on it.\n"
              "She offers to take you there if you give her a portion of the treasure.\n"
              "She takes you across.You explore for a while until you come across a passageway with 3 doorways.")
        choice = input("Which door do you choose? (red/yellow/blue) ")
        if choice == "red" or "Red" or "RED":
            print("You trigger a booby trap and get burned by fire! Game over.")
        elif choice == "yellow" or "Yellow" or "YELLOW":
            print("Piles of gold lay all around. You win!")
        elif choice == "blue" or "Blue" or "BLUE":
            print("You hear a loud growl and don't have time to react before a beast lunges upon you. Game over.")
        else:
            print("That is the wrong input. Game over.")
    else:
        print("That is the wrong input. Game over.")
else:
    print("That is the wrong input. Game over.")

