'''
def my_function():
    print("Hello")
    print("bye")

my_function()
'''

# Reeborg's World

"""

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
 
    def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
def jump():
    turn_left()
    while wall_on_right() == True and front_is_clear == False:
        move()
        turn_right()
    while front_is_clear == True:
        move()


while at_goal() == False:
    if front_is_clear () == True:
        move()
    elif wall_on_right() == True:
        jump()
    elif front_is_clear and wall_on_right() == False:
        turn_right()
    elif wall_on_right == False:
        turn_left()
       



"""
