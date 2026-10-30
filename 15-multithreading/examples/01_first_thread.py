"""Create a thread with threading.Thread, start it and wait for it.

Run: python 01_first_thread.py
Shows target and args, start() and join(), giving a thread a name,
and threading.current_thread().name.
"""

import threading


def greet(person, times):
    # current_thread() tells us which thread is running this code right now.
    thread_name = threading.current_thread().name
    for count in range(1, times + 1):
        print(f"[{thread_name}] Hello, {person}! ({count}/{times})")


print("Main thread is called:", threading.current_thread().name)

# target = the function to run, args = a tuple with its arguments.
worker = threading.Thread(target=greet, args=("Aarav", 3), name="GreeterThread")

print("Alive before start()?", worker.is_alive())
worker.start()      # the function starts running in a new thread
worker.join()       # wait here until that thread has finished
print("Alive after join()?", worker.is_alive())

# Without a name, Python numbers the thread and adds the function name.
unnamed = threading.Thread(target=greet, args=("Sita", 1))
unnamed.start()
unnamed.join()

print("Main thread finished.")
