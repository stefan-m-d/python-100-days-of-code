from turtle import Turtle 

ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle): 
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.speed("fastest")
        self.score_left = 0
        self.score_right = 0
        self.score = str(self.score_left)+" | "+str(self.score_right)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGN, font = FONT)
    
    def increase_score(self,dir):
        if dir == 1:
            self.score_left += 1
            self.score = str(self.score_left)+" | "+str(self.score_right)
        else: 
            self.score_right += 1
            self.score = str(self.score_left)+" | "+str(self.score_right)
        self.clear()
        self.update_scoreboard()
        
    def game_over(self, winner):
        self.color ("blue")
        self.goto(0, 0)
        self.write (f"GAME OVER! Winner is {winner} .", align = ALIGN, font = FONT)