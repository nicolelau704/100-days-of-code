#Lesson on Object Oriented Programming (OOP)

#Use the Turtle Class
# import turtle
#
# timmy = turtle.Turtle()       #create a turtle object from the Turtle class
# print(timmy)
# timmy.shape("turtle")     #modify the object using a method
# timmy.color("DarkSeaGreen")
# timmy.forward(100)
#
# my_screen = turtle.Screen()   #display the turtle on the screen
# print(my_screen.canvheight)
# my_screen.exitonclick()

#Use the prettytable package
from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]    #use a method to change your object
table.add_row(["Pikachu","Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.align = "l"   #use attributes to change the style of the table
print(table)