from tkinter import *

BACKGROUND = "#FFEBB2"


class ContactList:
    def __init__(self):
        self.contact_list_label = Label(text="Contact List", fg="black", bg=BACKGROUND,
                                        font=("Courier New", 24, "bold"))
        self.contact_list_label.place(x=390, y=80)

        self.contact_list_box = Listbox(width=18, fg="black", bg="white", font=("Courier New", 20))
        self.contact_list_box.place(x=380, y=120)
        self.refresh_list()

    def insert_records(self, name, phone):
        contact_info = f"{name}: {phone}"
        self.contact_list_box.insert(END, contact_info)

    def refresh_list(self):
        self.contact_list_box.delete(0, END)
        try:
            with open("contacts_list.txt") as file:
                for line in file.readlines():
                    contact_data = [item.strip() for item in line.strip().split("\t")]
                    self.insert_records(contact_data[0], contact_data[1])
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred:", e)

    def selection(self):
        selection = self.contact_list_box.curselection()
        return selection
