from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.positions = []
        self.create_snake()
        self.head = self.positions[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_position = Turtle("square")
            new_position.penup()
            new_position.color("white")
            new_position.goto(position)
            self.positions.append(new_position)

    def move(self):
        for pos_num in range(len(self.positions) - 1, 0, -1):
            new_x = self.positions[pos_num - 1].xcor()
            new_y = self.positions[pos_num - 1].ycor()
            self.positions[pos_num].goto(new_x, new_y)
        self.positions[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)