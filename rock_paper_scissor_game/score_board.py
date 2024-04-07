from tkinter import *


class ScoreBoard:
    def __init__(self):
        self.user_score_value = 0
        self.computer_score_value = 0
        self.canvas = Canvas(width=600, height=460, bg="black", highlightthickness=0)
        self.canvas.create_line(300, 50, 300, 440, dash=(10, 12), fill="white")
        self.canvas.place(x=0, y=0)
        self.score_label = Label(text="Score", fg="white", bg="black", font=("Courier", 40, "normal"))
        self.score_label.place(x=240, y=10)

        self.user_score_label = Label(text="User:", fg="white", bg="black", font=("Courier", 40, "normal"))
        self.user_score_label.place(x=100, y=60)

        self.user_score = Label(text=self.user_score_value, fg="white", bg="black", font=("Courier", 40, "normal"))
        self.user_score.place(x=220, y=60)

        self.computer_score = Label(text=self.computer_score_value, fg="white", bg="black",
                                    font=("Courier", 40, "normal"))
        self.computer_score.place(x=540, y=60)

        self.computer_score_label = Label(text="Computer:", fg="white", bg="black", font=("Courier", 40, "normal"))
        self.computer_score_label.place(x=320, y=60)

    def update_score(self, result):
        if result == "computer":
            self.computer_score_value += 1
        elif result == "user":
            self.user_score_value += 1

        self.computer_score.config(text=self.computer_score_value)
        self.user_score.config(text=self.user_score_value)

    def get_winner(self):
        if self.user_score_value < self.computer_score_value:
            return "Computer"
        elif self.user_score_value > self.computer_score_value:
            return "User"
        else:
            return "Draw"

    def reset_score(self):
        self.user_score_value = 0
        self.computer_score_value = 0
        self.computer_score.config(text=self.computer_score_value)
        self.user_score.config(text=self.user_score_value)
