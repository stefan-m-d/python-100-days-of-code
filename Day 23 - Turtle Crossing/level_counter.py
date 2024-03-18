from turtle import Turtle 

ALIGN = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle): 
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 260)
        self.color("black")
        self.speed("fastest")
        self.level = 0 
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align = ALIGN, font = FONT)
    
    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        self.color ("blue")
        self.goto(0, 0)
        self.write ("GAME OVER", align = ALIGN, font = FONT)