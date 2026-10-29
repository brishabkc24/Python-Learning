"""Reverse strings in two ways and check whether words and phrases are
palindromes (read the same forwards and backwards).

Run: python 04_reverse_and_palindrome.py
"""

word = "python"

# Way 1: a slice with step -1 walks from the end to the start.
reversed_by_slice = word[::-1]
print("Reversed by slicing:", reversed_by_slice)

# Way 2: build the result one character at a time, putting each new
# character in front of what we have so far.
reversed_by_loop = ""
for character in word:
    reversed_by_loop = character + reversed_by_loop
print("Reversed by a loop: ", reversed_by_loop)

print()

# A palindrome equals its own reverse.
for candidate in ["level", "python", "madam", "noon"]:
    is_palindrome = candidate == candidate[::-1]
    print(f"{candidate}: palindrome = {is_palindrome}")

print()

# Phrases need cleaning first: ignore capitals and spaces.
phrase = "Never odd or even"
cleaned = phrase.lower().replace(" ", "")
print("Phrase:", phrase)
print("Cleaned:", cleaned)
print("Palindrome:", cleaned == cleaned[::-1])

# Reversing the order of the words is different from reversing the letters.
sentence = "Python is easy to learn"
words = sentence.split()
print()
print("Words reversed:", " ".join(words[::-1]))
