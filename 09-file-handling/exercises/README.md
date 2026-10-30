# Exercises: File Handling

Solve each exercise in a new file. Compare with the files in [solutions/](solutions/) only after you have tried. Files that your program creates should be written next to the program with a clear name such as `output_fruits.txt`.

Scripts in the `solutions/` folder find the datasets with `Path(__file__).resolve().parents[3] / "datasets"` because they sit three folders below the repository root.

## 1. Write and read back

**Fruit list.** Write the words `apple`, `banana` and `cherry` to a file called `output_fruits.txt`, one per line. Then open the file again, read it line by line and print each line with its line number.

Example:

```
1. apple
2. banana
3. cherry
```

## 2. Longest line

**Line lengths.** Read `datasets/sample_text.txt`, count the lines, and print the longest line together with its length in characters.

Example:

```
Lines: 5
Longest line (104 characters):
Python is a popular programming language. It was created by Guido van Rossum and first released in 1991.
```

## 3. Number statistics

**Numbers report.** Read `datasets/numbers.txt`, which has one integer per line. Print how many numbers there are, their sum, their average rounded to two decimals, the smallest and the largest.

Example:

```
Count   : 20
Sum     : 759
Average : 37.95
Smallest: 2
Largest : 99
```

## 4. Append to a log

**Visit counter.** Each time the program runs it should add one line `Visit N` to `output_visits.txt`, where `N` is one more than the number of lines already in the file. Print the total number of visits recorded. Running the program three times gives a file with three lines. Use mode `a` and handle the case where the file does not exist yet.

Example (first run, then second run):

```
Recorded Visit 1. Total visits: 1
Recorded Visit 2. Total visits: 2
```

## 5. Top students CSV

**Filter and save.** Read `datasets/students.csv` with `csv.DictReader`. Keep the students with marks of 80 or more, sort them by marks from highest to lowest, and write them to `output_top_students.csv` with `csv.DictWriter` using the columns `name`, `city` and `marks`. Print each saved row.

Example:

```
Kiran Adhikari,Bhaktapur,95
Sita Rai,Pokhara,92
Anjali Shrestha,Kathmandu,88
Aarav Sharma,Kathmandu,85
Saved 4 students to output_top_students.csv
```

## 6. Department salaries JSON

**Average per department.** Read `datasets/employees.json`. Work out the average salary of each department, rounded to two decimals. Save the result as a dictionary in `output_department_salaries.json` using `indent=2`, then print the file content.

Example:

```
{
  "Engineering": 84666.67,
  "Marketing": 64000.0,
  "Finance": 71500.0,
  "Human Resources": 58000.0
}
```

## 7. Word frequency

**Most common words.** Count how often each word appears in `datasets/sample_text.txt`. Ignore case and ignore punctuation such as commas and full stops. Print the five most common words with their counts using `collections.Counter`.

Example:

```
python: 4
and: 4
is: 3
it: 3
a: 2
```

## 8. Marks report

**Report file.** Read `datasets/marks.txt`, where each line is `name maths science english`. Write `output_marks_report.txt` with one line per student showing the name, the total and the average (two decimals), and a final line naming the student with the highest average. Then print the content of the report file.

Example:

```
Aarav    total 253  average 84.33
Sita     total 275  average 91.67
...
Topper: Sita with 91.67
```
