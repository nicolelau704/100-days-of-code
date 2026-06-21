import random
import art

#Create deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Calculate the value of a hand of cards
def score_value (hand):
    score = 0
    for card in hand:
        score += card
    return score

# Create hands
user_hand = []
computer_hand = []

def blackjack():
    end_game = False
    while not end_game:
        # If there are no cards in the hand, then populate two cards for the user and one for the computer
        if len(user_hand) == 0 and len(computer_hand) == 0:
            print(art.logo)
            user_hand.append(random.choice(cards))
            user_hand.append(random.choice(cards))
            computer_hand.append(random.choice(cards))
            if user_hand[0] == user_hand[1]:
                user_hand[0] = 1

        #Display hands to user
        print(f"Your cards: {user_hand}, Current score: {score_value(user_hand)}")
        print(f"Computer's first card: {computer_hand}")

        #Ask user if they want to hit or stand
        hit_or_stand = input("Type 'y' to get another card, type 'n' to pass: ")

        if hit_or_stand == "y":
            #Add card to user's hand
            user_hand.append(random.choice(cards))

            #Check if user hand exceeds value of 21
            if score_value(user_hand) > 21:
                #If there is an Ace in the user's hand, then convert the value from 11 to 1 so they are no longer over 21
                if 11 in user_hand:
                    user_hand.remove(11)
                    user_hand.append(1)
                    blackjack()
                #If there is no Ace in the user's hand, then the user went over 21 and loses
                else:
                    print(f"Your final hand: {user_hand}, Final score: {score_value(user_hand)}")
                    print(f"Computer's final hand: {computer_hand}, Final score: {score_value(computer_hand)}")
                    print("You went over. You lose! 😭")
            else:
                #If the user's hand is still less than 21, then go back to the beginning to
                #display the new hand and ask if they want to hit or stand
                blackjack()
        elif hit_or_stand == "n":
            #Now that the user is done getting cards, get cards for the computer
            while score_value(computer_hand) < 21 and score_value(computer_hand) < score_value(user_hand):
                computer_hand.append(random.choice(cards))

            #Display the final hands of both the user and computer
            print(f"Your final hand: {user_hand}, Final score: {score_value(user_hand)}")
            print(f"Computer's final hand: {computer_hand}, Final score: {score_value(computer_hand)}")

            #Display who won
            if score_value(computer_hand) > 21:
                print("Opponent went over. You win! 😊")
            elif score_value(user_hand) > score_value(computer_hand):
                print("You win! 😊")
            elif score_value(user_hand) == score_value(computer_hand):
                print("It's a draw! 😐")
            else:
                print("You lose! 😭")
        else:
            print("That is the wrong input")
            end_game = True

        #Clear both hands
        user_hand.clear()
        computer_hand.clear()

        # Ask user if they want to play again
        answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if answer == "y":
            print("\n" * 100)
        else:
            print("Thanks for playing! Goodbye!")
            end_game = True

blackjack()