# Multithreading: Exercises

Solutions are in the [solutions](solutions/) folder. Try each exercise yourself before looking. Where threads print at the same time, the order of your output may differ from the example.

## 1. Greeting threads

**Three named threads.** Create three threads named `Worker-1`, `Worker-2` and `Worker-3`. Each one prints `Hello from <its own name>` using `threading.current_thread().name`. Start all three, wait for all three, then print `All done`.

Example:

```
Hello from Worker-1
Hello from Worker-2
Hello from Worker-3
All done
```

## 2. Squares and cubes

**Two threads, two tables.** Write one function that prints the squares of 1 to 5 and another that prints the cubes of 1 to 5, each sleeping 0.1 seconds between numbers. Run them in two threads at the same time and print `Finished` when both are done.

Example (order may vary):

```
Square of 1 is 1
Cube of 1 is 1
Square of 2 is 4
Cube of 2 is 8
...
Finished
```

## 3. Sequential versus threads

**Measure the gain.** Three tasks take 0.3, 0.5 and 0.2 seconds (use `time.sleep()`). Run them one after another and measure the total time with `time.perf_counter()`. Then run them in three threads and measure again. Print both times rounded to one decimal place.

Example:

```
Backup done
Email done
Report done
Report done
Backup done
Email done
Sequential: 1.0 s
Threads:    0.5 s
```

## 4. Daemon progress indicator

**A background message.** Start a daemon thread that prints `working...` every 0.2 seconds forever. In the main thread, "process" three items, sleeping 0.3 seconds for each and printing `Processed item N`. Finish with `Main thread finished`. The program must end on its own even though the daemon thread never returns.

Example (the number of `working...` lines may vary):

```
working...
working...
Processed item 1
working...
Processed item 2
working...
working...
Processed item 3
Main thread finished
```

## 5. Thread pool

**map and submit.** Using `ThreadPoolExecutor` with two workers, use `map()` to get the length of every word in `["python", "thread", "lock", "executor", "pool"]` and print `word -> length` for each. Then use `submit()` twice to add up two lists of marks and print both totals.

Example:

```
python -> 6
thread -> 6
lock -> 4
executor -> 8
pool -> 4
Total maths marks: 322
Total science marks: 315
```

## 6. Safe counter class

**A Counter with a Lock.** Write a `Counter` class with a `value` attribute and an `increment()` method protected by a `threading.Lock`. Start five threads that each call `increment()` 1000 times. Print the expected value and the real value; they must both be 5000. Add `time.sleep(0)` between reading and writing the value to prove the lock is doing its job.

Example:

```
Expected: 5000
Got:      5000
```

## 7. Ticket booking

**Only three seats.** A `TicketCounter` class starts with 3 seats. Its `book(customer)` method checks that a seat is free, sleeps 0.05 seconds (printing the ticket), reduces the seat count and prints a confirmation; if no seat is free it prints `sorry, sold out`. Five customer threads call `book()` at the same time. Use a lock so that exactly three bookings succeed and the final seat count is 0, never negative.

Example (order may vary):

```
Aarav: booked, seats left: 2
Sita: booked, seats left: 1
Bikash: booked, seats left: 0
Priya: sorry, sold out
Rohan: sorry, sold out
Seats left at the end: 0
```
