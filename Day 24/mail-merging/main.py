#Open the template letter and save its contents to variable letter_contents
with open("Input/Letters/starting_letter.txt") as file_letter:
    letter_contents = file_letter.read()

#Open the list of names and save them to a list
with open("Input/Names/invited_names.txt") as file_names:
    name_list = file_names.read()
    formatted_names = name_list.splitlines()

#For each name in the list, create a personalized letter using the template letter_contents
for name in formatted_names:
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as new_letter:
        content = letter_contents.replace("[name]", f"{name}")
        new_letter.write(f"{content}")
