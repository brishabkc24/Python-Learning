# Exercises: Strings

Write each solution in its own `.py` file and run it with `python filename.py`. Solutions are in the `solutions/` folder; try on your own first.

## 1. First and last

**Task:** Store the word `programming` in a variable. Print its length, its first three characters and its last three characters using slicing.

**Example**

```
Length: 11
First three: pro
Last three: ing
```

## 2. Count a letter

**Task:** Count how many times the letter `s` appears in the sentence `Sally sells sea shells by the sea shore`. Capital and small letters both count.

**Example**

```
The letter s appears 8 times.
```

## 3. Python files

**Task:** Start with the list `["notes.txt", "main.py", "data.csv", "test_app.py"]`. For each name, print whether it is a Python file by checking its ending.

**Example**

```
notes.txt: not a Python file
main.py: Python file
data.csv: not a Python file
test_app.py: Python file
```

## 4. Reverse each word

**Task:** Reverse the letters of every word in `Python is fun` but keep the words in the same order.

**Example**

```
nohtyP si nuf
```

## 5. Upper and lower count

**Task:** Count the upper-case letters and the lower-case letters in `Hello World From Python`. Spaces do not count. Use the methods `isupper()` and `islower()`, which work like `isdigit()`.

**Example**

```
Upper case: 4
Lower case: 16
```

## 6. Palindrome phrase

**Task:** Ask the user for a phrase and report whether it is a palindrome. Ignore capitals and spaces.

**Example**

```
Enter a phrase: Was it a car or a cat I saw
Palindrome: True
```

## 7. Text statistics

**Task:** Read `datasets/sample_text.txt` with `Path(...).read_text()` as shown in the examples. Print the number of lines, the number of words and the number of characters, then the longest word in the file.

**Example**

```
Lines: 5
Words: 68
Characters: 408
Longest word: intelligence
```
