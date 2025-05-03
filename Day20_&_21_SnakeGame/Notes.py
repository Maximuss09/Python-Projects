import turtle
import time

screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.bgcolor("grey")
screen.title("Snake Game")
screen.tracer(0)

# --------------------------------
# "Metodo largo"
snake = turtle.Turtle("square")
# snake2 = turtle.Turtle("square")
# snake3 = turtle.Turtle("square")
# snake2.setx(-20)
# snake3.setx(-40)
# --------------------------------

# starting_position = [(0,0), (-20,0), (-40,0)]
# new_segments = []

# for position in starting_position:
#     segment = turtle.Turtle("square")
#     segment.pu()
#     segment.goto(position)
#     new_segments.append(segment)



# game_on = True

# while game_on:
    
#     screen.update()
#     time.sleep(0.1)
    
#     for seg_num in range(len(new_segments) - 1, 0, -1):
#         new_x = new_segments[seg_num - 1].xcor()
#         new_y = new_segments[seg_num - 1].ycor()
#         new_segments[seg_num].goto(new_x, new_y)
#     new_segments[0].forward(20)
#     new_segments[0].left(90)

#tracking_score = 0

#score = turtle

#score.goto(0, 320)
#score.write(arg= f"Score: {tracking_score}", move= False, align="center", font=('Times New Roman', 18, 'bold'))



screen.exitonclick()
