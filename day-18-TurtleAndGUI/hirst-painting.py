import random
import colorgram
import turtle as turtle_module
from turtle import  Screen

# Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
# color_drop =[]
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_drop.append(new_color)
#
# print(color_drop)
color_list = [(246, 243, 241), (245, 241, 243), (231, 245, 238), (177, 12, 35), (182, 171, 16), (210, 159, 81), (244, 214, 77), (237, 242, 247), (177, 76, 29), (168, 23, 16), (118, 181, 200), (218, 130, 160), (54, 95, 153), (246, 64, 23), (62, 48, 108), (65, 36, 57), (158, 52, 75), (105, 188, 165), (39, 134, 89), (36, 53, 71), (218, 73, 129), (72, 47, 40), (24, 168, 149), (148, 212, 222), (53, 171, 187), (238, 202, 4), (160, 183, 228), (233, 165, 182), (41, 61, 59), (81, 104, 184)]
turtle_module.colormode(255)
tim = turtle_module.Turtle()
screen = Screen()
tim.shape("turtle")

size_dot = 20
size_space = 50
i = 10
j = 10

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for dot_count in range(1 ,i*j):
    tim.dot(size_dot, random.choice(color_list))
    tim.forward(size_space)
    if dot_count % 10 == 0 :
        tim.setheading(90)
        tim.forward(size_space)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen.exitonclick()