import time
from turtle import Turtle
from snake_food import SnakeFruit
from score_board import ScoreBoard

class Snake:
    screen = {"height": 0.0, "width": 0.0}
    def __init__(self, page_height = screen["height"],page_width = screen["height"]):
        self.segments = []
        self.fruit = SnakeFruit()
        self.score_board = ScoreBoard()
        self.direction = 0
        self.game_on = True
        self.added_segment: Turtle = None
        self.add_snake_segment()
        self.screen = {"height": float(page_height), "width": float(page_width)}

    def add_snake_segment(self):
        segments = self.segments;
        new_segment = Turtle("square")
        new_segment.shapesize(0.5, 0.5)
        new_segment.color((255, 255, 255))
        new_segment.pencolor((0, 0, 0))
        last_segment_index = len(self.segments) - 1

        if last_segment_index != -1:
            last_segment: Turtle = segments[last_segment_index]
            heading = int(last_segment.heading())
            x = last_segment.xcor() - 10 if heading == 0 or heading == 180 else last_segment.xcor()
            y = last_segment.ycor() - 10 if heading == 90 or heading == 270 else last_segment.ycor()
            new_segment.setpos((x, y))
            new_segment.setheading(last_segment.heading())
        else:
            new_segment.setpos((0, 0))
        self.added_segment = new_segment

    def eat_fruit(self, segment):
        return int(segment.distance(self.fruit.pos())) == 0

    def onEatFruit(self):
        self.add_snake_segment()
        self.fruit.new_fruit()
        self.score_board.set_score()

    def checkCollision(self):
        first_segment: Turtle = self.segments[0]
        xcor = first_segment.xcor()
        ycor = first_segment.ycor()

        if xcor >= self.screen["width"] / 2 or xcor <= 0 - self.screen["width"] / 2:
            self.game_on = False

        if ycor >= self.screen["height"] / 2 or ycor <= 0 - self.screen["height"] / 2:
            self.game_on = False

        if not self.game_on:
            for segment_index in range(1, len(self.segments)):
                curr_segment: Turtle = self.segments[segment_index]
                if first_segment.pos() == curr_segment.pos():
                    self.game_on = False

    def move(self):
        for segment_index in range(len(self.segments)-1, -1, -1):
            # break game if collision is detected
            if not self.game_on:
                self.score_board.game_over()
                break

            segment: Turtle = self.segments[segment_index]
            segment.setheading(self.direction)
            if segment_index == 0:
                segment.forward(10)
                self.checkCollision()
                if self.eat_fruit(segment):
                    self.onEatFruit()
            else:
                prev_segment: Turtle = self.segments[segment_index - 1]
                segment.setpos(prev_segment.pos())

        if(self.added_segment):
            self.segments.append(self.added_segment)
            self.added_segment = None

    def change_direction(self, direction: int):
        if direction == 0 and self.direction != 180 or direction == 180 and self.direction != 0 or direction == 90 and self.direction != 270 or direction == 270 and self.direction != 90:
            self.direction = direction





