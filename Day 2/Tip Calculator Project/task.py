#Get input from the user
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

#calculate the tip for the whole bill then add it to the bill
tip = float((tip / 100) * bill)
bill += tip

#divide the new bill total by the number of people
total = (bill / people)

#formal the total to 2 decimal places
total = round(total, 2)

#Display the total each person needs to pay to the user
print(f"Each person should pay ${total}")
