#Greeting
print("Welcome to the rollercoaster!")

#Ask user for their height
height = int(input("What is your height in cm? "))

#Check if the user 120cm tall or greater
if height >= 120:
    #Ask for the user's age
    age = int(input("What is your age? "))

    #Check if the user is at least 18 years old
    if age >= 18:
        print("You can ride the rollercoaster")
    else:
        #Tell user that they are not old enough
        print("You can enter the park, but you are not old enough for the rollercoaster.")

    #Tell the user how much their ticket costs based on their age
    if age < 12:
        print("Your ticket is $5.")
    elif age < 18:
        print("Your ticket is $7.")
    else:
        print("Your ticket is $12.")
else:
    #Tell user that they are not tall enough for the rollercoaster
    print("Sorry you have to grow taller before you can ride the rollercoaster.")
