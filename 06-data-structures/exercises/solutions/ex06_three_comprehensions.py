"""Exercise 6: a list, a dictionary and a set built with comprehensions."""

odd_squares = [n * n for n in range(1, 16) if n % 2 == 1]
print("Odd squares:", odd_squares)

cubes = {n: n ** 3 for n in range(1, 6)}
print("Cubes:", cubes)

words = ["apple", "fig", "cherry", "kiwi", "plum"]
word_lengths = {len(word) for word in words}
print("Word lengths:", sorted(word_lengths))
