from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("fastest")


def move_forwards():
    tim.forward(5)

def move_backwards():
    tim.backward(5)

def rotate_clockwise():
    tim.right(5)

def rotate_counterclockwise():
    tim.left(5)

def draw_circle():
    tim.circle(5)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="d", fun=rotate_clockwise)
screen.onkeypress(key="a", fun=rotate_counterclockwise)
screen.onkeypress(clear_drawing, "c")

screen.exitonclick()
