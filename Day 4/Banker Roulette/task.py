import random

#list of friend names
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

which_friend = random.randint(0,4)

#Pick a random name from the list of friends
print(friends[which_friend])

#alternate solution
print(random.choice(friends))

