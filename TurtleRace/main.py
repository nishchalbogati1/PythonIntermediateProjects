import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
turtle.colormode(255)
screen.setup(width=500, height=500)
colors = ["red", "orange", "green", "blue", "yellow", "purple"]
turtles = []

def create_turtles():
    for _ in range(6):
        turtles.append(Turtle())

def speed(turtles):
    for turtle in turtles:
        turtle.shape("turtle")
        turtle_color = random.choice(colors)
        colors.remove(turtle_color)
        turtle.color(turtle_color)
        turtle.penup()

def starting_position():
    y = [0, 40, -40, 80, -80, 120]
    for turtle,y in zip(turtles,y):
        turtle.goto(-200, y)


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? ").lower()

if user_bet:
    is_on = True
else:
    is_on = False

create_turtles()
speed(turtles)
starting_position()

while is_on:
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() >= 225:
            winner = turtle
            is_on = False
            break

if winner.color()[0] == user_bet:
    print(f"You guessed correctly! {winner.color()[0].capitalize()} turtle is the winner!")
else:
    print(f"Your guess was wrong! {winner.color()[0].capitalize()} turtle is the winner!")
screen.exitonclick()
