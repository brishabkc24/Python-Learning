"""Split a sentence into words with re.split on non-word characters and count them."""

import re

sentence = "Hello, world! Regex is fun; is it not?"

parts = re.split(r"\W+", sentence)
words = [part for part in parts if part]     # drop the empty string at the end

print(words)
print(len(words), "words")
