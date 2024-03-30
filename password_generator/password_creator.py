import string
import random

SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class PasswordCreator:
    def __init__(self, length, complexity):
        self.password_list = []
        self.password_length = length
        self.password_complexity = complexity.lower()
        self.password = ""
        if self.password_complexity == "low":
            self.list_characters = [string.ascii_letters]
        elif self.password_complexity == "medium":
            self.list_characters = [string.ascii_letters, string.digits]
        else:
            self.list_characters = [string.ascii_letters, string.digits, SYMBOLS]

    def create_password(self):
        for _ in range(self.password_length):
            word = random.choice(self.list_characters)
            self.password_list += [char for char in random.choice(random.choice(word))]
        self.password = "".join(self.password_list)
        return self.password
