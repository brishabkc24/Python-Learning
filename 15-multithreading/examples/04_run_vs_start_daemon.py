"""run() versus start(), and daemon threads.

Run: python 04_run_vs_start_daemon.py
Part 1 shows that calling run() does not create a new thread.
Part 2 starts a daemon thread that would tick forever; the program
still ends when the main thread ends. About three ticks are printed.
"""

import threading
import time


def show_thread():
    print("Running inside:", threading.current_thread().name)


print("--- Part 1: run() versus start() ---")
# A Thread object can be started only once, so we make one object for
# each experiment.
first = threading.Thread(target=show_thread, name="WorkerThread")
first.run()         # just a normal function call, no new thread is made

second = threading.Thread(target=show_thread, name="WorkerThread")
second.start()      # now the function really runs in WorkerThread
second.join()


def tick_forever():
    while True:
        print("tick")
        time.sleep(0.25)


print("--- Part 2: a daemon thread ---")
# A daemon thread is a background helper. Python does not wait for it
# when the main thread finishes. Without daemon=True this program
# would never end, because tick_forever() never returns.
ticker = threading.Thread(target=tick_forever, daemon=True)
ticker.start()

time.sleep(0.6)     # the main thread does its own work for a while
print("Main thread is done; the daemon thread is dropped.")
