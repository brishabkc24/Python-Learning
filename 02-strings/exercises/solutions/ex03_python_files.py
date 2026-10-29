"""Report whether each file name in a list is a Python file."""

file_names = ["notes.txt", "main.py", "data.csv", "test_app.py"]

for name in file_names:
    if name.endswith(".py"):
        print(f"{name}: Python file")
    else:
        print(f"{name}: not a Python file")
