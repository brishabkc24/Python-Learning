"""Reverse the letters of every word in a sentence, keeping the word order."""

sentence = "Python is fun"

# Build the answer one word at a time, adding a space after each word.
result = ""
for word in sentence.split():
    result = result + word[::-1] + " "

# strip() removes the extra space left after the last word.
print(result.strip())
