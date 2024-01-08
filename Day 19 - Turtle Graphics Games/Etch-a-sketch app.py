from turtle import Turtle, Screen

tim = Turtle()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def rotate_left():
    tim.left(10)

def rotate_right():
    tim.right(10)

screen = Screen()

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

#move forward

screen.onkeypress(key="w", fun=move_forwards)

#move backwards
screen.onkeypress(key="s", fun=move_backwards)

#rotate left

screen.onkeypress(key="a", fun=rotate_left)

#rotate right

screen.onkeypress(key="d", fun=rotate_right)

#clear screen
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()