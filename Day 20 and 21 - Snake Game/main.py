import time
import random
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on: 
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # feeding time
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    
    # detect collision with wall
    
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_on = False
        scoreboard.game_over()
    
    # detect collision with tail
    
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
    
screen.exitonclick()