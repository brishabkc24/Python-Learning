"""
Demonstrates the else and finally blocks: else runs only when no error
happened, and finally runs every time, which makes it the right place to
close files and connections.
Run: python 03_else_and_finally.py
Reads datasets/numbers.txt and then tries a file that does not exist.
"""

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "datasets"


def sum_file(filename):
    print(f"Opening {filename}")
    file = None
    try:
        file = open(DATA_DIR / filename, encoding="utf-8")
        total = sum(int(line) for line in file)
    except FileNotFoundError:
        print("  except: file not found")
    except ValueError:
        print("  except: the file contains something that is not a number")
    else:
        print("  else: total is", total)       # only when everything worked
    finally:
        if file is not None:
            file.close()
        print("  finally: file closed")


sum_file("numbers.txt")
sum_file("missing.txt")

# The complete flow in one small example without files.
for divisor in [4, 0]:
    try:
        print(f"Trying 20 / {divisor}")
        result = 20 / divisor
    except ZeroDivisionError:
        print("  except: division by zero")
    else:
        print("  else: result is", result)
    finally:
        print("  finally: done with", divisor)
