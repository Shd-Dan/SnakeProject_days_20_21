from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # attribute added in day24 lesson
        with open("data.txt", mode='r') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Scoreboard: {self.score} High score {self.high_score}", align=ALIGNMENT, font=FONT)

    # day24
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    def counter(self):
        self.score += 1
        self.update_scoreboard()
