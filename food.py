from turtle import Turtle
import random
COLORS = ["purple", "green", "blue", "red", "yellow", "orange", "pink", "gray"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color("purple")
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.color(random.choice(COLORS))


