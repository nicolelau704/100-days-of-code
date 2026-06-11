#Greeting
print("Welcome to Python Pizza Deliveries!")

#Get the user's pizza order
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#Calculate the bill for the user's order
bill = 0
#Check the size of the pizza
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")

#Check for pepperoni
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
#Check for cheese
if extra_cheese == "Y":
    bill += 1

#Display the total bill to the user
print(f"Your final bill is: ${bill}.")
