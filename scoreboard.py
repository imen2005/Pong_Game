from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align= "center", font= ("Courier", 50, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align= "center", font= ("Courier", 50, "normal"))