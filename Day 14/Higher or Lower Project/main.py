import random
import art
from game_data import data

#Display the logo
print(art.logo)

#Get 2 different people from game_data module
person1 = random.choice(data)
data.remove(person1)
person2 = random.choice(data)

#Displays data for first person
def get_person1(first_person):
    name = first_person["name"]
    description = first_person["description"]
    country = first_person["country"]

    print(f"Compare A: {name}, a {description}, from {country}.")

#Displays data for second person
def get_person2(second_person):
    name = second_person["name"]
    description = second_person["description"]
    country = second_person["country"]

    print(f"Against B: {name}, a {description}, from {country}.")
    return

#Compares the follower count for each person and sees which one is higher
def compare_data(person_a, person_b):
    followers_a = person_a["follower_count"]
    followers_b = person_b["follower_count"]

    if followers_a > followers_b:
        return "a"
    else:
        return "b"

get_person1(person1)
print(art.vs)
get_person2(person2)
compare_data(person1, person2)