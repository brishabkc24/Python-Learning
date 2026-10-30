"""Time three simulated tasks run one after another and then run with threads, and print both durations."""

import threading
import time

TASKS = [("Backup", 0.3), ("Email", 0.5), ("Report", 0.2)]


def do_task(name, seconds):
    time.sleep(seconds)
    print(f"{name} done")


start_time = time.perf_counter()
for name, seconds in TASKS:
    do_task(name, seconds)
sequential_time = time.perf_counter() - start_time

start_time = time.perf_counter()
threads = [threading.Thread(target=do_task, args=(name, seconds)) for name, seconds in TASKS]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
threaded_time = time.perf_counter() - start_time

print(f"Sequential: {sequential_time:.1f} s")
print(f"Threads:    {threaded_time:.1f} s")
