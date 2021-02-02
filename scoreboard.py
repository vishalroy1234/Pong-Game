from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(position)
        if position == (0, 0):
            pass
        else:
            self.print_score()

    def print_score(self):
        self.write(f"{self.score}", False, "center", ("Courier", 80, "normal"))

    def print_winner(self, winner):
        self.write(f"{winner} player wins", False, "center", ("Courier", 30, "normal"))

    def increase(self):
        self.clear()
        self.score += 1
        self.print_score()
