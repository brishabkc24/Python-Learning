"""Two threads print even and odd numbers at the same time.

Run: python 02_even_odd.py
Each thread sleeps a little after every number, so the two threads
take turns. The exact order of the lines can differ between runs.
"""

import threading
import time


def print_even(limit):
    for number in range(0, limit + 1, 2):
        print(f"Even: {number}")
        time.sleep(0.1)     # simulate a small amount of work


def print_odd(limit):
    for number in range(1, limit + 1, 2):
        print(f"Odd:  {number}")
        time.sleep(0.1)


even_thread = threading.Thread(target=print_even, args=(10,), name="EvenThread")
odd_thread = threading.Thread(target=print_odd, args=(10,), name="OddThread")

# Start both first, then wait for both. If we joined the first thread
# before starting the second, they would run one after the other.
even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()

print("Both threads finished.")
