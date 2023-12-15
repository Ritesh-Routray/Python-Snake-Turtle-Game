from turtle import *

class Score_board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.color("white")
        self.touch()
        self.update_score_board()

    # function used to update the score board of game
    def update_score_board(self):
        self.write(f"Score = {self.score}", align="center", font=("Arial", 24, "normal"))

    # function used to detect when the game is over
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24,"normal"))

    def touch(self):
        self.score += 1
        self.clear()
        self.update_score_board()