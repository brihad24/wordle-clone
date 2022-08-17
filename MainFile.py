from rich.console import Console
from random import choice
from words import word_list
from GameLoop import game

WELCOME_MESSAGE = f'\n[white on blue] Welcome to Wordle! [/]\n'
PLAYER_INSTRUCTIONS = "Try to figure out the chosen word \n You have 6 guesses \n 🟩 - Coorect letter, Correct place \n 🟨 - Correct letter, Wrong place \n ⬜ - Wrong letter \n You may start guessing!\n"
GUESS_STATEMENT = "\nEnter your guess"
ALLOWED_GUESSES = 6

if __name__ == '__main__':
    console = Console()
    chosen_word = choice(word_list)
    console.print(WELCOME_MESSAGE)
    console.print(PLAYER_INSTRUCTIONS)
    game(console, chosen_word)