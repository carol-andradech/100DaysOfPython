import turtle
import turtle as t
from turtle import  Turtle, Screen
import random


tim = t.Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("blue")
# for x in range(0,4):
#     tim.forward(100)
#     tim.left(90)

# for x in range(0, 15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


#draw form with different colors
# colors = ['red', 'green', 'blue', 'purple', 'orange', 'yellow', 'pink', 'cyan', 'magenta', 'brown']
#
# def angle(sides):
#     return 360/sides
#
# def draw(sides):
#     angle_form = angle(sides)
#     for i in range (sides):
#         tim.forward(100)
#         tim.left(angle_form)
#
# for x in range(3, 11):
#     tim.color(random.choice(colors))
#     draw(x)

# colors = ['red', 'green', 'blue', 'purple', 'orange', 'yellow', 'pink', 'cyan', 'magenta', 'brown']
# direction = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed("fastest")

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
#
# for x in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))



for y in range(36):
    tim.color(random_color())
    tim.circle(50)
    move = tim.heading() + 10
    tim.setheading(move)





# Heart <3
# tim.color("red")
# tim.speed(1)
# tim.penup()
# tim.goto(0, -100)
# tim.pendown()
#
# tim.begin_fill()
# tim.left(140)
# tim.forward(224)
#
# for x in range(200):
#     tim.right(1)
#     tim.forward(2)
# tim.left(120)
# for x in range(200):
#     tim.right(1)
#     tim.forward(2)
# tim.forward(224)
# tim.end_fill()





screen.exitonclick()
