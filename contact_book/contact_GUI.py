from tkinter import *
from contact_modify import ContactModify

BACKGROUND = "#FFEBB2"


class ContactGUI:

    def __init__(self):
        self.selected = None
        self.window = Tk()
        self.window.minsize(620, 480)
        self.window.title("Contact Book")
        self.window.config(bg=BACKGROUND)

        self.title_label = Label(text="Contact Book", fg="black", bg=BACKGROUND, font=("Courier New", 30, "bold"))
        self.title_label.place(x=200, y=20)

        self.add_contact = ContactModify()

        self.add_button = Button(width=8, text="Add", highlightthickness=0, font=("Courier New", 18),
                                 command=self.add_contact.add_contact_detail)
        self.add_button.place(x=20, y=400)

        self.search_button = Button(width=8, text="Search", highlightthickness=0, font=("Courier New", 18)
                                    , command=self.add_contact.search_contacts)
        self.search_button.place(x=160, y=400)

        self.edit_button = Button(width=8, text="Edit", highlightthickness=0, font=("Courier New", 18),
                                  command=self.hide_edit_button)
        self.edit_button.place(x=310, y=400)

        self.delete_button = Button(width=8, text="Delete", highlightthickness=0, font=("Courier New", 18),
                                    command=self.add_contact.delete_contact)
        self.delete_button.place(x=460, y=400)

        self.window.mainloop()

    def hide_edit_button(self):
        self.edit_button.place_forget()
        self.selected = self.add_contact.update_contact()
        self.edit_button = Button(width=8, text="Save", highlightthickness=0, font=("Courier New", 18),
                                  command=self.reveal_edit_button)
        self.edit_button.place(x=310, y=400)

    def reveal_edit_button(self):
        result = self.add_contact.save_contact(self.selected)
        if result:
            self.edit_button = Button(width=8, text="Edit", highlightthickness=0, font=("Courier New", 18),
                                      command=self.hide_edit_button)
            self.edit_button.place(x=310, y=400)
        else:
            self.edit_button = Button(width=8, text="Save", highlightthickness=0, font=("Courier New", 18),
                                      command=self.reveal_edit_button)
            self.edit_button.place(x=310, y=400)


if __name__ == "__main__":
    ContactGUI()
