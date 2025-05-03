import turtle

#position_right = (570, 0)
#position_left = (-570, 0)
width = 5
height = 1

class Padel(turtle.Turtle):

    def __init__(self, shape: str = "square", undobuffersize: int = 5000, visible: bool = True,) -> None:
        super().__init__(shape, undobuffersize, visible)


    def move(self, position):    
        self.shapesize(width, height, 0)
        self.pu()
        self.color('white')
        self.goto(position)
        self.speed("fastest")
        
    def go_up(self):
        new_y = self.ycor() + 35
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 35
        self.goto(self.xcor(), new_y)








