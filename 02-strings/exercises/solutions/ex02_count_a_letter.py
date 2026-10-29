"""Count how many times the letter s appears in a sentence, ignoring case."""

sentence = "Sally sells sea shells by the sea shore"

# lower() first, so that the capital S in "Sally" is counted too.
count = sentence.lower().count("s")

print(f"The letter s appears {count} times.")
