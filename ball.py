from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_move = 10
        self.x_move = 10
        self.move_speed = 0.1

    def move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        if self.move_speed > 0:
            self.move_speed -= 0.005

    def reset_ball(self):
        self.move_speed = 0.1
        self.setposition(0, 0)
        num = random.randint(0, 1)
        if num == 0:
            self.bounce_x()
        else:
            self.bounce_y()
