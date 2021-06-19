from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data") as data:
            self.high_score=int(data.read())

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score {self.high_score}", align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0   #THIS one is to reset the score
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over" ,align="center", font=("Arial", 20, "normal"))
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

