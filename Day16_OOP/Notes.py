'''
Object Oriented Programming = OOP
In OOP we're trying to module real life objects and those objects have:
attributes. And also can do things: mothods

'''

# All about the turtle: https://docs.python.org/3/library/turtle.html
# PrettyTable doc: https://pypi.org/project/prettytable/
import turtle

tommas = turtle.Turtle()
print(tommas)
tommas.shape("turtle")
tommas.color("red")
tommas.forward(100)




# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable

table = prettytable.PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"]
    ]
)

table.align = "r"

#print(table)