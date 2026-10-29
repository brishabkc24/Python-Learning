"""Tidy up messy user input: fix spacing and capitals, build a username
and an email address, and compare strings.

Run: python 06_clean_names.py
"""

# Data typed by people is rarely tidy. Each name below has a problem.
raw_names = ["  asha THAPA ", "ravi   shrestha", "MEERA karki  "]

for raw in raw_names:
    # strip() removes the spaces at the ends; split() then join() collapses
    # the repeated spaces in the middle; title() fixes the capitals.
    full_name = " ".join(raw.split()).title()

    # A username is the name without spaces, in lower case.
    username = full_name.replace(" ", "").lower()

    # Fictional addresses at example.com.
    email = username + "@example.com"

    print(f"Raw: '{raw}'")
    print(f"  Clean name: {full_name}")
    print(f"  Username:   {username}")
    print(f"  Email:      {email}")

print()

# Comparing strings. == checks that every character matches, including case.
print("'Asha' == 'asha':", "Asha" == "asha")
print("'Asha'.lower() == 'asha':", "Asha".lower() == "asha")

# < and > compare alphabetically, character by character. Capital letters
# come before lower-case letters, so compare in one case to be safe.
print("'apple' < 'banana':", "apple" < "banana")
print("'Zebra' < 'apple':", "Zebra" < "apple")
print("'zebra' < 'apple':", "zebra" < "apple")

# Repetition with * is handy for simple lines in text output.
print()
print("=" * 30)
print("Report complete")
print("=" * 30)
