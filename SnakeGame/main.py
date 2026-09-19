from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect the snake's collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    # Detect the snake's collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
        print("Game Over! You collided with the wall!")

    # Detect the snake's collision with tail
    #if head collides with any segment in tail
    for position in snake.segments[1:]:
        if snake.head.distance(position) < 10:
            game_is_on = False
            scoreboard.game_over()









screen.exitonclick()