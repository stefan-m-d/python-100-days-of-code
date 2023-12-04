# import colorgram

# rgb_colors = []
# colors = colorgram.extract("D:\python course code and others\Day 18 - Turtle GUI\Hirst Painting Project\image.jpg", 25)
# for color in colors: 
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    
# print (rgb_colors)

colors_list = [(184, 147, 94), (151, 104, 46), (228, 229, 231), (178, 150, 22), (83, 34, 27), (12, 57, 73), (31, 100, 120), (101, 41, 47), (56, 137, 122), (108, 39, 29), (22, 65, 50), (39, 81, 7), (94, 62, 68), (199, 91, 65), (110, 8, 9), (116, 167, 77), (226, 232, 227), (131, 178, 92), (139, 167, 176), (217, 203, 140), (179, 148, 151), (177, 205, 178), (226, 177, 167)]

#Requirements for painting
# 10 by 10 rows of dots
# each dot is 20 in diameter with 50 spacing between them

import turtle as t 
import random
t.colormode(255)

voldetort = t.Turtle()

voldetort.speed(0)
voldetort.penup()
voldetort.hideturtle()

voldetort.setheading(225)
voldetort.forward(300)
voldetort.setheading(0)
number_of_dots=100

for dot_count in range(1, number_of_dots+1):
    voldetort.dot(20, random.choice(colors_list))
    voldetort.forward(50)
    
    if dot_count % 10 == 0:
        voldetort.setheading(90)
        voldetort.forward(50)
        voldetort.setheading(180)
        voldetort.forward(500)
        voldetort.setheading(0)

screen = t.Screen()
screen.exitonclick()