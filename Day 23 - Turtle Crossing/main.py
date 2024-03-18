from turtle import Turtle, Screen
from turtle_crosser import Turtle_Crosser
from car import CarManager
import time 
from level_counter import Scoreboard

#set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
starting_position = (0, -280)

turtle = Turtle_Crosser(starting_position)

car_manager = CarManager()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(turtle.go_up, "w")

game_on = True

while game_on:
    
    time.sleep(0.1)
    screen.update ()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    #detect collision with cars
    
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            scoreboard.game_over()
            game_on = False
    
    #detect if player has passed the level
    
    if turtle.ycor() == 280:
        turtle.reset_position(starting_position)
        scoreboard.increase_level()
        car_manager.remove_cars()
        car_manager.increase_speed()
        
screen.exitonclick()