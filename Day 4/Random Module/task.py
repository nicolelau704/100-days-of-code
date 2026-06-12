import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.my_favorite_number)

rand_num_0_to_1 = random.random()
print(rand_num_0_to_1)

#1
coin_side = random.randint(1,2)
if coin_side == 0:
    print("Heads")
else:
    print("Tails")
