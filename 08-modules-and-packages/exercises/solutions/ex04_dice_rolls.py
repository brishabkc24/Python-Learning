"""Exercise 4: roll a die 20 times with a fixed seed, count the sixes and show how often each face came up."""

import random

random.seed(7)

rolls = []
for _ in range(20):
    rolls.append(random.randint(1, 6))

print("Rolls:", rolls)
print("Sixes:", rolls.count(6))

for face in range(1, 7):
    print("Face", face, "->", rolls.count(face))
