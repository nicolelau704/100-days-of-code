#Greeting
print("Welcome to Python Pizza Deliveries!")

#Get the user's pizza order
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#Calculate the bill for the user's order
#Check the size of the pizza and set the bill
bill = 0
if size == "S":
    bill += 15

    #Check what toppings the user wanted and add it to the bill
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size =="M":
    bill += 20

    #Check what toppings the user wanted and add it to the bill
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill += 25

    #Check what toppings the user wanted and add it to the bill
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
else:
    print("You typed the wrong inputs.")

#Display the total bill to the user
print(f"The total bill for your pizza is ${bill}.")
