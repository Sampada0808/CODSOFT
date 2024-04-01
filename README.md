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

# Task 1: Rock Paper Scissors Game

## Overview

This project implements a simple Rock Paper Scissors game using Python and Tkinter for the graphical user interface (GUI).

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

