from turtle import Turtle
Alignment= "center"
Font = ("Arial", 15, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,220)
        self.update_scoreborad()
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=Alignment, font=Font)
    def update_scoreborad(self):
        self.write(f"Score: {self.score}", align=Alignment, font=Font)
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreborad()
