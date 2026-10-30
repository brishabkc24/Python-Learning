# Multithreading

A thread lets a program do more than one thing at a time. This topic shows how to start threads, wait for them, keep shared data safe with a lock, and when threads help (waiting) and when they do not (heavy calculation).

## What you will learn

- The difference between a process and a thread
- Why programs use threads: waiting on input and output, doing several things at once
- Creating threads with `threading.Thread`, `start()` and `join()`
- Thread names, `run()` versus `start()`, and daemon threads
- The thread life cycle
- Race conditions and how a `Lock` fixes them
- `ThreadPoolExecutor` for running many small tasks
- What the GIL is and why it matters

## 1. Process versus thread

A **process** is a running program with its own memory. When you start Python, the operating system creates a process. A **thread** is a path of execution inside a process. Every process has at least one thread, the **main thread**, and it can create more. Threads in one process share the same memory, so they can read and change the same variables.

An everyday analogy: a process is a kitchen, and threads are the cooks working in it. The cooks share the same fridge and counters.

| | Process | Thread |
|---|---|---|
| What it is | A running program | A unit of work inside a process |
| Memory | Own, separate memory | Shared with the other threads of the process |
| Creating one | Slow and heavy | Fast and light |
| Sharing data | Needs special tools (files, pipes, queues) | Just use the same variables |
| If one crashes | Other processes keep running | The whole process can go down |
| Python module | `multiprocessing` | `threading` |

```python
import threading

print("Current thread:", threading.current_thread().name)
print("Threads alive right now:", threading.active_count())
```

Output:

```
Current thread: MainThread
Threads alive right now: 1
```

## 2. Why use threads

Programs spend a lot of time **waiting**: for a web page to arrive, for a file to be read, for a user to type. While one thread waits, another thread can do useful work. Threads also let a program do several things at once, such as downloading three files together instead of one after another.

In this lesson `time.sleep()` stands for "waiting on something slow". The example below "downloads" three files. One after another takes 0.6 seconds; with threads it takes about 0.3 seconds, the time of the slowest file.

```python
import threading
import time


def download(file_name, seconds):
    time.sleep(seconds)     # pretend to wait for the network
    print(f"Finished {file_name}")


files = [("photo.jpg", 0.3), ("notes.txt", 0.1), ("song.mp3", 0.2)]

start_time = time.perf_counter()
for file_name, seconds in files:
    download(file_name, seconds)
print(f"One after another: {time.perf_counter() - start_time:.1f} s")

start_time = time.perf_counter()
threads = []
for file_name, seconds in files:
    thread = threading.Thread(target=download, args=(file_name, seconds))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print(f"With threads: {time.perf_counter() - start_time:.1f} s")
```

Output (in the threaded part, the files finish fastest first, so the order can differ from the list order):

```
Finished photo.jpg
Finished notes.txt
Finished song.mp3
One after another: 0.6 s
Finished notes.txt
Finished song.mp3
Finished photo.jpg
With threads: 0.3 s
```

## 3. Creating a thread: target, args, start() and join()

`threading.Thread(target=function, args=(...))` creates a thread object. `target` is the function the thread will run and `args` is a tuple of arguments for it. Nothing runs until you call `start()`. `join()` makes the calling thread wait until that thread has finished. Without `join()`, the main thread may print "finished" before the worker is done.

A thread object can be started only once. To run the same function again, create a new `Thread`.

```python
import threading


def greet(person, times):
    for count in range(1, times + 1):
        print(f"Hello, {person}! ({count}/{times})")


worker = threading.Thread(target=greet, args=("Aarav", 3))
print("Alive before start()?", worker.is_alive())
worker.start()      # the function begins running in a new thread
worker.join()       # wait until the thread has finished
print("Alive after join()?", worker.is_alive())
print("Main thread finished.")
```

Output:

```
Alive before start()? False
Hello, Aarav! (1/3)
Hello, Aarav! (2/3)
Hello, Aarav! (3/3)
Alive after join()? False
Main thread finished.
```

Note the trailing comma in `args=("Aarav", 3)`. With one argument you must still write a tuple: `args=("Aarav",)`.

