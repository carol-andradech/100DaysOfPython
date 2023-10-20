# Part 1
# Create a snake body
# Move the Snake
# Control the Snake
# Part 2
# Detect collision with food
# Create a scoreboard
# Detect collision with wall
# Detect collision with tail

from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food= Food()
scoreboard = Scoreboard()

screen.listen()
# UP:90ª, LEFT:180ª, DOWN:270ª, RIGHT:0ª
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # Delay for 0.1s and then refresh the screen
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset() 


    #Detect colision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()




screen.exitonclick()