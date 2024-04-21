from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.speed('fast')
turtle.width(5)
colorList = [
  'AliceBlue',
  'AntiqueWhite',
  'Aqua',
  'Aquamarine',
  'Azure',
]

# def draw_shape(sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         turtle.forward(10)
#         turtle.right(angle)
#
# for shape_side in range(3,11):
#     turtle.color(random.choice(colorList))
#     draw_shape(shape_side)

# directions = [1,2,3,4]
# steps = 10000
# dist = 10
#
# for _ in range(0, steps):
#     dir = random.choice(directions)
#     turtle.pencolor(random.choice(colorList))
#     turtle.right(random.choice(directions) * 90)
#     turtle.fd(dist)



screen = Screen()
screen.exitonclick()
