"""Two threads with different speeds: one prints months, one prints days.

Run: python 03_months_and_days.py
The months thread pauses 0.2 seconds per item and the days thread 0.3
seconds. Together they take about as long as the slower one alone.
The order of the lines can differ between runs.
"""

import threading
import time

MONTHS = ["January", "February", "March", "April", "May", "June"]
DAYS = ["Monday", "Tuesday", "Wednesday"]


def print_items(label, items, pause):
    for item in items:
        print(f"{label}: {item}")
        time.sleep(pause)


start_time = time.perf_counter()

months_thread = threading.Thread(target=print_items, args=("Month", MONTHS, 0.2))
days_thread = threading.Thread(target=print_items, args=("Day", DAYS, 0.3))

months_thread.start()
days_thread.start()

months_thread.join()
days_thread.join()

elapsed = time.perf_counter() - start_time
print(f"Months alone would need {len(MONTHS) * 0.2:.1f} s, days alone {len(DAYS) * 0.3:.1f} s.")
print(f"Running both together took about {elapsed:.1f} s.")
