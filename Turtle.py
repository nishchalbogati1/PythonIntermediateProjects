import turtle
from turtle import Turtle,Screen
import random

tur = Turtle()
tur.shape("turtle")

# tur.forward(100)
# tur.right(90)
# tur.forward(100)
# tur.right(90)
# tur.forward(100)
# tur.right(90)
# tur.forward(100)
#
# for _ in range(4):
#     tur.forward(100)
#     tur.left(90)

# for _ in range(10):
#     tur.pendown()
#     tur.forward(10)
#     tur.penup()
#     tur.forward(10)

# no_sides = 3
# is_on = True
# while is_on:
#     shape_color = random.choice(color)
#     tur.color(shape_color)
#     color.remove(shape_color)
#     angle = 360 / no_sides
#     for _ in range(no_sides):
#         tur.forward(100)
#         tur.left(angle)
#     no_sides += 1
#     print(no_sides)
#     if no_sides > 10:
#         is_on = False

color = ["royal blue", "lime", "red", "green", "pink", "yellow", "cyan", "purple"]
turtle.colormode(255)
direction = [0, 90, 180, 270]
tur.pensize(1)
tur.speed(20)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color =  (r,g,b)
    return random_color

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tur.color(random_color())
        tur.circle(100)
        tur.setheading(tur.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()