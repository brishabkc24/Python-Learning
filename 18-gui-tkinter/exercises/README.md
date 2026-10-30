# Exercises: GUI with Tkinter

Solve each exercise in its own file. The solutions are in the `solutions/` folder; try on your own before you look. Every window must open with `tk.Tk()` and stay open with `mainloop()`.

## 1. Click counter

**Task:** Create a window with a label that says `Clicks: 0` and a button labelled `Click`. Each click on the button increases the number by one.

Example: after three clicks the label reads `Clicks: 3`.

## 2. Colour buttons

**Task:** Show a wide label with the text `Pick a colour` and three buttons: `Red`, `Green` and `Blue`. Clicking a button changes the background colour of the label to that colour. Create the three buttons in a loop.

Example: clicking `Green` turns the label green; clicking `Red` turns it red.

## 3. Temperature converter

**Task:** Make an `Entry` for a temperature in Celsius, a `Convert` button and a result label. Clicking the button shows the temperature in Fahrenheit (`F = C * 9 / 5 + 32`), rounded to one decimal. If the box does not contain a number, show `Please enter a number` in red instead.

Example:

```
Celsius: 25      ->  77.0 F
Celsius: abc     ->  Please enter a number   (in red)
```

## 4. Key and mouse watcher

**Task:** Create a window with a coloured box (a `Label` with a background colour) and two labels under it. Pressing any key updates the first label to `Last key: <name>`. Clicking inside the box with the left mouse button updates the second label to `Clicked at: <x>, <y>`.

Example: pressing the space bar shows `Last key: space`; clicking near the top left of the box shows `Clicked at: 14, 9`.

## 5. Feedback form

**Task:** Build a form with a name `Entry`, a `Scale` from 1 to 5 for a rating, two `Radiobutton` widgets (`Yes` / `No`) under the question "Would you recommend us?", a `Checkbutton` "Contact me", and a `Submit` button. Submit shows all the answers in a `messagebox.showinfo` dialog. If the name is empty, show a `messagebox.showerror` instead.

Example dialog text:

```
Name: Asha
Rating: 4 out of 5
Recommend: Yes
Contact me: no
```

## 6. Shopping list

**Task:** Build a shopping list with an `Entry`, an `Add` button, a `Listbox`, a `Remove selected` button and a label that always shows how many items are in the list. The Enter key must add an item too. Ignore empty input. Removing with nothing selected shows a warning dialog.

Example: after adding `milk`, `bread` and `eggs` and removing `bread`, the list shows `milk` and `eggs` and the label reads `2 item(s)`.

## 7. Text tools

**Task:** Place a `Text` widget with three buttons under it: `Uppercase`, `Lowercase` and `Clear`. The first two replace the text in the box with its uppercase or lowercase version. `Clear` empties the box. A label under the buttons always shows `Characters: <n>` and must update after every button click.

Example: with `Hello World` in the box, `Uppercase` changes it to `HELLO WORLD` and the label reads `Characters: 11`.

---

[Back to the lesson](../README.md)
