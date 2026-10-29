"""Exercise 5: count the words in a sentence with a dictionary and find the most common one."""

sentence = "the cat and the dog and the bird"

counts = {}
for word in sentence.split():
    counts[word] = counts.get(word, 0) + 1

for word, count in counts.items():
    print(word + ":", count)

most_common = max(counts, key=counts.get)
print("Most common:", most_common)
