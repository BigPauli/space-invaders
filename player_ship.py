from turtle import *


class PlayerShip(Turtle):
    def __init__(self):
        super(PlayerShip, self).__init__()
        self.up()
        self.speed('fastest')
        self.color('white')
        self.shapesize(stretch_wid=4, stretch_len=4)
        self.setheading(90)
        self.goto(x=0, y=-400)

    def move_left(self):
        if self.xcor() > -1420:
            self.setheading(180)
            self.forward(10)
            self.setheading(90)

    def move_right(self):
        if self.xcor() < 1420:
            self.setheading(0)
            self.forward(10)
            self.setheading(90)

    def back_to_start(self):
        self.goto(x=0, y=-400)