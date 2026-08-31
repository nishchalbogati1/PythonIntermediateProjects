import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
turtle.colormode(255)
tim_1 = Turtle()
tim_2 = Turtle()
tim_3 = Turtle()
tim_4 = Turtle()
tim_5 = Turtle()
turtles = [tim_1, tim_2, tim_3, tim_4, tim_5]
colors = ["red", "green", "blue", "yellow", "purple"]

def speed(turtles):
    for turtle in turtles:
        turtle.shape("turtle")
        turtle_color = random.choice(colors)
        colors.remove(turtle_color)
        turtle.color(turtle_color)
        turtle.penup()

screen.setup(width=500, height=500)
speed(turtles)
is_on = True
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? ")
tim_1.goto(-225,0)
tim_2.goto(-225,50)
tim_3.goto(-225,-50)
tim_4.goto(-225,100)
tim_5.goto(-225,-100)
while is_on:
    for turtle in turtles:
        turtle.forward(random.randrange(10, 20, 5))
        if turtle.xcor() >= 225:
            winner = turtle
            is_on = False
            break

if winner.color()[0] == user_bet:
    print(f"You guessed correctly! {winner.color()[0].capitalize()} turtle is the winner!")
else:
    print(f"Your guess was wrong! {winner.color()[0].capitalize()} turtle is the winner!")
screen.exitonclick()
