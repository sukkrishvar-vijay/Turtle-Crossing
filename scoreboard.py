from turtle import Turtle
FONT = ("Courier", 12, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        #self.color("white")
        self.penup()
        self.hideturtle()
        self.level_score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 270)
        self.write(f"Level: {self.level_score}", align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
