"""Print each letter of "abc" using iter() and next(), stopping on StopIteration."""

letters = iter("abc")

while True:
    try:
        letter = next(letters)
    except StopIteration:
        break
    print(letter)

print("done")