## 4. Naming threads

Give a thread a name with `name=...`. Inside any function, `threading.current_thread().name` tells you which thread is running it. The main thread is called `MainThread`. Threads without a name get a number plus the function name, such as `Thread-1 (greet)`.

```python
import threading


def greet():
    print("Running in:", threading.current_thread().name)


print("Running in:", threading.current_thread().name)

named = threading.Thread(target=greet, name="GreeterThread")
named.start()
named.join()

unnamed = threading.Thread(target=greet)
unnamed.start()
unnamed.join()
```

Output:

```
Running in: MainThread
Running in: GreeterThread
Running in: Thread-1 (greet)
```

## 5. Several threads together

Start all the threads first, then join them all. If you start one, join it, and only then start the next, the threads run one after another and you gain nothing. Here two threads print even and odd numbers; the small sleep lets them take turns. The exact order of the lines can change from run to run.

```python
import threading
import time


def print_even(limit):
    for number in range(0, limit + 1, 2):
        print(f"Even: {number}")
        time.sleep(0.1)


def print_odd(limit):
    for number in range(1, limit + 1, 2):
        print(f"Odd:  {number}")
        time.sleep(0.1)


even_thread = threading.Thread(target=print_even, args=(6,))
odd_thread = threading.Thread(target=print_odd, args=(6,))

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()
print("Both threads finished.")
```

Output (order may vary between runs):

```
Even: 0
Odd:  1
Even: 2
Odd:  3
Even: 4
Odd:  5
Even: 6
Both threads finished.
```

See `examples/03_months_and_days.py` for the same idea with two threads that run at different speeds.

## 6. run() versus start()

Every thread has a `run()` method that calls the target function. `start()` creates a new thread and makes it call `run()`. If you call `run()` yourself, no new thread is created: the function simply runs in the current thread like any normal function call.

```python
import threading


def show_thread():
    print("Running inside:", threading.current_thread().name)


first = threading.Thread(target=show_thread, name="WorkerThread")
first.run()         # a normal call, still in the main thread

second = threading.Thread(target=show_thread, name="WorkerThread")
second.start()      # really runs in WorkerThread
second.join()
```

Output:

```
Running inside: MainThread
Running inside: WorkerThread
```

## 7. Daemon threads

By default Python waits for every thread to finish before the program ends. A **daemon thread** is a background helper that Python does not wait for: when the main thread ends, the daemon thread is dropped. Use it for things like a progress indicator or a clock that should stop when the program stops. Set `daemon=True` when creating the thread.

```python
import threading
import time


def tick_forever():
    while True:
        print("tick")
        time.sleep(0.25)


ticker = threading.Thread(target=tick_forever, daemon=True)
ticker.start()

time.sleep(0.6)     # the main thread works for a while
print("Main thread is done; the daemon thread is dropped.")
```

Output (about three ticks; the exact number depends on timing):

```
tick
tick
tick
Main thread is done; the daemon thread is dropped.
```

Without `daemon=True` this program would never end, because `tick_forever()` never returns.

## 8. The thread life cycle

A thread moves through a few states from creation to the end. You cannot see every state from Python, but `is_alive()` tells you whether a thread has been started and has not yet finished.

| State | Meaning | How it gets there |
|---|---|---|
| New | The `Thread` object exists but has not started | `threading.Thread(...)` |
| Runnable | Ready to run, waiting for its turn on the CPU | `start()` was called |
| Running | Its code is being executed right now | The operating system picked it |
| Waiting / Blocked | Paused until something happens | `time.sleep()`, waiting for a lock, `join()`, reading input |
| Terminated | The target function returned (or raised an error) | End of the function |

```python
import threading
import time


def short_task():
    time.sleep(0.2)     # waiting state


thread = threading.Thread(target=short_task)
print("New:        alive =", thread.is_alive())

thread.start()
print("Started:    alive =", thread.is_alive())

thread.join()
print("Terminated: alive =", thread.is_alive())
```

Output:

```
New:        alive = False
Started:    alive = True
Terminated: alive = False
```

