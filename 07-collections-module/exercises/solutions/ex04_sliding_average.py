"""Exercise 4: average of the last three readings using a deque with maxlen=3."""

from collections import deque

readings = [20, 22, 25, 30, 28, 24]
last_three = deque(maxlen=3)

for reading in readings:
    last_three.append(reading)
    if len(last_three) == 3:
        average = round(sum(last_three) / 3, 2)
        print("After " + str(reading) + ": last three " + str(list(last_three)) + ", average", average)
