from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

pad_right = Paddle()
pad_right.position(350)
pad_left = Paddle()
pad_left.position(-350)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(pad_right.go_up, "Up")
screen.onkey(pad_right.go_down, "Down")
screen.onkey(pad_left.go_up, "a")
screen.onkey(pad_left.go_down, "z")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(pad_right) < 50 and ball.xcor() > 320 or ball.distance(pad_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < - 380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()