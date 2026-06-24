try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in an invalid number. Please try again using a numerical input like 10")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
else:
    print(f"You cannot drive at {age}.")
