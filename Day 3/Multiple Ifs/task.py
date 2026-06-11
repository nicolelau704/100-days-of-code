#Greeting
print("Welcome to the rollercoaster!")

#Ask user for their height in cm
height = int(input("What is your height in cm? "))

#If the user is 120cm or taller, then they can ride the rollercoaster
if height >= 120:
    print("You can ride the rollercoaster")

    #The price of the ticket depends on the user's age
    age = int(input("What is your age? "))
    price = 0
    if age <= 12:
        print("The ticket costs $5.")
        price = 5
    elif age <= 18:
        print("The ticket costs $7.")
        price = 7
    else:
        print("The ticket costs $12.")
        price = 12

    #Ask the user if they want photos
    wants_photos = input("Would you like to buy photos? (y/n) ")
    if wants_photos == "y":
        #Add amount to total bill and display it to the user
        price += 3
        print(f"Photos are $3 more. The total bill is {price}")
    else:
        #Display the total bill to the user
        print(f"The total bill is {price}.")
else:
    print("Sorry you have to grow taller before you can ride.")
