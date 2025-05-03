# import colorgram


# colors = colorgram.extract('spots_colors.jpg', 8)
# rgb_colors = [ ]

# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

# print(rgb_colors)
import random
import turtle

turtle.colormode(255)
color_list = [(199, 175, 117), (73, 136, 224), (181, 142, 213), (168, 106, 57), (181, 218, 227), (186, 158, 53)]

jimmy_the_turtle = turtle.Turtle()
jimmy_the_turtle.shape('turtle')

x = -250
y = 250

jimmy_the_turtle.hideturtle()
jimmy_the_turtle.penup()
jimmy_the_turtle.setpos(x,y)
jimmy_the_turtle.penup()

def drawing():
    jimmy_the_turtle.color(random.choice(color_list))
    jimmy_the_turtle.pd()
    jimmy_the_turtle.dot(20)
    jimmy_the_turtle.pu()
    

for _ in range(1, 11):
    for _ in range(1, 11):
        drawing()
        jimmy_the_turtle.forward(50)
    y -= 50
    jimmy_the_turtle.setpos(x, y)

screen = turtle.Screen()
screen.exitonclick()