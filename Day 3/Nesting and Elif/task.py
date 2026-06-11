#Greeting
print("Welcome to the rollercoaster!")

#Ask user for their height
height = int(input("What is your height in cm? "))

#Check if the user 120cm tall or greater
if height >= 120:
    #Check if the user is at least 18 years old
    age = int(input("What is your age? "))
    if age >= 18:
        print("You can ride the rollercoaster")
    else:
        #Tell user that they are not old enough
        print("Sorry, you are not old enough to ride this rollercoaster.")
else:
    #Tell user that they are not tall enough
    print("Sorry you have to grow taller before you can ride.")
