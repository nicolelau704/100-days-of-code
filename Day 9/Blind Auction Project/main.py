import art

#print logo
print(art.logo)

#Greeting
print("Welcome to the secret auction program!")

# 1: Ask the user for input
bidders = {}
auction_open = True
while auction_open:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))

    # 2: Save data into dictionary {name: price}
    bidders[name] = price

    # 3: Whether if new bids need to be added
    answer = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if answer == "yes":
        print("\n" * 100)
    elif answer == "no":
        auction_open = False
    else:
        print("That is the wrong input.")
        auction_open = False

# 4: Compare bids in dictionary
highest_bidder = ""
highest_bid = 0
for person in bidders:
    if bidders[person] > highest_bid:
        highest_bid = bidders[person]
        highest_bidder = person

#Display winner
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
