from turtle import Turtle


def score_history_read():
    with open("score_history.txt") as file:
        score_string = file.read()
        for char in score_string.split():
            if char.isdigit():
                score = char
        return int(score)


def score_history_write(score):
    with open("score_history.txt", "w") as file:
        file.write(f"High_score = {score}")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = score_history_read()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Verdana", 22, "normal"))

    def high_score_fun(self):
        if self.score > self.high_score:
            self.high_score = self.score
            score_history_write(self.high_score)
        self.score = 0
        self.update_score()

