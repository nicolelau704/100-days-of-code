#Open, read, and then close a file using python
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

#Another way to access a file without opening it
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

#Write to a file(replace the contents)
# with open("my_file.txt", mode="w") as file:
#     file.write("\nNew text.")

#Write to a file(Append to it)
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")

#Create a new file by opening a file in write mode
# with open("new_file.txt", mode="w") as file:
#     file.write("This is my new file.")

#Read the file when it's located in a different place
with open("../Lesson/new_file.txt") as file:
    contents = file.read()
    print(contents)
