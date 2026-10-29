"""Count the upper-case and lower-case letters in a sentence."""

sentence = "Hello World From Python"

upper_count = 0
lower_count = 0
for character in sentence:
    if character.isupper():
        upper_count += 1
    elif character.islower():
        lower_count += 1

print("Upper case:", upper_count)
print("Lower case:", lower_count)
