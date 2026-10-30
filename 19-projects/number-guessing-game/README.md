# Number Guessing Game

## What it does

The computer picks a secret number between 1 and 100. You type guesses, and after each one the game says "Go higher!" or "Go lower!". It counts your attempts, tells you when you win, remembers your best score and asks whether you want to play again.

## Concepts used

- `random.randint()` to pick the secret number
- `while` loops that run until a condition is met
- Functions with return values (`pick_secret`, `ask_for_guess`, `play_round`, `ask_play_again`)
- Input validation with `try` / `except ValueError` and range checks
- `if` / `elif` / `else` for the higher/lower/correct decision
- Handling `KeyboardInterrupt` and `EOFError` so Ctrl+C ends the game politely

## Files

| File | Purpose |
|---|---|
| `guessing_game.py` | the whole game |

## How to run

```
cd 19-projects/number-guessing-game
python guessing_game.py
```

## Sample session

```
Welcome to the Number Guessing Game!

I am thinking of a number between 1 and 100.
Attempt 1 - your guess (1-100): 50
Go higher!
Attempt 2 - your guess (1-100): abc
Please type a whole number.
Attempt 2 - your guess (1-100): 200
The number is between 1 and 100. Try again.
Attempt 2 - your guess (1-100): 75
Go lower!
Attempt 3 - your guess (1-100): 62
Correct! The number was 62. You needed 3 attempt(s).
That is your best score so far!
Play again? (y/n): n

Thanks for playing! Rounds: 1, best score: 3 attempt(s).
```

## Ideas to extend it

- Let the player choose the range (for example 1 to 1000).
- Limit the number of attempts and show "You lose" when they run out.
- Save the best score to a file so it survives between runs.

---

[Back to the project index](../README.md)
