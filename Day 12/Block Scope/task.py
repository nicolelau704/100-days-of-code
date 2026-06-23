#There is no block scope in python!
#
# if 3 > 2:
#     a_variable = 10 #global scope

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
#
# if game_level < 5:
#     new_enemy = enemies[0]
#
# print(new_enemy) #skeleton prints out because it's a global variable

#Recommends doing this instead
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = ""  #best to declare a variable with an empty string in case the game level is greater than 5
                    #because otherwise the variable is never declared inside the if statement
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)
