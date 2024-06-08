from turtle import Turtle, Screen
from snake_class import Snake
from snake_food import Food
from snake_scorecard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nokia's Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.up, "W")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "Down")
screen.onkey(snake.down, "s")
screen.onkey(snake.down, "S")
screen.onkey(snake.right, "Right")
screen.onkey(snake.right, "d")
screen.onkey(snake.right, "D")
screen.onkey(snake.left, "Left")
screen.onkey(snake.left, "a")
screen.onkey(snake.left, "A")


def hit_wall():
    if snake.head.xcor() > 280:
        return True
    if snake.head.xcor() < -280.0:
        return True
    if snake.head.ycor() > 280:
        return True
    if snake.head.ycor() < -280:
        return True


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detecting collision with food
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend()
        scoreboard.increase_score()
    if hit_wall():
        game_is_on = False
        scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
