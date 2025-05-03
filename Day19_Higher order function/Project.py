import turtle as tp
import random

screen = tp.Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False

x_point = 600
y_point = 550
y_offset = 60

screen.setup(width=x_point, height=y_point)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Pick a color: ").lower
all_turtles = []


for index in range (6):

    ted = tp.Turtle(shape="turtle")
    ted.penup()
    selected_color = random.choice(colors)
    ted.color(selected_color)
    colors.remove(selected_color)
    ted.goto(x=-(x_point/2.2), y=-(y_point/3.5) + (y_offset*index))
    all_turtles.append(ted)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 255:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won. The {winning_color} turtle won")
            else:
                print(f"You lost. The {winning_color} turtle won")


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
             

screen.exitonclick()
