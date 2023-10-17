import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.onkey(player.move,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > 290:
       # New level
        scoreboard.new_level()
        player.reset()


    for car in car_manager.all_cars:
        if car.distance(player)<20:
            player.reset()
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()