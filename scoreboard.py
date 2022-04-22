from turtle import Turtle


# Static function for reading high score from score_history.txt
def score_history_read():
    with open("score_history.txt") as file:
        score_string = file.read()
        for char in score_string.split():
            if char.isdigit():
                score = char
        return int(score)


# Static function for writing high score to score_history.txt
def score_history_write(score):
    with open("score_history.txt", "w") as file:
        file.write(f"High_score = {score}")


class ScoreBoard(Turtle):

    # Function of initialization
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = score_history_read()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    # This function drawing a scoreboard at the top of game screen
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 18, "normal"))

    # This function updating scoreboard when food is eaten
    def increase_score(self):
        self.score += 1
        self.update_score()

    # This function is controlling above static function and update high score
    def high_score_fun(self):
        if self.score > self.high_score:
            self.high_score = self.score
            score_history_write(self.high_score)
        self.score = 0
        self.update_score()

