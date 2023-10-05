import random
import turtle as t
from turtle import  Turtle, Screen
import random


tim = t.Turtle()
screen = Screen()
tim.shape("turtle")
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

color_generated = random_color()
color_rgb = tim.dot(50, color_generated)
tim.penup()
tim.forward(100)


# print(color_generated)
red = color_generated[0]
green = color_generated[1]
blue = color_generated[2]

if( red > green and red > blue):
    print("The color has more red")

if( green > red and green > blue):
    print("The color has more green")

if( blue > green and blue > red):
    print("The color has more blue")


screen.exitonclick()