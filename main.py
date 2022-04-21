from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(600, 600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score_table = ScoreBoard()

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

run = True

while run:
    screen.update()
    time.sleep(0.08)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.adding_segments()
        score_table.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_table.high_score_fun()
        snake.restart()

    for segment in snake.segments[1:]:
        if snake.head.position() == segment.position():
            score_table.high_score_fun()
            snake.restart()

screen.exitonclick()
