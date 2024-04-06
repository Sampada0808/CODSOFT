from tkinter import *
import random


class DisplayImage:
    def __init__(self, choice):
        self.user = None
        self.user_canvas = Canvas(width=230, height=230, bg="black", highlightthickness=0)
        self.computer_canvas = Canvas(width=230, height=230, bg="black", highlightthickness=0)
        self.rock_image = PhotoImage(file="Images/rock_hand.png")
        self.paper_image = PhotoImage(file="Images/paper_hand.png")
        self.scissor_image = PhotoImage(file="Images/scissor_hand.png")
        self.list = [self.rock_image, self.paper_image, self.scissor_image]
        self.user_choices(choice)
        self.user_canvas_choice = self.user_canvas.create_image(225, 225, anchor="se", image=self.user)
        self.user_canvas.place(x=40, y=160)
        self.computer_choice = random.choice(self.list)
        self.computer_canvas_choice = self.computer_canvas.create_image(225, 225, anchor="se",
                                                                        image=self.computer_choice)
        self.computer_canvas.place(x=360, y=160)

    def user_choices(self, user_choice):
        if user_choice == "scissor":
            self.user = self.scissor_image
        elif user_choice == "paper":
            self.user = self.paper_image
        else:
            self.user = self.rock_image

    def results(self):
        if ((self.computer_choice == self.scissor_image and self.user == self.paper_image or
             self.computer_choice == self.paper_image and self.user == self.rock_image)
                or self.computer_choice == self.rock_image and self.user == self.scissor_image):
            return "computer"
        elif ((self.user == self.scissor_image and self.computer_choice == self.paper_image or
               self.user == self.paper_image and self.computer_choice == self.rock_image)
              or self.user == self.rock_image and self.computer_choice == self.scissor_image):
            return "user"
        else:
            return "draw"
