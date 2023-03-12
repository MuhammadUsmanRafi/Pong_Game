from turtle import Screen
from ball import Ball
from Paddle import Paddle
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.tracer(0)

# screen setting
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")


Paddle_r = Paddle((380, 0))
Paddle_l = Paddle((-390, 0))
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(Paddle_r.go_up, "Up")
screen.onkey(Paddle_r.go_down, "Down")
screen.onkey(Paddle_l.go_up, "w")
screen.onkey(Paddle_l.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(Paddle_r) < 30 and ball.xcor() > 320 or ball.distance(Paddle_l) < 30 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 410:
        scoreboard.r_score()
        ball.reset_ball()

    if ball.xcor() < -410:
        scoreboard.l_score()
        ball.reset_ball()

    if scoreboard.score_r == 5 or scoreboard.score_l == 5:
        if scoreboard.score_r == 5:
            scoreboard.end_game("r")
            ball.hideturtle()
        else:
            scoreboard.end_game("l")
            ball.hideturtle()
        game_is_on = False

    screen.update()

screen.exitonclick()
