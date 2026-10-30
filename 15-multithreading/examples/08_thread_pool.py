"""ThreadPoolExecutor: let a pool of worker threads run tasks for you.

Run: python 08_thread_pool.py
submit() hands one task to the pool and returns a Future; its result()
method waits for the answer. map() applies a function to every item
and gives the results back in the original order.
"""

import time
from concurrent.futures import ThreadPoolExecutor


def fetch_page(site):
    # Pretend to download a web page; the sleep stands for network waiting.
    time.sleep(0.3)
    return f"{site}: 200 OK"


def square(number):
    time.sleep(0.1)
    return number * number


start_time = time.perf_counter()

# max_workers is how many threads the pool keeps. The with statement
# waits for every task to finish before the pool is closed.
with ThreadPoolExecutor(max_workers=3) as pool:
    print("--- submit() ---")
    future_one = pool.submit(fetch_page, "example.com")
    future_two = pool.submit(fetch_page, "example.org")
    print("Result 1:", future_one.result())
    print("Result 2:", future_two.result())

    print("--- map() ---")
    numbers = [1, 2, 3, 4, 5, 6]
    for number, result in zip(numbers, pool.map(square, numbers)):
        print(f"{number} squared is {result}")

elapsed = time.perf_counter() - start_time
print(f"All tasks done in about {elapsed:.1f} s")
