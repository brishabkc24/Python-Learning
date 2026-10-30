"""
Number Guessing Game
====================
The computer picks a secret number from 1 to 100. You guess until you
find it. After every wrong guess the game says "higher" or "lower" and
counts your attempts. When you win you can play again.

Run: python guessing_game.py

Sample session:
    Attempt 1 - your guess (1-100): 50
    Go higher!
    Attempt 2 - your guess (1-100): abc
    Please type a whole number.
    Attempt 2 - your guess (1-100): 75
    Go lower!
    ...
    Correct! The number was 62. You needed 5 attempt(s).
    Play again? (y/n): n
"""

import random

LOWEST = 1
HIGHEST = 100


def pick_secret():
    """Return a random whole number between LOWEST and HIGHEST (both included)."""
    return random.randint(LOWEST, HIGHEST)


def ask_for_guess(attempt_number):
    """Keep asking until the player types a whole number inside the range."""
    while True:
        answer = input(f"Attempt {attempt_number} - your guess ({LOWEST}-{HIGHEST}): ").strip()
        try:
            guess = int(answer)
        except ValueError:
            print("Please type a whole number.")
            continue
        if guess < LOWEST or guess > HIGHEST:
            print(f"The number is between {LOWEST} and {HIGHEST}. Try again.")
            continue
        return guess


def play_round():
    """Play one full round and return how many attempts it took."""
    secret = pick_secret()
    attempts = 0
    print(f"\nI am thinking of a number between {LOWEST} and {HIGHEST}.")

    while True:
        attempts += 1
        guess = ask_for_guess(attempts)
        if guess < secret:
            print("Go higher!")
        elif guess > secret:
            print("Go lower!")
        else:
            print(f"Correct! The number was {secret}. You needed {attempts} attempt(s).")
            return attempts


def ask_play_again():
    """Return True if the player wants another round."""
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer y or n.")


def main():
    print("Welcome to the Number Guessing Game!")
    rounds_played = 0
    best_score = None       # fewest attempts so far

    while True:
        attempts = play_round()
        rounds_played += 1
        if best_score is None or attempts < best_score:
            best_score = attempts
            print("That is your best score so far!")
        if not ask_play_again():
            break

    print(f"\nThanks for playing! Rounds: {rounds_played}, best score: {best_score} attempt(s).")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C or the end of piped input ends the game politely.
        print("\nGoodbye!")