## 9. Race conditions

A **race condition** happens when two threads change the same data at the same time and the result depends on who gets there first. Adding 1 to a counter is really three steps: read the value, add 1, write it back. If thread A reads 5, then thread B reads 5, both write 6, and one update is lost.

To make the problem visible, the code below splits the update into those three steps and calls `time.sleep(0)` between them. `time.sleep(0)` means "let other threads run now". Real programs get interrupted in the same way, just less predictably. Each thread adds 1 ten thousand times, so the correct answer is 20000. The printed result is wrong, and it changes from run to run.

```python
import threading
import time

counter = 0


def unsafe_increment(times):
    global counter
    for _ in range(times):
        current = counter       # read
        time.sleep(0)           # another thread may run here
        counter = current + 1   # write back; an update may be lost


first = threading.Thread(target=unsafe_increment, args=(10_000,))
second = threading.Thread(target=unsafe_increment, args=(10_000,))
first.start()
second.start()
first.join()
second.join()
print("Expected 20000, got", counter)
```

Output (the number differs on every run):

```
Expected 20000, got 10068
```

On modern Python a plain `counter += 1` inside a loop often survives, because the interpreter only switches threads at certain points. Never rely on that. Any shared data that is read and then written needs a lock.

## 10. Lock and the with statement

A `threading.Lock` is like the key to a single-person room. A thread takes the key with `acquire()`, works, and gives it back with `release()`. While one thread holds the key, every other thread that asks for it waits. The `with lock:` statement takes the key and always gives it back, even if an error happens inside the block, so prefer it over calling `acquire()` and `release()` yourself.

```python
import threading
import time

counter = 0
lock = threading.Lock()


def safe_increment(times):
    global counter
    for _ in range(times):
        with lock:                  # only one thread at a time in here
            current = counter
            time.sleep(0)
            counter = current + 1


first = threading.Thread(target=safe_increment, args=(10_000,))
second = threading.Thread(target=safe_increment, args=(10_000,))
first.start()
second.start()
first.join()
second.join()
print("Expected 20000, got", counter)
```

Output:

```
Expected 20000, got 20000
```

Keep the locked block as short as possible. Code inside it runs one thread at a time, so a long locked block slows everything down.

## 11. A bank account with and without a lock

The same mistake with money. Two people withdraw 80 from an account holding 100. Without a lock both threads pass the `if self.balance >= amount` check before either one subtracts, and the balance ends at -60. With a lock the check and the subtraction happen together, so the second withdrawal is refused.

```python
import threading
import time


class BankAccount:
    def __init__(self, balance, use_lock):
        self.balance = balance
        self.use_lock = use_lock
        self.lock = threading.Lock()

    def withdraw(self, amount):
        if self.use_lock:
            with self.lock:
                self._do_withdraw(amount)
        else:
            self._do_withdraw(amount)

    def _do_withdraw(self, amount):
        name = threading.current_thread().name
        if self.balance >= amount:
            time.sleep(0.1)     # the bank "processes" the request
            self.balance -= amount
            print(f"{name}: withdrew {amount}, balance is now {self.balance}")
        else:
            print(f"{name}: not enough money for {amount}, balance is {self.balance}")


def try_both(account):
    thread_a = threading.Thread(target=account.withdraw, args=(80,), name="Aarav")
    thread_b = threading.Thread(target=account.withdraw, args=(80,), name="Sita")
    thread_a.start()
    thread_b.start()
    thread_a.join()
    thread_b.join()
    print("Final balance:", account.balance)


print("--- Without a lock ---")
try_both(BankAccount(100, use_lock=False))
print("--- With a lock ---")
try_both(BankAccount(100, use_lock=True))
```

Output:

```
--- Without a lock ---
Aarav: withdrew 80, balance is now 20
Sita: withdrew 80, balance is now -60
Final balance: -60
--- With a lock ---
Aarav: withdrew 80, balance is now 20
Sita: not enough money for 80, balance is 20
Final balance: 20
```

## 12. ThreadPoolExecutor

