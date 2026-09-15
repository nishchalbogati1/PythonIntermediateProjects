from turtle import Screen,Turtle
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_positions = [(0,0), (-20,0), (-40,0)]
positions = []

for position in starting_positions:
    new_position = Turtle("square")
    new_position.penup()
    new_position.color("white")
    new_position.goto(position)
    positions.append(new_position)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for pos_num in range(len(positions) - 1, 0,-1):
        new_x = positions[pos_num - 1].xcor()
        new_y = positions[pos_num - 1].ycor()
        positions[pos_num].goto(new_x, new_y)
    positions[0].forward(20)












screen.exitonclick()