#Test the compatability between two names

def calculate_love_score(name1, name2):
    name1.lower()
    name2.lower()
    name3 = name1 + name2

    true_count = 0
    love_count = 0

    true_list = ["t", "r", "u", "e"]
    love_list = ["l", "o", "v", "e"]

    #Count how many times the letters from "TRUE" appear among both names
    for letter in name3:
        if letter in true_list:
            true_count += 1

    #Count how many times the letters from "LOVE" appear among both names
    for letter in name3:
        if letter in love_list:
            love_count += 1

    #Concatenate the first number and second number together
    print(str(true_count) + str(love_count))


calculate_love_score("Kanye West", "Kim Kardashian")
