import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.tracking_score_l = 0
        self.tracking_score_r = 0
        self.color('white')
        self.pu()
        self.goto(0, 300)
        self.write(arg= f"Left: {self.tracking_score_l}      |", move= False, align="right", font=('Courier', 25, 'bold'))
        self.write(arg= f"      Right: {self.tracking_score_r}", move= False, align="left", font=('Courier', 25, 'bold'))
        
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center", font=('Courier', 20, 'bold'))

    def increase_score_l(self):
        self.tracking_score_l += 1
        self.clear()
        self.write(arg= f"Left: {self.tracking_score_l}      |", move= False, align="right", font=('Courier', 25, 'bold'))
        self.write(arg= f"      Right: {self.tracking_score_r}", move= False, align="left", font=('Courier', 25, 'bold'))
        
    def increase_score_r(self):
        self.tracking_score_r += 1
        self.clear()
        self.write(arg= f"Left: {self.tracking_score_l}      |", move= False, align="right", font=('Courier', 25, 'bold'))
        self.write(arg= f"      Right: {self.tracking_score_r}", move= False, align="left", font=('Courier', 25, 'bold'))
        
        
          