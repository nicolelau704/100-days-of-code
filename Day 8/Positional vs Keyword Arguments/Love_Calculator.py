def calculate_love_score(name1, name2):
    name1.lower()
    name2.lower()
    name3 = name1 + name2

    true_count = 0
    love_count = 0

    true_list = ["t", "r", "u", "e"]
    love_list = ["l", "o", "v", "e"]

    for letter in name3:
        if letter in true_list:
            true_count += 1

    for letter in name3:
        if letter in love_list:
            love_count += 1

    print(str(true_count) + str(love_count))


calculate_love_score("Kanye West", "Kim Kardashian")
