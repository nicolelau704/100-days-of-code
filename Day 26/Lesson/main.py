numbers = [1,2,3]
new_list = [(n+1) for n in numbers]
print(new_list)

name = "nicole"
letters = [letter for letter in name]
print(letters)

double = [(n*2) for n in range(1,5)]
print(double)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Frank"]
short_names = [n for n in names if (len(n) < 5)]
long_names = [l.upper() for l in names if (len(l) > 4)]
print(short_names)
print(long_names)

