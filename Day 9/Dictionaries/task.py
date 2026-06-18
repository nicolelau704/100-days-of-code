programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

#create a dictionary
colours = {
    "apple": "red",
    "pear" : "green",
    "banana" : "yellow"
}

print(colours["pear"])      #retrieve items from a dictionary

my_empty_dictionary = {}    #create an empty dictionary

colours["peach"] = "pink"   #add to dictionary
colours["apple"] = "maroon" #change dictionary entry

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key] + "\n")