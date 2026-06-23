# Modifying Global Scope

#Create the global variable
#enemies = "Skeleton"
enemies = 2

#Uses the local variable
# def increase_enemies():
#     enemies = "Ghost"
#     print(f"enemies inside function: {enemies}")

#modifies the global variable
# def increase_enemies():
#     global enemies
#     enemies = "Ghost"
#     print(f"enemies inside function: {enemies}")

#Best not to modify the global variable and just pass a new value back with a return statement
def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1


#Call the function
print(increase_enemies(enemies))
print(f"enemies outside function: {enemies}")


