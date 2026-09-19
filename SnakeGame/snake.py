from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction = RIGHT        # direction of the last actual move
        self.next_direction = RIGHT   # direction requested for the next move

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.shapesize(stretch_wid=0.5, stretch_len=0.5)
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        self.direction = self.next_direction
        self.head.setheading(self.direction)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self,position):
        segment = Turtle("square")
        segment.shapesize(stretch_wid=0.5, stretch_len=0.5)
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def up(self):
        if self.direction != DOWN:
            self.next_direction = UP

    def down(self):
        if self.direction != UP:
            self.next_direction = DOWN

    def left(self):
        if self.direction != RIGHT:
            self.next_direction = LEFT

    def right(self):
        if self.direction != LEFT:
            self.next_direction = RIGHT