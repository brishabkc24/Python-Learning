# Quiz App

## What it does

A multiple-choice quiz about Python. The ten questions are stored in `questions.json`. The program asks them in a random order, accepts only `a`, `b`, `c` or `d` as an answer, tells you at once whether you were right, and at the end shows your score and every question you got wrong together with the correct option.

## Concepts used

- Loading structured data with `json.load()`
- `random.shuffle()` on a copy of the list so the original order is untouched
- `zip()` to pair the letters `a` to `d` with the options
- `enumerate()` with `start=1` for numbering
- Functions that return more than one value (`run_quiz` returns the score and the mistakes)
- A list of tuples to remember the mistakes for the final report
- Input validation inside a `while True` loop

## Files

| File | Purpose |
|---|---|
| `quiz.py` | the program |
| `questions.json` | the questions; each has a `question`, four `options` and the `answer` letter |

To add a question, copy one block in `questions.json` and change the text. Keep exactly four options and an answer from `a` to `d`.

## How to run

```
cd 19-projects/quiz-app
python quiz.py
```

## Sample session

The order of the questions changes on every run.

```
Python Quiz: 10 questions. Type the letter of your answer.

Question 1 of 10
Which keyword defines a function in Python?
  a) func
  b) def
  c) function
  d) define
Your answer (a-d): b
Correct!

Question 2 of 10
What is the result of 7 // 2?
  a) 3.5
  b) 3
  c) 4
  d) 1
Your answer (a-d): x
Please type a, b, c or d.
Your answer (a-d): a
Wrong. The correct answer is b) 3

...

========================================
You scored 8 out of 10 (80%).
Good work. Review the questions below.

Questions you got wrong:

- What is the result of 7 // 2?
  Your answer:    a) 3.5
  Correct answer: b) 3

- What does len("Python") return?
  Your answer:    a) 5
  Correct answer: b) 6
```

## Ideas to extend it

- Let the user choose how many questions to answer.
- Add a time limit per question with the `time` module.
- Save the best score to a file and show it at the start.

---

[Back to the project index](../README.md)
