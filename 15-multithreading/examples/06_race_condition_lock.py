"""A shared counter updated by two threads, without and then with a Lock.

Run: python 06_race_condition_lock.py
Each thread adds 1 to the counter 10,000 times, so the right answer is
20,000. Without a lock, updates get lost and the printed result changes
from run to run. With a lock the result is always 20,000.
"""

import threading
import time

counter = 0
lock = threading.Lock()


def unsafe_increment(times):
    global counter
    for _ in range(times):
        current = counter       # 1. read the shared value
        time.sleep(0)           # 2. let another thread run (this can happen anyway)
        counter = current + 1   # 3. write it back; another update may be lost


def safe_increment(times):
    global counter
    for _ in range(times):
        # Only one thread at a time can be inside this block.
        with lock:
            current = counter
            time.sleep(0)
            counter = current + 1


def run_test(label, function):
    global counter
    counter = 0
    first = threading.Thread(target=function, args=(10_000,))
    second = threading.Thread(target=function, args=(10_000,))
    first.start()
    second.start()
    first.join()
    second.join()
    print(f"{label}: expected 20000, got {counter}")


run_test("Without lock", unsafe_increment)
run_test("With lock   ", safe_increment)
