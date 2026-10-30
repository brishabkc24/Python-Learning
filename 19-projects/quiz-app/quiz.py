"""
Quiz App
========
A multiple-choice Python quiz. The questions live in questions.json in
this folder. They are asked in a random order, the score is counted, and
at the end every wrong answer is shown together with the correct option.

Run: python quiz.py

Sample session:
    Question 1 of 10
    Which keyword defines a function in Python?
      a) func
      b) def
      c) function
      d) define
    Your answer (a-d): b
    Correct!
"""

import json
import random
from pathlib import Path

QUESTIONS_FILE = Path(__file__).resolve().parent / "questions.json"
LETTERS = "abcd"


def load_questions():
    """Read the question list from the JSON file next to this script."""
    with open(QUESTIONS_FILE, encoding="utf-8") as file:
        return json.load(file)


def ask_question(number, total, question):
    """Show one question and return the letter the user chose."""
    print(f"\nQuestion {number} of {total}")
    print(question["question"])
    for letter, option in zip(LETTERS, question["options"]):
        print(f"  {letter}) {option}")

    while True:
        answer = input("Your answer (a-d): ").strip().lower()
        if answer in LETTERS:
            return answer
        print("Please type a, b, c or d.")


def option_text(question, letter):
    """Return the text of an option, for example 'b) def'."""
    return f"{letter}) {question['options'][LETTERS.index(letter)]}"


def run_quiz(questions):
    """Ask every question in random order. Return the score and the mistakes."""
    order = questions[:]              # copy so the original list is untouched
    random.shuffle(order)

    score = 0
    mistakes = []                     # (question, chosen letter) pairs
    for number, question in enumerate(order, start=1):
        chosen = ask_question(number, len(order), question)
        if chosen == question["answer"]:
            score += 1
            print("Correct!")
        else:
            print(f"Wrong. The correct answer is {option_text(question, question['answer'])}")
            mistakes.append((question, chosen))
    return score, mistakes


def show_results(score, total, mistakes):
    percent = score / total * 100
    print("\n" + "=" * 40)
    print(f"You scored {score} out of {total} ({percent:.0f}%).")
    if percent == 100:
        print("Perfect! Well done.")
    elif percent >= 70:
        print("Good work. Review the questions below.")
    else:
        print("Keep practising. Review the questions below.")

    if mistakes:
        print("\nQuestions you got wrong:")
        for question, chosen in mistakes:
            print(f"\n- {question['question']}")
            print(f"  Your answer:    {option_text(question, chosen)}")
            print(f"  Correct answer: {option_text(question, question['answer'])}")


def main():
    questions = load_questions()
    print(f"Python Quiz: {len(questions)} questions. Type the letter of your answer.")
    score, mistakes = run_quiz(questions)
    show_results(score, len(questions), mistakes)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nQuiz stopped. Goodbye!")
