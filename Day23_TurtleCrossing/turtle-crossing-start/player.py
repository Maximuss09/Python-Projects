import turtle

STARTING_POSITION = (-50, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    def __init__(self, shape = "turtle", undobuffersize = 1000, visible = True, ):
        super().__init__(shape, undobuffersize, visible)
  

    def movement(self):
        self.pu()        
        self.speed("fastest")
        self.turtlesize(1, 1, 0.5)
        self.seth(90)
        self.goto(STARTING_POSITION)

    def start_position(self):
        self.goto(STARTING_POSITION)


    def walking(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False






