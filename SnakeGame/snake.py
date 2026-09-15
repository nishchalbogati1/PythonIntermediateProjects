from turtle import Turtle

class Snake:
    def __init__(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.positions = []

        for position in starting_positions:
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
        self.positions[0].forward(20)

