from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
from middle_dotted_line import Dotted_Line_Center
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
left_cor = (350,0)
right_cor = (-350,0)

r_paddle = Paddle(left_cor)
l_paddle = Paddle(right_cor)
ball = Ball()
scoreboard = Scoreboard()
center = Dotted_Line_Center()

center.draw_line()

screen.listen()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #Detect collision with wall
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #Detect collision with paddles
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    elif ball.xcor() > 370:
        scoreboard.increase_score(1)
        ball.reset_position()
    elif ball.xcor() < -370: 
        scoreboard.increase_score(0)
        ball.reset_position()
    
    #Game over condition - score 10 points
    
    if scoreboard.score_left == 10:
        game_on = False
        scoreboard.game_over(winner="Left")
    elif scoreboard.score_right == 10:
        game_on = False 
        scoreboard.game_over(winner="Right")
        
    
screen.exitonclick()