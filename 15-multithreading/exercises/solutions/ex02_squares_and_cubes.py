"""Run two threads at the same time: one prints the squares of 1 to 5, the other prints the cubes."""

import threading
import time


def print_squares():
    for number in range(1, 6):
        print(f"Square of {number} is {number ** 2}")
        time.sleep(0.1)


def print_cubes():
    for number in range(1, 6):
        print(f"Cube of {number} is {number ** 3}")
        time.sleep(0.1)


squares_thread = threading.Thread(target=print_squares)
cubes_thread = threading.Thread(target=print_cubes)

squares_thread.start()
cubes_thread.start()

squares_thread.join()
cubes_thread.join()

print("Finished")
