import turtle

width_b = 1
height_b = 1
y_move = -10
x_move = -10

class Ball(turtle.Turtle):
    
    def __init__(self, shape = "circle", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.y_move = 10
        self.x_move = 10
        self.move_speed = 0.050
    
    def visual(self):
        self.shapesize(width_b, height_b)
        self.pu()
        self.color('red')
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed -= 0.01

    def r_reset_ball(self):
        self.y_move = -10
        self.x_move = -10
        self.goto([self.x_move, self.y_move])
        self.move_speed = 0.05

    def l_reset_ball(self):
        self.y_move = 10
        self.x_move = 10
        self.goto([self.y_move, self.x_move])
        self.move_speed = 0.05