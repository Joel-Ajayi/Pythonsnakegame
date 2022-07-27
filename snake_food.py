from turtle import Turtle
import random

class SnakeFruit(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color((255, 255, 255))
        self.penup()
        self.shapesize(0.5, 0.5)
        self.setpos(20, 0)

    def new_fruit(self):
        y_pos = random.randrange(-390, 360, 10)
        x_pos = random.randrange(-390, 390, 10)
        self.setpos(x_pos, y_pos)
