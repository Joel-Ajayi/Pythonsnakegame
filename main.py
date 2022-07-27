import turtle
from turtle import Screen, Turtle
import random
from snake import Snake
from snake_food import SnakeFruit
import time

screen = Screen()
screen.colormode(255)

turtle.setup(width=800, height=800)
turtle.bgcolor((0,0,0))
turtle.tracer(0)
turtle.listen()

snake = Snake(turtle.window_height(), turtle.window_width())

screen.onkey(key="Right", fun=lambda dr=0: snake.change_direction(dr))
screen.onkey(key="Up", fun=lambda dr=90: snake.change_direction(dr))
screen.onkey(key="Left", fun=lambda dr=180: snake.change_direction(dr))
screen.onkey(key="Down", fun=lambda dr=270: snake.change_direction(dr))

while True:
    screen.update()
    snake.move()
    if not snake.game_on:
        break
    time.sleep(0.1)

screen.exitonclick()