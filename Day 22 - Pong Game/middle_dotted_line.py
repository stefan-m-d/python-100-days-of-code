from turtle import Turtle

class Dotted_Line_Center (Turtle): 
    def __init__(self):
        super().__init__()
        self.shape ("square")
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.speed("fastest")
        self.setheading(270)
        self.pensize(7)
        
    def draw_line(self):
        self.pendown()
        for x in range (280, -280, -40):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
        
        self.hideturtle()