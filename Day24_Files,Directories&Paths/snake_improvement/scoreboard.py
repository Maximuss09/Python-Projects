import turtle




class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.tracking_score = 0
        with open("data") as data: 
            self.high_score = int(data.read())
        self.pu()
        self.goto(0, 320)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(0, 320)
        self.write(arg= f"Score: {self.tracking_score}    |     High Score: {self.high_score}", 
                   move= False, align="center", font=('Times New Roman', 18, 'bold'))



    def restore(self):
        if self.tracking_score > self.high_score:
            self.high_score = self.tracking_score
            with open("data", mode='w') as data: 
                data.write(f"{self.high_score}")
        self.tracking_score = 0
        self.update_scoreboard()
        

    def game_over(self):
        self.goto(0,100)
        self.write("GAME OVER",align="center", font=('Times New Roman', 18, 'bold'))
    


    def increase_score(self):
        self.tracking_score += 1
        # self.clear()
        self.update_scoreboard()
        