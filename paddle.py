from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        self.goto(self.xcor(), self.ycor()-20)


