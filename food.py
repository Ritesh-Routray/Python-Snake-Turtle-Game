from turtle import *
import random

class Food(Turtle):

    # function used to create the food for the snake
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(x=random.randint(-270, 270), y=random.randint(-270, 270))