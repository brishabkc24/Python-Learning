"""Use while loops, break, continue and the else clause of a loop.

Run: python 02_while_break_continue.py
"""

# A while loop repeats as long as its condition is True. Something inside
# the loop must change the condition, or the loop never ends.
count = 1
while count <= 5:
    print("count is", count)
    count += 1
print("Loop finished, count is now", count)

print()

# Doubling until a limit is passed: the number of repeats is not known in
# advance, which is exactly when while is the right choice.
amount = 1000
years = 0
while amount < 2000:
    amount = amount * 1.07     # 7 percent growth per year
    years += 1
print(f"1000 doubles in {years} years at 7 percent (reaches {amount:.2f})")

print()

# break leaves the loop at once, even if the condition is still True.
for number in range(1, 100):
    if number * number > 50:
        print("First square above 50 is", number * number, "for number", number)
        break

# continue skips the rest of this round and starts the next one.
print("Odd numbers below 10:", end=" ")
for number in range(10):
    if number % 2 == 0:
        continue
    print(number, end=" ")
print()

print()

# A loop can have an else block. It runs only when the loop was NOT ended
# by break, which is useful for "searched everything and found nothing".
for number in [4, 9, 15, 22]:
    if number % 7 == 0:
        print("Found a multiple of 7:", number)
        break
else:
    print("No multiple of 7 in the list")

for number in [4, 9, 14, 22]:
    if number % 7 == 0:
        print("Found a multiple of 7:", number)
        break
else:
    print("No multiple of 7 in the list")

print()

# while True runs forever until a break. This is the usual shape for a
# program that keeps going until something specific happens.
total = 0
step = 0
while True:
    step += 1
    total += step
    if total > 20:
        break
print(f"Adding 1, 2, 3, ... passes 20 after {step} steps (total {total})")
