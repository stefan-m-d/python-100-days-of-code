import random
from turtle import Turtle, Screen

race_on = False

screen = Screen()

#set screen - X,Y = 0,0 is the very center of it. 
screen.setup(width=500, height=400)

user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race? Enter a color (purple, blue, green, yellow, orange, red): ")

colors = ["purple", "blue", "green", "yellow", "orange", "red"]

y_positions = [160, 120, 80, 40, 0, -40]

all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
    

if user_bet:
    race_on = True

while race_on: 
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()