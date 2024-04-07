# CODSOFT
Python Programming Internship Project by CodSoft

# Task 1: Password Generator

## Project Overview

**Problem Statement**: 
Design a user-friendly password generator application using Python.

### Requirements
- Python
- Tkinter (for GUI)

## Project Description

The Password Generator project is a Python application aimed at generating secure and customizable passwords for users. It utilizes Tkinter, a GUI library in Python, to provide an intuitive user interface for generating passwords with various complexities.

## Features

1. **Graphical User Interface (GUI)**:
   - The project includes a graphical user interface built using Tkinter, providing users with an easy-to-use interface to generate passwords.

2. **Password Complexity Options**:
   - Users can select the complexity of the generated password, choosing from options such as low, medium, and high.

3. **Customizable Password Length**:
   - Users can specify the length of the generated password according to their requirements.

4. **Object-Oriented Design**:
   - The project follows the principles of Object-Oriented Programming (OOP), with separate classes for password generation and GUI functionality.

## Project Structure

- **`main.py`**: 
  - Entry point of the application where the GUI is instantiated and run.

- **`password_creator.py`**: 
  - Contains the `PasswordCreator` class responsible for generating passwords based on user-defined complexity and length.

- **`password_GUI.py`**: 
  - Defines the `PasswordGUI` class, which implements the graphical user interface using Tkinter.

- **`README.md`**: 
  - Documentation file providing an overview of the project, its features, and usage instructions.

## Future Enhancements

- Implement password strength indicator.
- Add option for saving generated passwords to a file.
- Improve GUI design for better user experience.
  

# Task 2: Rock Paper Scissors Game

## Overview

This project implements a simple Rock Paper Scissors game using Python and Tkinter for the graphical user interface (GUI).

### Requirements
- Python
- Tkinter (for GUI)


### Features

- Graphical user interface built with Tkinter.
- Players can choose between Rock, Paper, or Scissors.
- The computer opponent selects its move randomly.
- Scoreboard to keep track of the user and computer scores.
- Game ends after a fixed number of rounds (default: 5).

## Project Structure

- **`main.py`**: Entry point of the application, contains the `GameGUI` class to handle game logic and GUI interactions.
- **`score_board.py`**: Defines the `ScoreBoard` class to manage and display the game scores.
- **`display_images.py`**: Implements the `DisplayImage` class to display the user and computer choices in the GUI.
- **`Images/`**: Directory containing image assets used in the game.

## Future Improvements

- Implement more sophisticated AI for the computer opponent.
- Enhance GUI design for better user experience.
- Allow customization of the number of rounds.

# Task 3: Contact Book

## Project Overview

**Problem Statement**: 
Design a contact book application using Python and Tkinter to manage contact details efficiently.

### Requirements
- Python
- Tkinter (for GUI)

## Project Description

The Contact Book project is a Python application aimed at providing users with a platform to manage their contact details effectively. It utilizes Tkinter, a GUI library in Python, to offer a user-friendly interface for adding, editing, searching, and deleting contacts.

## Features

1. **Graphical User Interface (GUI)**:
   - The project includes a graphical user interface built using Tkinter, providing users with an intuitive platform to manage their contacts.

2. **Add Contacts**:
   - Users can add new contacts by entering details such as name, phone number, email, and address.

3. **Edit Contacts**:
   - Existing contacts can be edited to update their details, such as name, phone number, email, and address.

4. **Search Contacts**:
   - Users can search for contacts by name or phone number, making it easier to find specific contacts in the list.

5. **Delete Contacts**:
   - Contacts can be deleted from the list, allowing users to remove unwanted or outdated contacts.

6. **Listbox Display**:
   - The project includes a listbox to display the saved contacts, providing users with a clear overview of their contact list.

7. **Data Persistence**:
   - Contact details are saved to a text file (`contacts_list.txt`), ensuring that users' contact information is retained even after closing the application.

## Project Structure

- **`contact_GUI.py`**: 
  - Contains the `ContactGUI` class, which implements the graphical user interface using Tkinter.

- **`contact_modify.py`**: 
  - Defines the `ContactModify` class, responsible for adding, editing, searching, and deleting contacts.

- **`contact_list.py`**: 
  - Implements the `ContactList` class, which manages the listbox display of contacts and maintains the contact records.

- **`contacts_list.txt`**: 
  - Text file to store contact details.

## Future Enhancements

- Implement sorting functionality for the contact list.
- Add validation for email addresses to ensure they are in the correct format.
- Improve error handling to provide more informative error messages to users.
- Enhance the GUI design for better aesthetics and user experience.


