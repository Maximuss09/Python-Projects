import turtle
import random

tommas_turtle = turtle.Turtle()

# tommas_turtle.shape("turtle")

# for _ in range(4):
#    tommas_turtle.forward(100)
#    tommas_turtle.right(90)

# for _ in range(10):

#    tommas_turtle.forward(10)
#    tommas_turtle.penup()
#    tommas_turtle.forward(10)
#    tommas_turtle.pendown()

#-----------------------------------
"MANY SHAPES WITH DIFFERENT COLORS"

# colours = ["red", "blue", "green", "gray", "purple", "purple2", "salmon"]

# def drew_shape(num_sides):
#    angle = 360/num_sides
#    for _ in range (num_sides):
#        tommas_turtle.forward(100)
#        tommas_turtle.right(angle)

# for shape_side in range(3, 11):
#    tommas_turtle.color(random.choice(colours))
#    drew_shape(shape_side)

# ---------------------------------------------
"RANDOM WALK"



angle = (90, 180, 360, 270)
tommas_turtle.speed("fast")
turtle.colormode (255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def direction ():
   tommas_turtle.forward(50)
   tommas_turtle.right(random.choice(angle))

def size():
   width = 10
   tommas_turtle.pensize(width)

for _ in range(100):
   tommas_turtle.color(random_color())
   size()
   direction()
    

# -------------------------------------------
"CIRCULOS"


#tommas_turtle.speed("fast")

# def circle ():
#     radio = 200
#     extend = 360
#     steps = 360
#     circle = (radio, extend, steps)
#     return circle

# for _ in range (36):
#     tommas_turtle.speed("fastest")
#     tommas_turtle.pensize(2)
#     tommas_turtle.color(random_color())  
#     tommas_turtle.circle(100)
#     tommas_turtle.right(5)

#  n = 0
# for _ in range(50):
#     tommas_turtle.color(random_color())
#     tommas_turtle.pensize(5)
#     tommas_turtle.right(10)
#     tommas_turtle.speed("fast")
#     for _ in range(360):
#         tommas_turtle.forward(n + 1)
#         tommas_turtle.left(n + 1)
        
# screen = turtle.Screen()
# screen.exitonclick()



