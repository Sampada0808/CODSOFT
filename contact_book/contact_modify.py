from tkinter import *
from tkinter import messagebox

from contact_list import ContactList

BACKGROUND = "#FFEBB2"
FONT = ("Courier New", 20)


class ContactModify:
    def __init__(self):
        self.add_contact_label = Label(text="Add a Contact:", fg="black", bg=BACKGROUND,
                                       font=("Courier New", 24, "bold"))
        self.add_contact_label.place(x=10, y=80)

        self.name_label = Label(text="Name:", fg="black", bg=BACKGROUND, font=FONT)
        self.name_label.place(x=10, y=120)

        self.phone_number_label = Label(text="Phone No.:", fg="black", bg=BACKGROUND, font=FONT)
        self.phone_number_label.place(x=10, y=180)

        self.email_label = Label(text="Email:", fg="black", bg=BACKGROUND, font=FONT)
        self.email_label.place(x=10, y=240)

        self.address_label = Label(text="Address:", fg="black", bg=BACKGROUND, font=FONT)
        self.address_label.place(x=10, y=300)

        self.name_entry = Entry(width=16, fg="black", bg="white", font=FONT, borderwidth=0)
        self.name_entry.place(x=150, y=120)

        self.phone_number_entry = Entry(width=16, fg="black", bg="white", font=FONT, borderwidth=0)
        self.phone_number_entry.place(x=150, y=180)

        self.email_entry = Entry(width=16, fg="black", bg="white", font=FONT, borderwidth=0)
        self.email_entry.place(x=150, y=240)

        self.address_entry = Entry(width=16, fg="black", bg="white", font=FONT, borderwidth=0)
        self.address_entry.place(x=150, y=300)
        self.contact_list = ContactList()

    def add_contact_detail(self):
        name = self.name_entry.get()
        phone = self.phone_number_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not name:
            messagebox.showerror(message="Please fill in the name")
            return

        if not phone.isdigit():
            messagebox.showerror(message="Please enter a valid phone number")
            return

        if "@" not in email or "." not in email or len(email) < 3:
            messagebox.showerror(message="Please enter a valid email address")
            return

        contact_data = (name, phone, email, address)
        with open("contacts_list.txt", "a") as file:
            for data in contact_data:
                file.write(data + "\t")
            file.write("\n")

        self.contact_list.insert_records(name, phone)

        self.name_entry.delete(0, END)
        self.phone_number_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.address_entry.delete(0, END)

    def search_contacts(self):
        found_contacts = []
        name = self.name_entry.get()
        phone = self.phone_number_entry.get()
        if name == "" and phone == "":
            messagebox.showerror(message="Please Enter Name or Phone Number to Search Contacts")
        else:
            with open("contacts_list.txt") as file:
                for line in file.readlines():
                    data = line.strip().split("\t")
                    if name in data or phone in data:
                        found_contacts.append(data)
                if not found_contacts:
                    return messagebox.showinfo(message="The contact Does not exist")
            if not found_contacts:
                messagebox.showinfo(message="The contact does not exist")
            else:
                contacts = found_contacts[0]
                self.name_entry.delete(0, END)
                self.name_entry.insert(0, contacts[0])
                self.phone_number_entry.delete(0, END)
                self.phone_number_entry.insert(0, contacts[1])
                self.email_entry.delete(0, END)
                self.email_entry.insert(0, contacts[2])
                self.address_entry.delete(0, END)
                self.address_entry.insert(0, contacts[3])

    def delete_contact(self):
        selection = self.contact_list.selection()
        if not selection:
            messagebox.showinfo(message="Please select a contact to delete")
        else:
            selected_indices = set(selection)
            with open("contacts_list.txt", "r") as file:
                lines = file.readlines()
            with open("contacts_list.txt", "w") as file:
                for i, line in enumerate(lines):
                    if i not in selected_indices:
                        file.write(line)
            messagebox.showinfo(message="Selected contacts have been deleted")
            self.contact_list = ContactList()

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_number_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        selection = self.contact_list.selection()
        if not selection:
            messagebox.showinfo(message="Please select a contact to update")
        else:
            selected_index = selection[0]
            with open("contacts_list.txt", "r") as file:
                lines = file.readlines()
            contact_info = lines[selected_index].strip().split("\t")
            self.name_entry.delete(0, END)
            self.name_entry.insert(0, contact_info[0])
            self.phone_number_entry.delete(0, END)
            self.phone_number_entry.insert(0, contact_info[1])
            self.email_entry.delete(0, END)
            self.email_entry.insert(0, contact_info[2])
            self.address_entry.delete(0, END)
            self.address_entry.insert(0, contact_info[3])
            return selected_index

    def save_contact(self, selected_index):
        name = self.name_entry.get()
        phone = self.phone_number_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not all((name, phone, email, address)):
            messagebox.showerror(message="Please fill all contact details")
            return False

        if not phone.isdigit():
            messagebox.showerror(message="Phone number should contain only digits")
            return False

        if "@" not in email and "." not in email and len(email) < 2:
            messagebox.showerror(message="Please enter a valid email address")
            return False

        with open("contacts_list.txt", "r") as file:
            lines = file.readlines()

        lines[selected_index] = f"{name}\t{phone}\t{email}\t{address}\n"

        with open("contacts_list.txt", "w") as file:
            file.writelines(lines)

        self.name_entry.delete(0, END)
        self.phone_number_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.address_entry.delete(0, END)

        self.contact_list.refresh_list()
        return True
