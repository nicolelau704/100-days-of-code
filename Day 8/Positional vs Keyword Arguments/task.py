# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Jack Bauer")

#Functions with multiple inputs
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Nicole", "California")  #positional argument
greet_with(location = "California", name = "Nicole")  #keyword argument
