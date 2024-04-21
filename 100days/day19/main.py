import turtle
from turtle import *
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which color will win the race:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
pos = -100
all_turtles = []

for color in colors:
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(x=-230, y=pos)
    pos += 40
    all_turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You've won! The {turtle.pencolor()} turtle won")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle won")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)


screen.exitonclick()