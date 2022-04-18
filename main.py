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
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

run = True

while run:
    screen.update()
    time.sleep(0.08)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.adding_segments()
        score_table.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or  snake.head.ycor() > 290 or snake.head.ycor() < -290:
        run = False
        score_table.game_over()

    for segment in snake.segments[1:]:
        if snake.head.position() == segment.position():
            run = False
            score_table.game_over()

screen.exitonclick()
