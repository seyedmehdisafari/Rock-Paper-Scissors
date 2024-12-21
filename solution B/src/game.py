"""
Author: M.Safari
Date created: 2024/12/18
Description: Rock, Paper, Scissors game with GUI.
"""

import random
import tkinter as tk
from tkinter import messagebox
from typing import List, Tuple


class RockPaperScissors:
    """Main class for Rock Paper Scissors game."""
    def __init__(self, name: str):
        self.choices: List[str] = ['rock', 'paper', 'scissors']
        self.player_name: str = name
        self.window = tk.Tk()
        self.window.title("Rock, Paper, Scissors")
        self.create_ui()

    def create_ui(self):
        """Create the graphical user interface (GUI)."""
        tk.Label(self.window, text="Choose your option:", font=("Arial", 16)).pack(pady=10)
        
        # Create buttons for Rock, Paper, and Scissors
        for choice in self.choices:
            btn = tk.Button(self.window, text=choice.capitalize(), 
                            font=("Arial", 14), 
                            width=10, 
                            command=lambda choice=choice: self.play(choice))
            btn.pack(pady=5)

        # Exit button
        exit_button = tk.Button(self.window, text="Exit", font=("Arial", 12), command=self.window.quit)
        exit_button.pack(pady=10)

    def get_computer_choice(self) -> str:
        """Randomly select a choice for the computer."""
        return random.choice(self.choices)

    def decide_winner(self, user_choice: str, computer_choice: str) -> str:
        """Determine the winner of the game based on player and computer choices."""
        if user_choice == computer_choice:
            return "It's a tie!"
        
        win_combinations: List[Tuple[str, str]] = [('rock', 'scissors'), 
                                                   ('paper', 'rock'), 
                                                   ('scissors', 'paper')]
        
        if (user_choice, computer_choice) in win_combinations:
            return "Congratulations! You won!"
        
        return "Oh no! The computer won!"

    def play(self, user_choice: str):
        """Play a single round of the game."""
        computer_choice = self.get_computer_choice()
        
        result = self.decide_winner(user_choice, computer_choice)
        
        message = (f"Your choice: {user_choice.capitalize()}\n"
                   f"Computer's choice: {computer_choice.capitalize()}\n\n"
                   f"{result}")
        
        # Show result in a message box
        messagebox.showinfo("Game Result", message)

    def run(self):
        """Run the GUI application."""
        self.window.mainloop()


if __name__ == "__main__":
    game = RockPaperScissors('Player')
    game.run()