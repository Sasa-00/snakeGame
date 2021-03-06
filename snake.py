from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    # Function of initialization
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # This function is calling when we want to create a snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    # This function is calling when we want to move a snake constantly forward
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Next four functions is for keyboard functionality (controlling with arrows)
    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    # This function allows us to size up our snake
    def adding_segments(self):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(new_segment)

    # If our snake bites itself, or hit the wall, this function bring it to start from scratch
    def restart(self):
        for seg in self.segments:
            seg.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]