import turtle
from turtle import *

screen = Screen()
screen.title('US_States')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

score = 0

answer_state = screen.textinput(f"{score}/50 States Correct", "Enter the name of the states:")

with open('50_states.csv') as file