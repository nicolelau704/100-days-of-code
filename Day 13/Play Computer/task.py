year = int(input("What's your year of birth? "))

if year < 1964:
    print("You are a Boomer")
elif year < 1980:
    print("You are Gen X")
elif year >= 1980 and year <= 1994:
    print("You are a Millennial.")
elif year > 1994:
    print("You are a Gen Z.")
elif year >= 2010:
    print("You are Gen Alpha")
elif year >= 2024:
    print("You are Gen Beta")
else:
    print("That is the wrong input")
