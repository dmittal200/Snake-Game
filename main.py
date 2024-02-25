from turtle import Turtle, Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0) #To stop the animation

game_on = True

snake = Snake()
food = Food()
Score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while game_on:
    screen.update() #To update screen after every change
    sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) <13:
        food.refresh()
        snake.extend()
        Score.increase_score()

    # detect collision with walls
    if snake.head.xcor()>240 or snake.head.xcor()<-240 or snake.head.ycor()>220 or snake.head.ycor()<-240:
        game_on = False
        Score.game_over()

    #detect collision with body
    for segmnt in snake.segment:
        if segmnt==snake.head:
            pass
        elif snake.head.distance(segmnt)<10:
            game_on = False
            Score.game_over()

screen.exitonclick()
