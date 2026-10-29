"""
deque: a queue (first in, first out), a stack (last in, first out),
rotate, maxlen, and a timing test that shows why popping from the left
of a deque beats popping from the front of a list.

Run: python 06_deque_queue_stack.py
"""

import time
from collections import deque

# Queue: customers are served in the order they arrived.
counter_queue = deque()
for customer in ["Sita", "Aarav", "Bikash"]:
    counter_queue.append(customer)
    print("joined:", customer, "->", list(counter_queue))
while counter_queue:
    print("serving:", counter_queue.popleft(), "| waiting:", list(counter_queue))

print()
# Stack: the last action is the first one undone.
undo_stack = deque()
for action in ["type 'a'", "type 'b'", "delete 'b'"]:
    undo_stack.append(action)
print("actions:", list(undo_stack))
print("undo:", undo_stack.pop())
print("undo:", undo_stack.pop())
print("left:", list(undo_stack))

print()
# appendleft and rotate.
days = deque(["Mon", "Tue", "Wed", "Thu", "Fri"])
days.appendleft("Sun")
print("appendleft:", days)
days.rotate(2)
print("rotate(2):", days)
days.rotate(-2)
print("rotate(-2):", days)

# maxlen keeps only the newest items: a sliding window of readings.
readings = deque(maxlen=3)
for temperature in [20, 22, 25, 30, 28]:
    readings.append(temperature)
    print("last three readings:", list(readings), "| average:", round(sum(readings) / len(readings), 1))

print()
# Timing: 20,000 removals from the front. Your numbers will differ.
SIZE = 20_000
as_list = list(range(SIZE))
as_deque = deque(range(SIZE))

start = time.perf_counter()
while as_list:
    as_list.pop(0)          # shifts every remaining item left each time
list_time = time.perf_counter() - start

start = time.perf_counter()
while as_deque:
    as_deque.popleft()      # no shifting at all
deque_time = time.perf_counter() - start

print("list.pop(0) took", round(list_time * 1000, 1), "ms")
print("deque.popleft() took", round(deque_time * 1000, 1), "ms")
