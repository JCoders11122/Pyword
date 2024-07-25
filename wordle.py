import os
import random
from colorama import Fore, Style, init

# Initialize colorama
init()

# ANSI escape codes for colors
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
GRAY = Fore.BLACK
RESET = Style.RESET_ALL

def load_words(file_path):
    """Load words from a file, filtering to ensure they are 5 letters long."""
    absolute_path = os.path.abspath(file_path)
    print("Attempting to open file at:", absolute_path)
    
    try:
        with open(file_path, 'r') as file:
            words = [line.strip().upper() for line in file if len(line.strip()) == 5]
        
        if not words:
            print("No valid 5-letter words found in the file.")
        else:
            print(f"Loaded {len(words)} words.")
        
        return words

    except IOError as e:
        print("Error opening file:", e)
        return []

def display_word(secret_word, correct_guesses):
    """Display the current state of the word with 'X' for hidden letters and revealed letters."""
    displayed_word = ''.join([letter if letter in correct_guesses else 'X' for letter in secret_word])
    print("Word: " + displayed_word)

def provide_feedback(secret_word, guess):
    """Provide feedback on the guess with colors."""
    feedback = ['_'] * 5
    feedback_colors = [GRAY] * 5

    # Check for exact matches (green)
    for i in range(5):
        if guess[i] == secret_word[i]:
            feedback[i] = guess[i]
            feedback_colors[i] = GREEN

    # Check for incorrect positions but correct letters (yellow)
    for i in range(5):
        if guess[i] != secret_word[i] and guess[i] in secret_word:
            if feedback[i] != GREEN:  # Avoid overwriting green
                feedback[i] = guess[i]
                feedback_colors[i] = YELLOW

    # Print feedback with colors
    colored_feedback = ''.join(f"{feedback_colors[i]}{feedback[i]}{RESET}" for i in range(5))
    print("Feedback: " + colored_feedback)

def get_guess():
    """Get a guess from the user."""
    while True:
        guess = input("Enter your guess (a 5-letter word): ").strip().upper()
        if len(guess) == 5 and guess.isalpha():
            return guess
        else:
            print("Invalid guess. Please enter a 5-letter word.")

def wordle_game():
    # Specify the path to the file
    file_path = r'C:\Users\Jamie\Documents\Coded Games\words.txt'
    
    # Load words from the file
    words = load_words(file_path)
    if not words:
        print("No valid words found in the word list. Make sure your words.txt file contains valid 5-letter words.")
        return

    # Choose a random word from the list
    secret_word = random.choice(words)
    correct_guesses = set()
    attempts = 6  # Total attempts allowed

    print("Welcome to Wordle!")
    
    while attempts > 0:
        display_word(secret_word, correct_guesses)
        
        guess = get_guess()
        
        if guess == secret_word:
            print(f"Congratulations! You've guessed the word: {secret_word}")
            break
        
        provide_feedback(secret_word, guess)
        correct_guesses.update([letter for letter in guess if letter in secret_word])
        attempts -= 1

        if attempts == 0:
            print(f"Sorry, you've run out of attempts. The word was: {secret_word}")

    # Prompt the user to press Enter before closing
    input("Press Enter to exit...")

if __name__ == "__main__":
    wordle_game()


