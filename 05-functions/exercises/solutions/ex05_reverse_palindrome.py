"""Exercise 5: reverse a string with a loop and use it to detect palindromes."""


def reverse_text(text):
    reversed_text = ""
    for letter in text:
        reversed_text = letter + reversed_text
    return reversed_text


def is_palindrome(text):
    lowered = text.lower()
    return lowered == reverse_text(lowered)


print("reverse_text('python') =", reverse_text("python"))
print("is_palindrome('Level') =", is_palindrome("Level"))
print("is_palindrome('python') =", is_palindrome("python"))
