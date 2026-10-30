# Calculator (Tkinter)

## What it does

A desktop calculator with a display, a grey history line and a grid of buttons. It computes one operation at a time, for example `12+3`, `7/2` or `6*7`, and shows the answer in the display with the sum above it. Division by zero or an incomplete sum opens an error dialog instead of crashing. The keyboard works as well: digits, `+ - * /`, Enter for `=`, Backspace to delete one character and Escape to clear.

## Concepts used

- A class that inherits from `tk.Tk`, so the window and its data live together
- `grid()` with `columnspan` and `rowspan` for the double-width `0` key and the tall `=` key
- Buttons created in a loop with `lambda k=key: self.press(k)`
- `StringVar` for the display and the history line
- `bind()` for keyboard shortcuts
- The `operator` module as a dictionary of arithmetic functions
- `try` / `except ZeroDivisionError` and `except ValueError` with `messagebox.showerror`

## Files

| File | Purpose |
|---|---|
| `calculator.py` | the whole program |

## How to run

```
cd 19-projects/calculator-gui
python calculator.py
```

## Sample session

There is no text output; this is what happens in the window.

1. Click `7`, `/`, `2`, `=`. The display shows `3.5` and the grey line above it shows `7/2 =`.
2. Click `5`, `/`, `0`, `=`. A dialog says "Cannot divide by zero." and the display is cleared.
3. Type `12+3` on the keyboard and press Enter. The display shows `15`.
4. Type `123`, press Backspace twice, then `+5` and Enter. The display shows `6`.
5. Press Escape. The display and the history line are emptied.

## Ideas to extend it

- Support a chain of operations such as `1+2*3` by evaluating step by step.
- Add a `%` key and a square-root key.
- Keep a scrollable list of all past calculations.

---

[Back to the project index](../README.md)
