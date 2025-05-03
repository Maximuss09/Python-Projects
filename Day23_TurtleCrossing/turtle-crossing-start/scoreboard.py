import turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.pu()
        self.goto(-260, 250)
        self.write(f"level: {self.level}", align="left", font=FONT)

    def update(self):
        self.clear()
        self.write(f"level: {self.level}", align="left", font=FONT)
    
    def increse_level(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="left", font=FONT)



