from turtle import Turtle

class Turtle_Crosser (Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def reset_position(self, position):
        self.goto(position)