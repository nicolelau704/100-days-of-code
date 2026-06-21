import random
import art

#Pick a random card from a deck of cards
def get_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#Calculate the value of a hand of cards
def score_value (hand):
    if sum(hand) > 21 and 11 in hand:
        # If there is an Ace in the hand, then convert the value from 11 to 1 so they are no longer over 21
        hand.remove(11)
        hand.append(1)

    return sum(hand)

#Determine the winner
def who_won (user, computer):
    if user > 21:
        return "You went over. You lose! 😭"
    elif computer > 21:
        return "Opponent went over. You win! 😊"
    elif user > computer:
        return "You win! 😊"
    elif user == computer:
        return "It's a draw! 😐"
    else:
        return "You lose! 😭"

def blackjack():
    #Display the logo
    print(art.logo)

    # Create hands
    user_hand = []
    computer_hand = []

    #Populate two cards for the user and one for the computer
    user_hand.append(get_card())
    user_hand.append(get_card())
    computer_hand.append(get_card())

    #Keep playing game
    end_game = False
    while not end_game:
        #Display hands to user
        print(f"Your cards: {user_hand}, Current score: {score_value(user_hand)}")
        print(f"Computer's first card: {computer_hand}")

        #Ask user if they want to hit or stand
        hit_or_stand = input("Type 'y' to get another card, type 'n' to pass: ")

        if hit_or_stand == "y":
            #Add card to user's hand
            user_hand.append(get_card())
            if score_value(user_hand) > 21:
                end_game = True

        elif hit_or_stand == "n":
            #Now that the user is done getting cards, get cards for the computer
            while score_value(computer_hand) < 17:
                computer_hand.append(get_card())
            end_game = True

        else:
            print("That is the wrong input")
            end_game = True

    # Display the final hands of both the user and computer
    print(f"Your final hand: {user_hand}, Final score: {score_value(user_hand)}")
    print(f"Computer's final hand: {computer_hand}, Final score: {score_value(computer_hand)}")

    # Display who won
    user_score = score_value(user_hand)
    computer_score = score_value(computer_hand)
    print(who_won(user_score, computer_score))

# Ask user if they want to play again
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 100)
    blackjack()
