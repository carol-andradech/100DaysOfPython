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

"""
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Center%201&url=worlds%2Ftutorial_en%2Fcenter1.json

count = 0
while front_is_clear():
    move()
    count+=1

walk_final = round(count/2)
turn_left()
turn_left()

for number in range(1, walk_final+1):
    move()
    if number == walk_final:
        put()

Other way:

while front_is_clear():
        move()
        if object_here():
            turn_left()
            turn_left()
            take()
            move()
            if object_here():
                done()
            else:
                put()
                
        if wall_in_front():
            turn_left()
            turn_left()
            put()
            move()

"""
