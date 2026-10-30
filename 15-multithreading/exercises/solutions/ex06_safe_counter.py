"""Write a Counter class whose increment method is protected by a Lock, and prove it with five threads of 1000 increments each."""

import threading
import time


class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            current = self.value
            time.sleep(0)       # invite other threads to interrupt here
            self.value = current + 1


def work(counter, times):
    for _ in range(times):
        counter.increment()


counter = Counter()
threads = [threading.Thread(target=work, args=(counter, 1000)) for _ in range(5)]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("Expected:", 5 * 1000)
print("Got:     ", counter.value)
