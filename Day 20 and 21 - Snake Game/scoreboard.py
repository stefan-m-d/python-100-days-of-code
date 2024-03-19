from turtle import Turtle 
import os

filename = "highscore.txt"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, filename)

ALIGN = "right"
ALIGN_HIGHSCORE = "left"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle): 
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.speed("fastest")
        self.score = 0 
        self.highscore = self.get_highscore()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGN, font = FONT)
        self.write_highscore()
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        self.color ("blue")
        self.goto(0, 0)
        self.write ("GAME OVER", align = "center", font = FONT)
        
    def write_highscore(self):
        self.write(f"Highscore: {self.highscore}", align = ALIGN_HIGHSCORE, font = FONT)
        
    def get_highscore(self):
        with open (file_path, "r") as file:
            content = file.read()
        return content
    
    def update_highscore(self):
        if len(str(self.highscore)) == 0 or int(self.score) > int(self.highscore):
            f = open(file_path, "w")
            f.write(str(self.score))
            f.close()
        
