from turtle import Turtle

starting_position = [(0,0), (-20,0), (-40,0)]
move_distance = 20

class Snakes:


    def __init__(self):
        self.my_turtles = []
        self.create_snake()
        self.head = self.my_turtles[0]

    # function used to create snake
    def create_snake(self):
        for pos in starting_position:
            self.add_segment(pos)

    # function used to add segments and extend the snakes
    def add_segment(self, pos):
        rishi = Turtle()
        rishi.shape("turtle")
        rishi.color("white")
        rishi.penup()
        rishi.goto(pos)
        self.my_turtles.append(rishi)

    def extend(self):
        self.add_segment(self.my_turtles[-1].position())


    # function used to move the snake
    def move(self):
            for tur in range(len(self.my_turtles) -1, 0, -1):
                new_x = self.my_turtles[tur-1].xcor()
                new_y = self.my_turtles[tur - 1].ycor()
                self.my_turtles[tur].goto(new_x,new_y)
                self.my_turtles[0].speed("fastest")
            self.my_turtles[0].forward(move_distance)

    # different functions used to control the snake movements
    def up(self):
        self.my_turtles[0].setheading(90)

    def down(self):
        self.my_turtles[0].setheading(270)

    def left(self):
        self.my_turtles[0].setheading(180)

    def right(self):
        self.my_turtles[0].setheading(0)