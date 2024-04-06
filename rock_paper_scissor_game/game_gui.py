from tkinter import *
from score_board import ScoreBoard
from display_images import DisplayImage
from tkinter import messagebox


class GameGUI:
    def __init__(self):
        self.rounds_played = 0
        self.display = None
        self.window = Tk("Rock Paper Scissor Game")
        self.window.minsize(600, 600)
        self.window.config(bg="black")
        self.value = ""

        self.score = ScoreBoard()

        self.rock_img = PhotoImage(file="Images/ButtonImages/rock.png")
        self.rock_button = Button(image=self.rock_img, command=self.rock_clicked)
        self.rock_button.place(x=60, y=460)

        self.paper_img = PhotoImage(file="Images/ButtonImages/paper.png")
        self.paper_button = Button(image=self.paper_img, command=self.paper_clicked)
        self.paper_button.place(x=240, y=460)

        self.scissor_img = PhotoImage(file="Images/ButtonImages/scissor.png")
        self.scissor_button = Button(image=self.scissor_img, command=self.scissor_clicked)
        self.scissor_button.place(x=420, y=460)

        self.window.mainloop()

    def scissor_clicked(self):
        self.play_round("scissor")

    def rock_clicked(self):
        self.play_round("rock")

    def paper_clicked(self):
        self.play_round("paper")

    def play_round(self, choice):
        if self.rounds_played < 5:
            self.rounds_played += 1
            self.display = DisplayImage(choice)
            result = self.display.results()
            self.score.update_score(result)
            if self.rounds_played == 5:
                self.display_winner()
                messagebox.showinfo("Game Over", "You've completed 5 rounds!")
                self.ask_play_again()

    def display_winner(self):
        winner = self.score.get_winner()
        if winner == "User" or winner == "Computer":
            messagebox.showinfo("Game Over", f"The winner is {winner}!")
        else:
            messagebox.showinfo("Game Over", "It's a tie!")

    def ask_play_again(self):
        answer = messagebox.askyesno("Play Again?", "Do you want to play another round?")
        if answer:
            self.rounds_played = 0
            self.score.reset_score()
        else:
            self.window.destroy()


if __name__ == "__main__":
    GameGUI()
