# importing modules
import time
import snake
from food import *
from score_board import *

# making object using class
snake = snake.Snakes()
food = Food()
score_board = Score_board()

# setting screen attributes
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Turtle Game")

# setting the screen to function on the keys
my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.right,"Right")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.down,"Down")

# making the snake to move
game = True
while game:
    my_screen.update()
    time.sleep(0.1)

    snake.move()

    # snake to eat its food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.touch()
        snake.extend()

    # snake collision on walls
    if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() > 270 or snake.head.xcor() < -270:
        game = False
        score_board.game_over()

    # snakes collision with its tail
    for segments in snake.my_turtles:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            game = False
            score_board.game_over()

my_screen.exitonclick()