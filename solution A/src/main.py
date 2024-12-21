  
"""
Author: M.Safari
Date created: 2024/12/18
Descriptions: Rock, Paper, Scissors game.
"""

import random
from typing import List, Tuple

class RockPaperScissors:
    """Main class for Rock Paper Scissors game."""
    def __init__(self, name: str):
        self.choices: List[str] = ['rock', 'paper', 'scissors']
        self.name = name
        self.player_name: str = name

    def get_player_choice(self):
        user_choice = input(f'Enter your choice ({self.choices}): ')
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        
        print(f"Invalid choice. Please try again. You must select from ({self.choices}). ")
        return get_palyer_choice
    # Write another way : while loop 

    def get_computer_choice(self):
        """To get computer choice randomly from choices : Rock , Pape, Scissors """
        return random.choice(self.choices)

    def decide_winner(self, user_choice: str, computer_choice: str) -> str:
        """Descide the winner of the game base on user choices and computer choice.
        Args:
            user_choice (_type_): _description_
            computer_choice (_type_): _description_
        Returns:
            _type_: _description_
        """
        if user_choice == computer_choice:
            return "It's Tie"
        
        win_combination: List[Tuple[str, str]] = [('rock, scissors'), ('paper, rock'), ('scissors, paper')]
        for win_comb in win_combination:
            if (user_choice == win_comb[0]) & (computer_choice == user_choice[1]):
                return "Congragulation! You won!."
        
        return "_oh no! The computer won!."

    def play(self):
        """Play the game
        - Get user choice
        - Get computer choice
        - Decide the winner
        - Print the result
        """
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(f'Computer choice: {computer_choice}')
        print(self.decide_winner(user_choice, computer_choice))


if __name__ == "__main__":
    game = RockPaperScissors('Player')

    while True:
        game.play()

        continue_game = input('Do you want to play again? (Enter any key to play agin, enter q/Q to exit!): ')
        if continue_game.lower() == 'q':
            break
