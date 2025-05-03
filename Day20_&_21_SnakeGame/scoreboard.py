import turtle


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.tracking_score = 0
        
        self.pu()
        self.goto(0, 320)
        self.write(arg= f"Score: {self.tracking_score}", move= False, align="center", font=('Times New Roman', 18, 'bold'))
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center", font=('Times New Roman', 18, 'bold'))

    def increase_score(self):
        self.tracking_score += 1
        self.clear()
        self.write(arg= f"Score: {self.tracking_score}", move= False, align="center", font=('Times New Roman', 18, 'bold'))