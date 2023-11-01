import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S., States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor())
#
# # Keep the screen open
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
states = data.state.tolist()
x = data.x.tolist()
y = data.y.tolist()

t = turtle.Turtle()
t.penup()
t.color("black")
t.hideturtle()

guessed_states=[]
while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?" ).title()

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        # missing_states = []
        # for state in states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break



    if answer_state in states:
        guessed_states.append(answer_state)
        index = states.index(answer_state)
        x_move = x[index]
        y_move = y[index]
        # A row of data. state_data.x, state_data.y
        # state_data = data[data.state == answer_state]
        t.goto(x_move, y_move)
        t.write(answer_state)