Creating a thread for every small task is tedious. A **thread pool** keeps a fixed number of worker threads and hands them tasks. `ThreadPoolExecutor` from `concurrent.futures` does this. `submit(function, arguments)` queues one task and returns a **Future**, an object whose `result()` method waits for the answer. `map(function, items)` runs the function on every item and returns the results in the original order. The `with` statement waits for all tasks before the pool closes.

```python
import time
from concurrent.futures import ThreadPoolExecutor


def fetch_page(site):
    time.sleep(0.3)
    return f"{site}: 200 OK"


def square(number):
    time.sleep(0.1)
    return number * number


start_time = time.perf_counter()
with ThreadPoolExecutor(max_workers=3) as pool:
    future_one = pool.submit(fetch_page, "example.com")
    future_two = pool.submit(fetch_page, "example.org")
    print(future_one.result())
    print(future_two.result())

    for number, result in zip([1, 2, 3, 4, 5, 6], pool.map(square, [1, 2, 3, 4, 5, 6])):
        print(f"{number} squared is {result}")

print(f"All tasks done in about {time.perf_counter() - start_time:.1f} s")
```

Output:

```
example.com: 200 OK
example.org: 200 OK
1 squared is 1
2 squared is 4
3 squared is 9
4 squared is 16
5 squared is 25
6 squared is 36
All tasks done in about 0.5 s
```

## 13. The GIL in one paragraph

The standard Python interpreter has a **Global Interpreter Lock (GIL)**: a lock that lets only one thread run Python code at any moment. Threads still switch quickly, and a thread that is waiting (for the network, a file, or `time.sleep()`) gives the lock to another thread. So threads are a good fit for programs that wait a lot. They do not make heavy calculation faster, because only one thread computes at a time. For number crunching on several CPU cores, use the `multiprocessing` module, which runs separate processes, each with its own interpreter and its own GIL.

```python
import threading
import time


def count_to(limit):
    total = 0
    for number in range(limit):
        total += number


start_time = time.perf_counter()
count_to(5_000_000)
count_to(5_000_000)
print(f"Two calls, one thread: {time.perf_counter() - start_time:.1f} s")

start_time = time.perf_counter()
first = threading.Thread(target=count_to, args=(5_000_000,))
second = threading.Thread(target=count_to, args=(5_000_000,))
first.start()
second.start()
first.join()
second.join()
print(f"Two calls, two threads: {time.perf_counter() - start_time:.1f} s")
```

Output (the numbers depend on your computer, but the two lines are about equal):

```
Two calls, one thread: 0.6 s
Two calls, two threads: 0.6 s
```

## Common mistakes

- Forgetting `start()` and calling `run()` instead -> `run()` runs the function in the current thread; call `start()` to get a new thread.
- Writing `args=("Aarav")` for a single argument -> that is just a string; write `args=("Aarav",)` with the comma so it is a tuple.
- Starting a thread and joining it before starting the next one -> start all threads first, then join them all, or they run one after another.
- Changing shared data from several threads without a lock -> wrap the read-and-write in `with lock:`.
- Expecting lines to print in a fixed order -> the operating system decides which thread runs when; design the program so the order does not matter, or use `join()` to wait.
- Using threads to speed up heavy calculation -> the GIL allows one running thread at a time; use `multiprocessing` for that.

## Summary

- A process has its own memory; threads share the memory of their process.
- `threading.Thread(target=f, args=(...))`, then `start()` to run it and `join()` to wait for it.
- `threading.current_thread().name` tells you which thread is running; name threads with `name=`.
- `run()` is a plain function call; only `start()` creates a new thread.
- Daemon threads are dropped when the main thread ends.
- A race condition is a lost or wrong update when threads change shared data together; a `Lock` with `with lock:` fixes it.
- `ThreadPoolExecutor` runs many tasks on a few worker threads with `submit()` and `map()`.
- Because of the GIL, threads help with waiting, not with heavy computation.

## Exercises

Practice what you learned in [exercises/README.md](exercises/README.md).

---

[Previous: Regular Expressions](../14-regular-expressions/README.md) | [Next: Network Programming](../16-network-programming/README.md) | [Home](../README.md)
