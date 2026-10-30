"""
Demonstrates validation with fullmatch(): phone numbers, email addresses,
dates in two formats and strong passwords. All sample values are
fictional.
Run: python 05_validation.py
"""

import re

PHONE = re.compile(r"^(98|97)\d{8}$")
EMAIL = re.compile(r"^[\w.]+@[\w.]+\.[a-z]{2,}$")
DATE_YMD = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DATE_DMY = re.compile(r"^\d{2}-\d{2}-\d{4}$")


def is_strong_password(password):
    """8 to 16 characters with an upper, a lower, a digit and a special one."""
    if not 8 <= len(password) <= 16:
        return False
    rules = [r"[A-Z]", r"[a-z]", r"\d", r"[!@#$%^&*]"]
    return all(re.search(rule, password) for rule in rules)


def report(label, pattern, values):
    print(label)
    for value in values:
        status = "valid" if pattern.fullmatch(value) else "invalid"
        print(f"  {value:<24} {status}")


report("Phone numbers (98 or 97, then 8 more digits):", PHONE,
       ["9800000001", "9712345678", "9600000001", "98000", "98000000012"])

report("Email addresses:", EMAIL,
       ["asha@example.com", "bibek.thapa@example.com", "no-at-sign.com", "a@b", "x@mail.example.org"])

report("Dates as YYYY-MM-DD:", DATE_YMD, ["2024-03-15", "15-03-2024", "2024-3-15"])
report("Dates as DD-MM-YYYY:", DATE_DMY, ["15-03-2024", "2024-03-15", "15/03/2024"])

print("Passwords (8-16 long, upper, lower, digit, special):")
for password in ["Password123!", "password123", "Short1!", "ALLUPPER123!", "Good@Pass2024"]:
    status = "strong" if is_strong_password(password) else "weak"
    print(f"  {password:<24} {status}")
