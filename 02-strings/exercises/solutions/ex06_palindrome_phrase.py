"""Ask for a phrase and report whether it is a palindrome, ignoring case and spaces."""

phrase = input("Enter a phrase: ")

cleaned = phrase.lower().replace(" ", "")
is_palindrome = cleaned == cleaned[::-1]

print("Palindrome:", is_palindrome)
