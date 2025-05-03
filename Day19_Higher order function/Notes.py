import turtle as tp

ted = tp.Turtle()
screen = tp.Screen()

def move_forwards():
    ted.forward(20)

def move_backwards():
    ted.back(20)

def turn_left():
    ted.left(90)

def turn_right():
    ted.right(90)

def clear_screem():
    ted.clear()
    ted.pu()
    ted.home()
    ted.pd()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screem)


screen.exitonclick()
