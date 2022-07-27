from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        hight_score = open("hight_score.txt", "r").read()
        hight_score = int(hight_score) if hight_score else 0
        self.score = 0
        self.high_score = hight_score
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setpos(0, 370)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=(20))

    def game_over(self):
        self.clear()
        self.write("Game over", align="center", font=(20))

    def set_score(self):
        self.score += 1
        score = open("hight_score.txt", "w")
        if self.score > self.high_score:
            score.write(f"{self.score}")
            self.high_score = self.score
        self.write_score()

