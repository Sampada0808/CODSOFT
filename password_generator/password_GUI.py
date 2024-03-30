from tkinter import *
from tkinter import messagebox
from password_creator import PasswordCreator


class PasswordGUI:
    def __init__(self):
        self.password = ""
        self.window = Tk()
        self.window.minsize(500, 400)
        self.window.title("Password Generator")
        self.window.config(bg="white")
        self.title = Label(text="Password Generator", fg="black", bg="white", font=("Arial", 30, "bold"), pady=20,
                           padx=20)
        self.title.grid(row=0, column=0, columnspan=2, padx=120)

        self.canvas = Canvas(width=400, height=100, bg="white", highlightthickness=0)
        self.bg = PhotoImage(file="password_img.png")
        self.canvas.create_image(367, 83, anchor="se", image=self.bg)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=120)

        self.password_length = Label(text="Length:", font=("Arial", 20), fg="black", bg="white")
        self.password_length.grid(row=2, column=0, pady=10)

        self.password_length_entry = Entry(bg="white", fg="grey", width=34)
        self.password_length_entry.insert(0, "Enter Password length")
        self.password_length_entry.grid(row=2, column=1, pady=10)

        self.password_complexity = Label(text="Complexity:", font=("Arial", 20), fg="black", bg="white")
        self.password_complexity.grid(row=3, column=0, pady=10)

        self.password_complexity_entry = Entry(bg="white", fg="grey", width=34)
        self.password_complexity_entry.insert(0, "Enter Password Complexity (Low/Medium/High)")
        self.password_complexity_entry.grid(row=3, column=1, pady=10)

        self.submit_button = Button(text="Submit", width=20, bg="white", fg="black", highlightbackground="black",
                                    command=self.check_data)
        self.submit_button.grid(row=4, column=0, pady=10, columnspan=2)

        self.password_generated_label = Label(text="Password Generated:", font=("Arial", 20), fg="black", bg="white")
        self.password_generated_label.grid(row=5, column=0, pady=10)

        self.password_generated = Label(text="", font=("Arial", 20), fg="black", bg="white")
        self.password_generated.grid(row=5, column=1, pady=10)

        self.window.mainloop()

    def check_data(self):
        if self.password_length_entry.get() == "" and self.password_complexity_entry.get() == "":
            messagebox.showwarning("Empty Fields", message="Please fill the fields")
        else:
            try:
                password_length = int(self.password_length_entry.get())
                if not self.password_complexity_entry.get().isdigit():
                    password_complexity = str(self.password_complexity_entry.get())
                else:
                    raise ValueError
            except ValueError:
                messagebox.showwarning("Invalid data", message="Please fill Correct data")
            else:
                password_creator = PasswordCreator(password_length, password_complexity)
                self.password = password_creator.create_password()
                self.password_generated.config(text=self.password)
