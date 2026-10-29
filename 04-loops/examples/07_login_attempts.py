"""A login prompt that allows at most three attempts.

Run: python 07_login_attempts.py

Sample session:
    Username: asha
    Password: wrong
    Wrong username or password. 2 attempt(s) left.
    Username: asha
    Password: password123
    Welcome, asha!
"""

# Fictional credentials. A real program would never keep a password in
# the code; this is only to practise the loop.
CORRECT_USERNAME = "asha"
CORRECT_PASSWORD = "password123"
MAX_ATTEMPTS = 3

attempts_used = 0
logged_in = False

# Keep asking while attempts remain and nobody has logged in yet.
while attempts_used < MAX_ATTEMPTS and not logged_in:
    username = input("Username: ")
    password = input("Password: ")
    attempts_used += 1

    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        logged_in = True
    else:
        attempts_left = MAX_ATTEMPTS - attempts_used
        print(f"Wrong username or password. {attempts_left} attempt(s) left.")

if logged_in:
    print(f"Welcome, {username}!")
else:
    print("Too many failed attempts. Account locked.")
