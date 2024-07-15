mport pandas
import turtle
from turtle import *

screen = Screen()
screen.title('US_States')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
states_list = data['state'].to_list()
# print(states_list)

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct",
                                    "Enter the name of the states:").title()
    if answer_state in states_list:
        t = Turtle()
        t.penup()
        t.hideturtle()
        name = data[data.state == answer_state]
        t.goto(int(name.x), int(name.y))
        t.write(answer_state)
        t.hideturtle()
        guessed_states.append(answer_state)

    if answer_state == 'Exit':
        miss_states = [state for state in states_list if state not in guessed_states]
        learn = pandas.DataFrame(miss_states)
        learn.to_csv('learn.csv')
        break
