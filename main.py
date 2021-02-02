
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")

screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()
l_scorebaord = Scoreboard((-100, 190))
r_scorebaord = Scoreboard((100, 190))


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
            ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        l_scorebaord.increase()

    if ball.xcor() < -380:
        ball.reset_position()
        r_scorebaord.increase()

    if l_scorebaord.score == 5 or r_scorebaord.score == 5:
        game_is_on = False

winner = Scoreboard((0, 0))
if l_scorebaord.score-r_scorebaord.score > 0:
    winner.print_winner("left")
else:
    winner.print_winner("right")

screen.exitonclick()

